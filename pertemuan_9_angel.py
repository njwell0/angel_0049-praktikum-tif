#OPERASI DAN MANIPULASI LIST

print ("\n9.1 LIST\n") # 9.1 list
print ("---angka---") #data angka
data_angka = [1,3,6,2]
print (data_angka)
###
print ("---string---") #data string
data_string = ["dandy","jason","noel","bian"]
print (data_string)
###
print ("---boolean---") #data boolean
data_boolean = [True, False, True, False]
print (data_boolean)
###
print ("---campuran---") #data campuran
data_campur = [5, "angel", 10, True, "aduh", False]
print (data_campur)
###
print ("---list pake for---")
listFor = [i **2 for i in range (0,10)] #bikin list pake "for"
print (listFor)
###
print ("---list pake for if---") #bikin list pae for if
listForIf = [i for i in range (0,10) if 1 !=5] #syarat if bebas
print (listForIf)
print ("\n============================\n")

print ("\n9.2 OPERASI LIST\n") 
dessert = ["cuwi kuki","kuki","moci"] #list menu dessert
###
pilihdessert = dessert[0]
print (f"dessert pertama = {pilihdessert}") #mengambil data dari list
###
dessertTerakhir = dessert[-1]
print (f"dessert terakhir = {dessertTerakhir}") #mengambil data terakhir dari list
###
jumlahDessert = len(dessert)
print (f"jumlah dessert = {jumlahDessert}") #mengetahui jumlah data dalam list

print ("\n---manipulasi data---")
dessert.insert (1, "crepes") #menambahkan data ke dalam index tertentu
print (f"dessert setelah ditambah = \n{dessert}")
###
dessert.append ("matcha") #menambah data di akhir
print (f"dessert setelah ditambah lagi = \n{dessert}")
dessertNew = ["chocobar","cheesecake","lavacake"] #data baru
dessert.extend (dessertNew)
print (f"penggabungan dessert = \n{dessert}")
###
dessert[0] = "pie" #mengganti/merubah data
print (f"perubahan dessert = \n{dessert}")
###
dessert.remove ("moci") #menghapus data
print (f"menghapus dessert = \n{dessert}")
###
dessert.pop() #menghapus data terakhir 
print (f"menghapus dessert terakhir = \n{dessert}")

print ("\n9.2 OPERASI LIST\n")
angka = [1,3,3,2,4,5,2,2,4,4,5,1]
CHNCE = ["sandy","soni","aji","fiki"]

jumlah2 = angka.count(2) #menghitung data
print (f"jumlah angka 2 = {jumlah2}")
###
soni = CHNCE.index("soni") #mengetahui index data
print (f"index si soni = {soni}")
###
angka.sort()
print (f"angka diurutkan = {angka}")
angka.reverse()
print (f"angka dibalik = {angka}")

print ("\n9.3 NESTED LIST\n")
absen1 = ["Esther", 25, "Perempuan"]
absen2 = ["Baila", 20, "Perempuan"]
absen3 = ["Darren", 21, "Laki-laki"]
absen4 = ["Valen", 22, "Laki-laki"]

absensi = [absen1, absen2, absen3, absen4] #gabungin list
print(f"absen = {absensi}")
###
for murid in absensi: #misahin data dalam list
    print (f"nama\t: {murid[0]}")
    print (f"umur\t: {murid[1]}")
    print (f"gender\t: {murid[2]}\n")
