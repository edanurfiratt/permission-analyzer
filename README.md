# Permission Analyzer

Bu proje Python'da map, filter ve reduce fonksiyonlarını kullanarak geliştirilmiş basit bir dosya izin analiz aracıdır.

Program txt dosyasında bulunan dosya izinlerini analiz eder ve riskli izinleri tespit eder.

## Kullanılan Konular

- Fonksiyonlar
- map()
- filter()
- reduce()
- Dosya işlemleri
- Listeler ve dictionary yapısı

## Projenin Amacı

Dosya izinlerini inceleyerek güvenlik riski oluşturabilecek durumları belirlemek.

Kontrol edilen durumlar:

- Diğer kullanıcıların dosyaya yazabilmesi
- Diğer kullanıcıların dosyayı çalıştırabilmesi
- Diğer kullanıcıların dosyayı okuyabilmesi

## Dosya Yapısı

```text
permission-analyzer
│
├── main.py
├── sample_permissions.txt
└── README.md
```

## Programı Çalıştırma

Terminalden şu komut çalıştırılır:

```bash
python main.py
```

## Örnek Veri

sample_permissions.txt dosyası:

```text
notes.txt rw-r--r--
public.txt rw-rw-rw-
script.sh rwxr-xr-x
secret.key rw-------
open_file.txt rwxrwxrwx
```

## Örnek Çıktı

```text
DOSYA IZIN ANALIZ RAPORU
==============================

Dosya: notes.txt
Izin : rw-r--r--
Durum: Riskli

Dosya: public.txt
Izin : rw-rw-rw-
Durum: Riskli
```

## Test Senaryoları

1. Güvenli dosya izinleri
2. Yazma izni açık dosyalar
3. Çalıştırma izni açık dosyalar

## Not

Bu proje Python Programlamaya Giriş dersi ödevi olarak hazırlanmıştır.
