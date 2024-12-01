from MODUL_aritmatika import *

def hitungan_aritmatika():
    print('\nPilih operasi aritmatika yang ingin dilakukan')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Pangkat')
    
    pilihan = int(input('\nMasukkan nomor operasi aritmatika yang dipilih (1-5): '))
    
    if pilihan == 1:
        a = float(input('Masukkan angka pertama: '))
        b = float(input('Masukkan angka kedua: '))
        print('Hasil penjumlahan: ', tambah(a, b))
    elif pilihan == 2:
        a = float(input('Masukkan angka pertama: '))
        b = float(input('Masukkan angka kedua: '))
        print('Hasil pengurangan: ', kurang(a, b))
    elif pilihan == 3:
        a = float(input('Masukkan angka pertama: '))
        b = float(input('Masukkan angka kedua: '))
        print('Hasil perkalian: ', kali(a, b))
    elif pilihan == 4:
        a = float(input('Masukkan angka pertama: '))
        b = float(input('Masukkan angka kedua: '))
        print('Hasil pembagian: ', bagi(a, b))
    elif pilihan == 5:
        a = float(input('Masukkan angka pertama: '))
        b = float(input('Masukkan angka kedua: '))
        print('Hasil pangkat: ', pangkat(a, b))
    else:
        print('Pilihan tidak valid')

# Memanggil fungsi untuk menjalankan
hitungan_aritmatika()
