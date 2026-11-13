print ("\n==== PERTEMUAN 11 ====\n")

print ("-- 11.1 Multi Keys & Nesting Dictionary --\n")
import datetime #biar data bisa dimasukkin tanggal
pasien1 = {
    "nama" : "Pinoeskup",
    "HP": "081111111",
    "BPJS" : False,
    "lahir": datetime.datetime(2000,2,2)
}
pasien2 = {
    "nama" : "Lune",
    "HP": "082222222",
    "BPJS" : True,
    "lahir": datetime.datetime(2003,3,30)
}
pasien3 = {
    "nama" : "dudun",
    "HP": "083333333",
    "BPJS" : True,
    "lahir": datetime.datetime(2001,10,1)
}
dataPasien = {
    "p1" : pasien1,
    "p2" : pasien2,
    "p3" : pasien3
}
for pasien in dataPasien:
    KEY1 = pasien 
    NAMA = dataPasien[KEY1]["nama"]
    HP = dataPasien[KEY1]["HP"]
    BPJS = dataPasien[KEY1]["BPJS"]
    LAHIR = dataPasien[KEY1]["lahir"].strftime("%x")

    print(f"{KEY1:<6} {NAMA:<17} {HP:<3} {BPJS:<9} {LAHIR:<10}")
    
print ("\n---\n")

print ("\n--- 11.2 & 11.3 dictionary ---\n")
import datetime
import os
import string
import random
Mahtemp = {
    "Nama" : "Nama",
    "nim" : 000000,
    "sks" : 00,
    "lahir" : datetime.datetime(1111,11,11)
}
dataMahasiswa = {}
while True:
    os.system("clear")
    print (f"{"WELCOME":^20}")
    print (f"{"DATA MAHASISWA":^20}")
    print ("-"*20)
    Mahasiswa = dict.fromkeys(Mahtemp.keys())
    Mahasiswa["Nama"] = input("Nama : ")
    Mahasiswa["nim"] = int(input("NIM : "))
    Mahasiswa["sks"] = int(input("SKS : "))
    tahun = int(input("Tahun lahir : "))
    bulan = int(input("Bulan lahir : "))
    tanggal = int(input("Tanggal lahir : "))
    Mahasiswa["lahir"] = datetime.datetime(tahun,bulan,tanggal)

    KEY = "".join((random.choice(string.ascii_uppercase)for i in range(6))) #buat randomize key
    dataMahasiswa.update({KEY:Mahasiswa})
    
    print (f"\n{"KEY":<6} {"Nama":<17} {"NIM":<8} {"SKS":<10} {"Tanggal Lahir":<10}")
    print ("-"*50)
    for mahasiswa in dataMahasiswa:
        NAME = dataMahasiswa[KEY]["Nama"]
        NIM = dataMahasiswa[KEY]["nim"]
        SKS = dataMahasiswa[KEY]["sks"]
        LAHIR = dataMahasiswa[KEY]["lahir"].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
    print ("\n")
    isDone = input("lanjutkan/end? ")
    if isDone == "end":
        break