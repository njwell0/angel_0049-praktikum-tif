#PERTEMUAN 5 "PERULANGAN DAN KONTROL ALUR"

print ("\n=====FOR=====\n")
#5.1 program FOR
angka1a = 1
print (angka1a)
angka1a = angka1a + 1
print (angka1a)
angka_1a = angka1a + 1
print (angka1a)

#FOR kondisi:
#    aksi
#dengan list angka
angkalistb = [0,1,2,3,4]
print (angkalistb)
for i in angkalistb:
    print (i)
print ("end program\n")

#dengan range
angka1c = range (10)
for i in angka1c:
    print(i)
print ("end program\n")
angka1d = range (1,10)
for i in angka1d:
    print (i)
print ("end program\n")

#versi string
str1 = "i love Ryul"
for huruf in str1:
    print(huruf)
print("end program\n")

#5.2 WHILE LOOP
print ("=====WHILE=====\n")
print ("---contoh 1---\n")
angka2a = 15
while angka2a >10:
    print ("CUKING")
    angka2a = angka2a + 1

print ("---contoh 2---\n")
angka2b = 0
print (angka2b)
while angka2b < 3:
    angka2b += 1 #angka + 1
    print (angka2b)
    print ("KUCING")
print ("end program\n")

#5.3 CONTINUE, PASS

#pass = sebagai dummy
angka3a = 0
while angka3a <3:
    angka3a = angka3a + 1

    if (angka3a == 2):
        pass
    print (angka3a)

#continue 
angka3b = 0
print (angka3b)
while angka3b <5:
    angka3b = angka3b + 1
    print (angka3b)

    if (angka3b == 3):
        print ("gudd")
        continue
    print ("uda benerr wuw:p")

#5.4 BREAK 

angka4a = 0
print (angka4a)
while angka4a <7:
    angka4a = angka4a + 1
    print (angka4a)

    if (angka4a == 5):
        print ("cukuppp")
        break 
    print ("yg ini gabisa")

#5.5 LATIHAN PERULANGAN
#bikin segitiga 

#pakai FOR
sisi1 = 4
count1 = 1
for i in range (sisi1):
    print ("*" * count1)
    count1 += 1

#pakai while 
sisi2 = 4
count2 = 1
while True:
    print ("*" * count2)
    count1 += 1
    if count2 > sisi2:
        break
print ("doneee")
