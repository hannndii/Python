from pymavlink import mavutil
import time
import threading
import math

# Connection setup
string_koneksi1 = 'udp:127.0.0.1:14551'
konek = mavutil.mavlink_connection(string_koneksi1)
konek.wait_heartbeat()
print(f"Koneksi tersambung dari sistem: {konek.target_system} dan komponen: {konek.target_component}")

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
    # Hexagon parameters
    speed = 5  # m/s
    segment_duration = 5  # seconds
    angles = [0, 60, 120, 180, 240, 300]  # degrees for hexagon
    
    for angle in angles:
        # Convert angle to radians
        rad = math.radians(angle)
        
        # Calculate velocity components
        vx = speed * math.cos(rad)
        vy = speed * math.sin(rad)
        
        # Fly straight for 5 seconds
        print(f"Flying at angle {angle} degrees")
        set_velocity(vx, vy, 0)
        time.sleep(segment_duration)
        

def main():
    # Set to GUIDED mode
    set_mode("GUIDED")
    time.sleep(1)
    
    # Arm the drone
    print("Arming drone...")
    arm_drone()
    time.sleep(2)
    
    # Take off to 10 feet (≈ 3 meters)
    print("Taking off...")
    takeoff(3)
    time.sleep(10)  # Wait for altitude
    
    # Start hexagon pattern
    print("Starting hexagon pattern...")
    while True:
        fly_hexagon()
        print("Completed one hexagon, starting next...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna")
        set_velocity(0, 0, 0)  # Stop movement