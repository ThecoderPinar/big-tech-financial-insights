import pandas as pd

# Ham verileri yükleyin
companies = pd.read_csv('../data/raw/big_tech_companies.csv')
stock_prices = pd.read_csv('../data/raw/big_tech_stock_prices.csv')

# Veri işleme adımları (örnek)
stock_prices['date'] = pd.to_datetime(stock_prices['date'])
stock_prices = stock_prices.dropna()

# İşlenmiş veriyi kaydedin
stock_prices.to_csv('../data/processed/processed_stock_data.csv', index=False)
print("Veri işleme tamamlandı ve işlenmiş veri kaydedildi.")
