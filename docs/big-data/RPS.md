# 📋 Rencana Pembelajaran Semester (RPS) — Big Data IFR229

## 🏛️ RANCANGAN PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
### PROGRAM STUDI S-1 INFORMATIKA — FAKULTAS SAINS DAN TEKNOLOGI
### UNIVERSITAS UBUDIYAH INDONESIA

---

### A. IDENTITAS MATA KULIAH

| Komponen | Keterangan |
| :--- | :--- |
| **Mata Kuliah** | **Big Data** |
| **Kode Mata Kuliah** | `IFR229` |
| **Bobot SKS** | **3 SKS** (2 SKS Teori / 1 SKS Praktikum) |
| **Semester / Tahun Akademik** | VI (Enam) / **2026 Ganjil** |
| **Kelas** | **RPL (Rekognisi Pembelajaran Lampau)** |
| **Rumpun MK** | Sains Data & Sistem Terdistribusi |
| **Dosen Pengembang RPS** | **Mahendar Dwi Payana, S.ST., M.T.** |
| **Koordinator RMK** | Desita Ria Yusian TB, S.ST., M.T. |
| **Ketua Program Studi** | M. Bayu Wibawa, S.Kom., MMSI |
| **Prasyarat** | Basis Data, Algoritma & Pemrograman, Pemrograman Berorientasi Objek |
| **Jumlah Pertemuan** | **8 pertemuan** |
| **Beban Waktu** | TM: 2×50' + P: 1×170' per pertemuan |

---

### A.1 PENDEKATAN PEMBELAJARAN KELAS RPL

**RPL (Rekognisi Pembelajaran Lampau)** mengakui pengalaman kerja, pelatihan nonformal/informal, dan pendidikan formal sebelumnya sebagai SKS. Pembelajaran dirancang **theory-first** dan menghargai pengalaman peserta:

1. **Konsep sebelum alat:** setiap pertemuan dimulai dari masalah, prinsip, dan trade-off; tools dipelajari sebagai implementasi.
2. **Pengalaman sebagai kasus:** mahasiswa menganalisis sistem/laporan nyata dari tempat kerja.
3. **Praktik sebagai verifikasi:** laboratorium bersifat pengayaan, bukan syarat tunggal kompetensi.
4. **Refleksi terstruktur:** mahasiswa menjelaskan keputusan teknis dan kaitannya dengan CPMK.
5. **Penilaian berimbang:** 60% konsep/penalaran, 40% penerapan.
6. **Fleksibilitas konteks:** studi kasus dapat disesuaikan dengan domain kerja masing-masing.

> **Bacaan wajib:** **[Buku Teori Big Data untuk Kelas RPL](/big-data/TEORI-RPL)** — delapan bab teori dengan analogi, studi kasus kerja, dan pertanyaan refleksi.

---

### B. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

| Kode CPL | Rumusan Capaian Pembelajaran Lulusan |
| :--- | :--- |
| **CPL01** | **Pengetahuan:** Menguasai konsep sistem terdistribusi, penyimpanan data skala besar, model pemrosesan batch/streaming, dan arsitektur data modern. |
| **CPL03** | **Problem Solving:** Mampu menganalisis kebutuhan data, memilih arsitektur, serta merancang solusi untuk volume, kecepatan, dan variasi data yang tinggi. |
| **CPL04** | **Solusi Rekayasa Komputasi:** Mampu membangun pipeline data, aplikasi analitik, dan integrasi layanan data yang andal, teruji, dan dapat di-deploy. |
| **CPL05** | **Inovasi & Kecerdasan Artifisial:** Mampu menerapkan analitik dan machine learning terdistribusi untuk menghasilkan wawasan dan layanan cerdas. |
| **CPL08** | **Etika & Sikap:** Menerapkan tata kelola data, keamanan, privasi (UU PDP), integritas akademik, dan pertimbangan biaya dalam rekayasa sistem data. |

---

### C. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK) & SUB-CPMK

