#input usia user
usia = int(input("masukkan usia anda : "))
#mengkategorikan berdasar usia
if usia <=12: 
    print ("anak-anak")
if usia >12 <=17:
    print ("remaja")
if usia >17 <=59:
    print ("dewasa")
if usia >59:
    print("lansia")