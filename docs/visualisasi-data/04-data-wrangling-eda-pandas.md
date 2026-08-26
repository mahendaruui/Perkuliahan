# 📘 Modul 04: Fondasi Data Wrangling & EDA dengan Pandas

## 🎯 Capaian Pembelajaran (Sub-CPMK 2)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memuat, menginspeksi, dan membersihkan dataset tabular mentah menggunakan pustaka **Python Pandas**.
2. Melakukan manipulasi data: filtering, transformasi tipe data, penanganan missing values (*imputation/dropping*), dan deteksi outlier.
3. Melakukan agregasi data multi-tingkat dengan `groupby`, `pivot_table`, dan `melt` untuk merapikan format data (*tidy data*).
4. Menghitung ringkasan statistik deskriptif untuk memandu proses visualisasi data.

---

## 1. Konsep Tidy Data (Data Rapi)

Hadley Wickham mendefinisikan standar struktur data rapi (*tidy data*):
1. Setiap variabel membentuk satu kolom (*Column*).
2. Setiap observasi atau entitas membentuk satu baris (*Row*).
3. Setiap jenis unit observasi membentuk satu tabel (*Table*).

---

## 2. Implementasi Hands-on Python Pandas

```python
import pandas as pd
import numpy as np

# 1. Memuat Dataset
df = pd.read_csv('data_penjualan.csv')

# 2. Inspeksi Cepat & Struktur Memori
print(df.info())
print(df.describe(include='all'))

# 3. Penanganan Missing Values
df['kategori'] = df['kategori'].fillna('Uncategorized')
df['pendapatan'] = df['pendapatan'].fillna(df['pendapatan'].median())

# 4. Transformasi Tipe Data Waktu
df['tanggal'] = pd.to_datetime(df['tanggal'])
df['bulan'] = df['tanggal'].dt.to_period('M')

# 5. Agregasi & Ringkasan Data (Groupby & Pivot)
ringkasan_wilayah = df.groupby(['wilayah', 'kategori'])['pendapatan'].agg(
    total_sales='sum',
    rata_rata='mean',
    transaksi='count'
).reset_index()

print(ringkasan_wilayah.head())
```

---

## 3. Deteksi Outlier Berbasis Rentang Interkuartil (IQR)

```python
def filter_outlier_iqr(data, kolom):
    Q1 = data[kolom].quantile(0.25)
    Q3 = data[kolom].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[kolom] >= lower_bound) & (data[kolom] <= upper_bound)]
```