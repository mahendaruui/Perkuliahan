#!/usr/bin/env python3
"""Generate 8 interactive Big Data (IFR229) presentation decks.

The visual shell (CSS, keyboard navigation, timer, narration drawer) is reused
from the existing Visualisasi Data deck so all courses share one design system.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "docs" / "public" / "presentasi"
DOCS_PRESENTASI = ROOT / "docs" / "presentasi"
TEMPLATE = PUBLIC / "pertemuan-11-time-series.html"

BASE = "/Perkuliahan"
AUDIO_BASE = f"{BASE}/audio/big-data"

COMPACT_CSS = """
/* Big Data deck: compact density on short viewports */
@media (max-height: 820px){
  .slide{padding:28px 36px}
  h1.slide-title{font-size:1.95rem;margin-bottom:9px}
  h2.slide-subtitle{font-size:.95rem;margin-bottom:14px}
  .card-box{padding:13px 15px}
  .card-title{font-size:.98rem;margin-bottom:4px}
  .card-desc{font-size:.8rem;line-height:1.5}
  .custom-table th,.custom-table td{padding:6px 9px;font-size:.76rem}
  pre{font-size:.73rem;padding:11px;line-height:1.45}
  .step{padding:9px 12px}
  .step .txt p{font-size:.77rem}
  .steps{display:grid;grid-template-columns:1fr 1fr;gap:8px;align-items:stretch}
  .step{height:100%}
  .step .no{flex:0 0 28px;height:28px;font-size:.78rem}
  details.quiz{padding:10px 12px;margin-top:7px}
  details.quiz summary{font-size:.86rem}
  .callout{padding:9px 13px;font-size:.8rem}
  .check-list li{padding:7px 11px;font-size:.8rem}
  .grid-2,.grid-3,.grid-4{gap:12px}
}
"""


def esc(text: str) -> str:
    return html.escape(text.strip(), quote=False)


def code(text: str) -> str:
    return f"<pre><code>{esc(text)}</code></pre>"


def card(icon: str, title: str, desc: str, border: str = "") -> str:
    style = f' style="border-left:4px solid {border}"' if border else ""
    return (
        f'<div class="card-box"{style}>'
        f'<div class="card-title">{icon} {title}</div>'
        f'<div class="card-desc">{desc}</div></div>'
    )


def grid(cards: list[str], cols: int = 2) -> str:
    return f'<div class="grid-{cols} anim">{"".join(cards)}</div>'


def table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    return (
        f'<table class="custom-table anim"><thead><tr>{head}</tr></thead>'
        f"<tbody>{body}</tbody></table>"
    )


def callout(kind: str, text: str) -> str:
    return f'<div class="callout callout-{kind} anim">{text}</div>'


def checklist(items: list[str]) -> str:
    lis = "".join(f"<li><span>✔️</span>{i}</li>" for i in items)
    return f'<ul class="check-list anim">{lis}</ul>'


def steps(items: list[tuple[str, str]]) -> str:
    out = []
    for idx, (title, desc) in enumerate(items, 1):
        out.append(
            f'<div class="step"><div class="no">{idx}</div>'
            f'<div class="txt"><b>{title}</b><p>{desc}</p></div></div>'
        )
    return f'<div class="steps anim">{"".join(out)}</div>'


def quiz(items: list[tuple[str, str]]) -> str:
    out = []
    for q, a in items:
        out.append(
            f'<details class="quiz anim"><summary>❓ {q}</summary>'
            f'<div class="answer">✅ {a}</div></details>'
        )
    return "".join(out)


def cover(
    num: int,
    title: str,
    subtitle: str,
    stats: list[tuple[str, str]],
    badge: str | None = None,
) -> tuple[str, str]:
    badge = badge or f"🗄️ IFR229 · 3 SKS · KELAS RPL · PERTEMUAN {num} / 8"
    stat_html = "".join(f"<div class='stat'><b>{a}</b><small>{b}</small></div>" for a, b in stats)
    html_slide = f"""
<div class="slide active cover-slide">
<div class="hero-orbs"><div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div></div>
<div style="position:relative">
<span class="cover-badge">{badge}</span>
<h1 class="slide-title anim" style="font-size:2.5rem;max-width:980px;">{title}</h1>
<h2 class="slide-subtitle anim" style="max-width:840px;margin:0 auto 10px auto;">{subtitle}</h2>
<div class="stat-row anim" style="max-width:820px;margin:18px auto 0 auto;">{stat_html}</div>
<div class="avatar-box anim"><div class="avatar-img">MD</div><div class="author-info"><div class="author-name">Mahendar Dwi Payana, S.ST., M.T.</div><div class="author-role">Dosen Pengampu · Program Studi S1 Informatika · FST UUI</div></div></div>
</div>
</div>"""
    narration = (
        f"Selamat datang pada pertemuan {num} mata kuliah Big Data IFR229. "
        f"Topik kita hari ini adalah {title}. {subtitle} "
        "Mari kita mulai dengan memahami masalahnya, lalu membangun solusinya langkah demi langkah."
    )
    return html_slide, narration


def content(tag: str, title: str, subtitle: str, body: str) -> tuple[str, str]:
    return (
        f'<div class="slide"><div class="slide-tag">{tag}</div>'
        f'<h1 class="slide-title anim">{title}</h1>'
        f'<h2 class="slide-subtitle anim">{subtitle}</h2>{body}</div>',
        f"{title}. {subtitle}",
    )


def divider(label: str, title: str, subtitle: str) -> tuple[str, str]:
    return (
        f'<div class="slide divider-slide"><div class="divider-num">{label}</div>'
        f'<h1 class="slide-title">{title}</h1>'
        f'<h2 class="slide-subtitle">{subtitle}</h2></div>',
        f"Bagian berikutnya: {title}. {subtitle}",
    )


def closing(quote: str, stats: list[tuple[str, str]], next_text: str) -> tuple[str, str]:
    stat_html = "".join(f"<div class='stat'><b>{a}</b><small>{b}</small></div>" for a, b in stats)
    return (
        f"""<div class="slide cover-slide">
<div class="hero-orbs"><div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div></div>
<div style="position:relative">
<span class="cover-badge">✅ RANGKUMAN &amp; TINDAK LANJUT</span>
<h1 class="slide-title anim" style="font-size:2.4rem;">Terima Kasih &amp; Selamat Belajar!</h1>
<h2 class="slide-subtitle anim" style="max-width:800px;margin:0 auto 12px auto;">{quote}</h2>
<div class="stat-row anim" style="max-width:820px;margin:16px auto 0 auto;">{stat_html}</div>
<div class="avatar-box anim" style="margin-top:18px;"><div class="avatar-img">MD</div><div class="author-info"><div class="author-name">Mahendar Dwi Payana, S.ST., M.T.</div><div class="author-role">Program Studi S1 Informatika · Universitas Ubudiyah Indonesia</div></div></div>
</div></div>""",
        f"Demikian pertemuan kita. {quote} {next_text} Terima kasih, selamat belajar, dan sukses selalu.",
    )


# ---------------------------------------------------------------------------
# DECK 1
# ---------------------------------------------------------------------------
DECK1 = {
    "num": 1,
    "slug": "pengantar-big-data",
    "file": "pertemuan-1-pengantar-big-data.html",
    "module": "01-pengantar-big-data",
    "title": "Fondasi & Lanskap Big Data",
    "subtitle": "Dari 5V ke arsitektur data modern: memahami masalah sebelum memilih teknologi.",
    "description": "Slide interaktif Pertemuan 1 Big Data IFR229: karakteristik 5V, keterbatasan RDBMS, evolusi arsitektur data, batch vs streaming, peran software engineer, dan estimasi kapasitas.",
    "slides": [
        cover(
            1,
            "Fondasi & Lanskap Big Data",
            "Dari 5V ke arsitektur data modern: memahami masalah sebelum memilih teknologi.",
            [("5V + 2V", "Karakteristik data"), ("3 Lapisan", "Arsitektur modern"), ("1 Rumus", "Estimasi kapasitas")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 1",
            "Setelah sesi ini, Anda mampu membedakan masalah data besar dari data biasa — dan memilih respons arsitektur yang tepat.",
            grid(
                [
                    checklist([
                        "Menjelaskan 5V + 2V dengan implikasi teknis",
                        "Menganalisis kapan RDBMS cukup dan kapan tidak",
                        "Memetakan lapisan arsitektur data modern",
                        "Menghitung estimasi kapasitas & biaya",
                        "Menentukan batch, micro-batch, atau streaming",
                        "Menyiapkan environment praktikum",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ 5V & miskonsepsi<br>2️⃣ Batas RDBMS<br>3️⃣ Arsitektur modern<br>4️⃣ Batch vs streaming<br>5️⃣ Peran engineer RPL<br>6️⃣ Lab & estimasi", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — MENDEFINISIKAN MASALAH", "Apa Itu Big Data?", "Bukan sekadar volume besar, melainkan data yang melampaui kapasitas alat dan proses konvensional."),
        content(
            "📊 Karakteristik",
            "5V + 2V yang Wajib Dikenali",
            "Setiap karakteristik menuntut keputusan rekayasa yang berbeda:",
            table(
                ["Karakteristik", "Pertanyaan", "Implikasi"],
                [
                    ["<b>Volume</b>", "Seberapa besar?", "Storage terdistribusi, kompresi, partisi"],
                    ["<b>Velocity</b>", "Seberapa cepat?", "Streaming, buffer, backpressure"],
                    ["<b>Variety</b>", "Seberapa beragam?", "Data lake, schema management"],
                    ["<b>Veracity</b>", "Seberapa tepercaya?", "Validasi, dedup, quality gate"],
                    ["<b>Value</b>", "Apa nilainya?", "Metrik bisnis, evaluasi dampak"],
                    ["<b>Variability</b>", "Apakah pola berubah?", "Desain lentur, versioning, monitoring"],
                    ["<b>Visualization</b>", "Bagaimana dikomunikasikan?", "Serving layer, dashboard, API"],
                ],
            ),
        ),
        content(
            "⚠️ Miskonsepsi",
            "Volume Bukan Satu-satunya Ukuran",
            "Arsitektur ditentukan oleh pola akses dan SLA, bukan angka volume semata:",
            grid(
                [
                    card("🏪", "Data Kecil, Cepat", "5.000 transaksi/detik tetap menantang karena <b>velocity</b> dan kebutuhan latensi.", "#dc2626"),
                    card("🗄️", "Data Besar, Jarang Diakses", "100 TB arsip mungkin cukup di object storage murah tanpa cluster komputasi besar.", "#059669"),
                    card("📈", "Data Sedang, Bertumbuh", "Rancang untuk 2–3 tahun ke depan, bukan hanya kebutuhan bulan ini.", "#0284c7"),
                    card("🔍", "Kuncinya: Pola Akses", "Query harian, retensi, puncak beban, dan toleransi keterlambatan menentukan teknologi.", "#9333ea"),
                ],
                2,
            ),
        ),
        content(
            "🏛️ Batas Relasional",
            "Mengapa RDBMS Tidak Selalu Cukup?",
            "RDBMS tetap unggul untuk transaksi; tantangan muncul pada skala dan keragaman ekstrem:",
            table(
                ["Aspek", "RDBMS", "Kebutuhan Big Data"],
                [
                    ["Skala", "Umumnya scale-up, mahal", "Scale-out banyak node commodity"],
                    ["Skema", "Ketat, butuh migrasi", "Schema-on-read / evolusi"],
                    ["Beban", "OLTP + OLAP bercampur", "Pemisahan beban & pipeline"],
                    ["Format", "Dominan terstruktur", "Teks, JSON, log, sensor"],
                    ["Biaya", "Lisensi & hardware proprietary", "Open source + object storage"],
                    ["Kegagalan", "Sering single point of failure", "Replikasi & recovery default"],
                ],
            ),
        ),
        divider("BAGIAN II — ARSITEKTUR MODERN", "Dari Warehouse ke Lakehouse", "Evolusi 50 tahun platform data dalam satu peta jalan."),
        content(
            "🕰️ Evolusi",
            "Lima Generasi Platform Data",
            "Setiap generasi menjawab keterbatasan generasi sebelumnya:",
            steps([
                ("1970 — RDBMS", "Model relasional Codd: integritas transaksi, SQL, normalisasi."),
                ("1990 — Data Warehouse", "Inmon & Kimball: gudang data terpusat untuk BI dan OLAP."),
                ("2006 — Hadoop", "GFS + MapReduce: penyimpanan & komputasi terdistribusi di hardware murah."),
                ("2009–2011 — Spark & Kafka", "Pemrosesan in-memory dan log event real-time."),
                ("2020+ — Lakehouse", "Delta Lake, Iceberg, Hudi: ACID + tata kelola di atas data lake."),
            ]),
        ),
        content(
            "🏗️ Arsitektur",
            "Enam Lapisan Platform Data",
            "Setiap lapisan punya tanggung jawab dan alat yang berbeda:",
            grid(
                [
                    card("📥", "1. Ingestion", "Batch connector, CDC, Kafka. Menarik data dari sumber tanpa membebani sistem transaksi.", "#0284c7"),
                    card("💾", "2. Storage", "Bronze → Silver → Gold. Object storage + format kolumnar + katalog.", "#059669"),
                    card("⚙️", "3. Processing", "Spark, Hive, stream processor. Transformasi, join, agregasi, ML.", "#9333ea"),
                    card("📤", "4. Serving", "Warehouse, NoSQL, cache, API, dashboard. Melayani konsumen data.", "#d97706"),
                    card("🔁", "5. Orkestrasi", "Airflow/Dagster: jadwal, dependensi, retry, backfill, alert.", "#db2777"),
                    card("🛡️", "6. Governance", "Katalog, lineage, kualitas, keamanan, privasi, biaya, observabilitas.", "#0f766e"),
                ],
                3,
            ),
        ),
        content(
            "🌊 Mode Pemrosesan",
            "Batch vs Micro-batch vs Streaming",
            "Mulai dari batch; tambahkan streaming hanya jika latensi terukur benar-benar dibutuhkan:",
            table(
                ["Aspek", "Batch", "Micro-batch", "Streaming"],
                [
                    ["Latensi", "Menit–jam", "Detik–menit", "Milidetik–detik"],
                    ["Alat", "Spark batch, Hive", "Spark Structured Streaming", "Kafka Streams, Flink"],
                    ["Kompleksitas", "Rendah", "Sedang", "Tinggi"],
                    ["Cocok untuk", "Laporan, backfill", "Dashboard near-real-time", "Fraud, alerting, IoT"],
                ],
            ),
        ),
        divider("BAGIAN III — PERAN ENGINEER & PRAKTIKUM", "Dari Konsep ke Kode", "Apa yang dikerjakan software engineer di kelas RPL?"),
        content(
            "👨‍💻 Peran RPL",
            "Big Data Bukan Hanya Milik Data Scientist",
            "Anda membangun perangkat lunak yang membuat data dapat dipercaya dan berguna:",
            grid(
                [
                    card("📜", "Kontrak Data", "Skema event, versioning, validasi di batas sistem.", "#0284c7"),
                    card("🔌", "Integrasi", "API/database → Kafka/S3 dengan retry dan idempotensi.", "#059669"),
                    card("🧪", "Pengujian", "Unit test transformasi, integration test dengan data sampel.", "#9333ea"),
                    card("📡", "Observabilitas", "Log terstruktur, metrik record gagal, alert keterlambatan.", "#d97706"),
                    card("🔐", "Keamanan", "Secret management, least privilege, masking PII.", "#dc2626"),
                    card("💰", "Biaya", "Format kompresi, partisi, ukuran cluster secara sadar.", "#0f766e"),
                ],
                3,
            ),
        ),
        content(
            "🌍 Studi Kasus",
            "Di Mana Big Data Dipakai?",
            "Pola yang sama, domain yang berbeda:",
            table(
                ["Domain", "Sumber Data", "Nilai Bisnis"],
                [
                    ["E-commerce", "Klik, keranjang, transaksi", "Rekomendasi, stok, deteksi fraud"],
                    ["Fintech", "Transaksi, login, device", "Anti-fraud, scoring kredit, AML"],
                    ["Telekomunikasi", "CDR, jaringan, sensor", "Optimasi jaringan, churn"],
                    ["Smart city", "Sensor lalu lintas, CCTV, AQI", "Manajemen lalu lintas, peringatan dini"],
                    ["Kesehatan", "Rekam medis, klaim, IoT", "Analitik populasi, efisiensi (wajib privasi)"],
                    ["Observability", "Log, metrik, trace", "Troubleshooting, keamanan, SLO"],
                ],
            ),
        ),
        content(
            "🧮 Estimasi",
            "Back-of-the-Envelope yang Wajib Dikuasai",
            "Contoh: 5 juta event/hari × 800 byte, retensi 1 tahun, replikasi 3×, Parquet 4× lebih kecil:",
            grid(
                [
                    code("""mentah/hari   = 5.000.000 x 800 B  ~= 4 GB
