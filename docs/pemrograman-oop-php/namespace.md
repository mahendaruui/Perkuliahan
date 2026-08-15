# Minggu 9: Namespace dan Autoloading (Composer)

## 🎯 Capaian Pembelajaran (Sub-CPMK 4)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Memahami konsep **Namespace** untuk menghindari konflik nama class.
2. Menggunakan **`use`** statement untuk mengimpor class dari namespace lain.
3. Mengatur **Autoloading PSR-4** dengan **Composer**.
4. Menyusun struktur folder project PHP yang profesional.

---

## 1. Apa itu Namespace?

**Namespace** di PHP mirip konsep *package* di Java — mengelompokkan class ke dalam ruang nama hierarkis untuk menghindari bentrok nama.

```php
<?php
// File: src/Model/Mahasiswa.php
namespace App\Model;

class Mahasiswa
{
    public function __construct(
        public readonly string $nim,
        public string $nama,
        public float $ipk = 0.0
    ) {}

    public function tampilkan(): void
    {
        echo "{$this->nim} - {$this->nama} (IPK: {$this->ipk})\n";
    }
}
```

### Menggunakan Class dari Namespace Lain:
```php
<?php
// File: src/Main.php
namespace App;

use App\Model\Mahasiswa;

$mhs = new Mahasiswa("240101", "Fajar", 3.80);
$mhs->tampilkan();
```

---

## 2. Autoloading dengan Composer (PSR-4)

### Setup Composer:
```bash
# Inisialisasi Composer di root project
composer init

# Struktur folder
src/
├── Model/
│   ├── Mahasiswa.php
│   └── Dosen.php
├── Service/
│   └── AkademikService.php
└── App.php
composer.json
```

### Konfigurasi `composer.json`:
```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

### Generate Autoloader:
```bash
composer dump-autoload
```

### Penggunaan:
```php
<?php
// File: src/App.php
require_once __DIR__ . '/../vendor/autoload.php';

use App\Model\Mahasiswa;
use App\Service\AkademikService;

$mhs = new Mahasiswa("240101", "Budi");
```

---

## 📝 Latihan Praktik

1. Buat proyek dengan Composer dan struktur namespace `App\Entity`, `App\Service`, `App\Util`.
2. Buat class `Buku` di namespace `App\Entity` dan `PeminjamanService` di `App\Service`.
3. Hubungkan semuanya menggunakan PSR-4 autoloading.
