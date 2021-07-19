isim = input('Lütfen isminizi giriniz:--> ')
yas = int(input('Lütfen Yaşınızı Giriniz:--> '))
ortalama = int(input('Ortalamanızı giriniz:--> '))

if(yas>=17 and yas<22 and ortalama>=80):
    print(isim + ': geçti')
else: 
    print(isim + ': kaldı')