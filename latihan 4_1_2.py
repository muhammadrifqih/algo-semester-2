print('Muhammad Rifqi Hidayat')
print('2210010126')
print('2AReg Pagi Banjarbaru \n')

print("Program Jual Disc")
print('***************/n')
beli = int(input("Total pembelian ="))

match beli:
    case beli if 0 <= beli <= 1000:disc = 100
    case beli if 1001 <= beli <= 10000:disc = 500
    case beli if 10001 <= beli <= 30000:disc = 2000

    case _:
        print("Persediaan tidak mencukupi")

print("\n")
print("Jumlah Pembelian = Rp. ", beli)
print("discount = Rp. ", disc)
print("")
print("Jumlah yang dibayar : Rp. ", beli - disc)