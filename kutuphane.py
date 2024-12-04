

class Benim_Kutuphanem:
    def __init__(self):
        self.kitaplar = []
        self.odunc_verilenler = []
        
    def kitap_ekle(self, kitap):
        if kitap in self.kitaplar: 
            return f"Bu kitap zaten kütüphanede mevcut: {kitap}"
        self.kitaplar.append(kitap)
        return f"Kitap eklendi: {kitap}"
    
    def kitap_sil(self, kitap):
       if kitap in self.kitaplar:
           self.kitaplar.remove(kitap)
           return f"Kitap silindi: {kitap}"
       return f"Kitap kütüphanede bulunamadı: {kitap}"
    
    def kitap_listesi(self):
        if not self.kitaplar:
            return "Kütüphanede kitap yok."
        return f"Kitap listesi: {self.kitaplar}"
    
    def kitap_odunc(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            self.odunc_verilenler.append(kitap)
            return f"Kitap ödünç alındı: {kitap}"
        elif kitap in self.odunc_verilenler:
            return f"Kitap zaten ödünç verilmiş: {kitap}"
        else:
            return f"Kitap bulunamadı: {kitap}"
    
    def odunc_listesi(self):
        if not self.odunc_verilenler:
            return "Şu an ödünç verilen kitap yok."
        return f"Ödünç verilen kitaplar: {self.odunc_verilenler}"
    
    def kitap_iade(self, kitap):
        if kitap in self.odunc_verilenler:
            self.odunc_verilenler.remove(kitap)
            self.kitaplar.append(kitap)
            return f"Kitap iade edildi: {kitap}"
        return f"Bu kitap ödünç alınmamış:{kitap}"
    

        
        
    
kutuphane = Benim_Kutuphanem()

print(kutuphane.kitap_ekle("Harry Potter"))
print(kutuphane.kitap_ekle("Nutuk"))
print(kutuphane.kitap_ekle("El Kızı"))
print(kutuphane.kitap_ekle("Harry Potter"))


print(kutuphane.kitap_odunc("El Kızı"))
print(kutuphane.kitap_odunc("El Kızı"))


print(kutuphane.kitap_listesi())


print(kutuphane.odunc_listesi())

print(kutuphane.kitap_iade("El Kızı"))
print(kutuphane.kitap_iade("El Kızı"))

print(kutuphane.kitap_sil("Harry Potter"))
print(kutuphane.kitap_sil("Harry Potter"))
