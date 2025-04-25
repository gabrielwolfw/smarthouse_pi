#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include "gpio.h"

// Pins para prueba (ajusta según tus necesidades)
#define OUTPUT_PIN1 22  // GPIO 534 (22 + 512)
#define OUTPUT_PIN2 23  // GPIO 535 (23 + 512)
#define INPUT_PIN   24  // GPIO 536 (24 + 512)

volatile sig_atomic_t running = 1;

void signal_handler(int signum) {
    running = 0;
}

int main() {
    // Configurar manejador de señales para terminar limpiamente
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);

    printf("Iniciando prueba de GPIO...\n");

    // Configurar pines
    if (pinMode(OUTPUT_PIN1, OUTPUT) != GPIO_SUCCESS) {
        fprintf(stderr, "Error configurando OUTPUT_PIN1\n");
        return 1;
    }

    if (pinMode(OUTPUT_PIN2, OUTPUT) != GPIO_SUCCESS) {
        fprintf(stderr, "Error configurando OUTPUT_PIN2\n");
        return 1;
    }

    if (pinMode(INPUT_PIN, INPUT) != GPIO_SUCCESS) {
        fprintf(stderr, "Error configurando INPUT_PIN\n");
        return 1;
    }

    printf("Pines configurados exitosamente\n");

    // Prueba digitalWrite
    printf("Probando digitalWrite en pin %d...\n", OUTPUT_PIN1);
    digitalWrite(OUTPUT_PIN1, HIGH);
    sleep(1);
    digitalWrite(OUTPUT_PIN1, LOW);

    // Prueba blink
    printf("Iniciando blink en pin %d por 5 segundos...\n", OUTPUT_PIN2);
    blink(OUTPUT_PIN2, 1.0, 5);  // 1 Hz durante 5 segundos

    // Prueba digitalRead
    printf("Leyendo estado del pin %d: ", INPUT_PIN);
    int value = digitalRead(INPUT_PIN);
    if (value != GPIO_ERROR) {
        printf("%d\n", value);
    } else {
        printf("Error al leer\n");
    }

    return 0;
}