mentah/tahun  = 4 GB x 365        ~= 1,46 TB
Parquet (1/4) = 1,46 TB / 4       ~= 0,37 TB
replikasi 3x  = 0,37 TB x 3       ~= 1,1 TB"""),
                    card("💡", "Kesimpulan", "Storage biasanya <b>bukan</b> bottleneck utama. Yang mahal adalah <b>komputasi</b>, <b>shuffle</b>, dan <b>operasional</b>.", "#0284c7")
                    + callout("amber", "⚠️ Jangan lupa: overhead metadata, small files, pertumbuhan data, biaya egress, retensi PII, dan puncak beban."),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "Menyiapkan Environment & Dataset",
            "Semua tugas semester menggunakan environment yang sama:",
            grid(
                [
                    steps([
                        ("Verifikasi tools", "<span class='pill-code'>python --version</span> · <span class='pill-code'>java -version</span> · <span class='pill-code'>docker --version</span>"),
                        ("Buat virtualenv & instal", "<span class='pill-code'>python -m venv .venv</span> lalu <span class='pill-code'>pip install pyspark pandas pyarrow</span>."),
                        ("Buat dataset sintetis", "200.000 event JSONL: event_id, user, produk, kota, amount, timestamp."),
                        ("Eksplorasi awal", "Hitung shape, distribusi event_type, statistik amount, dan missing values."),
                    ]),
                    code("""import pandas as pd

df = pd.read_json(
    "data/bronze/events/events_2026-09-01.jsonl",
    lines=True,
)
print(df.shape)
print(df["event_type"].value_counts())
print(df.isna().sum())"""),
                ],
                2,
            ),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa data 5.000 transaksi/detik bisa disebut big data meski volumenya tidak besar?", "Karena <b>velocity</b>-nya tinggi. Sistem harus menyerap dan merespons dalam hitungan milidetik; solusinya berbeda dari batch harian."),
                ("Kapan RDBMS tetap pilihan terbaik?", "Saat data relasional, transaksi multi-tabel penting, volume masih wajar, dan tim butuh konsistensi kuat. Jangan memaksakan NoSQL tanpa alasan."),
                ("Apa risiko utama jika memilih streaming tanpa kebutuhan latensi?", "Kompleksitas operasional naik: checkpoint, exactly-once, rebalancing, monitoring lag — tanpa manfaat bisnis yang sepadan."),
            ]),
        ),
        closing(
            "Big data adalah masalah arsitektur, bukan sekadar masalah kapasitas disk.",
            [("📖 Modul 1", "Fondasi & estimasi"), ("🧪 Tugas 1", "Rancangan kapasitas"), ("➡️ Berikutnya", "Arsitektur & penyimpanan")],
            "Sebelum pertemuan berikutnya, selesaikan Tugas 1 dan pastikan environment praktikum Anda berjalan.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 2
# ---------------------------------------------------------------------------
DECK2 = {
    "num": 2,
    "slug": "arsitektur-penyimpanan",
    "file": "pertemuan-2-arsitektur-penyimpanan.html",
    "module": "02-arsitektur-terdistribusi-penyimpanan",
    "title": "Arsitektur Terdistribusi & Penyimpanan",
    "subtitle": "Replikasi, partisi, CAP, HDFS, format kolumnar, dan seni menghindari small files.",
    "description": "Slide interaktif Pertemuan 2 Big Data IFR229: replikasi dan partisi, CAP/PACELC, arsitektur HDFS, object storage, data lake vs warehouse vs lakehouse, format Parquet/Avro, dan strategi partisi.",
    "slides": [
        cover(
            2,
            "Arsitektur Terdistribusi & Penyimpanan",
            "Replikasi, partisi, CAP, HDFS, format kolumnar, dan seni menghindari small files.",
            [("CAP/PACELC", "Trade-off konsistensi"), ("HDFS", "Block & replikasi"), ("Parquet", "Format analitik")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 2",
            "Setelah sesi ini, Anda mampu merancang penyimpanan yang benar sejak awal — bukan menambal data lake yang kacau.",
            grid(
                [
                    checklist([
                        "Menjelaskan replikasi vs partisi",
                        "Memilih CP/AP berdasarkan kebutuhan bisnis",
                        "Menjelaskan peran NameNode & DataNode",
                        "Membandingkan lake, warehouse, lakehouse",
                        "Memilih format file sesuai pola akses",
                        "Merancang partisi & menghitung jumlah file",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Sistem terdistribusi<br>2️⃣ CAP & PACELC<br>3️⃣ HDFS<br>4️⃣ Object storage & lakehouse<br>5️⃣ Format file<br>6️⃣ Partisi & lab", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — SISTEM TERDISTRIBUSI", "Mengapa Satu Mesin Tidak Cukup?", "Skala horizontal mengubah kegagalan menjadi kondisi normal, bukan pengecualian."),
        content(
            "⚖️ Dua Strategi Dasar",
            "Replikasi vs Partisi",
            "Sistem nyata menggabungkan keduanya: data dipartisi, lalu setiap partisi direplikasi.",
            grid(
                [
                    card("📑", "Replikasi", "Salinan data yang sama di beberapa node. Memberi <b>ketersediaan</b> dan kecepatan baca. Tantangan: konsistensi antar salinan.", "#0284c7")
                    + card("✂️", "Partisi / Sharding", "Data dibagi berdasarkan key ke banyak node. Memberi <b>skalabilitas tulis</b> dan paralelisme. Tantangan: hot partition dan query lintas partisi.", "#059669"),
                    card("📈", "Scale-Up", "Tambah CPU/RAM/disk pada satu mesin. Sederhana, tetapi mahal dan ada batas fisik.", "#9333ea")
                    + card("🧱", "Scale-Out", "Tambah banyak mesin commodity. Hampir linear, tetapi koordinasi dan kegagalan makin kompleks.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "🌐 Teorema CAP",
            "Consistency, Availability, Partition Tolerance",
            "Saat partisi jaringan terjadi, pilih konsistensi atau ketersediaan — bukan keduanya:",
            table(
                ["Sistem", "Klasifikasi", "Perilaku Saat Partisi"],
                [
                    ["HBase, ZooKeeper", "CP", "Menolak operasi jika tidak mencapai quorum"],
                    ["MongoDB (majority)", "CP", "Menunggu mayoritas replika"],
                    ["Cassandra", "AP", "Menerima tulisan, konflik diselesaikan belakangan"],
                    ["DynamoDB", "AP (dapat diatur)", "Selalu menerima tulisan, konsistensi eventual"],
                ],
            )
            + callout("blue", "💡 <b>PACELC:</b> jika tidak ada partisi (E), pilih <b>Latency</b> atau <b>Consistency</b>. Quorum tinggi = lebih konsisten, tetapi lebih lambat."),
        ),
        divider("BAGIAN II — HDFS & OBJECT STORAGE", "Di Mana Data Disimpan?", "HDFS untuk throughput file besar; object storage untuk elastisitas dan biaya."),
        content(
            "🗄️ HDFS",
            "Arsitektur Hadoop Distributed File System",
            "NameNode menyimpan metadata; DataNode menyimpan blok data. Blok default 128 MB, replikasi 3×.",
            grid(
                [
                    card("🧠", "NameNode", "Metadata: pohon direktori, pemetaan blok → DataNode. <b>Tidak</b> menyimpan data file.", "#0284c7"),
                    card("💽", "DataNode", "Menyimpan blok dan melayani baca/tulis. Melapor via heartbeat & block report.", "#059669"),
                    card("🛟", "Standby NameNode", "Konfigurasi HA dengan JournalNodes untuk failover otomatis.", "#9333ea"),
                    card("📦", "Blok 128 MB", "Blok besar mengurangi overhead metadata; replikasi 3× memberi toleransi kegagalan.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "🔁 Alur Baca & Tulis",
            "Data Mengalir, Metadata Memandu",
            "Client selalu bertanya lokasi ke NameNode, lalu membaca/menulis langsung ke DataNode:",
            grid(
                [
                    steps([
                        ("Baca", "Client minta lokasi blok ke NameNode → NameNode kembalikan daftar DataNode terdekat → client membaca blok langsung."),
                        ("Tulis", "Client minta izin → NameNode pilih pipeline replikasi → paket data diteruskan antar DataNode → ack → blok selesai."),
                        ("Fault tolerance", "Jika satu DataNode gagal, client mencoba replika berikutnya; NameNode membuat replika baru."),
                    ]),
                    code("""hdfs dfs -mkdir -p /data/bronze/events
hdfs dfs -put events.jsonl /data/bronze/events/
hdfs dfs -ls -h /data/bronze/events
hdfs dfs -du -h /data/bronze/events
hdfs fsck /data/bronze/events -files -blocks"""),
                ],
                2,
            ),
        ),
        content(
            "🏞️ Tiga Arsitektur",
            "Data Lake vs Warehouse vs Lakehouse",
            "Pilih berdasarkan kebutuhan pengguna, bukan tren:",
            table(
                ["Aspek", "Warehouse", "Data Lake", "Lakehouse"],
                [
                    ["Data", "Terstruktur, termodel", "Semua format, mentah", "Semua format + tabel ACID"],
                    ["Skema", "Schema-on-write", "Schema-on-read", "Schema-on-read + enforcement"],
                    ["ACID", "Ya", "Umumnya tidak", "Ya (Delta/Iceberg/Hudi)"],
                    ["Pengguna", "BI, analis SQL", "Data scientist", "Keduanya"],
                    ["Risiko", "Kaku & mahal", "Data swamp", "Kompleksitas operasional"],
                ],
            ),
        ),
        divider("BAGIAN III — FORMAT & PARTISI", "Detail yang Menentukan Biaya", "Format dan layout partisi bisa menghemat 80% biaya scan — atau menghancurkan performa."),
        content(
            "📄 Format File",
            "Baris vs Kolom",
            "Query analitik hanya menyentuh beberapa kolom; format kolumnar membaca jauh lebih sedikit data:",
            table(
                ["Format", "Tipe", "Kompresi", "Schema", "Cocok Untuk"],
                [
                    ["CSV", "Baris", "Terbatas", "Tidak", "Pertukaran sederhana"],
                    ["JSON", "Baris", "Ya", "Fleksibel", "Event, API, semi-terstruktur"],
                    ["Avro", "Baris", "Ya", "Ya + registry", "Streaming, write-heavy"],
                    ["Parquet", "Kolom", "Ya", "Ya", "Analitik, data lake, Spark"],
                    ["ORC", "Kolom", "Ya", "Ya", "Hive, tabel ACID"],
                ],
            )
            + callout("green", "✅ <b>Column pruning</b> + <b>predicate pushdown</b> + <b>kompresi</b> = tiga alasan Parquet/ORC mendominasi analitik."),
        ),
        content(
            "🧩 Columnar & Evolusi Skema",
            "Mengapa Parquet Menang untuk Analitik?",
            "Nilai sejenis berdekatan → kompresi lebih baik, dan statistik min/max mempercepat filter.",
            grid(
                [
                    code("""Baris (CSV):
[id,user,city,amount] [id,user,city,amount] ...

