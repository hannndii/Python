# ================ DICTIONARY  =================
import time
import dic_theater

# ================ KAMUS GLOBAL ================
current_theater = None

# ================ ALGORITMA  =================
def barrier():
    print('= = = = = = = = = = = = = = = = = = = = = = \n')

def login():
    print('- - - - - - - SELAMAT DATANG DI THEATERKU - - - - - - -')
    username_user = str(input("Username: "))
    pass_user = str(input("Password: "))
    if pass_user == "Admin" and username_user == "Admin":
        menu_admin()
    else:
        menu_pelanggan()

def menu_admin():
    # untuk Admin
    barrier()
    while True:
        print('- - - - - - - ADMINISTRATOR - - - - - - -')
        print('1. Update Jadwal')
        print('2. Update Film')
        print('3. Update Jumlah Kursi')
        print('4. Keluar')
        masukan = input('Pilih(1-4): ')
        pilihan = int(masukan)
        if pilihan == 1:
            update_jadwal()
        elif pilihan == 2:
            update_film()
        elif pilihan == 3:
            update_kursi()
        elif pilihan == 4:
            break
        else:
            print('Pilihan tidak valid')
    
def menu_pelanggan():
    # Untuk Pelanggan
    barrier()
    while True:
        print('SELAMAT DATANG DI THEATERKU')
        print('1. Pesan Tiket')
        print('2. Lihat Daftar Transaksi')
        print('3. Lihat Rating dan Ulasan Film')
        print('4. Beri Rating dan Ulasan Film')
        print('5. Keluar')
        masukan = input('Masukan: ')
        pilihan = int(masukan)
        if pilihan == 1:
            pilih_theater()
        elif pilihan == 2:
            lihat_transaksi()
        elif pilihan == 3:
            lihat_rating()
        elif pilihan == 4:
            beri_rating()
        elif pilihan == 5:
            break
        else:
            print('Pilihan tidak valid')

def message():
    print('\t = Transaksi Berhasil = \t ')

def pilih_theater():
    barrier()
    list_lokasi = dic_theater["lokasi"]  # Mengakses lokasi dari dictionary
    print('- - - - Theater Yang Tersedia - - - -')
    time.sleep(1)
    for i, lokasi in enumerate(list_lokasi, start=1):
        print(f"{i} - {lokasi}")
    pilih = int(input('Pilih lokasi: '))

    if 1 <= pilih <= len(list_lokasi):
        theater_pilihan = list_lokasi[pilih - 1]  # Lokasi yang dipilih pengguna
        temp_film = pilih_film()  # Memilih film
        no_kursi = daftar_kursi(temp_film)  # Memilih kursi
        temp_bayar = bayar_film()  # Melakukan pembayaran
        info_resi(temp_film, theater_pilihan, no_kursi, temp_bayar)  # Menampilkan resi

        dic_theater.riwayat['List'].append({
            "film": temp_film,
            "lokasi": theater_pilihan,
            "kursi": no_kursi,
            "pembayaran": temp_bayar,
            "waktu": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
        })
    else:
        print("Pilihan tidak valid")

def pilih_film():
    if current_theater is None:
        print("Pilih lokasi theater terlebih dahulu.")
        pilih_lokasi()
    
    print("Film yang tersedia:")
    films = list(current_theater["films"].keys())
    for i, film in enumerate(films, start=1):
        print(f"{i}. {film}")
    pilihan_film = int(input("Masukkan pilihan film: ")) - 1
    if 0 <= pilihan_film < len(films):
        film_terpilih = films[pilihan_film]
        print("Jadwal tersedia:")
        jadwal = current_theater["films"][film_terpilih]
        for i, waktu in enumerate(jadwal, start=1):
            print(f"{i}. {waktu}")
        pilihan_jadwal = int(input("Pilih jadwal tayang: ")) - 1
        if 0 <= pilihan_jadwal < len(jadwal):
            return film_terpilih, jadwal[pilihan_jadwal]
        else:
            print("Pilihan jadwal tidak valid.")
    else:
        print("Pilihan film tidak valid.")
    return pilih_film()


def select_film_schedule(film_schedule):
    for i in range(len(film_schedule)):
        print(i+1, "- ", film_schedule[i])
    pilih_jam = int(input("Pilih jam tayang: "))
    if 1 <= pilih_jam <= len(film_schedule):
        return film_schedule[pilih_jam - 1]
    else:
        print("Pilihan tidak valid")
        return select_film_schedule(film_schedule)

