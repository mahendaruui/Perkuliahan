# 🚀 Modul 15: Integrasi Proyek Capstone Visualisasi Data

## 🎯 Capaian Pembelajaran (Sub-CPMK 3 & 4)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Mengintegrasikan seluruh kompetensi teori dan teknis (Modul 1 s.d. 14) ke dalam satu aplikasi dashboard analitik terpadu.
2. Memilih dan menyelesaikan persoalan data nyata dari 4 pilihan domain industri (*Kesehatan Publik, Finansial & Risiko, E-Commerce & RFM, Lingkungan & Bencana*).
3. Membangun aplikasi web dashboard multi-halaman mandiri (*Streamlit*) yang responsif, terintegrasi peta geospasial, dan model AI/ML.
4. Menerapkan standar kode bersih (*Clean Code*), arsitektur repositori modular, dan publikasi repositori GitHub profesional.

---

## 📋 Empat Pilihan Domain Studi Kasus Industri

Setiap kelompok (atau individu) wajib memilih salah satu dari 4 domain studi kasus berikut:

```mermaid
flowchart TD
    subgraph PilihanDomain["🏛️ 4 Domain Pilihan Capstone Project"]
        D1["🏥 <b>Domain A: Kesehatan Publik & Epidemiologi Spasial</b><br>• Analisis persebaran penyakit/stunting per kabupaten<br>• Peta Choropleth interaktif & prediksi tren mingguan"]
        D2["💰 <b>Domain B: Finansial, Saham & Manajemen Risiko</b><br>• Dashboard portofolio investasi & volatilitas pasar saham<br>• Candlestick OHLC interaktif & matriks korelasi aset"]
        D3["🛒 <b>Domain C: E-Commerce & Segmentasi Pelanggan (RFM)</b><br>• Analisis Recency, Frequency, Monetary pelanggan<br>• Visualisasi klaster 3D PCA & corong penjualan (Funnel)"]
        D4["🌍 <b>Domain D: Kualitas Lingkungan & Sensor Kebencanaan</b><br>• Monitoring polusi udara PM2.5 / sensor hidrologi banjir<br>• Heatmap spasial titik panas & dekomposisi deret waktu"]
    end

    style PilihanDomain fill:#f8fafc,stroke:#334155,stroke-width:2px
    style D1 fill:#eff6ff,stroke:#2563eb,stroke-width:1px
    style D2 fill:#ecfdf5,stroke:#10b981,stroke-width:1px
    style D3 fill:#fdf4ff,stroke:#c084fc,stroke-width:1px
    style D4 fill:#fefce8,stroke:#ca8a04,stroke-width:1px
```

---

## 🏗️ Struktur Arsitektur Repositori Proyek Standar

Struktur folder proyek Capstone wajib mengikuti standar arsitektur modular berikut:

```text
capstone-dataviz-kelompokX/
├── .streamlit/
│   └── config.toml               # Konfigurasi tema warna Streamlit
├── data/
│   ├── raw/                      # Dataset mentah asli
│   └── processed/                # Dataset bersih hasil data wrangling
├── notebooks/
│   └── 01_exploratory_eda.ipynb  # Notebook analisis awal & eksperimen
├── pages/
│   ├── 1_📊_Analitik_Deskriptif.py
│   ├── 2_🗺️_Peta_Geospasial.py
│   └── 3_🤖_Prediksi_dan_Klaster_AI.py
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Modul pemuatan data & caching
│   ├── cleaning.py               # Fungsi imputasi & filter outlier
│   └── viz_helpers.py            # Template kustomisasi grafik Plotly/Matplotlib
├── app.py                        # Berkas utama Streamlit (Landing Dashboard)
├── requirements.txt              # Daftar pustaka Python yang dibutuhkan
└── README.md                     # Dokumentasi proyek, panduan instalasi, & insight
```

---

## ⏱️ Timeline Sprint Pengerjaan Proyek (3 Minggu)

```mermaid
gantt
    title Roadmap Pengerjaan Proyek Capstone Visualisasi Data
    dateFormat  YYYY-MM-DD
    section Sprint 1
    Pencarian Dataset & Formulasi Masalah   :2026-09-01, 4d
    Data Cleaning & Notebook EDA Pandas    :2026-09-05, 5d
    section Sprint 2
    Perancangan Visualisasi Plotly/Folium  :2026-09-10, 5d
    Pembangunan Dashboard Streamlit        :2026-09-15, 6d
    section Sprint 3
    Integrasi Model AI & Polishing UI      :2026-09-21, 4d
    Deployment Cloud & Finalisasi README   :2026-09-25, 4d
```

---

## 📋 Checklist Kualitas Proyek (Quality Gate)

Sebelum mempresentasikan proyek pada Minggu 16 (UAS), pastikan proyek Anda memenuhi kriteria berikut:
- [ ] **Volume Data:** Dataset riil minimal **1.000+ baris data**.
- [ ] **Data-Ink Ratio:** Bebas dari elemen dekoratif tidak bermakna (*chartjunk*), sumbu diagram batang dimulai dari 0.
- [ ] **Aksesibilitas Warna:** Menggunakan palet yang aman bagi penyandang buta warna (*Colorblind Safe*).
- [ ] **Interaktivitas:** Memuat minimal 3 filter interaktif dinamis di *sidebar* yang terhubung langsung ke semua grafik.
- [ ] **Peta Geospasial:** Memuat minimal 1 layer peta Folium interaktif atau Peta Choropleth wilayah.
- [ ] **Komponen AI/ML:** Memuat visualisasi evaluasi model (*Confusion Matrix/ROC*) atau reduksi dimensi (*PCA/t-SNE*).
- [ ] **Publikasi:** Repositori GitHub publik dengan `README.md` terstruktur dan aplikasi ter-deploy di Streamlit Community Cloud.