| Kode CPMK | Deskripsi CPMK | CPL |
| :--- | :--- | :--- |
| **CPMK 1** | Menjelaskan karakteristik big data, evolusi arsitektur data, serta peran rekayasa perangkat lunak dalam sistem data modern. | CPL01 |
| **CPMK 2** | Merancang penyimpanan dan pemrosesan batch terdistribusi menggunakan HDFS, MapReduce, Hive, dan Apache Spark. | CPL01, CPL03, CPL04 |
| **CPMK 3** | Membangun integrasi data NoSQL dan streaming event dengan MongoDB, Cassandra, dan Apache Kafka. | CPL03, CPL04 |
| **CPMK 4** | Mengotomasi pipeline data, menjamin kualitas data, serta menerapkan analitik dan machine learning terdistribusi. | CPL04, CPL05 |
| **CPMK 5** | Menerapkan tata kelola, keamanan, privasi, dan optimasi biaya pada proyek sistem big data. | CPL08 |

| Kode Sub-CPMK | Rumusan Sub-CPMK | CPMK | Pertemuan |
| :--- | :--- | :---: | :---: |
| **Sub-CPMK 1** | Menjelaskan 5V, evolusi arsitektur data, komponen arsitektur modern, dan peran engineer dalam ekosistem big data. | CPMK 1 | 1 |
| **Sub-CPMK 2** | Menganalisis trade-off CAP/PACELC serta merancang penyimpanan terdistribusi, format file, dan strategi partisi. | CPMK 2 | 2 |
| **Sub-CPMK 3** | Mengimplementasikan pemrosesan batch dengan MapReduce, YARN, dan Hive serta mendiagnosis bottleneck-nya. | CPMK 2 | 3 |
| **Sub-CPMK 4** | Membangun pipeline Spark (RDD/DataFrame/SQL) yang benar, efisien, dan dapat diuji. | CPMK 2 | 4 |
| **Sub-CPMK 5** | Merancang model data NoSQL dan integrasi event streaming yang idempoten serta tahan kegagalan. | CPMK 3 | 5 |
| **Sub-CPMK 6** | Mengotomasi pipeline dengan orkestrasi, uji kualitas data, observabilitas, dan CI/CD. | CPMK 4 | 6 |
| **Sub-CPMK 7** | Membangun pipeline machine learning terdistribusi dan mengevaluasi kesiapan produksinya. | CPMK 4 | 7 |
| **Sub-CPMK 8** | Menyajikan proyek end-to-end dengan tata kelola, keamanan, privasi, dan optimasi biaya yang terdokumentasi. | CPMK 5 | 8 |

---

### D. RANCANGAN PEMBELAJARAN MINGGUAN (8 PERTEMUAN)

