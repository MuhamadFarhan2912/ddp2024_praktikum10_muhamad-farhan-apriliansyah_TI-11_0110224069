import math

def volume_kubus(sisi):
    return sisi ** 3
def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def volume_tabung(radius, tinggi):
    return math.pi * radius ** 2 * tinggi
def luas_permukaan_tabung(radius, tinggi):
    return 2 * math.pi * radius * (radius + tinggi)

def volume_kerucut(radius, tinggi):
    return (1/3) * math.pi * radius ** 2 * tinggi
def luas_permukaan_kerucut(radius, tinggi):
    s = math.sqrt(radius ** 2 + tinggi ** 2)
    return math.pi * radius * (radius + s)

def volume_prisma_segitiga(alas, tinggi_alas, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_alas
    return luas_alas * tinggi_prisma
def luas_permukaan_prisma_segitiga(alas, tinggi_alas, tinggi_prisma):
    keliling_alas = 3 * alas
    luas_alas = 0.5 * alas * tinggi_alas
    return 2 * luas_alas + keliling_alas * tinggi_prisma