# Pertemuan 5: ETL & Kualitas Data

::: info 🎓 Bacaan Teori Wajib (Kelas RPL)
Baca **[Buku Teori Data Warehouse — Pertemuan 5](/datawarehouse/TEORI-RPL#p5)** sebelum praktik. Latihan teknis di modul ini adalah **pengayaan/verifikasi**; fokus utama adalah pemahaman konsep dan kemampuan menjelaskan trade-off.
:::

::: tip 🎙️ Slide Presentasi Interaktif
Buka **[slide presentasi Pertemuan 5](/presentasi/pertemuan-5-datawarehouse)** — dilengkapi navigasi keyboard, timer, transkrip, dan narasi audio.
Untuk presentasi layar penuh, buka **[HTML interaktif](/Perkuliahan/presentasi/pertemuan-5-etl-kualitas-data.html)** di tab baru.
:::

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 5)
- **CPMK Terkait:** CPMK 3
- **CPL Terkait:** CPL03, CPL04, CPL08
- **Indikator:** Mahasiswa mampu membangun ETL incremental yang idempoten, menerapkan aturan kualitas data, menangani baris ditolak, dan merekonsiliasi hasil load.
:::

---

## 1. Dari Sumber ke Star Schema

ETL adalah proses memindahkan data dari sumber operasional ke data warehouse melalui tiga tahap:

```mermaid
flowchart LR
    E["Extract<br/>ambil data sumber"] --> T["Transform<br/>bersihkan, standarisasi,<br/>resolve key, hitung measure"]
    T --> L["Load<br/>isi dimension & fact"]
    L --> Q["Quality Check<br/>rekonsiliasi"]
    Q --> P["Publish<br/>siap untuk BI"]
```

| Tahap | Pertanyaan Kunci | Risiko |
| :--- | :--- | :--- |
| **Extract** | Data apa yang berubah sejak load terakhir? | Data hilang, duplikat, sumber berubah |
| **Transform** | Bagaimana aturan bisnis diterapkan? | Definisi tidak konsisten, key tidak ketemu |
| **Load** | Bagaimana menulis tanpa duplikasi? | Double load, partial load |
| **Quality** | Apakah hasilnya benar? | Dashboard menampilkan angka salah |

---

## 2. Extract: Full vs Incremental vs CDC

| Strategi | Cara | Kelebihan | Kekurangan |
| :--- | :--- | :--- | :--- |
| **Full extract** | Ambil semua data setiap run | Sederhana, tahan perubahan | Berat untuk data besar |
| **Incremental** | Ambil berdasarkan `updated_at` / watermark | Efisien | Butuh kolom andal, risiko telat |
| **CDC** | Baca log perubahan database (WAL/binlog) | Near-real-time, lengkap | Infrastruktur lebih kompleks |

### Watermark

```sql
CREATE SCHEMA IF NOT EXISTS etl;

CREATE TABLE etl.watermark (
    pipeline       TEXT PRIMARY KEY,
    last_loaded_at TIMESTAMP NOT NULL
);

INSERT INTO etl.watermark (pipeline, last_loaded_at)
VALUES ('orders_incremental', TIMESTAMP '2024-01-01 00:00:00')
ON CONFLICT (pipeline) DO NOTHING;
```

```sql
-- Ekstrak hanya data baru/berubah
SELECT *
FROM oltp.orders
WHERE updated_at > (
    SELECT last_loaded_at
    FROM etl.watermark
    WHERE pipeline = 'orders_incremental'
);
```

> **Penting:** gunakan `>` bukan `>=` jika watermark disimpan sebagai waktu maksimum yang sudah diproses. Jika ada data terlambat, proses ulang jendela beberapa hari.

### CDC Sederhana

Jika sumber tidak punya `updated_at`, tambahkan trigger atau gunakan log:

```sql
ALTER TABLE oltp.orders
ADD COLUMN updated_at TIMESTAMP NOT NULL DEFAULT now();

CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_orders_updated
BEFORE UPDATE ON oltp.orders
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
```

---

## 3. Transform: Aturan Bisnis

### 3.1 Standarisasi

