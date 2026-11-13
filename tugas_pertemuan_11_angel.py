print ("\nTUGAS PERTEMUAN 11\n")
print ("-----------------------")

import datetime
import os
import string
import random

BukuTemp = {
    "judul" : "JUDUL BUKU",
    "penulis" : "PENULIS",
    "tahun" : 0000,
    "tanggal" : datetime.datetime(1111,10,1),
    "status" : "TERSEDIA/TIDAK"
}
DataBuku = {}
while True:
    os.system("clear")
    print ("\nWELCOME TO LIBRARY\n")
    print ("-"*50)
    buku = dict.fromkeys(BukuTemp.keys())
    buku["judul"] = input("Judul Buku : ")
    buku["penulis"] = input("Nama Penulis : ")
    buku["tahun"] = int(input("Tahun Terbit Buku : "))
    tahun = int(input("tahun pinjam : "))
    bulan = int(input("bulan pinjam : "))
    tanggal = int(input("tanggal pinjam : "))
    buku["tanggal"] = datetime.datetime(tahun,bulan,tanggal)
    buku["status"] = input("tersedia/tidak : ")
    KEY = "".join((random.choice(string.ascii_uppercase)for i in range(6))) #buat randomize key
    DataBuku.update({KEY:buku})

    print (f"\n{"KEY":<6} {"JUDUL":<20} {"PENULIS":<10} {"TAHUN":<10} {"TANGGAL":<10} {"STATUS":<5}")
    print ("-"*75)

    for k, v in DataBuku.items():
        JUDUL = v["judul"]
        PENULIS = v["penulis"]
        TAHUN = v["tahun"]
        TANGGAL = v["tanggal"].strftime("%Y/%m/%d")
        STATUS = v["status"]
        print (f"\n{k:<6} {JUDUL:<20} {PENULIS:<10} {TAHUN:<10} {TANGGAL:<10} {STATUS:<5}")
    print ("-"*75)
    isDone = input("tambah buku? ")
    if isDone == "end":
        break