Kolom (Parquet):
[id,id,id,...] [user,user,...]
[city,city,...] [amount,amount,...]"""),
                    card("🔄", "Schema Evolution", "Tambah kolom nullable aman. Rename/ubah tipe perlu perencanaan. Simpan schema di katalog.", "#0284c7")
                    + card("📊", "Statistik Blok", "Parquet menyimpan min/max per row group; Spark/Hive melewati blok yang tidak relevan.", "#059669"),
                ],
                2,
            ),
        ),
        content(
            "🧮 Partisi & Small Files",
            "Hitung Sebelum Menulis",
            "1 TB/hari, partisi per tanggal + event_type (10 nilai), target file 512 MB:",
            grid(
                [
                    code("""1 TB/hari / 10 tipe = 100 GB per partisi
100 GB / 512 MB      ~= 200 file per partisi
200 x 10             = 2.000 file/hari
2.000 x 365          ~= 730.000 file/tahun"""),
                    card("⚠️", "Risiko", "Terlalu banyak file membuat listing, metadata, dan task overhead membengkak.", "#dc2626")
                    + card("✅", "Mitigasi", "Partisi lebih kasar, kompaksi berkala, tabel lakehouse, dan target file 128 MB–1 GB.", "#059669"),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "JSON → Parquet Berpartisi",
            "Konversi dataset Pertemuan 1 dan bandingkan ukuran serta jumlah file:",
            grid(
                [
                    code("""from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder
    .appName("bronze-to-silver")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate())

events = spark.read.json("data/bronze/events")
events = (events
    .withColumn("event_ts", F.to_timestamp("event_ts"))
    .withColumn("event_date", F.to_date("event_ts"))
    .dropDuplicates(["event_id"]))

(events.repartition("event_date")
       .write.mode("overwrite")
       .partitionBy("event_date")
       .parquet("data/silver/events_parquet"))"""),
                    steps([
                        ("Jalankan konversi", "Perhatikan jumlah partisi dan waktu eksekusi."),
                        ("Bandingkan ukuran", "<span class='pill-code'>du -sh</span> JSON vs Parquet."),
                        ("Hitung file", "<span class='pill-code'>find ... -name '*.parquet' | wc -l</span>."),
                        ("Verifikasi schema", "Baca kembali dengan PyArrow/Spark dan cek tipe data."),
                        ("Analisis", "Berapa rasio kompresi? Apakah jumlah file wajar?"),
                    ]),
                ],
                2,
            ),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa HDFS tidak cocok untuk jutaan file 1 KB?", "Metadata NameNode membengkak dan biaya seek mendominasi; throughput jatuh. Gabungkan file atau gunakan format/tabel yang mendukung kompaksi."),
                ("Kapan memilih object storage daripada HDFS?", "Saat butuh elastisitas, durability tinggi, pemisahan storage–compute, dan data jarang diakses. HDFS unggul untuk komputasi data lokal berulang."),
                ("Apa dampak partisi berdasarkan user_id?", "Kardinalitas tinggi membuat jutaan folder/file kecil. Partisi berdasarkan tanggal atau dimensi dengan kardinalitas terkontrol."),
            ]),
        ),
        closing(
            "Penyimpanan yang baik adalah keputusan desain, bukan hasil menambah disk.",
            [("📖 Modul 2", "HDFS & format"), ("🧪 Tugas 2", "Layout 1 TB/hari"), ("➡️ Berikutnya", "MapReduce & Hive")],
            "Selesaikan Tugas 2: rancang layout penyimpanan 1 TB event per hari beserta perhitungan jumlah file.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 3
# ---------------------------------------------------------------------------
DECK3 = {
    "num": 3,
    "slug": "hadoop-mapreduce-hive",
    "file": "pertemuan-3-hadoop-mapreduce-hive.html",
    "module": "03-hadoop-mapreduce-hive",
    "title": "Hadoop: MapReduce, YARN & Hive",
    "subtitle": "Model mental split → map → shuffle → reduce yang menjadi dasar semua mesin data modern.",
    "description": "Slide interaktif Pertemuan 3 Big Data IFR229: alur MapReduce, mapper-reducer Python, combiner dan partitioner, YARN, Hive Metastore, external table, partitioning, dan data skew.",
    "slides": [
        cover(
            3,
            "Hadoop: MapReduce, YARN & Hive",
            "Model mental split → map → shuffle → reduce yang menjadi dasar semua mesin data modern.",
            [("3 Fase", "Map · Shuffle · Reduce"), ("YARN", "Resource manager"), ("HiveQL", "SQL di atas HDFS")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 3",
            "Setelah sesi ini, Anda mampu membaca job MapReduce, menulis mapper–reducer, dan mendiagnosis bottleneck-nya.",
            grid(
                [
                    checklist([
                        "Menjelaskan fase map, shuffle, reduce",
                        "Menulis mapper/reducer yang tahan input rusak",
                        "Memilih combiner & partitioner dengan tepat",
                        "Menjelaskan peran YARN",
                        "Membuat external table Hive berpartisi",
                        "Mendeteksi dan memitigasi data skew",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Model MapReduce<br>2️⃣ Streaming Python<br>3️⃣ YARN<br>4️⃣ Hive DDL<br>5️⃣ Query analitik<br>6️⃣ Skew & optimasi", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — MODEL MAPREDUCE", "Divide and Conquer", "Pecah input, proses paralel, kelompokkan berdasarkan key, lalu agregasi."),
        content(
            "⚙️ Alur Job",
            "Split → Map → Shuffle → Reduce",
            "Prinsip utama: <b>move compute to data</b>, bukan memindahkan data ke komputasi.",
            steps([
                ("Input split", "File HDFS dipecah menjadi split (default seukuran blok 128 MB)."),
                ("Map", "Setiap split diproses paralel menjadi pasangan (key, value)."),
                ("Shuffle & sort", "Semua nilai dengan key sama dikelompokkan; ini fase paling mahal."),
                ("Reduce", "Agregasi per key: sum, count, max, join, dan sebagainya."),
                ("Output", "Hasil ditulis kembali ke HDFS dengan replikasi."),
            ])
            + callout("amber", "⚠️ <b>Shuffle adalah biaya terbesar.</b> Semua optimasi pada dasarnya mengurangi data yang melewati jaringan atau menyeimbangkan beban."),
        ),
        content(
            "📋 Anatomi",
            "Di Mana Waktu Habis?",
            "Kenali bottleneck di setiap fase sebelum menambah cluster:",
            table(
                ["Fase", "Yang Terjadi", "Bottleneck Umum"],
                [
                    ["Input", "Split file", "Terlalu banyak file kecil"],
                    ["Map", "Proses per record", "Parsing JSON, komputasi mahal"],
                    ["Spill & sort", "Buffer penuh → disk", "RAM kurang, kompresi mahal"],
                    ["Shuffle", "Ambil output map", "Jaringan & disk I/O"],
                    ["Reduce", "Group by key", "Data skew"],
                    ["Output", "Tulis HDFS", "Banyak file output kecil"],
                ],
            ),
        ),
        content(
            "🧰 Tiga Alat Optimasi",
            "Combiner, Partitioner, Join",
            "Ketiganya menentukan seberapa banyak data yang bergerak di jaringan:",
            grid(
                [
                    card("🔽", "Combiner", "Mini-reducer di sisi map. Aman untuk operasi komutatif & asosiatif (sum, max), <b>tidak</b> untuk median/rata-rata langsung.", "#0284c7"),
                    card("🧭", "Partitioner", "Menentukan key ke reducer mana. Default <span class='pill-code'>hash(key) % numReducers</span>. Kustom untuk menyebar key besar.", "#059669"),
                    card("🔗", "Reduce-side Join", "Kedua dataset di-shuffle berdasarkan join key. Cocok untuk besar–besar, tetapi mahal.", "#9333ea"),
                    card("📡", "Map-side Join", "Tabel kecil dibroadcast ke semua mapper. Jauh lebih cepat, tetapi butuh memori.", "#d97706"),
                ],
                2,
            ),
        ),
        divider("BAGIAN II — STREAMING & YARN", "Menulis MapReduce Tanpa Java", "Hadoop Streaming memungkinkan mapper/reducer dalam bahasa apa pun yang membaca stdin."),
        content(
            "🐍 Mapper & Reducer",
            "Word Count dengan Python",
            "Mapper mengeluarkan (kata, 1); reducer menjumlahkan per kata:",
            grid(
                [
                    code("""#!/usr/bin/env python3
# mapper.py
import re, sys

for line in sys.stdin:
    for word in re.findall(r"[a-zA-Z]+", line.lower()):
        print(f"{word}\\t1")"""),
                    code("""#!/usr/bin/env python3
# reducer.py
import sys

current, total = None, 0
for line in sys.stdin:
    word, count = line.rstrip().split("\\t", 1)
    count = int(count)
    if word == current:
        total += count
    else:
        if current is not None:
            print(f"{current}\\t{total}")
        current, total = word, count

if current is not None:
    print(f"{current}\\t{total}")"""),
                ],
                2,
            ),
        ),
        content(
            "🚀 Menjalankan Job",
            "Hadoop Streaming & Diagnostik",
            "Uji lokal dulu, baru kirim ke cluster. Perhatikan counter shuffle:",
            code("""# Uji lokal tanpa cluster
