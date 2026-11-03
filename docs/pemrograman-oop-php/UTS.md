# Ujian Tengah Semester (UTS) — Tugas Proyek Kelompok

**Mata Kuliah:** Pemrograman Berorientasi Objek (PHP 8+) — **IFR 214**
**Bobot:** 20% dari nilai akhir · **Sifat:** Kelompok (8 kelompok) · **Minggu:** 8
**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.

::: info 📌 Ringkasan Tugas
Setiap kelompok membangun **satu aplikasi OOP PHP 8+** sesuai tema yang ditetapkan. Proyek **wajib** menerapkan seluruh materi Minggu 1–7: *class & object, typed properties, constructor, method, encapsulation, inheritance, trait, polymorphism,* dan *abstraction (abstract class & interface)*. Data disimpan **in-memory (array)** — belum menggunakan database, Composer, file I/O, maupun exception handling karena materi tersebut baru diajarkan setelah UTS.
:::

---

## 🎯 Capaian yang Diuji

| Kode | Capaian | Bukti dalam Proyek |
| :--- | :--- | :--- |
| **CPMK-1** | Menjelaskan paradigma OOP | Penjelasan desain pada laporan |
| **CPMK-2** | Class, object, constructor, method | Struktur class & instansiasi objek |
| **CPMK-3** | Encapsulation, inheritance, polymorphism, abstraction | Penerapan 4 pilar pada kode |
| **CPL-KU1** | Berpikir logis & sistematis | Alur program & relasi antar class |
| **CPL-KK1** | Merancang & mendokumentasikan aplikasi | Dokumentasi desain class & README |
| **CPL-S1** | Kerja sama & etika akademik | Kontribusi tim & keaslian kode |

**Sub-CPMK 1–7:** konsep OOP · class & object · constructor & method · encapsulation · inheritance · polymorphism · abstraction.

---

## 📌 Ketentuan Umum

### A. Keanggotaan
1. Satu kelompok terdiri atas **4–5 mahasiswa**.
2. Setiap anggota **wajib** memiliki kontribusi yang jelas, dicantumkan pada tabel pembagian tugas di laporan.
3. Tema ditetapkan oleh dosen (lihat pembagian tema di bawah) dan **tidak boleh ditukar** tanpa persetujuan.

### B. Teknologi & Batasan
| Diperbolehkan | Dilarang (materi pasca-UTS) |
| :--- | :--- |
| PHP 8.1+ murni (tanpa framework) | Database (MySQL/PDO) |
| CLI (`php app.php`) atau HTML sederhana | Composer / Namespace / PSR-4 |
| Array sebagai penyimpanan in-memory | File I/O (`fopen`, `fwrite`, `json_encode` ke file) |
| Arsip ZIP (`.zip`) | Exception handling lanjutan (`try-catch`) |
| `declare(strict_types=1)` | Framework (Laravel, Symfony), library eksternal |

### C. Ketentuan Teknis Wajib
- [ ] Setiap file diawali `<?php` dan `declare(strict_types=1);`
- [ ] **Minimal 6 class** (tidak termasuk class pemanggil/`main`).
- [ ] **Minimal 1 abstract class** dan **1 interface**.
- [ ] **Minimal 1 trait** untuk *horizontal code reuse*.
- [ ] **Semua properti** bersifat `private` atau `protected` + getter/setter (encapsulation).
- [ ] **Inheritance minimal 2 level** (`abstract class → class konkret` dihitung 1 level; tambahkan turunan konkret).
- [ ] **Polymorphism** dibuktikan melalui parameter bertipe `interface`/`abstract class` yang menerima beberapa implementasi.
- [ ] Menggunakan **typed properties**, **constructor promotion**, dan **method dengan return type**.
- [ ] Program dapat dijalankan **tanpa error** dan menampilkan output yang dapat dibaca.
- [ ] Struktur folder rapi: `src/` (class), `app.php` (runner), `README.md`.