| **P** | **Sub-CPMK** | **Bahan Kajian (Materi Pokok)** | **Bentuk & Metode Pembelajaran** | **Estimasi Waktu** | **Kriteria & Bentuk Penilaian** | **Bobot** |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| **1** | Sub-CPMK 1 | **Fondasi & Lanskap Big Data:** definisi dan 5V, keterbatasan RDBMS, evolusi data warehouse → Hadoop → lakehouse, lapisan arsitektur data modern, peran data engineer vs software engineer, use case industri. | Kuliah konseptual, diskusi pengalaman kerja, demonstrasi ringan | TM: 2×50'<br>P: 1×170' | Kuis konsep; **T1**: estimasi kapasitas & klasifikasi beban batch/stream | **6%** |
| **2** | Sub-CPMK 2 | **Arsitektur Terdistribusi & Penyimpanan:** replikasi, partisi, CAP/PACELC, HDFS (NameNode/DataNode/block), object storage, data lake vs warehouse vs lakehouse, Parquet/Avro/ORC, partitioning & medallion architecture. | Analisis trade-off, studi kasus, praktik pengayaan | TM: 2×50'<br>P: 1×170' | **T2**: rancangan layout penyimpanan 1 TB event + justifikasi format/partisi | **6%** |
| **3** | Sub-CPMK 3 | **Hadoop: MapReduce, YARN & Hive:** anatomi job MapReduce, shuffle & sort, combiner/partitioner, join pattern, resource management YARN, Hive Metastore, tabel eksternal, partisi/bucket, HiveQL. | Kuliah, studi kasus batch, praktik pengayaan | TM: 2×50'<br>P: 1×170' | **T3**: analitik log dengan MapReduce/Hive + analisis bottleneck | **6%** |
| **4** | Sub-CPMK 4 | **Apache Spark & Optimasi ETL:** arsitektur driver–executor, lazy evaluation & DAG, RDD vs DataFrame, Catalyst & Tungsten, transformasi/aksi, shuffle, broadcast join, AQE, caching, uji job. | Case-based learning, simulasi konseptual, praktik pengayaan | TM: 2×50'<br>P: 1×170' | **T4**: pipeline ETL PySpark (bronze → silver → gold) + unit test; **UTS take-home dirilis** | **6%** |
| **5** | Sub-CPMK 5 | **NoSQL, Kafka & Event Streaming:** taksonomi NoSQL, BASE vs ACID, pemodelan dokumen MongoDB, pemodelan query-first Cassandra, topik/partisi/offset Kafka, consumer group, delivery semantics, CDC & outbox. | Kuliah, desain skema, praktik pengayaan | TM: 2×50'<br>P: 1×170' | **T5**: producer–consumer idempoten + model data NoSQL; **UTS dikumpulkan** | **6%** |
| **6** | Sub-CPMK 6 | **Pipeline, Orkestrasi & Kualitas Data:** ETL vs ELT, batch/micro-batch/streaming, DAG Airflow, idempotensi, retry/backfill, dbt & uji data, observabilitas, CI/CD pipeline data. | Workshop konseptual, studi kasus pipeline, praktik pengayaan | TM: 2×50'<br>P: 1×170' | Review UTS; **Milestone proyek 1**: DAG end-to-end & uji kualitas | — |
| **7** | Sub-CPMK 7 | **Analitik & ML Terdistribusi:** pipeline MLlib, feature engineering skala besar, klasifikasi & rekomendasi ALS, evaluasi model, batch scoring vs serving, versioning & monitoring model (MLOps). | Diskusi kasus ML, eksperimen terbimbing (opsional) | TM: 2×50'<br>P: 1×170' | **Milestone proyek 2**: pipeline ML + evaluasi; laporan kemajuan | — |
| **8** | Sub-CPMK 8 | **Proyek Akhir, Tata Kelola & Demo:** arsitektur end-to-end, katalog & lineage, keamanan dan privasi (UU PDP No. 27/2022), optimasi biaya, anti-pattern, demo dan pertanggungjawaban. | Presentasi, demo, peer review | TM: 2×50'<br>P: 1×170' | **UAS**: presentasi rancangan + demo terbatas + laporan + tanya jawab | **30%** |
| | | | **Ujian Tengah Semester (take-home)** | 120 menit | Studi kasus: desain + implementasi + justifikasi | **25%** |
| | | | **Partisipasi, diskusi & refleksi** | Sepanjang semester | Kehadiran, argumentasi, refleksi pengalaman kerja | **15%** |
| | | | **TOTAL BOBOT** | | | **100%** |

> **Catatan:** T1–T5 masing-masing berbobot 6% (total 30%). UTS bersifat *take-home* dan dikumpulkan pada Pertemuan 5. Proyek akhir dikerjakan berkelompok (3–4 orang) dengan penilaian individu melalui tanya jawab dan kontribusi Git. **Penekanan penilaian: 60% konsep/penalaran, 40% penerapan.** Praktik laboratorium tidak harus menggunakan cluster besar; studi kasus dan justifikasi desain dinilai setara.

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
| Kebenaran hasil | 40% | Output sesuai spesifikasi, perhitungan benar, edge case ditangani |
| Kualitas kode | 20% | Terstruktur, modular, penamaan jelas, tanpa duplikasi berlebihan |
| Pengujian & reproduksibilitas | 20% | Ada test/validasi, dapat dijalankan ulang dengan dokumentasi |
| Dokumentasi & analisis | 20% | README, diagram, penjelasan trade-off dan bottleneck |

#### F.2 UTS Take-Home

| Aspek | Bobot | Kriteria |
| :--- | :---: | :--- |
| Analisis masalah & rancangan | 30% | Pemilihan arsitektur, format, partisi, dan justifikasi trade-off |
| Implementasi | 40% | Pipeline berjalan, hasil benar, penanganan kegagalan |
| Kualitas rekayasa | 20% | Test, struktur repo, README, reproducibility |
| Presentasi tertulis | 10% | Kejelasan, sistematika, sitasi |

#### F.3 Proyek Akhir (UAS)

