print('========SEGAR MANIS========')
print('\n')

print('Buah Segar')
print('---------> 1.Kiwi')
print('---------> 2.Mangga')
print('---------> 3.Alpukat')
print('---------> 4.Apel\n')

# Input
plh2 = input('Pilih Buah                 :')
plh = plh2.lower()
kg = int(input('Berapa Kg Buah Yang di Beli :'))

print('\n')
# Perulangan 
match plh :
    case 'kiwi' :
        nb = 'Kiwi'
        h = (kg*10000)
        if kg > 5 :
            nb = 'Kiwi'
            h = (kg*10000)-(0.05*kg*10000)
        if kg > 20 :
            h -= h * 0.07
    case 'mangga' :
        nb = 'Mangga'
        h = (kg*15000)
        if kg > 5 :
            nb = 'Mangga'
            h = (kg*15000)-(0.025*kg*15000)
        if kg > 20 :
            h -= h*0.07
    case 'alpukat' :
        nb = 'Alpukat'
        h = (kg*20000)
        if kg > 5 :
            nb = 'Alpukat'
            h = (kg*20000)-(0.07*kg*20000)
            if kg > 10 :
                gif = 'Payung Cantik'
    case 'apel' :
        nb = 'Apel'
        h = (kg*25000)
        if kg > 5 :
            nb = 'Apel'
            h = (kg*25000)-(0.1*kg*15000)
            if kg > 15 :
                gif = 'Tas Lucu'


# Output
print('========SEGAR MANIS========')
print('---------------------------\n')
print('Nama Buah                 : ',nb)
print('Jumlah Berat /kg          : ',kg)
print('Total Harga Yang di bayar : ',h)
print('Hadiah Cantik             : ',gif)