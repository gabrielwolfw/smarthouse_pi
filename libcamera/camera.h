#ifndef CAMERA_H
#define CAMERA_H

// Inicializa la cámara
void camera_init();

// Toma una foto y la guarda en el sistema
void camera_take_photo(const char *filename);

#endif // CAMERA_H