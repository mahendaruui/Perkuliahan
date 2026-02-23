# Minggu 15 — Keamanan Web & Deployment

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa dapat:
- Memahami ancaman keamanan web yang umum (OWASP Top 10)
- Menerapkan teknik **keamanan dasar** pada aplikasi web
- Melakukan **pengujian (testing)** pada aplikasi
- Men-**deploy** aplikasi web ke server/hosting

---

## 1. Keamanan Web Dasar

### OWASP Top 10 yang Paling Relevan

| Peringkat | Serangan | Contoh |
|-----------|---------|--------|
| A01 | Broken Access Control | User biasa bisa akses halaman admin |
| A02 | Cryptographic Failures | Password tersimpan tanpa hash |
| A03 | **Injection** | SQL Injection, Command Injection |
| A07 | **XSS** (Cross-Site Scripting) | Menyisipkan `<script>` ke input |
| A05 | Security Misconfiguration | Info sensitif di pesan error |

---

## 2. SQL Injection (Recap)

```php
// ❌ Rentan
$sql = "SELECT * FROM user WHERE email = '$email' AND password = '$pass'";

// Serangan: email = "admin@x.com' -- " → bypass login!
// Query jadi: SELECT * WHERE email = 'admin@x.com' -- ' AND password = '...'

// ✅ Aman: Prepared Statement
$stmt = $pdo->prepare("SELECT * FROM user WHERE email = ? AND password = ?");
$stmt->execute([$email, $hashed_pass]);
```

---

## 3. XSS (Cross-Site Scripting)

**XSS** terjadi ketika input pengguna yang berisi kode JavaScript ditampilkan langsung di halaman.

```php
// Serangan: input pengguna = "<script>document.cookie...</script>"

// ❌ Rentan — menampilkan HTML mentah
echo $_GET["komentar"];

// ✅ Aman — escape output
echo htmlspecialchars($_GET["komentar"], ENT_QUOTES, 'UTF-8');

// Di Laravel/Blade — otomatis aman
{{ $variabel }}          // Ter-escape (aman)
{!! $variabel !!}        // Tidak ter-escape (gunakan hanya untuk HTML terpercaya!)
```

---

## 4. Keamanan Password

```php
// ❌ JANGAN simpan password dalam bentuk teks biasa atau MD5/SHA1
$pass_salah = md5($password); // SHA1 & MD5 sudah tidak aman!

// ✅ Gunakan password_hash (bcrypt)
$hash = password_hash($password, PASSWORD_BCRYPT);
// Simpan $hash ke database

// ✅ Verifikasi password
if (password_verify($inputPassword, $hashDariDB)) {
    echo "Login berhasil!";
} else {
    echo "Email atau password salah.";
}

// Di Laravel — otomatis dengan Hash facade
use Illuminate\Support\Facades\Hash;

$hash = Hash::make($password);
if (Hash::check($inputPassword, $user->password)) { ... }
```

---

## 5. CSRF (Cross-Site Request Forgery)

**CSRF** adalah serangan yang memaksa pengguna yang sudah login untuk mengirim permintaan berbahaya tanpa sepengetahuannya.

```html
<!-- Di Laravel Blade — wajib ada di setiap form POST/PUT/DELETE -->
<form method="POST" action="/mahasiswa">
    @csrf  <!-- Menghasilkan <input type="hidden" name="_token" value="..."> -->
    <!-- isi form -->
</form>

<!-- Untuk UPDATE/DELETE: tambahkan method spoofing -->
<form method="POST" action="/mahasiswa/1">
    @csrf
    @method('PUT')   <!-- atau @method('DELETE') -->
    <!-- isi form -->
</form>
```

---

## 6. Validasi Input

```php
// PHP Murni — validasi manual
function validasiEmail(string $email): bool {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Laravel — validasi deklaratif
$request->validate([
    'nama'     => 'required|string|min:3|max:100|regex:/^[a-zA-Z\s]+$/',
    'email'    => 'required|email:rfc,dns|unique:users',
    'password' => 'required|min:8|confirmed|regex:/^(?=.*[A-Za-z])(?=.*\d)/',
    'foto'     => 'nullable|image|mimes:jpg,jpeg,png,webp|max:2048',
]);
// Jika gagal → otomatis redirect kembali dengan error
```

