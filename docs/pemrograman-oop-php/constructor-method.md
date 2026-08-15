# Minggu 3: Constructor, Method, dan Static di PHP 8+

## 🎯 Capaian Pembelajaran (Sub-CPMK 2)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Memahami siklus hidup objek melalui magic method **`__construct()`** dan **`__destruct()`**.
2. Menerapkan fitur revolusioner **Constructor Property Promotion** di PHP 8.0+.
3. Menggunakan **Named Arguments** dan **Default Parameter Values** saat instansiasi objek.
4. Mendeklarasikan **Type Hints, Return Types**, dan **Union Types** pada method.
5. Memahami konsep **Static Properties & Static Methods** (`self::`, `static::`) serta pola *Static Factory Method*.

> [!TIP]
> 📽️ **Slide Presentasi Perkuliahan:** Anda dapat melihat dan memutar [Slide Interaktif Pertemuan 3 PHP](/presentasi/pertemuan-3-php) atau [Buka Layar Penuh (Tab Baru)](/Perkuliahan/presentasi/pertemuan-3-constructor-method-php.html){target="_blank"}.

---

## 1. Magic Method `__construct()`

**Constructor** adalah method spesial yang otomatis dieksekusi saat operator `new` dipanggil untuk menginisialisasi nilai awal (*state*) objek.

```php
<?php
declare(strict_types=1);

// Cara Tradisional (PHP 5/7)
class RekeningLama
{
    public string $nomorRekening;
    public string $pemilik;
    public float $saldo;

    public function __construct(string $nomorRekening, string $pemilik, float $saldoAwal = 0.0)
    {
        $this->nomorRekening = $nomorRekening;
        $this->pemilik = $pemilik;
        $this->saldo = $saldoAwal;
    }
}
```

---

## 2. Constructor Property Promotion (PHP 8.0+)

Di PHP 8+, Anda dapat menggabungkan **deklarasi properti, parameter constructor, dan assignment** menjadi satu baris yang sangat elegan:

```php
<?php
declare(strict_types=1);

class RekeningBank
{
    // Properti otomatis dibuat & diisi langsung dari parameter constructor!
    public function __construct(
        public readonly string $nomorRekening,
        public string $pemilik,
        public float $saldo = 0.0
    ) {}
}

$rek = new RekeningBank("12345678", "Budi Santoso", 500_000);
echo $rek->pemilik; // Output: Budi Santoso
```

---

## 3. Named Arguments (PHP 8.0+)

Dengan *Named Arguments*, pemanggilan method/constructor dapat menyebutkan nama parameternya secara eksplisit, sehingga **urutan parameter menjadi bebas**:

```php
<?php

class Pelanggan
{
    public function __construct(
        public string $nama,
        public string $email,
        public string $kota = "Banda Aceh",
        public bool $isMember = false
    ) {}
}

// Urutan parameter bebas karena menyebutkan namanya!
$p = new Pelanggan(
    email: "budi@email.com",
    nama: "Budi Pratama",
    isMember: true
);
```

---

## 4. Destructor: `__destruct()`

**Destructor** dipanggil otomatis saat objek tidak lagi memiliki referensi di memori atau saat skrip PHP selesai dieksekusi. Umumnya digunakan untuk melepaskan resource (menutup koneksi database, menghapus temporary file, atau mencatat log sesi).

```php
<?php

class SesiDatabase
{
    public function __construct(private string $koneksi)
    {
        echo "🔌 Koneksi ke {$this->koneksi} dibuka.\n";
    }

    public function __destruct()
    {
        echo "🔒 Koneksi ke {$this->koneksi} ditutup secara otomatis.\n";
    }
}

$db = new SesiDatabase("MySQL-Perkuliahan");
// Saat skrip selesai: "Koneksi ke MySQL-Perkuliahan ditutup secara otomatis."
```

---

## 5. Method Type Declarations & Union Types

```php
<?php

class Kalkulator
{
    // Union Type: $a dan $b bisa menerima tipe int ATAU float
    public function tambah(int|float $a, int|float $b): int|float
    {
        return $a + $b;
    }

    // Method void: Tidak mengembalikan nilai
    public function cetakHasil(string $label, float $nilai): void
    {
        echo "{$label}: " . number_format($nilai, 2) . "\n";
    }
}
```

---

## 6. Static Methods & Static Properties (`self::`)

Member `static` terikat pada **Class itu sendiri**, bukan pada instance objek tertentu. Diakses menggunakan operator scope resolution (`::`):

```php
<?php

class KonversiMataUang
{
    // Static Property (Konstanta kurs)
    public static float $kursUsdKeIdr = 16_200.0;

    // Static Method (Fungsi utilitas tanpa perlu membuat objek)
    public static function usdKeIdr(float $usd): float
    {
        return $usd * self::$kursUsdKeIdr;
    }

    public static function idrKeUsd(float $idr): float
    {
        return $idr / self::$kursUsdKeIdr;
    }
}

// Akses langsung lewat Class
echo "100 USD = Rp " . number_format(KonversiMataUang::usdKeIdr(100), 0, ',', '.');
```

---

## 7. Pola Static Factory Method

Karena PHP tidak mendukung multiple constructor, *Static Factory Method* adalah solusi standar industri untuk membuat objek dengan berbagai konfigurasi:

```php
<?php

class User
{
    private function __construct(
        public string $username,
        public string $email,
        public string $role
    ) {}

    // Factory 1: Membuat akun Member biasa
    public static function createMember(string $username, string $email): self
    {
        return new self($username, $email, 'Member');
    }

    // Factory 2: Membuat akun Administrator
    public static function createAdmin(string $username, string $email): self
    {
        return new self($username, $email, 'SuperAdmin');
    }
}

$user1 = User::createMember("budi99", "budi@mail.com");
$admin = User::createAdmin("admin_pusat", "admin@uui.ac.id");
```

---

## 📝 Tugas Praktikum Mandiri

1. Buat class `Karyawan` menggunakan **Constructor Property Promotion** dengan properti:
   - `$idKaryawan` (string, readonly)
   - `$nama` (string)
   - `$divisi` (string)
   - `$gajiPokok` (float)
   - `$jamLembur` (int, default 0)
2. Sediakan static method `buatStaffBaru(string $id, string $nama, string $divisi)` yang mengembalikan objek `Karyawan` dengan gaji pokok default Rp 4.500.000.
3. Sediakan static method `buatManager(string $id, string $nama)` dengan divisi "Manajerial" dan gaji pokok default Rp 9.000.000.
4. Buat file `main.php` untuk mendemonstrasikan pembuatan kedua karyawan tersebut menggunakan *Static Factory Method* dan *Named Arguments*!
