
class Kullanici: 
    def __init__(self, ad, hesap_numarasi, bakiye=0):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye
        
    def bakiye_goster(self):
        return f"{self.add} - Hesap Numarası: {self.hesap_numarasi}, Bakiye:{self.bakiye} TL"
    

class Banka:
    def __init__(self):
        self.kullanici_listesi = {}
        
    def hesap_olustur(self, ad, hesap_numarasi, bakiye = 0):
        if hesap_numarasi in self.kullanici_listesi:
            return "Hesap numarası zaten var!"
        kullanici = Kullanici(ad, hesap_numarasi, bakiye)
        self.kullanici_listesi[hesap_numarasi]=kullanici
        return f"Hesap başarıyla oluşturuldu: {ad} - Hesap Numarası: {hesap_numarasi}"
    
    def para_yatir(self, hesap_numarasi, miktar):
        if hesap_numarasi not in self.kullanici_listesi:
            return "Hesap numarası bulunamadı!"
        if miktar <= 0:
            return "Yatırılacak miktar sıfırdan büyük olmalı!"
        kullanici = self.kullanici_listesi[hesap_numarasi]
        kullanici.bakiye += miktar
        return f"{miktar} TL yatırıldı. Yeni bakiye: {kullanici.bakiye} TL"

    def para_cek(self, hesap_numarasi, miktar):
        if hesap_numarasi not in self.kullanici_listesi:
            return "Hesap numarası bulunamadı!"
        kullanici = self.kullanici_listesi[hesap_numarasi]
        if miktar<=0:
            return "Çekilecek miktar sıfırdan büyük olmalı!"
        if miktar> kullanici.bakiye:
            return "Yetersiz bakiye!"
        kullanici.bakiye -= miktar
        return f"{miktar} TL çekildi. Kalan bakiye: {kullanici.bakiye} TL"


    def bakiye_sorgula(self, hesap_numarasi):
        if hesap_numarasi not in self.kullanici_listesi:
            return "Hesap numarası bulunamadı!"
        kullanici = self.kullanici_listesi[hesap_numarasi]
        return f"{kullanici.ad} - Hesap Numarası : {hesap_numarasi}, Bakiye: {kullanici.bakiye} TL"
    
    
    
banka = Banka()


print(banka.hesap_olustur("Songül", "12345", 1000))
print(banka.hesap_olustur("Alperen", "67890", 500))

print(banka.para_yatir("12345", 500))

print(banka.bakiye_sorgula("12345"))


print(banka.para_cek("12345", 200))
print(banka.para_cek("12345", 1500))

print(banka.bakiye_sorgula("12345"))
