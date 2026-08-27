# 🎓 Modul 16: Evaluasi Akhir Semester (UAS)

## 🎯 Sasaran Evaluasi Akhir
Evaluasi Akhir Semester (UAS) merupakan puncak penilaian berbasis **Outcome-Based Education (OBE)** yang menguji pencapaian menyeluruh dari:
* **CPMK 1:** Penguasaan teori psikologi persepsi visual, etika grafis Tufte, dan framework Tamara Munzner.
* **CPMK 2:** Kemahiran manipulasi data (*Pandas*) serta perancangan visualisasi statistik (*Matplotlib & Seaborn*).
* **CPMK 3:** Kemampuan membangun visualisasi interaktif (*Plotly*), pemetaan spasial (*Folium*), dan aplikasi dashboard (*Streamlit*).
* **CPMK 4:** Keahlian narasi data (*Data Storytelling*), visualisasi model AI/ML, dan penyajian proyek capstone terpadu.

---

## 📋 Format Pelaksanaan UAS (Bobot: 20% dari Nilai Akhir)

| Komponen Asesmen | Bobot Sesi | Durasi | Metode Pelaksanaan |
| :--- | :---: | :---: | :--- |
| **1. Demonstrasi Live Dashboard Web** | **40%** | 8 Menit | Demonstrasi langsung fitur interaktif, filter dinamis, peta, dan responsivitas aplikasi Streamlit di hadapan penguji. |
| **2. Presentasi & Data Storytelling** | **30%** | 7 Menit | Penyampaian wawasan (*insight*), eliminasi clutter, struktur narasi 3 babak, dan rekomendasi keputusan bisnis. |
| **3. Tanya Jawab & Audit Kode** | **30%** | 10 Menit | Pertanggungjawaban sintaks Python, arsitektur *Clean Code*, penanganan error, dan orisinalitas karya repositori Git. |

---

## 🏆 Rubrik Penilaian Standar UAS Berbasis 4 Pilar OBE

::: tip 🏆 EVALUASI AKHIR SEMESTER (UAS): PROYEK CAPSTONE TERPADU
**Total Bobot Penilaian: 100 Poin (Mewakili 20% dari Nilai Akhir Semester)**
:::

| No | Pilar Kriteria Penilaian | Bobot | Indikator Kompetensi Teknis (Evidence of Learning) |
| :---: | :--- | :---: | :--- |
| **1** | 🌐 **Fungsionalitas & Interaktivitas Web** | **30 Poin** | • Kecepatan & kelancaran widget filter interaktif (*Sidebar, Sliders, Multi-select*)<br>• Pemanfaatan caching `@st.cache_data` yang optimal tanpa latensi berlebih<br>• Tata letak multi-halaman/tabs yang intuitif & bebas dari *runtime crash/error* |
| **2** | 💡 **Ketajaman Insight & Data Storytelling** | **25 Poin** | • Rumusan *The Big Idea* yang jelas dan berbasis bukti kuantitatif<br>• Struktur cerita 3 babak (*Status Quo → Konflik/Anomali → Solusi Terukur*)<br>• Kehadiran anotasi penunjuk fokus (*Direct Labeling*) yang memandu audiens |
| **3** | 📊 **Kualitas Desain Visual & Etika Tufte** | **25 Poin** | • Rasio data-ink tinggi, bebas dari *chartjunk*, 3D semu, dan distorsi sumbu<br>• Integritas grafis terjaga (Lie Factor ≈ 1.0)<br>• Penggunaan palet warna saintifik yang ramah bagi buta warna (*Colorblind Safe*) |
| **4** | 💻 **Kerapian Kode, Git & Dokumentasi** | **20 Poin** | • Kepatuhan kaidah *Clean Code* & modularitas fungsi Python di folder `src/`<br>• Kelengkapan berkas `requirements.txt` dan `config.toml`<br>• Kualitas `README.md` repositori GitHub lengkap dengan petunjuk instalasi |

---

## 📄 Template README.md Repositori GitHub Capstone

Gunakan struktur Markdown berikut sebagai standar dokumentasi repositori GitHub proyek akhir Anda:

```markdown
# 📊 [Nama Judul Proyek Capstone Anda]
> Dashboard Analitik Interaktif Berbasis Streamlit & Python untuk [Sebutkan Masalah Bisnis]

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/username/repo-name/main/app.py)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

## 📌 1. Latar Belakang & The Big Idea
* **Konteks Masalah:** [Jelaskan latar belakang persoalan data secara ringkas]
* **The Big Idea:** [Tuliskan 1 kalimat inti yang memuat wawasan kunci, risiko bisnis, dan rekomendasi aksi]

## 🛠️ 2. Arsitektur Teknologi & Library Stack
* **Bahasa Pemrograman:** Python 3.10+
* **Data Wrangling:** Pandas, NumPy
* **Visualisasi Grafis:** Matplotlib, Seaborn, Plotly Express & Graph Objects
* **Pemetaan Geospasial:** Folium / GeoPandas
* **Machine Learning:** Scikit-Learn (PCA / Classification)
* **Web Framework:** Streamlit

## 🚀 3. Panduan Instalasi & Menjalankan Secara Lokal
```bash
# 1. Clone Repositori
git clone https://github.com/username/capstone-dataviz.git
cd capstone-dataviz

# 2. Buat Virtual Environment & Aktifkan
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
# venv\Scripts\activate  # Untuk Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Jalankan Aplikasi Streamlit
streamlit run app.py
```

## 👥 Anggota Tim Pengembang (Fakultas Sains & Teknologi - UUI)
1. **Nama Mahasiswa 1** - NIM: `2101020001` (Role: Data Engineer & Machine Learning)
2. **Nama Mahasiswa 2** - NIM: `2101020002` (Role: UI/UX & Streamlit Developer)
```