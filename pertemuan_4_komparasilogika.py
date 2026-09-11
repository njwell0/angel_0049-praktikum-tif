#4.1 LOGICAL
print ("n/OPERASI LOGIKA ATAU BOOLEANn/")

#NOT
print ("===NOT===")
love = True
hate = not love
print ('ily =',love)
print ("=== NOT")
print ('bye =',hate)

#OR (jika salah satu true hasilnya true)
print ("===OR===")
apel = False
jeruk = False
jus = apel or jeruk
print (apel,'or',jeruk,'=',jus)
apel = False
jeruk = True
jus = apel or jeruk
print (apel,'or',jeruk,'=',jus)
apel = True
jeruk = False
jus = apel or jeruk
print (apel,'or',jeruk,'=',jus)
apel = True
jeruk = True
jus = apel or jeruk
print (apel,'or',jeruk,'=',jus)

#AND (keduanya true hasilnya true)
print ("===AND===")
aku = False
kamu = False
AK = aku and kamu
print (aku,'and',kamu,'=',AK)
aku = False
kamu = True
AK = aku and kamu
print (aku,'and',kamu,'=',AK)
aku = True
kamu = False
AK = aku and kamu
print (aku,'and',kamu,'=',AK)
aku = True
kamu = True
AK = aku and kamu
print (aku,'and',kamu,'=',AK)

#XOR (true jika salah satu true)
print ("===XOR===")
makan = False
minum = False
jadi = makan ^ minum
print (makan,'xor',minum,'=',jadi)
makan = False
minum = True
jadi = makan ^ minum
print (makan,'xor',minum,'=',jadi)
makan = False
minum = True
jadi = makan ^ minum
print (makan,'xor',minum,'=',jadi)
makan = True
minum = True
jadi = makan ^ minum
print (makan,'xor',minum,'=',jadi)

#4.2 LOGIKA DAN KOMPARASI
print ("n/LOGIKA DAN KOMPARASIn/")

#++++++5------10++++++
angka = int(input("masukan angka /nkurang dari 5/natau /nlebih besar dari 10/n:"))
#kurang dari 5
kurang = (angka <5)
print ("Kurang Dari 5 =",kurang)

#lebih dari 10
lebih = (angka >10)
print ("Lebih Dari 10 =",lebih)
correct = kurang or lebih
print ("angka yang anda masukkan",correct)

#4.3 IF AND ELSE 
nama = input("tuliskan nama anda : ")

#1. if inline
if nama =="angel":
    print ("CAKEEUPPP")
    print ("end program")

#2. else 
else:
    print ("paan luwh")
    print ("end program")


#4.4 ELIF

nama = input("siapa nama anjing anda? ")
if nama =="blacky":
    print ("hitam")
elif nama =="brownie":
    print ("coklat")
elif nama =="snowy":
    print ("putih")
else:
    print ("belum terdata")
    print ("end program")

    