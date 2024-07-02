####Alıştırma 1. Sıcaklık Dönüştürücü######
Kullanıcıdan Celsius sıcaklık değerini (ondalık sayı olabilir) girmesini isteyen, girilen değeri
Fahrenheit dereceye dönüştüren ve sonucu yazdıran kısa bir Python programı yazın.

celcius=input("Celcius Değerini Giriniz:")          #Celcius Değerini Giriniz:>? 25
celcius2=float(celcius)
sonuc=(celcius2*1.8)+32
print(f"Fahrenheit Değeri= {sonuc}")                #Fahrenheit Değeri= 77.0

------------------------------------------------------------------------------------------------
######Alıştırma 2. Mesafe Dönüştürücü (Kilometreden Mile)##############
Kullanıcıdan kilometre cinsinden bir mesafe (ondalık bir sayı olabilir) girmesini isteyen,
girilen mesafeyi mile çeviren ve sonucu yazdıran kısa bir Python programı yazın.

km=input("KM cinsinden bir mesafe giriniz:")
km2=float(km)                                   #KM cinsinden bir mesafe giriniz:>? 100
sonuc=float(km2/1.609344)
print (f"Mil Değeri= {sonuc}")                  #Mil Değeri= 62.13711922373339


-----------------------------------------------------------------------------------------
########Alıştırma 3. Üçgen Alan Hesaplayıcı#############
Kullanıcıdan bir üçgenin taban ve yüksekliğini (ondalık sayı olabilir) alacak bir program yazın.
Program, bu değerleri kullanarak üçgenin alanını hesaplamalı ve sonucu yazdırmalıdır.
(Üçgenin alanı hesaplama formülü: (taban x yükseklik) / 2)

taban=input("Üçgenin tabanını giriniz:")              #Üçgenin tabanını giriniz:>? 12.5
taban2=float(taban)
yukseklik=input("Üçgenin yüksekliğini giriniz:")
yukseklik2=float(yukseklik)                           #Üçgenin yükseklğini giriniz:>? 10.0
sonuc=float(taban2*yukseklik2/2)
print (f"Üçgenin alanı= {sonuc}")                      #Üçgenin alanı= 62.5