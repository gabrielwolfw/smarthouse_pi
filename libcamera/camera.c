#include "camera.h"
#include <stdio.h>
#include <stdlib.h>

void camera_init() {
    printf("Cámara inicializada.\n");
}

void camera_take_photo(const char *filename) {
    // Simulamos la captura de una foto con un comando del sistema
    char command[256];
    snprintf(command, sizeof(command), "fswebcam -r 640x480 --jpeg 85 %s", filename);
    int result = system(command);
    if (result == 0) {
        printf("Foto guardada en %s\n", filename);
    } else {
        printf("Error al tomar la foto.\n");
    }
}