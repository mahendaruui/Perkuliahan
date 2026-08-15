# Minggu 4: Encapsulation & Visibility

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Memahami prinsip **Encapsulation** dan **Information Hiding** di PHP.
2. Menggunakan 3 jenis **Visibility Modifiers**: `public`, `protected`, `private`.
3. Mengimplementasikan **Getter** dan **Setter** dengan validasi data.
4. Mengenal **Magic Methods** (`__get`, `__set`) untuk akses properti dinamis.

---

## 1. Visibility Modifiers di PHP

| Modifier | Class Sendiri | Child Class | Luar Class |
| :--- | :---: | :---: | :---: |
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

---

## 2. Implementasi Getter dan Setter

```php
<?php

class Pasien
{
    private string $nama;
    private int $umur;
    private float $beratBadan;

    public function __construct(string $nama, int $umur, float $beratBadan)
    {
        $this->nama = $nama;
        $this->setUmur($umur);
        $this->setBeratBadan($beratBadan);
    }

    // Getter
    public function getNama(): string
    {
        return $this->nama;
    }

    // Setter dengan validasi
    public function setUmur(int $umur): void
    {
        if ($umur >= 0 && $umur <= 150) {
            $this->umur = $umur;
        } else {
            echo "Error: Nilai umur tidak logis ({$umur})\n";
            $this->umur = 0;
        }
    }

    public function getUmur(): int
    {
        return $this->umur;
    }

    public function setBeratBadan(float $berat): void
    {
        if ($berat > 0) {
            $this->beratBadan = $berat;
        } else {
            echo "Error: Berat badan harus positif!\n";
        }
    }
}
```

---

## 3. Readonly Properties (PHP 8.1+)

Properti `readonly` hanya bisa di-set **satu kali** (biasanya di constructor), setelah itu tidak bisa diubah:

```php
<?php

class Mahasiswa
{
    public function __construct(
        public readonly string $nim,      // Tidak bisa diubah setelah dibuat
        public readonly string $nama,
        private float $ipk = 0.0
    ) {}

    public function setIpk(float $ipk): void
    {
        $this->ipk = $ipk; // IPK bisa diubah (bukan readonly)
    }
}

$mhs = new Mahasiswa("240101", "Budi");
// $mhs->nim = "999999"; // ❌ FATAL ERROR: Cannot modify readonly property
```

---

## 4. Studi Kasus: Dompet Digital (E-Wallet)

```php
<?php

class DompetDigital
{
    private float $saldo;

    public function __construct(
        private readonly string $nomorPonsel,
        private string $pin,
        float $saldoAwal = 0
    ) {
        $this->saldo = max(0, $saldoAwal);
    }

    public function getSaldo(): float
    {
        return $this->saldo;
    }

    public function getNomorPonsel(): string
    {
        return $this->nomorPonsel;
    }

    public function topUp(float $jumlah): void
    {
        if ($jumlah >= 10_000) {
            $this->saldo += $jumlah;
            echo "Top-up berhasil: Rp " . number_format($jumlah) . "\n";
            echo "Saldo sekarang: Rp " . number_format($this->saldo) . "\n";
        } else {
            echo "Gagal: Minimal top-up Rp 10.000\n";
        }
    }

    public function transfer(string $pinInput, float $jumlah, string $tujuan): bool
    {
        if ($this->pin !== $pinInput) {
            echo "Transfer gagal: PIN salah!\n";
            return false;
        }
        if ($jumlah <= 0 || $this->saldo < $jumlah) {
            echo "Transfer gagal: Saldo tidak mencukupi!\n";
            return false;
        }

        $this->saldo -= $jumlah;
        echo "Transfer Rp " . number_format($jumlah) . " ke {$tujuan} berhasil!\n";
        echo "Sisa saldo: Rp " . number_format($this->saldo) . "\n";
        return true;
    }
}
```

### Pengujian:
```php
$ewallet = new DompetDigital("081234567890", "123456", 50_000);

// $ewallet->saldo = 1_000_000; // ❌ ERROR: Cannot access private property

echo "Saldo awal: Rp " . number_format($ewallet->getSaldo()) . "\n";
$ewallet->topUp(50_000);
$ewallet->transfer("999999", 30_000, "089876543210"); // PIN salah
$ewallet->transfer("123456", 30_000, "089876543210"); // Berhasil
```

---

## 📝 Tugas Mandiri

1. Buat class `NilaiAkademik` dengan properti private: `$nilaiTugas`, `$nilaiUTS`, `$nilaiUAS`.
2. Pasang validasi pada setter: Nilai harus `0 – 100`.
3. Buat method `hitungNilaiAkhir()` (Tugas 30%, UTS 30%, UAS 40%).
4. Buat method `getGrade()` yang mengembalikan huruf mutu (A/B/C/D/E).