cat data/bronze/events/*.jsonl | ./mapper.py | sort | ./reducer.py | head

# Jalankan di Hadoop
hadoop jar "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar" \\
  -files mapper.py,reducer.py \\
  -mapper "python3 mapper.py" \\
  -reducer "python3 reducer.py" \\
  -combiner "python3 reducer.py" \\
  -input /data/input \\
  -output /data/output/wordcount""")
            + callout("blue", "💡 Cek <b>Reduce shuffle bytes</b>, <b>Spilled Records</b>, dan waktu task per reducer. Jika satu reducer jauh lebih lambat, curigai skew."),
        ),
        content(
            "🧱 YARN",
            "Manajemen Sumber Daya Cluster",
            "YARN memisahkan manajemen resource dari model pemrograman:",
            grid(
                [
                    card("🎛️", "ResourceManager", "Scheduler global: mengalokasikan resource dan menjadwalkan aplikasi.", "#0284c7"),
                    card("🖥️", "NodeManager", "Agen per node: memantau container dan melaporkan kapasitas.", "#059669"),
                    card("🧑‍💼", "ApplicationMaster", "Mengelola satu aplikasi: meminta container, memantau task.", "#9333ea"),
                    card("📦", "Container", "Alokasi CPU + RAM tempat task berjalan.", "#d97706"),
                ],
                2,
            )
            + callout("amber", "⚠️ Jika container meminta RAM melebihi kapasitas node, aplikasi berhenti di status ACCEPTED. Cocokkan <span class='pill-code'>executor.memory + overhead</span> dengan kapasitas node."),
        ),
        divider("BAGIAN III — HIVE", "SQL di Atas Hadoop", "Skema dan query SQL di atas file HDFS — tanpa memindahkan data ke database proprietary."),
        content(
            "🗂️ Hive",
            "External Table & Partisi",
            "Gunakan external table agar DROP TABLE tidak menghapus data lake:",
            code("""CREATE EXTERNAL TABLE analytics.events (
  event_id   STRING,
  user_id    STRING,
  event_type STRING,
  product_id STRING,
  city       STRING,
  amount     DOUBLE,
  event_ts   TIMESTAMP
)
PARTITIONED BY (dt DATE)
STORED AS PARQUET
LOCATION '/data/silver/events';

MSCK REPAIR TABLE analytics.events;""")
            + callout("green", "✅ <b>Partition pruning:</b> query dengan filter <span class='pill-code'>dt</span> hanya membaca folder yang relevan. Ini penghematan terbesar di Hive."),
        ),
        content(
            "📊 Query Analitik",
            "Funnel & Agregasi",
            "SQL yang sama dapat dijalankan di Hive, Spark SQL, atau Trino:",
            code("""SELECT dt,
       event_type,
       COUNT(*)                AS total_event,
       COUNT(DISTINCT user_id) AS unique_users
FROM analytics.events
WHERE dt BETWEEN DATE '2026-09-01' AND DATE '2026-09-07'
GROUP BY dt, event_type
ORDER BY dt, total_event DESC;

SELECT
  COUNT(DISTINCT CASE WHEN event_type='view'        THEN user_id END) AS viewers,
  COUNT(DISTINCT CASE WHEN event_type='add_to_cart' THEN user_id END) AS cart_users,
  COUNT(DISTINCT CASE WHEN event_type='payment'     THEN user_id END) AS payers
FROM analytics.events
WHERE dt = DATE '2026-09-01';"""),
        ),
        content(
            "⚡ Optimasi & Skew",
            "Saat 99% Job Macet di Reduce",
            "Satu key besar membuat satu reducer bekerja jauh lebih lama:",
            grid(
                [
                    card("🔍", "Gejala", "Satu task reduce berjalan sangat lama; stage tertahan di 99%. Cek distribusi key dengan <span class='pill-code'>GROUP BY key ORDER BY count DESC</span>.", "#dc2626"),
                    card("🧂", "Salting", "Tambahkan suffix acak pada key besar (<span class='pill-code'>Jakarta-0..9</span>), agregasi dua tahap, lalu gabungkan hasil.", "#059669"),
                    card("📡", "Broadcast Join", "Untuk tabel kecil, kirim ke semua mapper sehingga tidak ada shuffle tabel besar.", "#0284c7"),
                    card("⚙️", "Konfigurasi", "Aktifkan <span class='pill-code'>hive.optimize.skewjoin</span>, gunakan Tez/Spark, dan hindari <span class='pill-code'>SELECT *</span>.", "#9333ea"),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "Word Count & Log Analytics",
            "Tiga langkah yang harus terbukti di laporan:",
            steps([
                ("Word count lokal", "Uji mapper/reducer dengan <span class='pill-code'>cat | mapper | sort | reducer</span>."),
                ("Word count cluster", "Jalankan Hadoop Streaming dan catat jumlah map/reduce task."),
                ("Hive analytics", "Buat external table berpartisi, jalankan funnel, error rate, dan revenue per kota."),
                ("Analisis performa", "Bandingkan waktu sebelum/sesudah filter partisi dan penggunaan combiner."),
                ("Dokumentasi", "Sertakan perintah, counter, dan penjelasan bottleneck."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa combiner tidak boleh digunakan untuk menghitung median?", "Combiner hanya aman untuk operasi komutatif dan asosiatif. Median tidak dapat dihitung dari median sebagian data; diperlukan seluruh nilai."),
                ("Apa perbedaan NameNode dan ResourceManager?", "NameNode mengelola metadata HDFS (lokasi blok). ResourceManager mengelola resource cluster (CPU/RAM) untuk aplikasi YARN."),
                ("Mengapa external table lebih aman untuk data lake?", "DROP TABLE hanya menghapus metadata, bukan file data. Ini mencegah kehilangan data mentah secara tidak sengaja."),
            ]),
        ),
        closing(
            "MapReduce mengajarkan pola pikir yang tetap relevan: pecah, proses paralel, kelompokkan, agregasi.",
            [("📖 Modul 3", "MapReduce & Hive"), ("🧪 Tugas 3", "Analitik log"), ("➡️ Berikutnya", "Apache Spark")],
            "Selesaikan Tugas 3 dan catat satu bottleneck nyata dari job yang Anda jalankan.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 4
# ---------------------------------------------------------------------------
DECK4 = {
    "num": 4,
    "slug": "apache-spark",
    "file": "pertemuan-4-apache-spark.html",
    "module": "04-apache-spark",
    "title": "Apache Spark & Optimasi ETL",
    "subtitle": "Satu mesin untuk batch, SQL, streaming, dan ML — dengan biaya shuffle yang harus dikendalikan.",
    "description": "Slide interaktif Pertemuan 4 Big Data IFR229: arsitektur Spark, RDD vs DataFrame, lazy evaluation, Catalyst/AQE, pipeline PySpark, broadcast join, partisi, cache, skew, small files, dan unit test.",
    "slides": [
        cover(
            4,
            "Apache Spark & Optimasi ETL",
            "Satu mesin untuk batch, SQL, streaming, dan ML — dengan biaya shuffle yang harus dikendalikan.",
            [("DAG", "Lazy evaluation"), ("DataFrame", "Catalyst optimizer"), ("AQE", "Adaptive tuning")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 4",
            "Setelah sesi ini, Anda mampu membangun pipeline PySpark yang benar, efisien, dan dapat diuji.",
            grid(
                [
                    checklist([
                        "Menjelaskan driver, executor, job, stage, task",
                        "Membedakan transformasi sempit & lebar",
                        "Membangun pipeline bronze → silver → gold",
                        "Memilih repartition vs coalesce",
                        "Melakukan broadcast join & mengukur dampaknya",
                        "Menulis unit test untuk transformasi",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Mengapa Spark<br>2️⃣ Arsitektur & DAG<br>3️⃣ DataFrame ETL<br>4️⃣ SQL & window<br>5️⃣ Tuning<br>6️⃣ Testing & lab", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — MENGAPA SPARK?", "Dari Disk ke Memori", "MapReduce menulis antar-fase ke HDFS; Spark menjaga data di memori dan mengoptimasi seluruh DAG."),
        content(
            "⚖️ MapReduce vs Spark",
            "Apa yang Berubah?",
            "Spark bukan sekadar versi cepat MapReduce; ia mengubah cara job direncanakan dan dieksekusi:",
            table(
                ["Aspek", "MapReduce", "Spark"],
                [
                    ["Antar-fase", "Tulis ke HDFS", "In-memory / pipelining"],
                    ["Optimasi", "Terbatas, per job", "Catalyst + Tungsten + AQE"],
                    ["API", "Low-level map/reduce", "DataFrame, SQL, streaming, ML"],
                    ["Iterasi ML", "Mahal (disk I/O)", "Jauh lebih efisien"],
                    ["Interaktif", "Tidak", "Ya (notebook/shell)"],
                ],
            ),
        ),
        content(
            "🏗️ Arsitektur",
            "Driver, Executor, dan Cluster Manager",
            "Driver menyusun rencana; executor menjalankan task secara paralel:",
            grid(
                [
                    card("🧠", "Driver", "Menjalankan main(), membuat SparkSession, menyusun DAG, menjadwalkan task, mengumpulkan hasil.", "#0284c7"),
                    card("⚙️", "Executor", "Proses JVM di worker: menjalankan task, menyimpan cache, melaporkan status.", "#059669"),
                    card("🎛️", "Cluster Manager", "Mengalokasikan resource: YARN, Kubernetes, atau Standalone.", "#9333ea"),
                    card("📦", "Partisi & Task", "Satu task per partisi per stage; jumlah partisi menentukan paralelisme.", "#d97706"),
                ],
                2,
            )
            + callout("blue", "💡 <b>Job</b> dipicu satu aksi. <b>Stage</b> dipisahkan oleh shuffle. <b>Task</b> adalah unit kerja terkecil."),
        ),
        content(
            "⚡ Lazy & DAG",
            "Tidak Ada Eksekusi Sampai Ada Aksi",
            "Spark membangun rencana logis, lalu optimizer memilih strategi terbaik:",
            grid(
                [
                    code("""df = spark.read.parquet("...")      # lazy
clean = df.filter(F.col("amount") > 0) # lazy
agg = clean.groupBy("city").count()    # lazy
agg.show()                             # aksi -> eksekusi"""),
                    card("🧩", "Sempit (narrow)", "map, filter, select: satu partisi input → satu partisi output. Tanpa jaringan.", "#059669")
                    + card("🌐", "Lebar (wide)", "groupBy, join, distinct: butuh shuffle. Di sinilah waktu dan biaya habis.", "#dc2626"),
                ],
                2,
            ),
        ),
        divider("BAGIAN II — DATAFRAME & ETL", "Dari JSON Mentah ke Tabel Gold", "Tulis transformasi sebagai fungsi murni agar bisa diuji dan dipakai ulang."),
        content(
            "🧹 Bronze → Silver",
            "Membersihkan & Memvalidasi",
            "Empat aturan kualitas dasar: id tidak null, timestamp valid, amount non-negatif, event unik:",
            code("""from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder
    .appName("events-etl")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "8")
    .config("spark.sql.adaptive.enabled", "true")
    .getOrCreate())

raw = spark.read.json("data/bronze/events")

silver = (raw
    .withColumn("event_ts", F.to_timestamp("event_ts"))
    .withColumn("dt", F.to_date("event_ts"))
    .withColumn("amount", F.col("amount").cast("double"))
    .filter(F.col("event_id").isNotNull())
    .filter(F.col("event_ts").isNotNull())
    .filter(F.col("amount") >= 0)
    .dropDuplicates(["event_id"]))

(silver.write.mode("overwrite")
       .partitionBy("dt")
       .parquet("data/silver/events"))"""),
        ),
        content(
            "🥇 Silver → Gold",
            "Join, Agregasi, dan Metrik Bisnis",
            "Broadcast tabel kecil, lalu hasilkan agregat harian per kota:",
            code("""events = spark.read.parquet("data/silver/events")
products = spark.read.parquet("data/reference/products")  # kecil

enriched = events.join(F.broadcast(products), "product_id", "left")

daily_city = (enriched
    .groupBy("dt", "city")
    .agg(
        F.count("*").alias("total_events"),
        F.countDistinct("user_id").alias("unique_users"),
        F.sum(F.when(F.col("event_type") == "payment", F.col("amount"))
               .otherwise(0)).alias("revenue"),
    )
    .withColumn("conversion_rate",
        F.round(F.col("revenue") / F.col("unique_users"), 2)))

(daily_city.write.mode("overwrite")
           .partitionBy("dt")
           .parquet("data/gold/daily_city"))"""),
        ),
        content(
            "🔍 SQL & Window",
            "Deklaratif, Terbaca, Teroptimasi",
            "Gunakan SQL untuk agregasi; window function untuk analisis sesi dan funnel:",
            grid(
                [
                    code("""spark.sql('''
  SELECT dt, event_type,
         COUNT(*) AS total,
         COUNT(DISTINCT user_id) AS users
  FROM events
  WHERE dt >= DATE '2026-09-01'
  GROUP BY dt, event_type
  ORDER BY dt, total DESC
''').show(20)"""),
                    code("""from pyspark.sql import Window

w = Window.partitionBy("user_id").orderBy("event_ts")

funnel = (events
  .withColumn("prev_event", F.lag("event_type").over(w))
  .withColumn("prev_ts", F.lag("event_ts").over(w))
  .withColumn("seconds_since_prev",
      F.unix_timestamp("event_ts") - F.unix_timestamp("prev_ts")))"""),
                ],
                2,
            ),
        ),
        divider("BAGIAN III — TUNING", "Mengendalikan Shuffle", "Optimasi bukan menambah node; optimasi adalah mengurangi data yang bergerak."),
        content(
            "📊 Partisi & Shuffle",
            "Angka yang Wajib Diperhatikan",
            "Target ukuran partisi: 100–200 MB di memori. Default shuffle partition 200 sering terlalu banyak untuk data kecil:",
            table(
                ["Operasi", "Efek", "Kapan Dipakai"],
                [
                    ["<span class='pill-code'>repartition(n)</span>", "Shuffle penuh, seimbang", "Menambah paralelisme"],
                    ["<span class='pill-code'>repartition(n, col)</span>", "Shuffle by key", "Sebelum join/tulis"],
                    ["<span class='pill-code'>coalesce(n)</span>", "Gabung tanpa shuffle penuh", "Kurangi file sebelum write"],
                    ["<span class='pill-code'>broadcast(df)</span>", "Kirim tabel kecil ke executor", "Join tabel < 10 MB"],
                    ["<span class='pill-code'>cache()</span>", "Simpan di memori", "DataFrame dipakai berulang"],
                ],
            ),
        ),
        content(
            "🚀 Enam Pengungkit Performa",
            "Dari Broadcast sampai Small Files",
            "Urutkan dari yang paling sering memberi dampak:",
            grid(
                [
                    card("📡", "Broadcast Join", "Hindari shuffle tabel besar. Naikkan threshold hati-hati; tabel terlalu besar menyebabkan driver OOM.", "#0284c7"),
                    card("🧮", "AQE", "Coalesce partisi kecil, ubah join strategy, tangani skew otomatis. Aktif sejak Spark 3.2.", "#059669"),
                    card("💾", "Cache Bijak", "Cache hanya DataFrame yang dipakai berulang; selalu <span class='pill-code'>unpersist()</span>.", "#9333ea"),
                    card("🐍", "Hindari Python UDF", "Gunakan fungsi bawaan Catalyst; jika terpaksa, pakai pandas UDF berbasis Arrow.", "#d97706"),
                    card("🧂", "Skew", "Salting key besar, broadcast tabel kecil, atau pisahkan outlier.", "#dc2626"),
                    card("📦", "Small Files", "<span class='pill-code'>coalesce</span> atau <span class='pill-code'>maxRecordsPerFile</span>; target 128 MB–1 GB per file.", "#0f766e"),
                ],
                3,
            ),
        ),
        content(
            "🧪 Menguji Job",
            "Transformasi sebagai Fungsi Murni",
            "Pisahkan logika dari I/O agar dapat diuji dengan Spark lokal:",
            grid(
                [
                    code("""# jobs/transforms.py
from pyspark.sql import DataFrame, functions as F

def clean_events(df: DataFrame) -> DataFrame:
    return (df
      .withColumn("event_ts", F.to_timestamp("event_ts"))
      .withColumn("dt", F.to_date("event_ts"))
      .filter(F.col("event_id").isNotNull())
      .filter(F.col("amount") >= 0)
      .dropDuplicates(["event_id"]))"""),
                    code("""# tests/test_transforms.py
def test_clean_events(spark):
    data = [
      ("e1", 10.0, "2026-09-01T10:00:00"),
      ("e1", 10.0, "2026-09-01T10:00:00"),
      ("e2", -5.0, "2026-09-01T11:00:00"),
    ]
    df = spark.createDataFrame(
        data, ["event_id", "amount", "event_ts"])
    result = clean_events(df).collect()
    assert len(result) == 1"""),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "Pipeline & Eksperimen Tuning",
            "Buktikan dampak tuning dengan metrik, bukan opini:",
            steps([
                ("Bangun pipeline", "Bronze → silver → gold dengan minimal 4 aturan kualitas."),
                ("Tulis 3 unit test", "Gunakan Spark lokal dan data sampel kecil."),
                ("Eksperimen 1", "Shuffle partitions 200 vs 8: catat waktu dan jumlah task."),
                ("Eksperimen 2", "Join biasa vs broadcast: catat waktu dan shuffle bytes."),
                ("Eksperimen 3", "Tanpa vs dengan coalesce sebelum write: catat jumlah file."),
                ("Laporan", "Tabel percobaan + analisis mengapa terjadi perbedaan."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa lazy evaluation menguntungkan?", "Spark dapat mengoptimasi seluruh rencana sebelum eksekusi: predicate pushdown, column pruning, pemilihan join, dan penggabungan stage."),
                ("Kapan memilih coalesce daripada repartition?", "Saat hanya ingin mengurangi jumlah partisi/file sebelum write dan tidak butuh distribusi ulang yang seimbang. Coalesce menghindari shuffle penuh."),
                ("Apa gejala data skew di Spark?", "Beberapa task berjalan jauh lebih lama, stage tertahan di 99%, dan satu partisi jauh lebih besar. Cek distribusi key dan aktifkan AQE skew join."),
            ]),
        ),
        closing(
            "Spark memberi Anda kecepatan — tetapi disiplin partisi dan shuffle yang menentukan biayanya.",
            [("📖 Modul 4", "Spark & ETL"), ("🧪 Tugas 4", "Pipeline + tuning"), ("➡️ Berikutnya", "NoSQL & Kafka")],
            "Selesaikan Tugas 4 dan sertakan minimal dua eksperimen tuning dengan bukti metrik.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 5
# ---------------------------------------------------------------------------
DECK5 = {
    "num": 5,
    "slug": "nosql-kafka",
    "file": "pertemuan-5-nosql-kafka.html",
    "module": "05-nosql-kafka-streaming",
    "title": "NoSQL, Kafka & Event Streaming",
    "subtitle": "Memilih model data berdasarkan pola akses, lalu mengalirkan event dengan idempoten.",
    "description": "Slide interaktif Pertemuan 5 Big Data IFR229: taksonomi NoSQL, ACID vs BASE, MongoDB, Cassandra query-first, Kafka topics/partitions/offset, delivery semantics, outbox/CDC, dan idempotensi.",
    "slides": [
        cover(
            5,
            "NoSQL, Kafka & Event Streaming",
            "Memilih model data berdasarkan pola akses, lalu mengalirkan event dengan idempoten.",
            [("4 Tipe", "NoSQL"), ("3 Partisi", "Kafka paralelisme"), ("2 Pola", "Outbox & CDC")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 5",
            "Setelah sesi ini, Anda mampu memilih NoSQL dengan alasan dan membangun stream yang tahan duplikasi.",
            grid(
                [
                    checklist([
                        "Memilih jenis NoSQL berdasarkan pola akses",
                        "Merancang dokumen MongoDB (embed vs reference)",
                        "Merancang tabel Cassandra dari query",
                        "Menjelaskan topic, partition, offset, consumer group",
                        "Membedakan at-most/at-least/exactly-once",
                        "Membuat consumer idempoten & memantau lag",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Taksonomi NoSQL<br>2️⃣ MongoDB<br>3️⃣ Cassandra<br>4️⃣ Kafka<br>5️⃣ Delivery semantics<br>6️⃣ Outbox, CDC & lab", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — NOSQL", "Memilih Model Data", "NoSQL mengoptimalkan pola akses tertentu; ia bukan pengganti otomatis RDBMS."),
        content(
            "🗂️ Taksonomi",
            "Empat Keluarga NoSQL",
            "Pilih berdasarkan bentuk data dan cara Anda mengaksesnya:",
            grid(
                [
                    card("🔑", "Key-Value", "Redis, DynamoDB. Cache, session, counter, leaderboard. Akses hanya lewat key.", "#0284c7"),
                    card("📄", "Document", "MongoDB, CouchDB. Katalog, profil, konten. Dokumen JSON bersarang.", "#059669"),
                    card("📊", "Column-Family", "Cassandra, HBase. Time-series, event log, IoT. Partisi + clustering.", "#9333ea"),
                    card("🕸️", "Graph", "Neo4j. Jejaring sosial, rekomendasi, fraud ring. Node + edge + properti.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "⚖️ ACID vs BASE",
            "Konsistensi Bukan Hitam-Putih",
            "Banyak NoSQL modern mendukung transaksi; pahami jaminan aktual produknya:",
            table(
                ["ACID (RDBMS)", "BASE (banyak NoSQL)"],
                [
                    ["<b>Atomicity</b> — semua atau tidak sama sekali", "<b>Basically Available</b> — selalu merespons"],
                    ["<b>Consistency</b> — aturan integritas selalu benar", "<b>Soft state</b> — state dapat berubah"],
                    ["<b>Isolation</b> — transaksi tidak saling mengganggu", "<b>Eventual consistency</b> — konvergen akhirnya"],
                    ["<b>Durability</b> — data tersimpan permanen", "Tuning quorum menentukan konsistensi aktual"],
                ],
            ),
        ),
        content(
            "📄 MongoDB",
            "Rancang dari Query, Bukan dari Entitas",
            "Embed jika selalu dibaca bersama; reference jika data mandiri dan sering berubah:",
            grid(
                [
                    code("""{
  "_id": "ord-20260901-0001",
  "customer_id": "cust-001",
  "status": "paid",
  "items": [
    {"product_id": "prd-123",
     "price": 350000, "qty": 1}
  ],
  "total": 350000
}"""),
                    card("📌", "Embed", "Data selalu dibaca bersama, ukuran terbatas, jarang berubah. Contoh: item di dalam order.", "#0284c7")
                    + card("🔗", "Reference", "Data mandiri, sering berubah, many-to-many. Butuh query tambahan atau <span class='pill-code'>$lookup</span>.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "📊 Cassandra",
            "Query-First Data Modeling",
            "Satu tabel untuk satu query. Duplikasi normal; join tidak tersedia:",
            grid(
                [
                    code("""CREATE TABLE events_by_user (
  user_id    text,
  event_date date,
  event_ts   timestamp,
  event_type text,
  payload    text,
  PRIMARY KEY ((user_id), event_date, event_ts)
) WITH CLUSTERING ORDER BY
  (event_date DESC, event_ts DESC);

SELECT * FROM events_by_user
WHERE user_id = ? LIMIT 50;"""),
                    card("🧩", "Partition Key", "Menentukan node & distribusi. Pilih kardinalitas tinggi dan merata.", "#0284c7")
                    + card("📑", "Clustering", "Menentukan urutan dalam partisi; memungkinkan query rentang.", "#059669")
                    + callout("red", "❌ Hindari <span class='pill-code'>ALLOW FILTERING</span>: memindai banyak partisi dan tidak scalable. Buat tabel baru sesuai query."),
                ],
                2,
            ),
        ),
        divider("BAGIAN II — KAFKA", "Log Event Terdistribusi", "Bukan sekadar queue: event disimpan, dapat diputar ulang, dan dibaca banyak konsumen."),
        content(
            "🌊 Konsep Kafka",
            "Topic, Partition, Offset, Consumer Group",
            "Partition adalah unit paralelisme; urutan hanya dijamin di dalam satu partisi:",
            grid(
                [
                    card("📚", "Topic", "Kategori stream, seperti tabel pada database.", "#0284c7"),
                    card("🧩", "Partition", "Unit paralelisme & urutan. Gunakan key stabil agar event terkait satu partisi.", "#059669"),
                    card("🔢", "Offset", "Posisi record dalam partisi, dikelola per consumer group.", "#9333ea"),
                    card("👥", "Consumer Group", "Berbagi beban; satu partisi hanya untuk satu konsumen per group.", "#d97706"),
                ],
                2,
            )
            + callout("blue", "💡 Jumlah konsumen aktif tidak melebihi jumlah partisi. Kelebihan konsumen akan idle."),
        ),
        content(
            "💻 Producer & Consumer",
            "Idempoten Sejak Awal",
            "Aktifkan idempotence, commit manual setelah proses, dan gunakan upsert:",
            grid(
                [
                    code("""producer = KafkaProducer(
  bootstrap_servers="localhost:9092",
  acks="all",
  enable_idempotence=True,
  retries=5,
  key_serializer=lambda k: k.encode(),
  value_serializer=lambda v: json.dumps(v).encode(),
)
producer.send("orders.events",
              key=order_id, value=event)"""),
                    code("""consumer = KafkaConsumer(
  "orders.events",
  bootstrap_servers="localhost:9092",
  group_id="order-enricher",
  enable_auto_commit=False,
  value_deserializer=lambda b: json.loads(b.decode()),
)
for msg in consumer:
    process(msg.value)   # harus idempoten
    consumer.commit()"""),
                ],
                2,
            ),
        ),
        content(
            "📬 Delivery Semantics",
            "Pilih Tingkat Jaminan yang Realistis",
            "At-least-once + idempoten adalah pilihan paling pragmatis untuk sebagian besar sistem:",
            table(
                ["Mode", "Cara", "Risiko"],
                [
                    ["At most once", "Commit sebelum proses", "Kehilangan data jika crash"],
                    ["At least once", "Commit setelah proses", "Duplikasi jika crash sebelum commit"],
                    ["Exactly once", "Transaksi/idempoten end-to-end", "Paling kompleks, butuh dukungan sink"],
                ],
            )
            + callout("green", "✅ Kunci idempotensi: <span class='pill-code'>update_one(filter, {$setOnInsert: ...}, upsert=True)</span> atau simpan idempotency key."),
        ),
        divider("BAGIAN III — POLA INTEGRASI", "Menjaga Data Tetap Konsisten", "Dual-write adalah sumber inkonsistensi; outbox dan CDC menyelesaikannya."),
        content(
            "📤 Outbox & CDC",
            "Satu Transaksi, Satu Kebenaran",
            "Aplikasi menulis data bisnis dan event ke tabel outbox dalam transaksi yang sama:",
            steps([
                ("BEGIN", "Aplikasi membuka transaksi database."),
                ("Tulis data bisnis", "INSERT/UPDATE ke tabel order."),
                ("Tulis outbox", "INSERT event ke tabel outbox dalam transaksi yang sama."),
                ("COMMIT", "Keduanya sukses atau keduanya gagal."),
                ("CDC", "Debezium membaca WAL/binlog dan mempublikasikan event ke Kafka."),
                ("Consume", "Konsumen memproses event secara idempoten."),
            ])
            + callout("green", "✅ Tidak ada dual-write. Tidak ada event hilang atau data bisnis tanpa event."),
        ),
        content(
            "🛡️ Schema & Backpressure",
            "Agar Stream Tidak Pecah",
            "Perubahan skema dan lonjakan beban adalah dua penyebab insiden paling umum:",
            grid(
                [
                    card("📜", "Schema Registry", "Avro/Protobuf + kompatibilitas backward/forward/full. Deteksi perubahan sebelum merusak konsumen.", "#0284c7"),
                    card("📉", "Consumer Lag", "Pantau <span class='pill-code'>kafka-consumer-groups --describe</span>. Tambah konsumen sampai batas partisi.", "#059669"),
                    card("💀", "Dead Letter Queue", "Pesan gagal permanen dipindahkan agar tidak memblokir stream.", "#dc2626"),
                    card("🚦", "Backpressure", "Pause/resume, perbesar batch, atau scale out. Jangan biarkan lag menumpuk diam-diam.", "#d97706"),
                ],
                2,
            ),
        ),
        content(
            "💻 Praktikum",
            "Streaming Idempoten + MongoDB",
            "Buktikan sistem tetap benar saat event dikirim dua kali:",
            steps([
                ("Jalankan Kafka", "<span class='pill-code'>docker compose up -d</span> dan buat topic 3 partisi."),
                ("Producer", "Kirim 1.000 event dengan key <span class='pill-code'>order_id</span>."),
                ("Consumer", "Validasi, lalu tulis ke MongoDB dengan upsert."),
                ("Simulasi duplikasi", "Kirim ulang 100 event; pastikan hasil akhir tidak berubah."),
                ("DLQ", "Kirim pesan rusak ke <span class='pill-code'>orders.dlq</span>."),
                ("Metrik", "Catat diproses, duplikat, gagal, dan lag akhir."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa ordering Kafka hanya dijamin per partisi?", "Kafka mendistribusikan partisi ke banyak broker/konsumen. Urutan global akan memaksa satu titik serialisasi dan menghilangkan paralelisme."),
                ("Apa masalah dual-write?", "Menulis database dan mengirim event secara terpisah dapat menghasilkan salah satu sukses dan yang lain gagal, sehingga data dan event tidak konsisten."),
                ("Kapan memilih Cassandra daripada MongoDB?", "Saat butuh throughput tulis sangat tinggi, distribusi multi-datacenter, dan pola query sudah pasti per partisi. MongoDB lebih fleksibel untuk dokumen dan agregasi."),
            ]),
        ),
        closing(
            "NoSQL mengikuti pola akses; Kafka mengikuti aliran peristiwa. Keduanya menuntut desain, bukan konfigurasi default.",
            [("📖 Modul 5", "NoSQL & Kafka"), ("🧪 Tugas 5", "Streaming idempoten"), ("➡️ Berikutnya", "Pipeline & Airflow")],
            "Selesaikan Tugas 5 dan tunjukkan bukti bahwa pengiriman ganda tidak menggandakan data.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 6
# ---------------------------------------------------------------------------
DECK6 = {
    "num": 6,
    "slug": "pipeline-airflow",
    "file": "pertemuan-6-pipeline-airflow.html",
    "module": "06-pipeline-orkestrasi-kualitas",
    "title": "Pipeline, Orkestrasi & Kualitas Data",
    "subtitle": "Pipeline adalah produk: idempoten, terjadwal, teruji, terpantau, dan punya quality gate.",
    "description": "Slide interaktif Pertemuan 6 Big Data IFR229: ETL vs ELT, idempotensi, write-audit-publish, Airflow DAG, retry/backfill, kualitas data, observabilitas, dan CI/CD pipeline data.",
    "slides": [
        cover(
            6,
            "Pipeline, Orkestrasi & Kualitas Data",
            "Pipeline adalah produk: idempoten, terjadwal, teruji, terpantau, dan punya quality gate.",
            [("DAG", "Airflow"), ("5 Dimensi", "Kualitas data"), ("1 Gate", "Blokir data buruk")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 6",
            "Setelah sesi ini, Anda mampu mengubah skrip menjadi pipeline yang aman di-retry dan di-backfill.",
            grid(
                [
                    checklist([
                        "Membedakan ETL dan ELT",
                        "Merancang pipeline idempoten",
                        "Membuat DAG Airflow dengan retry & timeout",
                        "Menerapkan quality gate",
                        "Merancang observabilitas pipeline",
                        "Menyiapkan CI untuk pipeline data",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Pipeline sebagai produk<br>2️⃣ Idempotensi<br>3️⃣ Airflow<br>4️⃣ Kualitas data<br>5️⃣ Observabilitas<br>6️⃣ CI/CD & milestone", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — PIPELINE SEBAGAI PRODUK", "Lebih dari Sekadar Skrip", "Pipeline punya pemilik, kontrak, versi, test, SLA, dan biaya."),
        content(
            "🔁 ETL vs ELT",
            "Di Mana Transformasi Dilakukan?",
            "Cloud warehouse membuat ELT makin populer, tetapi ETL tetap relevan untuk data sensitif:",
            table(
                ["Aspek", "ETL", "ELT"],
                [
                    ["Urutan", "Transform sebelum load", "Load mentah, transform di warehouse"],
                    ["Cocok untuk", "Data sensitif, transformasi kompleks", "Cloud warehouse/lakehouse elastis"],
                    ["Contoh", "Sqoop → transform → warehouse", "Airbyte → dbt → warehouse"],
                    ["Kontrol", "Lebih ketat di luar DB", "Memanfaatkan kekuatan SQL warehouse"],
                ],
            ),
        ),
        content(
            "🛡️ Idempotensi",
            "Dijalankan Dua Kali, Hasilnya Sama",
            "Ini properti wajib, bukan nice-to-have:",
            grid(
                [
                    card("📦", "Partition Overwrite", "Tulis ulang seluruh partisi tanggal. Cara paling sederhana dan aman untuk batch harian.", "#0284c7"),
                    card("🔀", "MERGE / UPSERT", "Update berdasarkan primary key. Cocok untuk data yang berubah (CDC).", "#059669"),
                    card("🧹", "Dedup by event_id", "Simpan hanya versi terbaru; buang duplikat sebelum publish.", "#9333ea"),
                    card("🚧", "Write-Audit-Publish", "Tulis ke staging → audit kualitas → tukar ke tabel produksi.", "#d97706"),
                ],
                2,
            )
            + callout("red", "❌ <span class='pill-code'>mode('append')</span> tanpa deduplikasi adalah penyebab paling umum data ganda."),
        ),
        content(
            "🔁 Retry & Backfill",
            "Tanggal Logis, Bukan Tanggal Sekarang",
            "Backfill hanya benar jika pipeline menerima parameter tanggal:",
            grid(
                [
                    code("""# ❌ Salah: selalu hari ini
today = datetime.now().date()

# ✅ Benar: tanggal logis scheduler
def run(ds: str):
    process(date.fromisoformat(ds))"""),
                    card("⏱️", "Retry", "Untuk kegagalan sementara: jaringan, rate limit. Gunakan exponential backoff.", "#0284c7")
                    + card("📅", "Backfill", "Proses ulang tanggal historis setelah bug diperbaiki — tanpa menimpa data hari ini.", "#059669")
                    + callout("amber", "⚠️ Data terlambat? Proses ulang jendela 3 hari terakhir atau gunakan watermark."),
                ],
                2,
            ),
        ),
        divider("BAGIAN II — APACHE AIRFLOW", "Orkestrasi, Bukan Pemrosesan", "Airflow menjawab: apa yang jalan, kapan, dalam urutan apa, dan apa yang terjadi jika gagal."),
        content(
            "🧩 Konsep Airflow",
            "DAG, Operator, Task, XCom",
            "Pahami perbedaan komponen agar tidak menaruh logika bisnis di tempat yang salah:",
            table(
                ["Konsep", "Arti"],
                [
                    ["<b>DAG</b>", "Graf asiklik berarah: kumpulan task + dependensi"],
                    ["<b>Operator</b>", "Template task: Python, Bash, Spark, SQL, HTTP"],
                    ["<b>Task</b>", "Instance operator dalam DAG"],
                    ["<b>Scheduler</b>", "Memicu DAG sesuai jadwal & dependensi"],
                    ["<b>XCom</b>", "Pertukaran metadata kecil — <b>bukan</b> data besar"],
                    ["<b>Catchup</b>", "Menjalankan jadwal yang terlewat"],
                ],
            ),
        ),
        content(
            "🐍 DAG Produksi",
            "Extract → Transform → Quality Gate → Publish",
            "Retry, timeout, max active runs, dan quality gate yang memblokir publish:",
            code("""@dag(
    dag_id="orders_daily",
    schedule="0 2 * * *",
    start_date=datetime(2026, 9, 1),
    catchup=False,
    max_active_runs=1,
    default_args={"retries": 2,
                  "retry_delay": timedelta(minutes=5),
                  "execution_timeout": timedelta(hours=1)},
)
def orders_daily():
    extract = BashOperator(
        task_id="extract_to_bronze",
        bash_command="python jobs/extract.py --date {{ ds }}")

    transform = BashOperator(
        task_id="spark_bronze_to_gold",
        bash_command="spark-submit jobs/transform.py --date {{ ds }}")

    @task
    def quality_gate(ds: str):
        report = load_report(ds)
        if report["failed_checks"]:
            raise AirflowFailException(report["failed_checks"])

    publish = BashOperator(
        task_id="publish_gold",
        bash_command="python jobs/publish.py --date {{ ds }}")

    extract >> transform >> quality_gate() >> publish"""),
        ),
        content(
            "✅ Pola DAG yang Baik",
            "Satu Pipeline, Satu Tujuan",
            "DAG hanya orkestrasi; logika bisnis tinggal di modul yang teruji:",
            grid(
                [
                    card("🎯", "Satu DAG = satu pipeline bisnis", "Mudah dipantau, dimiliki, dan di-debug.", "#0284c7"),
                    card("🧩", "Task kecil & spesifik", "Retry tidak mengulang seluruh proses.", "#059669"),
                    card("🔁", "Idempoten", "Aman untuk retry dan backfill.", "#9333ea"),
                    card("📅", "Tanggal logis", "Konsisten saat memproses ulang data historis.", "#d97706"),
                    card("🚨", "Alert kegagalan", "Deteksi cepat sebelum pengguna melihat data basi.", "#dc2626"),
                    card("🧠", "Tanpa business logic", "DAG memanggil fungsi; fungsi diuji terpisah.", "#0f766e"),
                ],
                3,
            ),
        ),
        divider("BAGIAN III — KUALITAS & OBSERVABILITAS", "Data Buruk Harus Berhenti di Gate", "Lebih baik pipeline gagal daripada dashboard menampilkan angka salah."),
        content(
            "📏 Dimensi Kualitas",
            "Tujuh Pertanyaan yang Wajib Diuji",
            "Setiap dimensi memiliki ambang dan aksi yang berbeda:",
            table(
                ["Dimensi", "Pertanyaan", "Contoh Uji"],
                [
                    ["Completeness", "Apakah semua data ada?", "<span class='pill-code'>null_rate &lt; 1%</span>"],
                    ["Uniqueness", "Apakah ada duplikat?", "count(*) = count(distinct id)"],
                    ["Validity", "Apakah nilai sesuai domain?", "status IN ('paid','pending')"],
                    ["Consistency", "Apakah antar-tabel cocok?", "total order = sum item"],
                    ["Timeliness", "Apakah data cukup baru?", "max(ingested_at) &gt; now - 2h"],
                    ["Accuracy", "Apakah mencerminkan kenyataan?", "Rekonsiliasi dengan sumber"],
                    ["Volume", "Apakah jumlah wajar?", "±30% dari baseline 7 hari"],
                ],
            ),
        ),
        content(
            "🧪 Quality Gate",
            "Uji, Klasifikasikan, Blokir",
            "Bedakan critical (hentikan pipeline) dari warning (lanjutkan + alert):",
            grid(
                [
                    code("""def quality_report(df):
    total = df.count()
    checks = {
      "row_count_positive": total > 0,
      "event_id_not_null":
          df.filter(F.col("event_id").isNull()).count() == 0,
      "event_id_unique":
          total == df.select("event_id").distinct().count(),
      "amount_non_negative":
          df.filter(F.col("amount") < 0).count() == 0,
    }
    return {
      "total_rows": total,
      "failed_checks": [k for k, ok in checks.items() if not ok],
    }"""),
                    card("🚨", "Critical", "Data hilang, duplikat massal, skema rusak → hentikan pipeline.", "#dc2626")
                    + card("⚠️", "Warning", "Null naik sedikit, volume turun 10% → lanjutkan, kirim alert.", "#d97706")
                    + callout("green", "✅ Simpan laporan kualitas sebagai artefak agar bisa diaudit dan dibandingkan antar run."),
                ],
                2,
            ),
        ),
        content(
            "📡 Observabilitas & CI/CD",
            "Pipeline yang Tidak Terlihat Akan Ditinggalkan",
            "Pantau freshness, volume, error rate, durasi, dan biaya — lalu uji semuanya di CI:",
            grid(
                [
                    card("⏱️", "Freshness", "Waktu sejak data terakhir masuk. Alert jika &gt; 2 jam.", "#0284c7"),
                    card("📊", "Volume", "Jumlah baris per run; bandingkan dengan baseline 7 hari.", "#059669"),
                    card("🧬", "Schema Drift", "Kolom baru/hilang/tipe berubah tanpa kontrak.", "#9333ea"),
                    card("💰", "Cost", "Bytes scanned, DBU, durasi cluster per pipeline.", "#d97706"),
                    card("🔍", "Lineage", "Asal-usul tabel gold untuk audit & debugging.", "#0f766e"),
                    card("🤖", "CI", "Lint + unit test + integration test dengan data sampel.", "#dc2626"),
                ],
                3,
            ),
        ),
        content(
            "💻 Praktikum",
            "Airflow Lokal & Simulasi Kegagalan",
            "Buktikan quality gate benar-benar menghentikan publikasi:",
            steps([
                ("Jalankan Airflow", "Gunakan docker compose resmi; buka localhost:8080."),
                ("Tambahkan DAG", "Mount folder dags/ dan jobs/ ke container."),
                ("Trigger manual", "Periksa Graph View dan status setiap task."),
                ("Simulasi gagal", "Buat quality_gate selalu gagal; pastikan publish tidak berjalan."),
                ("Perbaiki", "Trigger ulang; pastikan pipeline selesai."),
                ("Diskusikan", "Mengapa retry tidak menyelesaikan masalah kualitas data?"),
            ]),
        ),
        content(
            "🏁 Milestone Proyek 1",
            "Pipeline End-to-End Pertama",
            "Bukan tugas baru — ini checkpoint proyek akhir:",
            checklist([
                "Diagram arsitektur: sumber → bronze → silver → gold → serving",
                "DAG Airflow (atau Makefile) dengan minimal 3 tahap",
                "Minimal 5 uji kualitas + quality gate",
                "README: cara menjalankan, dependency, asumsi",
                "Bukti eksekusi sukses + satu simulasi kegagalan",
                "Pembagian tugas kelompok yang jelas",
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa datetime.now() berbahaya di pipeline terjadwal?", "Saat backfill, pipeline akan memproses tanggal sekarang, bukan tanggal historis yang diminta. Gunakan tanggal logis dari scheduler."),
                ("Apa fungsi write-audit-publish?", "Menulis ke staging, mengaudit kualitas, lalu menukar ke tabel produksi hanya jika lolos. Data buruk tidak pernah terlihat pengguna."),
                ("Mengapa XCom tidak cocok untuk DataFrame besar?", "XCom disimpan di database metadata Airflow. Data besar membebani database dan memperlambat scheduler; simpan di object storage dan oper path-nya."),
            ]),
        ),
        closing(
            "Pipeline yang baik tidak hanya berjalan — ia tahu kapan harus berhenti.",
            [("📖 Modul 6", "Airflow & kualitas"), ("🏁 Milestone 1", "DAG + gate"), ("➡️ Berikutnya", "ML terdistribusi")],
            "Selesaikan Milestone 1 dan siapkan demo 10 menit untuk review kelompok.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 7
# ---------------------------------------------------------------------------
DECK7 = {
    "num": 7,
    "slug": "ml-terdistribusi",
    "file": "pertemuan-7-ml-terdistribusi.html",
    "module": "07-analitik-ml-terdistribusi",
    "title": "Analitik & Machine Learning Terdistribusi",
    "subtitle": "Dari fitur skala besar ke model yang dievaluasi jujur, dikirim, dan dipantau.",
    "description": "Slide interaktif Pertemuan 7 Big Data IFR229: analytics maturity, siklus ML, Spark MLlib, feature engineering, churn pipeline, metrik evaluasi, ALS, batch scoring, model registry, dan monitoring drift.",
    "slides": [
        cover(
            7,
            "Analitik & ML Terdistribusi",
            "Dari fitur skala besar ke model yang dievaluasi jujur, dikirim, dan dipantau.",
            [("MLlib", "Transformer & Estimator"), ("ROC-AUC", "Metrik ranking"), ("MLOps", "Versioning & drift")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 7",
            "Setelah sesi ini, Anda mampu membangun pipeline ML yang reproducible dan menilai kesiapannya untuk produksi.",
            grid(
                [
                    checklist([
                        "Menjelaskan siklus hidup ML",
                        "Membangun pipeline MLlib lengkap",
                        "Menangani imbalance & memilih metrik",
                        "Mencegah data leakage",
                        "Memilih batch vs online serving",
                        "Merancang monitoring drift & rollback",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Analytics maturity<br>2️⃣ Siklus ML<br>3️⃣ MLlib<br>4️⃣ Churn pipeline<br>5️⃣ Evaluasi<br>6️⃣ Deployment & monitoring", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — DARI ANALITIK KE ML", "Pertanyaan yang Menentukan Nilai", "Data besar hanya berguna jika membantu keputusan yang lebih baik."),
        content(
            "📈 Empat Tingkat Analitik",
            "Dari Deskriptif ke Preskriptif",
            "Naik tingkat hanya jika tingkat sebelumnya sudah dipercaya:",
            table(
                ["Tingkat", "Pertanyaan", "Contoh", "Keluaran"],
                [
                    ["Descriptive", "Apa yang terjadi?", "Penjualan harian", "Dashboard"],
                    ["Diagnostic", "Mengapa terjadi?", "Analisis funnel", "Root cause"],
                    ["Predictive", "Apa yang akan terjadi?", "Churn, fraud", "Skor prediksi"],
                    ["Prescriptive", "Apa yang sebaiknya dilakukan?", "Rekomendasi, harga", "Aksi"],
                ],
            ),
        ),
        content(
            "🔄 Siklus ML",
            "Model adalah Bagian Kecil dari Sistem",
            "Sebagian besar pekerjaan ada di data, fitur, evaluasi, dan operasi:",
            steps([
                ("Problem framing", "Keputusan apa yang dibantu? Bagaimana mengukur sukses?"),
                ("Data & fitur", "Representatif, bebas leakage, tersedia saat prediksi."),
                ("Training & tuning", "Baseline dulu, lalu model; simpan parameter & seed."),
                ("Evaluation", "Metrik sesuai biaya bisnis, bukan hanya accuracy."),
                ("Deployment", "Batch, online, atau streaming; siapkan rollback."),
                ("Monitoring", "Drift, performa aktual, kualitas data, biaya."),
            ]),
        ),
        content(
            "⚖️ Kapan Terdistribusi?",
            "Jangan Pakai Spark untuk Segalanya",
            "Distribusi menambah kompleksitas operasional yang harus dibayar:",
            grid(
                [
                    card("✅", "Gunakan Spark", "Data tabular sangat besar, preprocessing terdistribusi, banyak model per segmen, atau data sudah di lakehouse.", "#059669"),
                    card("❌", "Cukup scikit-learn", "Dataset muat di memori, model kecil, iterasi cepat. Sampel representatif sering lebih efektif.", "#dc2626"),
                    card("🧠", "Deep Learning", "Gunakan GPU + PyTorch/Ray; Spark untuk ETL dan feature engineering, bukan training per request.", "#0284c7"),
                    card("🔁", "Pola Umum", "Spark ETL → Parquet → training di library khusus → deploy model → monitoring.", "#9333ea"),
                ],
                2,
            ),
        ),
        divider("BAGIAN II — SPARK MLLIB", "Pipeline, Bukan Sekadar Model", "Preprocessing yang sama harus diterapkan saat training dan scoring."),
        content(
            "🧩 Konsep MLlib",
            "Transformer, Estimator, Pipeline",
            "Semua tahap dibungkus agar tidak terjadi training-serving skew:",
            grid(
                [
                    card("🔧", "Transformer", "<span class='pill-code'>transform(df)</span> → DataFrame baru. Contoh: StringIndexer, VectorAssembler.", "#0284c7"),
                    card("🎓", "Estimator", "<span class='pill-code'>fit(df)</span> → Transformer/model. Contoh: LogisticRegression, ALS.", "#059669"),
                    card("🔗", "Pipeline", "Rangkaian stage: preprocessing + model.", "#9333ea"),
                    card("📏", "Evaluator", "Menghitung metrik: AUC, F1, RMSE.", "#d97706"),
                ],
                2,
            )
            + callout("blue", "💡 Simpan seluruh <span class='pill-code'>PipelineModel</span>, bukan hanya model algoritma, agar mapping kategori dan scaling ikut tersimpan."),
        ),
        content(
            "🧪 Feature Engineering",
            "Kategori, Numerik, Missing",
            "StringIndexer → OneHotEncoder → Imputer → Assembler → Scaler:",
            code("""from pyspark.ml.feature import (
    StringIndexer, OneHotEncoder, VectorAssembler,
    StandardScaler, Imputer,
)

cat_cols = ["city", "channel", "plan_type"]
num_cols = ["tenure_months", "monthly_charge", "support_tickets"]

indexer = StringIndexer(
    inputCols=cat_cols,
    outputCols=[f"{c}_idx" for c in cat_cols],
    handleInvalid="keep")

encoder = OneHotEncoder(
    inputCols=[f"{c}_idx" for c in cat_cols],
    outputCols=[f"{c}_ohe" for c in cat_cols])

imputer = Imputer(
    inputCols=num_cols,
    outputCols=[f"{c}_imp" for c in num_cols],
    strategy="median")

assembler = VectorAssembler(
    inputCols=[f"{c}_ohe" for c in cat_cols] + [f"{c}_imp" for c in num_cols],
    outputCol="features_raw")

scaler = StandardScaler(
    inputCol="features_raw", outputCol="features",
    withMean=True, withStd=True)"""),
        ),
        content(
            "🎯 Churn Pipeline",
            "Latih, Evaluasi, Simpan",
            "Baseline dan validasi silang wajib sebelum mengklaim model berhasil:",
            code("""from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

df = spark.read.parquet("data/gold/customer_features")
df = df.withColumn("label", F.col("churn").cast("int")).drop("churn")
train, test = df.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(featuresCol="features", labelCol="label")
pipeline = Pipeline(stages=[indexer, encoder, imputer,
                            assembler, scaler, lr])
model = pipeline.fit(train)
pred = model.transform(test)

evaluator = BinaryClassificationEvaluator(
    labelCol="label", metricName="areaUnderROC")
print("ROC-AUC:", evaluator.evaluate(pred))

param_grid = (ParamGridBuilder()
    .addGrid(lr.regParam, [0.001, 0.01, 0.1])
    .addGrid(lr.elasticNetParam, [0.0, 0.5])
    .build())
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=param_grid,
                    evaluator=evaluator, numFolds=3)
cv_model = cv.fit(train)
cv_model.bestModel.write().overwrite().save("models/churn_pipeline")"""),
        ),
        divider("BAGIAN III — DEPLOYMENT & MLOPS", "Model yang Tidak Dipantau Akan Basi", "Performa produksi menurun bahkan tanpa perubahan kode."),
        content(
            "📏 Metrik Evaluasi",
            "Accuracy Sering Menyesatkan",
            "Pilih metrik berdasarkan biaya false positive vs false negative:",
            table(
                ["Metrik", "Fokus", "Catatan"],
                [
                    ["Accuracy", "Keseluruhan", "Buruk pada class imbalance"],
                    ["Precision", "Ketepatan positif", "Mahal jika false positive tinggi"],
                    ["Recall", "Menemukan positif", "Penting untuk fraud/penyakit"],
                    ["F1", "Keseimbangan P/R", "Ringkas, tetapi menyembunyikan trade-off"],
                    ["ROC-AUC", "Ranking keseluruhan", "Tidak sensitif pada imbalance ekstrem"],
                    ["PR-AUC", "Kelas minoritas", "Lebih informatif untuk fraud"],
                ],
            ),
        ),
        content(
            "📦 Batch Scoring & Registry",
            "Kirim Model dengan Jejak yang Jelas",
            "Untuk churn/risk score, batch scoring biasanya cukup dan jauh lebih sederhana:",
            grid(
                [
                    code("""from pyspark.ml import PipelineModel

model = PipelineModel.load("models/churn_pipeline")
today = spark.read.parquet("data/gold/customer_features_today")

scored = (model.transform(today)
    .select("customer_id", "probability",
            "prediction", "scored_at"))

(scored.write.mode("overwrite")
       .partitionBy("scored_at")
       .parquet("data/serving/churn_scores"))"""),
                    card("🏷️", "Model Card", "Tujuan, data training, metrik, batasan, risiko bias, penggunaan yang dilarang.", "#0284c7")
                    + card("🗂️", "Registry", "Versi model, versi data, commit Git, hyperparameter, metrik.", "#059669")
                    + callout("amber", "⚠️ Online inference per request jangan menjalankan Spark job. Ekspor model ke model server/ONNX."),
                ],
                2,
            ),
        ),
        content(
            "📡 Monitoring",
            "Tiga Drift yang Harus Dibedakan",
            "Tetapkan ambang alert, jadwalkan retraining, dan simpan model cadangan:",
            table(
                ["Jenis Drift", "Definisi", "Deteksi"],
                [
                    ["Data drift", "Distribusi fitur berubah", "PSI, KS-test, histogram"],
                    ["Concept drift", "Hubungan fitur–label berubah", "Penurunan metrik aktual"],
                    ["Prediction drift", "Distribusi skor berubah", "Rata-rata/kuantil skor"],
                    ["Data quality", "Null/aneh meningkat", "Uji kualitas pipeline"],
                ],
            )
            + callout("green", "✅ Simpan baseline distribusi saat training. Tanpa baseline, Anda tidak bisa membuktikan drift."),
        ),
        content(
            "💻 Praktikum & Milestone 2",
            "Churn End-to-End",
            "Integrasikan model ke pipeline data yang sudah Anda bangun:",
            steps([
                ("Siapkan fitur", "Minimal 50.000 baris; definisikan cutoff waktu untuk label."),
                ("Baseline", "Bandingkan dengan model mayoritas; jangan langsung tuning."),
                ("Pipeline", "Imputer → indexer → encoder → assembler → scaler → model."),
                ("Cross-validation", "3-fold, minimal 2 hyperparameter."),
                ("Simpan & scoring", "PipelineModel + metadata + batch score ke serving/."),
                ("Model card", "Tujuan, metrik, batasan, risiko bias, rencana monitoring."),
            ]),
        ),
        content(
            "🎮 Refleksi",
            "Kuis Kilat 3 Menit",
            "Jawab dulu, lalu klik untuk membuka jawaban:",
            quiz([
                ("Mengapa accuracy menyesatkan pada fraud detection?", "Jika hanya 1% transaksi fraud, model yang selalu menebak 'bukan fraud' mendapat accuracy 99% tetapi recall 0 dan tidak menangkap fraud sama sekali."),
                ("Apa itu data leakage?", "Menggunakan informasi yang tidak tersedia saat prediksi (misalnya fitur setelah label terjadi). Model terlihat bagus di test tetapi gagal di produksi."),
                ("Mengapa menyimpan PipelineModel, bukan hanya modelnya?", "Pipeline menyimpan mapping kategori, imputer, scaler, dan urutan transformasi, sehingga scoring konsisten dengan training."),
            ]),
        ),
        closing(
            "Model yang baik bukan yang paling akurat di notebook, tetapi yang tetap berguna saat data berubah.",
            [("📖 Modul 7", "MLlib & MLOps"), ("🏁 Milestone 2", "Pipeline ML"), ("➡️ Berikutnya", "Capstone & tata kelola")],
            "Selesaikan Milestone 2 dan siapkan model card satu halaman.",
        ),
    ],
}


# ---------------------------------------------------------------------------
# DECK 8
# ---------------------------------------------------------------------------
DECK8 = {
    "num": 8,
    "slug": "capstone-tata-kelola",
    "file": "pertemuan-8-capstone-tata-kelola.html",
    "module": "08-proyek-akhir-tata-kelola",
    "title": "Proyek Akhir, Tata Kelola & Optimasi Biaya",
    "subtitle": "Membuktikan sistem data yang berjalan, aman, patuh, dan masuk akal secara biaya.",
    "description": "Slide interaktif Pertemuan 8 Big Data IFR229: arsitektur capstone, deliverables, data governance, keamanan, UU PDP, anonimisasi, optimasi biaya, anti-pattern, dan rubrik proyek akhir.",
    "slides": [
        cover(
            8,
            "Proyek Akhir, Tata Kelola & Optimasi Biaya",
            "Membuktikan sistem data yang berjalan, aman, patuh, dan masuk akal secara biaya.",
            [("1 Command", "Dapat dijalankan ulang"), ("UU PDP", "Privasi data"), ("100 Poin", "Rubrik capstone")],
        ),
        content(
            "🎯 Capaian Pembelajaran",
            "Kompetensi Pertemuan 8",
            "Setelah sesi ini, Anda mampu mempertahankan proyek secara teknis, etis, dan ekonomis.",
            grid(
                [
                    checklist([
                        "Menyajikan arsitektur end-to-end",
                        "Mendokumentasikan katalog, lineage, ownership",
                        "Menerapkan keamanan & least privilege",
                        "Menangani PII sesuai UU PDP",
                        "Menghitung biaya & strategi penghematan",
                        "Menghindari anti-pattern umum",
                    ]),
                    card("🗺️", "Alur Hari Ini", "1️⃣ Referensi arsitektur<br>2️⃣ Deliverables<br>3️⃣ Tata kelola<br>4️⃣ Keamanan & privasi<br>5️⃣ Biaya<br>6️⃣ Rubrik & demo", "#0284c7"),
                ],
                2,
            ),
        ),
        divider("BAGIAN I — CAPSTONE", "Dari Data Mentah ke Layanan", "Satu sistem yang bisa dijalankan ulang dari kondisi bersih."),
        content(
            "🏗️ Arsitektur Referensi",
            "Enam Lapisan yang Harus Terlihat",
            "Setiap lapisan punya bukti: kode, konfigurasi, atau artefak:",
            steps([
                ("Sumber", "API/aplikasi, database OLTP, log/sensor."),
                ("Ingestion", "Batch connector + Kafka/CDC. Minimal satu batch dan satu streaming (boleh simulasi)."),
                ("Storage", "Bronze mentah → silver bersih → gold business-ready."),
                ("Processing", "Spark ETL, quality gate, model MLlib bila relevan."),
                ("Serving", "Dashboard, REST API, atau batch scores."),
                ("Operations", "Airflow, katalog/lineage, monitoring, IAM/secrets."),
            ])
            + callout("blue", "💡 Diagram harus menunjukkan <b>aliran data</b> dan <b>cross-cutting concerns</b>, bukan hanya logo teknologi."),
        ),
        content(
            "🎯 Pilihan Studi Kasus",
            "Satu Kasus, Ruang Lingkup Jelas",
            "Pilih yang datanya dapat Anda peroleh atau bangkitkan:",
            table(
                ["Kasus", "Pertanyaan Bisnis", "Komponen Wajib"],
                [
                    ["Funnel e-commerce", "Di tahap mana pengguna berhenti?", "Event stream, funnel, segmentasi"],
                    ["Deteksi fraud", "Transaksi mana yang mencurigakan?", "Aturan + model, near-real-time"],
                    ["Log analytics", "Bagaimana kesehatan layanan?", "Batch + dashboard error rate"],
                    ["IoT / smart city", "Bagaimana pola sensor & anomali?", "Time-series, agregasi jendela"],
                    ["Rekomendasi", "Apa yang relevan untuk pengguna?", "ALS, batch scoring"],
                    ["Churn", "Pelanggan mana berisiko berhenti?", "Feature pipeline, model, scoring"],
                ],
            ),
        ),
        content(
            "📦 Deliverables",
            "Sepuluh Artefak yang Dinilai",
            "Kualitas dokumentasi sama pentingnya dengan kode:",
            grid(
                [
                    card("📁", "Repositori Git", "Kode, DAG, test, README, .env.example.", "#0284c7"),
                    card("🏗️", "Diagram Arsitektur", "Aliran data + cross-cutting concerns.", "#059669"),
                    card("📖", "Data Dictionary", "Tabel, kolom, tipe, deskripsi, klasifikasi PII.", "#9333ea"),
                    card("⚙️", "Pipeline", "Batch + streaming, idempoten, dapat dijalankan ulang.", "#d97706"),
                    card("🧪", "Uji Kualitas", "≥5 checks + quality gate.", "#dc2626"),
                    card("📊", "Serving", "Dashboard/API/batch scores yang berfungsi.", "#0f766e"),
                    card("🤖", "Model Card", "Jika ada ML: metrik, versi, batasan, monitoring.", "#7c3aed"),
                    card("🛡️", "Governance Pack", "Ownership, lineage, retensi, akses, PII.", "#0891b2"),
                    card("📄", "Laporan", "8–12 halaman termasuk biaya & risiko.", "#be123c"),
                ],
                3,
            )
            + callout("green", "✅ <b>One command:</b> <span class='pill-code'>git clone → cp .env.example .env → docker compose up -d → make seed → make run → make test</span>"),
        ),
        divider("BAGIAN II — TATA KELOLA & KEAMANAN", "Data yang Tidak Dikelola Akan Menjadi Beban", "Katalog, kontrak, akses, dan audit membuat data dapat dipercaya."),
        content(
            "🗂️ Tata Kelola",
            "Tujuh Komponen Wajib",
            "Tanpa ownership dan lineage, debugging dan audit menjadi mustahil:",
            table(
                ["Komponen", "Pertanyaan", "Artefak"],
                [
                    ["Katalog", "Data apa yang kita punya?", "Data catalog"],
                    ["Lineage", "Dari mana data ini berasal?", "Graf table/column-level"],
                    ["Ownership", "Siapa penanggung jawab?", "Data owner & steward"],
                    ["Kontrak data", "Apa jaminan skema & SLA?", "Data contract berversi"],
                    ["Klasifikasi", "Seberapa sensitif?", "Public/Internal/Confidential/Restricted"],
                    ["Retensi", "Berapa lama disimpan?", "Kebijakan retensi & hapus"],
                    ["Akses", "Siapa boleh melihat?", "RBAC/ABAC, row/column security"],
                ],
            ),
        ),
        content(
            "📜 Kontrak Data",
            "Kesepakatan Produsen–Konsumen",
            "Perubahan skema yang merusak konsumen harus terdeteksi sebelum deploy:",
            grid(
                [
                    code("""name: orders.events
version: 1.0.0
owner: team-checkout
sla:
  freshness: 5m
  availability: 99.5%
schema:
  order_id: {type: string, required: true, unique: true}
  customer_id: {type: string, required: true, pii: true}
  amount: {type: decimal, required: true, min: 0}
  status: {type: enum, values: [created, paid, cancelled]}
compatibility: backward"""),
                    card("🕸️", "Data Mesh", "Domain ownership, data as a product, self-serve platform, federated governance.", "#0284c7")
                    + callout("amber", "⚠️ Data mesh adalah model organisasi, bukan alat. Jangan adopsi jika masalah utama masih pipeline rapuh dan kualitas buruk."),
                ],
                2,
            ),
        ),
        content(
            "🔐 Keamanan",
            "Kontrol yang Tidak Boleh Ditawar",
            "CIA triad diterjemahkan menjadi kontrol konkret:",
            table(
                ["Area", "Kontrol"],
                [
                    ["Autentikasi", "SSO, MFA, akun layanan terpisah"],
                    ["Otorisasi", "Least privilege, RBAC/ABAC, row/column-level"],
                    ["Enkripsi", "TLS 1.2+ in transit; AES-256 at rest; KMS"],
                    ["Jaringan", "Private subnet, security group, tanpa bucket publik"],
                    ["Rahasia", "Secret manager/Vault; tidak ada kredensial di Git"],
                    ["Audit", "Log akses & query, retensi sesuai kebijakan"],
                    ["Backup", "Uji restore, bukan hanya membuat backup"],
                ],
            )
            + callout("red", "❌ Bucket terbuka dan credential di repo publik adalah dua insiden paling umum — dan paling mudah dicegah."),
        ),
        divider("BAGIAN III — PRIVASI & BIAYA", "Kepatuhan dan Ekonomi", "Privasi bukan beban; biaya adalah requirement non-fungsional."),
        content(
            "🇮🇩 UU PDP",
            "UU No. 27 Tahun 2022",
            "Prinsip dan kewajiban utama yang relevan untuk pipeline data:",
            table(
                ["Konsep", "Penjelasan"],
                [
                    ["Data pribadi", "Data tentang individu yang teridentifikasi/dapat diidentifikasi"],
                    ["Data spesifik", "Kesehatan, biometrik, genetika, keuangan pribadi, anak"],
                    ["Pengendali", "Menentukan tujuan & cara pemrosesan"],
                    ["Prosesor", "Memproses atas nama pengendali"],
                    ["Hak subjek", "Informasi, akses, koreksi, hapus, tarik consent, portabilitas"],
                    ["Notifikasi bocor", "Maksimal 3×24 jam"],
                    ["Prinsip", "Tujuan terbatas, minimisasi, akurasi, retensi terbatas, keamanan"],
                ],
            ),
        ),
        content(
            "🕵️ Anonimisasi",
            "Menghapus Nama Tidak Cukup",
            "Kombinasi quasi-identifier dapat mengidentifikasi individu:",
            grid(
                [
                    card("🎭", "Pseudonimisasi", "Ganti identifier dengan token; mapping disimpan terpisah. Masih data pribadi menurut UU PDP.", "#0284c7"),
                    card("🔐", "Hashing + Salt", "Sulit dikembalikan jika salt aman; rentan brute-force pada ruang nilai kecil.", "#059669"),
                    card("🎫", "Tokenization", "Nomor kartu diganti token via vault. Cocok untuk data pembayaran.", "#9333ea"),
                    card("📊", "k-Anonymity", "Setiap kombinasi quasi-identifier muncul ≥ k kali. Tetap bisa rentan jika sensitif.", "#d97706"),
                    card("🌫️", "Differential Privacy", "Tambahkan noise terkalibrasi; ada trade-off akurasi.", "#dc2626"),
                    card("🧹", "Retensi & Hapus", "Hapus otomatis setelah masa retensi; pastikan right to erasure menjangkau turunan.", "#0f766e"),
                ],
                3,
            )
            + callout("amber", "⚠️ Selalu uji risiko re-identifikasi: tanggal lahir + kode pos + jenis kelamin bisa cukup."),
        ),
        content(
            "💰 Optimasi Biaya",
            "Ukur, Jangan Menebak",
            "Contoh ilustratif: 100 TB storage, 10 worker × 8 jam/hari, egress 5 TB:",
            grid(
                [
                    code("""Storage : 100 x 1.024 x 1.024 GB x $0.023
        ~= $2.416/bulan
Compute : 10 x 8 x 30 x $0.50
        = $1.200/bulan
Egress  : 5.000 GB x $0.09
        = $450/bulan
------------------------------------
Total kasar ~= $4.066/bulan"""),
                    card("📉", "Penghematan", "Parquet + kompresi (storage ↓80%) · matikan cluster idle (compute ↓50%) · partition pruning (scan ↓60–90%) · lifecycle cold storage (↓50–70%) · spot instance (↓50–70%).", "#059669")
                    + callout("blue", "💡 Metrik berguna: <b>cost per 1.000 event</b>, cost per query, storage per tabel, idle time, bytes scanned vs returned."),
                ],
                2,
            ),
        ),
        content(
            "🚫 Anti-Pattern",
            "Kesalahan yang Paling Sering Terjadi",
            "Kenali sebelum proyek Anda menjadi studi kasus:",
            table(
                ["Anti-pattern", "Akibat", "Perbaikan"],
                [
                    ["Data swamp", "Data tak ditemukan", "Katalog, ownership, klasifikasi"],
                    ["Dual write", "Data tidak konsisten", "Outbox/CDC"],
                    ["Cron + skrip manual", "Tidak ada retry/visibilitas", "Orkestrasi"],
                    ["Tidak idempoten", "Duplikasi saat retry", "Overwrite/upsert"],
                    ["SELECT *", "I/O boros", "Pilih kolom"],
                    ["Small files", "Metadata lambat", "Kompaksi, coalesce"],
                    ["Cluster selalu hidup", "Biaya tinggi", "Autoscaling, shutdown"],
                    ["Tanpa test", "Bug data lolos", "Unit + quality test"],
                    ["Hardcoded secret", "Kebocoran", "Secret manager"],
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
                            ["Problem & requirements", "15%"],
                            ["Arsitektur", "15%"],
                            ["Ingestion & storage", "15%"],
                            ["Processing & pipeline", "20%"],
                            ["Kualitas & pengujian", "10%"],
                            ["Governance/security/privacy", "10%"],
                            ["Demo & dokumentasi", "10%"],
                            ["Kolaborasi & defense", "5%"],
                        ],
                    ),
                    steps([
                        ("0–2 menit", "Masalah, pengguna, metrik sukses."),
                        ("2–4 menit", "Arsitektur & keputusan teknologi."),
                        ("4–8 menit", "Demo live: ingest → pipeline → gold → serving."),
                        ("8–9 menit", "Simulasi kegagalan + pemulihan."),
                        ("9–10 menit", "Biaya, keamanan, pelajaran."),
                    ]),
                ],
                2,
            ),
        ),
        content(
            "🎤 Pertahanan Proyek",
            "Delapan Pertanyaan yang Harus Anda Jawab",
            "Klik untuk melihat arah jawaban yang baik:",
            quiz([
                ("Mengapa memilih batch/streaming untuk kasus Anda?", "Kaitkan dengan kebutuhan latensi terukur dan biaya operasional, bukan preferensi teknologi."),
                ("Apa yang terjadi jika pipeline dijalankan dua kali untuk tanggal yang sama?", "Harus menghasilkan data identik: partition overwrite, upsert, atau dedup by key."),
                ("Di mana PII disimpan dan bagaimana dilindungi?", "Identifikasi kolom, masking/tokenization, akses minimum, enkripsi, retensi, audit."),
                ("Berapa biaya memproses 1.000 event?", "Tunjukkan perhitungan storage + compute + scan; bandingkan dengan baseline."),
                ("Bagaimana mendeteksi penurunan kualitas data?", "Freshness, volume anomaly, null rate, uniqueness, schema drift, alert."),
                ("Bagian mana yang paling rapuh?", "Jujur sebutkan risiko + mitigasi + rencana pengujian."),
            ]),
        ),
        closing(
            "Sistem data yang baik membuat keputusan lebih cepat, lebih murah, dan lebih dapat dipercaya.",
            [("📖 Modul 8", "Capstone & governance"), ("🏁 UAS", "Demo + laporan"), ("🎓 Selesai", "8 pertemuan")],
            "Siapkan demo 10 menit, laporan 8–12 halaman, dan pastikan proyek dapat dijalankan dari kondisi bersih.",
        ),
    ],
}


DECKS = [DECK1, DECK2, DECK3, DECK4, DECK5, DECK6, DECK7, DECK8]


def build_main(deck: dict) -> tuple[str, list[str]]:
    parts = []
    narrations = []
    total = len(deck["slides"])
    for idx, (slide_html, narration) in enumerate(deck["slides"], 1):
        # Every slide helper returns a string ending with </div>.
        numbered = slide_html[:-6] + f'<div class="slide-num">{idx:02d} / {total:02d}</div></div>'
        parts.append(numbered)
        narrations.append(narration)
    return "\n".join(parts), narrations


def build_deck(deck: dict) -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    head, rest = template.split("<body>", 1)
    # Replace document metadata.
    head = re.sub(r"<title>.*?</title>", f"<title>Pertemuan {deck['num']} - {deck['title']} | Big Data IFR229</title>", head, flags=re.S)
    head = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{html.escape(deck["description"], quote=True)}">',
        head,
        flags=re.S,
    )
    head = head.replace("</style>", COMPACT_CSS + "</style>")
    # Everything after </main> keeps footer, drawer, and the player script.
    suffix = rest.split("</main>", 1)[1]

    main_html, narrations = build_main(deck)
    header = f"""<body>
<header>
<div class="brand">
<img src="{BASE}/uuilogo.png" alt="UUI Logo" class="brand-logo" onerror="this.style.display='none'">
<div><div class="brand-text">BIG DATA <span>(IFR229)</span></div><div class="brand-sub">Universitas Ubudiyah Indonesia — Pertemuan {deck['num']}</div></div>
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
  <option value="1.0">1.0x</option>
  <option value="1.25" selected>1.25x</option>
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

    # Replace narration array and audio URL builder.
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
        "Penjelasan Dosen (Suara AI Ardi — Pak Mahendar)",
        "Penjelasan Dosen (Narasi AI — Pak Mahendar)",
    )
    suffix = suffix.replace(
        '<option value="1.0">1.0x</option>\n  <option value="1.25" selected>1.25x</option>',
        '<option value="1.0" selected>1.0x</option>\n  <option value="1.25">1.25x</option>',
    )
    suffix = suffix.replace("let currentPlaybackRate=1.25;", "let currentPlaybackRate=1.0;")

    out = head + header + suffix
    out_path = PUBLIC / deck["file"]
    out_path.write_text(out, encoding="utf-8")

    # Presentation page (VitePress) embedding the deck.
    page = f"""# Slide: Pertemuan {deck['num']} — {deck['title']}

<div style="margin-bottom: 16px; display: flex; gap: 10px; flex-wrap: wrap;">
  <a href="{BASE}/presentasi/{deck['file']}" target="_blank" style="background-color: #0284c7; color: white; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
    ⛶ Buka Slide Layar Penuh (Tab Baru)
  </a>
  <a href="{BASE}/big-data/{deck['module']}" style="background-color: #1e293b; color: #f8fafc; border: 1px solid #334155; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
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
    (DOCS_PRESENTASI / f"pertemuan-{deck['num']}-big-data.md").write_text(page, encoding="utf-8")
    print(f"OK  {deck['file']}  ({len(deck['slides'])} slides)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    DOCS_PRESENTASI.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for deck in DECKS:
        build_deck(deck)
        manifest[f"m{deck['num']}"] = [n for _, n in deck["slides"]]
    (ROOT / "scratch" / "big_data_audio_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Manifest: scratch/big_data_audio_manifest.json")
