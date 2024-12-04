# Basit Banka Sistemi

Bu proje, kullanıcıların hesap açabileceği, para yatırıp çekebileceği ve bakiye sorgulama işlemleri yapabileceği basit bir banka sistemini simüle etmektedir.

## Proje Tanımı

Bu uygulama, kullanıcıların hesap açmasını, para yatırmasını, para çekmesini ve hesap bakiyelerini sorgulamalarını sağlar. Ayrıca, birden fazla kullanıcıyı yönetebilecek şekilde tasarlanmıştır.

## Özellikler

- Kullanıcı hesabı oluşturma: Kullanıcı adı, hesap numarası ve başlangıç bakiyesi ile hesap açma.
- Para yatırma: Hesaba para yatırılabilir.
- Para çekme: Hesaptan para çekilebilir (bakiye kontrolü ile).
- Bakiye sorgulama: Hesabın mevcut bakiyesi sorgulanabilir.
- Birden fazla kullanıcı yönetimi: Farklı hesap numaralarına sahip birden fazla kullanıcı yönetilebilir.

## Kullanılan Sınıflar

### `Kullanici` Sınıfı
Bu sınıf, her bir kullanıcının bilgilerini tutar.
- **`ad`**: Kullanıcının adı.
- **`hesap_numarasi`**: Kullanıcının hesap numarası.
- **`bakiye`**: Kullanıcının hesabındaki bakiye.

### `Banka` Sınıfı
Bu sınıf, banka işlemlerini yönetir.
- **`hesap_olustur`**: Yeni bir kullanıcı hesabı oluşturur.
- **`para_yatir`**: Hesaba para yatırır.
- **`para_cek`**: Hesaptan para çeker (bakiye kontrolü ile).
- **`bakiye_sorgula`**: Hesabın mevcut bakiyesini gösterir.

## Kullanım

1. **Hesap Oluşturma:**
    - `Banka` sınıfı üzerinden `hesap_olustur` metodu kullanılarak yeni hesaplar oluşturulabilir.
    - Örnek:
      ```python
      banka.hesap_olustur("Ahmet", "12345", 1000)
      ```

2. **Para Yatırma:**
    - Hesaba para yatırmak için `para_yatir` metodu kullanılabilir.
    - Örnek:
      ```python
      banka.para_yatir("12345", 500)
      ```

3. **Para Çekme:**
    - Hesaptan para çekmek için `para_cek` metodu kullanılabilir. Yetersiz bakiye durumunda hata mesajı dönecektir.
    - Örnek:
      ```python
      banka.para_cek("12345", 200)
      ```

4. **Bakiye Sorgulama:**
    - Hesabın bakiyesi sorgulanabilir.
    - Örnek:
      ```python
      banka.bakiye_sorgula("12345")
      ```

