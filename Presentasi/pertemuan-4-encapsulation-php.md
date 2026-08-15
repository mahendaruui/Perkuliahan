---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 4'
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
# Encapsulation, Visibility & Readonly di PHP 8+
### Pertemuan 4 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 4

1. **Pilar 1 OOP: Filosofi Encapsulation & Information Hiding**
2. **3 Tingkat Visibility Modifiers:** `public`, `protected`, `private`
3. **Getter & Setter dengan Aturan Validasi Bisnis**
4. **Fitur PHP 8.1: Readonly Properties** & Immutability
5. **Fitur PHP 8.2: Readonly Classes** (Data Transfer Objects / DTO)
6. **Magic Methods `__get()` dan `__set()`**
7. **Studi Kasus Praktikum: Keamanan Dompet Digital (E-Wallet)**
8. **Tugas Praktikum Mandiri:** Class `NilaiAkademik`

---

## 💊 Pilar 1: Filosofi Encapsulation

```
┌────────────────────────────────────────────────────────┐
│  CLASS ENCAPSULATION (KAPSUL PELINDUNG)                │
│                                                        │
│   🔒 DATA RAHASIA (Private)                             │
│   • Saldo Rekening                                     │
│   • PIN / Password                                     │
│                                                        │
│   🔑 METODE AKSES (Public)                              │
│   • getSaldo()                                         │
│   • transfer(pin, nominal, tujuan)                     │
└────────────────────────────────────────────────────────┘
```

**Encapsulation:** Membungkus atribut dan method menjadi satu unit utuh dan menyembunyikan data internal dari akses langsung di luar class (*Information Hiding*).

---

## 🔑 Tiga Visibility Modifiers di PHP

| Modifier | Dari Class Sendiri | Dari Child Class | Dari Luar Class |
| :--- | :---: | :---: | :---: |
| **`public`** | ✅ Ya | ✅ Ya | ✅ Ya (Bebas diakses) |
| **`protected`** | ✅ Ya | ✅ Ya | ❌ Ditolak (Error) |
| **`private`** | ✅ Ya | ❌ Ditolak (Error) | ❌ Ditolak (Error) |

> **Prinsip Utama:** Properti harus berstatus `private` atau `protected` secara default, dan dimanipulasi lewat method publik tervalidasi.

---

## 🛡️ Getter dan Setter dengan Validasi

```php
class Pasien {
    private int $umur = 0;

    public function getUmur(): int {
        return $this->umur;
    }

    public function setUmur(int $umur): void {
        // Validasi logika bisnis
        if ($umur < 0 || $umur > 130) {
            throw new InvalidArgumentException("Umur tidak valid!");
        }
        $this->umur = $umur;
    }
}
```

---

## 🧊 Readonly Properties (PHP 8.1+)

Properti yang **hanya bisa diisi 1 kali** saat constructor dijalankan, setelah itu menjadi *immutable*:

```php
class Mahasiswa {
    public function __construct(
        public readonly string $nim,  // Bebas dibaca, mustahil diubah
        public readonly string $nama,
        private float $ipk = 0.0
    ) {}
}

$mhs = new Mahasiswa("240101", "Ahmad");
echo $mhs->nim; // ✅ Boleh dibaca

// $mhs->nim = "999999"; 
// 💥 Error: Cannot modify readonly property
```

---

## 📦 Readonly Classes (PHP 8.2+)

Seluruh properti dalam class otomatis berstatus `readonly`:

```php
readonly class DataPenggunaDTO {
    public function __construct(
        public string $userId,
        public string $email,
        public string $role,
        public DateTimeImmutable $createdAt
    ) {}
}

// Sangat ideal untuk Data Transfer Objects (DTO)
```

---

## 🪄 Magic Methods `__get()` & `__set()`

Menangani akses ke properti yang tidak terdaftar secara dinamis:

```php
class KamusData {
    private array $storage = [];

    public function __set(string $key, mixed $val): void {
        $this->storage[$key] = $val;
    }

    public function __get(string $key): mixed {
        return $this->storage[$key] ?? null;
    }
}

$k = new KamusData();
$k->tema = "Dark"; // Memicu __set
echo $k->tema;     // Memicu __get: Dark
```

---

## 💳 Studi Kasus: Dompet Digital

```php
class DompetDigital {
    private float $saldo;

    public function __construct(
        public readonly string $noHp,
        private string $pin,
        float $saldoAwal = 0
    ) {
        $this->saldo = max(0, $saldoAwal);
    }

    public function getSaldo(): float { return $this->saldo; }

    public function transfer(string $pin, float $nominal): bool {
        if ($this->pin !== $pin || $nominal > $this->saldo) return false;
        $this->saldo -= $nominal;
        return true;
    }
}
```

---

<!-- _class: lead -->
# Sesi Praktikum & Tanya Jawab 💬

### 📝 Tugas Praktikum Mandiri:
1. Buat class `NilaiAkademik` dengan properti private: `$tugas, $uts, $uas`.
2. Buat Setter & Getter dengan validasi rentang nilai `0.0 – 100.0`.
3. Buat method `hitungNilaiAkhir()` (Tugas 30%, UTS 30%, UAS 40%) dan `getGrade()`.
4. Uji penolakan setter saat diisi nilai tidak valid (misal: `-10` atau `150`).

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/encapsulation
