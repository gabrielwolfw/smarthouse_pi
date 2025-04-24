#ifndef GPIO_H
#define GPIO_H

// Modos de operación
#define INPUT  0
#define OUTPUT 1

// Valores
#define LOW  0
#define HIGH 1

// Offset para los GPIOs de Raspberry Pi 4
#define GPIO_OFFSET 512

// Códigos de error
#define GPIO_SUCCESS 0
#define GPIO_ERROR -1

// Funciones principales
/**
 * @brief Configura el modo de un pin GPIO
 * @param pin Número del pin (sin offset)
 * @param mode INPUT o OUTPUT
 * @return GPIO_SUCCESS en éxito, GPIO_ERROR en error
 */
int pinMode(int pin, int mode);

/**
 * @brief Escribe un valor digital en un pin
 * @param pin Número del pin (sin offset)
 * @param value HIGH o LOW
 * @return GPIO_SUCCESS en éxito, GPIO_ERROR en error
 */
int digitalWrite(int pin, int value);

/**
 * @brief Lee el valor de un pin digital
 * @param pin Número del pin (sin offset)
 * @return 1 (HIGH) o 0 (LOW), -1 en caso de error
 */
int digitalRead(int pin);

/**
 * @brief Hace parpadear un pin a una frecuencia específica
 * @param pin Número del pin (sin offset)
 * @param freq Frecuencia en Hz
 * @param duration Duración en segundos
 * @return GPIO_SUCCESS en éxito, GPIO_ERROR en error
 */
int blink(int pin, float freq, int duration);

#endif // GPIO_H