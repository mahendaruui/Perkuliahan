# Minggu 14: Implementasi dan Arsitektur Aplikasi OOP

## 🎯 Capaian Pembelajaran (Sub-CPMK 6)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Mengintegrasikan seluruh konsep OOP ke dalam aplikasi CLI PHP yang utuh.
2. Memahami pola arsitektur **Model-Service-Repository**.

---

## Studi Kasus: Sistem Perpustakaan Mini

### A. Model Entity
```php
<?php
// src/Model/Buku.php
namespace App\Model;

class Buku
{
    private bool $isDipinjam = false;

    public function __construct(
        public readonly string $isbn,
        public readonly string $judul,
        public readonly string $pengarang
    ) {}

    public function isDipinjam(): bool { return $this->isDipinjam; }
    public function setDipinjam(bool $status): void { $this->isDipinjam = $status; }

    public function __toString(): string
    {
        $status = $this->isDipinjam ? "Dipinjam" : "Tersedia";
        return "[{$this->isbn}] {$this->judul} - {$this->pengarang} ({$status})";
    }
}
```

### B. Custom Exception
```php
<?php
// src/Exception/PerpustakaanException.php
namespace App\Exception;

class PerpustakaanException extends \Exception {}
```

### C. Service Layer
```php
<?php
// src/Service/PerpustakaanService.php
namespace App\Service;

use App\Model\Buku;
use App\Exception\PerpustakaanException;

class PerpustakaanService
{
    /** @var Buku[] */
    private array $koleksi = [];

    public function tambahBuku(Buku $buku): void
    {
        if (isset($this->koleksi[$buku->isbn])) {
            throw new PerpustakaanException("ISBN {$buku->isbn} sudah terdaftar!");
        }
        $this->koleksi[$buku->isbn] = $buku;
    }

    /** @return Buku[] */
    public function getSemuaBuku(): array { return $this->koleksi; }

    public function pinjamBuku(string $isbn): void
    {
        if (!isset($this->koleksi[$isbn])) {
            throw new PerpustakaanException("Buku ISBN {$isbn} tidak ditemukan.");
        }
        $buku = $this->koleksi[$isbn];
        if ($buku->isDipinjam()) {
            throw new PerpustakaanException("Buku sedang dipinjam!");
        }
        $buku->setDipinjam(true);
    }
}
```

### D. Main Application
```php
<?php
// src/App.php
require_once __DIR__ . '/../vendor/autoload.php';

use App\Model\Buku;
use App\Service\PerpustakaanService;
use App\Exception\PerpustakaanException;

$service = new PerpustakaanService();

// Data awal
try {
    $service->tambahBuku(new Buku("B01", "Pemrograman PHP", "Lockhart"));
    $service->tambahBuku(new Buku("B02", "Clean Code", "Uncle Bob"));
} catch (PerpustakaanException $e) {}

while (true) {
    echo "\n=== SISTEM PERPUSTAKAAN ===\n";
    echo "1. Lihat Daftar Buku\n";
    echo "2. Tambah Buku\n";
    echo "3. Pinjam Buku\n";
    echo "4. Keluar\n";
    $opsi = trim(readline("Pilih: "));

    match($opsi) {
        '1' => (function() use ($service) {
            foreach ($service->getSemuaBuku() as $b) echo $b . "\n";
        })(),
        '2' => (function() use ($service) {
            try {
                $isbn = trim(readline("ISBN: "));
                $judul = trim(readline("Judul: "));
                $pengarang = trim(readline("Pengarang: "));
                $service->tambahBuku(new Buku($isbn, $judul, $pengarang));
                echo "✅ Berhasil!\n";
            } catch (PerpustakaanException $e) { echo "❌ {$e->getMessage()}\n"; }
        })(),
        '3' => (function() use ($service) {
            try {
                $isbn = trim(readline("ISBN: "));
                $service->pinjamBuku($isbn);
                echo "✅ Berhasil dipinjam!\n";
            } catch (PerpustakaanException $e) { echo "❌ {$e->getMessage()}\n"; }
        })(),
        '4' => exit("Terima kasih!\n"),
        default => echo "Pilihan tidak valid!\n",
    };
}
```

---

## 📝 Tugas Pengembangan

Tambahkan fitur: **Pengembalian Buku**, **Pencarian Buku**, dan **Simpan ke file JSON**.
