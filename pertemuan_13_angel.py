print ("\nPERTEMUAN 13 - 'VARIABEL LOKAL,GLOBAL, DAN EKSEPSI'\n")
print ("\n===================================================\n")

print ("--- 13.1 Fungsi dengan Variabel Global ---\n")
namaGlobal = "ANGEL" # variabel global
def FungNama(): # mengakses variabel global dalam fungsi
    print(f"=> Fungsi menampilkan {namaGlobal}")
FungNama()

print ("\n--- 13.2 Merubah Variabel Global di dalam Fungsi ---\n")
ang = 0
def UbahAng(angBaru):
    global ang
    ang = angBaru
print (f"=> Angka sebelum diubah : {ang}")
x = UbahAng(15)
print (f"=> Angka setelah diubah : {x}")

print ("\n--- 13.3 Penjebakan Eksepsi ---\n")
inputUser = int(input("=> Masukkan angka : "))
hasil = 0
try:
    hasil = 10/inputUser
except:
    print ("-- INVALID INPUT '0' --")
print (f"=> Hasil : {hasil}")