# 📋 Rencana Pembelajaran Semester (RPS) — Data Warehouse IFR237

## 🏛️ RANCANGAN PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
### PROGRAM STUDI S-1 INFORMATIKA — FAKULTAS SAINS DAN TEKNOLOGI
### UNIVERSITAS UBUDIYAH INDONESIA

---

### A. IDENTITAS MATA KULIAH

| Komponen | Keterangan |
| :--- | :--- |
| **Mata Kuliah** | **Data Warehouse** |
| **Kode Mata Kuliah** | `IFR237` |
| **Bobot SKS** | **3 SKS** (2 SKS Teori / 1 SKS Praktikum) |
| **Semester / Tahun Akademik** | IV (Empat) / **2026 Ganjil** |
| **Program Studi** | S-1 Informatika |
| **Rumpun MK** | Basis Data & Sains Data |
| **Dosen Pengembang RPS** | **Mahendar Dwi Payana, S.ST., M.T.** |
| **Koordinator RMK** | Desita Ria Yusian TB, S.ST., M.T. |
| **Ketua Program Studi** | M. Bayu Wibawa, S.Kom., MMSI |
| **Prasyarat** | Basis Data (`IFR222`), Algoritma & Pemrograman, Statistika |
| **Jumlah Pertemuan** | **8 pertemuan** |
| **Beban Waktu** | TM: 2×50' + P: 1×170' per pertemuan |

---

### B. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

| Kode CPL | Rumusan Capaian Pembelajaran Lulusan |
| :--- | :--- |
| **CPL01** | **Pengetahuan:** Menguasai konsep basis data, pemodelan dimensional, arsitektur data warehouse, dan teknologi Business Intelligence. |
| **CPL03** | **Problem Solving:** Mampu menerjemahkan kebutuhan bisnis menjadi rancangan data warehouse yang tepat dan dapat dipertanggungjawabkan. |
| **CPL04** | **Solusi Rekayasa Komputasi:** Mampu membangun ETL, skema dimensional, query OLAP, dan optimasi performa pada platform data warehouse. |
| **CPL05** | **Inovasi & Analitik:** Mampu memanfaatkan data warehouse untuk analitik, pelaporan, dan pengambilan keputusan berbasis data. |
| **CPL08** | **Etika & Sikap:** Menerapkan tata kelola, kualitas data, keamanan, privasi, dan integritas akademik. |

---

### C. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK) & SUB-CPMK

| Kode CPMK | Deskripsi CPMK | CPL |
| :--- | :--- | :--- |
| **CPMK 1** | Menjelaskan konsep data warehouse, Business Intelligence, OLTP vs OLAP, serta arsitektur dan evolusi platform data. | CPL01 |
| **CPMK 2** | Merancang model dimensional (fact, dimension, grain, star/snowflake) dan menangani perubahan dimensi (SCD). | CPL01, CPL03 |
| **CPMK 3** | Membangun pipeline ETL/ELT yang idempoten, teruji, dan menjaga kualitas data. | CPL03, CPL04 |
| **CPMK 4** | Mengimplementasikan query OLAP, optimasi performa, dan layanan BI pada data warehouse. | CPL04, CPL05 |
| **CPMK 5** | Menerapkan tata kelola, keamanan, privasi, dan menyajikan proyek data warehouse end-to-end. | CPL05, CPL08 |

| Kode Sub-CPMK | Rumusan Sub-CPMK | CPMK | Pertemuan |
| :--- | :--- | :---: | :---: |
| **Sub-CPMK 1** | Menjelaskan karakteristik data warehouse, perbedaan OLTP/OLAP, komponen BI, serta memetakan kebutuhan bisnis ke solusi DW. | CPMK 1 | 1 |
| **Sub-CPMK 2** | Menganalisis arsitektur DW (Inmon vs Kimball) dan menyusun bus matrix serta deklarasi grain. | CPMK 1, CPMK 2 | 2 |
| **Sub-CPMK 3** | Merancang fact table, dimension table, surrogate key, dan star schema yang sesuai grain bisnis. | CPMK 2 | 3 |
| **Sub-CPMK 4** | Menerapkan snowflake/galaxy serta SCD Tipe 2 untuk menjaga histori dimensi. | CPMK 2 | 4 |
| **Sub-CPMK 5** | Membangun ETL incremental yang idempoten, menangani kualitas data, dan mencatat kegagalan. | CPMK 3 | 5 |
| **Sub-CPMK 6** | Menulis query OLAP (roll-up, drill-down, window function) untuk menjawab pertanyaan bisnis. | CPMK 4 | 6 |
| **Sub-CPMK 7** | Mengoptimasi performa DW (index, partisi, materialized view) dan membangun transformasi dengan dbt. | CPMK 4 | 7 |
| **Sub-CPMK 8** | Menyajikan proyek DW end-to-end dengan tata kelola, keamanan, privasi, dan evaluasi biaya. | CPMK 5 | 8 |

