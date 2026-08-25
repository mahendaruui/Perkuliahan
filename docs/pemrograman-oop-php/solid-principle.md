# Minggu 13: Prinsip Desain Perangkat Lunak SOLID di PHP 8+

## 🎯 Capaian Pembelajaran (Sub-CPMK 5)
Setelah menyelesaikan materi pada bab ini, mahasiswa diharapkan mampu:
1. Memahami latar belakang lahirnya **Prinsip Desain SOLID** (*Robert C. Martin / Uncle Bob*) dalam mengeliminasi 4 gejala pembusukan arsitektur (*Rigidity, Fragility, Immobility, Viscosity*).
2. Menerapkan **Single Responsibility Principle (SRP)** untuk mencegah antipattern *God Object* dan memusatkan satu alasan perubahan per class.
3. Menerapkan **Open/Closed Principle (OCP)** dengan pola *Strategy Pattern* sehingga sistem mudah diperluas tanpa mengubah kode yang sudah teruji.
4. Menganalisis dan menegakkan **Liskov Substitution Principle (LSP)** termasuk aturan kovariansi (*Covariance*) dan kontravariansi (*Contravariance*) di PHP 8+.
5. Menerapkan **Interface Segregation Principle (ISP)** dengan memecah *Fat Interface* menjadi *Role-based Interfaces* yang ramping.
6. Menerapkan **Dependency Inversion Principle (DIP)** dan teknik **Constructor Dependency Injection** dengan fitur *Constructor Property Promotion* di PHP 8.0+.

> [!NOTE]
> 💡 **Filosofi Arsitektur:** Prinsip SOLID bukan sekadar aturan sintaksis, melainkan pedoman berpikir arsitektural untuk menghasilkan kode yang *clean*, fleksibel (*extensible*), dan mudah diuji (*testable*).

---

## 1. Fondasi Teoretis SOLID: Menghindari Pembusukan Perangkat Lunak

```mermaid
flowchart TD
    subgraph ClientLayer["Application Service Layer"]
        Checkout["CheckoutService<br>+prosesCheckout(Order, DiskonStrategy)"]
    end

    subgraph AbstractionLayer["Abstractions / Contracts (DIP)"]
        DiskonInt["interface DiskonStrategyInterface<br>+hitung(subtotal): float"]
        PaymentInt["interface PaymentGatewayInterface<br>+charge(amount): bool"]
        NotifInt["interface NotifierInterface<br>+send(msg): void"]
    end

    subgraph ConcreteLayer["Low-Level Implementation (OCP & LSP)"]
        D1["DiskonMember"]
        D2["DiskonFlashSale"]
        P1["MidtransGateway"]
        P2["XenditGateway"]
        N1["WhatsAppNotifier"]
        N2["EmailNotifier"]
    end

    Checkout --> DiskonInt
    Checkout --> PaymentInt
    Checkout --> NotifInt

    D1 ..|> DiskonInt
    D2 ..|> DiskonInt
    P1 ..|> PaymentInt
    P2 ..|> PaymentInt
    N1 ..|> NotifInt
    N2 ..|> NotifInt
```

Dalam literatur rekayasa perangkat lunak, sistem yang tidak dirancang dengan baik akan mengalami **Software Rot** (Pembusukan Perangkat Lunak) yang ditandai oleh 4 gejala:
1. **Rigidity (Kekakuan):** Setiap perubahan kecil menuntut modifikasi berantai pada puluhan berkas lain.
2. **Fragility (Kerapuhan):** Perbaikan pada satu modul merusak modul lain yang secara logika tidak berhubungan.
3. **Immobility (Ketakbergerakan):** Modul-modul sistem sulit dipindahkan atau digunakan kembali pada proyek lain karena terikat dependensi erat (*Tight Coupling*).
4. **Viscosity (Viskositas):** Pengembang lebih memilih menulis kode "tambal sulam" (*hack*) daripada mematuhi arsitektur yang benar karena arsitektur yang ada terlalu kaku.

---

## 2. Bedah Komprehensif 5 Prinsip SOLID di PHP 8+

### S — Single Responsibility Principle (SRP)
> *"A class should have one, and only one, reason to change."* — Robert C. Martin.

Sebuah class hanya boleh bertanggung jawab terhadap **satu aktor atau satu fungsi bisnis**. Class yang melakukan kalkulasi, validasi, penulisan database, dan pencetakan PDF sekaligus disebut sebagai antipattern **God Object**.

