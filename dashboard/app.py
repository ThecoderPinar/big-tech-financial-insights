import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
import os

# Stil dosyasını yükleyin
st.markdown(
    """
 <style>
/* Ana sayfa arka plan stil */
.stApp {
    background: linear-gradient(135deg, #0c0b29, #302b63, #7a0c2e);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
    font-family: 'Helvetica', sans-serif;
    color: #ffffff;
}

@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Yan menü stil */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #0c0b29, #302b63, #7a0c2e);
    color: #ffffff;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    transition: background 0.3s;
}

/* Menü stil */
.css-1d391kg {
    background: linear-gradient(135deg, #1a1a1a, #302b63, #7a0c2e);
    box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    border-radius: 10px;
    margin-bottom: 20px;
    padding: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.css-1d391kg:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.7);
}

/* Menü başlık stil */
.css-1v3fvcr {
    color: #ff00ff;
    font-size: 18px;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
    text-shadow: 1px 1px 2px #000000;
}

/* Menü öğe stil */
.option-menu {
    list-style-type: none;
    padding: 0;
}

.option-menu li {
    margin: 10px 0;
}

.option-menu a {
    color: #ffffff;
    font-size: 16px;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    transition: background 0.3s, color 0.3s;
    display: block;
    background-color: #302b63;
    margin-bottom: 5px;
}

.option-menu a:hover {
    background-color: #ff00ff;
    color: #0c0b29;
}

/* Menü simge stil */
.option-menu a i {
    margin-right: 10px;
    color: #ff00ff;
    transition: color 0.3s;
}

.option-menu a:hover i {
    color: #0c0b29;
}



/* Başlık stil */
.stTitle {
    color: #ff00ff;
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px #000000;
}

/* Alt başlık stil */
.stSubheader {
    color: #ff00ff;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
    text-shadow: 1px 1px 2px #000000;
}

/* Buton stil */
.stButton button {
    background-color: #ff00ff;
    color: #121212;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    box-shadow: 0 4px 8px rgba(255, 0, 255, 0.3);
}

.stButton button:hover {
    background-color: #cc00cc;
}

/* Grafik stil */
.plotly-graph {
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    margin: 20px 0;
    background: #0c0b29;
    padding: 10px;
}

/* Footer stil */
footer {
    background-color: #1e1e1e;
    color: #ff00ff;
    padding: 10px;
    text-align: center;
    border-top: 2px solid #ff00ff;
    position: fixed;
    width: 100%;
    bottom: 0;
    box-shadow: 0 -4px 8px rgba(255, 0, 255, 0.3);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: nowrap;
    z-index: 1000;
}

.footer-content {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer-content .social-icons {
    display: flex;
    gap: 10px;
}

.footer-content .social-icons a {
    color: #ff00ff;
    text-decoration: none;
    font-size: 18px;
    transition: color 0.3s;
}

.footer-content .social-icons a:hover {
    color: #cc00cc;
}

.footer-content p {
    margin: 0;
    text-align: left;
    flex: 1;
}

.footer-content .developed-by {
    margin: 0;
    text-align: right;
    flex: 1;
}



/* Card stil */
.card {
    background-color: #1a1a1a;
    border-radius: 25px;
    padding: 50px;
    margin: 30px 0;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.7);
    transition: transform 0.3s, box-shadow 0.3s;
    border: 2px solid #ff00ff;
    text-align: center;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
}

.card:hover {
    transform: translateY(-20px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.9);
}

.card img {
    border-radius: 50%;
    margin-bottom: 25px;
    width: 200px;
    height: 200px;
    object-fit: cover;
    border: 3px solid #ff00ff;
    padding: 10px;
    transition: transform 0.3s;
}

.card img:hover {
    transform: scale(1.1);
}

.card h2 {
    color: #ff00ff;
    font-size: 30px;
    margin: 20px 0;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.card p {
    color: #ffffff;
    font-size: 18px;
    margin: 10px 0;
    line-height: 1.8;
    text-align: center;
}

.card .social-icons {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 20px;
}

/* Table stil */
.styled-table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 14px;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    background-color: #1a1a1a;
    border-radius: 10px;
    overflow: hidden;
}

.styled-table thead tr {
    background-color: #ff00ff;
    color: #ffffff;
    text-align: left;
}

.styled-table th,
.styled-table td {
    padding: 8px 12px;
}

.styled-table tbody tr {
    border-bottom: 1px solid #303030;
}

.styled-table tbody tr:nth-of-type(even) {
    background-color: #2a2a2a;
}

.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #ff00ff;
}

.styled-table tbody tr.active-row {
    font-weight: bold;
    color: #ff00ff;
}

  /* Sosyal medya ikonları */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 10px;
    }

    .social-icons a {
        color: #ff00ff;
        text-decoration: none;
        font-size: 24px;
        transition: color 0.3s;
    }

    .social-icons a:hover {
        color: #cc00cc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menü
with st.sidebar:
    selected = option_menu(
        "Menü",
        ["Genel Bilgi", "Amaç ve Hedef", "Veri Seti Bilgisi", "Analiz", "Geliştirici Bilgisi", "İletişim"],
        icons=["info", "target", "database", "bar-chart", "person", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Genel Bilgi":
    st.title('')
    st.markdown("""
    <div class="card">
        <h2>Genel Bilgi</h2>
        <p>Bu proje, büyük teknoloji şirketlerinin hisse senedi verilerini analiz etmek ve bu verilere dayalı tahmin modelleri oluşturmak amacıyla geliştirilmiştir.</p>
        <p>Amacımız, yatırımcılara ve finansal analistlere karar verme süreçlerinde yardımcı olabilecek bilgiler sunmaktır.</p>
        <h3>Hedef Kitle:</h3>
        <ul>
            <li>Yatırımcılar</li>
            <li>Finansal Analistler</li>
            <li>Veri Bilimciler</li>
            <li>Akademisyenler</li>
        </ul>
        <h3>Proje Özellikleri:</h3>
        <ul>
            <li>Zaman serisi analizleri</li>
            <li>Hisse senedi fiyat tahmin modelleri</li>
            <li>Volatilite analizleri</li>
            <li>Etkileşimli veri görselleştirmeleri</li>
            <li>Risk ve getiri analizleri</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Amaç ve Hedef":
    st.title('')
    st.markdown("""
    <div class="card">
        <h2>Amaç ve Hedef</h2>
        <h3>Amaç:</h3>
        <p>Bu projenin amacı, büyük teknoloji şirketlerinin hisse senedi fiyatlarını analiz etmek, fiyat tahmin modelleri geliştirmek ve bu modelleri kullanarak gelecekteki fiyat hareketlerini öngörmektir. Ayrıca, yatırımcıların risk ve getiri analizleri yapmalarına yardımcı olacak araçlar sunmaktır.</p>
        <h3>Hedefler:</h3>
        <ul>
            <li>Hisse senedi fiyat verilerini toplamak ve temizlemek.</li>
            <li>Fiyat tahmin modelleri geliştirmek (ARIMA, GARCH vb.).</li>
            <li>Hisse senedi fiyatları ve makroekonomik göstergeler arasındaki ilişkileri analiz etmek.</li>
            <li>Anomali tespit yöntemleri uygulamak.</li>
            <li>Yatırımcılar için risk ve getiri analizleri sağlamak.</li>
            <li>Etkileşimli panolar ve görselleştirmeler oluşturmak.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Veri Seti Bilgisi":
    st.title('')
    st.markdown("""
    <div class="card">
        <h2>Veri Seti Bilgisi</h2>
        <p>Bu projede kullanılan veri setleri, büyük teknoloji şirketlerinin hisse senedi fiyat verilerini içermektedir. Veriler, hisse senedi sembolleri, tarih, açılış fiyatı, en yüksek fiyat, en düşük fiyat, kapanış fiyatı, düzeltilmiş kapanış fiyatı ve işlem hacmi gibi bilgileri içermektedir.</p>
        <h3>Veri Setleri:</h3>
        <ul>
            <li><strong>big_tech_companies.csv:</strong> Büyük teknoloji şirketlerinin hisse senedi sembolleri ve şirket isimleri.</li>
            <li><strong>big_tech_stock_prices.csv:</strong> Büyük teknoloji şirketlerinin tarihsel hisse senedi fiyat verileri.</li>
        </ul>
        <h3>Örnek Veriler:</h3>
        <table class="styled-table">
            <thead>
                <tr>
                    <th>stock_symbol</th>
                    <th>date</th>
                    <th>open</th>
                    <th>high</th>
                    <th>low</th>
                    <th>close</th>
                    <th>adj_close</th>
                    <th>volume</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AAPL</td>
                    <td>2010-01-04</td>
                    <td>7.622500</td>
                    <td>7.660714</td>
                    <td>7.585000</td>
                    <td>7.643214</td>
                    <td>6.515213</td>
                    <td>493729600</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>2010-01-05</td>
                    <td>7.664286</td>
                    <td>7.699643</td>
                    <td>7.616071</td>
                    <td>7.656429</td>
                    <td>6.526476</td>
                    <td>601904800</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>2010-01-06</td>
                    <td>7.656429</td>
                    <td>7.686786</td>
                    <td>7.526786</td>
                    <td>7.534643</td>
                    <td>6.422664</td>
                    <td>552160000</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>2010-01-07</td>
                    <td>7.562500</td>
                    <td>7.571429</td>
                    <td>7.466071</td>
                    <td>7.520714</td>
                    <td>6.410790</td>
                    <td>477131200</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>2010-01-08</td>
                    <td>7.510714</td>
                    <td>7.571429</td>
                    <td>7.466429</td>
                    <td>7.570714</td>
                    <td>6.453412</td>
                    <td>447610800</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Analiz":
    st.title('Büyük Teknoloji Şirketleri Hisse Senedi Analizi')

    # İşlenmiş veriyi yükleyin
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'processed', 'processed_stock_data.csv')
    data = pd.read_csv(data_path)

    # Hisse senedi seçimi
    stock_symbol = st.sidebar.selectbox('Hisse Senedi Sembolü Seçin', data['stock_symbol'].unique())

    # Tarih aralığı seçimi
    start_date = st.sidebar.date_input('Başlangıç Tarihi', value=pd.to_datetime(data['date']).min())
    end_date = st.sidebar.date_input('Bitiş Tarihi', value=pd.to_datetime(data['date']).max())

    # Seçilen hisse senedi ve tarih aralığına göre veriyi filtreleme
    filtered_data = data[
        (data['stock_symbol'] == stock_symbol) & (data['date'] >= str(start_date)) & (data['date'] <= str(end_date))]

    # Fiyat grafiği oluşturma
    st.subheader(f'{stock_symbol} Fiyat Grafiği ({start_date} - {end_date})')
    fig_price = px.line(filtered_data, x='date', y='close',
                        title=f'{stock_symbol} Fiyat Grafiği ({start_date} - {end_date})')
    fig_price.update_layout(
        plot_bgcolor='#0c0b29',
        paper_bgcolor='#0c0b29',
        font=dict(color='#ffffff'),
        title=dict(font=dict(size=20, color='#ff00ff')),
        xaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff')),
        yaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff'))
    )
    st.plotly_chart(fig_price)

    # ARIMA tahmin modeli
    st.subheader(f'{stock_symbol} Fiyat Tahmini (ARIMA)')
    model_arima = ARIMA(filtered_data['close'], order=(5, 1, 0))
    model_fit_arima = model_arima.fit()
    forecast_arima = model_fit_arima.forecast(steps=30)
    forecast_dates = pd.date_range(start=filtered_data['date'].iloc[-1], periods=30, freq='D')
    fig_forecast = go.Figure()
    fig_forecast.add_trace(
        go.Scatter(x=filtered_data['date'], y=filtered_data['close'], mode='lines', name='Close Price'))
    fig_forecast.add_trace(
        go.Scatter(x=forecast_dates, y=forecast_arima, mode='lines', name='Forecast', line=dict(color='red')))
    fig_forecast.update_layout(
        title=f'{stock_symbol} Fiyat Tahmini (ARIMA)',
        xaxis_title='Tarih',
        yaxis_title='Fiyat',
        plot_bgcolor='#0c0b29',
        paper_bgcolor='#0c0b29',
        font=dict(color='#ffffff'),
        title_font=dict(size=20, color='#ff00ff'),
        xaxis_title_font=dict(color='#ff00ff'),
        yaxis_title_font=dict(color='#ff00ff'),
        xaxis_tickfont=dict(color='#ff00ff'),
        yaxis_tickfont=dict(color='#ff00ff')
    )
    st.plotly_chart(fig_forecast)

    # GARCH modeli ile volatilite tahmini
    st.subheader(f'{stock_symbol} Volatilite (GARCH)')
    filtered_data.loc[:, 'return'] = filtered_data['close'].pct_change()  # .loc kullanarak atama yapma
    filtered_data = filtered_data.dropna(subset=['return'])
    model_garch = arch_model(filtered_data['return'] * 100, vol='Garch', p=1, q=1)
    model_fit_garch = model_garch.fit(disp='off')
    volatility = model_fit_garch.conditional_volatility / 100
    volatility = volatility.reindex(filtered_data.index, method='bfill')
    fig_volatility = go.Figure()
    fig_volatility.add_trace(go.Scatter(x=filtered_data['date'], y=volatility, mode='lines', name='Volatility'))
    fig_volatility.update_layout(
        title=f'{stock_symbol} Volatilite (GARCH)',
        xaxis_title='Tarih',
        yaxis_title='Volatilite',
        plot_bgcolor='#0c0b29',
        paper_bgcolor='#0c0b29',
        font=dict(color='#ffffff'),
        xaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff')),
        yaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff'))
    )
    st.plotly_chart(fig_volatility)

    # Hisse senedi getirilerinin dağılımı
    st.subheader(f'{stock_symbol} Getirilerin Dağılımı')
    fig_returns_histogram = px.histogram(filtered_data, x='return', nbins=50,
                                         title=f'{stock_symbol} Getirilerin Dağılımı')
    fig_returns_histogram.update_layout(
        xaxis_title='Getiri',
        yaxis_title='Frekans',
        plot_bgcolor='#0c0b29',
        paper_bgcolor='#0c0b29',
        font=dict(color='#ffffff'),
        title=dict(font=dict(size=20, color='#ff00ff')),
        xaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff')),
        yaxis=dict(title=dict(font=dict(color='#ff00ff')), tickfont=dict(color='#ff00ff'))
    )
    st.plotly_chart(fig_returns_histogram)

    # Ek analizler
    st.sidebar.header('Ek Analizler')
    analysis_type = st.sidebar.selectbox('Analiz Türü Seçin', ['Korelasyon Analizi', 'Mevsimsel Analiz'])

    if analysis_type == 'Korelasyon Analizi':
        st.subheader('Korelasyon Matrisi')
        numeric_data = data.select_dtypes(include=[float, int])  # Yalnızca sayısal sütunları seçin
        correlation_matrix = numeric_data.corr()
        st.write(correlation_matrix)

    elif analysis_type == 'Mevsimsel Analiz':
        st.subheader('Aylık Ortalama Fiyat Analizi')
        filtered_data['month'] = pd.to_datetime(filtered_data['date']).dt.to_period('M')
        monthly_avg_prices = filtered_data.groupby('month')['close'].mean().reset_index()
        fig_monthly_avg = px.line(monthly_avg_prices, x='month', y='close',
                                  title=f'{stock_symbol} Aylık Ortalama Fiyatlar')
        fig_monthly_avg.update_layout(
            plot_bgcolor='#0c0b29',
            paper_bgcolor='#0c0b29',
            font=dict(color='#ffffff'),
            yaxis_title_font=dict(color='#ff00ff'),
            xaxis_tickfont=dict(color='#ff00ff'),
            yaxis_tickfont=dict(color='#ff00ff')
        )
        st.plotly_chart(fig_monthly_avg)

    st.sidebar.subheader('Seçenekler')
    show_volume = st.sidebar.checkbox('İşlem Hacmi Grafiğini Göster')

    if show_volume:
        st.subheader(f'{stock_symbol} İşlem Hacmi')
        fig_volume = px.line(filtered_data, x='date', y='volume', title=f'{stock_symbol} İşlem Hacmi')
        fig_volume.update_layout(
            plot_bgcolor='#0c0b29',
            paper_bgcolor='#0c0b29',
            font=dict(color='#ffffff'),
            title_font=dict(size=20, color='#ff00ff'),
            xaxis_title_font=dict(color='#ff00ff'),
            yaxis_title_font=dict(color='#ff00ff'),
            xaxis_tickfont=dict(color='#ff00ff'),
            yaxis_tickfont=dict(color='#ff00ff')
        )
        st.plotly_chart(fig_volume)

elif selected == "Geliştirici Bilgisi":
    st.title('Geliştirici Bilgisi')
    st.markdown("""
                <div class="card">
                    <img src="https://via.placeholder.com/150" alt="Developer Photo" width="150">
                    <h2>Pinar Topuz</h2>
                    <p>Veri Bilimi ve Makine Öğrenimi Uzmanı</p>
                    <p>Lise Mezunu Geliştiri</p>
                    <p>3+ yıllık deneyim</p>
                    <div class="social-icons">
                        <a href="https://www.linkedin.com/in/piinartp" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://twitter.com/llBeest" target="_blank"><i class="fab fa-twitter"></i></a>
                        <a href="https://github.com/ThecoderPinar" target="_blank"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

elif selected == "İletişim":
    st.title('')
    st.markdown("""
                <div class="card">
                    <h2>İletişim Bilgileri</h2>
                    <p>Proje ile ilgili sorularınız veya geri bildirimleriniz için aşağıdaki iletişim bilgilerini kullanabilirsiniz:</p>
                    <p><strong>E-posta:</strong> piinartp@gmail.com</p>
                    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/piinartp" target="_blank">linkedin.com/in/piinartp</a></p>
                    <p><strong>Twitter:</strong> <a href="https://twitter.com/llBeest" target="_blank">twitter.com/llBeest</a></p>
                    <p><strong>GitHub:</strong> <a href="https://github.com/ThecoderPinar" target="_blank">github.com/pinuto</a></p>
                    <p><strong>Kaggle:</strong> <a href="https://www.kaggle.com/pinuto" target="_blank">kaggle.com/pinuto</a></p>
                    <p><strong>İnstagram:</strong> <a href="https://www.instagram.com/piinar.py" target="_blank">instagram.com/piinar.py</a></p>
                    <div class="social-icons">
                        <a href="https://www.linkedin.com/in/piinartp" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://twitter.com/llBeest" target="_blank"><i class="fab fa-twitter"></i></a>
                        <a href="https://github.com/ThecoderPinar" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://www.kaggle.com/pinuto" target="_blank"><i class="fab fa-kaggle"></i></a>
                        <a href="https://www.instagram.com/piinar.py" target="_blank"><i class="fab fa-instagram"></i></a>
                </div>
                </div>
                """, unsafe_allow_html=True)

    # Footer
st.markdown(
    """
  <footer>
    <div class="footer-content">
        <p>&copy; 2024 Big Tech Stock Analysis</p>
        <div class="social-icons">
            <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com" target="_blank"><i class="fab fa-github"></i></a>
        </div>
        <p>Developed by Pinar Topuz</p>
    </div>
</footer>
    """,
    unsafe_allow_html=True
)
