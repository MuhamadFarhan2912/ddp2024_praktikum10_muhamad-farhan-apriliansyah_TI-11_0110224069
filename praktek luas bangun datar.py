from MODUL_luas_bangun_datar import *

def luas_bangun_datar():
    print('\npilih operasi luas bangun datar yang ini dilakukan')
    print('1. luas persegi')
    print('2. luas persegi panjang')
    print('3. luas lingkaran')
    print('4. luas segitiga')
    print('5. luas jajar genjang')

    pilihan=int(input('\nmasukan nomor operasi yang ingin dilakukan (1-5): '))

    if pilihan==1:
        sisi=float(input('Masukan sisi persegi'))
        print('hasil luas persegi: ', luas_persegi(sisi))

    elif pilihan==2:
        panjang=float(input('Masukan panjang'))
        lebar=float(input('Masukan lebar'))
        print('hasil luas persegi panjang: ', luas_persegi_panjang(panjang, lebar))

    elif pilihan==3:
        radius=float(input('Masukan jari jari lingkaran'))
        print('hasil luas lingkaran: ', luas_lingkaran(radius))

    elif pilihan==4:
        alas=float(input('Masukan alas'))
        tinggi=float(input('Masukan tinggi'))
        print('hasil luas segitiga: ', luas_segitiga(alas, tinggi))

    elif pilihan==5:
        alas=float(input('Masukan alas'))
        tinggi=float(input('Masukan tinggi'))
        print('hasil luas lingkaran: ', luas_jajar_genjang(alas, tinggi))
    
    else:
        print(' Pilihan tidak valid, pilih nomor antara 1 dan 5.')


luas_bangun_datar()
