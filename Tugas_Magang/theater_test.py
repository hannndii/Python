import theater_function
# ================ MAIN  =================

# KAMUS GLOBAL
dicT = theater_function

#  FUNCTION MAIN
# ================ LOGIN PENGGUNA ==============
def login_user():
    print('- - - - - - - SELAMAT DATANG DI THEATERKU - - - - - - -')
    username_user = str(input("Username (Maks 10 kata): "))
    while(len(username_user) > 11):
        print("Maksimal 10 karakter!")
        username_user = str(input("Username: "))
    pass_user = str(input("Password: "))
    while(len(pass_user) > 11):
        print("Maksimal 10 karakter!")
        pass_user = str(input("Password: "))
    
    dicT.menu_pelanggan()

# ================ LOGIN ADMIN ==============
def login_admin():
    maxLog = 0
    print('- - - - - - - ADMIN CONTROL ACCESS - - - - - - -')
    username_user = str(input("Username: "))
    pass_user = str(input("Password: "))
    while(username_user != "Admin" and pass_user != "Admin" ):
        print("-> DATA SALAH! Silahkan masukkan kembali :(")
        dicT.barrier()
        maxLog += 1
        if maxLog == 5:
            print("-> Terdeteksi aktivitas mencurigakan !!!")
            break
        username_user = str(input("Username: "))
        pass_user = str(input("Password: "))
        
    if username_user == "Admin" and pass_user == "Admin":
        dicT.menu_admin()

# ================== ALGORITMA ==================
pilihan = int(input("Pilih Role: "))
if pilihan == 1:
    login_admin()
elif pilihan == 2:
    login_user()
    


#  END ALGORITMA



