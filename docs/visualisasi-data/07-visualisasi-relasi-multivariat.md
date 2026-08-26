# 📘 Modul 07: Visualisasi Korelasi, Matriks & Multivariat

## 🎯 Capaian Pembelajaran (Sub-CPMK 2)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Menganalisis korelasi antar variabel kuantitatif menggunakan **Matriks Korelasi (Correlation Heatmap)**.
2. Memvisualisasikan data multidimensi menggunakan **Pair Plot**, **Bubble Chart**, dan **Parallel Coordinates**.
3. Menyajikan hubungan hierarki dan aliran proporsi data menggunakan **Treemap** dan **Sankey Diagram**.
4. Menghindari jebakan korelasi semu (*Spurious Correlation*) dan paradoks Simpson (*Simpson's Paradox*).

---

## 1. Heatmap Matriks Korelasi (Pearson / Spearman)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
df = sns.load_dataset('penguins').dropna()
corr = df.select_dtypes(include=[np.number]).corr(method='pearson')

# Membuat Mask untuk Segitiga Atas (Upper Triangle) demi efisiensi visual Tufte
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
sns.heatmap(corr, mask=mask, cmap='vlag', vmin=-1, vmax=1, annot=True,
            fmt='.2f', square=True, linewidths=1.5, cbar_kws={"shrink": .8})

ax.set_title("Matriks Korelasi Morfologi Pinguin", fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
```

---

## 2. Visualisasi Hierarki: Treemap

Treemap merepresentasikan data bersarang (*nested hierarchical data*) sebagai sekumpulan persegi panjang dengan ukuran luas yang proporsional terhadap nilai kuantitatifnya.

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=['continent', 'country'], values='pop',
                 color='lifeExp', hover_data=['iso_alpha'],
                 color_continuous_scale='RdBu',
                 title='Populasi & Harapan Hidup Global Berdasarkan Benua (2007)')
fig.show()
```