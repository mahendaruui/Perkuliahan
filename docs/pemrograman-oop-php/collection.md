# Minggu 11: PHP Collections & Array Functions

## 🎯 Capaian Pembelajaran (Sub-CPMK 4)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Menguasai **PHP Array** sebagai struktur data utama (indexed, associative, multidimensional).
2. Menggunakan fungsi-fungsi array bawaan PHP untuk manipulasi data.
3. Membangun pola **Collection Object** sederhana menggunakan OOP.

---

## 1. Array di PHP (Review & Lanjutan)

PHP memiliki array yang sangat fleksibel — berperan sebagai list, map, stack, dan queue sekaligus.

### Indexed Array:
```php
$buah = ["Apel", "Mangga", "Jeruk"];
$buah[] = "Semangka"; // Tambah elemen
```

### Associative Array (seperti HashMap):
```php
$mahasiswa = [
    "2401001" => "Budi Santoso",
    "2401002" => "Siti Aminah",
    "2401003" => "Andi Wijaya",
];

echo $mahasiswa["2401002"]; // Siti Aminah
```

---

## 2. Fungsi Array yang Penting

```php
<?php

$nilai = [85, 72, 90, 65, 78, 95, 88];

// Sorting
sort($nilai);                    // [65, 72, 78, 85, 88, 90, 95]
rsort($nilai);                   // Descending

// Filtering
$lulusCumLaude = array_filter($nilai, fn($n) => $n >= 85);
// [85, 88, 90, 95]

// Mapping (transformasi)
$nilaiHuruf = array_map(function($n) {
    return match(true) {
        $n >= 85 => 'A',
        $n >= 70 => 'B',
        $n >= 55 => 'C',
        default  => 'D',
    };
}, $nilai);

// Reduce (akumulasi)
$total = array_reduce($nilai, fn($carry, $item) => $carry + $item, 0);
$rataRata = $total / count($nilai);
```

---

## 3. Koleksi Objek (Object Collection Pattern)

```php
<?php

class Produk
{
    public function __construct(
        public readonly string $id,
        public string $nama,
        public float $harga,
        public int $stok
    ) {}

    public function __toString(): string
    {
        return "[{$this->id}] {$this->nama} - Rp " . number_format($this->harga) . " ({$this->stok} pcs)";
    }
}

class KoleksiProduk
{
    /** @var Produk[] */
    private array $items = [];

    public function tambah(Produk $produk): void
    {
        $this->items[$produk->id] = $produk;
    }

    public function cariById(string $id): ?Produk
    {
        return $this->items[$id] ?? null;
    }

    public function semua(): array
    {
        return $this->items;
    }

    public function totalNilaiStok(): float
    {
        return array_reduce($this->items, function(float $total, Produk $p) {
            return $total + ($p->harga * $p->stok);
        }, 0);
    }

    public function filterByMinHarga(float $min): array
    {
        return array_filter($this->items, fn(Produk $p) => $p->harga >= $min);
    }
}

// Penggunaan
$inventaris = new KoleksiProduk();
$inventaris->tambah(new Produk("P01", "Laptop ASUS", 12_500_000, 5));
$inventaris->tambah(new Produk("P02", "Mouse Logitech", 350_000, 20));
$inventaris->tambah(new Produk("P03", "Monitor LG 24\"", 2_800_000, 8));

foreach ($inventaris->semua() as $p) {
    echo $p . "\n";
}

echo "\nTotal Nilai Stok: Rp " . number_format($inventaris->totalNilaiStok()) . "\n";
```

---

## 📝 Tugas Praktikum

1. Buat class `Mahasiswa` dan class `DaftarMahasiswa` (Collection).
2. Implementasikan fitur: tambah, cari berdasarkan NIM, filter IPK cumlaude ($\ge$ 3.50), urutkan berdasarkan IPK (tertinggi dulu).
