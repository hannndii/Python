# ================ DICTIONARY  =================
import time
import dic_theater

# ================ KAMUS GLOBAL ================
current_theater = None
# ================ FUNCTION  =================


def barrier():
    print('= = = = = = = = = = = = = = = = = = = = = = ')


def login():
    print('SELAMAT DATANG DI THEATERKU')
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
        print('ADMINISTRATOR')
        print('1. Update Jadwal')
        print('2. Update Film')
        print('3. Update Jumlah Kursi')
        print('4. keluar')
        masukan = input('Masukan: ')
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
    list_film = dic_theater.t1['Film']
    list_lokasi = dic_theater.lok_theater['Lokasi']
   
    print('- - - - Theater Yang Tersedia - - - -')
    time.sleep(1)
    for i in range(len(list_lokasi)):
        print(i+1,'- ', list_lokasi[i])
    pilih = int(input('Pilih lokasi: '))
    if 1 <= pilih <= len(list_lokasi):
        theater_pilihan = list_lokasi[pilih - 1]  # Lokasi yang dipilih pengguna
        temp_film = pilih_film()  # Memilih film
        no_kursi = daftar_kursi()  # Memilih kursi
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
    barrier()
    film = dic_theater.t1['Film']
    filmA = dic_theater.t1['Film A']
    filmB = dic_theater.t1['Film B']
    filmC = dic_theater.t1['Film C']

    print("= Film Yang Sedang Tayang =")
    for i in range(len(film)):
        print(i+1, "- ", film[i])
    pilih_f = int(input("Pilih film: "))

    if pilih_f == 1:
        return select_film_schedule(filmA)
    elif pilih_f == 2:
        return select_film_schedule(filmB)
    elif pilih_f == 3:
        return select_film_schedule(filmC)
    else:
        print("Pilihan tidak valid")
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

def daftar_kursi():
    barrier()
    kursiA = dic_theater.t1['Kursi_Film_A']

    print("= Kursi Yang Tersedia =")
    current_row = ""
    for i, k in enumerate(kursiA):
        if k[0] != current_row:
            if current_row != "":
                print()  # Pindah ke baris baru
            current_row = k[0]
        print(f"{i+1}. {k}", end=" \t")
    print()

    pilih_kursi = int(input("Pilih kursi: "))
    if 1 <= pilih_kursi <= len(kursiA):
        return kursiA[pilih_kursi - 1]
    else:
        print("Pilihan tidak valid")
        return daftar_kursi()


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
    print("= Pilih Lokasi Teater =")
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
    global current_theater
    if current_theater is None:
        print("Silakan pilih lokasi teater terlebih dahulu.")
        pilih_lokasi()
        return

    barrier()
    print("= Update Jadwal =")
    film_list = current_theater["Film"]
    print("Film tersedia:")
    for i, film in enumerate(film_list, start=1):
        print(f"{i}. {film}")
    
    pilihan_film = int(input("Pilih film yang ingin diupdate jadwalnya: "))
    if 1 <= pilihan_film <= len(film_list):
        film = film_list[pilihan_film - 1]
        jadwal = current_theater[film]
        print(f"Jadwal saat ini untuk {film}:")
        for i, jam in enumerate(jadwal, start=1):
            print(f"{i}. {jam}")
        
        print("\n1. Tambah Jadwal")
        print("2. Hapus Jadwal")
        pilihan = int(input("Pilih aksi: "))
        
        if pilihan == 1:
            jadwal_baru = input("Masukkan jadwal baru (format HH:MM - HH:MM): ")
            jadwal.append(jadwal_baru)
            print(f"Jadwal berhasil ditambahkan untuk {film}.")
        elif pilihan == 2:
            hapus_jadwal = int(input("Pilih jadwal yang ingin dihapus: "))
            if 1 <= hapus_jadwal <= len(jadwal):
                jadwal.pop(hapus_jadwal - 1)
                print(f"Jadwal berhasil dihapus untuk {film}.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid.")

def update_film():
    global current_theater
    if current_theater is None:
        print("Silakan pilih lokasi teater terlebih dahulu.")
        pilih_lokasi()
        return

    barrier()
    print("= Update Film =")
    film_list = current_theater["Film"]
    print("Film tersedia:")
    for i, film in enumerate(film_list, start=1):
        print(f"{i}. {film}")
    
    print("\n1. Tambah Film")
    print("2. Hapus Film")
    pilihan = int(input("Pilih aksi: "))
    
    if pilihan == 1:
        film_baru = input("Masukkan nama film baru: ")
        if film_baru in film_list:
            print("Film sudah tersedia.")
        else:
            film_list.append(film_baru)
            current_theater[film_baru] = []
            print(f"Film {film_baru} berhasil ditambahkan.")
    elif pilihan == 2:
        hapus_film = int(input("Pilih film yang ingin dihapus: "))
        if 1 <= hapus_film <= len(film_list):
            film_hapus = film_list.pop(hapus_film - 1)
            current_theater.pop(film_hapus, None)
            print(f"Film {film_hapus} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid.")

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