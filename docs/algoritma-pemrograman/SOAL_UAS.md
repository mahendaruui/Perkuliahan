# Minggu 16: Bank Soal & Evaluasi UAS (Capstone Project OBE)

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 7)
- **CPMK Terkait:** CPMK0101 (Konsep Dasar Pemrograman), CPMK0106 (Logika Algoritma & Perancangan)
- **CPL Terkait:** CPL01 (Pengetahuan Teori), CPL08 (Etika & Sikap Profesional), CPL03 (Problem Solving), CPL04 (Solusi Rekayasa)
- **Indikator:** Mahasiswa mampu mengintegrasikan seluruh materi perkuliahan (struktur kontrol, array, fungsi modular, searching, dan sorting) ke dalam solusi program aplikasi mini terpadu berstandar *Clean Code*.
:::

---

## 📋 Rubrik Penilaian Proyek Mini & UAS (Standar OBE)

| Kriteria Penilaian | Indikator Kompetensi | Bobot (%) | Terkait CPMK |
| :--- | :--- | :---: | :--- |
| **1. Logika & Kebenaran Algoritma** | Program bebas dari bug logika, menghasilkan output sesuai spesifikasi kasus, dan menangani validasi input. | **35%** | CPMK0101, CPMK0106 |
| **2. Modularitas & Arsitektur Kode** | Penggunaan fungsi & prosedur yang terisolasi secara bersih (*Single Responsibility*), parameter passing tepat. | **25%** | CPMK0101 |
| **3. Efisiensi Struktur Data & Algoritma** | Pemilihan algoritma pencarian (*Binary Search*) dan pengurutan (*Sorting*) yang tepat dan optimal. | **20%** | CPMK0106 |
| **4. Kualitas Kode & Etika Akademik** | Penamaan variabel intuitif (*camelCase/snake_case*), indentasi rapi, dokumentasi komentar, **bebas plagiarisme (CPL08)**. | **20%** | CPL08, CPMK0101 |

---

## 🎯 Paket Soal Capstone Project: Sistem Manajemen Inventaris & Nilai Terpadu

Rancang dan bangunlah aplikasi konsol interaktif berbasis menu yang mencakup fitur-fitur berikut:

1. **Struktur Data:** Gunakan array / struct untuk menyimpan minimal 10 record data (NPM, Nama, Nilai Tugas, Nilai UTS, Nilai UAS, Nilai Akhir, dan Grade).
2. **Kalkulasi Modular:** Buat fungsi terpisah untuk menghitung Nilai Akhir ($30\% \text{ Tugas} + 35\% \text{ UTS} + 35\% \text{ UAS}$) dan penentuan Grade Mutu.
3. **Fitur Pengurutan (Sorting):** Menu untuk mengurutkan data mahasiswa berdasarkan Nilai Akhir tertinggi (*Descending*) menggunakan algoritma **Insertion Sort** atau **Bubble Sort**.
4. **Fitur Pencarian (Searching):** Menu pencarian mahasiswa berdasarkan NPM menggunakan **Binary Search** (dengan pengurutan NPM terlebih dahulu).
5. **Statistik Kelas:** Menampilkan nilai rata-rata kelas, nilai tertinggi, dan nilai terendah.

---

## 💡 Kunci Penilaian Sukses OBE
- Tuliskan dokumentasi header fungsi dengan jelas (*docstring/comment*).
- Validasi seluruh input pengguna untuk mencegah program mengalami *crash*.
- Demonstrasikan pemahaman alur kerja program saat sesi presentasi dan live coding mandiri.
