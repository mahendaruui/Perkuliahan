---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 5'
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
# Inheritance (Pewarisan) & Trait di PHP 8+
### Pertemuan 5 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 5

1. **Pilar 2 OOP: Filosofi Inheritance & Relasi "Is-A"**
2. **Sintaks Pewarisan:** Keyword `extends` & `parent::__construct()`
3. **Visibilitas `protected`** untuk Akses Keluarga Turunan
4. **Method Overriding:** Menyesuaikan Perilaku Subclass
5. **Keyword `final`:** Mengunci Pewarisan Class & Method
6. **Trait PHP:** Solusi *Horizontal Code Reuse*
7. **Trait Conflict Resolution (`insteadof` & `as`)**
8. **Studi Kasus Praktikum:** Hirarki Karyawan + Trait Logging

---

## 🧬 Pilar 2: Konsep Inheritance ("Is-A")

```
                 ┌─────────────────────────────────┐
                 │   SUPERCLASS (PARENT):          │
                 │   Kendaraan ($merk, $tahun)     │
                 └────────────────┬────────────────┘
                                  │ extends (Is-A)
                 ┌────────────────┴────────────────┐
                 ▼                                 ▼
┌─────────────────────────────────┐ ┌─────────────────────────────────┐
│ SUBCLASS (CHILD 1):             │ │ SUBCLASS (CHILD 2):             │
│ Mobil ($jumlahPintu, AC)        │ │ Motor ($adaBox, wheelie)        │
└─────────────────────────────────┘ └─────────────────────────────────┘
```

**Inheritance:** Mekanisme pewarisan atribut dan method dari superclass ke subclass tanpa perlu menulis ulang kode (*DRY Principle*).

---

## 🏗️ Sintaks `extends` & `parent::`

```php
// Parent Class
class Kendaraan {
    public function __construct(
        protected string $merk,
        protected int $tahun
    ) {}
}

// Child Class
class Mobil extends Kendaraan {
    public function __construct(
        string $merk,
        int $tahun,
        private int $jumlahPintu = 4
    ) {
        // Panggil constructor parent
        parent::__construct($merk, $tahun);
    }
}
```

---

## ⚡ Method Overriding

Subclass dapat menimpa method induk dan memanggil fungsionalitas induk dengan `parent::method()`:

```php
class Mobil extends Kendaraan {
    public function infoKendaraan(): void {
        parent::infoKendaraan(); // Jalankan info dari parent
        echo "Pintu: {$this->jumlahPintu} unit\n";
    }
}

$avanza = new Mobil("Toyota", 2024);
$avanza->infoKendaraan();
```

---

## 🔒 Kata Kunci `final`

- **Final Class:** Mencegah class di-extends oleh siapa pun.
- **Final Method:** Mencegah method di-override oleh child class.

```php
// Tidak bisa di-extends:
final class DatabaseConfig {}

class Rekening {
    // Tidak bisa di-override child class:
    final public function hitungPajakBaku() {}
}
```

---

## 🧩 Solusi Single Inheritance: Trait

Menyisipkan potongan method (*horizontal code reuse*) ke berbagai class tanpa batasan hierarki:

```php
trait Loggable {
    public function log(string $pesan): void {
        echo "[" . date('H:i:s') . "] [" . static::class . "] {$pesan}\n";
    }
}

trait Exportable {
    public function toJSON(): string {
        return json_encode(get_object_vars($this));
    }
}

class Produk {
    use Loggable, Exportable; // Pasang 2 trait sekaligus
}
```

---

## 🛠️ Trait Conflict Resolution

Jika dua trait memiliki nama method yang sama, gunakan `insteadof` dan `as`:

```php
trait A { public function cetak() { echo "A"; } }
trait B { public function cetak() { echo "B"; } }

class Dokumen {
    use A, B {
        A::cetak insteadof B;   // Pilih method Trait A
        B::cetak as cetakVersiB; // Beri alias untuk method Trait B
    }
}
```

---

## 💼 Studi Kasus: Hirarki Karyawan

```php
class Karyawan {
    public function __construct(
        protected string $nama,
        protected float $gajiPokok
    ) {}
    public function hitungGaji(): float { return $this->gajiPokok; }
}

class Manager extends Karyawan {
    public function __construct($nama, $gaji, private float $tunjangan) {
        parent::__construct($nama, $gaji);
    }
    public function hitungGaji(): float {
        return $this->gajiPokok + $this->tunjangan;
    }
}
```

---

<!-- _class: lead -->
# Sesi Praktikum & Tanya Jawab 💬

### 📝 Tugas Praktikum Mandiri:
1. Buat parent class `Bentuk` dengan properti `$warna`.
2. Buat subclass `Persegi` dan `Lingkaran` yang meng-override `hitungLuas()`.
3. Buat trait `IdentitasObjek` dengan method `cetakInfo()`, pasang di kedua subclass.

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/inheritance
