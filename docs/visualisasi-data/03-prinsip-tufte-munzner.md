# 📘 Modul 03: Prinsip Desain Edward Tufte & Kerangka Kerja Tamara Munzner

## 🎯 Capaian Pembelajaran (Sub-CPMK 1)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memahami dan mengkalkulasi metrik **Data-Ink Ratio** serta mengeliminasi **Chartjunk**.
2. Menghitung **Lie Factor** untuk menjamin integritas grafis (*Graphical Integrity*).
3. Menganalisis desain visualisasi menggunakan kerangka kerja bertingkat **Tamara Munzner (*What-Why-How Model*)**.
4. Menerapkan teknik *Small Multiples* untuk visualisasi data multivariat kompleks.

---

## 1. Prinsip Desain Analitis Edward Tufte

Edward Tufte (Profesor Emeritus Universitas Yale) meletakkan fondasi filosofis modern mengenai grafika kuantitatif melalui bukunya *The Visual Display of Quantitative Information*.

### A. Data-Ink Ratio (Rasio Tinta Data)
Tufte merumuskan bahwa setiap tetes tinta pada kertas (atau pixel pada layar komputer) harus digunakan untuk menampilkan informasi substantif data.

::: info 📐 Formula: Data-Ink Ratio (Edward Tufte)
**Data-Ink Ratio** = **Tinta / Piksel Data Kunci** ÷ **Total Tinta / Piksel Seluruh Grafik**

* **Nilai Ideal:** Mendekati **1.0** (100% elemen visual difokuskan untuk menampilkan data substantif).
* **Rasio Rendah:** Menunjukkan visualisasi dipenuhi elemen dekoratif tidak penting (*chartjunk*).
:::

**Aturan Emas Tufte:**
- Maksimalkan rasio data-ink (mendekati **1.0**).
- Hapus tinta non-data (*erase non-data-ink*).
- Hapus tinta data yang berlebihan atau redundan (*erase redundant data-ink*).

### B. Eliminasi Chartjunk (Sampah Visual)
*Chartjunk* adalah elemen visual dekoratif yang tidak menambah nilai analisis data namun membebani kognisi audiens, seperti:
- Efek 3D semu pada diagram batang atau diagram lingkaran (*3D pseudo-perspective*).
- Pola arsir (*moiré vibration patterns*) yang memusingkan mata.
- Garis kisi-kisi (*gridlines*) yang terlalu tebal dan gelap.
- Gambar latar belakang kartun yang mengalihkan perhatian dari data.

### C. Lie Factor & Integritas Grafis
Visualisasi harus merepresentasikan proporsi angka yang jujur secara geometris.

::: info 📐 Formula: Lie Factor (Integritas Grafis)
**Lie Factor** = **Persentase Efek Ukuran pada Grafik** ÷ **Persentase Efek Riil pada Data Tabular**

* **Lie Factor = 1.0** → Grafik objektif, jujur, dan proporsional.
* **Lie Factor > 1.05** → Grafik melebih-lebihkan realitas perubahan data (*exaggeration / misleading*).
* **Lie Factor < 0.95** → Grafik meremehkan perubahan data riil (*understatement*).
:::

---

## 2. Kerangka Kerja Tamara Munzner: Model What-Why-How

Tamara Munzner (Universitas British Columbia) merumuskan kerangka kerja sistematis untuk merancang visualisasi analitik melalui 3 pertanyaan mendasar:

```mermaid
flowchart TD
    A["1. WHAT: Karakteristik Data<br>• Tipe Data: Nominal, Ordinal, Kuantitatif<br>• Struktur Data: Tabel, Jaringan, Spasial"] --> B["2. WHY: Tugas Pengguna (Task Abstraction)<br>• Tindakan: Discover, Present, Query, Explore<br>• Target: Tren, Outlier, Korelasi, Distribusi"]
    B --> C["3. HOW: Rancangan Visual (Encoding)<br>• Visual Mark: Titik, Garis, Area<br>• Visual Channel: Posisi, Ukuran, Warna, Orientasi"]

    style A fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style B fill:#fdf4ff,stroke:#c084fc,stroke-width:2px
    style C fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

### Hierarki Keefektifan Saluran Visual (Visual Channels) untuk Data Kuantitatif:
1. **Posisi pada Skala Umum (*Position on Common Scale*)** $	o$ *Tingkat Akurasi Tertinggi*
2. **Posisi pada Skala Tidak Sejajar (*Position on Unaligned Scale*)**
3. **Panjang Batang (*Length / 1D Size*)**
4. **Sudut & Kemiringan (*Angle / Slope*)**
5. **Luas Area 2D (*Area 2D*)**
6. **Kedalaman 3D (*Volume 3D*)** $	o$ *Tingkat Akurasi Rendah*
7. **Saturasi & Kecerahan Warna (*Color Luminance*)** $	o$ *Hanya untuk estimasi kasar*