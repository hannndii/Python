# hasilA = int(input("input pertama: "))
# hasilB = int(input("input kedua: "))

# print("Isi dari hasil A: ", hasilA, ", dengan alamat: ", hex(id(hasilA)))
# print("Isi dari hasil B: ", hasilB, ", dengan alamat: ", hex(id(hasilA)))

# print("Apakah string A sama dengan string B? ", hasilA is hasilB)

# print("Tipe data hasil A: ", type(hasilA))
# print("Tipe data hasil B: ", type(hasilB))

# if (hasilA + hasilB == 4) ^ (hasilA * hasilB == 4):
#     print("Benar")
# else :
#     print("salah")


# i = 0
# hasil = 1
# for i in range(5):
#     perkalian = int(input("input: "))
#     hasil = perkalian * hasil
#     print("Tipe data", type(hasil))
#     print("Alamat elemen: ", hex(id(hasil)))
# print("Hasil: ", hasil)

class menu():
    def menu1():
        print("= = = = = = MENU = = = = = =")
        print("| \t 1. Pertambahan")
        print("| \t 2. Pengurangan")
        print("| \t 3. Pembagian")
        print("| \t 4. Perkalian")
        print("| \t 9. Exit")
        inputA = int(input("Pilih: "))

Menu = menu()

i = 0
print("= = = = = =  SELAMAT DATANG  = = = = = = ")
for i in range(10):
    Menu.menu1()
    if input == 1:
        print("Masukkan Panjang: ")
        a = int(input)
        print("Masukkan Lebar: ")
        b = int(input)
        print("Hasil: ", a + b)
    elif input == 2:
        print("Masukkan Panjang: ")
        a = int(input)
        print("Masukkan Lebar: ")
        b = int(input)
        print("Hasil: ", a - b)
    elif input == 3:
        print("Masukkan Panjang: ")
        a = int(input)
        print("Masukkan Lebar: ")
        b = int(input)
        print("Hasil: ", a * b)
    elif input == 4:
        print("Masukkan Panjang: ")
        a = int(input)
        print("Masukkan Lebar: ")
        b = int(input)
        print("Hasil: ", a / b)
    elif input == 9:
        break
        



    