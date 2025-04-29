class MockGPIO:
    def __init__(self):
        self.BCM = "BCM"
        self.OUT = "OUT"
        self.IN = "IN"
        self.HIGH = True
        self.LOW = False
        self.PUD_DOWN = "PUD_DOWN"
        self._pins = {}
    
    def setmode(self, mode):
        print(f"[MOCK] Modo establecido: {mode}")
    
    def setwarnings(self, flag):
        pass
    
    def setup(self, pin, mode, pull_up_down=None):
        print(f"[MOCK] Configurando pin {pin} como {mode}")
        self._pins[pin] = self.LOW
    
    def output(self, pin, value):
        print(f"[MOCK] Escribiendo {value} en pin {pin}")
        self._pins[pin] = value
    
    def input(self, pin):
        return self._pins.get(pin, self.LOW)
    
    def cleanup(self):
        print("[MOCK] Limpieza de pines")
        self._pins.clear()