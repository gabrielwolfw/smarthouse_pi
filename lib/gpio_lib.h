#ifndef GPIO_LIB_H
#define GPIO_LIB_H

typedef enum {
    GPIO_INPUT = 0,
    GPIO_OUTPUT = 1
} gpio_mode_t;

// Exporta el pin y configura su modo (entrada o salida)
int pinMode(int pin, gpio_mode_t mode);

// Escribe un valor (0 o 1) en el pin (debe estar como salida)
int digitalWrite(int pin, int value);

// Lee el valor (0 o 1) de un pin digital (debe estar como entrada)
int digitalRead(int pin);

// Hace parpadear (blink) un pin a una frecuencia (Hz) y duración (segundos)
int blink(int pin, float freq, int duration);

#endif // GPIO_LIB_H