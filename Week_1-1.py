isim = input("İsminizi giriniz: ")
yas = int(input("Yaşınız giriniz: "))
ortalama = int(input("Not ortalamanızı giriniz: "))

if (yas>=17 and yas<=21 and ortalama >= 80 and ortalama <= 100):
    print("Sınıfı Geçti")
else:
    print("Sınıfı Geçemedi")
