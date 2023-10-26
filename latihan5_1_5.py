print("Nama  : Muhammad Rifqi Hidayat")
print("NPM   : 2210010126\n")

print("Program Membalik Kata dari Belakang")
print("*********************************\n")

kata = input("Tulis kata yang akan dibalik = ")

balik = " "
for i in kata:
    balik = i + balik
print("Hasilnya :", balik)
