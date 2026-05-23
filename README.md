Ders: Python Programlamaya Giriş

Öğrenci: Edanur Fırat

Numara: 2220656031

Ödev No: 99

Tarih: 23.05.2026


PYTHON SÜRÜMÜ:
Python 3.10


GEREKLİ KÜTÜPHANELER:
functools


ÇALIŞTIRMA KOMUTU:
python src/main.py


DOSYA YAPISI:

python_permission_project

- README.txt
- src/main.py
- tests/normal_permissions.txt
- tests/risky_permissions.txt
- tests/error_permissions.txt
- tests/sample_permissions.txt
- screenshots/output.png


ÖRNEK KULLANIM:

Program, tests klasöründeki test dosyalarını okuyarak
dosya izinlerini analiz eder.

Riskli dosya izinleri ekrana yazdırılır
ve toplam risk sayısı hesaplanır.


HATIRLATILAN DERS KAVRAMLARI:

Bu projede İşletim Sistemleri dersindeki
Linux dosya izin sistemi (rwx) mantığı kullanılmıştır.

Program içerisinde:

- map() fonksiyonu veri dönüşümü için
- filter() fonksiyonu riskli dosyaları ayırmak için
- reduce() fonksiyonu toplam risk sayısını hesaplamak için

kullanılmıştır.


TEST SENARYOLARI:

1. Normal Durum Testi
- Güvenli dosya izinleri kontrol edilmiştir.

2. Riskli Durum Testi
- Yazma, okuma ve çalıştırma izinleri açık olan
dosyalar analiz edilmiştir.

3. Hata Durumu Testi
- Hatalı veya eksik veri içeren satırlar test edilmiştir.


EK DOSYALAR:

screenshots klasörü içerisinde
program çıktısına ait ekran görüntüsü bulunmaktadır.


BİLİNEN SORUNLAR:

Bilinen bir hata bulunmamaktadır.
