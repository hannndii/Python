# Penjelasan Detail Kode Program Deteksi Warna dan Kontrol Drone

## 1. Import Tambahan

```python
import cv2
import numpy as np
```
- cv2: Library OpenCV untuk pemrosesan gambar dan computer vision
- numpy: Library untuk operasi array dan matematika

## 2. Variabel Global

```python
purple_detected = False
```
- Flag global untuk status deteksi warna ungu
- Digunakan untuk komunikasi antar thread

## 3. Fungsi return_to_launch()

```python
def return_to_launch():
    set_mode("RTL")
    print("Returning to launch position...")
```
- Mengubah mode drone ke RTL (Return To Launch)
- RTL akan mengembalikan drone ke posisi takeoff
- Drone akan landing otomatis di posisi awal

## 4. Fungsi detect_purple()

```python
def detect_purple():
    global purple_detected
```
- Deklarasi fungsi deteksi warna ungu
- Menggunakan global flag untuk update status deteksi

```python
    cap = cv2.VideoCapture(0)
```
- Membuka kamera laptop (index 0)
- Menginisialisasi capture video stream

```python
    while True:
        ret, frame = cap.read()
```
- Loop kontinu untuk membaca frame
- ret: status pembacaan berhasil/gagal
- frame: gambar dari kamera

```python
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
- Konversi frame dari BGR ke HSV color space
- HSV lebih baik untuk deteksi warna spesifik

```python
        lower_purple = np.array([130, 50, 50])
        upper_purple = np.array([160, 255, 255])
```
- Mendefinisikan range warna ungu dalam HSV
- H: 130-160 (hue ungu)
- S: 50-255 (saturasi)
- V: 50-255 (value/kecerahan)

```python
        purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)
```
- Membuat mask binary untuk pixel warna ungu
- Pixel ungu akan berwarna putih (255)
- Pixel lain akan berwarna hitam (0)

```python
        result = cv2.bitwise_and(frame, frame, mask=~purple_mask)
```
- Aplikasi mask ke frame original
- ~purple_mask: inversi mask (semua warna kecuali ungu)
- Hasil: frame dengan warna ungu diblok

```python
        purple_pixels = cv2.countNonZero(purple_mask)
        if purple_pixels > 5000:
            purple_detected = True
```
- Hitung jumlah pixel ungu dalam frame
- Jika lebih dari threshold (5000), set flag deteksi
- Threshold dapat disesuaikan sesuai kebutuhan

```python
        cv2.imshow('Original', frame)
        cv2.imshow('Masked (Non-Purple)', result)
```
- Menampilkan frame original dan hasil masking
- Monitoring visual untuk deteksi

## 5. Modifikasi Fungsi fly_hexagon()

```python
def fly_hexagon():
    global purple_detected
```
- Tambahan akses ke flag global

```python
    for angle in angles:
        if purple_detected:
            return True
```
- Cek status deteksi di setiap iterasi
- Return True jika ungu terdeteksi untuk trigger RTL

## 6. Modifikasi Fungsi main()

```python
    detection_thread = threading.Thread(target=detect_purple)
    detection_thread.daemon = True
    detection_thread.start()
```
- Membuat thread terpisah untuk deteksi warna
- daemon=True: thread akan berhenti saat program utama selesai
- Start thread sebelum operasi drone

```python
    while not purple_detected:
        should_rtl = fly_hexagon()
        if should_rtl:
            break
```
- Loop utama dengan pengecekan deteksi
- should_rtl: status untuk trigger RTL
- Break loop jika ungu terdeteksi

```python
    if purple_detected:
        return_to_launch()
```
- Eksekusi RTL jika ungu terdeteksi

## 7. Error Handling Update

```python
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna")
        set_velocity(0, 0, 0)
        cv2.destroyAllWindows()
```
- Tambahan cleanup untuk window OpenCV
- Menutup semua window display saat program berhenti

## Catatan Penting:
1. Kalibrasi Warna:
   - Range HSV untuk warna ungu dapat disesuaikan
   - Perlu testing di kondisi pencahayaan berbeda

2. Performa:
   - Thread terpisah mencegah lag pada kontrol drone
   - Deteksi warna berjalan paralel dengan navigasi

3. Keamanan:
   - RTL otomatis saat warna terdeteksi
   - Cleanup proper saat program berhenti

4. Hardware:
   - Membutuhkan kamera laptop/webcam
   - Pastikan driver kamera terinstall

5. Dependencies:
   - OpenCV (`cv2`)
   - NumPy (`numpy`)
   - PyMavlink (`pymavlink`)

