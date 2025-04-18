# mock_gpio.py

BCM = "BCM"
OUT = "OUT"
IN = "IN"
HIGH = True
LOW = False
PUD_DOWN = "PUD_DOWN"

_pins = {}

def setmode(mode):
    print(f"[MOCK GPIO] setmode({mode})")

def setwarnings(flag):
    pass

def setup(pin, mode, pull_up_down=None):
    print(f"[MOCK GPIO] setup(pin={pin}, mode={mode}, pud={pull_up_down})")
    _pins[pin] = LOW

def output(pin, value):
    print(f"[MOCK GPIO] output(pin={pin}, value={value})")
    _pins[pin] = value

def input(pin):
    return _pins.get(pin, LOW)

def cleanup():
    print("[MOCK GPIO] cleanup()")
