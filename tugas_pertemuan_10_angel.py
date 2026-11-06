print ("\nTUGAS PERTEMUAN 10 - TUPLES, SET, DICTIONARY\n")
print ("=========================================")

print ("\n-- 1 TUPLE --\n")
print ("\na. Membuat biodata") #soal a
biodata = ("Archangela Girlani Sekar Sabat", 2605060049, "S1 Teknologi Informasi")
print (biodata)
print ("\nb. Menampilkan NIM dan Prodi") #soal b
print (f"NIM : {biodata[1]}")
print (f"Prodi : {biodata[2]}")
print ("\nc. Mengapa code error?") #soal c
#biodata[2] = "teknologi informasi" 
print ("code 'biodata[2] = teknologi informasi' akan error karena di jenis data Tuple memiliki sifat immutable atau bersifat tetap dan tidak dapat dirubah")
print ("\nd. Mengapa angka 10 dan 4 hanya muncul sekali?") #soal d
NilaiAngka = {10,4,3,2,4,10,7,5}
print (NilaiAngka)
print ("Pada data diatas nilai 4 dan 10 hanya ditampilkan sekali karena jenis data 'SET' tidak memperbolehkan adanya duplikat data")

print ("\n-- 2 MANIPULASI DICTIONARY --\n")
print ("\na. Membuat data mahasiswa") #soal a
DataMahasiswa = {"NIM":"240101","NAMA":"Budi Santoso","PRODI":"Teknologi Informasi"}
print (DataMahasiswa)
print ("\nb. Mengganti prodi dan menambah data Angkatan") #soal b
DataMahasiswa ["PRODI"] = "Sastra Mesin" #mengganti value dari key prodi
DataMahasiswa.update ({"ANGKATAN":"2026"}) #menambah key angkatan
print (DataMahasiswa)
print ("\nc. Menghapus data NIM") #soal c  
del DataMahasiswa["NIM"]
print (DataMahasiswa)

print ("\n-- 3 PERULANGAN DICTIONARY --\n")
print ("\na. Membuat DICT keranjang") #soal a
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print (keranjang)

print ("\nb. Menampilkan Buah dan Harganya") #soal b
for buah,nominal in keranjang.items():
    print (f"Harga {buah}, = Rp.{nominal}")

print ("\nc. Menjumlah total belanja") #soal c
TotalHarga = 0
for harga in keranjang.items():
    TotalHarga += nominal
print (f"Total Belanja : Rp.{TotalHarga}")
