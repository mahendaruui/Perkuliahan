---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek (PHP 8+) — Pertemuan 2'
footer: 'Mahendar Dwi Payana, S.ST., M.T. • Universitas Ubudiyah Indonesia'
style: |
  section {
    background-color: #0f172a;
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
    background-color: #0f172a;
    color: #334155;
  }
  code {
    background-color: #e2e8f0;
    color: #4338ca;
  }
---

<!-- _class: lead -->
# Class, Object, dan Perilaku di PHP 8+
### Pertemuan 2 • IFR 214 (3 SKS)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 2

1. **Konsep Blueprint vs Instance** (Class vs Object di memori)
2. **Typed Properties di PHP 7.4/8+** & Nilai Default
3. **Mendefinisikan Method** & Menggunakan Pseudo-Variable `$this`
4. **Instansiasi Objek** dengan Operator `new` & Operator Panah (`->`)
5. **Jebakan:** *Uninitialized Typed Property Error* & Solusinya
6. **Manajemen Memori Objek:** Object Reference Handle vs Keyword `clone`
7. **Studi Kasus Praktikum:** Class `Produk` Kasir
8. **Tugas Praktikum Mandiri:** Class `Karyawan`

---

## 🏛️ Dari Prototype (Class) Menjadi Produk Nyata (Object)

```
[ PROTOTYPE / BLUEPRINT (Class) ] ━━━━( new Operator )━━━━▶ [ PRODUK NYATA 1 ] & [ PRODUK NYATA 2 ]
```

### 1. 🏭 Prototype Pabrik ➔ 🚗 Mobil Fisik
- **Class (Prototype):** Desain spesifikasi rangka, mesin 1500cc, 4 roda.
- **Object (Produk):** Mobil Merah (Plat B 1234) & Mobil Hitam (Plat D 5678).

### 2. 🍪 Cetakan Kue ➔ 🧁 Kue Matang
- **Class (Cetakan):** Cetakan kue bentuk bintang.
- **Object (Kue Jadi):** Kue rasa Coklat & Kue rasa Keju.

### 3. 🏡 Denah Arsitek ➔ 🏠 Bangunan Rumah Fisik
- **Class (Denah 2D):** Gambar tata letak kamar dan pintu.
- **Object (Rumah Nyata):** Rumah No. 10 Cat Putih & Rumah No. 12 Cat Hijau.

---

## 📝 Anatomi Deklarasi Class di PHP 8+

```php
<?php
declare(strict_types=1);

class Mahasiswa
{
    // 1. Properti Bertipe Data (Typed Properties)
    public string $nim;
    public string $nama;
    public string $jurusan = "Sistem Informasi";
    public float $ipk = 0.0;

    // 2. Method / Perilaku Objek
    public function belajar(string $mataKuliah): void
    {
        echo "{$this->nama} sedang belajar {$mataKuliah}.\n";
    }
}
```

---

## 🎯 Instansiasi Objek & Operator Arrow (`->`)

```php
// 1. Buat Objek Baru
$mhs1 = new Mahasiswa();
$mhs1->nim = "240101001";
$mhs1->nama = "Ahmad Pratama";
$mhs1->ipk = 3.85;

$mhs2 = new Mahasiswa();
$mhs2->nim = "240101002";
$mhs2->nama = "Rina Melati";
$mhs2->jurusan = "Informatika";
$mhs2->ipk = 3.92;

// 2. Panggil Method
$mhs1->belajar("PHP OOP"); // Ahmad Pratama sedang belajar PHP OOP.
```

> **Catatan:** Jangan gunakan tanda `$` pada nama properti saat mengakses via arrow (`$mhs1->nama`, BUKAN `$mhs1->$nama`).

---

## 🔍 Peran Variabel Pseudo `$this`

- `$this` adalah variabel otomatis yang **merujuk ke objek pemanggil saat ini** (*current instance*).
- Tanpa `$this->`, PHP akan menganggap variabel tersebut sebagai variabel lokal fungsi!

```php
class PersegiPanjang {
    public float $panjang;
    public float $lebar;

    public function hitungLuas(): float {
        return $this->panjang * $this->lebar;
    }
}
```

---

## ⚠️ Jebakan: Uninitialized Typed Property

Di PHP 7.4+, membaca properti bertipe sebelum diinisialisasi akan menghasilkan **Fatal Error**:

```php
class User {
    public string $username; // Tidak ada default value
}

$u = new User();
echo $u->username; 
// 💥 Error: Typed property User::$username must not be accessed before initialization
```

### ✅ Solusi:
1. Berikan nilai default: `public string $username = "";`
2. Atau gunakan nullable type: `public ?string $username = null;`

---

## 🧠 Alokasi Memori: Referensi vs `clone`

Objek di PHP dilewatkan berdasarkan *Object Handle*, bukan salinan nilai:

```php
// Kasus 1: Referensi (Objek yang SAMA)
$a = new Mahasiswa();
$a->nama = "Budi";
$b = $a;
$b->nama = "Siti";
echo $a->nama; // Output: "Siti" ($a ikut berubah!)

// Kasus 2: Duplikasi Fisik dengan clone
$c = clone $a;
$c->nama = "Andi";
echo $a->nama; // Output tetap: "Siti"
```

---

## 🛒 Studi Kasus: Class `Produk` Kasir

```php
class Produk {
    public string $kode;
    public string $nama;
    public float $harga;
    public int $stok = 0;

    public function jual(int $qty): bool {
        if ($this->stok >= $qty) {
            $this->stok -= $qty;
            return true;
        }
        return false;
    }
}
```

---

<!-- _class: lead -->
# Sesi Praktikum & Tanya Jawab 💬

### 📝 Tugas Mandiri Pertemuan 2:
- Buat class `Karyawan` dengan properti: `$id, $nama, $divisi, $gajiPokok, $jamLembur`.
- Tambahkan method `tambahLembur($jam)` dan `hitungTotalGaji()` (Rp 50.000/jam).
- Instansiasi 2 objek karyawan dan cetak slip gajinya.

**Modul Materi Lengkap:**  
https://mahendaruui.github.io/Perkuliahan/pemrograman-oop-php/class-dan-object
