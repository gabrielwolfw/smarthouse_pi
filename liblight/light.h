#ifndef LIGHT_H
#define LIGHT_H

// Inicializa el sistema de luces
void light_init();

// Enciende una luz específica
void light_turn_on(int light_id);

// Apaga una luz específica
void light_turn_off(int light_id);

// Enciende todas las luces
void light_turn_all_on();

// Apaga todas las luces
void light_turn_all_off();

#endif // LIGHT_H