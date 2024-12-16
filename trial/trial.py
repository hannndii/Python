import numpy as np
import cv2

# =====================================================================
# Algoritma
# 1. Membuka kamera (0 biasanya adalah default untuk kamera laptop)
# 2. Memeriksa apakah kamera berhasil diakses
# 3. Gunakan perulangan untuk membaca frame dari kamera
# 4. Konversi frame ke HSV
# 5. Definisikan rentang warna untuk deteksi
# 6. Gabungkan semua masker
# 7. Terapkan masker ke frame asli
# 8. Tampilkan frame asli dengan area deteksi warna merah
# 9. Keluar dengan tombol 'q'
# 10. Melepaskan kamera dan menutup semua jendela
# =====================================================================

def show_color_info(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Ketika klik kiri
        hsv_value = hsv[y, x]  # Mendapatkan nilai HSV pada titik (x, y)
        print(f"HSV: {hsv_value}")
        
        # Cek warna terdekat berdasarkan hue (untuk tujuan demonstrasi)
        hue = hsv_value[0]
        if 0 <= hue <= 10 or 170 <= hue <= 180:
            print("Warna yang terdeteksi: Merah")
        elif 100 <= hue <= 125:
            print("Warna yang terdeteksi: Biru")
        elif 140 <= hue <= 150:
            print("Warna yang terdeteksi: Ungu")
        else:
            print("Warna Tidak Teridentifikasi")

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera Tidak Terbuka")
    exit()

# Set callback mouse
cv2.namedWindow("Deteksi Warna")
cv2.setMouseCallback("Deteksi Warna", show_color_info)
while True:
    ret, frame = cap.read()
    
    if not ret: 
        print("Gagal Membaca Kamera")
        break
#  = = = = = = = = = = ALGORITMA DETEKSI WARNA = = = = = = = = = =    
    # 4. Konversi frame ke HSV
    # Mengubah frame dari ruang warna BGR ke HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
   
    # 5. Definisikan rentang warna untuk deteksi
    # Rentang warna merah
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2
    
    # Rentang warna biru
    lower_blue = np.array([100, 150, 150])
    upper_blue = np.array([125, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Rentang warna ungu
    lower_purple = np.array([140, 90, 150])  # Hue minimum untuk ungu
    upper_purple = np.array([150, 255, 255])  # Hue maksimum untuk ungu
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

    # 6. Gabungkan semua masker
    mask = mask_red | mask_blue | mask_purple
    
    # 7. Terapkan masker ke frame asli
    result = cv2.bitwise_or(frame, frame, mask=mask)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Gabungkan frame asli dengan hasil deteksi untuk membuat semua warna terlihat
    # cv2.addWeighted menggabungkan dua gambar (frame dan result) dengan bobot tertentu.
    # Frame asli (frame) diberi bobot 0.7 atau 70%, sehingga tetap terlihat lebih dominan.
    # Bobot menentukan seberapa besar kontribusi setiap gambar dalam hasil akhir.
    # Hasil deteksi warna merah (result) diberi bobot 0.3, sehingga warna deteksinya "terpadu" dengan frame asli.
    combined = cv2.addWeighted(frame, 0.7, result, 0.3, 0)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Temukan kontur pada masker merah
    # cv2.findContours digunakan untuk menemukan batas (kontur) area yang memenuhi masker merah.
    # cv2.RETR_TREE untuk mendapatkan semua hierarki kontur.
    # cv2.CHAIN_APPROX_SIMPLE mengurangi jumlah titik kontur untuk efisiensi.
    # Output: contours adalah daftar koordinat kontur merah yang ditemukan dalam gambar.
    

    # Proses deteksi area merah
    # Filter kontur kecil: cv2.contourArea(contour) > 500 memastikan area yang terlalu kecil (noise) diabaikan.
    # Dapatkan bounding box: cv2.boundingRect memberikan koordinat (x, y) serta dimensi (w, h) dari persegi panjang yang mengelilingi area kontur.
    # Gambar persegi panjang: cv2.rectangle menggambar persegi panjang hijau di sekitar area yang terdeteksi.
    # Tandai deteksi: Jika area merah terdeteksi, variabel merah_terdeteksi diatur menjadi True.
    # Deteksi merah
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_red:
        if cv2.contourArea(contour) > 500:  # Threshold area
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(combined, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Tambahkan teks di atas rectangle merah
            text_red = "FOUND MERAH"
            text_size_red = cv2.getTextSize(text_red, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x_red = x + (w - text_size_red[0]) // 2
            text_y_red = y - 10 if y - 10 > 20 else y + h + 20
            cv2.putText(combined, text_red, (text_x_red, text_y_red), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Deteksi biru
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_blue:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(combined, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Tambahkan teks di atas rectangle biru
            text_blue = "FOUND BLUE"
            text_size_blue = cv2.getTextSize(text_blue, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x_blue = x + (w - text_size_blue[0]) // 2
            text_y_blue = y - 10 if y - 10 > 20 else y + h + 20
            cv2.putText(combined, text_blue, (text_x_blue, text_y_blue), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Deteksi ungu
    contours_purple, _ = cv2.findContours(mask_purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_purple:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(combined, (x, y), (x + w, y + h), (255, 0, 255), 2)

            # Tambahkan teks di atas rectangle ungu
            text_purple = "FOUND PURPLE"
            text_size_purple = cv2.getTextSize(text_purple, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x_purple = x + (w - text_size_purple[0]) // 2
            text_y_purple = y - 10 if y - 10 > 20 else y + h + 20
            cv2.putText(combined, text_purple, (text_x_purple, text_y_purple), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Jika warna merah terdeteksi, tampilkan teks tambahan di atas frame (opsional)
    # Jika setidaknya satu area merah terdeteksi, teks "Warna Merah Terdeteksi!" akan muncul di bagian atas layar pada posisi tetap (50, 50).
    # Teks ini memberikan informasi tambahan secara keseluruhan kepada pengguna.
    # if merah_terdeteksi:
    #     cv2.putText(combined, "Warna Merah Terdeteksi!", (50, 50), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # 8. Tampilkan frame asli dengan deteksi warna merah
    cv2.imshow("Deteksi Warna Merah", combined)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # 9. Keluar dengan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

cap.release()
cv2.destroyAllWindows()
