from ultralytics import YOLO




model = YOLO(r'D:\My Code\PYTHON\Tugas_Magang_03\best.pt')
result = model(source=1, show=True, conf=0.5, save=True)
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("kamera tidak ada")
#     exit()
    
# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Gagal membaca frame dari kamera")
#         break
    
#     result = model.predict(frame, conf=0.5, show=True)
    
#     cv2.imshow("Detect Plane", frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()


# from ultralytics import YOLO
# import cv2

# # Load model YOLO
# model = YOLO(r"D:\My Code\PYTHON\Tugas_Magang_03\DataSet\best.pt")  # Ganti dengan path model YOLO Anda

# # Path file video yang ingin dideteksi
# video_path = "D:\My Code\PYTHON\Tugas_Magang_03\Video\WhatsApp Video 2024-12-16 at 21.36.18_9b4f810f.mp4"  # Ganti dengan path file video Anda
# output_path = "D:\My Code\PYTHON\Tugas_Magang_03\Video"  # Path untuk menyimpan hasil deteksi

# # Buka video menggunakan OpenCV
# cap = cv2.VideoCapture(video_path)

# # Periksa apakah video berhasil dibuka
# if not cap.isOpened():
#     print("Error: Video tidak dapat dibuka.")
#     exit()
# # Proses setiap frame dalam video
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break  # Keluar dari loop jika video selesai

#     # Prediksi menggunakan model YOLO
#     results = model.predict(frame, conf=0.5, show=False)  # conf=0.5 adalah confidence threshold

#     # Tampilkan hasil prediksi pada frame
#     annotated_frame = results[0].plot()  # Gambar hasil deteksi pada frame    

#     # Tampilkan frame (opsional, jika ingin melihat real-time di jendela)
#     cv2.imshow("YOLO Detection", annotated_frame)

#     # Tekan 'q' untuk keluar dari loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release semua resource
# cap.release()
# cv2.destroyAllWindows()

# print(f"Deteksi selesai! Hasil disimpan di: {output_path}")


