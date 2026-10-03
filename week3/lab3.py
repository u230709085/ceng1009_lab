import math
import turtle

# 1. Soru: Dikdörtgen Alanı Hesabı
genislik = float(input("Genişliği giriniz: "))
yukseklik = float(input("Yüksekliği giriniz: "))
alan = genislik * yukseklik
print("Dikdörtgenin Alani:", alan)

# 2. Soru: Araç Yakıt Hesabı (MPG)
gidilen_mil = float(input("Gidilen mili giriniz: "))
harcanan_galon = float(input("Harcanan galon miktarini giriniz: "))
mpg = gidilen_mil / harcanan_galon
print("Mil/Galon (MPG) değeri:", mpg)

# 3. Soru: Fahrenheit - Celsius Dönüşümü
fahrenheit = float(input("Fahrenheit sicakliğini giriniz: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius değeri:", celsius)

# 4. Soru: Tatil Dönüş Günü Hesabı (Mod 7)
baslangic_gunu = int(input("Başlangiç günü (0=Pazar, 1=Pazartesi ... 6=Cumartesi): "))
tatil_gun_sayisi = int(input("Tatil kaç gün sürecek: "))
donus_gunu = (baslangic_gunu + tatil_gun_sayisi) % 7
print("Dönüş günü koda göre:", donus_gunu)

# 5. Soru: Dairenin Çevresi
yaricap = float(input("Dairenin yariçapini giriniz: "))
cevre = 2 * math.pi * yaricap
print("Dairenin çevresi:", cevre)

# 6. Soru: Yaş Hesabı (2024 Yılına Göre)
dogum_yili = int(input("Doğum yilinizi giriniz: "))
yas = 2024 - dogum_yili
print("Hesaplanan yaşiniz:", yas)

# 7. Soru: Turtle ile Kare Çizimi
kalem = turtle.Turtle()
for i in range(4):
    kalem.forward(100)
    kalem.right(90)

turtle.done()