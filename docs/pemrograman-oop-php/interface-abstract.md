# Minggu 7: Abstraction (Interface dan Abstract Class)

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Mendefinisikan dan menerapkan **Abstract Class** dan **Abstract Method**.
2. Mendefinisikan dan mengimplementasikan **Interface** dengan `implements`.
3. Membedakan kapan menggunakan Abstract Class vs Interface.
4. Mengimplementasikan **Multiple Interface**.

---

## 1. Abstract Class

```php
<?php

abstract class BangunDatar
{
    public function __construct(protected string $nama) {}

    // Concrete method (punya implementasi)
    public function info(): void
    {
        echo "Bangun datar: {$this->nama}\n";
    }

    // Abstract method (WAJIB diimplementasikan subclass)
    abstract public function hitungLuas(): float;
    abstract public function hitungKeliling(): float;
}

class Lingkaran extends BangunDatar
{
    public function __construct(private float $jariJari)
    {
        parent::__construct("Lingkaran");
    }

    public function hitungLuas(): float
    {
        return M_PI * $this->jariJari ** 2;
    }

    public function hitungKeliling(): float
    {
        return 2 * M_PI * $this->jariJari;
    }
}

class Persegi extends BangunDatar
{
    public function __construct(private float $sisi)
    {
        parent::__construct("Persegi");
    }

    public function hitungLuas(): float
    {
        return $this->sisi ** 2;
    }

    public function hitungKeliling(): float
    {
        return 4 * $this->sisi;
    }
}
```

---

## 2. Interface

**Interface** mendefinisikan kontrak — semua method yang harus diimplementasikan oleh class yang meng-`implements`:

```php
<?php

interface Pembayaran
{
    public function bayar(float $nominal): void;
    public function cetakBukti(): string;
}

interface NotifikasiSMS
{
    public function kirimSMS(string $nomorHp, string $pesan): void;
}
```

### Multiple Interface Implementation:

```php
<?php

class TransaksiECommerce implements Pembayaran, NotifikasiSMS
{
    public function __construct(private string $idPesanan) {}

    public function bayar(float $nominal): void
    {
        echo "Pesanan {$this->idPesanan} dibayar Rp " . number_format($nominal) . "\n";
    }

    public function cetakBukti(): string
    {
        return "Bukti pembayaran order: {$this->idPesanan}";
    }

    public function kirimSMS(string $nomorHp, string $pesan): void
    {
        echo "SMS ke {$nomorHp}: {$pesan}\n";
    }
}
```

---

## 3. Perbandingan Abstract Class vs Interface

| Kriteria | Abstract Class | Interface |
| :--- | :--- | :--- |
| **Kata Kunci** | `abstract class` + `extends` | `interface` + `implements` |
| **Multiple** | ❌ (hanya 1 parent) | ✅ (bisa banyak interface) |
| **Properti** | Bisa punya properti biasa | Hanya konstanta (`const`) |
| **Method** | Campuran (abstract + concrete) | Semua abstract (kecuali `default` method) |
| **Constructor** | ✅ Bisa punya | ❌ Tidak bisa |
| **Tujuan** | Berbagi kode + kontrak (IS-A) | Kontrak perilaku murni (CAN-DO) |

---

## 4. Enum (PHP 8.1+)

PHP 8.1 memperkenalkan **Enum** — tipe data yang membatasi nilai ke sekumpulan opsi:

```php
<?php

enum StatusPesanan: string
{
    case Pending = 'pending';
    case Diproses = 'diproses';
    case Dikirim = 'dikirim';
    case Selesai = 'selesai';

    public function label(): string
    {
        return match($this) {
            self::Pending => '⏳ Menunggu',
            self::Diproses => '🔄 Sedang Diproses',
            self::Dikirim => '🚚 Dalam Pengiriman',
            self::Selesai => '✅ Selesai',
        };
    }
}

$status = StatusPesanan::Dikirim;
echo $status->label(); // 🚚 Dalam Pengiriman
```

---

## 📝 Tugas Praktikum

1. Buat interface `BisaTerbang` (method `terbang()`) dan `BisaBerenang` (method `berenang()`).
2. Buat abstract class `Hewan` dengan properti `$nama` dan abstract method `makan()`.
3. Buat class `Bebek` yang extends `Hewan` dan implements `BisaTerbang, BisaBerenang`.
4. Buat class `Penguin` yang extends `Hewan` dan hanya implements `BisaBerenang`.
5. Buat Enum `JenisHewan` dengan case `Domestik`, `Liar`, `Langka`.
