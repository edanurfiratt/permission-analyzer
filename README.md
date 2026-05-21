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
