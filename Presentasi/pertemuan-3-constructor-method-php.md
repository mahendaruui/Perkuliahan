---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 3'
footer: 'Mahendar Dwi Payana, S.ST., M.T. • Universitas Ubudiyah Indonesia'
style: |
  section {
    background-color: #0f172a;
    color: #f8fafc;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  h1 {
    color: #818cf8;
  }
  h2 {
    color: #94a3b8;
  }
  th {
    background-color: #1e293b;
    color: #ffffff;
  }
  td {
    background-color: #0f172a;
    color: #cbd5e1;
  }
  code {
    background-color: #1e293b;
    color: #a5b4fc;
  }
---

<!-- _class: lead -->
# Constructor, Method & Static di PHP 8+
### Pertemuan 3 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 3

1. **Peran Magic Method `__construct()`** dalam Inisialisasi Objek
2. **Revolusi PHP 8.0: Constructor Property Promotion**
3. **Named Arguments & Default Parameter Values**
4. **Siklus Pelepasan Resource:** Magic Method `__destruct()`
5. **Type Declarations & Union Types (`int|float`)** pada Method
6. **Static Member (`self::` & `static::`)** Tingkat Class
7. **Pola Desain Static Factory Method**
8. **Studi Kasus & Latihan Praktikum Mandiri**

---

## 🛠️ Mengapa Kita Membutuhkan Constructor?

- **Tanpa Constructor:** Objek rentan dibuat dalam kondisi kosong / tidak lengkap (*uninitialized state*).
- **Dengan Constructor:** Memaksa pengembang memberikan data wajib sejak saat objek pertama kali diinstansiasi dengan `new`.

```php
// Constructor memaksa inisialisasi nomor rekening dan nama pemilik
$rek = new RekeningBank(
    nomorRekening: "123-456",
    pemilik: "Budi Santoso",
    saldoAwal: 500_000
);
```

---

## 🚀 Revolusi PHP 8: Constructor Property Promotion

### ❌ PHP 7 (16 Baris Boilerplate):
```php
class User {
    public string $id;
    public string $nama;
    public function __construct(string $id, string $nama) {
        $this->id = $id;
        $this->nama = $nama;
    }
}
```

### ✅ PHP 8+ (5 Baris Bersih):
```php
class User {
    public function __construct(
        public readonly string $id,
        public string $nama
    ) {}
}
```

---

## 🎯 Named Arguments di PHP 8

Memanggil parameter constructor/method berdasarkan nama parameter eksplisit (urutan bebas):

```php
class Produk {
    public function __construct(
        public string $nama,
        public float $harga,
        public int $stok = 0,
        public string $kategori = "Umum"
    ) {}
}

// Urutan bebas & parameter default ($stok) bisa dilewati
$p = new Produk(
    kategori: "Elektronik",
    harga: 12_500_000,
    nama: "Monitor LG 27 Inch"
);
```

---

## 🧹 Destructor: `__destruct()`

Method yang otomatis dieksekusi saat siklus hidup objek berakhir:

```php
class KoneksiDatabase {
    public function __construct(private string $host) {
        echo "🔌 Koneksi ke {$this->host} dibuka.\n";
    }

    public function __destruct() {
        echo "🔒 Koneksi ke {$this->host} ditutup otomatis.\n";
    }
}

$db = new KoneksiDatabase("localhost:3306");
// Saat script selesai dieksekusi, destructor otomatis jalan!
```

---

## 🛡️ Type Declarations & Union Types

```php
declare(strict_types=1);

class KalkulatorKeuangan {
    // Union Type (int|float): Menerima integer ATAU float
    public function hitungPajak(int|float $nominal, float $persen): float {
        return $nominal * ($persen / 100);
    }

    // Nullable Type (?string): Boleh mengembalikan string atau null
    public function cariVoucher(string $kode): ?string {
        return ($kode === "HEMAT50") ? "Diskon 50%" : null;
    }
}
```

---

## ⚡ Static Member (`self::`)

Member yang terikat pada Class itu sendiri (tidak membutuhkan objek instance):

```php
class KursValuta {
    public static float $kursUsd = 16_200.0;

    public static function usdKeIdr(float $usd): float {
        return $usd * self::$kursUsd;
    }
}

// Panggil langsung via Class tanpa new:
echo KursValuta::usdKeIdr(100); // 1.620.000
```

---

## 🏭 Pola Static Factory Method

Alternatif elegan multiple constructor di PHP:

```php
class User {
    private function __construct(
        public string $username,
        public string $role
    ) {}

    public static function createMember(string $username): self {
        return new self($username, "Member");
    }

    public static function createAdmin(string $username): self {
        return new self($username, "SuperAdmin");
    }
}

$user = User::createMember("budi99");
$admin = User::createAdmin("admin_pusat");
```

---

<!-- _class: lead -->
# Sesi Praktikum & Tanya Jawab 💬

### 📝 Tugas Praktikum Mandiri:
1. Buat class `Karyawan` menggunakan **Constructor Property Promotion**.
2. Buat static factory method `buatStaff($id, $nama)` (gaji: 4.5jt) dan `buatManager($id, $nama)` (gaji: 9jt).
3. Instansiasi objek menggunakan Named Arguments dan cetak profilnya.

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/constructor-method
