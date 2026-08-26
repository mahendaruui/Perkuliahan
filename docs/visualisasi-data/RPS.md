# 📋 Rencana Pembelajaran Semester (RPS) Berbasis OBE

## 🏛️ RANCANGAN PEMBELAJARAN SEMESTER (RPS)
### PROGRAM STUDI S-1 INFORMATIKA — FAKULTAS SAINS DAN TEKNOLOGI
### UNIVERSITAS UBUDIYAH INDONESIA

---

### A. IDENTITAS MATA KULIAH

| Komponen | Keterangan |
| :--- | :--- |
| **Mata Kuliah** | **Visualisasi Data** (*Data Visualization*) |
| **Kode Mata Kuliah** | `IFR309` |
| **Bobot SKS** | **3 SKS** (2 SKS Teori / 1 SKS Praktikum Lab) |
| **Semester** | V (Lima) / Ganjil |
| **Rumpun MK** | Sains Data & Informatika Cerdas |
| **Dosen Pengembang RPS** | **Mahendar Dwi Payana, S.ST., M.T.** |
| **Koordinator RMK** | Desita Ria Yusian TB, S.ST., M.T. |
| **Ketua Program Studi** | M. Bayu Wibawa, S.Kom., MMSI |

---

### B. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN PADA MK

| Kode CPL | Rumusan Capaian Pembelajaran Lulusan (CPL) |
| :--- | :--- |
| **CPL01** | **Pengetahuan:** Memiliki pengetahuan komprehensif tentang teori grafika, psikologi persepsi visual manusia (Gestalt), semiotika data, teori warna, dan prinsip efisiensi grafis Tufte. |
| **CPL03** | **Keterampilan Kerja Umum:** Mampu merumuskan persoalan eksplorasi data, melakukan data wrangling, serta memilih representasi visual yang tepat untuk dataset dinamis. |
| **CPL04** | **Keterampilan Khusus:** Mampu merancang, membangun, dan menyajikan solusi visualisasi interaktif, peta geospasial, serta dashboard analitik bisnis (*Business Intelligence*). |
| **CPL05** | **Inovasi AI / Distributed:** Mampu memvisualisasikan data berdimensi tinggi (*High-Dimensional Data*) dengan teknik reduksi dimensi (PCA/t-SNE) dan visualisasi evaluasi model AI/ML. |
| **CPL08** | **Sikap & Etika:** Mematuhi etika integritas data visual (*Graphical Integrity*), bebas dari manipulasi bias (*Lie Factor*), dan menjunjung tinggi orisinalitas karya. |

---

### C. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK) & SUB-CPMK

| Kode CPMK | Deskripsi Capaian Pembelajaran Mata Kuliah | Terkait CPL |
| :--- | :--- | :--- |
| **CPMK 1** | Menguasai teori persepsi visual, prinsip desain grafis analitis (Tufte, Gestalt, Munzner), dan semiotika visual data. | CPL01, CPL08 |
| **CPMK 2** | Mampu mengolah, mentransformasi, dan memvisualisasikan data statistik serta distribusi menggunakan Python (Matplotlib dan Seaborn). | CPL01, CPL03 |
| **CPMK 3** | Mampu membangun visualisasi data interaktif, eksplorasi multivariat, pemetaan geospasial, dan dashboard analitik berbasis web (Plotly, Folium, Streamlit). | CPL03, CPL04 |
| **CPMK 4** | Mampu menyusun narasi data (*Data Storytelling*), memvisualisasikan model AI/Machine Learning, dan mempublikasikan dashboard proyek capstone terpadu. | CPL04, CPL05, CPL08 |

---

### D. RANCANGAN PEMBELAJARAN MINGGUAN (16 MINGGU)

