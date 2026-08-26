# 📘 Modul 06: Visualisasi Statistik & Distribusi Lanjut dengan Seaborn

## 🎯 Capaian Pembelajaran (Sub-CPMK 2)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memahami keunggulan pustaka **Seaborn** dalam memodelkan estimasi statistik secara otomatis.
2. Memvisualisasikan distribusi univariat dan bivariat: Histogram, Kernel Density Estimation (KDE), ECDF Plot.
3. Membandingkan sebaran statistik multi-grup menggunakan Box Plot, Violin Plot, dan Stripplot.
4. Menerapkan `FacetGrid`, `catplot`, dan `displot` untuk analisis multi-kondisi.

---

## 1. Anatomi Plot Distribusi Kunci

<div style="margin: 20px 0;">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
    
    <div style="background: var(--vp-c-bg-soft); border-left: 5px solid #3b82f6; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
      <h4 style="margin: 0 0 6px 0; color: #2563eb; font-weight: bold; font-size: 1.05rem;">
        📈 1. Histogram & KDE Plot
      </h4>
      <p style="margin: 0; font-size: 0.92rem; color: var(--vp-c-text-2); line-height: 1.5;">
        Menilai bentuk sebaran frekuensi, kemiringan data (<em>skewness</em>), modus, dan menguji kurva normalitas data kontinu.
      </p>
    </div>

    <div style="background: var(--vp-c-bg-soft); border-left: 5px solid #a855f7; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
      <h4 style="margin: 0 0 6px 0; color: #9333ea; font-weight: bold; font-size: 1.05rem;">
        📦 2. Box Plot (Box & Whisker)
      </h4>
      <p style="margin: 0; font-size: 0.92rem; color: var(--vp-c-text-2); line-height: 1.5;">
        Menampilkan ringkasan 5 angka statistik (Median, Kuartil Q1 & Q3, rentang IQR) serta mendeteksi titik pencilan (<em>outlier</em>).
      </p>
    </div>

    <div style="background: var(--vp-c-bg-soft); border-left: 5px solid #10b981; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
      <h4 style="margin: 0 0 6px 0; color: #059669; font-weight: bold; font-size: 1.05rem;">
        🎻 3. Violin Plot
      </h4>
      <p style="margin: 0; font-size: 0.92rem; color: var(--vp-c-text-2); line-height: 1.5;">
        Menggabungkan ketajaman kuartil box plot dengan estimasi kontur kepadatan probabilitas (<em>Kernel Density Estimation</em>).
      </p>
    </div>

    <div style="background: var(--vp-c-bg-soft); border-left: 5px solid #f59e0b; border-radius: 10px; padding: 16px 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
      <h4 style="margin: 0 0 6px 0; color: #d97706; font-weight: bold; font-size: 1.05rem;">
        📉 4. ECDF Plot (Empirical CDF)
      </h4>
      <p style="margin: 0; font-size: 0.92rem; color: var(--vp-c-text-2); line-height: 1.5;">
        Menyajikan fungsi distribusi kumulatif empiris nyata dari 0% ke 100% tanpa bias pemilihan jumlah/lebar <em>bin</em>.
      </p>
    </div>

  </div>
</div>

---

## 2. Implementasi Python Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set tema estetika Seaborn
sns.set_theme(style="ticks", palette="muted")
tips = sns.load_dataset("tips")

# 1. Multi-Plot Komparasi Distribusi: Boxen + Stripplot
fig, axes = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

# Violin Plot dengan Titik Data Individu
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True,
               inner="quart", palette={"Yes": "#38bdf8", "No": "#f43f5e"}, ax=axes[0])
axes[0].set_title("Distribusi Total Tagihan (Violin Split by Smoker)", fontweight='bold')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# ECDF Plot Komparatif
sns.ecdfplot(data=tips, x="total_bill", hue="time", palette="crest", ax=axes[1])
axes[1].set_title("Empirical Cumulative Distribution Function (ECDF)", fontweight='bold')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
```