---

### D. RANCANGAN PEMBELAJARAN MINGGUAN (8 PERTEMUAN)

| **P** | **Sub-CPMK** | **Bahan Kajian (Materi Pokok)** | **Bentuk & Metode Pembelajaran** | **Estimasi Waktu** | **Kriteria & Bentuk Penilaian** | **Bobot** |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| **1** | Sub-CPMK 1 | **Fondasi DW & BI:** definisi Inmon, OLTP vs OLAP, mengapa DW dipisahkan, komponen BI, data mart/ODS/lake, evolusi platform, use case industri, pengenalan tools. | Kuliah interaktif, diskusi kasus, demo environment | TM: 2×50'<br>P: 1×170' | Kuis konsep; **T1**: analisis kasus OLTP→OLAP & profil data | **6%** |
| **2** | Sub-CPMK 2 | **Arsitektur & Pemodelan Konseptual:** Inmon top-down vs Kimball bottom-up, staging & presentation layer, bus matrix, requirement gathering, 4 langkah Kimball, deklarasi grain. | Problem-based learning, workshop bus matrix | TM: 2×50'<br>P: 1×170' | **T2**: bus matrix + grain statement + pertanyaan bisnis | **6%** |
| **3** | Sub-CPMK 3 | **Dimensional Modeling:** fact table & jenisnya, dimension table, surrogate vs natural key, star schema, additivity, degenerate/junk/role-playing dimension, DDL PostgreSQL. | Kuliah, perancangan skema, praktikum DDL | TM: 2×50'<br>P: 1×170' | **T3**: star schema retail + data sampel + query validasi | **6%** |
| **4** | Sub-CPMK 4 | **Snowflake, Galaxy & SCD:** normalisasi dimensi, star vs snowflake, conformed dimension, galaxy schema, SCD Tipe 0–6, late-arriving dimension, bridge table. | Studi kasus, live coding SCD2 | TM: 2×50'<br>P: 1×170' | **T4**: implementasi SCD2 + query point-in-time; **UTS take-home dirilis** | **6%** |
| **5** | Sub-CPMK 5 | **ETL & Kualitas Data:** full vs incremental, CDC, staging, transformasi, deduplikasi, upsert/merge, reject table, rekonsiliasi, orkestrasi, logging & retry. | Workshop ETL, praktikum data quality | TM: 2×50'<br>P: 1×170' | **T5**: ETL incremental + 5 quality checks; **UTS dikumpulkan** | **6%** |
| **6** | Sub-CPMK 6 | **OLAP & SQL Analytics:** kubus, roll-up, drill-down, slice/dice, pivot, GROUPING SETS/CUBE/ROLLUP, window functions, YTD, moving average, share of total. | Praktikum SQL intensif, studi kasus BI | TM: 2×50'<br>P: 1×170' | Review UTS; **Milestone proyek 1**: 8 query OLAP + insight | — |
| **7** | Sub-CPMK 7 | **Implementasi & Optimasi:** physical design, index, partisi, materialized view, columnar/cloud DW, dbt models & tests, EXPLAIN ANALYZE, tuning workflow, biaya. | Workshop tuning, praktikum dbt | TM: 2×50'<br>P: 1×170' | **Milestone proyek 2**: optimasi terbukti + model dbt + dokumentasi | — |
| **8** | Sub-CPMK 8 | **Capstone, Tata Kelola & UAS:** integrasi end-to-end, metadata & lineage, ownership, keamanan & privasi (UU PDP), retensi, biaya, anti-pattern, demo dan pertanggungjawaban. | Presentasi, demo, peer review | TM: 2×50'<br>P: 1×170' | **UAS**: demo DW, dashboard/query, laporan, tanya jawab | **35%** |
| | | | **Ujian Tengah Semester (take-home)** | 120 menit | Studi kasus: desain + implementasi + justifikasi | **25%** |
| | | | **Partisipasi, kuis & kehadiran** | Sepanjang semester | Kehadiran ≥ 75%, kuis, kontribusi lab | **10%** |
| | | | **TOTAL BOBOT** | | | **100%** |

> **Catatan:** T1–T5 masing-masing 6% (total 30%). UTS bersifat *take-home* dan dikumpulkan pada Pertemuan 5. Proyek akhir dikerjakan berkelompok (3–4 orang) dengan penilaian individu melalui tanya jawab dan kontribusi Git.

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

---

### F. RUBRIK PENILAIAN

#### F.1 Tugas Terstruktur (T1–T5)

| Aspek | Bobot | Kriteria |
| :--- | :---: | :--- |
| Kebenaran hasil | 40% | Skema/query/ETL sesuai spesifikasi, edge case ditangani |
| Kualitas rancangan & kode | 20% | Normalisasi tepat, penamaan konsisten, SQL terbaca |
| Pengujian & reproduksibilitas | 20% | Ada validasi, dapat dijalankan ulang, dokumentasi |
| Dokumentasi & analisis | 20% | Diagram, data dictionary, penjelasan trade-off |

