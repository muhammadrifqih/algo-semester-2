print('Muhammad Rifqi Hidayat')
print('2210010126')
print('2AReg Pagi Banjarbaru \n')

print('Program penghitungan')
print("********************\n")
print("\n")

print('Pilih Menu')
print('=========> 1. Penjumlahan')
print('=========> 2. Pengurangan')
print('=========> 3. Pengkalian')
print('=========> 4. Pembagian')
print('\n')
pilih = int(input("Masukan Pilihan :"))
a = int(input('Nilai Pertama :'))
b = int(input('Nilai Kedua :'))
print("\n")

match pilih:
    case 1:
        print("Penjumlahan\n")
        print("Hasil = ",a+b)
    case 2:
        print("Pengurangan\n")
        print("Hasil = ",a-b)
    case 3:
        print("Pengalian")
        print("Hasil = ",a*b) 
    case 4:
        print("Pembagian")
        print("Hasil = ",a/b)
    case _:
        print("Pilihan Tidak Ada")
        print("\n")