::: warning ⚠️ Aturan penilaian penting
Proyek yang **tidak** memiliki abstract class **atau** interface **atau** trait akan kehilangan komponen nilai "Penerapan 4 Pilar" secara signifikan. Setiap properti `public` yang seharusnya dienkapsulasi akan mengurangi nilai *Kualitas Desain*.
:::

---

## 🧩 Pembagian 8 Tema Proyek

| Kelompok | Tema Proyek | Fokus OOP Utama |
| :---: | :--- | :--- |
| **1** | Sistem Kasir Toko Retail (POS Mini) | Abstract produk · interface diskon · trait log |
| **2** | Sistem Perpustakaan Kampus | Abstract item · interface pinjam · trait denda |
| **3** | Sistem Akademik (SIAKAD Mini) | Abstract orang · interface penilaian · trait identitas |
| **4** | Sistem Klinik & Rekam Medis | Abstract tenaga medis · interface layanan · trait jadwal |
| **5** | Sistem Parkir Kendaraan | Abstract kendaraan · interface tarif · trait durasi |
| **6** | Sistem Penggajian Karyawan | Abstract karyawan · interface hitung gaji · trait absensi |
| **7** | Sistem E-Commerce Sederhana | Abstract produk · interface pembayaran · trait keranjang |
| **8** | Sistem Reservasi Hotel | Abstract kamar · interface layanan · trait reservasi |

---

## 🛒 Kelompok 1 — Sistem Kasir Toko Retail (POS Mini)

**Kasus:** Sebuah toko kelontong membutuhkan aplikasi kasir sederhana untuk mencatat produk, menghitung total belanja, menerapkan diskon, dan memproses pembayaran.

**Fitur wajib:**
1. Menampilkan daftar produk (nama, harga, stok).
2. Menambahkan produk ke keranjang beserta jumlah.
3. Menghitung subtotal, diskon, dan total akhir.
4. Memproses pembayaran (tunai/QRIS) dan menghitung kembalian.
5. Mengurangi stok secara otomatis setelah transaksi.

**Rancangan class minimum:**
- `abstract class Produk` → turunan `ProdukMakanan`, `ProdukElektronik`.
- `interface Diskon` → `DiskonPersen`, `DiskonNominal`.
- `interface Pembayaran` → `Tunai`, `Qris`.
- `trait LogTransaksi` → mencatat riwayat transaksi.
- Class pendukung: `ItemKeranjang`, `Keranjang`, `Kasir`.

**Output minimum:** struk belanja berisi daftar item, subtotal, diskon, total, metode bayar, dan kembalian.

---

## 📚 Kelompok 2 — Sistem Perpustakaan Kampus

**Kasus:** Perpustakaan UUI membutuhkan sistem pencatatan peminjaman buku, anggota, dan perhitungan denda keterlambatan.

**Fitur wajib:**
1. Menampilkan daftar koleksi (buku, majalah, jurnal).
2. Mendaftarkan anggota (mahasiswa/dosen) dengan batas pinjam berbeda.
3. Memproses peminjaman dan pengembalian.
4. Menghitung denda berdasarkan jumlah hari keterlambatan.
5. Menampilkan status ketersediaan setiap item.

**Rancangan class minimum:**
- `abstract class ItemPustaka` → `Buku`, `Majalah`, `Jurnal`.
- `interface BisaDipinjam` → diterapkan pada item yang dapat dipinjam.
- `trait PerhitunganDenda` → logika denda per hari.
- Class pendukung: `Anggota`, `Mahasiswa`, `Dosen`, `Peminjaman`, `Perpustakaan`.

**Output minimum:** daftar pinjaman aktif + simulasi pengembalian dengan denda.

---

## 🎓 Kelompok 3 — Sistem Akademik (SIAKAD Mini)

**Kasus:** Program studi membutuhkan sistem untuk mengelola data mahasiswa, dosen, mata kuliah, KRS, dan nilai akhir.

**Fitur wajib:**
1. Menampilkan data mahasiswa dan dosen.
2. Menampilkan daftar mata kuliah beserta SKS.
3. Mengambil mata kuliah (KRS) dengan validasi batas SKS.
4. Menghitung nilai akhir dari komponen tugas, UTS, dan UAS.
5. Menampilkan transkrip nilai dan IPK sederhana.