---

## 7. HTTPS & Header Keamanan

```apache
# .htaccess — Redirect HTTP ke HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Header keamanan
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-XSS-Protection "1; mode=block"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Content-Security-Policy "default-src 'self'; script-src 'self' cdn.jsdelivr.net"
```

---

## 8. Pengujian Aplikasi Web

### Pengujian Manual (Checklist)

Sebelum deploy, uji secara manual:

```
Fungsionalitas:
☐ Semua form berfungsi (tambah, edit, hapus)
☐ Validasi form bekerja (coba input kosong, input salah)
☐ Navigasi berpindah ke halaman yang benar
☐ Pagination berfungsi

Keamanan:
☐ Form login tidak bisa di-bypass
☐ Halaman admin tidak bisa diakses tanpa login
☐ Input teks panjang tidak merusak tampilan
☐ Coba input: <script>alert('xss')</script>

Responsif:
☐ Tampilan di desktop (1280px)
☐ Tampilan di tablet (768px)
☐ Tampilan di mobile (375px)

Browser:
☐ Google Chrome
☐ Mozilla Firefox
☐ Microsoft Edge
```

### PHPUnit (Unit Testing di Laravel)

```bash
# Buat test
php artisan make:test MahasiswaTest

# Jalankan semua test
php artisan test
```

```php
<?php
// tests/Feature/MahasiswaTest.php
namespace Tests\Feature;

use App\Models\Mahasiswa;
use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class MahasiswaTest extends TestCase {
    use RefreshDatabase;

    public function test_dapat_melihat_daftar_mahasiswa(): void {
        Mahasiswa::factory()->count(5)->create();
        
        $response = $this->get('/mahasiswa');
        
        $response->assertStatus(200);
        $response->assertViewIs('mahasiswa.index');
        $response->assertViewHas('mahasiswa');
    }

    public function test_dapat_tambah_mahasiswa(): void {
        $data = [
            'nim'   => '21001234',
            'nama'  => 'Ahmad Test',
            'email' => 'ahmad@test.com',
            'prodi' => 'IF',
            'ipk'   => 3.5,
        ];

        $response = $this->post('/mahasiswa', $data);

        $response->assertRedirect('/mahasiswa');
        $this->assertDatabaseHas('mahasiswa', ['nim' => '21001234']);
    }

    public function test_validasi_nim_duplikat(): void {
        Mahasiswa::factory()->create(['nim' => '21001234']);

        $response = $this->post('/mahasiswa', [
            'nim'   => '21001234',
            'nama'  => 'Duplikat',
            'email' => 'duplikat@test.com',
            'prodi' => 'IF',
            'ipk'   => 3.0,
        ]);

        $response->assertSessionHasErrors('nim');
    }
}
```

---

## 9. Deployment

### Opsi Hosting

| Jenis | Contoh | Cocok untuk |
|-------|--------|-------------|
| **Shared Hosting** | Niagahoster, Domainesia | Proyek kecil, mudah, murah |
| **VPS (Virtual Private Server)** | DigitalOcean, Vultr, Linode | Lebih fleksibel, kontrol penuh |
| **PaaS** | Railway, Render, Heroku | Deploy mudah via Git |
| **Cloud** | AWS, Google Cloud, Azure | Skala besar, enterprise |
| **Self-hosted** | Server kampus, PC sendiri | Development/belajar |

### Deploy ke Shared Hosting (cPanel)

```bash
# 1. Optimasi Laravel untuk produksi
php artisan config:cache
php artisan route:cache
php artisan view:cache
php artisan optimize

# 2. Atur .env untuk produksi
APP_ENV=production
APP_DEBUG=false      # ← WAJIB false di produksi!
APP_URL=https://domain-anda.com
```

