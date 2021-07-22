print("Kenar uzunluklarını girerken küçükten büyüğe doğru gidiniz.")
a = float(input("İlk kenar uzunluğunu giriniz: "))
b = float(input("İkinci kenar uzunluğunu giriniz: "))
c = float(input("Üçüncü kenar uzunluğunu giriniz: "))

if (c**2 == (a**2 + b**2)):
    print(f"{a}, {b}, {c} kenar uzunluklarına sahip bu üçgen dik üçgendir.")
if (a == b or b == c or a == c):
    print(f"{a}, {b}, {c} kenar uzunluklarına sahip bu üçgen ikizkenar üçgendir.")
else:
    print("Girdiğiniz kenar uzunlukları herhangi bir üçgen tipine uymuyor. Lütfen tekrar deneyin!")