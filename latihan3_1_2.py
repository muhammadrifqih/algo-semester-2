print('Nama  : Muhammad Rifqi Hidayat')
print('NPM   : 2210010126\n')
print('\n')
print("Program Menentukan Bilangan yang Terbesar")
print("***************************************\n")
a = int(input("masukkan bilangan ke 1 ="))
b = int(input("masukkan bilangan ke 2 ="))
c = int(input("masukkan bilangan ke 3 ="))

print('\n')

if(a > b) and (a > c):
    print("Bilangan ke 1 Paling Besar")
elif(b > a) and (b > c):
    print("Bilangan ke 2 Paling Besar")
elif(c > a) and (c > b):
    print("Bilangan ke 3 Paling Besar")
else:
    print("ada dua atau tiga masukan memiliki nilai sama")