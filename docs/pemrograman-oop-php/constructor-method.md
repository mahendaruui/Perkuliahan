# Minggu 3: Constructor dan Method

## 🎯 Capaian Pembelajaran (Sub-CPMK 2)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Memahami fungsi **Constructor** (`__construct`) dan **Destructor** (`__destruct`).
2. Menerapkan **Constructor Promotion** (PHP 8.0+) untuk penulisan yang lebih ringkas.
3. Memahami perbedaan **method biasa** dan **static method**.
4. Mengimplementasikan method dengan return type dan parameter type hints.

---

## 1. Constructor: `__construct()`

**Constructor** adalah method khusus yang otomatis dipanggil saat objek diinstansiasi (`new`). Di PHP, constructor dideklarasikan dengan nama magic method `__construct()`.

```php
<?php

class RekeningBank
{
    public string $nomorRekening;
    public string $pemilik;
    public float $saldo;

    // Constructor klasik
    public function __construct(string $nomorRekening, string $pemilik, float $saldoAwal = 0)
    {
        $this->nomorRekening = $nomorRekening;
        $this->pemilik = $pemilik;
        $this->saldo = $saldoAwal;
    }
}

// Pemakaian
$rek1 = new RekeningBank("123456", "Budi", 500000);
$rek2 = new RekeningBank("789012", "Siti"); // saldo default = 0
```

---

## 2. Constructor Promotion (PHP 8.0+)

PHP 8 memperkenalkan fitur **Constructor Promotion** — deklarasi properti langsung di parameter constructor, sehingga kode jauh lebih ringkas:

```php
<?php

class RekeningBank
{
    // Properti otomatis dideklarasikan dari parameter constructor
    public function __construct(
        public string $nomorRekening,
        public string $pemilik,
        public float $saldo = 0
    ) {}
}

$rek = new RekeningBank("123456", "Budi", 500000);
echo $rek->pemilik; // Output: Budi
```

> [!TIP]
> Constructor Promotion sangat dianjurkan di PHP 8+ karena mengurangi boilerplate code secara signifikan.

---

## 3. Destructor: `__destruct()`

**Destructor** dipanggil otomatis saat objek dihancurkan atau skrip selesai dieksekusi:

```php
<?php

class KoneksiDatabase
{
    public function __construct(private string $host)
    {
        echo "Koneksi ke {$this->host} dibuka.\n";
    }

    public function __destruct()
    {
        echo "Koneksi ke {$this->host} ditutup.\n";
    }
}

$db = new KoneksiDatabase("localhost");
// ... kode lainnya ...
// Saat script selesai: "Koneksi ke localhost ditutup."
```

---

## 4. Method dengan Type Hints & Return Type

PHP modern mendukung **type declaration** pada parameter dan return value:

```php
<?php

class Kalkulator
{
    // Method dengan return type int
    public function tambah(int $a, int $b): int
    {
        return $a + $b;
    }

    // Method dengan return type float
    public function bagi(float $a, float $b): float
    {
        if ($b == 0) {
            throw new \DivisionByZeroError("Tidak bisa membagi dengan nol!");
        }
        return $a / $b;
    }

    // Method void (tidak mengembalikan nilai)
    public function tampilkanHasil(string $operasi, float $hasil): void
    {
        echo "Hasil {$operasi}: {$hasil}\n";
    }
}
```

---

## 5. Static Method & Static Property

**Static member** milik Class secara keseluruhan — bisa diakses tanpa membuat objek menggunakan operator `::`:

```php
<?php

class KonversiSuhu
{
    // Konstanta class
    public const FAKTOR_REAMUR = 0.8;

    // Static method
    public static function celciusKeFahrenheit(float $celcius): float
    {
        return ($celcius * 9 / 5) + 32;
    }

    public static function celciusKeReamur(float $celcius): float
    {
        return $celcius * self::FAKTOR_REAMUR;
    }
}

// Akses tanpa membuat objek (menggunakan ::)
echo KonversiSuhu::celciusKeFahrenheit(100); // 212
echo KonversiSuhu::celciusKeReamur(100);     // 80
```

---

## 6. Named Arguments (PHP 8.0+)

PHP 8 mendukung pemanggilan fungsi/constructor dengan menyebutkan nama parameter:

```php
<?php

class Produk
{
    public function __construct(
        public string $nama,
        public float $harga,
        public int $stok = 0,
        public string $kategori = 'Umum'
    ) {}
}

// Named arguments — urutan bebas!
$produk = new Produk(
    nama: "Laptop ASUS",
    harga: 12_500_000,
    kategori: "Elektronik",
    stok: 15
);
```

---

## 📝 Tugas Praktikum

1. Buat class `AkunPengguna` menggunakan **Constructor Promotion** dengan properti: `$username`, `$email`, `$statusAktif` (bool), dan `$role` (string, default "User").
2. Tambahkan static method `buatAdmin(string $username, string $email)` yang mengembalikan objek `AkunPengguna` dengan `$role = "Admin"`.
3. Tambahkan method `tampilkanProfil()` untuk menampilkan semua informasi akun.
4. Uji program di file `main.php` — buat 1 user biasa dan 1 admin menggunakan static method.