| **Mg** | **Sub-CPMK** | **Bahan Kajian (Materi Pokok)** | **Bentuk & Metode Pembelajaran** | **Estimasi Waktu** | **Kriteria & Bentuk Penilaian** | **Bobot (%)** |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| **1** | Sub-CPMK 1 | **Hakikat & Epistemologi Visualisasi Data**: Definisi, sejarah komputasi visual (Florence Nightingale, John Snow), model komunikasi data, peran visualisasi dalam Data Science. | Kuliah Interaktif, Demonstrasi Galeri Visual | TM: 2x50' <br>P: 1x170' | Partisipasi aktif & resume sejarah visualisasi data (Tugas 1) | **3%** |
| **2** | Sub-CPMK 1 | **Psikologi Persepsi Visual & Teori Gestalt**: Mekanisme penglihatan manusia, memori sensorik, atribut pra-atentif (*Pre-attentive Attributes*), 6 Hukum Gestalt, aksesibilitas warna. | Kuliah Teori, Simulasi Atribut Pra-atentif | TM: 2x50' <br>P: 1x170' | Analisis efektivitas visual & audit warna ramah buta warna | **4%** |
| **3** | Sub-CPMK 1 | **Prinsip Desain Grafis Edward Tufte & Framework Tamara Munzner**: *Data-Ink Ratio*, *Chartjunk*, *Lie Factor*, *Graphical Integrity*, serta kerangka *What-Why-How* Munzner. | Problem-Based Learning, Bedah Kasus Misleading Chart | TM: 2x50' <br>P: 1x170' | Kalkulasi Lie Factor & redrawn chartjunk (Tugas 2) | **4%** |
| **4** | Sub-CPMK 2 | **Fondasi Data Wrangling & Exploratory Data Analysis (EDA)**: Pembersihan data (*cleaning*), agregasi, grouping, handling missing values, transformasi data tabular dengan Pandas. | Live Coding di Lab, Hands-on Jupyter | TM: 2x50' <br>P: 1x170' | Kebenaran transformasi data & ringkasan statistik EDA | **5%** |
| **5** | Sub-CPMK 2 | **Visualisasi Statis Fundamental dengan Matplotlib**: Arsitektur Object-Oriented Matplotlib (`Figure`, `Axes`), kustomisasi grafik, subplot multi-panel, anotasi, export HD. | Praktikum Terbimbing, Live Coding | TM: 2x50' <br>P: 1x170' | Kualitas tata letak subplot OO Matplotlib (Tugas 3) | **4%** |
| **6** | Sub-CPMK 2 | **Visualisasi Statistik & Distribusi Lanjut dengan Seaborn**: Analisis distribusi (Histogram, KDE, ECDF), Box Plot, Violin Plot, Ridge Plot, FacetGrid multi-panel. | Praktikum Komparatif, Studi Kasus Data Riil | TM: 2x50' <br>P: 1x170' | Ketepatan pemilihan plot distribusi & interpretasi statistik | **5%** |
| **7** | Sub-CPMK 2 | **Visualisasi Relasi, Komposisi & Multivariat**: Scatter plot, Heatmap Korelasi, Pair Plot, Bubble Chart, Treemap, Sankey Diagram, Parallel Coordinates. | Praktikum Intensif Lab | TM: 2x50' <br>P: 1x170' | Keakuratan representasi hubungan multivariat (Tugas 4) | **5%** |
| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Tengah Semester (Teori Desain Grafis & Live Coding EDA Mandiri)** | Ujian Tertulis & Live Coding Session | 120 Menit | Rubrik Penilaian Mandiri Teori & Live Coding UTS | **20%** |
| **9** | Sub-CPMK 3 | **Visualisasi Interaktif & Web-Ready dengan Plotly**: Plotly Express, Plotly Graph Objects, hover tooltip kustom, zoom, pan, slider rentang waktu, animasi transisi data. | Collaborative Coding, Praktikum Lab | TM: 2x50' <br>P: 1x170' | Interaktivitas chart & estetika Plotly (Tugas 5) | **4%** |
| **10** | Sub-CPMK 3 | **Visualisasi Data Geospasial & Pemetaan Wilayah**: Koordinat GPS, GeoJSON, Choropleth Map, Heatmap spasial, peta interaktif dengan Folium & GeoPandas. | Praktikum GIS Komputasi | TM: 2x50' <br>P: 1x170' | Peta choropleth interaktif & analisis spasial wilayah | **4%** |
| **11** | Sub-CPMK 3 | **Visualisasi Deret Waktu (Time Series) & Finansial**: Line chart tren multi-skala, Candlestick finansial, Moving Average, Seasonal Decomposition, Stacked Area. | Studi Kasus Data Keuangan / Sensor IoT | TM: 2x50' <br>P: 1x170' | Ketepatan visualisasi pola musiman & tren deret waktu (Tugas 6) | **5%** |
| **12** | Sub-CPMK 4 | **Visualisasi Model Machine Learning & Reduksi Dimensi**: Reduksi dimensi dengan PCA & t-SNE, Confusion Matrix Heatmap, ROC-AUC Curve, Feature Importance. | Eksperimen Visualisasi Model AI | TM: 2x50' <br>P: 1x170' | Kejelasan interpretasi visual model Machine Learning | **5%** |
| **13** | Sub-CPMK 3 | **Pembangunan Dashboard Analitik Interaktif dengan Streamlit**: Arsitektur web Streamlit, widget input, layout multi-kolom, caching data, live deployment dashboard data apps. | Project-Based Learning, Lab Workshop | TM: 2x50' <br>P: 1x170' | Fungsionalitas aplikasi dashboard interaktif (Tugas 7) | **5%** |
| **14** | Sub-CPMK 4 | **Data Storytelling & Komunikasi Bisnis Efektif**: Menghubungkan visualisasi dengan audiens, eliminasi clutter kognitif, teknik *Highlighting Focus*, executive summary. | Workshop Presentasi, Peer Review | TM: 2x50' <br>P: 1x170' | Kualitas narasi data & pengurangan beban kognitif | **4%** |
| **15** | Sub-CPMK 4 | **Integrasi Capstone Project Visualisasi Data**: Asistensi & workshop pembangunan aplikasi dashboard analitik berbasis studi kasus riil industri. | Asistensi Proyek Terbimbing | TM: 2x50' <br>P: 1x170' | Kinerja arsitektur kode & kelengkapan fitur capstone | **5%** |
| **16** | **EVALUASI AKHIR SEMESTER (UAS)** | **Ujian Akhir Semester & Presentasi Capstone Project Visualisasi Data** | Presentasi, Demo Aplikasi & Pertanggungjawaban | 150 Menit | Rubrik Capstone Project & Penguasaan Komprehensif | **20%** |
| | | | **TOTAL BOBOT PENILAIAN** | | | **100%** |

---

### E. SISTEM PENILAIAN & BOBOT MUTU UUI

| Nilai Angka | Nilai Huruf | Bobot Mutu | Kualifikasi Kompetensi |
| :---: | :---: | :---: | :--- |
| **85.00 – 100.00** | **A** | **4.00** | Istimewa / Sangat Kompeten |
| **80.00 – 84.99** | **A-** | **3.75** | Sangat Baik |
| **75.00 – 79.99** | **B+** | **3.50** | Baik Sekali |
| **70.00 – 74.99** | **B** | **3.00** | Baik / Kompeten |
| **65.00 – 69.99** | **B-** | **2.75** | Cukup Baik |
| **60.00 – 64.99** | **C+** | **2.50** | Cukup |
| **55.00 – 59.99** | **C** | **2.00** | Lulus Standar Minimum |
| **45.00 – 54.99** | **D** | **1.00** | Kurang (Wajib Mengulang) |
| **0.00 – 44.99** | **E** | **0.00** | Gagal / Tidak Lulus |