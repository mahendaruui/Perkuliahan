---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 7'
footer: 'Mahendar Dwi Payana, S.ST., M.T. • Universitas Ubudiyah Indonesia'
style: |
  section {
    background-color: #f8fafc;
    color: #0f172a;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  h1 {
    color: #4f46e5;
  }
  h2 {
    color: #475569;
  }
  th {
    background-color: #e2e8f0;
    color: #0f172a;
  }
  td {
    background-color: #ffffff;
    color: #334155;
  }
  code {
    background-color: #e2e8f0;
    color: #4338ca;
  }
---

<!-- _class: lead -->
# Abstraction, Abstract Classes & Interfaces di PHP 8+
### Pertemuan 7 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 7

1. **Pilar 4 OOP: Filosofi Abstraction & Penyembunyian Kerumitan**
2. **Abstract Class & Abstract Method (Kerangka Dasar Wajib)**
3. **Interface: Standarisasi Kontrak Antarmuka Perilaku**
4. **Multiple Interface Implementation di PHP**
5. **Matriks Komparasi: Abstract Class (IS-A) vs Interface (CAN-DO)**
6. **Backed Enum di PHP 8.1+ untuk Status yang Type-Safe**
7. **Studi Kasus: Sistem Notifikasi Kampus Multi-Channel**
8. **Persiapan Ujian Tengah Semester (UTS) Minggu Depan**

---

## 🧩 Pilar 4: Filosofi Abstraction

- **Fokus Utama:** Menyajikan antarmuka penting (*WHAT*) dan menyembunyikan detail teknis yang rumit (*HOW*).
- **Contoh Nyata:** Pengemudi mobil cukup menekan pedal gas untuk mempercepat kendaraan tanpa perlu mengatur injeksi katup bahan bakar secara manual.

---

## 🏛️ Abstract Class & Abstract Method

Class induk setengah jadi yang **tidak dapat diinstansiasi langsung**:

```php
abstract class BangunDatar {
    public function __construct(protected string $nama) {}
    public function getNama(): string { return $this->nama; }

    // Wajib diimplementasikan subclass:
    abstract public function hitungLuas(): float;
    abstract public function hitungKeliling(): float;
}

class Persegi extends BangunDatar {
    public function __construct(private float $sisi) { parent::__construct("Persegi"); }
    public function hitungLuas(): float { return $this->sisi ** 2; }
    public function hitungKeliling(): float { return 4 * $this->sisi; }
}
```

---

## 📜 Interface: Kontrak Murni

```php
interface NotifikasiInterface {
    public function kirim(string $tujuan, string $pesan): bool;
}

class EmailNotifikasi implements NotifikasiInterface {
    public function kirim(string $tujuan, string $pesan): bool {
        echo "📧 Email terkirim ke {$tujuan}\n";
        return true;
    }
}
```

---

## 🔗 Multiple Interface Implementation

```php
interface KirimPesan { public function kirim(string $msg): void; }
interface LogAudit   { public function catatWaktu(): void; }

class WhatsAppService implements KirimPesan, LogAudit {
    public function kirim(string $msg): void { echo "📲 WA: {$msg}\n"; }
    public function catatWaktu(): void { echo "⏱️ Log dicatat.\n"; }
}
```

---

## ⚖️ Abstract Class vs Interface

| Kriteria | Abstract Class | Interface |
| :--- | :--- | :--- |
| **Kata Kunci** | `abstract class` & `extends` | `interface` & `implements` |
| **Jumlah Implementasi** | Single Inheritance (1 parent) | Multiple (Bisa banyak) |
| **Properti Data** | Boleh punya properti biasa | Hanya konstanta (`const`) |
| **Constructor** | Boleh ada `__construct()` | Tidak boleh ada |
| **Relasi** | **IS-A** (Keluarga terikat) | **CAN-DO** (Kontrak kemampuan) |

---

## 📦 Backed Enum di PHP 8.1+

```php
enum StatusPesanan: string {
    case PENDING = 'Menunggu Pembayaran';
    case KIRIM   = 'Dalam Pengiriman';
    case SELESAI = 'Pesanan Selesai';

    public function icon(): string {
        return match($this) {
            self::PENDING => '⏳',
            self::KIRIM   => '🚚',
            self::SELESAI => '✅',
        };
    }
}
```

---

<!-- _class: lead -->
# Evaluasi Tengah Semester (UTS) 🎯

### 📋 Cakupan Materi UTS (Pertemuan 1 s/d 7):
1. **Konsep & Fondasi OOP PHP 8+**
2. **Class, Object, Typed Properties & `$this`**
3. **Constructor, Promotion, Named Arguments & Static Member**
4. **Encapsulation & Readonly**
5. **Inheritance & Trait**
6. **Polymorphism & Dynamic Dispatch**
7. **Abstraction, Abstract Classes & Interfaces**

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/interface-abstract
