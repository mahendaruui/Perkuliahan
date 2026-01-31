# SOAL UJIAN AKHIR SEMESTER (UAS)
# ALGORITMA DAN PEMROGRAMAN

---

**Mata Kuliah**: Algoritma dan Pemrograman  
**Waktu**: 120 menit  
**Sifat**: Closed Book  
**Jumlah Soal**: 5 Soal

---

## PETUNJUK UMUM

1. Bacalah setiap soal dengan teliti sebelum menjawab
2. Kerjakan soal yang Anda anggap mudah terlebih dahulu
3. Tuliskan kode program dengan rapi dan berikan komentar yang jelas
4. Untuk soal pemrograman, Anda boleh menggunakan bahasa pemrograman: **Python**, **C++**, atau **Java**
5. Pastikan kode program yang Anda tulis dapat dikompilasi/dijalankan tanpa error
6. Tulis algoritma atau pseudocode terlebih dahulu jika diminta

---

## SOAL 1: ARRAY DAN PERULANGAN (Bobot: 20%)

### Deskripsi Soal

Buatlah program untuk mengelola data nilai mahasiswa dalam sebuah kelas. Program harus dapat:

1. Menerima input jumlah mahasiswa (N)
2. Menerima input nilai untuk setiap mahasiswa (0-100)
3. Menampilkan:
   - Nilai tertinggi
   - Nilai terendah
   - Rata-rata nilai
   - Jumlah mahasiswa yang lulus (nilai ≥ 60)
   - Jumlah mahasiswa yang tidak lulus (nilai < 60)

### Contoh Input/Output

```
Masukkan jumlah mahasiswa: 5
Masukkan nilai mahasiswa ke-1: 85
Masukkan nilai mahasiswa ke-2: 70
Masukkan nilai mahasiswa ke-3: 55
Masukkan nilai mahasiswa ke-4: 90
Masukkan nilai mahasiswa ke-5: 65

=== HASIL ANALISIS ===
Nilai Tertinggi: 90
Nilai Terendah: 55
Rata-rata Nilai: 73.0
Jumlah Lulus: 4 mahasiswa
Jumlah Tidak Lulus: 1 mahasiswa
```

### Yang Harus Dikerjakan

a) **[5 poin]** Tuliskan **algoritma** atau **pseudocode** untuk menyelesaikan masalah di atas

b) **[15 poin]** Implementasikan algoritma tersebut dalam bahasa pemrograman pilihan Anda (Python/C++/Java)

---

## SOAL 2: FUNGSI DAN REKURSI (Bobot: 20%)

### Deskripsi Soal

Deret Fibonacci adalah deret bilangan yang dimulai dengan 0 dan 1, kemudian setiap bilangan berikutnya adalah hasil penjumlahan dua bilangan sebelumnya.

Contoh: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

### Yang Harus Dikerjakan

a) **[8 poin]** Buatlah **fungsi rekursif** dengan nama `fibonacci(n)` yang mengembalikan bilangan Fibonacci ke-n.

   **Contoh:**
   - `fibonacci(0)` → 0
   - `fibonacci(1)` → 1
   - `fibonacci(5)` → 5
   - `fibonacci(8)` → 21

b) **[7 poin]** Buatlah **fungsi iteratif** (menggunakan perulangan) dengan nama `fibonacciIteratif(n)` yang melakukan hal yang sama.

c) **[5 poin]** Jelaskan **perbedaan** antara pendekatan rekursif dan iteratif dalam menghitung Fibonacci, serta **kelebihan dan kekurangan** masing-masing pendekatan.

---

## SOAL 3: STRING DAN MANIPULASI DATA (Bobot: 20%)

### Deskripsi Soal

Buatlah program untuk menganalisis sebuah kalimat yang diinput oleh user. Program harus dapat menghitung dan menampilkan:

1. Jumlah total karakter (termasuk spasi)
2. Jumlah total karakter (tanpa spasi)
3. Jumlah kata
4. Jumlah huruf vokal (a, i, u, e, o - case insensitive)
5. Jumlah huruf konsonan
6. Kalimat dalam bentuk UPPERCASE
7. Kalimat dalam bentuk lowercase
8. Kalimat dengan urutan kata terbalik

### Contoh Input/Output

