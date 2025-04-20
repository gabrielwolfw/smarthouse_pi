#include "light.h"
#include <stdio.h>  // Para printf (depuración)

// Simulamos las luces con un array
#define NUM_LIGHTS 5
static int lights[NUM_LIGHTS] = {0};

void light_init() {
    for (int i = 0; i < NUM_LIGHTS; i++) {
        lights[i] = 0; // Todas las luces apagadas
    }
    printf("Sistema de luces inicializado.\n");
}

void light_turn_on(int light_id) {
    if (light_id < 0 || light_id >= NUM_LIGHTS) {
        printf("ID de luz inválido: %d\n", light_id);
        return;
    }
    lights[light_id] = 1;
    printf("Luz %d encendida.\n", light_id);
}

void light_turn_off(int light_id) {
    if (light_id < 0 || light_id >= NUM_LIGHTS) {
        printf("ID de luz inválido: %d\n", light_id);
        return;
    }
    lights[light_id] = 0;
    printf("Luz %d apagada.\n", light_id);
}

void light_turn_all_on() {
    for (int i = 0; i < NUM_LIGHTS; i++) {
        lights[i] = 1;
    }
    printf("Todas las luces encendidas.\n");
}

void light_turn_all_off() {
    for (int i = 0; i < NUM_LIGHTS; i++) {
        lights[i] = 0;
    }
    printf("Todas las luces apagadas.\n");
}