#### F.2 UTS Take-Home

| Aspek | Bobot | Kriteria |
| :--- | :---: | :--- |
| Analisis kebutuhan & grain | 30% | Pertanyaan bisnis jelas, grain tepat, dimensi/fakta konsisten |
| Implementasi skema & ETL | 40% | DDL berjalan, data benar, integritas terjaga |
| Kualitas rekayasa | 20% | Test, struktur repo, README, reproducibility |
| Presentasi tertulis | 10% | Kejelasan, sistematika, sitasi |

#### F.3 Proyek Akhir (UAS)

| Aspek | Bobot | Kriteria |
| :--- | :---: | :--- |
| Problem framing & requirement | 15% | Kebutuhan bisnis nyata, KPI, ruang lingkup |
| Model dimensional | 20% | Bus matrix, star/snowflake, grain, SCD |
| ETL & kualitas data | 20% | Incremental, idempoten, quality checks, rekonsiliasi |
| OLAP & serving | 15% | Query analitik benar, dashboard/API berfungsi |
| Optimasi & biaya | 10% | Index/partisi/materialized view, bukti performa |
| Tata kelola & keamanan | 10% | Metadata, lineage, akses, PII, retensi |
| Demo & dokumentasi | 10% | One command, runbook, demo lancar, tanya jawab |

---

### G. KEBIJAKAN PERKULIAHAN

1. **Kehadiran:** minimal **75%** dari 8 pertemuan. Mahasiswa dengan kehadiran kurang tidak berhak mengikuti UAS kecuali ada alasan medis/force majeure yang sah.
2. **Keterlambatan tugas:** pengurangan **10% per hari** (maksimal 3 hari); setelah itu tugas tidak diterima kecuali disepakati sebelumnya.
3. **Integritas akademik:** kode dan laporan harus karya sendiri/kelompok. Plagiarisme mengakibatkan nilai nol dan proses sesuai kebijakan akademik.
4. **Penggunaan AI:** diperbolehkan sebagai alat bantu dengan **disclosure** pada bagian *Acknowledgements*. Mahasiswa wajib mampu menjelaskan setiap baris SQL/kode yang dikumpulkan.
5. **Komunikasi:** pertanyaan di luar kelas melalui forum/LMS; respons maksimal 1×24 jam pada hari kerja.
6. **Perangkat:** wajib membawa laptop dengan PostgreSQL/Docker/Python terpasang untuk sesi praktikum.
7. **Etika data:** dataset yang digunakan tidak boleh memuat data pribadi nyata tanpa izin; gunakan data sintetis/anonymized.

---

### H. REFERENSI

**Utama:**
1. Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit* (3rd ed.). Wiley.
2. Inmon, W. H. (2005). *Building the Data Warehouse* (4th ed.). Wiley.
3. Adamson, C. (2010). *Star Schema: The Complete Reference*. McGraw-Hill.
4. Golfarelli, M., & Rizzi, S. (2018). *Data Warehouse Design* (2nd ed.). McGraw-Hill.

**Pendukung:**
5. Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering*. O'Reilly Media.
6. Kimball, R., & Ross, M. (2013). *The Kimball Group Reader* (2nd ed.). Wiley.
7. Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.
8. Dokumentasi resmi PostgreSQL, dbt, DuckDB, dan Metabase.

---

### I. CATATAN PENYESUAIAN 8 PERTEMUAN

Karena mata kuliah diselenggarakan dalam **8 pertemuan**, cakupan materi reguler 16 minggu dipadatkan sebagai berikut:

| Cakupan Reguler (16 minggu) | Dipadatkan ke |
| :--- | :---: |
| Pengantar DW & BI, OLTP vs OLAP | P1 |
| Arsitektur DW, Inmon vs Kimball, requirement | P2 |
| Dimensional modeling, fact/dimension, star schema | P3 |
| Snowflake, galaxy, SCD | P4 |
| ETL & data quality | P5 |
| OLAP & SQL analytics | P6 |
| Implementasi, tuning, dbt, modern DW | P7 |
| Capstone, governance, keamanan, biaya | P8 |

Pendalaman dilakukan melalui **tugas dan proyek**, bukan menambah jam tatap muka. Mahasiswa diharapkan mengalokasikan waktu belajar mandiri ±4–6 jam per pertemuan.

---

**Disahkan oleh:**

| Disusun oleh | Diperiksa oleh | Disetujui oleh |
| :---: | :---: | :---: |
| **Mahendar Dwi Payana, S.ST., M.T.**<br>Dosen Pengampu | **Desita Ria Yusian TB, S.ST., M.T.**<br>Koordinator RMK | **M. Bayu Wibawa, S.Kom., MMSI**<br>Ketua Program Studi |