```
Masukkan kalimat: Algoritma dan Pemrograman

=== HASIL ANALISIS ===
Total karakter (dengan spasi): 26
Total karakter (tanpa spasi): 24
Jumlah kata: 3
Jumlah vokal: 10
Jumlah konsonan: 14
UPPERCASE: ALGORITMA DAN PEMROGRAMAN
lowercase: algoritma dan pemrograman
Kata terbalik: Pemrograman dan Algoritma
```

### Yang Harus Dikerjakan

a) **[5 poin]** Tuliskan **algoritma** untuk menyelesaikan masalah di atas

b) **[15 poin]** Implementasikan program lengkap dalam bahasa pemrograman pilihan Anda

**Hint:** Gunakan fungsi-fungsi string yang tersedia di bahasa pemrograman Anda.

---

## SOAL 4: ALGORITMA PENCARIAN DAN PENGURUTAN (Bobot: 20%)

### Deskripsi Soal

Sebuah perpustakaan memiliki data buku dengan kode buku berupa angka. Buatlah program untuk mengelola data kode buku tersebut.

### Data Awal

```
Kode Buku: [45, 23, 67, 12, 89, 34, 56, 78, 90, 11]
```

### Yang Harus Dikerjakan

a) **[8 poin]** Implementasikan **algoritma Bubble Sort** untuk mengurutkan kode buku dari yang terkecil ke terbesar. Tampilkan hasil setiap iterasi/pass.

   **Output yang diharapkan:**
   ```
   Data Awal: [45, 23, 67, 12, 89, 34, 56, 78, 90, 11]
   
   Pass 1: [23, 45, 12, 67, 34, 56, 78, 89, 11, 90]
   Pass 2: [23, 12, 45, 34, 56, 67, 78, 11, 89, 90]
   Pass 3: [12, 23, 34, 45, 56, 67, 11, 78, 89, 90]
   ...
   
   Data Terurut: [11, 12, 23, 34, 45, 56, 67, 78, 89, 90]
   ```

b) **[7 poin]** Setelah data terurut, implementasikan **algoritma Binary Search** untuk mencari kode buku tertentu. Program harus menampilkan:
   - Apakah kode buku ditemukan atau tidak
   - Jika ditemukan, di posisi/indeks berapa
   - Berapa kali perbandingan yang dilakukan

   **Contoh:**
   ```
   Masukkan kode buku yang dicari: 56
   
   Kode buku 56 DITEMUKAN pada indeks ke-5
   Jumlah perbandingan: 3 kali
   ```

c) **[5 poin]** Jelaskan mengapa **Binary Search lebih efisien** daripada **Linear Search** untuk data yang sudah terurut. Sertakan analisis kompleksitas waktu (Big O) dari kedua algoritma.

---

## SOAL 5: STUDI KASUS KOMPREHENSIF (Bobot: 20%)

### Deskripsi Soal

Buatlah program **Sistem Manajemen Toko Buku Sederhana** dengan fitur-fitur berikut:

### Fitur Program

1. **Tambah Buku**
   - Input: Kode Buku, Judul Buku, Harga, Stok
   - Maksimal 50 buku

2. **Tampilkan Semua Buku**
   - Menampilkan semua data buku dalam bentuk tabel

3. **Cari Buku** (berdasarkan kode buku)
   - Menggunakan algoritma pencarian
   - Tampilkan detail buku jika ditemukan

4. **Update Stok**
   - Input: Kode Buku, Jumlah Perubahan Stok (bisa + atau -)
   - Validasi: stok tidak boleh negatif

5. **Urutkan Buku** (berdasarkan harga, ascending)
   - Menggunakan algoritma pengurutan pilihan Anda

6. **Statistik**
   - Total buku yang tersedia
   - Total nilai inventori (sum of: harga × stok untuk semua buku)
   - Buku termahal
   - Buku termurah

7. **Keluar**

### Contoh Tampilan Menu

```
=== SISTEM MANAJEMEN TOKO BUKU ===
1. Tambah Buku
2. Tampilkan Semua Buku
3. Cari Buku
4. Update Stok
5. Urutkan Buku (berdasarkan Harga)
6. Statistik
7. Keluar

Pilih menu [1-7]: _
```

