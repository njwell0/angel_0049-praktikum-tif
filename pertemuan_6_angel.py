print ("\nMATERI 6 - NESTED IF DAN LOOP\n")
print ("===================================")

#nested IF
print ("\nNested IF\n")
#ATM sederhana
statusATM = "active"
saldoATM = 50000000
penarikan = 2000000

if statusATM == "active":
    if penarikan <= saldoATM:
        if penarikan >= 50000:
            balance = saldoATM - penarikan
            print(f"transaction succeed: Rp. {penarikan}")
            print(f"current balance: Rp. {balance}")
        else:
            print("failed! minimum withdrawl amount Rp.2000000")
    else:
        print ("insufficient balance")
else:
    print ("your account is expired")

#6.2 nested WHILE
print ("\nNested WHILE\n")
a = 1
while a <=2:
    b = 1
    while b <=3:
        print("enjelll")
        b += 1
print ("\n")
a += 1

#6.3 nested FOR 
print ("\nNested FOR\n")
for i in range (1,3):
    for u in range (1,4):
        print(f"[{i},{u}]")

#6.4 for in while
print ("\nFor in While\n")
sesi = 1
while sesi <= 2:
    print (f"mulai sesi: {sesi}")
    for antrian in range (1,6):
        print (f"antrian ke: {antrian}")
    sesi += 1
    print ("---")
    