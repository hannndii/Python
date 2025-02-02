from flask import Flask, jsonify, render_template
from pymavlink import mavutil
import time
import threading
import math

app = Flask(__name__)

# Connection setup
string_koneksi1 = 'tcp:127.0.0.1:5760'
konek = mavutil.mavlink_connection(string_koneksi1)
konek.wait_heartbeat()
print(f"Koneksi tersambung dari sistem: {konek.target_system} dan komponen: {konek.target_component}")

# Drone control functions
def set_mode(mode):
    if mode not in konek.mode_mapping():
        print(f'Mode {mode} tidak tersedia')
        return
    mode_id = konek.mode_mapping()[mode]
    konek.mav.set_mode_send(
        konek.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id)

def arm_drone():
    konek.mav.command_long_send(
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)
    
def takeoff(altitude):
    konek.mav.command_long_send(
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,
        0, 0, 0, 0, 0, 0, altitude)

def set_velocity(vx, vy, vz, yaw_rate=0):
    konek.mav.set_position_target_local_ned_send(
        0,
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111000111,
        0, 0, 0,
        vx, vy, vz,
        0, 0, 0,
        yaw_rate, 0)

def fly_hexagon():
    speed = 5  # m/s
    segment_duration = 5  # seconds
    angles = [0, 60, 120, 180, 240, 300]  # degrees for hexagon
    
    for angle in angles:
        rad = math.radians(angle)
        vx = speed * math.cos(rad)
        vy = speed * math.sin(rad)
        print(f"Flying at angle {angle} degrees")
        set_velocity(vx, vy, 0)
        time.sleep(segment_duration)

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_drone_data')
def get_drone_data():
    try:
        # Request data
        msg = konek.recv_match(type=['GLOBAL_POSITION_INT', 'VFR_HUD'], blocking=True, timeout=1)
        
        if msg is not None:
            data = {
                'status': 'Connected',
                'altitude': msg.relative_alt / 1000.0 if msg.get_type() == 'GLOBAL_POSITION_INT' else 0,
                'latitude': msg.lat / 1e7 if msg.get_type() == 'GLOBAL_POSITION_INT' else 0,
                'longitude': msg.lon / 1e7 if msg.get_type() == 'GLOBAL_POSITION_INT' else 0,
                'heading': msg.hdg / 100.0 if msg.get_type() == 'GLOBAL_POSITION_INT' else 0,
                'groundspeed': msg.groundspeed if msg.get_type() == 'VFR_HUD' else 0
            }
        else:
            data = {
                'status': 'No Data',
                'altitude': 0,
                'latitude': 0,
                'longitude': 0,
                'heading': 0,
                'groundspeed': 0
            }
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Control endpoints
@app.route('/arm')
def arm():
    try:
        set_mode("GUIDED")
        time.sleep(1)
        arm_drone()
        return jsonify({'status': 'success', 'message': 'Drone armed'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/takeoff/<int:altitude>')
def takeoff_command(altitude):
    try:
        takeoff(altitude)
        return jsonify({'status': 'success', 'message': f'Taking off to {altitude}m'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/start_hexagon')
def start_hexagon():
    try:
        # Start hexagon pattern in a separate thread
        thread = threading.Thread(target=fly_hexagon)
        thread.daemon = True
        thread.start()
        return jsonify({'status': 'success', 'message': 'Started hexagon pattern'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/stop')
def stop():
    try:
        set_velocity(0, 0, 0)
        return jsonify({'status': 'success', 'message': 'Stopped movement'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    try:
        # Run Flask app in a separate thread
        flask_thread = threading.Thread(target=lambda: app.run(debug=False, host='127.0.0.1', port=5000))
        flask_thread.daemon = True
        flask_thread.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna")
        set_velocity(0, 0, 0)