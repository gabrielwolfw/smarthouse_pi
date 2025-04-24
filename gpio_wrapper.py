from ctypes import CDLL, c_int, c_float, c_void_p, POINTER
from enum import IntEnum
import os
from pathlib import Path

class GPIOMode(IntEnum):
    INPUT = 0
    OUTPUT = 1

# Carga la biblioteca compartida
LIB_PATH = str(Path(__file__).parent / "lib" / "gpio_lib.so")

try:
    gpio_lib = CDLL(LIB_PATH)
    
    # Configuración de funciones
    gpio_lib.pinMode.argtypes = [c_int, c_int]
    gpio_lib.pinMode.restype = c_int
    
    gpio_lib.digitalWrite.argtypes = [c_int, c_int]
    gpio_lib.digitalWrite.restype = c_int
    
    gpio_lib.digitalRead.argtypes = [c_int]
    gpio_lib.digitalRead.restype = c_int
    
    gpio_lib.blink.argtypes = [c_int, c_float, c_int]
    gpio_lib.blink.restype = c_int

except Exception as e:
    print(f"Error cargando la biblioteca GPIO: {e}")
    raise

# Funciones de conveniencia
def setup_pin(pin, mode):
    return gpio_lib.pinMode(pin, mode)

def write_pin(pin, value):
    return gpio_lib.digitalWrite(pin, value)

def read_pin(pin):
    return gpio_lib.digitalRead(pin)

def blink_pin(pin, freq, duration):
    return gpio_lib.blink(pin, freq, duration)