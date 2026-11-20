print ("\nPERTEMUAN 12\n")
print ("\n=== FUNCTION ===\n")

print ("--- 12.1 pengenalan fungsi ---\n") #void function
def hello_guys():
    print ("hi vlog welcome to my guys")
    print ("like")
    print ("comment")
    print ("subscribe")
hello_guys() #memanggil fungsi

print ("\n --- 12.2 fungsi dengan argumen ---\n")
print ("1. \n")
def sapa (nama1):
    print (f"welcome our new fella, {nama1}")
sapa("angel") #memanggil fungsi + argumen

print ("\n2. parameter penjumlahan \n")
def penjumlahan (ang1, ang2):
    hasilplus = ang1 + ang2 
print ("hasil dari 4+3 = ")
penjumlahan (4,3)

print ("\n3. parameternya array \n")
def ukt(list):
    data = list.copy()
    for peserta in list:
        print (f"{peserta}, BAYAR UKT!!")
dataMah = ["dudun","bambang","seto"]
ukt(dataMah)

print ("\n --- 12.3 fungsi denga return ---\n")
print ("1. menghitung kuadrat \n")
def kuadrat(angka):
    hasilKuadrat = angka ** 2
    return hasilKuadrat
k1 = kuadrat(8) 
k2 = 100 + kuadrat(2)
print(f"8 kuadrat adalah = {k1}")
print(f"hasil dari 100 + 2 kuadrat adalah = {k2}")

print ("\n 2. fungsi tambah di return \n")
def ftambah(angka1, angka2):
    return angka1 + angka2
x = ftambah(20,12)
print(f"hasil 20 + 12 = {x}")

print ("\n 2. operasi matematika \n")
def operasimtk(angA, angB):
    tambah = angA+angB
    kurang = angA-angB
    kali = angA*angB
    bagi = angA/angB
    return tambah,kurang,kali,bagi

a,b,c,d = operasimtk(100,10)
print ("hasil operasi (100,10)")
print (f"a. hasil tambah = {a}")
print (f"b. hasil kurang = {b}")
print (f"c. hasil kali = {c}")
print (f"d. hasil bagi = {d}")

print ("\n --- 12.4 default argumen fungsi --- \n")
print ("1. kalau fungsi 'hai' ada defaultnya\n")
def hai(nama = "ohyul"):
    print (f"haii {nama}")
print ("a. parameter 'angel'")
hai("angel")
print ("b. parameter default")
hai()

print ("\n2. kalau fungsi menyimpan pesan \n")
def menyapa(nama2, pesan = "whats good?"):
    print (f"hai {nama2}, {pesan}")
print ("a. kalau parameter diubah")
menyapa("dandy","udah makan belum?")
print ("b. kalau parameter default")
menyapa("christy")

print ("\n3. kalau fungsi menyimpan pesan \n")
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil
print(f"a. 2 pangkat 4 = {hitung_pangkat(2,4)}")
hasil = hitung_pangkat(pangkat=2, angka=10)
print(f"b. 10 pangkat 2 = {hasil}")

print ("\n4. kalau fungsi menyimpan banyak nilai \n")
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil
print(f"a. hasil faktorial default {faktorial()}")
print(f"b. hasil faktorial input {faktorial(input_3 = 10)}")