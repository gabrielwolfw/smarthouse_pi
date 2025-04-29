from ctypes import CDLL, c_int, c_float
from enum import IntEnum
import os
from pathlib import Path

class GPIOMode(IntEnum):
    INPUT = 0
    OUTPUT = 1

# Ubicaciones posibles de la biblioteca
_lib_locations = [
    "/usr/lib/libgpio.so.0",  # Ubicación instalada
    "/usr/lib/libgpio.so",
    str(Path(__file__).parent / "lib" / "libgpio.so"),  # Ubicación relativa al módulo
]

# Intentar cargar la biblioteca
gpio_lib = None
for _lib_path in _lib_locations:
    if os.path.exists(_lib_path):
        try:
            gpio_lib = CDLL(_lib_path)
            break
        except OSError:
            continue

if gpio_lib is None:
    raise RuntimeError("No se pudo encontrar o cargar libgpio.so")

# Configuración de funciones
gpio_lib.pinMode.argtypes = [c_int, c_int]
gpio_lib.pinMode.restype = c_int

gpio_lib.digitalWrite.argtypes = [c_int, c_int]
gpio_lib.digitalWrite.restype = c_int

gpio_lib.digitalRead.argtypes = [c_int]
gpio_lib.digitalRead.restype = c_int

gpio_lib.blink.argtypes = [c_int, c_float, c_int]
gpio_lib.blink.restype = c_int

# Funciones de conveniencia
def setup_pin(pin, mode):
    return gpio_lib.pinMode(pin, mode)

def write_pin(pin, value):
    return gpio_lib.digitalWrite(pin, value)

def read_pin(pin):
    return gpio_lib.digitalRead(pin)

def blink_pin(pin, freq, duration):
    return gpio_lib.blink(pin, freq, duration)