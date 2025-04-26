from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
import os
import datetime
from auth import setup_auth_routes, login_required

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or "dev-key-insecure"
app.config['SESSION_COOKIE_SECURE'] = False  # True en producción con HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Configurar rutas de autenticación
setup_auth_routes(app)
CORS(app)

# ===== Configuración de GPIO =====
light_pins = {
    'cuarto1': 17,
    'cuarto2': 27,
    'sala': 22,
    'comedor': 5,
    'cocina': 6
}

door_pins = {
    'delantera': 26,
    'trasera': 23,
    'cuarto1': 24,
    'cuarto2': 25
}

# Intenta cargar la biblioteca personalizada
try:
    from gpio_wrapper import setup_pin, write_pin, read_pin, GPIOMode
    
    # Inicialización de pines
    for pin in light_pins.values():
        setup_pin(pin, GPIOMode.OUTPUT)
        write_pin(pin, 0)  # Apagar todos al inicio
    
    for pin in door_pins.values():
        setup_pin(pin, GPIOMode.INPUT)
    
    real_hardware = True
    print("[INFO] Usando biblioteca personalizada de GPIO")

except Exception as e:
    print(f"[INFO] Usando modo simulación: {e}")
    from mock_gpio import MockGPIO
    GPIO = MockGPIO()
    real_hardware = False
    simulated_lights = {room: False for room in light_pins}
    simulated_doors = {door: False for door in door_pins}

# ===== Rutas de la API =====
@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/api/lights', methods=['GET', 'POST'])
@login_required
def light_control():
    if request.method == 'POST':
        data = request.json
        room = data['room']
        state = data['state']
        if real_hardware:
            write_pin(light_pins[room], state)
        else:
            simulated_lights[room] = state
        return jsonify({'success': True})

    if real_hardware:
        lights_state = {room: read_pin(pin) for room, pin in light_pins.items()}
    else:
        lights_state = simulated_lights
    return jsonify(lights_state)

@app.route('/api/doors', methods=['GET'])
@login_required
def door_status():
    if real_hardware:
        doors_state = {name: read_pin(pin) for name, pin in door_pins.items()}
    else:
        doors_state = simulated_doors
    return jsonify(doors_state)

@app.route('/api/toggle_door', methods=['POST'])
@login_required
def toggle_door():
    if not real_hardware:
        data = request.json
        name = data['name']
        state = data['state']
        simulated_doors[name] = state
    return jsonify({'success': True})

@app.route('/api/capture', methods=['GET'])
@login_required
def capture():
    filename = f"static/capture_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    if real_hardware:
        os.system(f"fswebcam -r 640x480 --no-banner {filename}")
    else:
        filename = "static/placeholder.jpg"
    return jsonify({"image": filename})

@app.route('/shutdown', methods=['POST'])
@login_required
def shutdown():
    if real_hardware:
        print("[INFO] Limpieza de GPIO (personalizada)")
    return jsonify({"message": "Sistema apagado correctamente"})

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nServidor detenido")