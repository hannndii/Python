# ================ DICTIONARY  =================
import time
import dic_theater

# ================ KAMUS GLOBAL ================
current_theater = None

# ================ ALGORITMA  =================
def barrier():
    print('= = = = = = = = = = = = = = = = = = = = = = ')


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
        print('\t SELAMAT DATANG DI THEATERKU')
        print("- - - - - - - - - - - - - - - - - - - - -")
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
    list_lokasi = dic_theater.lok_theater['Lokasi']
   
    print('- - - - Theater Yang Tersedia - - - -')
    time.sleep(1)
    for i in range(len(list_lokasi)):
        print(i+1,'- ', list_lokasi[i])
    pilih = int(input('Pilih lokasi: '))
    if 1 <= pilih <= len(list_lokasi):
        theater_pilihan = list_lokasi[pilih - 1]  # Lokasi yang dipilih pengguna
        temp_film = pilih_film(theater_pilihan)  # Memilih film
        temp_tayang = pilih_jam_tayang(theater_pilihan, temp_film)
        no_kursi = daftar_kursi()  # Memilih kursi
        temp_bayar = bayar_film()  # Melakukan pembayaran
        info_resi(temp_film, temp_tayang, theater_pilihan, no_kursi, temp_bayar)  # Menampilkan resi

        dic_theater.riwayat['List'].append({
            "film": temp_film,
            "jam tayang" : temp_tayang,
            "lokasi": theater_pilihan,
            "kursi": no_kursi,
            "pembayaran": temp_bayar,
            "waktu": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
        })
    else:
        print("Pilihan tidak valid")

def pilih_film(lokasi_terpilih):
    barrier()

    # Memetakan lokasi ke data film dan jadwal
    if lokasi_terpilih == "Transmart Buah Batu XXI":
        film_list = dic_theater.t1['Film']
    elif lokasi_terpilih == "Summarecon Mall Bandung XXI":
        film_list = dic_theater.t2['Film']
    elif lokasi_terpilih == "Braga XXI":
        film_list = dic_theater.t3['Film']
    else:
        print("Lokasi tidak valid.")
        return None

    # Menampilkan daftar film
    print("= Film Yang Sedang Tayang =")
    for i, film in enumerate(film_list, start=1):
        print(f"{i} - {film}")

    # Memilih film
    pilih_f = int(input("Pilih film: "))
    if 1 <= pilih_f <= len(film_list):
        return film_list[pilih_f - 1]  
    else:
        print("Pilihan tidak valid")
        return pilih_film(lokasi_terpilih)

def pilih_jam_tayang(lokasi_terpilih, film):
    barrier()

    # Memetakan lokasi ke data jadwal berdasarkan film
    if lokasi_terpilih == "Transmart Buah Batu XXI":
        film_schedule = dic_theater.t1[film]
    elif lokasi_terpilih == "Summarecon Mall Bandung XXI":
        film_schedule = dic_theater.t2[film]
    elif lokasi_terpilih == "Braga XXI":
        film_schedule = dic_theater.t3[film]
    else:
        print("Lokasi tidak valid.")
        return None

    # Menampilkan jadwal tayang film
    print(f"= Jadwal Tayang untuk {film} =")
    for i, jadwal in enumerate(film_schedule, start=1):
        print(f"{i} - {jadwal}")

    # Memilih jadwal tayang
    pilih_j = int(input("Pilih jadwal tayang: "))
    if 1 <= pilih_j <= len(film_schedule):
        return film_schedule[pilih_j - 1]  
    else:
        print("Pilihan tidak valid")
        return pilih_jam_tayang(lokasi_terpilih, film)

def select_film_schedule(jadwal_film):
    print("= Jadwal Film =")
    for i, jadwal in enumerate(jadwal_film, start=1):
        print(f"{i} - {jadwal}")
    
    pilih_jam = int(input("Pilih jam tayang: "))
    if 1 <= pilih_jam <= len(jadwal_film):
        return jadwal_film[pilih_jam - 1]
    else:
        print("Pilihan tidak valid")
        return select_film_schedule(jadwal_film)

def daftar_kursi():
    barrier()
    kursiA = dic_theater.t1['Kursi_Film_A']

    print("= Kursi Yang Tersedia =")
    current_row = ""
    for i, k in enumerate(kursiA):
        if k[0] != current_row:
            if current_row != "":
                print()  
            current_row = k[0]
        print(f"{i+1}. {k}", end=" \t")
    print()

    pilih_kursi = int(input("Pilih kursi: "))
    if 1 <= pilih_kursi <= len(kursiA):
        return kursiA[pilih_kursi - 1]
    else:
        print("Pilihan tidak valid")
        return daftar_kursi()


def info_resi(nama_film, tayang, lokasi, no_kursi, type_bayar):
    current_time = time.localtime()
    barrier()

    print("- - - - - - - DETAIL PEMBAYARAN - - - - - - -")
    print(f"Nama Film: {nama_film}")
    print(f"Jam Tayang: {tayang}")
    print(f"Lokasi Tayang: {lokasi}")
    print(f"Waktu Pemesanan: {current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}")
    print(f"Nomor Kursi: {no_kursi}")
    print(f"Tipe Pembayaran: {type_bayar}")
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
            print("- - - - - - - - - - - - - -")
            print(f"Film: {transaksi['film']}") 
            print(f"Jam Tayang: {transaksi['jam tayang']}")
            print(f"Lokasi:  {transaksi['lokasi']}")
            print(f"Kursi: {transaksi['kursi']}")
            print(f"Pembayaran: {transaksi['pembayaran']}")
            print(f"Waktu: {transaksi['waktu']}")
            print("- - - - - - - - - - - - - -\n")
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
    global current_theater
    if current_theater is None:
        barrier()
        print("Silakan pilih lokasi teater terlebih dahulu.")
        pilih_lokasi()
        return

    barrier()
    print("- - - - - - - UPDATE JADWAL - - - - - - -")
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
        barrier()
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
        if pilihan_film == 1:
            kursi_film_list = current_theater['Kursi_Film_A'] 
        elif pilihan_film == 2:
            kursi_film_list = current_theater['Kursi_Film_B'] 
        elif pilihan_film == 3:
            kursi_film_list = current_theater['Kursi_Film_C']

        kursi_key = f"Kursi_{film.replace(' ', '_')}"
        kursi_list = kursi_film_list
        print(f"Kursi saat ini untuk {film}: {', '.join(kursi_list)}")
        
        print("\n- - - - - - - - - - Perintah Yang Tersedia - - - - - - - - - -")
        print("1. Tambah Kursi")
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
    barrier()

def lihat_rating():
    barrier()
    print("- - - - - - - - REVIEW FILM TAHUN 2024 - - - - - - - -")
    for film, data in dic_theater.film_reviews.items():
        avg_rating = sum(data["ratings"]) / len(data["ratings"]) if data["ratings"] else 0
        print(f"Film: {film}, Rating rata-rata: {avg_rating:.1f}")
        print("Ulasan:")
        for review in data["reviews"]:
            print(f"- {review}")
        print()
        barrier()

# ======================= ENDPROGRAM =========================