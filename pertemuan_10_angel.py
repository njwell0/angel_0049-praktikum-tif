print ("\nPERTEMUAN 10 'TUPLES, SET, DICTIONARY'\n")
print ("=======================================")

#10.1
print ("\n10.1 Tuples dan Set\n")
tuples = (9,7,8,2,3)
print (f"ini contoh tuple --> {tuples}") #gabisa diganti pakai "tuple [1] = 9" karena sifatnya tetap
print (f"\n=> memanggil data dalam index {tuples[2]}") #gabisa dipanggil pake append[1]
print ("\n---")
print ("SET (himpunan)")
sets = {10,2,9,7,8,7,2}
print (f"ini contoh data SET --> {sets}") #angka gaboleh duplikat jadi kalo ada yg double cuma diprint sekali

print ("\n=====\n")
#10.2
print ("\n10.2 Dictionary\n")
CukingKomplek = {
    "blokA":"MOCCHI",
    "blokB":"DUBBAI",
    "blokC":"SNOWY",
    "blokD":"LILLO"
}
print (f"ini data cuking --- \n{CukingKomplek}")
print (f"\n=> cuking di blokB {CukingKomplek["blokB"]}")
print (f"=> cuking di blokD {CukingKomplek["blokD"]}")

print ("\n=====\n")
#10.3
print ("\n10.3 Operasi Dictionary\n")
DataUmur = {
    "seto": 20,
    "joeng": 23,
    "ajeng": 55,
    "joko": 39
}
print (f"data umur --- \n{DataUmur}")
panjangData = len(DataUmur) #mengetahui panjang data
print (f"\n=> panjang data diatas {panjangData}\n")
KEY = "seto"
CHECKKEY = KEY in DataUmur #cek key data
print(f"=> apakah {KEY} ada di data_dict: {CHECKKEY}\n")
print ("=> mengakses data pakai .get")
print(DataUmur["ajeng"])
print(DataUmur.get("ajeng"))
print(DataUmur.get("kisya","key tidak ditemukan\n"))
print ("=> mengupdate data")
DataUmur["seto"] = "30"
print(DataUmur)
print ("\n=> menambah data")
DataUmur.update ({"wisnu":32})
print (DataUmur)
print ("\n=> menghapus data")
del DataUmur ["joko"]
print (DataUmur)

print ("\n=====\n")
#10.4
print ("\n10.4 Perulangan Dictionary\n")
Ipop = {
    "SEEN":"Dndy",
    "CHNCE":"Sandy",
    "NONA":"Christy",
    "V1RST":"Jessica"
}
print (Ipop)
print ("\n=> menampilkan keys nya aja --- ")
for grup in Ipop.keys(): #nampilin key
    print (f"list Ipop group {grup}")
print ("\n=> menampilkan value nya aja --- ")
for nama in Ipop.values(): #nampilin value
    print (f"nama artis {nama}")
print ("\n=> nampilin semua --- ")
for semua in Ipop.items():
    print (semua)
print ("\n=> nampilin semua lebih rapi --- ")
for grup,nama in Ipop.items():
    print (f"grup : {grup} --- anggota : {nama}")
 