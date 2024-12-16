import numpy as np
import cv2

# =====================================================================
# Algoritma
# 1. Membuka kamera (0 biasanya adalah default untuk kamera laptop)
# 2. Memeriksa apakah kamera berhasil diakses
# 3. Gunakan perulangan untuk membaca frame dari kamera
# 4. Buat kondisi pengecekan frame dari kamera
# 5. Tampilkan Frame pada Window
# 6. Keluar loop dengan input
# 7. Melepaskan kamera dan menutup semua jendela
# =====================================================================

# 1. Membuka kamera (0 biasanya adalah default untuk kamera laptop)
cap = cv2.VideoCapture(1)

# 2. Memeriksa apakah kamera berhasil diakses

if not cap.isOpened():
    print("Kamera Tidak Terbuka")
    exit()
    

# 3. Gunakan perulangan untuk membaca frame dari kamera
while True:
    # ret: Boolean yang menunjukkan apakah frame berhasil diambil.
    # frame: Frame gambar dari kamera.
    ret, frame = cap.read()
    
    if not ret:
        print("Gagal Membaca Kamera")
        break
    
    cv2.namedWindow('Handi', cv2.WINDOW_NORMAL)
    # 5. Tampilkan Frame pada Window
    cv2.imshow("Kamera Laptop Endi", frame)
    
    # 6. Keluar loop dengan input
    # 0xFF adalah bilangan heksadesimal yang sama dengan 255 dalam desimal.
    # Ini digunakan untuk masking atau mengambil 8 bit terakhir dari nilai yang 
    # dikembalikan oleh cv2.waitKey(1).
    # Fungsi ord() mengembalikan kode ASCII dari karakter yang diberikan.
    # cv2.waitKey(1) & 0xFF: Mengambil nilai ASCII dari tombol yang ditekan (hanya 8 bit terakhir).
    # ord('q'): Nilai ASCII dari huruf q adalah 113.

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

# 7. Melepaskan kamera dan menutup semua jendela 
cap.release()
cv2.destroyAllWindows()

    