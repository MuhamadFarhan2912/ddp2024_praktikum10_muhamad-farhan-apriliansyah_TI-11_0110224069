import math

def tambah (a,b):
    return a+b

def kurang (a,b):
    return a-b

def kali (a,b):
    return a*b

def bagi (a,b):
    if b==0:
        return"error:pembagian oleh nol tidak bisa"
    else:
        return a/b
    
def pangkat (a,b):
    return math.pow(a,b)