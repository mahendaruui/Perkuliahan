# Minggu 6: Polymorphism (Polimorfisme)

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Memahami **Polymorphism** dalam konteks PHP.
2. Menerapkan **Method Overriding** dengan anotasi konsisten.
3. Menggunakan **Type Hinting** dan **Union Types** (PHP 8.0+).
4. Memanfaatkan **Upcasting** dan operator `instanceof`.

---

## 1. Polymorphism di PHP

PHP tidak mendukung **method overloading** (beberapa method dengan nama sama tapi parameter berbeda) seperti Java. Di PHP, polymorphism dicapai melalui:
1. **Method Overriding** — Subclass menyediakan implementasi spesifik.
2. **Type Hinting** pada parameter — Menerima parent class/interface sebagai tipe.

---

## 2. Method Overriding

```php
<?php

class Hewan
{
    public function bersuara(): string
    {
        return "Hewan mengeluarkan suara umum...";
    }
}

class Kucing extends Hewan
{
    public function bersuara(): string
    {
        return "Kucing: Meong... meong...";
    }
}

class Anjing extends Hewan
{
    public function bersuara(): string
    {
        return "Anjing: Guk... guk!";
    }
}

class Burung extends Hewan
{
    public function bersuara(): string
    {
        return "Burung: Cicit cuit...";
    }
}
```

---

## 3. Array Polimorfik & Type Hinting

```php
<?php

function periksaHewan(Hewan $h): void
{
    // PHP otomatis memanggil method milik objek asli (Dynamic Dispatch)
    echo $h->bersuara() . "\n";
}

// Upcasting: variabel bertipe Hewan menampung objek subclass
$kebunBinatang = [
    new Kucing(),
    new Anjing(),
    new Burung(),
    new Kucing(),
];

echo "--- Kebun Binatang ---\n";
foreach ($kebunBinatang as $hewan) {
    periksaHewan($hewan);
}
```

Output:
```text
--- Kebun Binatang ---
Kucing: Meong... meong...
Anjing: Guk... guk!
Burung: Cicit cuit...
Kucing: Meong... meong...
```

---

## 4. Operator `instanceof`

```php
<?php

class DokterHewan
{
    public function obati(Hewan $h): void
    {
        echo "Dokter memeriksa pasien...\n";
        echo $h->bersuara() . "\n";

        if ($h instanceof Kucing) {
            echo "-> Berikan vaksin khusus kucing.\n";
        } elseif ($h instanceof Anjing) {
            echo "-> Cek rabies & kebersihan telinga.\n";
        }
    }
}
```

---

## 5. Union Types & Intersection Types (PHP 8.0+)

```php
<?php

// Union Types: parameter bisa menerima int ATAU float
function hitungDiskon(int|float $harga, float $persen): float
{
    return $harga * ($persen / 100);
}

// Nullable type (shorthand: ?Type)
function cariMahasiswa(string $nim): ?Mahasiswa
{
    // return null jika tidak ditemukan
    return null;
}
```

---

## 6. Studi Kasus: Sistem Pembayaran

```php
<?php

class MetodePembayaran
{
    public function __construct(protected float $jumlah) {}

    public function prosesPembayaran(): string
    {
        return "Memproses pembayaran Rp " . number_format($this->jumlah);
    }
}

class TransferBank extends MetodePembayaran
{
    public function __construct(float $jumlah, private string $noRekening)
    {
        parent::__construct($jumlah);
    }

    public function prosesPembayaran(): string
    {
        return "Transfer ke {$this->noRekening}: Rp " . number_format($this->jumlah) . " [SUKSES]";
    }
}

class PembayaranQris extends MetodePembayaran
{
    public function __construct(float $jumlah, private string $idTransaksi)
    {
        parent::__construct($jumlah);
    }

    public function prosesPembayaran(): string
    {
        return "QRIS {$this->idTransaksi}: Rp " . number_format($this->jumlah) . " [LUNAS]";
    }
}

// Polimorfisme dalam aksi
$pembayaran = [
    new TransferBank(500_000, "BCA-123456"),
    new PembayaranQris(150_000, "TRX-A001"),
    new TransferBank(2_000_000, "BNI-789012"),
];

foreach ($pembayaran as $p) {
    echo $p->prosesPembayaran() . "\n";
}
```

---

## 📝 Tugas Praktikum

1. Buat class `AkunBank` dengan method `hitungBungaBulanan()`.
2. Buat subclass `TabunganBiasa` (bunga 1%/tahun), `Deposito` (5%/tahun), `TabunganSyariah` (nisbah).
3. Buat program yang menyimpan ketiga jenis akun dalam array `$daftarAkun` dan cetak bunga masing-masing menggunakan loop polimorfik.