#### ✅ Refactoring Menuju SRP:
```php
<?php
declare(strict_types=1);

namespace App\Domain\Model;

// 1. Model Murni (Hanya memegang state dan aturan invariant pesanan)
class Pesanan
{
    public function __construct(
        public readonly string $nomorPesanan,
        public readonly float $subtotal
    ) {}
}

// 2. Layanan Kalkulasi Pajak Terpisah
class KalkulatorPajakService
{
    public function hitungPpn(float $nominal, float $persen = 0.11): float
    {
        return $nominal * $persen;
    }
}

// 3. Layanan Pencetakan Dokumen Terpisah
class InvoicePdfPrinter
{
    public function render(Pesanan $p, float $pajak): string
    {
        return "[PDF INVOICE] Pesanan: {$p->nomorPesanan} | Total: Rp " . number_format($p->subtotal + $pajak);
    }
}
```

---

### O — Open/Closed Principle (OCP)
> *"Software entities should be open for extension, but closed for modification."* — Bertrand Meyer.

Perangkat lunak harus dirancang agar fungsionalitas baru dapat ditambahkan (misal jenis diskon baru, metode pembayaran baru) **tanpa perlu mengubah kode sumber yang sudah ada dan sudah berjalan di produksi**.

#### ✅ Penerapan OCP dengan Strategy Pattern:
```php
<?php
declare(strict_types=1);

namespace App\Domain\Diskon;

// Kontrak Abstraksi Terbuka
interface DiskonStrategyInterface
{
    public function hitungDiskon(float $subtotal): float;
}

// Implementasi 1: Diskon Member Reguler
class DiskonMemberReguler implements DiskonStrategyInterface
{
    public function hitungDiskon(float $subtotal): float
    {
        return $subtotal * 0.05; // 5%
    }
}

// Implementasi 2: Diskon Flash Sale (Dapat ditambah kapan saja tanpa edit class CheckoutService!)
class DiskonFlashSale implements DiskonStrategyInterface
{
    public function hitungDiskon(float $subtotal): float
    {
        return $subtotal * 0.20; // 20%
    }
}

// Kode Layanan Tertutup dari Modifikasi:
class CheckoutService
{
    public function hitungTotalAkhir(float $subtotal, DiskonStrategyInterface $diskonStrategy): float
    {
        $potongan = $diskonStrategy->hitungDiskon($subtotal);
        return max(0.0, $subtotal - $potongan);
    }
}
```

---

### L — Liskov Substitution Principle (LSP)
> *"Subtypes must be substitutable for their base types without altering the correctness of the program."* — Barbara Liskov (1987).

Objek turunan (*subclass*) harus dapat menggantikan objek induknya (*superclass*) tanpa menimbulkan perilaku aneh atau merusak jalannya program.

#### ❌ Pelanggaran Klasik LSP:
```php
class Burung { public function terbang(): void { echo "Terbang tinggi..."; } }
class BurungUnta extends Burung {
    public function terbang(): void {
        throw new \LogicException("Burung Unta tidak bisa terbang!"); // ❌ Melanggar LSP!
    }
}
```

#### ✅ Penegakan LSP yang Benar:
Pisahkan kemampuan terbang ke dalam interface terpisah (`TerbangInterface`) sehingga hanya burung yang benar-benar bisa terbang yang mengimplementasikannya. Subclass dilarang memperketat prekondisi atau memperlemah postkondisi parent.

---

### I — Interface Segregation Principle (ISP)
> *"Clients should not be forced to depend upon interfaces that they do not use."*

Lebih baik membuat **banyak interface kecil dan spesifik (*Role Interfaces*)** daripada satu interface raksasa yang serba-bisa (*Fat Interface*).

```php
<?php
declare(strict_types=1);

namespace App\Kontrak;

// Interface Spesifik Ramping:
interface BisaCetakDokumen { public function cetak(): void; }
interface BisaPindaiDokumen { public function scan(): void; }
interface BisaFaksimili { public function fax(): void; }

// Printer Biasa hanya mengimplementasikan apa yang sanggup dilakukannya:
class PrinterRumahan implements BisaCetakDokumen
{
    public function cetak(): void { echo "Mencetak dokumen kertas A4.\n"; }
}

// Printer Enterprise Kantor:
class MesinFotokopiMultifungsi implements BisaCetakDokumen, BisaPindaiDokumen, BisaFaksimili
{
    public function cetak(): void { echo "Mencetak cepat laser.\n"; }
    public function scan(): void { echo "Memindai dokumen ke PDF.\n"; }
    public function fax(): void { echo "Mengirim fax ke tujuan.\n"; }
}
```

---

### D — Dependency Inversion Principle (DIP)
> *"1. High-level modules should not depend on low-level modules. Both should depend on abstractions."*  
> *"2. Abstractions should not depend on details. Details should depend on abstractions."*