### Yang Harus Dikerjakan

a) **[5 poin]** Buatlah **struktur data** yang tepat untuk menyimpan informasi buku (bisa menggunakan array of struct/class atau array paralel)

b) **[10 poin]** Implementasikan **minimal 4 fitur** dari 7 fitur yang diminta (wajib: Tambah Buku, Tampilkan Semua Buku, dan 2 fitur lainnya)

c) **[5 poin]** Implementasikan **validasi input** yang baik:
   - Kode buku tidak boleh duplikat
   - Harga dan stok harus positif
   - Menu yang dipilih harus valid (1-7)

### Kriteria Penilaian

- **Fungsionalitas**: Program berjalan sesuai spesifikasi (40%)
- **Struktur Kode**: Penggunaan fungsi/prosedur yang tepat (30%)
- **Validasi & Error Handling**: Penanganan input yang baik (20%)
- **Kerapian Kode**: Indentasi, komentar, penamaan variabel (10%)

---

## KRITERIA PENILAIAN KESELURUHAN

| **Aspek** | **Kriteria** | **Bobot** |
|-----------|--------------|-----------|
| **Ketepatan Algoritma** | Algoritma/pseudocode benar dan logis | 20% |
| **Implementasi Kode** | Kode dapat dijalankan tanpa error | 40% |
| **Efisiensi** | Penggunaan struktur data dan algoritma yang tepat | 15% |
| **Kerapian & Dokumentasi** | Kode rapi, terstruktur, dan terdokumentasi | 15% |
| **Kreativitas** | Solusi kreatif dan penambahan fitur bonus | 10% |

---

## CATATAN PENTING

1. **Keaslian**: Kerjakan sendiri. Plagiarisme akan mendapat nilai 0
2. **Bahasa Pemrograman**: Pilih salah satu (Python/C++/Java) dan gunakan konsisten
3. **Pengumpulan**: 
   - File source code (.py/.cpp/.java)
   - Screenshot output program
   - Dokumentasi singkat (cara menjalankan program)
4. **Bonus**: +5 poin untuk setiap fitur tambahan yang kreatif dan bermanfaat pada Soal 5

---

## RUBRIK PENILAIAN PER SOAL

### Soal 1-4 (Masing-masing 20 poin)

| **Nilai** | **Kriteria** |
|-----------|--------------|
| 18-20 | Sempurna: Algoritma benar, implementasi lengkap, output sesuai |
| 15-17 | Baik: Algoritma benar, implementasi hampir lengkap, sedikit error |
| 12-14 | Cukup: Algoritma cukup benar, implementasi parsial, beberapa error |
| 8-11 | Kurang: Algoritma kurang tepat, implementasi tidak lengkap |
| 0-7 | Sangat Kurang: Tidak mengerjakan atau sangat tidak sesuai |

### Soal 5 (20 poin)

| **Nilai** | **Kriteria** |
|-----------|--------------|
| 18-20 | Implementasi 6-7 fitur, semua berjalan sempurna, validasi lengkap |
| 15-17 | Implementasi 4-5 fitur, berjalan baik, validasi cukup |
| 12-14 | Implementasi 3-4 fitur, berjalan dengan beberapa bug |
| 8-11 | Implementasi 2-3 fitur, banyak bug |
| 0-7 | Implementasi < 2 fitur atau tidak berjalan |

---

## TIPS MENGERJAKAN

1. **Baca Semua Soal**: Pahami semua soal terlebih dahulu sebelum mulai mengerjakan
2. **Manajemen Waktu**: Alokasikan waktu yang seimbang untuk setiap soal
3. **Tulis Algoritma Dulu**: Untuk soal yang meminta algoritma, tulis dulu sebelum coding
4. **Test Program**: Pastikan program di-test dengan berbagai input
5. **Komentar Kode**: Berikan komentar untuk bagian-bagian penting
6. **Backup**: Simpan file Anda secara berkala

---

**SELAMAT MENGERJAKAN!** 🚀

*Kejujuran adalah kunci kesuksesan. Percayalah pada kemampuan Anda sendiri.*

---

**Dibuat oleh**: Tim Pengajar Algoritma dan Pemrograman  
**Semester**: Ganjil 2025/2026  
**Tanggal**: Januari 2026
