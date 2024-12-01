from MODUL_luas_bangun_ruang import *

print('\nPilih operasi luas atau volume bangun ruang yang ingin dilakukan:')
print('1. Volume dan Luas Permukaan Kubus')
print('2. Volume dan Luas Permukaan Balok')
print('3. Volume dan Luas Permukaan Tabung')
print('4. Volume dan Luas Permukaan Kerucut')
print('5. Volume dan Luas Permukaan Prisma Segitiga')

pilihan = int(input('\nMasukkan nomor operasi yang ingin dilakukan (1-5): '))

if pilihan == 1:
    sisi = float(input('Masukkan sisi kubus: '))
    print('Volume kubus: ', volume_kubus(sisi))
    print('Luas permukaan kubus: ', luas_permukaan_kubus(sisi))

elif pilihan == 2:
    panjang = float(input('Masukkan panjang balok: '))
    lebar = float(input('Masukkan lebar balok: '))
    tinggi = float(input('Masukkan tinggi balok: '))
    print('Volume balok: ', volume_balok(panjang, lebar, tinggi))
    print('Luas permukaan balok: ', luas_permukaan_balok(panjang, lebar, tinggi))

elif pilihan == 3:
    radius = float(input('Masukkan radius tabung: '))
    tinggi = float(input('Masukkan tinggi tabung: '))
    print('Volume tabung: ', volume_tabung(radius, tinggi))
    print('Luas permukaan tabung: ', luas_permukaan_tabung(radius, tinggi))

elif pilihan == 4:
    radius = float(input('Masukkan radius kerucut: '))
    tinggi = float(input('Masukkan tinggi kerucut: '))
    print('Volume kerucut: ', volume_kerucut(radius, tinggi))
    print('Luas permukaan kerucut: ', luas_permukaan_kerucut(radius, tinggi))

elif pilihan == 5:
    alas = float(input('Masukkan panjang alas segitiga: '))
    tinggi_alas = float(input('Masukkan tinggi segitiga: '))
    tinggi_prisma = float(input('Masukkan tinggi prisma: '))
    print('Volume prisma segitiga: ', volume_prisma_segitiga(alas, tinggi_alas, tinggi_prisma))
    print('Luas permukaan prisma segitiga: ', luas_permukaan_prisma_segitiga(alas, tinggi_alas, tinggi_prisma))

else:
    print('Pilihan tidak valid, pilih nomor antara 1 dan 5.')