| Masalah | Contoh | Solusi |
| :--- | :--- | :--- |
| Huruf besar/kecil | `Elektronik`, `ELEKTRONIK` | `LOWER(TRIM(...))` atau mapping |
| Spasi ganda | `"Banda  Aceh"` | `REGEXP_REPLACE(..., '\s+', ' ', 'g')` |
| Format tanggal | `01/09/2024`, `2024-09-01` | `TO_TIMESTAMP` dengan format eksplisit |
| Nilai kosong | `''`, `'NULL'`, `'-'` | `NULLIF` |
| Mata uang | `"Rp 1.000.000"` | Bersihkan karakter non-digit |

### 3.2 Deduplikasi

```sql
-- Ambil baris terbaru per order line
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY order_id, line_no
               ORDER BY updated_at DESC
           ) AS rn
    FROM staging.raw_orders
)
SELECT *
FROM ranked
WHERE rn = 1;
```

### 3.3 Resolusi Surrogate Key

Fact table tidak boleh menyimpan natural key. Lakukan lookup:

```sql
JOIN dw.dim_product p ON p.product_code = s.product_code
JOIN dw.dim_customer c ON c.customer_code = s.customer_code
JOIN dw.dim_store st ON st.store_code = s.store_code
```

Jika key tidak ditemukan, **jangan** buang diam-diam. Catat ke reject table atau gunakan inferred member.

### 3.4 Perhitungan Measure

```sql
quantity * unit_price                AS gross_revenue,
COALESCE(discount, 0)                AS discount,
quantity * unit_price - discount     AS net_revenue,
quantity * product_cost              AS cost
```

Pastikan tipe data `NUMERIC`, bukan `FLOAT`, untuk nilai uang.

---

## 4. Load: Idempotensi

Pipeline harus aman dijalankan ulang. Tiga pola utama:

### 4.1 Append + Unique Constraint

```sql
INSERT INTO dw.fact_sales (...)
SELECT ...
ON CONFLICT (order_id, line_no) DO NOTHING;
```

Cocok jika data tidak pernah berubah.

### 4.2 Upsert (ON CONFLICT DO UPDATE)

```sql
INSERT INTO dw.fact_sales (
    date_key, product_key, customer_key, store_key,
    order_id, line_no, quantity, gross_revenue, discount, net_revenue, cost
)
SELECT ...
ON CONFLICT (order_id, line_no) DO UPDATE
SET quantity      = EXCLUDED.quantity,
    net_revenue   = EXCLUDED.net_revenue,
    cost          = EXCLUDED.cost;
```

Cocok untuk koreksi/retur.

### 4.3 Partition Overwrite

Untuk fact harian, hapus partisi tanggal lalu muat ulang:

```sql
BEGIN;
DELETE FROM dw.fact_sales WHERE date_key = 20240901;
INSERT INTO dw.fact_sales (...) SELECT ... WHERE date_key = 20240901;
COMMIT;
```

Sederhana dan idempoten, tetapi mahal untuk partisi besar.

### 4.4 MERGE (PostgreSQL 15+)

```sql
MERGE INTO dw.dim_product AS t
USING staging.stg_product AS s
ON t.product_code = s.product_code
WHEN MATCHED THEN
    UPDATE SET product_name = s.product_name,
               category     = s.category,
               cost         = s.cost
WHEN NOT MATCHED THEN
    INSERT (product_code, product_name, category, cost)
    VALUES (s.product_code, s.product_name, s.category, s.cost);
```

---

## 5. Kualitas Data

### 5.1 Dimensi Kualitas

| Dimensi | Pertanyaan | Contoh Uji |
| :--- | :--- | :--- |
| **Completeness** | Apakah semua data ada? | `null_rate < 1%` |
| **Uniqueness** | Apakah ada duplikat? | `COUNT(*) = COUNT(DISTINCT order_id, line_no)` |
| **Validity** | Apakah nilai sesuai domain? | `status IN ('paid','cancelled')` |
| **Consistency** | Apakah antar-tabel cocok? | Setiap `product_key` ada di `dim_product` |
| **Timeliness** | Apakah data cukup baru? | `MAX(loaded_at) > now() - interval '2 hours'` |
| **Accuracy** | Apakah cocok dengan sumber? | `SUM(fact.net_revenue) = SUM(source.net_revenue)` |
| **Volume** | Apakah jumlah wajar? | `row_count` ±30% baseline |

