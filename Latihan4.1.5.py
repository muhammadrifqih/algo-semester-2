print('Muhammad Rifqi Hidayat')
print('2210010126')
print('2AReg Pagi Banjarbaru \n')
import time;

print('========SEGAR MANIS========')
print('\n')
print('Buah Segar')
print('---------> 1.Kiwi')
print('---------> 2.Mangga')
print('---------> 3.Alpukat')
print('---------> 4.Apel\n')

# Input
plh = str.lower(input('Pilih Buah                 :'))
kg = int(input('Berapa Kg Buah Yang di Beli :'))

print('\n')
# Perulangan 
match plh :
    case 'kiwi' | '1' :
        nb = 'Kiwi'
        per = 0.05
        hrg = 10000
        gif = '-'
    case 'mangga' | '2' :
        nb = 'Mangga'
        per = 0.025
        hrg = 15000
        gif = '-'
    case 'alpukat' | '3' :
        nb = 'Alpukat'
        per = 0.07
        hrg = 20000
        gif = '-'
    case 'apel' | '4':
        nb = 'Apel'
        per = 0.1
        hrg = 25000
        gif = '-'

h = (kg*hrg)
if (plh == 'kiwi' or plh == 'mangga' or plh == '1' or plh == '2') and (kg > 5 ):
    h = (kg*hrg)-(per*kg*hrg)
elif (plh == 'alpulkat' or plh == '3') and (kg > 10):
    gif = 'Payung cantik'
elif (plh == 'apel' or plh == '4') and (kg > 15) :
    gif = 'Tas Lucu'
# Output
print('========SEGAR MANIS========')
print('---------------------------')
print(time.asctime( time.localtime(time.time()) ),'\n')
print('Nama Buah                 : ',nb)
print('Jumlah Berat /kg          : ',kg)
print('Total Harga Yang di bayar : ',h)
print('Hadiah Cantik             : ',gif)