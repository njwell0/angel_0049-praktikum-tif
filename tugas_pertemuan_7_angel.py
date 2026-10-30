#TUGAS 9
print ("\nTUGAS PERTEMUAN 9 -- ARCHANGELA GIRLANI SEKAR SABAT -- 2605060049\n")
print ("-- 1 --\n")
kendaraan = ["motor","mobil","sepeda","bus"]
print (kendaraan)
###
#tambahkan "truk" di akhir list
kendaraan.append("truk")
print (f"\na. menambahkan 'truk' di akhir = \n{kendaraan}\n")
#sisipkan 'becak' di index-1
kendaraan.insert(1,"becak")
print (f"b.sisipkan 'becak di index-1 = \n{kendaraan}\n")
#hapus data belakang
kendaraan.pop()
print (f"c. menghapus data terakhir = \n{kendaraan}\n")
#mengubah 'sepeda' jadi 'skuter'
kendaraan[2] = "skuter"
print (f"d. mengubah sepeda jadi skuter = \n{kendaraan}\n")
#informasi jumlah data dalam list
jumlahKendaraan = len(kendaraan)
print (f"e. jumlah data dalam list kendaraan = \n{jumlahKendaraan}\n")

print ("\n-- 2 --\n")
angka = [75,80,90,75,85,100,65]
print (angka)
###
#mengetahui index angka 100
in100 = angka.index(100)
print (f"\na. 100 berada di index ke {in100}\n")
#menghitung berapa banyak nilai 75
nilai75 = angka.count(75)
print (f"b. yang mendapat nilai 75 ada = {nilai75} siswa\n")
#mengurutkan skor ujian
skor_ujian = angka.sort()
print (f"c. urutan skor ujian = \n{skor_ujian}\n")
#balikkan urutan skor ujian
skor_balik = angka.reverse()
print(f"d. membalikkan urutan skor ujian = \n{skor_balik}\n")

print ("\n-- 3 --\n")
menu_utama = ["Nasi Goreng","Mie Ayam"]
menu_tambahan = ["Kerupuk","Es Teh"]
print (menu_utama)
print (menu_tambahan)
#menggabungkan list
menuGab = [menu_utama,menu_tambahan]
print (f"menu gabungan = \n{menuGab}")

print ("\n-- 4 --\n")
data_barang = [["buku",5000],["pensil",2000],["penggaris",3000]]
###
#enampilkan harga pensil
print (f"a. harga pensil = {data_barang[1][1]}")
#menampilkan dta satu persatu
print ("b. membaca data satu per satu")
for alattulis in data_barang:
    print (f"Nama\t: {alattulis[0]}")
    print (f"Harga\t: {alattulis[1]}")