### 5.2 Reject Table

```sql
CREATE TABLE etl.rejected_rows (
    reject_id   BIGSERIAL PRIMARY KEY,
    pipeline    TEXT NOT NULL,
    reason      TEXT NOT NULL,
    payload     JSONB,
    rejected_at TIMESTAMP NOT NULL DEFAULT now()
);
```

Contoh mencatat baris tanpa customer:

```sql
INSERT INTO etl.rejected_rows (pipeline, reason, payload)
SELECT 'orders_incremental', 'customer_not_found', TO_JSONB(s)
FROM staging.stg_orders s
LEFT JOIN dw.dim_customer c ON c.customer_code = s.customer_code
WHERE c.customer_key IS NULL;
```

### 5.3 Rekonsiliasi

```sql
-- Sumber
SELECT SUM(quantity * unit_price - COALESCE(discount, 0)) AS source_revenue
FROM staging.stg_orders
WHERE status = 'paid' AND load_date = DATE '2024-09-01';

-- Warehouse
SELECT SUM(net_revenue) AS dw_revenue
FROM dw.fact_sales f
JOIN dw.dim_date d ON d.date_key = f.date_key
WHERE d.full_date = DATE '2024-09-01';

-- Selisih harus 0 (atau dijelaskan)
```

### 5.4 Quality Gate

Pipeline harus berhenti jika uji kritis gagal:

```sql
-- Gagal jika ada duplikat
SELECT order_id, line_no, COUNT(*)
FROM dw.fact_sales
GROUP BY order_id, line_no
HAVING COUNT(*) > 1;

-- Gagal jika referensi rusak
SELECT COUNT(*) AS orphan_rows
FROM dw.fact_sales f
LEFT JOIN dw.dim_product p ON p.product_key = f.product_key
WHERE p.product_key IS NULL;
```

---

## 6. Orkestrasi & Operasional

| Komponen | Tujuan | Contoh |
| :--- | :--- | :--- |
| **Scheduler** | Menjalankan pipeline tepat waktu | Airflow, cron, Dagster |
| **Dependency** | Urutan extract → dim → fact → quality | DAG |
| **Retry** | Menangani kegagalan sementara | 3× dengan backoff |
| **Logging** | Melacak jumlah baris & error | Tabel `etl.run_log` |
| **Alert** | Memberi tahu kegagalan | Email/Slack |
| **Idempotency** | Aman dijalankan ulang | Upsert/overwrite |

```sql
CREATE TABLE etl.run_log (
    run_id      BIGSERIAL PRIMARY KEY,
    pipeline    TEXT NOT NULL,
    started_at  TIMESTAMP NOT NULL DEFAULT now(),
    finished_at TIMESTAMP,
    status      TEXT NOT NULL DEFAULT 'running',
    rows_read   INTEGER DEFAULT 0,
    rows_loaded INTEGER DEFAULT 0,
    rows_rejected INTEGER DEFAULT 0,
    message     TEXT
);
```

---

## 7. Praktik Terbimbing (Pengayaan): ETL Incremental + Quality Checks

### 7.1 Siapkan Data CSV

```text
order_id,order_ts,customer_code,product_code,store_code,quantity,unit_price,discount,status
O0001,2024-09-01 10:00:00,C001,P001,S001,2,150000,0,paid
O0002,2024-09-01 10:15:00,C002,P002,S001,1,250000,10000,paid
O0003,2024-09-01 11:00:00,C999,P003,S002,1,90000,0,paid
```

`C999` sengaja tidak ada di `dim_customer` untuk menguji reject table.

### 7.2 Load ke Staging dengan Python

```python
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg://postgres:dw123@localhost:5432/retail_dw"
)

raw = pd.read_csv("data/orders_2024-09-01.csv")
raw["load_date"] = "2024-09-01"

raw.to_sql(
    "stg_orders",
    engine,
    schema="staging",
    if_exists="replace",
    index=False,
)

with engine.begin() as conn:
    conn.execute(text("""
        INSERT INTO etl.rejected_rows (pipeline, reason, payload)
        SELECT 'orders_incremental', 'customer_not_found', TO_JSONB(s)
        FROM staging.stg_orders s
        LEFT JOIN dw.dim_customer c ON c.customer_code = s.customer_code
        WHERE c.customer_key IS NULL
    """))
```

