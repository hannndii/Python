import numpy as np
import cv2 
# CAMERA VISION

def show_color_info(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  
        hsv_value = hsv[y, x]  
        print(f"HSV: {hsv_value}")
        
        hue = hsv_value[0]
        
        if 0 <= hue <= 10 or 170 <= hue <= 180:
            print("Warna yang terdeteksi: Merah")
        elif 100 <= hue <= 125:
            print("Warna yang terdeteksi: Biru")
        elif 140 <= hue <= 150:
            print("Warna yang terdeteksi: Ungu")
        else:
            print("Warna Tidak Teridentifikasi")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera Tidak Terbuka")
    exit()

cv2.namedWindow("Deteksi Warna")
cv2.setMouseCallback("Deteksi Warna", show_color_info)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Gagal Membaca Kamera")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2

    lower_blue = np.array([100, 150, 150])
    upper_blue = np.array([125, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    lower_purple = np.array([140, 90, 120])
    upper_purple = np.array([155, 255, 255])
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

    mask = mask_red | mask_blue | mask_purple
    result = cv2.bitwise_or(frame, frame, mask=mask)

    combined = cv2.addWeighted(frame, 0.7, result, 0.3, 0)

    def detect_and_draw(mask, text, color, combined_image):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(combined_image, (x, y), (x + w, y + h), color, 2)

                text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                text_x = x + (w - text_size[0]) // 2
                text_y = y - 10 if y - 10 > 20 else y + h + 20
                cv2.putText(combined_image, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    detect_and_draw(mask_red, "FOUND MERAH", (0, 0, 255), combined)

    detect_and_draw(mask_blue, "FOUND BLUE", (255, 0, 0), combined)

    detect_and_draw(mask_purple, "FOUND PURPLE", (255, 0, 255), combined)

    cv2.imshow("Deteksi Warna", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

