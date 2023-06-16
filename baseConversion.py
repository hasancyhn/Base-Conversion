# 20010011091/Hasan/Ceyhan

while True:
    print("1- İkilik tabandan onluk tabana çevirme\n"
          "2- Onluk tabandan ikilik tabana çevirme\n"
          "3- Çıkış\n")
    secim = int(input("Seçim yapınız: "))
    if secim == 1:
        while True:
            sayi = input("İkilik tabandaki sayıyı giriniz: ")
            yanlislar = "23456789"
            hataliSayi = False # Kontrol degişkeni
            onluk = 0
            sayac = len(sayi)

            for i in sayi:
                if i in yanlislar:
                    print("Yalnızca 0 ve 1 rakamlarını girin.\n")
                    hataliSayi = True # Hatalı sayı girişi var
                    break # 0 ve 1'den farklı sayı tespit ettiği için döngüden çıkar
            if hataliSayi: # TRUE olduğu zaman çalışır
                continue # while döngüsü başına döner
            else: # FALSE oldugğ zaman çevrimi yapar
                for i in sayi:
                    if i == "1":
                        onluk = onluk + (2 ** (sayac - 1))
                    sayac = sayac - 1
                print("Onluk tabandaki karşılığı: {}\n".format(onluk))
                break # İkilik sayı çevriminden çıkar menüye döner
    elif secim == 2:
        ikilik_Tabandaki_Sayi = ""
        onluk_Tabandaki_Sayi = int(input("Onluk tabandaki sayıyı giriniz: ")) # Onluk tabandaki sayıyı integer tipinde aldık
        while onluk_Tabandaki_Sayi != 0: # "onluk_Tabandaki_Sayi" isimli değişkene 0 girilmediği sürece döngü devam edecek
            ikilik_Tabandaki_Sayi = str(onluk_Tabandaki_Sayi % 2) + ikilik_Tabandaki_Sayi # Onluk tabandaki sayıyı stringe çevirdik ve 2'ye göre modunu alıp "ikilik_Tabandaki_Sayi" isimli değişkenle topladık
            onluk_Tabandaki_Sayi = onluk_Tabandaki_Sayi // 2 # "onluk_Tabandaki_Sayi" isimli değişkenin 2'ye göre tam bölmesini gerçekleştirdik
        print("İkilik tabandaki karşılığı: {}\n".format(ikilik_Tabandaki_Sayi))

    elif secim == 3:
        print("Çıkış sağlanıyor")
        quit()