### 7.3 Transform & Load

```sql
INSERT INTO dw.fact_sales (
    date_key, product_key, customer_key, store_key,
    order_id, line_no, quantity, gross_revenue, discount, net_revenue, cost
)
SELECT
    TO_CHAR(s.order_ts::TIMESTAMP, 'YYYYMMDD')::INT,
    p.product_key,
    c.customer_key,
    st.store_key,
    s.order_id,
    ROW_NUMBER() OVER (PARTITION BY s.order_id ORDER BY s.product_code)::INT,
    s.quantity::INT,
    s.quantity::NUMERIC * s.unit_price::NUMERIC,
    COALESCE(s.discount::NUMERIC, 0),
    s.quantity::NUMERIC * s.unit_price::NUMERIC - COALESCE(s.discount::NUMERIC, 0),
    s.quantity::NUMERIC * p.cost
FROM staging.stg_orders s
JOIN dw.dim_product p  ON p.product_code = s.product_code
JOIN dw.dim_customer c ON c.customer_code = s.customer_code
JOIN dw.dim_store st  ON st.store_code = s.store_code
WHERE s.status = 'paid'
ON CONFLICT (order_id, line_no) DO UPDATE
SET quantity     = EXCLUDED.quantity,
    net_revenue  = EXCLUDED.net_revenue,
    cost         = EXCLUDED.cost;
```

### 7.4 Uji Kualitas

```sql
-- 1. Tidak ada duplikat
SELECT COUNT(*) FROM (
    SELECT order_id, line_no
    FROM dw.fact_sales
    GROUP BY order_id, line_no
    HAVING COUNT(*) > 1
) d;

-- 2. Tidak ada orphan dimension
SELECT COUNT(*)
FROM dw.fact_sales f
LEFT JOIN dw.dim_product p ON p.product_key = f.product_key
WHERE p.product_key IS NULL;

-- 3. Rekonsiliasi revenue
SELECT
    (SELECT SUM(quantity * unit_price - COALESCE(discount,0))
     FROM staging.stg_orders WHERE status = 'paid') AS source,
    (SELECT SUM(net_revenue) FROM dw.fact_sales) AS target;
```

### 7.5 Jalankan Dua Kali

Jalankan langkah 7.2–7.3 dua kali. Jumlah baris fact **tidak boleh bertambah**. Inilah bukti idempotensi.

---

## 8. Tugas 5 — ETL Incremental + Kualitas (6%)

1. Bangun ETL dari data sumber (CSV/OLTP) ke star schema Anda.
2. Gunakan **watermark** atau strategi incremental lain.
3. Terapkan minimal **5 aturan kualitas**.
4. Catat baris ditolak ke `rejected_rows` beserta alasannya.
5. Buktikan **idempotensi** dengan menjalankan dua kali.
6. Lakukan **rekonsiliasi** sumber vs warehouse.
7. Sertakan log eksekusi (rows read/loaded/rejected, durasi).

**Penilaian:** fungsionalitas ETL (35%), idempotensi & penanganan error (25%), kualitas data (20%), dokumentasi & bukti (20%).

---

## 9. Checklist

- [ ] Saya dapat memilih full, incremental, atau CDC.
- [ ] Saya dapat menggunakan watermark dengan benar.
- [ ] Saya dapat membersihkan dan menstandarkan data.
- [ ] Saya dapat melakukan upsert/merge yang idempoten.
- [ ] Saya dapat menulis reject table dan rekonsiliasi.
- [ ] Saya dapat membuktikan pipeline aman dijalankan ulang.

---

## 📚 Bacaan Lanjutan

- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit*, Bab 19–20.
- Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering*, Bab 8–9.
- PostgreSQL Documentation — *INSERT ... ON CONFLICT*, *MERGE*.
- dbt Documentation — *Data Tests*.
