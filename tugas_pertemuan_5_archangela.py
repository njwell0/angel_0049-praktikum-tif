print ("\nTUGAS PERTEMUAN 3 'PERULANGAN DAN KONTROL ALUR'\n")

print ("==========================")
print ("\nNOMER 1\n")
#tugas 1
angka1 = 1
while angka1 <=50:
    print(angka1)
    angka1 += 1
print ("end program\n")

print ("==========================")
print ("\nNOMER 2\n")
#tugas 2
angka2 = 2
while angka2 <=100:
    pembagi = 2
    prima = True
    while pembagi <angka2:
        if angka2 % pembagi == 0:
            prima = False
            pembagi += 1
        if prima:
            print(angka2)
        angka2 += 1