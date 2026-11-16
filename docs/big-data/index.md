# 🗄️ Big Data (IFR229)

Selamat datang di portal pembelajaran mata kuliah **Big Data (`IFR229`)** untuk **Kelas RPL (Rekayasa Perangkat Lunak)**, Program Studi S-1 Informatika, Fakultas Sains dan Teknologi, Universitas Ubudiyah Indonesia.

Mata kuliah ini membekali mahasiswa dengan kemampuan **merancang, membangun, menguji, dan mengoperasikan perangkat lunak pengolah data berskala besar**. Penekanan diberikan pada sisi rekayasa perangkat lunak: bagaimana sistem data yang andal dibangun dari komponen terdistribusi (Hadoop, Spark, Kafka, NoSQL, Airflow), diuji, dipantau, diamankan, dan dikelola biayanya.

> **"Big data is not just about volume — it is about building systems that turn raw events into reliable decisions."**

---

## 🏛️ Identitas Mata Kuliah

| Komponen | Keterangan |
| :--- | :--- |
| **Kode Mata Kuliah** | `IFR229` |
| **Nama Mata Kuliah** | Big Data |
| **Bobot SKS** | **3 SKS** (2 SKS Teori / 1 SKS Praktikum) |
| **Semester / Tahun Akademik** | VI (Enam) / **2026 Ganjil** |
| **Kelas** | **RPL (Rekayasa Perangkat Lunak)** |
| **Rumpun Mata Kuliah** | Sains Data & Sistem Terdistribusi |
| **Dosen Pengampu** | **Mahendar Dwi Payana, S.ST., M.T.** |
| **Prasyarat** | Basis Data, Algoritma & Pemrograman, Pemrograman Berorientasi Objek |
| **Sifat** | Wajib Program Studi |
| **Jumlah Pertemuan** | **8 pertemuan** (masing-masing 2×50' teori + 1×170' praktikum) |

---

## 🎯 Capaian Pembelajaran

### Capaian Pembelajaran Lulusan (CPL)

- **CPL01 (Pengetahuan):** Menguasai konsep sistem terdistribusi, penyimpanan data skala besar, model pemrosesan batch/streaming, dan arsitektur data modern.
- **CPL03 (Problem Solving):** Mampu menganalisis kebutuhan data, memilih arsitektur, serta merancang solusi untuk volume, kecepatan, dan variasi data yang tinggi.
- **CPL04 (Solusi Rekayasa Komputasi):** Mampu membangun pipeline data, aplikasi analitik, dan integrasi layanan data yang andal, teruji, dan dapat di-deploy.
- **CPL05 (Inovasi & Kecerdasan Artifisial):** Mampu menerapkan analitik dan machine learning terdistribusi untuk menghasilkan wawasan dan layanan cerdas.
- **CPL08 (Etika & Sikap):** Menerapkan tata kelola data, keamanan, privasi (UU PDP), integritas akademik, dan pertimbangan biaya dalam rekayasa sistem data.

### Capaian Pembelajaran Mata Kuliah (CPMK)

| Kode | Rumusan CPMK | CPL |
| :--- | :--- | :--- |
| **CPMK 1** | Menjelaskan karakteristik big data, evolusi arsitektur data, serta peran rekayasa perangkat lunak dalam sistem data modern. | CPL01 |
| **CPMK 2** | Merancang penyimpanan dan pemrosesan batch terdistribusi menggunakan HDFS, MapReduce, Hive, dan Apache Spark. | CPL01, CPL03, CPL04 |
| **CPMK 3** | Membangun integrasi data NoSQL dan streaming event dengan MongoDB, Cassandra, dan Apache Kafka. | CPL03, CPL04 |
| **CPMK 4** | Mengotomasi pipeline data, menjamin kualitas data, serta menerapkan analitik dan machine learning terdistribusi. | CPL04, CPL05 |
| **CPMK 5** | Menerapkan tata kelola, keamanan, privasi, dan optimasi biaya pada proyek sistem big data. | CPL08 |

---

## 🗺️ Peta Materi 8 Pertemuan

```mermaid
flowchart TD
    subgraph F["🧱 Fondasi"]
        P1["P1 · Fondasi & Lanskap Big Data"]
        P2["P2 · Arsitektur Terdistribusi & Penyimpanan"]
    end

    subgraph B["⚙️ Pemrosesan Batch"]
        P3["P3 · Hadoop: MapReduce, YARN & Hive"]
        P4["P4 · Apache Spark & Optimasi ETL"]
    end

    subgraph S["🌊 Data Real-Time & NoSQL"]
        P5["P5 · NoSQL, Kafka & Event Streaming"]
    end

    subgraph O["🔁 Operasional & Analitik"]
        P6["P6 · Pipeline, Orkestrasi & Kualitas Data"]
        P7["P7 · Analitik & ML Terdistribusi"]
    end

    subgraph A["🚀 Capstone"]
        P8["P8 · Proyek Akhir, Tata Kelola & Demo"]
    end

    P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8

    style F fill:#e0f2fe,stroke:#0284c7
    style B fill:#dcfce7,stroke:#16a34a
    style S fill:#fef9c3,stroke:#ca8a04
    style O fill:#fae8ff,stroke:#a21caf
    style A fill:#fee2e2,stroke:#dc2626
```

