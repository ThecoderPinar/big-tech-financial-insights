import pandas as pd
from jinja2 import Template
import os

# Betiğin çalıştığı dizini belirleyelim
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# İşlenmiş veriyi yükleyin
data_path = os.path.join(base_dir, 'data', 'processed', 'processed_stock_data.csv')
data = pd.read_csv(data_path)


# Rapor oluşturma fonksiyonu
def generate_report(data, report_type='daily'):
    template_path = os.path.join(base_dir, 'templates', f'{report_type}_report_template.html')
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Şablon dosyası bulunamadı: {template_path}")

    with open(template_path) as file:
        template = Template(file.read())

    rendered_report = template.render(data=data.to_dict(orient='records'))
    report_path = os.path.join(base_dir, 'reports', f'{report_type}_report.html')

    with open(report_path, 'w') as f:
        f.write(rendered_report)

    print(f"{report_type.capitalize()} raporu oluşturuldu ve {report_path} dosyasına kaydedildi.")


# Günlük, haftalık ve aylık raporları oluşturma
generate_report(data, report_type='daily')
generate_report(data, report_type='weekly')
generate_report(data, report_type='monthly')
