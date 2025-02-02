from flask import Flask, jsonify, render_template
from flask_cors import CORS
from pymavlink import mavutil
import time
import threading
import math

app = Flask(__name__)
CORS(app)
app.template_folder = 'templates'  # Pastikan folder template terdeteksi

# Shared drone data
drone_data = {
    "altitude": 0,
    "speed": 0,
    "battery": 100,
    "mode": "DISCONNECTED",
    "position": {"lat": 0, "lon": 0},
    "heading": 0,
    "armed": False
}
data_lock = threading.Lock()

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/drone_data')
def get_drone_data():
    with data_lock:
        return jsonify(drone_data)

def mavlink_listener():
    global drone_data
    konek = mavutil.mavlink_connection('udp:127.0.0.1:14551')
    
    while True:
        try:
            msg = konek.recv_match()
            if not msg:
                continue
                
            with data_lock:
                if msg.get_type() == 'HEARTBEAT':
                    drone_data['armed'] = bool(msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
                    drone_data['mode'] = konek.flightmode if konek.flightmode else "UNKNOWN"
                    
                elif msg.get_type() == 'GLOBAL_POSITION_INT':
                    drone_data['altitude'] = msg.alt / 1000
                    drone_data['heading'] = msg.hdg / 100
                    
                elif msg.get_type() == 'VFR_HUD':
                    drone_data['speed'] = msg.groundspeed
                    
                elif msg.get_type() == 'BATTERY_STATUS':
                    drone_data['battery'] = msg.battery_remaining
                    
        except Exception as e:
            print(f"MAVLink error: {str(e)}")
            continue

if __name__ == '__main__':
    # Start MAVLink thread
    mav_thread = threading.Thread(target=mavlink_listener)
    mav_thread.daemon = True
    mav_thread.start()
    
    # Start Flask server
    print("Server running at http://127.0.0.1:5000")
    print("Tekan CTRL+C untuk berhenti")
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)