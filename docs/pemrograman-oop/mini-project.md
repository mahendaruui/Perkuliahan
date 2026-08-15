# Minggu 15: Mini Project OOP & Panduan Studi Kasus

## 🎯 Capaian Pembelajaran (Sub-CPMK 6)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Menyusun ide proyek perangkat lunak berbasis OOP yang memecahkan masalah riil.
2. Menerapkan minimal 4 pilar OOP (*Encapsulation, Inheritance, Polymorphism, Abstraction*).
3. Menggunakan struktur data *Collections*, penanganan error *Exception Handling*, dan persistensi data *File Handling*.
4. Bekerja sama dalam tim atau mandiri untuk menyelesaikan *deliverable* aplikasi tepat waktu.

---

## 📋 Ketentuan Mini Project

### 1. Kriteria Wajib Proyek
Setiap kelompok/individu wajib memastikan aplikasinya memenuhi spesifikasi teknis berikut:
- **Paradigma OOP:** Menerapkan Class, Objek, dan 4 Pilar OOP.
- **Pewarisan & Polimorfisme:** Terdapat minimal 1 Superclass/Abstract Class/Interface dengan minimal 2 Subclass implementasi.
- **Collection Framework:** Menggunakan `ArrayList` atau `HashMap` untuk manajemen data dinamis di memori.
- **Exception Handling:** Menggunakan blok `try-catch` dan membuat minimal 1 *Custom Exception* untuk validasi bisnis.
- **File I/O:** Memiliki fitur penyimpanan dan pemuatan data dari berkas teks (`.txt` atau `.csv`).
- **Antarmuka:** Console CLI interaktif yang rapi atau GUI sederhana (Java Swing/JavaFX - opsional nilai tambah).

---

## 💡 Pilihan Topik Studi Kasus

Mahasiswa dapat memilih salah satu topik berikut (atau mengajukan topik mandiri dengan persetujuan dosen):

### Topik 1: Sistem Kasir & Point of Sale (POS) Toko Retail
- **Deskripsi:** Mengelola inventaris barang (Makanan, Elektronik, Pakaian), transaksi kasir, diskon member/non-member (Polymorphism), struk belanja, dan riwayat transaksi.
- **Poin Kunci:** Perhitungan pajak, diskon bertingkat, update stok otomatis, simpan transaksi ke CSV.

### Topik 2: Sistem Reservasi Hotel / Penginapan
- **Deskripsi:** Pengelolaan kamar (Standard, Deluxe, Suite), pemesanan oleh tamu, check-in, check-out, kalkulasi biaya menginap, serta cetak bukti reservasi.
- **Poin Kunci:** Validasi ketersediaan kamar, penanganan tanggal, exception kamar penuh.

### Topik 3: Sistem Rekam Medis & Antrian Klinik
- **Deskripsi:** Pendaftaran pasien (Umum, BPJS, Asuransi Swasta), dokter spesialis, antrian poli, resep obat, dan riwayat diagnosa pasien.
- **Poin Kunci:** Antrian prioritas, pencarian riwayat medis pasien berdasar NIK.

### Topik 4: Sistem Manajemen Rental Kendaraan
- **Deskripsi:** Rental mobil, motor, dan bus. Fitur tarif harian, denda keterlambatan, status perawatan kendaraan, dan laporan pendapatan.
- **Poin Kunci:** Hierarki class kendaraan, perhitungan denda berbasis hari, export laporan ke file.

---

## 📁 Struktur Repository Proyek yang Diharapkan

```
Proyek-OOP-[NamaKelompok]/
├── docs/
│   ├── class-diagram.png     # Class Diagram UML
│   └── README.md             # Panduan instalasi dan deskripsi fitur
├── src/
│   └── id/ac/uui/app/
│       ├── model/            # Class Entity/Model
│       ├── service/          # Business logic
│       ├── exception/        # Custom exceptions
│       ├── repository/       # File I/O handler
│       └── App.java          # Entry point utama
├── data/
│   └── database.csv          # File persistensi data
└── README.md
```

---

## ⏱️ Timeline Pengerjaan & Milestone

| Minggu | Kegiatan | Luaran (Deliverable) |
| :---: | :--- | :--- |
| **Minggu 14** | Pembentukan tim, pemilihan topik, dan perancangan UML Class Diagram | Dokumen proposal & rancangan class |
| **Minggu 15** | Implementasi kode utama, File I/O, Exception handling, dan konsultasi progres | Source code 80% siap & konsultasi |
| **Minggu 16** | *Code freeze*, pembuatan laporan singkat, dan **Presentasi Proyek (UAS)** | Demo aplikasi & presentasi |
