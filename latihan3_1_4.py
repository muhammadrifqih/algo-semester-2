print('Nama  : Muhammad Rifqi Hidayat')
print('NPM   : 2210010126\n')
print('\n')
print('Program Menghitung Luas')
print('**********************\n')
print('\n')
print('Pilih Menu')
print('=========> 1. Luas Lingkaran')
print('           2. Luas Persergi')
print('           3. Luas Segitiga')
print('\n')
pilihan = int(input("Masukkan Pilihan ="))
print('\n')

if pilihan == 1:
    print('Program Lingkaran')
    print('*******************************\n')
    print('\n')
    jari = float(input('Masukan Jari-Jari :'))
    luas = 3.14*jari*jari
    print('Luas adalah =',luas)
elif pilihan == 2:
    print("Program Persegi Panjang")
    print('=====================\n')
    print('\n')
    panjang = int(input('Input Panjang :'))
    lebar = int(input('Input Lebar :'))
    luas = panjang * lebar
    print('Luas adalah : ',luas)
elif pilihan == 3:
    print("Program Segitiga")
    print('==============\n')
    print('\n')
    a = int(input("Masukkan Alas ="))
    t = int(input("Masukkan Tinggi ="))
    luas = 0.5 * a * t
    print("Luas adalah :", luas)
else:
    print("Pilihan Menu Tidak Ada")