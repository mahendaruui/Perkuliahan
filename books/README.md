# Sistem Generator Buku Ajar Multi-Mata Kuliah
**Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia (UUI)**
Penulis / Dosen Pengampu: **Mahendar Dwi Payana, S.ST., M.T.**

Repositori ini menyediakan arsitektur pembuatan dokumen Buku Ajar resmi berformat Word (.docx) standar akademik (A4, Margin 4-3-3-3 cm, KDT/Hak Cipta, Daftar Isi Presisi, Code Syntax Highlighter multi-bahasa, dan Green Tips Highlight).

---

## 📁 Arsitektur Direktori Multi-Buku

```
books/
├── core/                                # 🧠 ENGINE INTI (Dapat digunakan bersama oleh semua buku)
│   ├── __init__.py
│   └── book_builder.py                  # Standar styling, margin A4, tabel KDT, daftar isi, blok kode & tips
│
├── oop-php/                             # 🐘 BUKU 1: Pemrograman Berorientasi Objek (PHP 8+)
│   ├── generate.py                      # Skrip kompilasi buku OOP PHP
│   └── output/                          # Berkas luaran Word (.docx) berversi
│       ├── Buku_Ajar_OOP_PHP8_v1.0.0_Mahendar_Dwi_Payana.docx
│       └── Buku_Ajar_OOP_PHP8_Latest.docx
│
├── struktur-data-golang/                # 🔷 BUKU 2: Struktur Data (Golang) [Siap dikembangkan]
├── algoritma-pemrograman/               # ⚡ BUKU 3: Algoritma & Pemrograman (Python / C++) [Siap dikembangkan]
├── pemrograman-web/                     # 🌐 BUKU 4: Pemrograman Web (PHP / Laravel) [Siap dikembangkan]
├── mobile-programming/                  # 📱 BUKU 5: Pemrograman Mobile (React Native) [Siap dikembangkan]
├── pemrograman-oop-java/                # ☕ BUKU 6: Pemrograman Berorientasi Objek (Java) [Siap dikembangkan]
├── kompleksitas-algoritma/              # 📊 BUKU 7: Kompleksitas Algoritma [Siap dikembangkan]
└── README.md
```

---

## 🚀 Cara Men-generate Buku

### 1. Men-generate Buku OOP PHP 8+:
```bash
# Rilis versi default (v1.0.0)
.venv/bin/python books/oop-php/generate.py

# Rilis versi kustom (misal v1.1.0 atau v2.0.0)
.venv/bin/python books/oop-php/generate.py --version 1.1.0
```

Berkas hasil akan otomatis terbit di folder `books/oop-php/output/`.

---

## 🛠️ Menambahkan Buku Mata Kuliah Baru di Masa Mendatang

Untuk membuat buku dari modul mata kuliah lain di VitePress (misalnya *Struktur Data Golang*):
1. Buat folder baru di bawah `books/`, misal `books/struktur-data-golang/`.
2. Buat skrip `generate.py` di dalam folder tersebut dan import core engine:
   ```python
   from books.core.book_builder import AcademicBookBuilder
   ```
3. Susun bab materi dari berkas Markdown di `docs/struktur-data/` dan jalankan generator.
