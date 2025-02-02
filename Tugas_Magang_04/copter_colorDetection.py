from pymavlink import mavutil
import time
import threading
import math
import cv2
import numpy as np

string_koneksi1 = 'udp:127.0.0.1:14550'
konek = mavutil.mavlink_connection(string_koneksi1)
konek.wait_heartbeat()
print(f"Koneksi tersambung dari sistem: {konek.target_system} dan komponen: {konek.target_component}")

purple_detected = False

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

def return_to_launch():
    set_mode("RTL")
    print("Returning to launch position...")

def detect_purple():
    global purple_detected
    
    cap = cv2.VideoCapture(0)
    
    while not purple_detected:
        ret, frame = cap.read()
        if not ret:
            break
            
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_purple = np.array([140, 90, 120])
        upper_purple = np.array([155, 255, 255])
        
        purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)
        
        result = cv2.bitwise_and(frame, frame, mask=~purple_mask)
        combined = cv2.addWeighted(frame, 0.7, result, 0.3, 0)
        
        def detect_and_draw(purple_mask, text, color, combined_image):
            global purple_detected
            contours, _ = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:  
                    purple_detected = True
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(combined_image, (x, y), (x + w, y + h), color, 2)

                    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                    text_x = x + (w - text_size[0]) // 2
                    text_y = y - 10 if y - 10 > 20 else y + h + 20
                    cv2.putText(combined_image, 
                                text, 
                                (text_x, text_y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 
                                0.7, 
                                color, 
                                2)

        detect_and_draw(purple_mask, "FOUND PURPLE", (155, 0, 255), combined)
        

        cv2.imshow('Deteksi warna', combined)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def fly_hexagon():
    global purple_detected
    speed = 2
    segment_duration = 5
    angles = [0, 60, 120, 180, 240, 300]
    
    for angle in angles:
        if purple_detected:
            return True
            
        rad = math.radians(angle)
        vx = speed * math.cos(rad)
        vy = speed * math.sin(rad)
        set_velocity(vx, vy, 0)
        time.sleep(segment_duration)
        
    
    return False

def main():
    detection_thread = threading.Thread(target=detect_purple)
    detection_thread.daemon = True
    detection_thread.start()
    
    set_mode("GUIDED")
    time.sleep(1)
    
    print("Arming drone...")
    arm_drone()
    time.sleep(2)
    
    print("Taking off...")
    takeoff(3)
    time.sleep(10)
    
    print("Starting hexagon pattern...")
    while not purple_detected:
        should_rtl = fly_hexagon()
        if should_rtl:
            break
        print("Completed one hexagon, starting next...")
    
    if purple_detected:
        return_to_launch()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram Closed")
        set_velocity(0, 0, 0)
        cv2.destroyAllWindows()
        