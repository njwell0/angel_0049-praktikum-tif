#3.1 operasi aritmatika 
print ("\nOPERASI ARITMATIKA\n")
a = 5
b = 10

#operasi tambah 
tambah = a + b
print (a, '+' ,b,'=',tambah)
#operasi kurang 
kurang = b - a 
print (b,'-',b,'=',kurang)
#operasi perkalian 
kali = a * b
print (a,'*',b,'=',kali)
#operasi pembagian
bagi = b / a
print (b,'/',b,'=',bagi)
#pangkat
pangkat = b ** a
print (b,'**',a,'=',pangkat)

#3.2 konversi celcius ke satuan lainnya
print ("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('suhu dalam celcius:'))
print ("suhu adalah", celcius, "celcius")
#konversi reamur 
reamur = (4/5) * celcius
print ("suhu dalam reamur adalah", reamur, "reamur")
#konversi fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print ("suhu dalam fahrenheit", fahrenheit, "fahrenheit")
#konversi kelvin
kelvin = celcius + 273
print ("suhu dalam kelvin", kelvin, "kelvin")

#3.3 operasi komperasi (hasilnya boolean)
print ("\nOPERASI KOMPERASI\n")
a = 10
b = 2

#komperasi lebih besar dari >
print ("'>'")
besar = a > 5
print (a,'>',5,'=',besar)
#komperasi kurang dari <
print ("'<'")
kurang = b < 5
print (b,'<',5,'=',kurang)
#lebih dari sama dengan >=
print ("'>='")
lebihsama = a >= 10
print (a,'>=',10,'=',lebihsama)
#kurang dari sama dengan <=
print ("'<='")
kurangsama = b <= 10
print (b,'<=',10,'=',kurangsama)
#sama dengan ==
print ("'=='")
sama = b == 2
print (b,'==',2,'=',sama)
#tidak sama dengan 
tidaksama = a != b
print (a,'!=',b,'=',tidaksama)


