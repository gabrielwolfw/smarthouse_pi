#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <errno.h>
#include <fcntl.h>
#include "gpio.h"

// Función auxiliar para exportar un GPIO
static int exportGPIO(int pin) {
    char buffer[64];
    int fd, len;
    
    fd = open("/sys/class/gpio/export", O_WRONLY);
    if (fd < 0) {
        fprintf(stderr, "Error al abrir export: %s\n", strerror(errno));
        return GPIO_ERROR;
    }
    
    len = snprintf(buffer, sizeof(buffer), "%d", pin + GPIO_OFFSET);
    if (write(fd, buffer, len) != len) {
        fprintf(stderr, "Error al exportar GPIO: %s\n", strerror(errno));
        close(fd);
        return GPIO_ERROR;
    }
    
    close(fd);
    // Esperar a que el sistema cree los archivos
    usleep(100000);
    return GPIO_SUCCESS;
}

// Función auxiliar para establecer la dirección
static int setDirection(int pin, const char *direction) {
    char path[128];
    int fd, len;
    
    snprintf(path, sizeof(path), "/sys/class/gpio/gpio%d/direction", pin + GPIO_OFFSET);
    fd = open(path, O_WRONLY);
    if (fd < 0) {
        if (errno == ENOENT) {
            if (exportGPIO(pin) == GPIO_SUCCESS) {
                // Intentar abrir nuevamente después de exportar
                fd = open(path, O_WRONLY);
            }
        }
        if (fd < 0) {
            fprintf(stderr, "Error al abrir direction: %s\n", strerror(errno));
            return GPIO_ERROR;
        }
    }
    
    len = strlen(direction);
    if (write(fd, direction, len) != len) {
        fprintf(stderr, "Error al establecer dirección: %s\n", strerror(errno));
        close(fd);
        return GPIO_ERROR;
    }
    
    close(fd);
    return GPIO_SUCCESS;
}

int pinMode(int pin, int mode) {
    const char *direction = (mode == INPUT) ? "in" : "out";
    return setDirection(pin, direction);
}

int digitalWrite(int pin, int value) {
    char path[128];
    int fd;
    
    snprintf(path, sizeof(path), "/sys/class/gpio/gpio%d/value", pin + GPIO_OFFSET);
    fd = open(path, O_WRONLY);
    if (fd < 0) {
        fprintf(stderr, "Error al abrir value para escritura: %s\n", strerror(errno));
        return GPIO_ERROR;
    }
    
    if (write(fd, value ? "1" : "0", 1) != 1) {
        fprintf(stderr, "Error al escribir valor: %s\n", strerror(errno));
        close(fd);
        return GPIO_ERROR;
    }
    
    close(fd);
    return GPIO_SUCCESS;
}

int digitalRead(int pin) {
    char path[128], value;
    int fd;
    
    snprintf(path, sizeof(path), "/sys/class/gpio/gpio%d/value", pin + GPIO_OFFSET);
    fd = open(path, O_RDONLY);
    if (fd < 0) {
        fprintf(stderr, "Error al abrir value para lectura: %s\n", strerror(errno));
        return GPIO_ERROR;
    }
    
    if (read(fd, &value, 1) != 1) {
        fprintf(stderr, "Error al leer valor: %s\n", strerror(errno));
        close(fd);
        return GPIO_ERROR;
    }
    
    close(fd);
    return (value == '1') ? HIGH : LOW;
}

int blink(int pin, float freq, int duration) {
    struct timespec delay;
    time_t end_time;
    float period_us;
    
    if (freq <= 0 || duration < 0) {
        return GPIO_ERROR;
    }
    
    period_us = (1000000.0f / freq) / 2.0f;
    delay.tv_sec = (time_t)(period_us / 1000000);
    delay.tv_nsec = (long)((period_us - (delay.tv_sec * 1000000)) * 1000);
    
    end_time = time(NULL) + duration;
    
    while (time(NULL) < end_time) {
        if (digitalWrite(pin, HIGH) != GPIO_SUCCESS) return GPIO_ERROR;
        nanosleep(&delay, NULL);
        if (digitalWrite(pin, LOW) != GPIO_SUCCESS) return GPIO_ERROR;
        nanosleep(&delay, NULL);
    }
    
    return GPIO_SUCCESS;
}