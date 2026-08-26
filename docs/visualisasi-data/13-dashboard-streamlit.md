# 📘 Modul 13: Pembangunan Dashboard Interaktif dengan Streamlit

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memahami arsitektur eksekusi dan siklus reaktif aplikasi web **Streamlit**.
2. Mengintegrasikan komponen input interaktif: `st.selectbox`, `st.slider`, `st.date_input`, dan `st.file_uploader`.
3. Mengatur layout antarmuka profesional: `st.sidebar`, `st.columns`, `st.tabs`, dan `st.metric`.
4. Mengoptimalkan performa pemuatan data besar dengan decorator `@st.cache_data`.
5. Menghubungkan visualisasi Plotly/Matplotlib ke dalam antarmuka web Streamlit.

---

## 1. Struktur Kode Aplikasi Dashboard Streamlit (`app.py`)

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="Dashboard Eksekutif Penjualan", page_icon="📊", layout="wide")

# 2. Caching Pemuatan Data demi Efisiensi Kinerja
@st.cache_data
def load_data():
    df = pd.DataFrame({
        "Wilayah": ["Aceh", "Sumut", "Sumbar", "Riau", "Kepri", "Aceh", "Sumut"],
        "Kategori": ["Laptop", "Smartphone", "Laptop", "Aksesoris", "Smartphone", "Aksesoris", "Laptop"],
        "Pendapatan": [15000000, 8500000, 12000000, 3200000, 9100000, 2800000, 16200000],
        "Bulan": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar"]
    })
    return df

df = load_data()

# 3. Sidebar Filter Interaktif
st.sidebar.header("🔍 Filter Analisis")
wilayah_terpilih = st.sidebar.multiselect("Pilih Wilayah:", options=df["Wilayah"].unique(), default=df["Wilayah"].unique())

df_filtered = df[df["Wilayah"].isin(wilayah_terpilih)]

# 4. Header & KPI Metrik Ringkasan
st.title("📊 Executive Sales Dashboard")
st.markdown("Dashboard analitik performa penjualan regional berbasis *Streamlit & Plotly*.")

col1, col2, col3 = st.columns(3)
col1.metric(label="Total Pendapatan", value=f"Rp {df_filtered['Pendapatan'].sum():,.0f}")
col2.metric(label="Total Transaksi", value=len(df_filtered))
col3.metric(label="Rata-rata Transaksi", value=f"Rp {df_filtered['Pendapatan'].mean():,.0f}")

st.divider()

# 5. Grid Grafik Visualisasi
tab1, tab2 = st.tabs(["📈 Distribusi Kategori", "🗺️ Pendapatan Regional"])

with tab1:
    fig_bar = px.bar(df_filtered, x="Kategori", y="Pendapatan", color="Wilayah", barmode="group",
                     title="Pendapatan Berdasarkan Kategori Produk")
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    fig_pie = px.pie(df_filtered, names="Wilayah", values="Pendapatan", hole=0.4,
                     title="Pangsa Pasar per Wilayah")
    st.plotly_chart(fig_pie, use_container_width=True)
```