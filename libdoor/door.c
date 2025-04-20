#include "door.h"
#include <stdio.h>  // Para printf (depuración)

#define NUM_DOORS 4
static int doors[NUM_DOORS] = {0};

void door_init() {
    for (int i = 0; i < NUM_DOORS; i++) {
        doors[i] = 0; // Todas las puertas cerradas
    }
    printf("Sistema de puertas inicializado.\n");
}

void door_set_state(int door_id, int state) {
    if (door_id < 0 || door_id >= NUM_DOORS) {
        printf("ID de puerta inválido: %d\n", door_id);
        return;
    }
    doors[door_id] = state;
    printf("Puerta %d %s.\n", door_id, state ? "abierta" : "cerrada");
}

int door_get_state(int door_id) {
    if (door_id < 0 || door_id >= NUM_DOORS) {
        printf("ID de puerta inválido: %d\n", door_id);
        return -1;
    }
    return doors[door_id];
}