from pymavlink import mavutil
import time
import threading

string_koneksi1 = 'udp:127.0.0.1:14551'
string_koneksi2 = 'tcp:127.0.0.1:5763'
konek = mavutil.mavlink_connection(string_koneksi1)
konek.wait_heartbeat()
print(f"koneksi tersambung dari sistem: {konek.target_system} dan komponen: {konek.target_component}")

def arm_drone():
    konek.arducopter_arm()
    konek.motors_armed_wait()
    print("ARMING")

def takeoff(altitude):
    altitude = float(altitude)

    print("takeoff")
    konek.mav.command_long_send(
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0, 0, 0, 0, 0, 0, 0, altitude
    )

def gerak(x, y, z):
    konek.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        10, 
        konek.target_system, 
        konek.target_component, 
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
        int(0b110111000111), 
        5, 1, 0, 
        x, y, z, 
        5, 1, 0, 
        0, 0
    ))
    print(f"Mengirim perintah gerakan sebesar x: {x} y: {y} z: {z} selama 5 detik . . . ")

def data_sensor():
    i = 0
    while True:
        i = i + 1
        print(f"diterima data ketinggian :{i}")
        time.sleep(1)

data_thread = threading.Thread(target=data_sensor)
data_thread.start()

def main():
    print("kode kendali telah dijalankan...")
    
    arm_drone()
    time.sleep(3)
    
    takeoff(10)
    time.sleep(10)
    
    gerak(5, 0, 0)  # maju
    time.sleep(5)
    
    
if __name__ == "__main__":
    main()
