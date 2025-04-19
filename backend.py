from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
import os
import datetime
import random

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Reemplazar en producción
CORS(app)

# Usuario y contraseña (en producción usar base de datos y HTTPS)
users = {
    "admin": generate_password_hash("1234")
}

# Detección de hardware
try:
    import RPi.GPIO as GPIO
    real_hardware = True
except (ImportError, RuntimeError):
    from mock_gpio import BCM, OUT, IN, HIGH, LOW, PUD_DOWN
    import mock_gpio as GPIO
    real_hardware = False
    print("[INFO] Usando mock_gpio para simulación")

# Pines definidos
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

# Inicialización de pines
if real_hardware:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in light_pins.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in door_pins.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
else:
    simulated_lights = {room: False for room in light_pins}
    simulated_doors = {door: False for door in door_pins}

# Rutas
@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in users and check_password_hash(users[user], pwd):
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return "Credenciales incorrectas", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/api/lights', methods=['GET', 'POST'])
def light_control():
    if 'user' not in session:
        return jsonify({'error': 'No autorizado'}), 403

    if request.method == 'POST':
        data = request.json
        room = data['room']
        state = data['state']
        if real_hardware and room in light_pins:
            GPIO.output(light_pins[room], GPIO.HIGH if state else GPIO.LOW)
        elif not real_hardware and room in simulated_lights:
            simulated_lights[room] = state
        return jsonify({'success': True})

    if real_hardware:
        lights_state = {room: GPIO.input(pin) == GPIO.HIGH for room, pin in light_pins.items()}
    else:
        lights_state = simulated_lights
    return jsonify(lights_state)

@app.route('/api/doors', methods=['GET'])
def door_status():
    if 'user' not in session:
        return jsonify({'error': 'No autorizado'}), 403

    if real_hardware:
        doors_state = {name: GPIO.input(pin) == GPIO.HIGH for name, pin in door_pins.items()}
    else:
        doors_state = simulated_doors
    return jsonify(doors_state)

@app.route('/api/toggle_door', methods=['POST'])
def toggle_door():
    if 'user' not in session:
        return jsonify({'error': 'No autorizado'}), 403

    data = request.json
    name = data['name']
    state = data['state']
    if not real_hardware and name in simulated_doors:
        simulated_doors[name] = state
    return jsonify({'success': True})

@app.route('/api/capture', methods=['GET'])
def capture():
    if 'user' not in session:
        return jsonify({'error': 'No autorizado'}), 403

    filename = f"static/capture_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    if real_hardware:
        os.system(f"fswebcam -r 640x480 --no-banner {filename}")
    else:
        filename = "static/placeholder.jpg"
    return jsonify({"image": filename})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    if real_hardware:
        GPIO.cleanup()
    return jsonify({"message": "GPIO cleaned up. Goodbye!"})

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        if real_hardware:
            GPIO.cleanup()
