from flask import Flask, jsonify, request
from pymavlink import mavutil
import time
import threading

app = Flask(__name__)

# Connection setup
string_koneksi1 = 'udp:127.0.0.1:14551'
konek = mavutil.mavlink_connection(string_koneksi1)
konek.wait_heartbeat()
print(f"Koneksi tersambung dari sistem: {konek.target_system} dan komponen: {konek.target_component}")

# Global variable untuk status
drone_status = {
    'armed': False,
    'mode': '',
    'altitude': 0,
    'latitude': 0,
    'longitude': 0,
    'heading': 0,
    'groundspeed': 0
}

def update_status():
    while True:
        msg = konek.recv_match(type=['GLOBAL_POSITION_INT', 'HEARTBEAT', 'VFR_HUD'], blocking=True)
        if msg is not None:
            if msg.get_type() == 'HEARTBEAT':
                drone_status['armed'] = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
                drone_status['mode'] = mavutil.mode_string_v10(msg)
            elif msg.get_type() == 'GLOBAL_POSITION_INT':
                drone_status['altitude'] = msg.relative_alt / 1000.0
                drone_status['latitude'] = msg.lat / 1e7
                drone_status['longitude'] = msg.lon / 1e7
                drone_status['heading'] = msg.hdg / 100.0
            elif msg.get_type() == 'VFR_HUD':
                drone_status['groundspeed'] = msg.groundspeed
        time.sleep(0.1)

@app.route('/get_drone_data')
def get_drone_data():
    return jsonify(drone_status)

@app.route('/set_mode/<mode>', methods=['POST'])
def change_mode(mode):
    try:
        mode_id = konek.mode_mapping()[mode]
        konek.set_mode(mode_id)
        return jsonify({'success': True, 'message': f'Mode changed to {mode}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Start the status update thread
status_thread = threading.Thread(target=update_status, daemon=True)
status_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
