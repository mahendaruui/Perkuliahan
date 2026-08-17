---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 6'
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
# Polymorphism (Polimorfisme) di PHP 8+
### Pertemuan 6 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 6

1. **Pilar 3 OOP: Filosofi Polymorphism ("Satu Antarmuka, Banyak Wujud")**
2. **Dynamic Method Dispatch & Late Binding di PHP Runtime**
3. **Polymorphic Type Hinting pada Parameter Fungsi/Method**
4. **Array Polimorfik (Koleksi Objek Heterogen)**
5. **Operator `instanceof` untuk Type Safety & Validasi Tipe Objek**
6. **Studi Kasus Praktikum: Arsitektur Payment Gateway Multi-Vendor**
7. **Prinsip Arsitektur: Open-Closed Principle (SOLID)**
8. **Tugas Praktikum Mandiri:** Class `AkunBank` & Perhitungan Bunga

---

## 🎭 Pilar 3: Filosofi Polymorphism

```
                    ┌───────────────────────────────┐
                    │   MetodePembayaran (Parent)   │
                    │   +bayar(nominal)             │
                    └───────────────┬───────────────┘
                                    │ Dynamic Dispatch
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│ TransferBank  │           │ PembayaranQRIS│           │  EWalletGoPay │
│  (Bank + Rek) │           │  (QR String)  │           │ (No. HP + PIN)│
└───────────────┘           └───────────────┘           └───────────────┘
```

**Polymorphism:** Objek dari berbagai subclass yang berbeda dapat merespons panggilan method yang sama dengan cara/perilaku unik mereka masing-masing.

---

## ⚡ Dynamic Method Dispatch

PHP mengeksekusi method berdasarkan class objek riil pada saat *runtime*:

```php
class Hewan {
    public function bersuara(): string { return "Suara umum..."; }
}

class Kucing extends Hewan {
    public function bersuara(): string { return "🐱 Meong... meong!"; }
}

class Anjing extends Hewan {
    public function bersuara(): string { return "🐶 Guk... guk!"; }
}

// Type Hinting Superclass:
function cetakSuara(Hewan $h): void {
    echo $h->bersuara() . "\n";
}

cetakSuara(new Kucing()); // 🐱 Meong... meong!
cetakSuara(new Anjing()); // 🐶 Guk... guk!
```

---

## 📚 Array Polimorfik

Memproses banyak objek turunan berbeda dalam satu perulangan seragam:

```php
$kebunBinatang = [
    new Kucing(),
    new Anjing(),
    new Kucing()
];

// Loop seragam tanpa if-else percabangan jenis hewan
foreach ($kebunBinatang as $hewan) {
    echo $hewan->bersuara() . "\n";
}
```

---

## 🛡️ Operator `instanceof`

Memeriksa tipe objek sebelum menjalankan aksi spesifik:

```php
class KlinikHewan {
    public function rawat(Hewan $h): void {
        echo $h->bersuara() . "\n";

        if ($h instanceof Kucing) {
            echo "💉 Berikan vaksin khusus kucing.\n";
        } elseif ($h instanceof Anjing) {
            echo "🧼 Mandi anti-kutu anjing.\n";
        }
    }
}
```

---

## 💳 Studi Kasus: Payment Gateway

```php
abstract class MetodePembayaran {
    public function __construct(protected float $nominal) {}
    abstract public function prosesBayar(): string;
}

class TransferBank extends MetodePembayaran {
    public function prosesBayar(): string {
        return "🏦 Transfer Bank Rp " . number_format($this->nominal);
    }
}

class PembayaranQRIS extends MetodePembayaran {
    public function prosesBayar(): string {
        return "📱 Scan QRIS Rp " . number_format($this->nominal);
    }
}
```

---

## 🛒 Client Code: Kasir E-Commerce

```php
class KasirOnline {
    // Type Hinting Polimorfik: Menerima SEMUA jenis metode bayar!
    public function checkout(MetodePembayaran $metode): void {
        echo "Memulai Transaksi...\n";
        echo $metode->prosesBayar() . " [SUKSES]\n";
    }
}

$kasir = new KasirOnline();
$kasir->checkout(new TransferBank(500_000));
$kasir->checkout(new PembayaranQRIS(35_000));
```

---

## ⚖️ Overriding vs Overloading di PHP

| Fitur | Dukungan PHP 8+ | Solusi di PHP |
| :--- | :---: | :--- |
| **Method Overriding** | ✅ Ya (Penuh) | Subclass menimpa method parent |
| **Method Overloading** (Multiple Signatures) | ❌ Tidak Ada | Gunakan Union Types (`int\|float`) & Default Values |

---

<!-- _class: lead -->
# Sesi Praktikum & Tanya Jawab 💬

### 📝 Tugas Praktikum Mandiri:
1. Buat class parent `AkunBank` dengan method `hitungBungaBulanan()`.
2. Buat subclass: `TabunganReguler` (1%/thn), `Deposito` (5.5%/thn), dan `TabunganSyariah` (bagi hasil).
3. Simpan ketiga akun dalam array polimorfik `$daftarAkun` dan cetak estimasi bunga bulanan.

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/polymorphism
