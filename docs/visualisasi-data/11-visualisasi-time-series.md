# 📘 Modul 11: Visualisasi Data Deret Waktu (Time Series) & Finansial

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memvisualisasikan pola data deret waktu: Tren (*Trend*), Musiman (*Seasonality*), Siklus (*Cycle*), dan Residu (*Noise*).
2. Menerapkan teknik pemulusan data (*Data Smoothing*): Moving Average dan Exponential Smoothing.
3. Membuat grafik finansial profesional: **Candlestick Chart** dan **Volume Bar**.
4. Melakukan dekomposisi komponen time series dengan pustaka *Statsmodels*.

---

## 1. Dekomposisi Komponen Time Series

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Simulasi / Load Data Time Series Bulanan
# df = pd.read_csv('data_penjualan_bulanan.csv', parse_dates=['tanggal'], index_col='tanggal')
# result = seasonal_decompose(df['nilai'], model='additive', period=12)

# fig = result.plot()
# fig.set_size_inches(10, 8)
# plt.tight_layout()
# plt.show()
```

---

## 2. Candlestick Chart Finansial dengan Plotly

```python
import plotly.graph_objects as go
import pandas as pd

# Contoh Data OHLC (Open, High, Low, Close)
data_saham = pd.DataFrame({
    'Tanggal': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Open': [100, 105, 102, 108, 107],
    'High': [110, 109, 108, 115, 112],
    'Low': [98, 101, 99, 105, 104],
    'Close': [106, 103, 107, 110, 109]
})

fig = go.Figure(data=[go.Candlestick(
    x=data_saham['Tanggal'],
    open=data_saham['Open'],
    high=data_saham['High'],
    low=data_saham['Low'],
    close=data_saham['Close'],
    increasing_line_color='#10b981', 
    decreasing_line_color='#ef4444'
)])

fig.update_layout(
    title='Pergerakan Harga Saham Harian (Candlestick)',
    xaxis_title='Tanggal',
    yaxis_title='Harga (IDR)',
    template='plotly_white'
)
fig.show()
```