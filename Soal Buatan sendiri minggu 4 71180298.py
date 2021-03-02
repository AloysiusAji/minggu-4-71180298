#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

#Membuat program untuk mencari nilai konversi mata uang asing ke rupiah
#Dolar 14500, Yen 134, Ringgit 3534, Euro 17269, Rupee 195.

def USD(Dolar):
    uangUSD = Dolar * 14500
    return uangUSD
def JPN(Yen):
    uangJPN = Yen * 134
    return uangJPN
def Malay(Ringgit):
    uangMalay = Ringgit * 3534
    return uangMalay
def Eropa(Euro):
    uangEropa = Euro * 17269
    return uangEropa
def India(Rupee):
    uangIndia = Rupee * 195
    return uangIndia

print("===Menu Konversi Mata Uang Asing Ke Rupiah===")
print("1. USA")
print("2. Jepang")
print("3. Malaysia")
print("4. Uni Eropa")
print("5. India")

pilihan = int(input("Masukan Pilihan Anda: "))

if pilihan == 1:
    Dolar = int(input("Masukan jumlah dolar yang di inginkan: "))
    print("Jumlah Rupiah yang didapat Rp.",USD(Dolar))
elif pilihan == 2:
    Yen = int(input("Masukan jumlah yen yang di inginkan: "))
    print("Jumlah Rupiah yang didapat Rp.",JPN(Yen))
elif pilihan == 3:
    Ringgit = int(input("Masukan jumlah ringgit yang di inginkan: "))
    print("Jumlah Rupiah yang didapat Rp.",Malay(Ringgit))
elif pilihan == 4:
    Euro = int(input("Masukan jumlah euro yang di inginkan: "))
    print("Jumlah Rupiah yang didapat Rp.",Eropa(Euro))
elif pilihan == 5:
    Rupee = int(input("Masukan jumlah rupee yang di inginkan: "))
    print("Jumlah Rupiah yang didapat Rp.",India(Rupee))
else:
    print("Inputan yang anda masukan salah")



