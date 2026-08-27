# 📝 Modul 08: Evaluasi Tengah Semester (UTS)

## 🎯 Sasaran Evaluasi Komprehensif
Evaluasi Tengah Semester (UTS) menguji penguasaan komprehensif mahasiswa terhadap capaian pembelajaran:
* **Sub-CPMK 1:** Penguasaan teori psikologi persepsi visual, prinsip Gestalt, metrik efisiensi grafis Edward Tufte (*Data-Ink Ratio*, *Lie Factor*), dan kerangka kerja bertingkat Tamara Munzner (*What-Why-How*).
* **Sub-CPMK 2:** Keterampilan rekayasa data (*Data Wrangling*) dengan Pandas serta pembuatan visualisasi analitis berstandar publikasi menggunakan pustaka Python **Matplotlib** (Object-Oriented API) dan **Seaborn**.

---

## 📋 Struktur Pelaksanaan UTS (Bobot: 20% dari Nilai Akhir)

| Sesi Ujian | Fokus Asesmen | Bobot Sesi | Durasi | Metode & Media |
| :---: | :--- | :---: | :---: | :--- |
| **Sesi 1** | **Ujian Teori & Bedah Desain Visual** | **40%** | 45 Menit | Tertulis / CBT (Analisis grafik misleading, hitung Lie Factor, audit Gestalt & Munzner). |
| **Sesi 2** | **Live Coding Test Mandiri di Lab** | **60%** | 75 Menit | Praktikum Komputasi di Lab (Wrangling data tabular mentah & pembuatan 4 grafik publikasi). |

---

## 📚 Contoh Paket Soal Standar UTS

### Sesi 1: Soal Teori & Analisis Kritis Desain (45 Menit)

#### Soal 1: Kalkulasi Lie Factor & Audit Integritas Grafis
Sebuah perusahaan logistik mempublikasikan infografis yang membandingkan pertumbuhan armada pengiriman:
* **Data Riil:** Jumlah armada tahun 2022 adalah **1.000 unit**, dan pada tahun 2024 meningkat menjadi **1.300 unit** ($+30\%$).
* **Representasi Visual:** Grafik menggunakan ilustrasi truk 2D. Panjang truk tahun 2022 digambar $2\text{ cm}$ (luas area $4\text{ cm}^2$), sedangkan truk tahun 2024 digambar dengan panjang $6\text{ cm}$ (luas area $36\text{ cm}^2$, meningkat $+800\%$).

**Tugas Anda:**
1. Hitung nilai **Lie Factor** dari grafik infografis tersebut secara matematis!
2. Jelaskan apakah grafik tersebut melanggar integritas grafis Edward Tufte dan apa rekomendasi perbaikan visual yang tepat.

---

#### Soal 2: Kerangka Kerja Tamara Munzner (What-Why-How)
Diberikan skenario bisnis: *"Manajer operasional rumah sakit ingin menganalisis korelasi antara waktu tunggu pasien di IGD (dalam menit) dengan tingkat kepuasan layanan (skor 1-100) serta melihat apakah ada perbedaan pola antara pasien BPJS dan pasien Umum."*

**Tugas Anda:** Uraikan solusi visualisasi berdasarkan kerangka kerja Tamara Munzner:
- **WHAT:** Sebutkan semua variabel data beserta tipe datanya (Categorical, Ordered, atau Quantitative).
- **WHY:** Identifikasi tugas analitis (*Action*) dan sasaran temuan (*Target*).
- **HOW:** Tentukan jenis tanda (*Marks*) dan saluran visual (*Visual Channels*) yang memiliki tingkat akurasi persepsi tertinggi untuk skenario tersebut.

---

### Sesi 2: Live Coding Test Mandiri di Lab Komputer (75 Menit)

Mahasiswa diberikan sebuah berkas dataset mentah `dataset_evaluasi_uts.csv` (atau skrip generator data sintetis) yang memuat transaksi retail multi-cabang dengan data kotor (*missing values*, outlier, format tanggal acak).

#### Instruksi Pengerjaan Live Coding:
1. **Data Wrangling (Pandas):**
   - Muat dataset dan tampilkan ringkasan struktur memori serta statistik deskriptif.
   - Bersihkan teks inkonsisten dan lakukan imputasi nilai hilang (*missing values*) secara rasional.
   - Deteksi dan lakukan penanganan nilai pencilan (*outliers*) menggunakan metode Rentang Interkuartil (IQR).
   - Ekstrak fitur tanggal menjadi kolom `Bulan` dan `Tahun`.
2. **Visualisasi 1: Analisis Tren Berstandar Publikasi (Matplotlib OO):**
   - Buat grafik garis (*Line Plot*) dengan *Confidence Interval* yang membandingkan performa penjualan bulanan 2 cabang utama.
   - Terapkan eliminasi spines atas & kanan, serta berikan anotasi pada titik penjualan tertinggi.
3. **Visualisasi 2: Komparasi Distribusi Statistik Lanjut (Seaborn):**
   - Buatlah **Split Violin Plot** atau **Boxen Plot** untuk membandingkan distribusi pengeluaran pelanggan antar kategori produk.
4. **Visualisasi 3: Analisis Korelasi Multivariat (Heatmap):**
   - Buat **Correlation Heatmap** ber-masking segitiga atas (*triangular mask*) dengan palet divergen untuk fitur-fitur numerik.
5. **Insight & Storytelling:**
   - Tuliskan 3 butir kesimpulan analitis berbasis wawasan (*actionable insight*) pada sel Markdown notebook Anda.

---

## 🏆 Rubrik Penilaian Objektif UTS Berbasis OBE

::: tip 📊 RUBRIK PENILAIAN LIVE CODING & TEORI UTS (BOBOT: 100 POIN)
:::

| No | Dimensi Kriteria Penilaian | Bobot | Indikator Kompetensi Teknis |
| :---: | :--- | :---: | :--- |
| **1** | 📐 **Ketepatan Teori & Kalkulasi Lie Factor** | **25 Poin** | • Kebenaran rumus matematis & kalkulasi numerik Lie Factor<br>• Kejelasan dekonstruksi framework *What-Why-How* Munzner<br>• Pemahaman ergonomi warna & aksesibilitas buta warna |
| **2** | 🧹 **Kualitas Data Wrangling (Pandas)** | **25 Poin** | • Kebersihan data, ketepatan strategi imputasi missing values<br>• Keakuratan implementasi rumus IQR untuk filter outlier<br>• Ketepatan agregasi multi-tingkat (`groupby`, `pivot_table`) |
| **3** | 📊 **Kualitas Visualisasi Statis & Tufte Aesthetics** | **30 Poin** | • Penggunaan murni Matplotlib OO API (`fig, ax = plt.subplots`)<br>• Penerapan rasio data-ink tinggi & eliminasi total *chartjunk*<br>• Ketepatan pemilihan jenis plot distribusi & korelasi Seaborn<br>• Kehadiran anotasi penunjuk wawasan (*insightful annotation*) |
| **4** | 💡 **Ketajaman Wawasan & Rekomendasi Bisnis** | **20 Poin** | • Narasi analitis yang tajam, logis, dan menjawab tujuan data<br>• Bebas dari interpretasi bias atau asumsi spekulatif |