def daftar_kursi(film):
    seats = current_theater["seats"][film]
    print("Kursi yang tersedia:")
    for i, kursi in enumerate(seats, start=1):
        print(f"{i}. {kursi}")
    pilihan_kursi = int(input("Pilih kursi: ")) - 1
    if 0 <= pilihan_kursi < len(seats):
        return seats[pilihan_kursi]
    else:
        print("Pilihan kursi tidak valid.")
        return daftar_kursi(film)


def info_resi(nama_film, lokasi, no_kursi, type_bayar):
    current_time = time.localtime()
    barrier()

    print(" DETAIL PEMBAYARAN")
    print(f"Nama Film: {nama_film}")
    print(f"Lokasi Tayang: {lokasi}")
    print(f"Waktu Pemesanan: {current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}")
    print(f"Nomor Kursi: {no_kursi}")
    print(f"Tipe Pembayaran: {type_bayar}")
    print("\n")
    barrier()
    print("TERIMAKASIH ATAS PEMBELIAN NYA")
    input("Tekan Enter untuk kembali...")
    time.sleep(3)


def bayar_film():
    payment = dic_theater.pembayaran["list_type"]
    count_list = len(payment)
    count = 0
    while count != count_list:
            print(count+1, ". ", payment[count])
            count += 1

    pilih_bayar = int(input("Pilih Pembayaran: "))
    temp_bayar = payment[pilih_bayar-1]
    if pilih_bayar == 1:
        isi_no_bayar = str(input("Masukkan nomor rekening: "))
    elif pilih_bayar == 2:
        isi_no_bayar = str(input("Masukkan nomor telepon: "))
    elif pilih_bayar == 3:
        isi_no_bayar = print("Silahkan lakukan pembayaran melalui kasir Theater :)")

    checkout = str(input("Bayar (Yes/No)? "))
    if(checkout == "No"):
        bayar_film()
    else :
        print("Tunggu Sebentar")
        time.sleep(2)
        # cetak resi
        
    return temp_bayar
        

def lihat_transaksi():
    barrier()
    if not dic_theater.riwayat['List']:
        print("Belum ada transaksi yang dilakukan.")
    else:
        print("= = = RIWAYAT TRANSAKSI = = =")
        for i, transaksi in enumerate(dic_theater.riwayat['List'], start=1):
            print(f"{i}. Film: {transaksi['film']}, Lokasi: {transaksi['lokasi']}, Kursi: {transaksi['kursi']}, "
                  f"Pembayaran: {transaksi['pembayaran']}, Waktu: {transaksi['waktu']}")
    input("Tekan Enter untuk kembali...")
    time.sleep(3)
    
    
def pilih_lokasi():
    global current_theater
    barrier()
    print("- - - - - - - PILIH LOKASI THEATER - - - - - - -")
    lokasi_list = dic_theater.lok_theater['Lokasi']
    for i, lokasi in enumerate(lokasi_list, start=1):
        print(f"{i}. {lokasi}")
    pilihan = int(input("Pilih lokasi teater: "))
    
    if 1 <= pilihan <= len(lokasi_list):
        lokasi_pilihan = lokasi_list[pilihan - 1]
        if lokasi_pilihan == "Transmart Buah Batu XXI":
            current_theater = dic_theater.t1
        elif lokasi_pilihan == "Summarecon Mall Bandung XXI":
            current_theater = dic_theater.t2
        elif lokasi_pilihan == "Braga XXI":
            current_theater = dic_theater.t3
        print(f"Teater yang dipilih: {current_theater['Lokasi']}")
    else:
        print("Pilihan tidak valid.")

def update_jadwal():
    if current_theater is None:
        print("Pilih lokasi theater terlebih dahulu.")
        pilih_lokasi()

    films = list(current_theater["films"].keys())
    print("Film tersedia:")
    for i, film in enumerate(films, start=1):
        print(f"{i}. {film}")
    pilihan = int(input("Pilih film untuk update jadwal: ")) - 1
    if 0 <= pilihan < len(films):
        film = films[pilihan]
        print("Jadwal saat ini:", current_theater["films"][film])
        print("1. Tambah jadwal")
        print("2. Hapus jadwal")
        opsi = int(input("Pilih opsi: "))
        if opsi == 1:
            jadwal_baru = input("Masukkan jadwal baru: ")
            current_theater["films"][film].append(jadwal_baru)
            print("Jadwal berhasil ditambahkan.")
        elif opsi == 2:
            hapus_jadwal = int(input("Pilih jadwal untuk dihapus: ")) - 1
            if 0 <= hapus_jadwal < len(current_theater["films"][film]):
                current_theater["films"][film].pop(hapus_jadwal)
                print("Jadwal berhasil dihapus.")
        else:
            print("Opsi tidak valid.")
    else:
        print("Pilihan tidak valid.")