**Rancangan class minimum:**
- `abstract class Orang` → `Mahasiswa`, `Dosen`.
- `interface Penilaian` → `NilaiHuruf`, `NilaiAngka` (atau strategi bobot nilai).
- `trait Identitas` → NIM/NIDN, nama, program studi.
- Class pendukung: `MataKuliah`, `KRS`, `Transkrip`.

**Output minimum:** KRS mahasiswa + transkrip nilai dengan IPK.

---

## 🩺 Kelompok 4 — Sistem Klinik & Rekam Medis

**Kasus:** Klinik kampus membutuhkan sistem pendaftaran pasien, jadwal dokter, dan pencatatan rekam medis sederhana.

**Fitur wajib:**
1. Menampilkan daftar dokter dan jadwal praktik.
2. Mendaftarkan pasien (umum/asuransi) dengan nomor rekam medis.
3. Membuat janji konsultasi sesuai jadwal.
4. Mencatat diagnosis dan resep obat.
5. Menghitung total biaya layanan (konsultasi + obat).

**Rancangan class minimum:**
- `abstract class TenagaMedis` → `DokterUmum`, `DokterSpesialis`.
- `interface BisaDiperiksa` → layanan konsultasi.
- `trait JadwalPraktik` → hari & jam praktik.
- Class pendukung: `Pasien`, `RekamMedis`, `Resep`, `Klinik`.

**Output minimum:** ringkasan kunjungan pasien (dokter, diagnosis, resep, total biaya).

---

## 🅿️ Kelompok 5 — Sistem Parkir Kendaraan

**Kasus:** Area parkir kampus membutuhkan sistem pencatatan kendaraan masuk/keluar dan perhitungan tarif otomatis.

**Fitur wajib:**
1. Mencatat kendaraan masuk beserta jenis dan plat nomor.
2. Menghitung durasi parkir dari jam masuk dan keluar.
3. Menghitung tarif berbeda untuk motor, mobil, dan truk.
4. Menampilkan kapasitas slot parkir tersisa.
5. Mencetak struk parkir dan total pendapatan harian.

**Rancangan class minimum:**
- `abstract class Kendaraan` → `Motor`, `Mobil`, `Truk`.
- `interface Tarif` → strategi tarif per jam/harian.
- `trait Durasi` → perhitungan selisih waktu.
- Class pendukung: `TiketParkir`, `SlotParkir`, `AreaParkir`.

**Output minimum:** struk parkir + rekap pendapatan dan sisa slot.

---

## 💼 Kelompok 6 — Sistem Penggajian Karyawan

**Kasus:** Perusahaan membutuhkan sistem perhitungan gaji karyawan tetap, kontrak, dan magang dengan komponen lembur serta potongan.

**Fitur wajib:**
1. Menampilkan data karyawan berdasarkan jenis kontrak.
2. Mencatat absensi dan jam lembur.
3. Menghitung uang lembur dengan tarif per jam.
4. Menghitung potongan (mis. BPJS/asuransi) sesuai jenis karyawan.
5. Mencetak slip gaji lengkap.

**Rancangan class minimum:**
- `abstract class Karyawan` → `KaryawanTetap`, `KaryawanKontrak`, `KaryawanMagang`.
- `interface HitungGaji` → kontrak perhitungan gaji.
- `trait Absensi` → rekap hadir & lembur.
- Class pendukung: `SlipGaji`, `Perusahaan`.

**Output minimum:** slip gaji dua karyawan berbeda jenis dengan rincian komponen.

---

## 🛍️ Kelompok 7 — Sistem E-Commerce Sederhana

**Kasus:** Toko online sederhana membutuhkan katalog produk, keranjang belanja, dan beberapa metode pembayaran.

**Fitur wajib:**
1. Menampilkan katalog produk fisik dan digital.
2. Menambahkan produk ke keranjang (jumlah tervalidasi stok).
3. Menghitung ongkos kirim khusus produk fisik.
4. Memproses checkout dengan metode pembayaran berbeda.
5. Menampilkan ringkasan pesanan dan status pembayaran.

