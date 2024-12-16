import cv2

# Membaca gambar
image = cv2.imread('trial/The boy is holding a phone, a call or a message in his hands_ Vector flat illustration_.jpeg')
# Membuat jendela dengan nama dan properti khusus
cv2.namedWindow("My Window", cv2.WINDOW_AUTOSIZE)

# Menampilkan gambar pada jendela yang sudah dibuat
cv2.imshow("My Window", image)

# Menunggu hingga tombol ditekan
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


# Menutup semua jendela