def update_film():
    print("1. Tambah film baru")
    print("2. Hapus film yang ada")
    opsi = int(input("Pilih opsi: "))
    if opsi == 1:
        film_baru = input("Masukkan nama film baru: ")
        jadwal_baru = input("Masukkan jadwal film baru (pisahkan dengan koma): ").split(", ")
        current_theater["films"][film_baru] = jadwal_baru
        current_theater["seats"][film_baru] = [f"{film_baru[0]}{i}" for i in range(1, 6)]
        print("Film baru berhasil ditambahkan.")
    elif opsi == 2:
        films = list(current_theater["films"].keys())
        print("Film tersedia:")
        for i, film in enumerate(films, start=1):
            print(f"{i}. {film}")
        hapus_film = int(input("Pilih film untuk dihapus: ")) - 1
        if 0 <= hapus_film < len(films):
            del current_theater["films"][films[hapus_film]]
            del current_theater["seats"][films[hapus_film]]
            print("Film berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Opsi tidak valid.")

def update_kursi():
    global current_theater
   
    if current_theater is None:
        print("Silakan pilih lokasi teater terlebih dahulu.")
        pilih_lokasi()
        return

    barrier()
    print("= Update Jumlah Kursi =")
    film_list = current_theater["Film"]
    print("Film tersedia:")
    for i, film in enumerate(film_list, start=1):
        print(f"{i}. {film}")
    
    pilihan_film = int(input("Pilih film untuk update kursi: "))
    if 1 <= pilihan_film <= len(film_list):
        film = film_list[pilihan_film - 1]
        kursi_key = f"Kursi_{film.replace(' ', '_')}"
        kursi_list = current_theater[kursi_key]
        print(f"Kursi saat ini untuk {film}: {', '.join(kursi_list)}")
        
        print("\n1. Tambah Kursi")
        print("2. Hapus Kursi")
        pilihan = int(input("Pilih aksi: "))
        
        if pilihan == 1:
            kursi_baru = input("Masukkan kursi baru (format A1, B2, dll.): ")
            if kursi_baru in kursi_list:
                print("Kursi sudah tersedia.")
            else:
                kursi_list.append(kursi_baru)
                print(f"Kursi {kursi_baru} berhasil ditambahkan.")
        elif pilihan == 2:
            hapus_kursi = input("Masukkan kursi yang ingin dihapus (format A1, B2, dll.): ")
            if hapus_kursi in kursi_list:
                kursi_list.remove(hapus_kursi)
                print(f"Kursi {hapus_kursi} berhasil dihapus.")
            else:
                print("Kursi tidak ditemukan.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid.")


def beri_rating():
    print("Film yang tersedia:")
    for i, film in enumerate(dic_theater.film_reviews.keys(), start=1):
        print(f"{i}. {film}")
    pilih_film = int(input("Pilih film untuk memberikan rating: "))
    film_terpilih = list(dic_theater.film_reviews.keys())[pilih_film - 1]

    # Memberikan rating
    rating = int(input("Beri rating (1-5): "))
    if 1 <= rating <= 5:
        dic_theater.film_reviews[film_terpilih]["ratings"].append(rating)
    else:
        print("Rating tidak valid. Coba lagi.")

    # Menambahkan ulasan
    ulasan = input("Tulis ulasan: ")
    dic_theater.film_reviews[film_terpilih]["reviews"].append(ulasan)
    print("Terima kasih atas ulasan Anda!")

def lihat_rating():
    print("Film yang tersedia:")
    for film, data in dic_theater.film_reviews.items():
        avg_rating = sum(data["ratings"]) / len(data["ratings"]) if data["ratings"] else 0
        print(f"Film: {film}, Rating rata-rata: {avg_rating:.1f}")
        print("Ulasan:")
        for review in data["reviews"]:
            print(f"- {review}")
        print()

# ======================= END ALGORITMA =========================