#include "gpio_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>

#define SYSFS_GPIO_DIR "/sys/class/gpio"
#define BUFFER_MAX 64

static int write_sysfs(const char *path, const char *value) {
    int fd = open(path, O_WRONLY);
    if (fd < 0) return -1;
    int ret = write(fd, value, strlen(value));
    close(fd);
    return (ret < 0) ? -1 : 0;
}

int pinMode(int pin, gpio_mode_t mode) {
    char path[BUFFER_MAX];
    char buf[8];
    // Exportar el pin
    snprintf(path, BUFFER_MAX, SYSFS_GPIO_DIR "/export");
    snprintf(buf, sizeof(buf), "%d", pin);
    write_sysfs(path, buf); // Puede fallar si ya está exportado, pero no es crítico

    // Configurar dirección
    snprintf(path, BUFFER_MAX, SYSFS_GPIO_DIR "/gpio%d/direction", pin);
    return write_sysfs(path, (mode == GPIO_OUTPUT) ? "out" : "in");
}

int digitalWrite(int pin, int value) {
    char path[BUFFER_MAX];
    snprintf(path, BUFFER_MAX, SYSFS_GPIO_DIR "/gpio%d/value", pin);
    return write_sysfs(path, value ? "1" : "0");
}

int digitalRead(int pin) {
    char path[BUFFER_MAX], value_str[4];
    int fd;
    snprintf(path, BUFFER_MAX, SYSFS_GPIO_DIR "/gpio%d/value", pin);
    fd = open(path, O_RDONLY);
    if (fd < 0) return -1;
    int len = read(fd, value_str, 3);
    close(fd);
    if (len < 1) return -1;
    return (value_str[0] == '0') ? 0 : 1;
}

int blink(int pin, float freq, int duration) {
    int cycles = (int)(freq * duration);
    float delay = 0.5f / freq; // en segundos

    for (int i = 0; i < cycles; ++i) {
        digitalWrite(pin, 1);
        usleep((int)(delay * 1e6));
        digitalWrite(pin, 0);
        usleep((int)(delay * 1e6));
    }
    return 0;
}