| Aspek | Bobot | Kriteria |
| :--- | :---: | :--- |
| Problem framing & arsitektur | 20% | Masalah nyata, ruang lingkup, diagram arsitektur, alasan pemilihan teknologi |
| Fungsionalitas pipeline | 30% | Ingest → storage → transform → serving berjalan end-to-end |
| Kualitas & pengujian | 15% | Uji kualitas data, unit/integration test, idempotensi, penanganan error |
| Tata kelola, keamanan & biaya | 10% | Katalog/lineage, akses minimum, PII handling, estimasi biaya |
| Demo & dokumentasi | 15% | Demo lancar, README, runbook, laporan, tanya jawab |
| Kolaborasi & kontribusi | 10% | Pembagian kerja jelas, riwayat Git, peer assessment |

---

### G. KEBIJAKAN PERKULIAHAN

1. **Kehadiran:** minimal **75%** dari 8 pertemuan. Mahasiswa dengan kehadiran kurang tidak berhak mengikuti UAS kecuali ada alasan medis/force majeure yang sah.
2. **Keterlambatan tugas:** pengurangan **10% per hari** (maksimal 3 hari); setelah itu tugas tidak diterima kecuali disepakati sebelumnya.
3. **Integritas akademik:** kode dan laporan harus karya sendiri/kelompok. Plagiarisme mengakibatkan nilai nol dan proses sesuai kebijakan akademik.
4. **Penggunaan AI:** diperbolehkan sebagai alat bantu dengan **disclosure** (bagian *Acknowledgements*). Mahasiswa wajib mampu menjelaskan setiap baris kode yang dikumpulkan.
5. **Komunikasi:** pertanyaan di luar kelas melalui forum/LMS; respons maksimal 1×24 jam pada hari kerja.
6. **Perangkat:** wajib membawa laptop dengan Docker/Python terpasang untuk sesi praktikum.
7. **Etika data:** dataset yang digunakan tidak boleh memuat data pribadi nyata tanpa izin; gunakan data sintetis/anonymized.

---

### H. REFERENSI

**Utama:**
1. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media.
2. White, T. (2015). *Hadoop: The Definitive Guide* (4th ed.). O'Reilly Media.
3. Chambers, B., & Zaharia, M. (2018). *Spark: The Definitive Guide*. O'Reilly Media.
4. Narkhede, N., Shapira, G., & Palino, T. (2021). *Kafka: The Definitive Guide* (2nd ed.). O'Reilly Media.

**Pendukung:**
5. Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering*. O'Reilly Media.
6. Dehghani, Z. (2022). *Data Mesh*. O'Reilly Media.
7. Leskovec, J., Rajaraman, A., & Ullman, J. (2020). *Mining of Massive Datasets* (3rd ed.). Cambridge University Press.
8. Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.
9. Dokumentasi resmi Apache Hadoop, Apache Spark, Apache Kafka, Apache Airflow, dan MongoDB.

---

### I. CATATAN PENYESUAIAN 8 PERTEMUAN

Karena mata kuliah diselenggarakan dalam **8 pertemuan**, cakupan materi reguler 16 minggu dipadatkan sebagai berikut:

| Cakupan Reguler (16 minggu) | Dipadatkan ke |
| :--- | :---: |
| Pengantar big data & arsitektur data | P1 |
| Sistem terdistribusi, HDFS, format & lakehouse | P2 |
| Hadoop, MapReduce, YARN, Hive | P3 |
| Spark (RDD, DataFrame, SQL, tuning) | P4 |
| NoSQL + Kafka/streaming | P5 |
| ETL/ELT, orkestrasi, kualitas data | P6 |
| Analitik & ML terdistribusi | P7 |
| Capstone, tata kelola, keamanan, biaya | P8 |

Pendalaman topik dilakukan melalui **tugas dan proyek**, bukan dengan menambah jam tatap muka. Mahasiswa diharapkan mengalokasikan waktu belajar mandiri ±4–6 jam per pertemuan.

---

**Disahkan oleh:**

| Disusun oleh | Diperiksa oleh | Disetujui oleh |
| :---: | :---: | :---: |
| **Mahendar Dwi Payana, S.ST., M.T.**<br>Dosen Pengampu | **Desita Ria Yusian TB, S.ST., M.T.**<br>Koordinator RMK | **M. Bayu Wibawa, S.Kom., MMSI**<br>Ketua Program Studi |
