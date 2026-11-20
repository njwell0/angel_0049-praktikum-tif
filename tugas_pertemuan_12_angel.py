print ("\nTUGAS PERTEMUAN 12\n")
print ("\n==================================================================\n")
def luasPersegiPanjang(p,l):
    LPP = p*l
    return LPP

def volumePersegiPanjang(L,t):
    VPP = L*t
    return VPP
    
def luasLingkaran(r):
    phi = 3.14
    LL = phi*(r*r)
    return LL

def volumeBola(r):
    phi = 3.14
    VB = 3/4 * phi * (r**3)
    return VB

print ("\na. menghitung Luas Persegi Panjang\n")
panjang = float(input("=> masukkan panjang persegi panjang : "))
lebar = float(input("=> masukkan lebar persegi panjang : "))
LuasPP = luasPersegiPanjang(panjang,lebar)
print (f"--- Luas Persegi Panjang = {LuasPP}\n")

print ("\nb. menghitung Volume Persegi Panjang\n")
luas = luasPersegiPanjang
luasper = float(input("=> masukkan luas persegi panjang : "))
tinggi = float(input("=> masukkan tinggi persegi panjang : "))
VolPP = volumePersegiPanjang(luasper,tinggi)
print (f"--- Volume Persegi Panjang = {VolPP}")

print ("\nc. menghitung Luas Lingkaran\n")
jari1 = float(input("=> masukkan jari-jari lingkaran : "))
luasLing = luasLingkaran(jari1)
print (f"--- Luas Lingkaran = {luasLing}")

print ("\nd. menghitung volume bola\n")
jari2 = float(input("=> masukkan jari-jari bola : "))
VolBol = volumeBola(jari2)
print (f"--- Volume Bola = {VolBol}\n")
