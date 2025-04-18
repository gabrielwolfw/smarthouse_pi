from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import datetime
import random

app = Flask(__name__)
CORS(app)

# ----------------------------
# Detectar si estamos en Raspberry Pi
# ----------------------------
try:
    import RPi.GPIO as GPIO
    real_hardware = True
except (ImportError, RuntimeError):
    from mock_gpio import BCM, OUT, IN, HIGH, LOW, PUD_DOWN
    import mock_gpio as GPIO
    real_hardware = False
    print("[INFO] Usando mock_gpio para simulación")


# ----------------------------
# Configuración de pines (modo BCM)
# ----------------------------
light_pins = {
    'cuarto1': 17,
    'cuarto2': 18,
    'sala': 22,
    'comedor': 23,
    'cocina': 24
}

door_pins = {
    'delantera': 5,
    'trasera': 6,
    'cuarto1': 13,
    'cuarto2': 19
}

# ----------------------------
# Inicialización si hay hardware real
# ----------------------------
if real_hardware:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in light_pins.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in door_pins.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Simulación de estados persistentes
if not real_hardware:
    simulated_lights = {room: False for room in light_pins}
    simulated_doors = {name: False for name in door_pins}


# ----------------------------
# Rutas Flask
# ----------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/lights', methods=['GET', 'POST'])
def light_control():
    if request.method == 'POST':
        data = request.json
        room = data['room']
        state = data['state']
        if real_hardware and room in light_pins:
            GPIO.output(light_pins[room], GPIO.HIGH if state else GPIO.LOW)
        elif not real_hardware and room in simulated_lights:
            simulated_lights[room] = state
        return jsonify({'success': True})

    # Obtener estado actual
    if real_hardware:
        lights_state = {room: GPIO.input(pin) == GPIO.HIGH for room, pin in light_pins.items()}
    else:
        lights_state = simulated_lights
    return jsonify(lights_state)


@app.route('/api/doors', methods=['GET'])
def door_status():
    if real_hardware:
        doors_state = {name: GPIO.input(pin) == GPIO.HIGH for name, pin in door_pins.items()}
    else:
        # Simulación: estado aleatorio
        doors_state = {name: random.choice([True, False]) for name in door_pins}
    return jsonify(doors_state)

@app.route('/api/capture', methods=['GET'])
def capture():
    filename = f"static/capture_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    if real_hardware:
        os.system(f"fswebcam -r 640x480 --no-banner {filename}")
    else:
        # Simulación: usar una imagen genérica si no hay cámara
        filename = "static/placeholder.jpg"
    return jsonify({"image": filename})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    if real_hardware:
        GPIO.cleanup()
    return jsonify({"message": "GPIO cleaned up. Goodbye!"})

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        if real_hardware:
            GPIO.cleanup()

