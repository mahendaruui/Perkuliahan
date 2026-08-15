# Minggu 5: Inheritance (Pewarisan)

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Menerapkan kata kunci **`extends`** untuk pewarisan class.
2. Menggunakan **`parent::`** untuk memanggil constructor/method induk.
3. Memahami dan menerapkan **Trait** sebagai solusi *code reuse* tanpa multiple inheritance.

---

## 1. Pewarisan dengan `extends`

```php
<?php

// Superclass (Parent)
class Kendaraan
{
    public function __construct(
        protected string $merk,
        protected int $tahunProduksi
    ) {}

    public function infoKendaraan(): void
    {
        echo "Merk: {$this->merk} | Tahun: {$this->tahunProduksi}\n";
    }

    public function klakson(): void
    {
        echo "Tin tin!\n";
    }
}

// Subclass (Child)
class Mobil extends Kendaraan
{
    public function __construct(
        string $merk,
        int $tahunProduksi,
        private int $jumlahPintu
    ) {
        // Panggil constructor parent
        parent::__construct($merk, $tahunProduksi);
    }

    // Override method parent
    public function infoKendaraan(): void
    {
        parent::infoKendaraan();
        echo "Jumlah Pintu: {$this->jumlahPintu}\n";
    }

    public function nyalakanAC(): void
    {
        echo "AC Mobil {$this->merk} dinyalakan.\n";
    }
}
```

---

## 2. Trait: Code Reuse Tanpa Multiple Inheritance

PHP tidak mendukung multiple inheritance, tetapi menyediakan **Trait** — blok kode yang bisa di-*use* di banyak class:

```php
<?php

trait Loggable
{
    public function log(string $pesan): void
    {
        $waktu = date('Y-m-d H:i:s');
        echo "[{$waktu}] {$pesan}\n";
    }
}

trait Searchable
{
    public function cari(string $keyword): void
    {
        echo "Mencari '{$keyword}' di " . static::class . "...\n";
    }
}

class Produk
{
    use Loggable, Searchable; // Menggunakan 2 trait sekaligus

    public function __construct(
        public string $nama,
        public float $harga
    ) {
        $this->log("Produk '{$nama}' dibuat.");
    }
}

$p = new Produk("Laptop", 12_000_000);
$p->cari("Laptop");
```

---

## 3. Studi Kasus: Hirarki Karyawan

```php
<?php

class Karyawan
{
    public function __construct(
        protected string $nip,
        protected string $nama,
        protected float $gajiPokok
    ) {}

    public function hitungTotalGaji(): float
    {
        return $this->gajiPokok;
    }

    public function tampilkanProfil(): void
    {
        echo "NIP  : {$this->nip}\n";
        echo "Nama : {$this->nama}\n";
        echo "Total: Rp " . number_format($this->hitungTotalGaji()) . "\n\n";
    }
}

class Manager extends Karyawan
{
    public function __construct(
        string $nip, string $nama, float $gajiPokok,
        private float $tunjanganJabatan
    ) {
        parent::__construct($nip, $nama, $gajiPokok);
    }

    public function hitungTotalGaji(): float
    {
        return $this->gajiPokok + $this->tunjanganJabatan;
    }
}

class Programmer extends Karyawan
{
    public function __construct(
        string $nip, string $nama, float $gajiPokok,
        private float $bonusProyek
    ) {
        parent::__construct($nip, $nama, $gajiPokok);
    }

    public function hitungTotalGaji(): float
    {
        return $this->gajiPokok + $this->bonusProyek;
    }
}
```

---

## 4. Keyword `final`

Gunakan `final` untuk mencegah class diwarisi atau method di-override:

```php
final class Konfigurasi
{
    // Class ini TIDAK bisa di-extends
}

class Hewan
{
    final public function bernapas(): void
    {
        // Method ini TIDAK bisa di-override oleh child class
        echo "Bernapas...\n";
    }
}
```

---

## 📝 Tugas Praktikum

1. Buat class `Bentuk` (parent) dengan method `hitungLuas()` dan `hitungKeliling()`.
2. Buat subclass `Persegi` dan `Lingkaran` yang meng-override kedua method tersebut.
3. Buat trait `Printable` dengan method `cetak()` yang menampilkan info objek.
4. Gunakan trait tersebut di kedua subclass, lalu uji di `main.php`.