| Pertemuan | Topik | Fokus Praktikum |
| :---: | :--- | :--- |
| **1** | Fondasi & Lanskap Big Data | Menyiapkan environment, eksplorasi dataset, estimasi kapasitas |
| **2** | Arsitektur Terdistribusi & Penyimpanan | HDFS/MinIO, format Parquet, layout partisi |
| **3** | Hadoop: MapReduce, YARN & Hive | Word count, analitik log dengan Hive SQL |
| **4** | Apache Spark & Optimasi ETL | Pipeline PySpark, broadcast join, tuning shuffle |
| **5** | NoSQL, Kafka & Event Streaming | CRUD MongoDB, producer–consumer Kafka |
| **6** | Pipeline, Orkestrasi & Kualitas Data | DAG Airflow, uji kualitas, idempotensi |
| **7** | Analitik & ML Terdistribusi | Pipeline MLlib, evaluasi model, batch scoring |
| **8** | Proyek Akhir, Tata Kelola & Demo | Demo end-to-end, audit keamanan & biaya |

---

## 🧪 Lingkungan Praktikum

| Komponen | Versi / Rekomendasi | Keterangan |
| :--- | :--- | :--- |
| **Python** | 3.11+ | Bahasa utama praktikum (PySpark, Kafka client) |
| **Java** | JDK 17 | Dibutuhkan Spark 3.5+ |
| **Apache Spark** | 3.5.x | Mode `local[*]` untuk latihan, cluster untuk demo |
| **Apache Hadoop** | 3.3.x | HDFS, YARN, MapReduce, Hive |
| **Apache Kafka** | 3.7+ (KRaft) | Streaming event tanpa ZooKeeper |
| **MongoDB** | 7.x | Basis data dokumen |
| **Apache Airflow** | 2.9+ | Orkestrasi pipeline |
| **Docker Desktop** | Terbaru | Menjalankan layanan laboratorium |
| **Git + GitHub** | Terbaru | Version control & CI |

```bash
# Instalasi pustaka Python utama
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pyspark==3.5.* kafka-python pymongo pandas pyarrow pytest
```

::: tip Alternatif Tanpa Cluster
Jika laptop tidak sanggup menjalankan banyak container, gunakan **mode lokal** PySpark (`master("local[*]")`) dan **Redpanda/Kafka** satu node. Seluruh tugas wajib tetap dapat dijalankan dengan satu perintah (`make run` atau `docker compose up`).
:::

---

## 📊 Komponen Penilaian

| Komponen | Bobot | Keterangan |
| :--- | :---: | :--- |
| Partisipasi, kuis & kehadiran | **10%** | Kuis singkat di awal pertemuan, keaktifan lab |
| Tugas terstruktur (T1–T5) | **30%** | 5 tugas individu/kelompok kecil, masing-masing 6% |
| Ujian Tengah Semester (UTS) | **25%** | Studi kasus take-home setelah Pertemuan 4 |
| Proyek Akhir (UAS) | **35%** | Pipeline end-to-end + demo + laporan + tata kelola |
| **Total** | **100%** | |

Rincian rubrik, jadwal, dan kebijakan akademik tersedia pada halaman **[RPS OBE](/big-data/RPS)**.

---

## 📚 Referensi Utama

1. **Martin Kleppmann** (2017). *Designing Data-Intensive Applications*. O'Reilly Media.
2. **Tom White** (2015). *Hadoop: The Definitive Guide* (4th ed.). O'Reilly Media.
3. **Bill Chambers & Matei Zaharia** (2018). *Spark: The Definitive Guide*. O'Reilly Media.
4. **Neha Narkhede, Gwen Shapira & Todd Palino** (2021). *Kafka: The Definitive Guide* (2nd ed.). O'Reilly Media.
5. **Joe Reis & Matt Housley** (2022). *Fundamentals of Data Engineering*. O'Reilly Media.
6. **Zhamak Dehghani** (2022). *Data Mesh*. O'Reilly Media.
7. **Jure Leskovec, Anand Rajaraman & Jeffrey Ullman** (2020). *Mining of Massive Datasets* (3rd ed.). Cambridge University Press.
8. Dokumentasi resmi: [Spark](https://spark.apache.org/docs/latest/), [Kafka](https://kafka.apache.org/documentation/), [Hadoop](https://hadoop.apache.org/docs/stable/), [Airflow](https://airflow.apache.org/docs/), [MongoDB](https://www.mongodb.com/docs/).

---

## 🧭 Cara Menggunakan Modul

1. **Baca modul sebelum kelas** — setiap modul memuat tujuan, konsep, contoh kode, dan latihan.
2. **Jalankan contoh kode** di lingkungan lab; jangan hanya membaca.
3. **Kerjakan latihan bertahap** — latihan dirancang menumpuk menjadi komponen proyek akhir.
4. **Simpan semua pekerjaan di Git** dengan struktur folder yang konsisten.
5. **Gunakan checklist evaluasi** di akhir setiap modul untuk menilai kesiapan Anda.

::: warning Integritas Akademik & Penggunaan AI
Kode dan laporan harus Anda pahami dan dapat pertanggungjawabkan. Penggunaan asisten AI diperbolehkan sebagai alat bantu belajar, tetapi wajib dicantumkan pada bagian *Acknowledgements* dan tidak boleh menggantikan pemahaman konsep. Plagiarisme kode maupun laporan dikenakan sanksi sesuai kebijakan akademik.
:::
