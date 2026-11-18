#!/usr/bin/env python3
"""Generate 8 interactive Data Warehouse (IFR237) presentation decks."""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from generate_big_data_presentations import (  # noqa: E402
    BASE,
    COMPACT_CSS,
    TEMPLATE,
    build_main,
    callout,
    card,
    checklist,
    closing,
    code,
    content,
    cover,
    divider,
    grid,
    quiz,
    steps,
    table,
)

PUBLIC = ROOT / "docs" / "public" / "presentasi"
DOCS_PRESENTASI = ROOT / "docs" / "presentasi"
AUDIO_BASE = f"{BASE}/audio/datawarehouse"


def dw_cover(num: int, title: str, subtitle: str, stats: list[tuple[str, str]]) -> tuple[str, str]:
    return cover(
        num,
        title,
        subtitle,
        stats,
        badge=f"🏛️ IFR237 · 3 SKS · KELAS RPL · PERTEMUAN {num} / 8",
    )


# ---------------------------------------------------------------------------
# DECK 1
# ---------------------------------------------------------------------------
DECK1 = {
    "num": 1,
    "slug": "pengantar-dw-bi",
    "file": "pertemuan-1-pengantar-data-warehouse.html",
    "module": "01-pengantar-dw-bi",
    "title": "Data Warehouse & Business Intelligence",
    "subtitle": "Mengapa analitik dipisahkan dari transaksi: dari OLTP ke keputusan berbasis data.",
    "description": "Slide interaktif Pertemuan 1 Data Warehouse IFR237: karakteristik DW Inmon, OLTP vs OLAP, komponen BI, data mart/ODS/lake, use case KPI, dan praktikum PostgreSQL.",
    "slides": [
        dw_cover(
            1,
            "Data Warehouse & Business Intelligence",
            "Mengapa analitik dipisahkan dari transaksi: dari OLTP ke keputusan berbasis data.",
            [("4 Ciri", "Inmon"), ("OLTP vs OLAP", "Beban berbeda"), ("BI Stack", "Data → keputusan")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 1",
            "Setelah sesi ini, Anda mampu menjelaskan mengapa data warehouse ada dan kapan ia dibutuhkan.",
            grid(
                [
                    checklist([
                        "Menjelaskan empat karakteristik DW Inmon",
                        "Membedakan OLTP dan OLAP",
                        "Memetakan komponen Business Intelligence",
                        "Membedakan DW, data mart, ODS, lake",
                        "Menerjemahkan pertanyaan bisnis menjadi KPI",
                        "Menyiapkan environment PostgreSQL",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Masalah OLTP vs OLAP<br>2️⃣ Definisi & ciri DW<br>3️⃣ Arsitektur BI<br>4️⃣ Jenis platform<br>5️⃣ Use case & KPI<br>6️⃣ Lab PostgreSQL", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — MASALAHNYA", "Mengapa Tidak Cukup Database Operasional?", "Database yang baik untuk transaksi belum tentu baik untuk analisis."),
        content(
            "⚖️ Dua Dunia",
            "OLTP vs OLAP",
            "Beban kerja yang berbeda menuntut desain yang berbeda:",
            table(
                ["Aspek", "OLTP", "OLAP"],
                [
                    ["Tujuan", "Menjalankan operasi harian", "Mendukung analisis & keputusan"],
                    ["Operasi", "INSERT/UPDATE/DELETE", "SELECT agregasi, scan besar"],
                    ["Baris per query", "Sedikit (1–100)", "Jutaan"],
                    ["Skema", "Ternormalisasi (3NF)", "Dimensional (star/snowflake)"],
                    ["Histori", "Data aktif saja", "Panjang, time-variant"],
                    ["Prioritas", "Latensi & konsistensi transaksi", "Throughput scan & fleksibilitas"],
                ],
            ),
        ),
        content(
            "🏛️ Definisi",
            "Empat Karakteristik Data Warehouse",
            "Definisi Inmon yang masih menjadi rujukan:",
            grid(
                [
                    card("🎯", "Subject-Oriented", "Diorganisasi berdasarkan subjek bisnis (penjualan, pelanggan), bukan aplikasi sumber.", "#0284c7"),
                    card("🔗", "Integrated", "Menyatukan banyak sumber dengan definisi, kode, dan format yang konsisten.", "#059669"),
                    card("🕰️", "Time-Variant", "Menyimpan histori dan konteks waktu, bukan hanya kondisi terkini.", "#9333ea"),
                    card("🔒", "Nonvolatile", "Data dimuat dan dibaca; perubahan terkontrol, tidak update sembarangan.", "#d97706"),
                ],
                2,
            )
            + callout("blue", "💡 <b>Business Intelligence</b> adalah payung proses & teknologi untuk mengubah data menjadi keputusan; DW adalah fondasinya."),
        ),
        divider("BAGIAN II — ARSITEKTUR & PLATFORM", "Dari Sumber ke Dashboard", "Lima lapisan yang menghubungkan sistem operasional dengan pengguna bisnis."),
        content(
            "🏗️ Arsitektur BI",
            "Alur Data dari Sumber ke Keputusan",
            "Setiap lapisan punya tanggung jawab yang jelas:",
            steps([
                ("Source", "ERP, POS, CRM, web/API — data operasional yang kotor dan berubah."),
                ("Staging", "Salinan mentah untuk dimuat cepat; boleh duplikat, belum ada aturan bisnis."),
                ("Integration", "Bersihkan, standarkan, resolve key, simpan histori (SCD), bentuk dimensi."),
                ("Presentation", "Star/snowflake schema, agregat, tabel siap BI."),
                ("Access", "SQL, OLAP, dashboard, API, model analitik."),
            ])
            + callout("green", "✅ Pemisahan ini mencegah query analitik mengganggu aplikasi operasional."),
        ),
        content(
            "🗂️ Jenis Platform",
            "DW, Data Mart, ODS, Lake, Lakehouse",
            "Pilih berdasarkan cakupan dan kebutuhan, bukan tren:",
            table(
                ["Platform", "Cakupan", "Cocok Untuk"],
                [
                    ["ODS", "Operasional terintegrasi", "Customer service, near-real-time"],
                    ["Data Warehouse", "Enterprise", "BI korporat, analitik lintas domain"],
                    ["Data Mart", "Satu domain", "Marketing, keuangan, penjualan"],
                    ["Data Lake", "Semua data mentah", "Eksplorasi, data science, arsip"],
                    ["Lakehouse", "Lake + ACID", "Analitik modern skala besar"],
                ],
            ),
        ),
        content(
            "🕰️ Evolusi",
            "Lima Generasi Platform Data",
            "Dari database relasional ke lakehouse dan semantic layer:",
            steps([
                ("1970 — RDBMS", "Model relasional & OLTP."),
                ("1990 — Enterprise DW", "Inmon: integrasi, histori, subject-oriented."),
                ("1996 — Dimensional Modeling", "Kimball: star schema, bus matrix, conformed dimension."),
                ("2010 — Cloud DW", "Redshift, BigQuery, Snowflake: pisah storage & compute."),
                ("2020+ — Lakehouse & dbt", "ACID di data lake, transformasi sebagai kode, semantic layer."),
            ]),
        ),
        divider("BAGIAN III — NILAI BISNIS & PRAKTIKUM", "Dari KPI ke Query", "Data warehouse hanya bernilai jika menjawab pertanyaan yang dapat ditindaklanjuti."),
        content(
            "📊 Use Case & KPI",
            "Pertanyaan Bisnis yang Menjadi Alasan DW Dibangun",
            "Setiap KPI harus punya definisi tunggal dan sumber yang jelas:",
            table(
                ["Domain", "Pertanyaan", "KPI"],
                [
                    ["Retail", "Kategori mana yang menguntungkan?", "Revenue, margin, units"],
                    ["E-commerce", "Di tahap mana funnel bocor?", "Conversion, abandonment"],
                    ["Perbankan", "Segmen mana berisiko churn?", "Churn rate, CLV, NPL"],
                    ["Kampus", "Bagaimana performa akademik?", "IPK, kelulusan, retensi"],
                    ["Logistik", "Rute mana yang efisien?", "On-time delivery, cost"],
                    ["Klinik", "Bagaimana utilisasi layanan?", "Length of stay, readmission"],
                ],
            ),
        ),
        content(
            "💻 Praktikum",
            "Menyiapkan PostgreSQL & Data Sintetis",
            "Semua latihan semester menggunakan database yang sama:",
            grid(
                [
                    code("""docker run -d --name dw-postgres \\
  -e POSTGRES_PASSWORD=dw123 \\
  -e POSTGRES_DB=retail_dw \\
  -p 5432:5432 \\
  postgres:16

docker exec -it dw-postgres \\
  psql -U postgres -d retail_dw"""),
                    steps([
                        ("Buat schema", "oltp, staging, dw, etl."),
                        ("Buat tabel orders", "order_id, order_ts, customer, produk, qty, price, status."),
                        ("Isi 300.000 baris", "Gunakan generate_series + random()."),
                        ("Query OLTP", "Ambil satu order berdasarkan primary key."),
                        ("Query OLAP", "Agregasi revenue per bulan & kategori."),
                    ]),
                ],
                2,
            ),
        ),
        content(
            "🔬 Analisis",
            "Melihat Perbedaan Beban Secara Nyata",
            "Jalankan dua query dan bandingkan:",
            grid(
                [
                    code("""-- OLTP: satu baris
EXPLAIN ANALYZE
SELECT * FROM oltp.orders
WHERE order_id = 12345;

-- OLAP: agregasi seluruh data
EXPLAIN ANALYZE
SELECT date_trunc('month', order_ts) AS bulan,
       category,
       SUM(quantity * unit_price) AS revenue
FROM oltp.orders
WHERE status = 'paid'
GROUP BY 1, 2
ORDER BY 1, 3 DESC;"""),
                    card("💡", "Yang Diamati", "Query OLAP memindai hampir seluruh tabel. Jika dijalankan berulang di database operasional, aplikasi kasir melambat.", "#0284c7")
                    + callout("amber", "⚠️ Inilah alasan teknis dan bisnis mengapa analitik dipisahkan ke data warehouse."),
                ],
                2,
            ),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa data warehouse disebut nonvolatile?", "Data dimuat dan dibaca; transaksi historis tidak di-update sembarangan. Koreksi dilakukan melalui proses ETL terkontrol agar histori tetap dapat diaudit."),
                ("Apa perbedaan data mart dan data warehouse?", "Data mart fokus pada satu domain/departemen dan lebih kecil; data warehouse mencakup enterprise dan menjadi sumber konsistensi lintas domain."),
                ("Kapan data lake lebih tepat daripada data warehouse?", "Saat data mentah/beragam (gambar, log, JSON) perlu dieksplorasi oleh data scientist dan skema belum pasti. Untuk BI terstruktur, DW tetap lebih tepat."),
            ]),
        ),
        closing(
            "Data warehouse memisahkan beban analitik dari transaksi — dan menyatukan definisi bisnis.",
            [("📖 Modul 1", "Fondasi DW & BI"), ("🧪 Tugas 1", "Profil data & KPI"), ("➡️ Berikutnya", "Arsitektur & bus matrix")],
            "Selesaikan Tugas 1 dan pastikan PostgreSQL serta data sintetis Anda berjalan.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 2
# ---------------------------------------------------------------------------
DECK2 = {
    "num": 2,
    "slug": "arsitektur-pemodelan",
    "file": "pertemuan-2-arsitektur-pemodelan.html",
    "module": "02-arsitektur-pemodelan",
    "title": "Arsitektur & Pemodelan Konseptual",
    "subtitle": "Inmon vs Kimball, bus matrix, requirement gathering, dan deklarasi grain.",
    "description": "Slide interaktif Pertemuan 2 Data Warehouse IFR237: arsitektur Inmon dan Kimball, lapisan staging hingga presentation, bus matrix, empat langkah Kimball, grain, dan conformed dimension.",
    "slides": [
        dw_cover(
            2,
            "Arsitektur & Pemodelan Konseptual",
            "Inmon vs Kimball, bus matrix, requirement gathering, dan deklarasi grain.",
            [("2 Mazhab", "Inmon & Kimball"), ("1 Bus Matrix", "Proses × dimensi"), ("4 Langkah", "Kimball")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 2",
            "Setelah sesi ini, Anda mampu merancang kerangka data warehouse sebelum menulis satu baris DDL.",
            grid(
                [
                    checklist([
                        "Membandingkan Inmon dan Kimball",
                        "Menjelaskan lima lapisan arsitektur DW",
                        "Menyusun bus matrix",
                        "Menulis grain statement yang spesifik",
                        "Mengidentifikasi fakta & dimensi",
                        "Mendefinisikan KPI secara eksplisit",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Inmon vs Kimball<br>2️⃣ Lapisan arsitektur<br>3️⃣ Bus matrix<br>4️⃣ 4 langkah Kimball<br>5️⃣ Grain & requirement<br>6️⃣ Workshop", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — DUA MAZHAB", "Top-Down vs Bottom-Up", "Dua cara membangun data warehouse yang sama-sama valid, dengan trade-off berbeda."),
        content(
            "🏛️ Inmon vs Kimball",
            "Dari Enterprise ke Mart, atau Mart ke Enterprise?",
            "Pilihan memengaruhi kecepatan nilai, konsistensi, dan biaya awal:",
            table(
                ["Aspek", "Inmon (Top-Down)", "Kimball (Bottom-Up)"],
                [
                    ["Titik mulai", "Enterprise DW (3NF)", "Data mart dimensional"],
                    ["Kecepatan nilai", "Lambat", "Cepat"],
                    ["Konsistensi", "Tinggi secara terpusat", "Bergantung conformed dimension"],
                    ["Investasi awal", "Besar", "Kecil–sedang"],
                    ["Cocok untuk", "Organisasi besar, regulasi ketat", "Tim kecil, analitik per domain"],
                ],
            )
            + callout("blue", "💡 Implementasi modern sering <b>hybrid</b>: integration layer terpusat + presentation layer dimensional."),
        ),
        content(
            "🏗️ Lapisan Arsitektur",
            "Lima Lapisan yang Jelas",
            "Setiap lapisan punya tanggung jawab dan tingkat kebersihan data berbeda:",
            grid(
                [
                    card("📥", "Source", "ERP, POS, CRM, web/API. Skema OLTP, kotor, berubah.", "#0284c7"),
                    card("🗃️", "Staging", "Salinan mentah untuk load cepat. Boleh duplikat, belum ada aturan bisnis.", "#059669"),
                    card("🔧", "Integration", "Standarisasi, dedup, resolve key, histori SCD, surrogate key.", "#9333ea"),
                    card("⭐", "Presentation", "Star/snowflake, agregat, tabel siap BI.", "#d97706"),
                    card("📊", "Access", "SQL, OLAP, dashboard, API, model analitik.", "#0f766e"),
                ],
                3,
            ),
        ),
        content(
            "🔄 ETL vs ELT",
            "Di Mana Transformasi Dilakukan?",
            "Cloud DW membuat ELT populer, tetapi ETL tetap relevan:",
            table(
                ["Aspek", "ETL", "ELT"],
                [
                    ["Urutan", "Transform sebelum load", "Load mentah, transform di DW"],
                    ["Cocok", "Data sensitif, DW on-premise", "Cloud DW/lakehouse elastis"],
                    ["Alat", "SSIS, Informatica, Spark", "dbt, SQL, Spark"],
                    ["Kontrol", "Ketat di luar DW", "Memanfaatkan SQL & compute DW"],
                ],
            ),
        ),
        divider("BAGIAN II — BUS MATRIX", "Peta Jalan Data Warehouse", "Business process × conformed dimension = rencana pembangunan yang konsisten."),
        content(
            "🧩 Bus Matrix",
            "Contoh Retail",
            "Setiap ✔ berarti proses bisnis menggunakan dimensi tersebut:",
            table(
                ["Business Process", "Date", "Product", "Customer", "Store", "Promo", "Employee"],
                [
                    ["Sales", "✔", "✔", "✔", "✔", "✔", "✔"],
                    ["Returns", "✔", "✔", "✔", "✔", "", "✔"],
                    ["Inventory Snapshot", "✔", "✔", "", "✔", "", ""],
                    ["Shipment", "✔", "✔", "✔", "✔", "", ""],
                    ["Campaign Response", "✔", "✔", "✔", "", "✔", ""],
                ],
            )
            + callout("green", "✅ Dimensi yang sama di semua proses = <b>conformed dimension</b>; analisis lintas proses menjadi mungkin."),
        ),
        content(
            "🧭 Empat Langkah Kimball",
            "Dari Proses Bisnis ke Fact Table",
            "Urutan ini mencegah desain yang berubah-ubah:",
            steps([
                ("Pilih business process", "Aktivitas terukur: penjualan, retur, pengiriman, pendaftaran, kunjungan."),
                ("Deklarasikan grain", "Makna satu baris fact dalam bahasa bisnis, sedetail mungkin."),
                ("Identifikasi dimensi", "Siapa, apa, di mana, kapan, bagaimana — yang menjelaskan grain."),
                ("Identifikasi fakta", "Measure numerik: quantity, revenue, cost, margin, discount."),
            ]),
        ),
        content(
            "📏 Grain",
            "Kalimat yang Menentukan Segalanya",
            "Grain yang buruk membuat semua turunan salah:",
            table(
                ["Grain yang Baik", "Grain yang Buruk"],
                [
                    ["Satu baris per item pesanan per hari", "Data penjualan"],
                    ["Satu baris per produk per toko per akhir hari", "Snapshot stok"],
                    ["Satu baris per pendaftaran mahasiswa per semester", "Data akademik"],
                    ["Satu baris per kunjungan pasien", "Data rumah sakit"],
                ],
            )
            + callout("amber", "⚠️ Pilih grain paling atomik yang dibutuhkan. Agregasi dari detail lebih mudah daripada memecah agregat."),
        ),
        divider("BAGIAN III — REQUIREMENT & CONFORMED DIMENSION", "Dari Pertanyaan ke KPI", "Data warehouse harus menjawab pertanyaan yang benar-benar dipakai."),
        content(
            "❓ Requirement",
            "Pertanyaan Stakeholder → KPI → Grain",
            "Jangan mulai dari tabel; mulai dari keputusan:",
            table(
                ["Pertanyaan", "KPI", "Grain"],
                [
                    ["Kategori apa yang paling untung?", "Margin per kategori", "Item penjualan"],
                    ["Toko mana yang underperform?", "Revenue vs target", "Harian per toko"],
                    ["Apakah promosi efektif?", "Lift & ROI promosi", "Item penjualan per promo"],
                    ["Berapa stok akhir hari?", "Inventory on hand", "Produk per toko per hari"],
                ],
            ),
        ),
        content(
            "📐 Conformed Dimension",
            "Satu Definisi untuk Semua Mart",
            "Jika `dim_product` berbeda antar mart, laporan akan bertentangan:",
            grid(
                [
                    card("✅", "Conformed", "Nama, atribut, nilai key, dan hierarki sama di sales, returns, inventory, shipment.", "#059669"),
                    card("❌", "Silo", "Setiap mart punya kategori sendiri. Drill-across gagal, angka tidak cocok.", "#dc2626"),
                    card("🧩", "Bus Matrix", "Alat untuk merencanakan dan mengawasi conformed dimension.", "#0284c7"),
                    card("🛡️", "Governance", "Owner dimensi, definisi metrik, dan perubahan skema terkontrol.", "#9333ea"),
                ],
                2,
            ),
        ),
        content(
            "💻 Workshop",
            "Menyusun Bus Matrix & Grain",
            "Langkah praktikum di kelas:",
            steps([
                ("Pilih domain", "Retail, kampus, klinik, atau logistik."),
                ("Daftar 4 proses", "Aktivitas yang menghasilkan peristiwa terukur."),
                ("Daftar 6 dimensi", "Date, product, customer, store, promo, employee."),
                ("Tandai relasi", "✔ jika proses memakai dimensi."),
                ("Tulis grain", "Satu kalimat per proses, bukan per tabel."),
                ("Daftar fakta", "Minimal 5 measure per proses."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa bus matrix penting?", "Ia memastikan proses bisnis berbagi dimensi yang sama (conformed), sehingga analisis lintas proses konsisten dan tidak menjadi silo."),
                ("Apa contoh grain yang terlalu kasar?", "“Data penjualan” tidak menjelaskan satu baris mewakili apa. Grain harus menyebut level detail: per item, per hari, per toko."),
                ("Kapan Inmon lebih tepat daripada Kimball?", "Saat organisasi besar membutuhkan konsistensi enterprise, regulasi ketat, dan mampu berinvestasi lebih lama sebelum nilai terlihat."),
            ]),
        ),
        closing(
            "Arsitektur yang baik membuat keputusan sulit menjadi jelas sebelum kode ditulis.",
            [("📖 Modul 2", "Arsitektur & bus matrix"), ("🧪 Tugas 2", "Bus matrix & grain"), ("➡️ Berikutnya", "Star schema")],
            "Selesaikan Tugas 2: bus matrix, grain statement, dan definisi KPI untuk studi kasus Anda.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 3
# ---------------------------------------------------------------------------
DECK3 = {
    "num": 3,
    "slug": "fact-dimension-star",
    "file": "pertemuan-3-fact-dimension-star.html",
    "module": "03-dimensional-modeling",
    "title": "Fact, Dimension & Star Schema",
    "subtitle": "Menerjemahkan grain menjadi tabel fakta, dimensi, dan surrogate key yang benar.",
    "description": "Slide interaktif Pertemuan 3 Data Warehouse IFR237: fact table, dimension table, surrogate key, tipe fact, additivity, dimensi khusus, DDL star schema PostgreSQL, dan query validasi.",
    "slides": [
        dw_cover(
            3,
            "Fact, Dimension & Star Schema",
            "Menerjemahkan grain menjadi tabel fakta, dimensi, dan surrogate key yang benar.",
            [("1 Fact", "Di tengah"), ("4+ Dim", "Di sekeliling"), ("Star", "Skema analitik")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 3",
            "Setelah sesi ini, Anda mampu membangun star schema yang berjalan dan memvalidasinya dengan SQL.",
            grid(
                [
                    checklist([
                        "Menjelaskan peran fact dan dimension",
                        "Membedakan tipe fact table",
                        "Memilih surrogate key",
                        "Menangani additive & non-additive measure",
                        "Mengenali degenerate/junk/role-playing dimension",
                        "Membuat DDL star schema di PostgreSQL",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Anatomi star<br>2️⃣ Fact table<br>3️⃣ Dimension table<br>4️⃣ Desain khusus<br>5️⃣ DDL & load<br>6️⃣ Validasi", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — ANATOMI", "Satu Fakta, Banyak Konteks", "Fact menyimpan peristiwa; dimension memberi makna."),
        content(
            "⭐ Star Schema",
            "Fact di Tengah, Dimension di Sekeliling",
            "Fact hanya terhubung langsung ke dimensi — tanpa join antar-dimensi:",
            grid(
                [
                    card("📊", "Fact Table", "Foreign key + measure. Jutaan baris. Contoh: `fact_sales`.", "#0284c7"),
                    card("📅", "Dimension", "Konteks deskriptif: date, product, customer, store.", "#059669"),
                    card("📏", "Grain", "Makna satu baris fact. Contoh: satu item pesanan.", "#9333ea"),
                    card("🔢", "Measure", "Angka yang dianalisis: quantity, revenue, margin.", "#d97706"),
                ],
                2,
            )
            + callout("green", "✅ Star schema lebih mudah dipahami pengguna BI dan biasanya lebih cepat untuk query analitik."),
        ),
        content(
            "📋 Tipe Fact Table",
            "Empat Pola yang Sering Ditemui",
            "Pilih sesuai peristiwa yang ingin dicatat:",
            table(
                ["Tipe", "Isi", "Contoh", "Catatan"],
                [
                    ["Transaction", "Satu baris per peristiwa", "Item penjualan", "Paling umum, atomik"],
                    ["Periodic snapshot", "Kondisi pada interval", "Stok akhir hari", "Semi-additive"],
                    ["Accumulating snapshot", "Satu baris per proses + milestone", "Order → bayar → kirim", "Beberapa tanggal"],
                    ["Factless fact", "Tanpa measure", "Kehadiran, partisipasi promo", "Mencatat relasi"],
                ],
            ),
        ),
        content(
            "🗂️ Dimension Table",
            "Surrogate Key vs Natural Key",
            "Fact menyimpan integer key; natural key tetap disimpan di dimensi untuk traceability:",
            table(
                ["Aspek", "Surrogate Key", "Natural Key"],
                [
                    ["Bentuk", "Integer berurutan", "Kode bisnis (text)"],
                    ["Stabilitas", "Tidak berubah", "Bisa berubah"],
                    ["Kinerja join", "Cepat", "Lebih lambat"],
                    ["Mendukung SCD", "Ya", "Tidak cocok"],
                ],
            )
            + callout("blue", "💡 Gunakan surrogate key di fact. Simpan natural key di dimension untuk audit dan lookup."),
        ),
        divider("BAGIAN II — KEPUTUSAN DESAIN", "Detail yang Menentukan Kebenaran", "Additivity dan dimensi khusus sering menjadi sumber kesalahan."),
        content(
            "➕ Additivity",
            "Tidak Semua Angka Boleh Dijumlahkan",
            "Kesalahan agregasi menghasilkan laporan yang salah meski query-nya “jalan”:",
            table(
                ["Tipe", "Dapat Dijumlahkan", "Contoh", "Perlakuan"],
                [
                    ["Additive", "Semua dimensi", "Revenue, quantity", "SUM() aman"],
                    ["Semi-additive", "Semua kecuali waktu", "Saldo stok, saldo bank", "Rata-rata/akhir periode"],
                    ["Non-additive", "Tidak", "Rasio, persentase, harga", "Hitung dari pembilang/penyebut"],
                ],
            )
            + code("""-- ❌ Salah: menjumlahkan persentase
SELECT SUM(margin_pct) FROM fact_sales;

-- ✅ Benar: hitung dari agregat
SELECT SUM(margin) / NULLIF(SUM(net_revenue), 0) AS margin_pct
FROM fact_sales;"""),
        ),
        content(
            "🧩 Dimensi Khusus",
            "Degenerate, Junk, Role-Playing",
            "Tiga pola yang muncul di hampir semua data warehouse:",
            grid(
                [
                    card("🔢", "Degenerate Dimension", "Nomor dokumen (`order_id`, `invoice_no`) disimpan langsung di fact, tanpa tabel dimensi.", "#0284c7"),
                    card("🧷", "Junk Dimension", "Kombinasi flag kecil (`is_gift`, `is_promo`, `channel`) dalam satu tabel.", "#059669"),
                    card("🎭", "Role-Playing", "Satu dimensi berperan beberapa kali: order_date, ship_date, delivery_date.", "#9333ea"),
                    card("🌉", "Bridge Table", "Relasi many-to-many, mis. produk–supplier, dengan bobot alokasi.", "#d97706"),
                ],
                2,
            ),
        ),
        divider("BAGIAN III — IMPLEMENTASI", "Dari Diagram ke PostgreSQL", "DDL yang benar sejak awal menghemat refactor di kemudian hari."),
        content(
            "📅 DDL Dimensi",
            "Tanggal, Produk, Pelanggan, Toko",
            "Setiap dimensi memiliki surrogate key dan natural key yang unik:",
            code("""CREATE TABLE dw.dim_product (
    product_key   BIGSERIAL PRIMARY KEY,
    product_code  TEXT NOT NULL UNIQUE,
    product_name  TEXT NOT NULL,
    category      TEXT NOT NULL,
    subcategory   TEXT,
    cost          NUMERIC(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE dw.dim_customer (
    customer_key  BIGSERIAL PRIMARY KEY,
    customer_code TEXT NOT NULL UNIQUE,
    customer_name TEXT NOT NULL,
    city          TEXT,
    segment       TEXT
);

CREATE TABLE dw.dim_date (
    date_key    INTEGER PRIMARY KEY,
    full_date   DATE NOT NULL UNIQUE,
    year        INTEGER NOT NULL,
    quarter     INTEGER NOT NULL,
    month       INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL,
    is_weekend  BOOLEAN NOT NULL
);"""),
        ),
        content(
            "📊 DDL Fact",
            "Foreign Key + Measure + Degenerate Dimension",
            "Unique constraint `(order_id, line_no)` menjaga grain dan idempotensi:",
            code("""CREATE TABLE dw.fact_sales (
    sales_key     BIGSERIAL PRIMARY KEY,
    date_key      INTEGER NOT NULL REFERENCES dw.dim_date(date_key),
    product_key   BIGINT  NOT NULL REFERENCES dw.dim_product(product_key),
    customer_key  BIGINT  NOT NULL REFERENCES dw.dim_customer(customer_key),
    store_key     BIGINT  NOT NULL REFERENCES dw.dim_store(store_key),
    order_id      TEXT NOT NULL,
    line_no       INTEGER NOT NULL,
    quantity      INTEGER NOT NULL CHECK (quantity > 0),
    gross_revenue NUMERIC(14,2) NOT NULL,
    discount      NUMERIC(14,2) NOT NULL DEFAULT 0,
    net_revenue   NUMERIC(14,2) NOT NULL,
    cost          NUMERIC(14,2) NOT NULL DEFAULT 0,
    margin        NUMERIC(14,2)
        GENERATED ALWAYS AS (net_revenue - cost) STORED,
    UNIQUE (order_id, line_no)
);

CREATE INDEX idx_fact_sales_date
    ON dw.fact_sales(date_key);
CREATE INDEX idx_fact_sales_product
    ON dw.fact_sales(product_key);"""),
        ),
        content(
            "📥 Load Fact",
            "Lookup Surrogate Key Saat Load",
            "Fact tidak menyimpan kode produk/pelanggan; ia menyimpan key hasil join:",
            code("""INSERT INTO dw.fact_sales (
    date_key, product_key, customer_key, store_key,
    order_id, line_no, quantity,
    gross_revenue, discount, net_revenue, cost
)
SELECT
    TO_CHAR(o.order_ts::TIMESTAMP, 'YYYYMMDD')::INT,
    p.product_key,
    c.customer_key,
    s.store_key,
    o.order_id,
    ROW_NUMBER() OVER (PARTITION BY o.order_id
                       ORDER BY o.product_code)::INT,
    o.quantity::INT,
    o.quantity::NUMERIC * o.unit_price::NUMERIC,
    COALESCE(o.discount::NUMERIC, 0),
    o.quantity::NUMERIC * o.unit_price::NUMERIC
        - COALESCE(o.discount::NUMERIC, 0),
    o.quantity::NUMERIC * p.cost
FROM staging.raw_orders o
JOIN dw.dim_product p  ON p.product_code = o.product_code
JOIN dw.dim_customer c ON c.customer_code = o.customer_code
JOIN dw.dim_store s    ON s.store_code = o.store_code
WHERE o.status = 'paid';"""),
        ),
        content(
            "✅ Validasi",
            "Tiga Query untuk Membuktikan Skema Benar",
            "Revenue kategori, tren bulanan, dan margin yang dihitung dengan benar:",
            code("""SELECT p.category,
       SUM(f.net_revenue) AS revenue,
       SUM(f.quantity)    AS units
FROM dw.fact_sales f
JOIN dw.dim_product p ON p.product_key = f.product_key
GROUP BY p.category
ORDER BY revenue DESC;

SELECT d.year, d.month, SUM(f.net_revenue) AS revenue
FROM dw.fact_sales f
JOIN dw.dim_date d ON d.date_key = f.date_key
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

SELECT p.category,
       SUM(f.margin) / NULLIF(SUM(f.net_revenue), 0) * 100
           AS margin_pct
FROM dw.fact_sales f
JOIN dw.dim_product p ON p.product_key = f.product_key
GROUP BY p.category;"""),
        ),
        content(
            "💻 Praktikum",
            "Bangun Star Schema Anda",
            "Langkah minimum yang harus terbukti:",
            steps([
                ("Tentukan grain", "Satu kalimat di README."),
                ("Buat 4 dimensi", "Date, product, customer, store."),
                ("Buat fact", "FK + minimal 5 measure."),
                ("Isi data", "Minimal 10.000 baris fact."),
                ("Validasi", "5 query agregasi & filter."),
                ("Dokumentasi", "Diagram + data dictionary."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa fact table menyimpan surrogate key, bukan kode produk?", "Surrogate key integer lebih cepat untuk join, stabil meski kode bisnis berubah, dan mendukung banyak versi dimensi (SCD)."),
                ("Apa contoh measure non-additive?", "Persentase margin, rasio konversi, harga satuan. Jangan dijumlahkan; hitung dari agregat pembilang dan penyebut."),
                ("Apa fungsi unique constraint (order_id, line_no) di fact?", "Menjaga grain agar satu baris mewakili satu item pesanan, sekaligus memungkinkan upsert/idempotensi saat ETL dijalankan ulang."),
            ]),
        ),
        closing(
            "Star schema yang benar dimulai dari grain yang jelas, bukan dari banyaknya tabel.",
            [("📖 Modul 3", "Star schema"), ("🧪 Tugas 3", "DDL + 10k fact"), ("➡️ Berikutnya", "Snowflake & SCD")],
            "Selesaikan Tugas 3 dan pastikan lima query validasi mengembalikan hasil yang masuk akal.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 4
# ---------------------------------------------------------------------------
DECK4 = {
    "num": 4,
    "slug": "snowflake-scd",
    "file": "pertemuan-4-snowflake-scd.html",
    "module": "04-snowflake-scd",
    "title": "Snowflake, Galaxy & Slowly Changing Dimensions",
    "subtitle": "Menjaga histori dimensi dan konsistensi lintas fact table.",
    "description": "Slide interaktif Pertemuan 4 Data Warehouse IFR237: star vs snowflake, galaxy schema, conformed dimension, SCD tipe 0-6, implementasi SCD2, query point-in-time, dan late-arriving dimension.",
    "slides": [
        dw_cover(
            4,
            "Snowflake, Galaxy & SCD",
            "Menjaga histori dimensi dan konsistensi lintas fact table.",
            [("Star/Snow", "Trade-off"), ("Galaxy", "Conformed dim"), ("SCD2", "Histori dimensi")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 4",
            "Setelah sesi ini, Anda mampu menangani dimensi yang berubah tanpa kehilangan histori.",
            grid(
                [
                    checklist([
                        "Memilih star vs snowflake",
                        "Merancang galaxy schema",
                        "Menjelaskan conformed dimension",
                        "Memilih tipe SCD yang tepat",
                        "Mengimplementasikan SCD Tipe 2",
                        "Menulis query point-in-time",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Star vs snowflake<br>2️⃣ Galaxy & conformed<br>3️⃣ Tipe SCD<br>4️⃣ SCD2<br>5️⃣ Point-in-time<br>6️⃣ Late-arriving", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — BENTUK SKEMA", "Star, Snowflake, Galaxy", "Tiga bentuk yang menjawab kebutuhan berbeda."),
        content(
            "❄️ Star vs Snowflake",
            "Denormalisasi vs Normalisasi Dimensi",
            "Pilih berdasarkan kompleksitas dimensi dan kebutuhan query:",
            table(
                ["Aspek", "Star", "Snowflake"],
                [
                    ["Join", "Sedikit", "Lebih banyak"],
                    ["Query simplicity", "Tinggi", "Sedang"],
                    ["Redundansi", "Ada (disengaja)", "Minimal"],
                    ["Storage", "Lebih besar", "Lebih kecil"],
                    ["Kinerja baca", "Umumnya lebih cepat", "Tergantung optimizer"],
                    ["Cocok untuk", "BI, dashboard", "Dimensi besar & hierarki kompleks"],
                ],
            )
            + callout("green", "✅ Mulai dari star. Tambahkan snowflake hanya jika ada alasan kuat."),
        ),
        content(
            "❄️ Snowflake",
            "Contoh Dimensi Produk Ternormalisasi",
            "Kategori dan subkategori dipisahkan dari produk:",
            code("""CREATE TABLE dw.dim_category (
    category_key  BIGSERIAL PRIMARY KEY,
    category_name TEXT UNIQUE NOT NULL
);

CREATE TABLE dw.dim_subcategory (
    subcategory_key BIGSERIAL PRIMARY KEY,
    category_key    BIGINT REFERENCES dw.dim_category,
    subcategory_name TEXT NOT NULL,
    UNIQUE (category_key, subcategory_name)
);

CREATE TABLE dw.dim_product_snow (
    product_key    BIGSERIAL PRIMARY KEY,
    product_code   TEXT UNIQUE NOT NULL,
    product_name   TEXT NOT NULL,
    subcategory_key BIGINT REFERENCES dw.dim_subcategory,
    cost           NUMERIC(12,2)
);""")
            + callout("amber", "⚠️ Query kategori kini butuh dua join tambahan. Pastikan manfaat normalisasi sebanding dengan biaya kompleksitasnya."),
        ),
        content(
            "🌌 Galaxy Schema",
            "Beberapa Fact, Satu Set Dimensi",
            "Fact sales, returns, inventory, dan shipment berbagi dimensi yang sama:",
            grid(
                [
                    card("⭐", "Fact Sales", "Revenue, quantity, discount, margin.", "#0284c7"),
                    card("↩️", "Fact Returns", "Refund amount, return quantity, reason.", "#dc2626"),
                    card("📦", "Fact Inventory", "On-hand stock, reorder point, snapshot date.", "#059669"),
                    card("🚚", "Fact Shipment", "Shipping cost, delivery days, carrier.", "#d97706"),
                ],
                2,
            )
            + callout("blue", "💡 Semua fact memakai `dim_date`, `dim_product`, `dim_customer`, `dim_store` yang sama."),
        ),
        content(
            "🔗 Conformed Dimension",
            "Kunci Drill-Across",
            "Definisi yang sama memungkinkan perbandingan lintas proses:",
            code("""WITH sales AS (
    SELECT p.category, SUM(f.net_revenue) AS revenue
    FROM dw.fact_sales f
    JOIN dw.dim_product p ON p.product_key = f.product_key
    GROUP BY p.category
),
returns AS (
    SELECT p.category, SUM(r.refund_amount) AS refund
    FROM dw.fact_returns r
    JOIN dw.dim_product p ON p.product_key = r.product_key
    GROUP BY p.category
)
SELECT s.category, s.revenue,
       COALESCE(r.refund, 0) AS refund,
       ROUND(COALESCE(r.refund, 0)
             / NULLIF(s.revenue, 0) * 100, 2) AS return_pct
FROM sales s
LEFT JOIN returns r USING (category)
ORDER BY return_pct DESC;"""),
        ),
        divider("BAGIAN II — SLOWLY CHANGING DIMENSIONS", "Dimensi Berubah, Histori Harus Tetap", "Pilih tipe SCD berdasarkan pertanyaan bisnis, bukan kebiasaan."),
        content(
            "🕰️ Tipe SCD",
            "Tujuh Strategi Menangani Perubahan",
            "Semakin tinggi tipenya belum tentu lebih baik; pilih sesuai kebutuhan:",
            table(
                ["Tipe", "Strategi", "Histori", "Contoh"],
                [
                    ["0", "Pertahankan nilai asli", "Tidak", "Tanggal lahir, NIK"],
                    ["1", "Timpa nilai lama", "Tidak", "Koreksi ejaan"],
                    ["2", "Tambah baris + masa berlaku", "Ya", "Pelanggan pindah kota"],
                    ["3", "Tambah kolom previous", "Terbatas", "Satu perubahan terakhir"],
                    ["4", "Tabel histori terpisah", "Ya", "Dimensi besar"],
                    ["5", "Tipe 4 + mini dimension", "Ya", "Kombinasi"],
                    ["6", "Hybrid 1+2+3", "Ya", "Butuh current + history"],
                ],
            ),
        ),
        content(
            "🧱 SCD2",
            "Skema dengan Masa Berlaku",
            "`customer_key` baru untuk setiap versi; natural key tetap sama:",
            code("""CREATE TABLE dw.dim_customer_scd (
    customer_key  BIGSERIAL PRIMARY KEY,
    customer_code TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    city          TEXT,
    segment       TEXT,
    valid_from    TIMESTAMP NOT NULL,
    valid_to      TIMESTAMP,
    is_current    BOOLEAN NOT NULL DEFAULT TRUE,
    version       INTEGER NOT NULL DEFAULT 1,
    UNIQUE (customer_code, version)
);

-- Hanya satu versi current per customer
CREATE UNIQUE INDEX uq_customer_current
    ON dw.dim_customer_scd (customer_code)
    WHERE is_current;

CREATE INDEX idx_customer_validity
    ON dw.dim_customer_scd
    (customer_code, valid_from, valid_to);"""),
        ),
        content(
            "🔄 Proses SCD2",
            "Tutup Versi Lama, Buat Versi Baru",
            "Lakukan dalam satu transaksi agar tidak ada celah:",
            code("""BEGIN;

UPDATE dw.dim_customer_scd
SET valid_to = TIMESTAMP '2025-06-01',
    is_current = FALSE
WHERE customer_code = 'C001'
  AND is_current = TRUE;

INSERT INTO dw.dim_customer_scd
    (customer_code, customer_name, city, segment,
     valid_from, valid_to, is_current, version)
SELECT customer_code, customer_name,
       'Medan', 'Gold',
       TIMESTAMP '2025-06-01', NULL, TRUE,
       version + 1
FROM dw.dim_customer_scd
WHERE customer_code = 'C001'
ORDER BY version DESC
LIMIT 1;

COMMIT;"""),
        ),
        content(
            "🕰️ Point-in-Time",
            "Melihat Konteks Saat Transaksi Terjadi",
            "Fact harus menyimpan surrogate key versi yang tepat, bukan hanya natural key:",
            code("""SELECT f.order_id, f.net_revenue,
       c.city, c.segment
FROM dw.fact_sales f
JOIN dw.dim_customer_scd c
  ON c.customer_key = f.customer_key
WHERE c.customer_code = 'C001'
  AND TIMESTAMP '2025-03-01 12:00:00' >= c.valid_from
  AND (TIMESTAMP '2025-03-01 12:00:00' < c.valid_to
       OR c.valid_to IS NULL);""")
            + callout("blue", "💡 Tanpa SCD2, laporan historis akan memakai kota/segmen saat ini — bukan saat transaksi terjadi."),
        ),
        content(
            "📦 Late-Arriving Dimension",
            "Saat Fact Tiba Sebelum Dimensi",
            "Tiga strategi yang umum:",
            grid(
                [
                    card("👻", "Inferred Member", "Buat baris dimensi sementara (`is_inferred = TRUE`), fact tetap dimuat.", "#0284c7"),
                    card("⏸️", "Hold Fact", "Tunda fact sampai dimensi lengkap. Data bersih, pipeline tertahan.", "#d97706"),
                    card("🔧", "Late Update", "Muat dengan key sementara, update atribut saat dimensi tiba.", "#059669"),
                    card("🛡️", "Integritas", "Jangan buang fact diam-diam; catat ke reject table dan alert.", "#dc2626"),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "SCD2 End-to-End",
            "Buktikan histori dan konsistensi:",
            steps([
                ("Buat skema", "Tabel SCD2 + partial unique index."),
                ("Insert awal", "C001 Banda Aceh Silver."),
                ("Ubah 3×", "Segmen, kota, segmen lagi."),
                ("Verifikasi", "Hanya satu current; tidak ada tumpang tindih."),
                ("Point-in-time", "Query untuk 3 tanggal berbeda."),
                ("Galaxy", "Buat fact kedua + drill-across."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Kapan SCD Tipe 1 cukup?", "Saat histori tidak dibutuhkan dan perubahan hanya koreksi data, misalnya memperbaiki ejaan nama yang salah."),
                ("Mengapa fact menyimpan customer_key, bukan customer_code?", "Agar setiap transaksi terhubung ke versi dimensi yang berlaku saat itu. Natural key bisa sama untuk banyak versi SCD2."),
                ("Apa risiko late-arriving dimension?", "Fact bisa menunjuk key yang belum ada atau dimensi dibuat sementara. Solusinya inferred member, hold, atau late update yang terkontrol."),
            ]),
        ),
        closing(
            "Dimensi yang berubah bukan masalah — kehilangan histori itulah masalahnya.",
            [("📖 Modul 4", "Snowflake & SCD"), ("🧪 Tugas 4", "SCD2 + galaxy"), ("➡️ Berikutnya", "ETL & kualitas")],
            "Selesaikan Tugas 4 dan buktikan query point-in-time mengembalikan atribut yang benar.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 5
# ---------------------------------------------------------------------------
DECK5 = {
    "num": 5,
    "slug": "etl-kualitas-data",
    "file": "pertemuan-5-etl-kualitas-data.html",
    "module": "05-etl-kualitas-data",
    "title": "ETL & Kualitas Data",
    "subtitle": "Pipeline yang idempoten, incremental, dan berani berhenti saat data buruk.",
    "description": "Slide interaktif Pertemuan 5 Data Warehouse IFR237: extract full/incremental/CDC, watermark, transformasi, deduplikasi, upsert/merge, data quality, reject table, rekonsiliasi, dan orkestrasi.",
    "slides": [
        dw_cover(
            5,
            "ETL & Kualitas Data",
            "Pipeline yang idempoten, incremental, dan berani berhenti saat data buruk.",
            [("3 Tahap", "Extract · Transform · Load"), ("5 Checks", "Kualitas data"), ("1 Bukti", "Idempoten")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 5",
            "Setelah sesi ini, Anda mampu membangun ETL yang aman dijalankan ulang dan dapat diaudit.",
            grid(
                [
                    checklist([
                        "Memilih full, incremental, atau CDC",
                        "Menggunakan watermark dengan benar",
                        "Membersihkan & menstandarkan data",
                        "Melakukan upsert/merge idempoten",
                        "Menulis reject table & rekonsiliasi",
                        "Membuktikan pipeline aman diulang",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Extract<br>2️⃣ Transform<br>3️⃣ Load idempoten<br>4️⃣ Kualitas data<br>5️⃣ Orkestrasi<br>6️⃣ Lab", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — EXTRACT", "Mengambil Data dengan Aman", "Pilih strategi yang sesuai volume, frekuensi, dan kebutuhan latensi."),
        content(
            "📥 Tiga Strategi Extract",
            "Full vs Incremental vs CDC",
            "Incremental hampir selalu lebih baik untuk data besar, tetapi butuh kolom andal:",
            table(
                ["Strategi", "Cara", "Kelebihan", "Risiko"],
                [
                    ["Full", "Ambil semua data", "Sederhana", "Berat, boros"],
                    ["Incremental", "Berdasarkan watermark", "Efisien", "Data telat bisa terlewat"],
                    ["CDC", "Baca log perubahan", "Near-real-time", "Infrastruktur kompleks"],
                ],
            ),
        ),
        content(
            "🌊 Watermark",
            "Menyimpan Batas Data Terakhir",
            "Gunakan `>` dan proses ulang jendela waktu untuk data terlambat:",
            code("""CREATE SCHEMA IF NOT EXISTS etl;

CREATE TABLE etl.watermark (
    pipeline       TEXT PRIMARY KEY,
    last_loaded_at TIMESTAMP NOT NULL
);

INSERT INTO etl.watermark (pipeline, last_loaded_at)
VALUES ('orders_incremental', TIMESTAMP '2024-01-01')
ON CONFLICT (pipeline) DO NOTHING;

SELECT *
FROM oltp.orders
WHERE updated_at > (
    SELECT last_loaded_at
    FROM etl.watermark
    WHERE pipeline = 'orders_incremental'
);""")
            + callout("amber", "⚠️ Jika sumber tidak punya `updated_at`, tambahkan trigger atau gunakan CDC."),
        ),
        divider("BAGIAN II — TRANSFORM & LOAD", "Membersihkan dan Menulis Tanpa Duplikasi", "Aturan bisnis harus eksplisit dan dapat diuji."),
        content(
            "🧹 Aturan Transformasi",
            "Standarisasi Sebelum Masuk DW",
            "Kualitas dimensi dan measure ditentukan di sini:",
            table(
                ["Masalah", "Contoh", "Solusi"],
                [
                    ["Huruf/spasi", "`Banda  ACEH`", "`LOWER(TRIM())`, regex"],
                    ["Tanggal", "`01/09/2024`", "`TO_TIMESTAMP` format eksplisit"],
                    ["Nilai kosong", "`''`, `'-'`", "`NULLIF`"],
                    ["Mata uang", "`Rp 1.000.000`", "Bersihkan non-digit"],
                    ["Duplikat", "order line ganda", "`ROW_NUMBER()`"],
                ],
            ),
        ),
        content(
            "🧽 Deduplikasi",
            "Ambil Versi Terbaru per Business Key",
            "Jangan mengandalkan `DISTINCT`; gunakan urutan yang jelas:",
            code("""WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY order_id, line_no
               ORDER BY updated_at DESC
           ) AS rn
    FROM staging.raw_orders
)
SELECT *
FROM ranked
WHERE rn = 1;"""),
        ),
        content(
            "♻️ Load Idempoten",
            "Dijalankan Dua Kali, Hasilnya Sama",
            "Tiga pola utama:",
            grid(
                [
                    card("➕", "Append + Unique", "`ON CONFLICT DO NOTHING` — cocok untuk data yang tidak berubah.", "#0284c7"),
                    card("🔄", "Upsert", "`ON CONFLICT DO UPDATE` — cocok untuk koreksi/retur.", "#059669"),
                    card("🗓️", "Partition Overwrite", "Hapus partisi tanggal, muat ulang. Sederhana dan aman.", "#9333ea"),
                    card("🔀", "MERGE", "PostgreSQL 15+; cocok untuk sinkronisasi dimensi/fact.", "#d97706"),
                ],
                2,
            )
            + code("""INSERT INTO dw.fact_sales (...)
SELECT ...
ON CONFLICT (order_id, line_no) DO UPDATE
SET quantity    = EXCLUDED.quantity,
    net_revenue = EXCLUDED.net_revenue,
    cost        = EXCLUDED.cost;"""),
        ),
        divider("BAGIAN III — KUALITAS & OPERASIONAL", "Data Buruk Harus Berhenti di Gate", "Lebih baik pipeline gagal daripada dashboard menampilkan angka salah."),
        content(
            "📏 Dimensi Kualitas",
            "Tujuh Pertanyaan Wajib",
            "Setiap dimensi punya ambang dan aksi berbeda:",
            table(
                ["Dimensi", "Pertanyaan", "Contoh Uji"],
                [
                    ["Completeness", "Semua data ada?", "`null_rate < 1%`"],
                    ["Uniqueness", "Ada duplikat?", "`COUNT(*) = COUNT(DISTINCT key)`"],
                    ["Validity", "Nilai sesuai domain?", "`status IN ('paid','cancelled')`"],
                    ["Consistency", "Antar-tabel cocok?", "Semua FK ada di dimensi"],
                    ["Timeliness", "Cukup baru?", "`max(loaded_at) > now()-2h`"],
                    ["Accuracy", "Cocok dengan sumber?", "Rekonsiliasi revenue"],
                    ["Volume", "Jumlah wajar?", "±30% baseline 7 hari"],
                ],
            ),
        ),
        content(
            "🗑️ Reject & Rekonsiliasi",
            "Jangan Buang Data Diam-Diam",
            "Catat baris gagal dan buktikan angka sumber = angka warehouse:",
            grid(
                [
                    code("""CREATE TABLE etl.rejected_rows (
  reject_id BIGSERIAL PRIMARY KEY,
  pipeline  TEXT NOT NULL,
  reason    TEXT NOT NULL,
  payload   JSONB,
  rejected_at TIMESTAMP DEFAULT now()
);

INSERT INTO etl.rejected_rows
  (pipeline, reason, payload)
SELECT 'orders_incremental',
       'customer_not_found', TO_JSONB(s)
FROM staging.stg_orders s
LEFT JOIN dw.dim_customer c
  ON c.customer_code = s.customer_code
WHERE c.customer_key IS NULL;"""),
                    code("""-- Sumber
SELECT SUM(quantity * unit_price
           - COALESCE(discount,0)) AS source
FROM staging.stg_orders
WHERE status = 'paid';

-- Warehouse
SELECT SUM(net_revenue) AS target
FROM dw.fact_sales;

-- Selisih harus 0 atau dijelaskan"""),
                ],
                2,
            ),
        ),
        content(
            "🛠️ Orkestrasi",
            "Agar Pipeline Berjalan Tanpa Anda",
            "Komponen minimum operasional:",
            grid(
                [
                    card("⏰", "Scheduler", "Airflow/cron menjalankan sesuai jadwal.", "#0284c7"),
                    card("🔗", "Dependency", "Extract → dimension → fact → quality.", "#059669"),
                    card("🔁", "Retry", "3× dengan backoff untuk kegagalan sementara.", "#9333ea"),
                    card("📝", "Run Log", "Rows read/loaded/rejected, durasi, status.", "#d97706"),
                    card("🚨", "Alert", "Email/Slack saat gagal atau terlambat.", "#dc2626"),
                    card("🧪", "Quality Gate", "Blokir publish jika uji kritis gagal.", "#0f766e"),
                ],
                3,
            ),
        ),
        content(
            "💻 Praktikum",
            "ETL Incremental + 5 Quality Checks",
            "Gunakan data dari Pertemuan 3/4:",
            steps([
                ("Load CSV ke staging", "Gunakan pandas/SQLAlchemy."),
                ("Catat reject", "Customer C999 sengaja tidak ada."),
                ("Transform & load", "Lookup surrogate key + upsert."),
                ("Uji kualitas", "Duplikat, orphan, revenue, null, volume."),
                ("Jalankan dua kali", "Jumlah fact tidak bertambah."),
                ("Rekonsiliasi", "Sumber vs warehouse = 0."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa `>=` pada watermark bisa bermasalah?", "Baris dengan timestamp sama dapat diproses ulang atau terlewat. Gunakan `>` dengan batas yang disimpan, atau kunci unik + upsert agar aman."),
                ("Apa perbedaan reject table dan log error?", "Reject table menyimpan data yang gagal beserta alasannya untuk diperbaiki/diaudit; log error hanya mencatat kejadian teknis."),
                ("Bagaimana membuktikan ETL idempoten?", "Jalankan dua kali untuk periode yang sama, lalu tunjukkan jumlah baris dan nilai agregat tidak berubah."),
            ]),
        ),
        closing(
            "ETL yang baik tidak hanya memindahkan data — ia membuktikan bahwa data itu benar.",
            [("📖 Modul 5", "ETL & kualitas"), ("🧪 Tugas 5", "Incremental + checks"), ("➡️ Berikutnya", "OLAP & SQL")],
            "Selesaikan Tugas 5 dan lampirkan bukti idempotensi serta rekonsiliasi.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 6
# ---------------------------------------------------------------------------
DECK6 = {
    "num": 6,
    "slug": "olap-sql-analytics",
    "file": "pertemuan-6-olap-sql-analytics.html",
    "module": "06-olap-sql-analytics",
    "title": "OLAP & SQL Analytics",
    "subtitle": "Roll-up, drill-down, window function, dan insight yang dapat ditindaklanjuti.",
    "description": "Slide interaktif Pertemuan 6 Data Warehouse IFR237: kubus OLAP, roll-up/drill-down/slice/dice/pivot, ROLLUP/CUBE/GROUPING SETS, window functions YTD/YoY, top-N, share of total, dan materialized view.",
    "slides": [
        dw_cover(
            6,
            "OLAP & SQL Analytics",
            "Roll-up, drill-down, window function, dan insight yang dapat ditindaklanjuti.",
            [("6 Operasi", "OLAP"), ("3 Window", "YTD · YoY · MA"), ("8 Query", "Praktikum")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 6",
            "Setelah sesi ini, Anda mampu menjawab pertanyaan bisnis dengan SQL analitik yang benar.",
            grid(
                [
                    checklist([
                        "Menjelaskan operasi OLAP",
                        "Menulis ROLLUP, CUBE, GROUPING SETS",
                        "Menggunakan window function",
                        "Menghitung YTD, YoY, moving average",
                        "Menghitung share & top-N",
                        "Menerjemahkan query menjadi insight",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Konsep kubus<br>2️⃣ Operasi OLAP<br>3️⃣ SQL agregasi<br>4️⃣ Window functions<br>5️⃣ Pola BI<br>6️⃣ Praktikum", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — KONSEP OLAP", "Data sebagai Kubus", "Satu measure dapat dilihat dari banyak dimensi dan level."),
        content(
            "🧊 Elemen Kubus",
            "Dimension, Hierarchy, Measure",
            "Memahami elemen ini membuat query analitik lebih mudah dirancang:",
            grid(
                [
                    card("📅", "Dimension", "Sumbu analisis: waktu, produk, wilayah, segmen.", "#0284c7"),
                    card("🪜", "Hierarchy", "Tahun → Kuartal → Bulan → Hari.", "#059669"),
                    card("📊", "Measure", "Angka yang diukur: revenue, quantity, margin.", "#9333ea"),
                    card("🎯", "Cube", "Ruang multidimensi: revenue per bulan × kategori × kota.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "🔧 Operasi OLAP",
            "Enam Cara Melihat Data",
            "Semua operasi ini dapat ditulis dengan SQL:",
            table(
                ["Operasi", "Arti", "Contoh"],
                [
                    ["Roll-up", "Naik level agregasi", "Bulan → Kuartal → Tahun"],
                    ["Drill-down", "Turun ke detail", "Tahun → Bulan → Hari"],
                    ["Slice", "Pilih satu nilai", "Hanya tahun 2025"],
                    ["Dice", "Subset beberapa dimensi", "2025 + Elektronik + Medan"],
                    ["Pivot", "Tukar baris/kolom", "Bulan jadi kolom"],
                    ["Drill-across", "Gabung beberapa fact", "Sales vs Returns"],
                ],
            ),
        ),
        divider("BAGIAN II — SQL AGREGASI", "Dari GROUP BY ke Kubus", "ROLLUP, CUBE, dan GROUPING SETS menghasilkan subtotal otomatis."),
        content(
            "📊 ROLLUP & CUBE",
            "Subtotal Tanpa UNION Manual",
            "ROLLUP untuk hierarki; CUBE untuk semua kombinasi:",
            code("""-- Roll-up: tahun -> bulan
SELECT d.year, d.month, SUM(f.net_revenue) AS revenue
FROM dw.fact_sales f
JOIN dw.dim_date d ON d.date_key = f.date_key
GROUP BY ROLLUP (d.year, d.month)
ORDER BY d.year NULLS LAST, d.month NULLS LAST;

-- Cube: semua kombinasi kategori x region
SELECT p.category, s.region, SUM(f.net_revenue) AS revenue
FROM dw.fact_sales f
JOIN dw.dim_product p ON p.product_key = f.product_key
JOIN dw.dim_store s   ON s.store_key = f.store_key
GROUP BY CUBE (p.category, s.region)
ORDER BY p.category NULLS LAST, s.region NULLS LAST;"""),
        ),
        content(
            "🔄 Pivot & GROUPING SETS",
            "Membentuk Laporan Matriks",
            "Pivot dengan FILTER; GROUPING SETS untuk kombinasi terpilih:",
            code("""SELECT p.category,
  SUM(f.net_revenue) FILTER (WHERE d.month = 1) AS jan,
  SUM(f.net_revenue) FILTER (WHERE d.month = 2) AS feb,
  SUM(f.net_revenue) FILTER (WHERE d.month = 3) AS mar,
  SUM(f.net_revenue) AS total_q1
FROM dw.fact_sales f
JOIN dw.dim_date d    ON d.date_key = f.date_key
JOIN dw.dim_product p ON p.product_key = f.product_key
WHERE d.year = 2025 AND d.quarter = 1
GROUP BY p.category
ORDER BY total_q1 DESC;""")
            + callout("green", "✅ Pivot mengubah hasil panjang menjadi lebar — lebih mudah dibaca di dashboard."),
        ),
        divider("BAGIAN III — WINDOW FUNCTIONS", "Analisis Tanpa Menggabungkan Baris", "Setiap baris tetap ada, tetapi dapat melihat baris lain."),
        content(
            "📈 YTD & Moving Average",
            "Running Total per Tahun",
            "Berguna untuk laporan keuangan dan monitoring tren:",
            code("""WITH monthly AS (
  SELECT d.year, d.month, SUM(f.net_revenue) AS revenue
  FROM dw.fact_sales f
  JOIN dw.dim_date d ON d.date_key = f.date_key
  GROUP BY d.year, d.month
)
SELECT year, month, revenue,
  SUM(revenue) OVER (
    PARTITION BY year ORDER BY month
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS ytd,
  ROUND(AVG(revenue) OVER (
    ORDER BY year, month
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ), 2) AS ma_3m
FROM monthly
ORDER BY year, month;"""),
        ),
        content(
            "📉 YoY & Share",
            "Membandingkan dengan Periode Lalu",
            "`LAG` untuk periode sebelumnya; window total untuk kontribusi:",
            code("""-- Year-over-Year
SELECT year, month, revenue,
  LAG(revenue, 12) OVER (ORDER BY year, month) AS last_year,
  ROUND((revenue - LAG(revenue, 12) OVER (ORDER BY year, month))
        / NULLIF(LAG(revenue, 12) OVER (ORDER BY year, month), 0)
        * 100, 2) AS yoy_pct
FROM monthly
ORDER BY year, month;

-- Share of total per kategori
SELECT p.category,
  SUM(f.net_revenue) AS revenue,
  ROUND(SUM(f.net_revenue)
        / SUM(SUM(f.net_revenue)) OVER () * 100, 2) AS share_pct
FROM dw.fact_sales f
JOIN dw.dim_product p ON p.product_key = f.product_key
GROUP BY p.category
ORDER BY revenue DESC;"""),
        ),
        content(
            "🏆 Top-N per Kategori",
            "ROW_NUMBER dengan Partisi",
            "Jangan gunakan `LIMIT` global jika butuh top-N per grup:",
            code("""WITH product_revenue AS (
  SELECT p.category, p.product_name,
         SUM(f.net_revenue) AS revenue
  FROM dw.fact_sales f
  JOIN dw.dim_product p ON p.product_key = f.product_key
  GROUP BY p.category, p.product_name
),
ranked AS (
  SELECT *,
         ROW_NUMBER() OVER (
           PARTITION BY category
           ORDER BY revenue DESC
         ) AS rn
  FROM product_revenue
)
SELECT category, product_name, revenue, rn
FROM ranked
WHERE rn <= 3
ORDER BY category, rn;"""),
        ),
        content(
            "⚡ Materialized View",
            "Agregat Siap Saji untuk Dashboard",
            "Query dashboard berulang tidak perlu memindai fact setiap kali:",
            code("""CREATE MATERIALIZED VIEW dw.mv_sales_monthly AS
SELECT d.year, d.month, p.category,
       SUM(f.net_revenue) AS revenue,
       SUM(f.quantity)    AS units,
       SUM(f.margin)      AS margin
FROM dw.fact_sales f
JOIN dw.dim_date d    ON d.date_key = f.date_key
JOIN dw.dim_product p ON p.product_key = f.product_key
GROUP BY d.year, d.month, p.category;

CREATE UNIQUE INDEX ON dw.mv_sales_monthly
    (year, month, category);

REFRESH MATERIALIZED VIEW CONCURRENTLY dw.mv_sales_monthly;""")
            + callout("amber", "⚠️ Data bisa tertinggal sampai refresh. Dokumentasikan SLA kesegaran data."),
        ),
        content(
            "💻 Praktikum",
            "Delapan Query OLAP",
            "Setiap query harus disertai pertanyaan bisnis dan insight:",
            steps([
                ("Tren", "Revenue per kategori per bulan."),
                ("Roll-up", "Revenue per kuartal & tahunan."),
                ("Drill-down", "Tahun → bulan → hari."),
                ("Slice/dice", "Elektronik di Medan 2025."),
                ("Pivot", "Kategori × bulan Q1."),
                ("YoY", "Pertumbuhan bulanan."),
                ("Top-N", "3 produk teratas per kategori."),
                ("Share", "Kontribusi tiap kategori."),
            ]),
        ),
        content(
            "🏁 Milestone 1",
            "Dashboard Pertama",
            "Bukan tugas baru — checkpoint proyek akhir:",
            checklist([
                "Star schema berisi data",
                "8 query OLAP + insight",
                "Dokumentasi KPI (definisi & rumus)",
                "Draft dashboard/visualisasi",
                "README cara menjalankan",
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Apa beda ROLLUP dan CUBE?", "ROLLUP menghasilkan subtotal hierarkis (bulan → tahun → total). CUBE menghasilkan semua kombinasi dimensi, termasuk subtotal per dimensi secara independen."),
                ("Mengapa share of total tidak boleh dijumlahkan langsung?", "Persentase bersifat non-additive. Jika dijumlahkan, hasilnya bisa lebih dari 100% atau menyesatkan; hitung dari agregat pembilang/penyebut."),
                ("Kapan materialized view tepat dipakai?", "Saat query dashboard berulang dan mahal, data boleh tertinggal sesuai SLA, serta refresh dapat dijadwalkan."),
            ]),
        ),
        closing(
            "Query OLAP yang baik bukan yang paling rumit — tetapi yang menjawab keputusan dengan jelas.",
            [("📖 Modul 6", "OLAP & SQL"), ("🏁 Milestone 1", "8 query + dashboard"), ("➡️ Berikutnya", "Optimasi & dbt")],
            "Selesaikan Milestone 1 dan siapkan demo 10 menit untuk review kelompok.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 7
# ---------------------------------------------------------------------------
DECK7 = {
    "num": 7,
    "slug": "implementasi-optimasi",
    "file": "pertemuan-7-implementasi-optimasi.html",
    "module": "07-implementasi-optimasi",
    "title": "Implementasi & Optimasi Data Warehouse",
    "subtitle": "Index, partisi, materialized view, cloud DW, dan dbt — diukur, bukan ditebak.",
    "description": "Slide interaktif Pertemuan 7 Data Warehouse IFR237: physical design, EXPLAIN ANALYZE, index, partisi, materialized view, cloud DW, dbt models/tests, dan alur tuning terukur.",
    "slides": [
        dw_cover(
            7,
            "Implementasi & Optimasi",
            "Index, partisi, materialized view, cloud DW, dan dbt — diukur, bukan ditebak.",
            [("EXPLAIN", "Diagnosis"), ("Partisi", "Pruning"), ("dbt", "Transformasi teruji")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 7",
            "Setelah sesi ini, Anda mampu membuat query dashboard jauh lebih cepat dengan bukti pengukuran.",
            grid(
                [
                    checklist([
                        "Membaca EXPLAIN ANALYZE",
                        "Memilih index yang tepat",
                        "Mempartisi fact & membuktikan pruning",
                        "Membuat materialized view",
                        "Membangun model dbt + test",
                        "Mengukur before/after",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Physical design<br>2️⃣ Index & plan<br>3️⃣ Partisi & MV<br>4️⃣ Cloud DW<br>5️⃣ dbt<br>6️⃣ Tuning terukur", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — PHYSICAL DESIGN", "Model Logis vs Penyimpanan Fisik", "Model yang sama bisa dieksekusi dengan biaya yang sangat berbeda."),
        content(
            "🛠️ Teknik Optimasi",
            "Enam Alat Utama",
            "Pilih berdasarkan pola query, bukan kebiasaan:",
            table(
                ["Teknik", "Tujuan", "Kapan Dipakai"],
                [
                    ["Index", "Mempercepat filter/join", "Kolom sering difilter"],
                    ["Partition", "Memangkas data dibaca", "Fact besar per tanggal"],
                    ["Materialized view", "Simpan agregat", "Dashboard berulang"],
                    ["Clustering/sort", "Kelompokkan data sejenis", "Cloud DW"],
                    ["Columnar", "Baca kolom yang dipakai", "Analitik tabel lebar"],
                    ["Compression", "Kurangi I/O", "Semua tabel"],
                ],
            ),
        ),
        content(
            "🔍 EXPLAIN ANALYZE",
            "Melihat Apa yang Sebenarnya Terjadi",
            "Jangan menebak bottleneck — baca rencananya:",
            code("""EXPLAIN (ANALYZE, BUFFERS)
SELECT p.category, SUM(f.net_revenue)
FROM dw.fact_sales f
JOIN dw.dim_product p ON p.product_key = f.product_key
JOIN dw.dim_date d    ON d.date_key = f.date_key
WHERE d.year = 2025
GROUP BY p.category;""")
            + table(
                ["Node", "Arti", "Tindakan"],
                [
                    ["Seq Scan besar", "Scan seluruh tabel", "Index/partisi/filter"],
                    ["Sort besar", "Urutan mahal", "Index berurutan"],
                    ["Buffers read tinggi", "Banyak I/O", "Cache/kompresi/partisi"],
                ],
            ),
        ),
        content(
            "🧱 Index",
            "Tiga Jenis yang Paling Berguna",
            "Index mempercepat baca, tetapi memperlambat tulis:",
            grid(
                [
                    code("""-- Composite untuk filter + join
CREATE INDEX idx_fact_date_product
  ON dw.fact_sales (date_key, product_key);

-- Covering: sertakan measure
CREATE INDEX idx_fact_cover
  ON dw.fact_sales (date_key, product_key)
  INCLUDE (net_revenue, quantity);

-- BRIN untuk data append-only
CREATE INDEX idx_fact_brin
  ON dw.fact_sales USING BRIN (date_key);"""),
                    card("⚖️", "Trade-off", "Index berlebih memperlambat ETL. Ukur query yang benar-benar dipakai, lalu hapus index yang tidak terpakai.", "#d97706")
                    + callout("amber", "⚠️ Tabel kecil sering lebih cepat dengan seq scan. Index bukan solusi otomatis."),
                ],
                2,
            ),
        ),
        content(
            "📦 Partisi",
            "Partition Pruning",
            "Query hanya membaca partisi yang relevan:",
            code("""CREATE TABLE dw.fact_sales_part (
    sales_key    BIGSERIAL,
    date_key     INTEGER NOT NULL,
    product_key  BIGINT NOT NULL,
    net_revenue  NUMERIC(14,2) NOT NULL,
    PRIMARY KEY (sales_key, date_key)
) PARTITION BY RANGE (date_key);

CREATE TABLE dw.fact_sales_2024
  PARTITION OF dw.fact_sales_part
  FOR VALUES FROM (20240101) TO (20250101);

CREATE TABLE dw.fact_sales_2025
  PARTITION OF dw.fact_sales_part
  FOR VALUES FROM (20250101) TO (20260101);""")
            + callout("green", "✅ Unique constraint pada tabel terpartisi harus menyertakan partition key."),
        ),
        content(
            "⚡ Materialized View",
            "Agregat Siap Saji",
            "Cocok untuk dashboard; refresh terjadwal:",
            code("""CREATE MATERIALIZED VIEW dw.mv_sales_daily AS
SELECT date_key, product_key,
       SUM(net_revenue) AS revenue,
       SUM(quantity)    AS units
FROM dw.fact_sales
GROUP BY date_key, product_key;

CREATE UNIQUE INDEX ON dw.mv_sales_daily
    (date_key, product_key);

REFRESH MATERIALIZED VIEW CONCURRENTLY
    dw.mv_sales_daily;""")
            + callout("amber", "⚠️ Trade-off: query cepat, tetapi data tertinggal sampai refresh. Dokumentasikan SLA."),
        ),
        divider("BAGIAN II — CLOUD DW & DBT", "Prinsip Sama, Platform Berbeda", "Columnar, pruning, dan transformasi sebagai kode."),
        content(
            "☁️ Cloud Data Warehouse",
            "Empat Platform, Satu Prinsip",
            "Pisahkan storage & compute, pindai sesedikit mungkin:",
            table(
                ["Platform", "Karakteristik", "Optimasi Kunci"],
                [
                    ["BigQuery", "Serverless, columnar", "Partition, cluster, hindari SELECT *"],
                    ["Snowflake", "Multi-cluster, micro-partition", "Clustering key, warehouse sizing"],
                    ["Redshift", "MPP, columnar", "Dist/sort key, vacuum/analyze"],
                    ["DuckDB", "In-process columnar", "Parquet, predicate pushdown"],
                ],
            ),
        ),
        content(
            "🧰 dbt",
            "Transformasi sebagai Kode",
            "Model, test, dokumentasi, dan lineage dalam satu proyek:",
            grid(
                [
                    card("📁", "models/staging", "Bersihkan & standarkan sumber.", "#0284c7"),
                    card("⭐", "models/marts", "Dim & fact siap BI.", "#059669"),
                    card("🧪", "schema.yml", "Test not_null, unique, relationships.", "#9333ea"),
                    card("📖", "dbt docs", "Lineage & dokumentasi otomatis.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "🐍 Model dbt",
            "Staging & Fact Incremental",
            "`ref()` menjaga dependensi; `is_incremental()` memproses data baru:",
            code("""-- models/marts/fct_sales.sql
{{ config(materialized='incremental',
          unique_key=['order_id','line_no']) }}

SELECT
  TO_CHAR(o.order_ts, 'YYYYMMDD')::INT AS date_key,
  p.product_key, c.customer_key, s.store_key,
  o.order_id,
  ROW_NUMBER() OVER (PARTITION BY o.order_id
                     ORDER BY o.product_code)::INT AS line_no,
  o.quantity,
  o.quantity * o.unit_price AS gross_revenue,
  o.discount,
  o.quantity * o.unit_price - o.discount AS net_revenue,
  o.quantity * p.cost AS cost
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('dim_product') }} p  ON p.product_code = o.product_code
JOIN {{ ref('dim_customer') }} c ON c.customer_code = o.customer_code
JOIN {{ ref('dim_store') }} s    ON s.store_code = o.store_code

{% if is_incremental() %}
WHERE TO_CHAR(o.order_ts, 'YYYYMMDD')::INT
      > (SELECT COALESCE(MAX(date_key), 0) FROM {{ this }})
{% endif %}"""),
        ),
        content(
            "🧪 Test dbt",
            "Kualitas Data sebagai Kode",
            "Test berjalan di CI dan mencegah model buruk dipublikasikan:",
            code("""# models/marts/schema.yml
version: 2

models:
  - name: fct_sales
    columns:
      - name: order_id
        tests: [not_null]
      - name: net_revenue
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: ">= 0"
""")
            + callout("green", "✅ <span class='pill-code'>dbt test</span> + <span class='pill-code'>dbt docs generate</span> memberi kepercayaan dan lineage."),
        ),
        divider("BAGIAN III — TUNING TERUKUR", "Ukur, Perbaiki, Ukur Lagi", "Optimasi tanpa baseline hanyalah opini."),
        content(
            "🧭 Alur Tuning",
            "Lima Langkah",
            "Dokumentasikan setiap perubahan:",
            steps([
                ("Baseline", "Catat waktu & buffers query."),
                ("Diagnosis", "EXPLAIN ANALYZE: scan, join, sort."),
                ("Perbaikan", "Index, partisi, MV, rewrite."),
                ("Ukur ulang", "Metrik yang sama, data yang sama."),
                ("Simpan bukti", "Tabel before/after + kesimpulan."),
            ]),
        ),
        content(
            "💻 Praktikum",
            "Lima Eksperimen Optimasi",
            "Gunakan fact table dan query dari Pertemuan 6:",
            steps([
                ("E1", "Baseline + EXPLAIN."),
                ("E2", "Tambah index `(date_key)`."),
                ("E3", "Tambah composite `(date_key, product_key)`."),
                ("E4", "Partisi fact per tahun; cek pruning."),
                ("E5", "Materialized view untuk dashboard."),
                ("Laporan", "Tabel waktu & buffers + kesimpulan."),
            ]),
        ),
        content(
            "🏁 Milestone 2",
            "Optimasi & dbt",
            "Checkpoint proyek akhir:",
            checklist([
                "Query plan before/after minimal 2 query",
                "Index/partisi/MV yang diterapkan",
                "3 model dbt + test",
                "Dokumentasi performa & kesimpulan",
                "README cara menjalankan",
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa menambah index bisa memperlambat pipeline?", "Setiap INSERT/UPDATE harus memperbarui index. Terlalu banyak index memperbesar biaya tulis dan storage."),
                ("Apa bukti bahwa partisi bekerja?", "Rencana query hanya menyebut partisi yang relevan (partition pruning), dan jumlah buffer/baris yang dipindai turun."),
                ("Apa manfaat dbt dibanding skrip SQL lepas?", "Model ber-versi, dependensi otomatis via ref(), test kualitas, dokumentasi, dan lineage — semuanya dapat dijalankan di CI."),
            ]),
        ),
        closing(
            "Optimasi yang baik selalu punya angka sebelum dan sesudah.",
            [("📖 Modul 7", "Optimasi & dbt"), ("🏁 Milestone 2", "Before/after + dbt"), ("➡️ Berikutnya", "Capstone & UAS")],
            "Selesaikan Milestone 2 dengan tabel before/after dan model dbt yang lulus test.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 8
# ---------------------------------------------------------------------------
DECK8 = {
    "num": 8,
    "slug": "capstone-tata-kelola",
    "file": "pertemuan-8-dw-capstone.html",
    "module": "08-capstone-tata-kelola",
    "title": "Proyek Akhir, Tata Kelola & UAS",
    "subtitle": "Membuktikan data warehouse yang berjalan, dipercaya, aman, dan masuk akal secara biaya.",
    "description": "Slide interaktif Pertemuan 8 Data Warehouse IFR237: arsitektur capstone, deliverables, metadata & lineage, keamanan, UU PDP, masking PII, optimasi biaya, anti-pattern, rubrik, dan demo UAS.",
    "slides": [
        dw_cover(
            8,
            "Proyek Akhir, Tata Kelola & UAS",
            "Membuktikan data warehouse yang berjalan, dipercaya, aman, dan masuk akal secara biaya.",
            [("1 Command", "Dapat dijalankan"), ("UU PDP", "Privasi"), ("100 Poin", "Rubrik UAS")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 8",
            "Setelah sesi ini, Anda mampu mempertahankan proyek secara teknis, etis, dan ekonomis.",
            grid(
                [
                    checklist([
                        "Menyajikan arsitektur end-to-end",
                        "Mendokumentasikan metadata & lineage",
                        "Menerapkan akses minimum",
                        "Menangani PII sesuai UU PDP",
                        "Menghitung biaya & penghematan",
                        "Menghindari anti-pattern",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Capstone & deliverables<br>2️⃣ Tata kelola<br>3️⃣ Keamanan & privasi<br>4️⃣ Biaya<br>5️⃣ Anti-pattern<br>6️⃣ Rubrik & demo", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — CAPSTONE", "Dari Requirement ke Dashboard", "Satu sistem yang dapat dijalankan ulang dari kondisi bersih."),
        content(
            "🏗️ Arsitektur Capstone",
            "Enam Lapisan yang Harus Terlihat",
            "Setiap lapisan punya bukti: DDL, kode ETL, query, atau dokumentasi:",
            steps([
                ("Source", "POS/orders, CRM, inventory — minimal 2 sumber."),
                ("Staging", "Tabel `stg_*` / `raw_*` dengan metadata load."),
                ("Integration", "Dimensi, SCD2, surrogate key, aturan bisnis."),
                ("Fact", "Minimal 1 fact table dengan grain jelas."),
                ("Serving", "8 query OLAP + dashboard/visualisasi."),
                ("Operations", "Quality checks, log, dokumentasi, keamanan."),
            ])
            + callout("blue", "💡 Diagram harus menunjukkan <b>aliran data</b> dan <b>cross-cutting concerns</b>, bukan hanya logo tools."),
        ),
        content(
            "🎯 Pilihan Studi Kasus",
            "Satu Domain, Ruang Lingkup Jelas",
            "Pilih yang datanya dapat diperoleh atau dibangkitkan:",
            table(
                ["Kasus", "Pertanyaan Bisnis", "Fact Utama"],
                [
                    ["Retail sales", "Kategori/toko mana yang untung?", "fact_sales"],
                    ["E-commerce funnel", "Di tahap mana pengguna berhenti?", "fact_funnel"],
                    ["Inventory", "Kapan stok menipis/berlebih?", "fact_inventory"],
                    ["Perbankan", "Segmen mana berisiko?", "fact_transactions"],
                    ["Klinik", "Bagaimana utilisasi layanan?", "fact_visits"],
                    ["Kampus", "Bagaimana performa akademik?", "fact_enrollment"],
                ],
            ),
        ),
        content(
            "📦 Deliverables",
            "Sepuluh Artefak yang Dinilai",
            "Dokumentasi sama pentingnya dengan kode:",
            grid(
                [
                    card("📁", "Repositori", "DDL, ETL, dbt, query, README.", "#0284c7"),
                    card("📄", "Requirement", "Stakeholder, pertanyaan, KPI.", "#059669"),
                    card("🧩", "Bus matrix", "Proses × dimensi, grain.", "#9333ea"),
                    card("⭐", "Model dimensional", "Diagram, data dictionary.", "#d97706"),
                    card("⚙️", "ETL", "Incremental, idempoten, reject.", "#dc2626"),
                    card("🧪", "Quality checks", "≥5 uji + rekonsiliasi.", "#0f766e"),
                    card("📊", "OLAP & serving", "8 query + dashboard.", "#7c3aed"),
                    card("⚡", "Optimasi", "Before/after terukur.", "#0891b2"),
                    card("🛡️", "Governance", "Ownership, lineage, PII.", "#be123c"),
                ],
                3,
            ),
        ),
        content(
            "🚀 One Command",
            "Dosen Harus Bisa Menjalankan Tanpa Anda",
            "Uji dari kondisi bersih sebelum demo:",
            code("""git clone <repo>
cd dw-project
cp .env.example .env
docker compose up -d

make seed      # data sumber
make etl       # dimensi + fact
make quality   # 5 checks + rekonsiliasi
make test      # unit/integration test

# Buka dashboard/query
psql -U postgres -d retail_dw -f sql/olap_queries.sql"""),
        ),
        divider("BAGIAN II — TATA KELOLA & KEAMANAN", "Data yang Tidak Dikelola Akan Menjadi Beban", "Metadata, lineage, akses, dan audit membuat data dapat dipercaya."),
        content(
            "🗂️ Komponen Tata Kelola",
            "Tujuh Pertanyaan Wajib",
            "Tanpa ini, debugging dan audit menjadi mustahil:",
            table(
                ["Komponen", "Pertanyaan", "Artefak"],
                [
                    ["Metadata", "Apa arti tabel/kolom?", "Data dictionary"],
                    ["Lineage", "Dari mana angka ini?", "Diagram sumber → fact"],
                    ["Ownership", "Siapa penanggung jawab?", "Data owner"],
                    ["Kualitas", "Seberapa andal?", "Quality report & SLA"],
                    ["Retensi", "Berapa lama disimpan?", "Kebijakan retensi"],
                    ["Akses", "Siapa boleh melihat?", "RBAC/row security"],
                    ["Metrik", "Apa rumus resmi KPI?", "Metric dictionary"],
                ],
            ),
        ),
        content(
            "📖 Data & Metric Dictionary",
            "Definisi yang Disepakati",
            "Perbedaan definisi adalah sumber konflik laporan paling umum:",
            table(
                ["Metrik", "Definisi", "Rumus"],
                [
                    ["Net Revenue", "Pendapatan setelah diskon", "`SUM(qty*price - discount)`"],
                    ["Gross Margin", "Laba kotor", "`SUM(net_revenue - cost)`"],
                    ["Margin %", "Persentase margin", "`margin / net_revenue * 100`"],
                    ["Active Customer", "Aktif 30 hari", "`COUNT(DISTINCT customer_key)`"],
                ],
            )
            + callout("green", "✅ Simpan definisi di repositori dan review setiap perubahan."),
        ),
        content(
            "🔗 Lineage",
            "Impact Analysis dalam Satu Diagram",
            "Jika definisi berubah, ketahui dashboard mana yang terdampak:",
            steps([
                ("oltp.orders", "Sumber transaksi."),
                ("staging.stg_orders", "Bersihkan & standarkan."),
                ("dw.dim_customer", "SCD2 + surrogate key."),
                ("dw.fact_sales", "Grain: item pesanan."),
                ("dw.mv_sales_monthly", "Agregat dashboard."),
                ("Dashboard Revenue", "Konsumsi pengguna."),
            ]),
        ),
        content(
            "🔐 Keamanan",
            "Kontrol yang Tidak Boleh Ditawar",
            "CIA triad diterjemahkan menjadi kontrol konkret:",
            table(
                ["Area", "Kontrol"],
                [
                    ["Autentikasi", "SSO/MFA, akun ETL terpisah"],
                    ["Otorisasi", "Least privilege, role analyst/engineer/admin"],
                    ["Enkripsi", "TLS in transit, AES-256 at rest"],
                    ["Masking", "Email/telepon disamarkan untuk analis"],
                    ["Audit", "Log query & akses tabel sensitif"],
                    ["Backup", "Backup terjadwal + uji restore"],
                ],
            )
            + code("""CREATE ROLE dw_analyst NOLOGIN;
GRANT USAGE ON SCHEMA dw TO dw_analyst;
GRANT SELECT ON dw.fact_sales, dw.dim_product,
                dw.dim_date TO dw_analyst;
-- Tidak memberikan akses ke dim_customer (PII)"""),
        ),
        content(
            "🇮🇩 UU PDP & PII",
            "Privasi Bukan Beban Kepatuhan",
            "UU No. 27/2022 mengatur data pribadi dan hak subjek data:",
            grid(
                [
                    card("📋", "Prinsip", "Minimisasi, tujuan terbatas, retensi terbatas, keamanan.", "#0284c7"),
                    card("⏰", "Notifikasi Bocor", "Maksimal 3×24 jam kepada subjek & otoritas.", "#dc2626"),
                    card("🎭", "Pseudonimisasi", "Token/hash untuk analitik; mapping terpisah.", "#9333ea"),
                    card("🕵️", "Re-identifikasi", "Quasi-identifier (tanggal lahir + kode pos) tetap berisiko.", "#d97706"),
                ],
                2,
            )
            + code("""CREATE VIEW dw.v_customer_masked AS
SELECT customer_key, customer_code,
       LEFT(customer_name,1) || '***' AS customer_name,
       city, segment,
       REGEXP_REPLACE(email,
         '(^.{2}).*(@.*$)', '\\1***\\2') AS email
FROM dw.dim_customer;"""),
        ),
        divider("BAGIAN III — BIAYA & EVALUASI", "Ekonomi Data Warehouse", "Optimasi teknis harus berdampak pada biaya dan kecepatan."),
        content(
            "💰 Optimasi Biaya",
            "Ukur, Jangan Menebak",
            "Contoh ilustratif: storage 500 GB, warehouse 2 credits × 8 jam/hari, scan 10 TB/bulan:",
            grid(
                [
                    code("""Storage : 500 x $0.02        = $10
Compute : 2 x 8 x 30 x $2    = $960
Scan    : 10 x $5            = $50
------------------------------------
Total kasar                   ~= $1.020/bln"""),
                    card("📉", "Penghematan", "Auto-suspend (compute ↓50%) · MV (scan ↓70–90%) · partition pruning (↓50–80%) · kompresi (storage ↓30–60%).", "#059669")
                    + callout("blue", "💡 Metrik: biaya per 1.000 query, biaya per refresh dashboard, bytes scanned."),
                ],
                2,
            ),
        ),
        content(
            "🚫 Anti-Pattern",
            "Kesalahan yang Paling Sering Terjadi",
            "Kenali sebelum proyek menjadi studi kasus:",
            table(
                ["Anti-pattern", "Akibat", "Perbaikan"],
                [
                    ["Skema OLTP untuk DW", "Query lambat", "Star schema"],
                    ["Grain tidak jelas", "Agregasi salah", "Deklarasi grain"],
                    ["Natural key di fact", "Join lambat", "Surrogate key"],
                    ["Tanpa SCD", "Histori hilang", "SCD2"],
                    ["ETL tidak idempoten", "Duplikasi", "Upsert/overwrite"],
                    ["Tanpa quality check", "Dashboard salah", "Quality gate"],
                    ["SELECT *", "Scan & biaya besar", "Pilih kolom"],
                    ["PII tersebar", "Risiko kepatuhan", "Masking & akses"],
                ],
            ),
        ),
        content(
            "🏆 Rubrik & Demo",
            "Bagaimana Proyek Dinilai",
            "Fokus pada bukti, bukan klaim:",
            grid(
                [
                    table(
                        ["Aspek", "Bobot"],
                        [
                            ["Requirement & KPI", "15%"],
                            ["Model dimensional", "20%"],
                            ["ETL & kualitas", "20%"],
                            ["OLAP & serving", "15%"],
                            ["Optimasi & biaya", "10%"],
                            ["Tata kelola & keamanan", "10%"],
                            ["Demo & dokumentasi", "10%"],
                        ],
                    ),
                    steps([
                        ("0–2 menit", "Masalah, stakeholder, KPI."),
                        ("2–4 menit", "Arsitektur & model dimensional."),
                        ("4–7 menit", "Demo ETL → quality → OLAP → dashboard."),
                        ("7–8 menit", "Simulasi kegagalan/quality gate."),
                        ("8–10 menit", "Optimasi, biaya, tata kelola."),
                    ]),
                ],
                2,
            ),
        ),
        content(
            "🎤 Pertahanan Proyek",
            "Delapan Pertanyaan Kunci",
            "Klik untuk melihat arah jawaban yang baik:",
            quiz([
                ("Mengapa memilih grain tersebut?", "Kaitkan dengan pertanyaan bisnis paling detail yang harus dijawab; grain harus atomik dan konsisten dengan fact."),
                ("Mengapa star atau snowflake?", "Star untuk kesederhanaan & kinerja BI; snowflake jika hierarki besar dan normalisasi memberi manfaat nyata."),
                ("Bagaimana SCD2 menangani perubahan?", "Tutup versi lama dengan valid_to, buat versi baru, pertahankan satu is_current, dan fact menyimpan surrogate key versi saat transaksi."),
                ("Apa yang terjadi jika ETL dijalankan dua kali?", "Harus idempoten: upsert/overwrite, jumlah baris dan agregat tidak berubah."),
                ("Bagaimana membuktikan data benar?", "Quality checks, rekonsiliasi sumber vs warehouse, uji integritas FK, dan validasi query."),
                ("Query mana yang paling mahal?", "Tunjukkan EXPLAIN ANALYZE, buffers, dan optimasi yang memberi dampak terbesar."),
                ("Di mana PII dan bagaimana dilindungi?", "Identifikasi di data dictionary, masking/pseudonimisasi, akses minimum, audit, retensi."),
                ("Apa yang berubah jika data naik 10×?", "Partisi, kompresi, MV, tuning, biaya, dan bottleneck baru."),
            ]),
        ),
        closing(
            "Data warehouse yang baik membuat keputusan lebih cepat, lebih konsisten, dan lebih dapat dipercaya.",
            [("📖 Modul 8", "Capstone & governance"), ("🏁 UAS", "Demo + laporan"), ("🎓 Selesai", "8 pertemuan")],
            "Siapkan demo 10 menit, laporan 8–12 halaman, dan pastikan proyek berjalan dari kondisi bersih.",
        ),
    ],
}


DECKS = [DECK1, DECK2, DECK3, DECK4, DECK5, DECK6, DECK7, DECK8]


def build_deck_dw(deck: dict) -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    head, rest = template.split("<body>", 1)
    head = re.sub(
        r"<title>.*?</title>",
        f"<title>Pertemuan {deck['num']} - {deck['title']} | Data Warehouse IFR237</title>",
        head,
        flags=re.S,
    )
    head = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{html.escape(deck["description"], quote=True)}">',
        head,
        flags=re.S,
    )
    head = head.replace("</style>", COMPACT_CSS + "</style>")
    suffix = rest.split("</main>", 1)[1]

    main_html, narrations = build_main(deck)
    header = f"""<body>
<header>
<div class="brand">
<img src="{BASE}/uuilogo.png" alt="UUI Logo" class="brand-logo" onerror="this.style.display='none'">
<div><div class="brand-text">DATA WAREHOUSE <span>(IFR237)</span></div><div class="brand-sub">Universitas Ubudiyah Indonesia — Pertemuan {deck['num']}</div></div>
</div>
<div class="header-controls">
<button class="audio-header-btn" id="btnAudioToggle" onclick="toggleAudio()" title="Putar/Jeda Narasi Dosen (P/S)">
  <div class="sound-wave paused" id="soundWaveIcon"><div class="sound-bar"></div><div class="sound-bar"></div><div class="sound-bar"></div></div>
  <span id="audioBtnLabel">🎙️ Narasi Dosen</span>
</button>
<label class="autoplay-label" title="Otomatis putar suara saat pindah slide (A)">
  <input type="checkbox" id="chkAutoplay">
  <span>Auto-Play</span>
</label>
<select class="speed-select" id="selAudioSpeed" onchange="changePlaybackRate(this.value)" title="Kecepatan Suara">
  <option value="1.0" selected>1.0x</option>
  <option value="1.25">1.25x</option>
  <option value="1.5">1.5x</option>
</select>
<span class="timer-badge" id="presentationTimer" title="Timer Presentasi (Klik: Jeda/Lanjut, Dobel Klik: Reset)">⏱️ 00:00</span>
<span class="slide-badge" id="slideIndicator">SLIDE 1 / …</span>
<button class="btn-icon" onclick="toggleFullscreen()" title="Fullscreen (F)">⛶ Fullscreen</button>
</div>
</header>
<main>
{main_html}
</main>"""

    suffix = re.sub(
        r"const audioTranscripts=\[.*?\];",
        "const audioTranscripts=" + json.dumps(narrations, ensure_ascii=False) + ";",
        suffix,
        flags=re.S,
    )
    suffix = re.sub(
        r"function getAudioUrl\(i\)\{.*?\}",
        f"function getAudioUrl(i){{const num=String(i+1).padStart(2,'0');return '{AUDIO_BASE}/m{deck['num']}/slide-'+num+'.mp3'}}",
        suffix,
        flags=re.S,
    )
    suffix = suffix.replace(
        "Penjelasan Dosen (Narasi AI — Pak Mahendar)",
        "Penjelasan Dosen (Narasi AI — Pak Mahendar)",
    )
    suffix = suffix.replace("let currentPlaybackRate=1.25;", "let currentPlaybackRate=1.0;")

    (PUBLIC / deck["file"]).write_text(head + header + suffix, encoding="utf-8")

    page = f"""# Slide: Pertemuan {deck['num']} — {deck['title']}

<div style="margin-bottom: 16px; display: flex; gap: 10px; flex-wrap: wrap;">
  <a href="{BASE}/presentasi/{deck['file']}" target="_blank" style="background-color: #0284c7; color: white; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
    ⛶ Buka Slide Layar Penuh (Tab Baru)
  </a>
  <a href="{BASE}/datawarehouse/{deck['module']}" style="background-color: #1e293b; color: #f8fafc; border: 1px solid #334155; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
    📖 Baca Modul Pertemuan {deck['num']}
  </a>
</div>

<div style="position: relative; width: 100%; height: 75vh; border-radius: 12px; overflow: hidden; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
  <iframe
    src="{BASE}/presentasi/{deck['file']}"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
    allowfullscreen="true">
  </iframe>
</div>

> [!TIP]
> **Petunjuk Presentasi & Audio Narasi:**
> * ⌨️ **Navigasi Slide:** Klik area slide, lalu gunakan tombol panah <kbd>◀</kbd> / <kbd>▶</kbd> atau <kbd>Spasi</kbd>. Tekan <kbd>F</kbd> untuk presentasi layar penuh.
> * 🎙️ **Audio Narasi Dosen:** Tekan tombol <kbd>P</kbd> atau <kbd>S</kbd> untuk memutar/menjeda narasi suara penjelasan materi slide saat ini.
> * 🔁 **Mode Auto-Play:** Tekan tombol <kbd>A</kbd> atau centang `Auto-Play` di header slide agar suara otomatis memutar penjelasan setiap kali berpindah slide.
> * 💬 **Transkrip & Subtitle:** Tekan tombol <kbd>C</kbd> untuk membuka/menutup teks transkrip penjelasan dosen.
"""
    (DOCS_PRESENTASI / f"pertemuan-{deck['num']}-datawarehouse.md").write_text(page, encoding="utf-8")
    print(f"OK  {deck['file']}  ({len(deck['slides'])} slides)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    DOCS_PRESENTASI.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for deck in DECKS:
        build_deck_dw(deck)
        manifest[f"m{deck['num']}"] = [n for _, n in deck["slides"]]
    (ROOT / "scratch" / "dw_audio_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Manifest: scratch/dw_audio_manifest.json")