**Rancangan class minimum:**
- `abstract class Produk` → `ProdukFisik`, `ProdukDigital`.
- `interface Pembayaran` → `TransferBank`, `COD`, `EWallet`.
- `trait Keranjang` → operasi tambah/hapus/hitung total.
- Class pendukung: `ItemPesanan`, `Pesanan`, `Toko`.

**Output minimum:** ringkasan pesanan (produk, ongkir, total, metode bayar, status).

---

## 🏨 Kelompok 8 — Sistem Reservasi Hotel

**Kasus:** Hotel membutuhkan sistem pemesanan kamar dengan tipe kamar berbeda dan layanan tambahan.

**Fitur wajib:**
1. Menampilkan daftar kamar dan status ketersediaan.
2. Mendaftarkan tamu dan membuat reservasi (check-in/check-out).
3. Menghitung biaya menginap berdasarkan tipe kamar dan lama inap.
4. Menambahkan layanan tambahan (sarapan, laundry, antar-jemput).
5. Mencetak invoice reservasi.

**Rancangan class minimum:**
- `abstract class Kamar` → `KamarStandard`, `KamarDeluxe`, `KamarSuite`.
- `interface LayananTambahan` → layanan berbayar.
- `trait Reservasi` → validasi tanggal & durasi.
- Class pendukung: `Tamu`, `Invoice`, `Hotel`.

**Output minimum:** invoice reservasi lengkap dengan rincian kamar + layanan.

---

## 📦 Artefak yang Dikumpulkan

| No | Artefak | Keterangan |
| :--: | :--- | :--- |
| 1 | **Berkas ZIP (Source Code)** | Folder `src/`, `app.php`, dan `README.md` — dikompres ke dalam satu arsip |
| 2 | **Laporan PDF** | Memuat **screenshot kode**, **hasil pengujian**, dan **pembahasan** |
| 3 | **Slide Presentasi** | PDF/PPTX, maksimal 8 slide |

**Format nama berkas:** `UTS_PBO_Kelompok-XX_Judul.zip` — berisi laporan, slide, dan seluruh source code. Diunggah melalui **Edlink (Sevima)**.

### 📤 Ketentuan Pengumpulan (Edlink / Sevima)

1. Kumpulkan **satu berkas ZIP** melalui menu tugas UTS pada platform **Edlink (Sevima)**.
2. Struktur di dalam ZIP:
   ```text
   UTS_PBO_Kelompok-XX_Judul/
   ├── Laporan_UTS_Kelompok-XX.pdf
   ├── Slide_UTS_Kelompok-XX.pdf
   └── source-code/
       ├── src/            # seluruh class
       ├── app.php         # runner program
       └── README.md       # cara menjalankan
   ```
3. Pastikan ZIP **dapat diekstrak** dan program berjalan dengan `php app.php` setelah diekstrak.
4. Hanya **ketua kelompok** yang mengunggah; seluruh anggota tetap mencantumkan nama pada laporan.
5. Simpan bukti unggah (screenshot konfirmasi Edlink) sampai nilai keluar.

::: warning ⚠️ Berkas rusak atau tidak dapat diekstrak
Arsip yang corrupt, kosong, atau tidak berisi source code dianggap **belum mengumpulkan** dan mengikuti ketentuan keterlambatan.
:::

---

## 📊 Rubrik Penilaian (Bobot UTS 20%)

| Kriteria | Bobot | Indikator Sangat Baik (86–100) | Cukup (70–85) | Kurang (< 70) |
| :--- | :---: | :--- | :--- | :--- |
| **Penerapan 4 Pilar OOP** | 30% | Encapsulation, inheritance, polymorphism, abstraction diterapkan tepat & bermakna | Sebagian diterapkan, ada yang dipaksakan | Minimal/tidak sesuai konsep |
| **Kualitas Desain Class** | 20% | Relasi class logis, tanggung jawab tunggal, penamaan konsisten | Ada duplikasi/tanggung jawab bercampur | Desain berantakan (spaghetti) |
| **Kelengkapan Fitur** | 20% | Semua fitur wajib berjalan sesuai kasus | Sebagian fitur berjalan | Banyak fitur tidak berfungsi |
| **Kualitas Kode & Dokumentasi** | 15% | `strict_types`, typed properties, README & komentar jelas | Cukup rapi, dokumentasi minim | Tidak konsisten, sulit dibaca |
| **Pembahasan & Presentasi** | 15% | Pembahasan analitis & menjawab pertanyaan teknis | Menjelaskan dasar | Tidak menguasai kode |

