#TUGAS PERTEMUAN 3

#a. menghitung Luas,Keliling, dan Volume bangunan
#ukuran sebuah bangunan
panjang = 12
lebar = 5
tinggi = 8

#menghitung luas bangunan 
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print ("luas =", luas)
#mengitung Keliling bangunan
keliling_rusuk = 4 * (panjang + lebar)
print ("keliling =", keliling_rusuk)
#menghitung volume 
volume = panjang * lebar * tinggi
print ("volume =", volume)

#b. Apakah luas bangunan lebih luas dari 50?
luas = luas > 50
print (luas, '>' ,50, '=' ,luas)

#c. Apakah volume tersebut bernilai 480?
volume = volume == 480
print (volume, '==' ,480, '=' ,volume)