---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 1'
footer: 'Mahendar Dwi Payana, S.ST., M.T. • Universitas Ubudiyah Indonesia'
style: |
  section {
    background-color: #0f172a;
    color: #0f172a;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  h1 {
    color: #4f46e5;
  }
  h2 {
    color: #475569;
  }
  th {
    background-color: #e2e8f0;
    color: #0f172a;
  }
  td {
    background-color: #0f172a;
    color: #334155;
  }
  code {
    background-color: #e2e8f0;
    color: #4338ca;
  }
---

<!-- _class: lead -->
# Kontrak Perkuliahan & Pengantar OOP dengan PHP 8+
### IFR 214 • Bobot 3 SKS (T=2, P=1)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 1

1. **Kontrak Perkuliahan & Asesmen OBE** (CPL, CPMK, Bobot Nilai)
2. **Paradigma Pemrograman:** Transisi dari PHP Prosedural ke PHP Modern
3. **4 Pilar Fundamental OOP di PHP** (Encapsulation, Inheritance, Polymorphism, Abstraction)
4. **Fitur Mutakhir PHP 8+** (Constructor Promotion, Readonly, Enums, Union Types)
5. **Memodelkan Objek Nyata di PHP** (Class, Objek, Property, Method)
6. **Ekosistem Profesional:** Namespace & Composer (PSR-4 Autoloading)
7. **Tooling & Setup Lingkungan Lab** (PHP 8.1+, Composer, IDE)
8. **Tanya Jawab & Penugasan Eksplorasi**

---

## ⚖️ Kontrak Perkuliahan & Penilaian OBE

| Komponen Penilaian | Bobot (%) | Keterangan |
| :--- | :---: | :--- |
| **Kehadiran & Partisipasi** | **10%** | Minimal kehadiran 75% |
| **Tugas Individu** | **15%** | Latihan sintaks & pemahaman modul |
| **Tugas Kelompok / Studi Kasus** | **20%** | Case-Based Learning (CBL) |
| **Kuis Teori & Praktik** | **10%** | Evaluasi pemahaman berkala |
| **Ujian Tengah Semester (UTS)** | **20%** | Ujian tertulis & live coding |
| **UAS / Mini Project PHP OOP** | **25%** | Project-Based Learning (PjBL) |
| **Total** | **100%** | |

---

## 🔄 PHP Prosedural vs PHP Modern (OOP)

### 1. PHP Prosedural Tradisional (Legacy)
- Data dan fungsi terpisah (data mengalir bebas tanpa batasan).
- Mengandalkan fungsi global `function namaFungsi()`.
- Sulit di-maintain saat baris kode mencapai ribuan baris.
- Rawan konflik nama fungsi (*name collisions*).

### 2. PHP Berorientasi Objek Modern (PHP 8+)
- Data (properti) dan perilaku (method) dibungkus rapi dalam Class.
- Mendukung *Strict Type Checking*, *Readonly*, dan *Constructor Promotion*.
- Sangat modular, aman, dan mudah diuji dengan Unit Testing (PHPUnit).
- Fondasi mutlak framework enterprise (Laravel, Symfony).

---

## 🏛️ 4 Pilar Utama OOP di PHP

1. **🔒 Encapsulation (Pembungkusan):**
   Melindungi data dengan visibilitas `private`/`protected` dan `readonly`, akses melalui method getter/setter yang tervalidasi.

2. **🧬 Inheritance & Traits (Pewarisan):**
   Pewarisan sifat vertikal via `extends` dan pemanggilan `parent::`, serta pewarisan horizontal menggunakan **Trait**.

3. **🎭 Polymorphism (Banyak Bentuk):**
   Perilaku berbeda melalui *Method Overriding* dan *Type Hinting* berbasis Parent Class atau Interface.

4. **🧩 Abstraction (Abstraksi):**
   Memisahkan kontrak dan detail implementasi menggunakan `abstract class` dan `interface`.

---

## ⚡ Fitur Mutakhir PHP 8+ untuk OOP

- **Constructor Promotion (PHP 8.0):** Deklarasi properti langsung di parameter `__construct()`.
- **Union Types (PHP 8.0):** Parameter multi-tipe `int|float|string`.
- **Named Arguments (PHP 8.0):** Memanggil parameter fungsi sesuai namanya tanpa terikat urutan.
- **Enums (PHP 8.1):** Tipe data enumerasi native dengan fungsi helper.
- **Readonly Properties (PHP 8.1):** Properti yang immutable setelah inisialisasi.
- **Nullsafe Operator `?->` (PHP 8.0):** Mencegah fatal error saat membaca properti bertingkat yang bernilai `null`.

---

## 💻 Contoh Objek Nyata: Akun Bank di PHP 8+

```php
<?php
declare(strict_types=1);

class AkunBank {
    // PHP 8: Constructor Promotion + Readonly
    public function __construct(
        public readonly string $nomorRekening,
        public string $pemilik,
        private float $saldo = 0.0
    ) {}

    public function getSaldo(): float {
        return $this->saldo;
    }

    public function setor(float $jumlah): void {
        if ($jumlah <= 0) throw new InvalidArgumentException("Nominal harus > 0");
        $this->saldo += $jumlah;
    }
}
```

---

## 📦 Ekosistem: Namespace & Composer (PSR-4)

- **Namespace (`namespace App\Model;`):**
  Mengelompokkan class ke dalam modul hierarkis dan mencegah konflik nama.

- **Composer (`composer.json`):**
  Package manager standar industri PHP untuk mengelola dependensi pihak ketiga.

- **PSR-4 Autoloading:**
  Menghilangkan keharusan memanggil puluhan `require_once` secara manual — seluruh class otomatis dimuat oleh Composer!

```bash
composer init
composer dump-autoload
```

---

## 🛠️ Tooling & Persiapan Praktikum

### 1. PHP Runtime
- **PHP 8.1+ atau 8.2+** (XAMPP / Laragon / Homebrew)
- Periksa di terminal: `php -v`

### 2. Dependency Manager
- **Composer** (Unduh di [getcomposer.org](https://getcomposer.org))
- Periksa di terminal: `composer --version`

### 3. Editor & Ekstensi
- **VS Code:** Ekstensi *PHP Intelephense*, *PHP Debug*
- **PhpStorm** (Gratis via GitHub Student Developer Pack)

---

<!-- _class: lead -->
# Sesi Tanya Jawab & Diskusi 💬

### 📝 Persiapan Pertemuan 2:
- Pastikan PHP 8.1+ dan Composer sudah terpasang di laptop masing-masing.
- Kita akan langsung praktik membuat **Class, Object, Typed Properties, Constructor Promotion**, dan memahami variabel `$this`.

**Portal Bahan Ajar PHP OOP:**  
https://mahendar.github.io/Perkuliahan/pemrograman-oop-php/
