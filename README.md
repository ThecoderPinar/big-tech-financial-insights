# 📊 Big Tech Financial Insights 💹

Bu proje, büyük teknoloji şirketlerinin hisse senedi verilerini analiz etmek ve tahminlerde bulunmak için geliştirilmiştir. Proje, zaman serisi analizi, volatilite modellemesi, makroekonomik göstergelerin etkileri ve daha fazlasını içermektedir. Proje ayrıca etkileşimli panolar ve otomatik raporlama gibi özellikleri de kapsamaktadır.

## 📁 Proje Yapısı

big_tech_financial_insights/
├── dashboard/
│ ├── app.py
├── scripts/
│ ├── report_generator.py
├── templates/
│ ├── daily_report_template.html
│ ├── weekly_report_template.html
│ ├── monthly_report_template.html
├── data/
│ └── processed/
│ └── processed_stock_data.csv
├── requirements.txt
└── README.md


## 🚀 Başlangıç

Bu projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### Gereksinimler

Gerekli Python paketlerini yüklemek için `requirements.txt` dosyasını kullanın:

```bash
pip install -r requirements.txt
```

Streamlit uygulamasını çalıştırmak için:
```bash
streamlit run dashboard/app.py
```

Otomatik raporları oluşturmak için:
```bash
python scripts/report_generator.py
```

## 📈 Özellikler

**Zaman Serisi Analizi**

Büyük teknoloji şirketlerinin hisse senedi fiyat verilerini analiz ederek gelecekteki fiyat hareketlerini tahmin etmeyi amaçlıyoruz. ARIMA ve GARCH modelleri kullanılarak fiyat ve volatilite tahminleri yapılmaktadır.

**Volatilite Modellemesi**

GARCH modelleri ile hisse senedi fiyat volatilitesini modelleyebilir ve tahmin edebiliriz.

**Makroekonomik Göstergeler**

Faiz oranları ve enflasyon gibi makroekonomik verilerin hisse senedi fiyatları üzerindeki etkilerini modelleyebiliriz.

**Otomatik Alım Satım ve Robo-Danışmanlık**

Otomatik alım satım algoritmaları geliştirip, kişiselleştirilmiş yatırım önerileri sunan robo-danışmanlık hizmetleri oluşturabiliriz.

**Model Açıklanabilirliği**

SHAP veya LIME gibi tekniklerle makine öğrenimi model kararlarını açıklayıp, modellerdeki önyargıları analiz edebiliriz.

**Blok Zinciri ve Kripto Paralar**

Kripto para piyasaları için analiz ve tahmin modelleri geliştirip, finansal analizlerde blok zinciri teknolojisi ve akıllı sözleşmeleri kullanabiliriz.

**Görselleştirme ve Panolar**

Etkileşimli panolar oluşturup, fiyat trendlerini ve tahmin analizlerini görselleştirebiliriz.

**📊 Etkileşimli Panolar**

Streamlit kullanılarak oluşturulan etkileşimli panolar sayesinde hisse senedi verilerini analiz edebilir, farklı dönemlerdeki fiyat değişimlerini inceleyebilir ve gelecekteki fiyat hareketlerini tahmin edebilirsiniz.

**📑 Raporlama**

Günlük, haftalık ve aylık raporlar oluşturularak hisse senedi fiyatlarının detaylı analizleri yapılmaktadır. Raporlar, Jinja2 kullanılarak HTML formatında oluşturulmaktadır.

## 📋 Veri Setleri

Bu projede kullanılan veri setleri, büyük teknoloji şirketlerinin hisse senedi fiyat verilerini içermektedir:

1. [ ] big_tech_companies.csv: Büyük teknoloji şirketlerinin hisse senedi sembolleri ve şirket isimleri.
2. [ ] big_tech_stock_prices.csv: Büyük teknoloji şirketlerinin tarihsel hisse senedi fiyat verileri.