::: tip 💡 Tips memperoleh nilai tinggi
Fokus pada **kualitas desain**, bukan jumlah fitur. Satu sistem dengan 6 class yang relasi OOP-nya tepat dan bersih lebih bernilai daripada 15 class yang saling tumpang tindih tanggung jawab.
:::

---

## 🗓️ Linimasa Pengerjaan

| Pekan | Aktivitas | Output |
| :---: | :--- | :--- |
| **8 (UTS)** | Pengumuman tema & pembentukan kelompok | Daftar anggota |
| **8** | Konsultasi desain class (online/kelas) | Draft desain class |
| **9** | Pengumpulan progres + review desain | Berkas progres + desain class revisi |
| **9** | **Batas akhir pengumpulan** | Arsip ZIP (laporan + source code + slide) |
| **10** | Presentasi & tanya jawab kelompok | Slide |

::: warning ⚠️ Keterlambatan
Pengumpulan melewati batas waktu dikenakan pengurangan **10% per hari** (maksimal 3 hari). Setelah itu dianggap tidak mengumpulkan kecuali ada alasan medis/force majeure yang dibuktikan.
:::

---

## 📝 Format Laporan

1. **Halaman Judul** — judul sistem, nomor kelompok, nama & NIM.
2. **Latar Belakang & Rumusan Masalah** (1 halaman).
3. **Desain Sistem** — daftar class, abstract class, interface, dan trait beserta perannya masing-masing.
4. **Screenshot Kode** — tangkapan layar potongan kode inti untuk setiap pilar OOP (encapsulation, inheritance, polymorphism, abstraction), disertai penjelasan singkat.
5. **Hasil Pengujian** — tangkapan layar output program untuk setiap fitur wajib (minimal 5 skenario).
6. **Pembahasan** — analisis mengapa desain tersebut dipilih, kendala yang dihadapi, dan alternatif solusi yang dipertimbangkan.
7. **Pembagian Tugas** — tabel kontribusi per anggota (kode & laporan).
8. **Kesimpulan & Saran.**

---

## 🛡️ Integritas Akademik

- Kode harus **asli karya kelompok**. Mengambil kode dari repositori lain tanpa atribusi = **plagiarisme** (nilai 0).
- Referensi eksternal (dokumentasi PHP, artikel) **boleh**, tetapi wajib dicantumkan di README.
- Seluruh anggota harus mampu menjelaskan **bagian kodenya sendiri** saat presentasi. Ketidakmampuan menjelaskan akan mengurangi nilai individu.

---

## ✅ Checklist Sebelum Mengumpulkan

- [ ] Program berjalan tanpa error (`php app.php`).
- [ ] Minimal 6 class, 1 abstract class, 1 interface, 1 trait.
- [ ] Semua properti `private`/`protected` + getter/setter.
- [ ] Ada inheritance minimal 2 level.
- [ ] Polymorphism terlihat pada parameter bertipe interface/abstract.
- [ ] `declare(strict_types=1)` di semua file.
- [ ] README berisi cara menjalankan & daftar fitur.
- [ ] Laporan memuat **screenshot kode**, **hasil pengujian**, dan **pembahasan**.
- [ ] Tabel pembagian tugas mencantumkan kontribusi setiap anggota.
- [ ] Laporan PDF dan slide presentasi lengkap.

> [!TIP]
> Unggah **satu berkas ZIP** melalui **Edlink (Sevima)** sebelum tenggat. Pastikan arsip berisi laporan, slide, dan seluruh source code, serta dapat diekstrak dan dijalankan tanpa error.
