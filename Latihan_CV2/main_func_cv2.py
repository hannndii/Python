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

# ========= Membaca, Menulis, Menampilkan Gambar/Video ============
# Baca Gambar 
cv2.imread()
# Tampilkan Gambar
cv2.imshow()
# Menyimpan Gambar
cv2.imwrite()
# Membaca Video
cv2.VideoCapture()
# Menulis Video
cv2.VideoWriter

# ========= Transformasi Gambar ==========
# Mengubah Ukuran Gambar
cv2.resize()
# Rotasi 
cv2.warpAffine()
# Flip
cv2.flip()

# ========= Pemrosesan Gambar =========
# Konversi Warna
cv2.cvtColor()
# Deteksi Tepi
cv2.Canny()
# Blur / Smoothing
cv2.GaussianBlur, cv2.medianBlur()
# Thresholding
cv2.threshold()

# =========== Pengenalan Objek dan Fitur ===========
# Deteksi wajah
cv2.CascadeClassifier()
# Deteksi fitur seperti sudut dan garis
cv2.HoughLines(), cv2.cornerHarris()

# =========== Operasi Geometris dan Matematika pada Gambar ==========
# Penambahan, pengurangan, dan penggabungan gambar
# Operasi bitwise: 
cv2.bitwise_and(), cv2.bitwise_or()

# =========== Penggunaan Kamera dan Streaming Video ==========
# Menangkap gambar langsung dari kamera: 
cv2.VideoCapture()
# Pemrosesan video secara real-time.