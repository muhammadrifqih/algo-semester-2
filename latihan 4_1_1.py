print('Muhammad Rifqi Hidayat')
print('2210010126')
print('2AReg Pagi Banjarbaru \n')

print("Program memeriksa hari dalam bulan Maret 2012")
print("*********************************************\n")

tgl = int(input("Masukan Tanggal : "))

match tgl:
    case 5|12|19|26:print("Hari Senin")
    case 6|13|20|27:print("Hari Selasa")
    case 7|14|21|28:print("Hari Rabu")
    case 1|8|15|22|29:print("Hari kamis")
    case 2|9|16|23|20:print("Hari Jumat")
    case 3|10|17|24|31:print("Hari Sabtu")
    case 4|11|18|25:print("Hari Minggu")
    case _:
        print("Maaf tidak ada tanggal tersebut")