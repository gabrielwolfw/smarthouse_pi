#ifndef DOOR_H
#define DOOR_H

// Inicializa el sistema de puertas
void door_init();

// Actualiza el estado de una puerta (abierta/cerrada)
void door_set_state(int door_id, int state);

// Obtiene el estado de una puerta
int door_get_state(int door_id);

#endif // DOOR_H