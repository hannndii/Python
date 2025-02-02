# Penjelasan Detail Line-by-Line Kode Program Drone

## 1. Import dan Koneksi

```python
from pymavlink import mavutil
```
- Mengimport modul mavutil dari library pymavlink
- mavutil berisi fungsi-fungsi untuk komunikasi dengan drone via protokol MAVLink

```python
import time
```
- Mengimport modul time untuk fungsi delay dan pengukuran waktu
- Digunakan untuk memberi jeda antar perintah

```python
import threading
```
- Mengimport modul threading untuk menjalankan proses paralel
- Memungkinkan monitoring status drone bersamaan dengan kontrol

```python
import math
```
- Mengimport modul math untuk perhitungan matematika
- Dibutuhkan untuk kalkulasi trigonometri dalam pola hexagon

```python
string_koneksi1 = 'udp:127.0.0.1:14551'
```
- Mendefinisikan string koneksi UDP
- 127.0.0.1 adalah localhost (komputer sendiri)
- 14551 adalah port untuk komunikasi dengan Mission Planner

```python
konek = mavutil.mavlink_connection(string_koneksi1)
```
- Membuat objek koneksi MAVLink menggunakan string koneksi
- Menginisialisasi komunikasi dengan drone

```python
konek.wait_heartbeat()
```
- Menunggu sinyal heartbeat pertama dari drone
- Memastikan koneksi sudah established sebelum mengirim perintah

## 2. Fungsi set_mode()

```python
def set_mode(mode):
```
- Mendefinisikan fungsi untuk mengubah mode terbang
- Parameter 'mode' adalah string (misal: "GUIDED", "STABILIZE")

```python
    if mode not in konek.mode_mapping():
        print(f'Mode {mode} tidak tersedia')
        return
```
- Memeriksa apakah mode yang diminta tersedia
- konek.mode_mapping() berisi daftar mode yang didukung
- Jika tidak tersedia, print pesan error dan keluar fungsi

```python
    mode_id = konek.mode_mapping()[mode]
```
- Mendapatkan ID numerik untuk mode yang diminta
- Setiap mode memiliki ID unik dalam protokol MAVLink

```python
    konek.mav.set_mode_send(
        konek.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id)
```
- Mengirim perintah set_mode ke drone
- target_system: ID sistem drone
- MAV_MODE_FLAG_CUSTOM_MODE_ENABLED: flag untuk custom mode
- mode_id: ID mode yang akan diset

## 3. Fungsi arm_drone()

```python
def arm_drone():
```
- Mendefinisikan fungsi untuk arming drone
- Arming mengaktifkan motor-motor drone

```python
    konek.mav.command_long_send(
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,  # confirmation
        1,  # param1 (1=arm, 0=disarm)
        0, 0, 0, 0, 0, 0)  # param2-7 (tidak digunakan)
```
- Mengirim perintah arm via MAV_CMD_COMPONENT_ARM_DISARM
- target_system: ID sistem drone
- target_component: ID komponen (biasanya autopilot)
- Parameter 1=1 untuk arming
- Parameter lain diberi nilai 0 (tidak digunakan)

## 4. Fungsi takeoff()

```python
def takeoff(altitude):
```
- Mendefinisikan fungsi takeoff dengan parameter ketinggian
- altitude dalam meter

```python
    konek.mav.command_long_send(
        konek.target_system,
        konek.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,  # confirmation
        0, 0, 0, 0, 0, 0,  # param1-6 (tidak digunakan)
        altitude)  # param7 (target altitude)
```
- Mengirim perintah takeoff ke ketinggian tertentu
- MAV_CMD_NAV_TAKEOFF adalah command untuk takeoff
- Parameter terakhir menentukan target ketinggian

## 5. Fungsi set_velocity()

```python
def set_velocity(vx, vy, vz, yaw_rate=0):
```
- Mendefinisikan fungsi untuk mengatur kecepatan drone
- vx: kecepatan sumbu x (maju/mundur)
- vy: kecepatan sumbu y (kiri/kanan)
- vz: kecepatan sumbu z (atas/bawah)
- yaw_rate: kecepatan rotasi (opsional)

```python
    konek.mav.set_position_target_local_ned_send(
        0,  # timestamp
        konek.target_system,  # target system
        konek.target_component,  # target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # koordinat frame
        0b0000111111000111,  # type_mask
        0, 0, 0,  # posisi x,y,z (tidak digunakan)
        vx, vy, vz,  # kecepatan
        0, 0, 0,  # akselerasi (tidak digunakan)
        yaw_rate, 0)  # yaw dan yaw_rate
```
- Mengatur kecepatan dalam frame NED (North-East-Down)
- type_mask menentukan parameter mana yang aktif
- Menggunakan kecepatan (vx,vy,vz) bukan posisi
- Yaw rate untuk kontrol rotasi

## 6. Fungsi fly_hexagon()

```python
def fly_hexagon():
```
- Fungsi untuk mengimplementasikan pola terbang hexagon

```python
    speed = 2  # m/s
```
- Mendefinisikan kecepatan konstan 2 meter/detik

```python
    segment_duration = 5  # seconds
```
- Durasi terbang lurus untuk setiap segmen (5 detik)

```python
    angles = [0, 60, 120, 180, 240, 300, 0]
```
- Daftar sudut untuk membentuk hexagon
- 6 sudut dengan interval 60 derajat
- 0 terakhir untuk kembali ke posisi awal

```python
    for angle in angles:
        rad = math.radians(angle)
```
- Iterasi setiap sudut
- Konversi sudut dari derajat ke radian

```python
        vx = speed * math.cos(rad)
        vy = speed * math.sin(rad)
```
- Menghitung komponen kecepatan x dan y
- Menggunakan fungsi trigonometri
- cos(θ) untuk komponen x
- sin(θ) untuk komponen y

```python
        set_velocity(vx, vy, 0)
```
- Set kecepatan sesuai perhitungan
- vz = 0 (tidak ada pergerakan vertikal)

```python
        time.sleep(segment_duration)
```
- Tunggu selama durasi segmen (5 detik)
- Drone akan terbang lurus selama interval ini

## 7. Fungsi main()

```python
def main():
```
- Fungsi utama yang menjalankan seluruh program

```python
    set_mode("GUIDED")
    time.sleep(1)
```
- Set mode ke GUIDED untuk kontrol otomatis
- Tunggu 1 detik untuk mode change

```python
    print("Arming drone...")
    arm_drone()
    time.sleep(2)
```
- Arming drone
- Tunggu 2 detik untuk proses arming

```python
    print("Taking off...")
    takeoff(3)  # 3 meters = ~10 feet
    time.sleep(10)
```
- Takeoff ke ketinggian 3 meter
- Tunggu 10 detik untuk mencapai ketinggian

```python
    print("Starting hexagon pattern...")
    while True:
        fly_hexagon()
        print("Completed one hexagon, starting next...")
```
- Loop tak terbatas menjalankan pola hexagon
- Setiap selesai satu putaran, mulai putaran baru

## 8. Error Handling

```python
if __name__ == "__main__":
    try:
        main()
```
- Menjalankan fungsi main() jika script dijalankan langsung
- try-except untuk menangani interupsi

```python
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna")
        set_velocity(0, 0, 0)
```
- Menangkap Ctrl+C dari pengguna
- Menghentikan pergerakan drone
- Set semua kecepatan ke 0