```
3. Upload file via FTP/cPanel File Manager:
   - Upload semua file KECUALI folder vendor/ dan node_modules/
   - Upload file lewat Git jika hosting mendukung

4. Pindahkan folder public/ ke public_html/:
   - Konten public/ → public_html/
   - Ubah index.php di public_html:
     require __DIR__.'/../namaproyek/vendor/autoload.php';
     $app = require_once __DIR__.'/../namaproyek/bootstrap/app.php';

5. Buat database dan import skema di phpMyAdmin

6. Update .env dengan kredensial database hosting

7. Jalankan: php artisan migrate --force
```

### Deploy ke VPS (Ubuntu)

```bash
# 1. Koneksi ke VPS
ssh user@ip-server

# 2. Install dependensi
sudo apt update && sudo apt install -y \
  nginx php8.3-fpm php8.3-mysql php8.3-mbstring \
  php8.3-xml php8.3-curl php8.3-zip unzip git

# 3. Clone proyek
cd /var/www
git clone https://github.com/username/proyek.git
cd proyek

# 4. Install dependensi PHP
composer install --no-dev --optimize-autoloader

# 5. Konfigurasi
cp .env.example .env
php artisan key:generate
nano .env  # Isi DB_*, APP_URL, dll.

# 6. Migrate database
php artisan migrate --force
php artisan optimize

# 7. Atur izin folder
sudo chown -R www-data:www-data storage bootstrap/cache
sudo chmod -R 775 storage bootstrap/cache

# 8. Konfigurasi Nginx
sudo nano /etc/nginx/sites-available/proyek
```

```nginx
# /etc/nginx/sites-available/proyek
server {
    listen 80;
    server_name domain-anda.com www.domain-anda.com;
    root /var/www/proyek/public;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~ /\.(?!well-known).* {
        deny all;  # Sembunyikan file .env, .git, dll.
    }
}
```

```bash
# Aktifkan site & restart Nginx
sudo ln -s /etc/nginx/sites-available/proyek /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# 9. HTTPS dengan Let's Encrypt (gratis)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d domain-anda.com
```

---

## 10. Checklist Sebelum Go-Live

```
Konfigurasi:
☐ APP_DEBUG=false
☐ APP_ENV=production
☐ Kredensial database production (bukan localhost)
☐ APP_KEY sudah di-generate

Keamanan:
☐ HTTPS aktif (sertifikat SSL terpasang)
☐ File .env tidak bisa diakses publik
☐ Folder .git tidak bisa diakses publik
☐ Pesan error tidak menampilkan detail teknis

Database:
☐ Migrasi sudah dijalankan
☐ Data seed (jika perlu) sudah dijalankan
☐ Backup database terjadwal

Performa:
☐ Config cache aktif (artisan config:cache)
☐ Route cache aktif (artisan route:cache)
☐ Aset di-minify (CSS/JS)
☐ Gambar dioptimasi

Pengujian Akhir:
☐ Registrasi & login berfungsi
☐ CRUD berfungsi
☐ Form validasi berfungsi
☐ Tampilan responsif di mobile
```

---

## 🏗️ Proyek Praktikum

**Finalisasi & Deploy Proyek Kelompok**:

1. Lakukan code review bersama tim
2. Perbaiki semua bug yang ditemukan
3. Lakukan pengujian menyeluruh
4. Buat dokumentasi README.md
5. Deploy ke hosting pilihan (Railway/Render/Niagahoster)
6. Presentasikan hasil kepada dosen

**Isi README.md**:
- Nama proyek & deskripsi
- Fitur utama
- Anggota tim
- Teknologi yang digunakan
- Cara instalasi & menjalankan (development)
- URL demo (produksi)
- Screenshot

---

## 🏋️ Latihan

1. Coba uji aplikasi Anda dengan memasukkan `<script>alert('test')</script>` pada setiap kolom input. Apakah aman?
2. Periksa apakah file `.env` bisa diakses secara publik melalui browser.
3. Tulis satu unit test untuk salah satu fitur aplikasi Anda.
4. Deploy aplikasi ke **Railway** (free tier) dan bagikan URL-nya.

---

## 📚 Referensi

- [OWASP Top 10](https://owasp.org/Top10/)
- [Laravel Security](https://laravel.com/docs/security)
- [PHP: The Right Way — Security](https://phptherightway.com/#security)
- [Laravel Deployment](https://laravel.com/docs/deployment)