Modul tingkat tinggi (proses bisnis utama) tidak boleh bergantung langsung pada modul tingkat rendah (driver database, API pihak ketiga). Keduanya harus bergantung pada **Abstraksi (Interface)**.

#### ✅ Penerapan DIP & Constructor Dependency Injection di PHP 8+:
```php
<?php
declare(strict_types=1);

namespace App\Service;

interface NotifierInterface
{
    public function kirimNotifikasi(string $tujuan, string $pesan): bool;
}

class WhatsAppNotifier implements NotifierInterface
{
    public function kirimNotifikasi(string $tujuan, string $pesan): bool
    {
        echo "📲 [WHATSAPP] Mengirim pesan ke {$tujuan}: {$pesan}\n";
        return true;
    }
}

// High-Level Service yang Bersih (DIP):
class PendaftaranMahasiswaService
{
    // PHP 8.0: Constructor Property Promotion dengan Type-Hint Abstraksi
    public function __construct(
        private NotifierInterface $notifier
    ) {}

    public function daftarkan(string $nama, string $noHp): void
    {
        echo "✅ Mahasiswa [{$nama}] berhasil terdaftar di basis data.\n";
        // Menggunakan abstraksi tanpa tahu implementasi konkretnya:
        $this->notifier->kirimNotifikasi($noHp, "Selamat {$nama}, pendaftaran Anda berhasil!");
    }
}

// Pemasangan Dependensi (Dependency Injection):
$service = new PendaftaranMahasiswaService(new WhatsAppNotifier());
$service->daftarkan("Cut Nyak Dhien", "08123456789");
```

---

## 💻 3. Praktikum Terbimbing: E-Commerce Checkout Pipeline Berstandar SOLID

```php
<?php
declare(strict_types=1);

namespace App\Ecommerce;

// 1. Abstraksi Pembayaran
interface PaymentProcessorInterface
{
    public function bayar(float $nominal): bool;
}

class QrisPaymentProcessor implements PaymentProcessorInterface
{
    public function bayar(float $nominal): bool
    {
        echo "📱 Pembayaran QRIS sebesar Rp " . number_format($nominal, 0, ',', '.') . " BERHASIL.\n";
        return true;
    }
}

// 2. Pipeline Transaksi Terpadu
class TransaksiPipelineService
{
    public function __construct(
        private \App\Domain\Diskon\DiskonStrategyInterface $diskonStrategy,
        private PaymentProcessorInterface $paymentProcessor,
        private \App\Service\NotifierInterface $notifier
    ) {}

    public function selesaikanTransaksi(string $customer, float $subtotal, string $kontak): void
    {
        $diskon = $this->diskonStrategy->hitungDiskon($subtotal);
        $totalBayar = max(0.0, $subtotal - $diskon);

        echo "========================================================\n";
        echo "PROSES TRANSAKSI CHECKOUT E-COMMERCE\n";
        echo "Pelanggan   : {$customer}\n";
        echo "Subtotal    : Rp " . number_format($subtotal, 0, ',', '.') . "\n";
        echo "Diskon      : Rp " . number_format($diskon, 0, ',', '.') . "\n";
        echo "Total Bayar : Rp " . number_format($totalBayar, 0, ',', '.') . "\n";
        echo "--------------------------------------------------------\n";

        $this->paymentProcessor->bayar($totalBayar);
        $this->notifier->kirimNotifikasi($kontak, "Pesanan Anda sebesar Rp " . number_format($totalBayar) . " telah lunas.");
        echo "========================================================\n";
    }
}

// Eksekusi Pipeline
$pipeline = new TransaksiPipelineService(
    new \App\Domain\Diskon\DiskonFlashSale(),
    new QrisPaymentProcessor(),
    new \App\Service\WhatsAppNotifier()
);

$pipeline->selesaikanTransaksi("Teuku Iskandar", 500_000.0, "08119876543");
```

---

## 📝 Evaluasi & Tugas Praktikum Mandiri

1. **Analisis Reflektif Kasus Pelanggaran:**
   - Telaah class berikut: `class User { public function saveToDb() {} public function generatePdf() {} public function sendEmail() {} }`. Jelaskan mengapa class ini melanggar SRP dan rancang refactoring-nya!
2. **Implementasi Multi-Gateway dengan DIP:**
   - Buat interface `SmsGatewayInterface`.
   - Buat 2 implementor: `TwilioSmsGateway` dan `TelkomselSmsGateway`.
   - Pasang ke dalam `AuthOtpService` menggunakan Constructor Injection.
3. **Analisis Reflektif:**
   - Mengapa Dependency Inversion Principle (DIP) merupakan fondasi mutlak dalam mempermudah Automated Unit Testing menggunakan *Mock Objects*?
