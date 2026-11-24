# 📝 Minggu 08: Evaluasi Tengah Semester (UTS)

**Mata Kuliah:** Algoritma dan Pemrograman (**IFR206**) · **Bobot:** 30% dari Nilai Akhir · **Durasi:** 120 Menit · **Sifat:** Ujian Mandiri Bebas Plagiarisme

::: info 📌 Ringkasan Evaluasi UTS
Ujian Tengah Semester mengukur pencapaian kompetensi mahasiswa pada **paruh pertama semester (Minggu 1 s.d. Minggu 7)** yang mencakup **Sub-CPMK 1 hingga Sub-CPMK 4**. Evaluasi dilaksanakan melalui **Ujian Tertulis (Analisis & Trace Table)** serta **Live Coding Test Mandiri di Laboratorium** menggunakan C++ dan/atau Python 3.
:::

---

## 🎯 Capaian Pembelajaran yang Diujikan

| Minggu | Topik Utama | Sub-CPMK | Fokus Asesmen |
| :---: | :--- | :---: | :--- |
| **1** | Pengenalan Algoritma, Kriteria Knuth, Flowchart ISO 5807 & Pseudocode | Sub-CPMK 1 | Merancang flowchart presisi & menguji 5 kriteria Knuth |
| **2** | Variabel, Tipe Data, Konstanta, Alokasi RAM & Type Casting | Sub-CPMK 2 | Menghitung rentang bit, mendeteksi overflow & casting aman |
| **3** | Operator, Aljabar Boolean, Hukum De Morgan & Bitwise | Sub-CPMK 2 | Menyederhanakan ekspresi logika & evaluasi presedensi |
| **4** | Struktur Kontrol Percabangan (`if`, `if-else-if`, `nested-if`, Ternary) | Sub-CPMK 3 | Merancang cabang keputusan bersih dengan *Guard Clauses* |
| **5** | Percabangan Lanjut (`switch-case`, Fall-Through & Menu CLI) | Sub-CPMK 3 | Mengelola label diskrit, `break`, dan validasi menu CLI |
| **6** | Struktur Kontrol Perulangan (`for`, `while`, `do-while`, Nested Loop) | Sub-CPMK 3 | Menyusun *Trace Table*, akumulator, & kontrol `break`/`continue` |
| **7** | Struktur Data Larik (Array 1 Dimensi) & Two-Pointer | Sub-CPMK 4 | Pengalamatan memori kontigu, statistik array, & manipulasi indeks |

---

## 📋 Struktur Pelaksanaan & Rubrik Penilaian UTS

| Bagian Ujian | Bentuk Soal | Bobot Sesi | Durasi | Kriteria Penilaian Utama |
| :--- | :--- | :---: | :---: | :--- |
| **Bagian A — Teori & Trace Table** | Analisis kasus tertulis (tanpa eksekusi IDE) | **40%** | 45 Menit | Ketepatan simbol ISO 5807, evaluasi aljabar Boolean, serta akurasi langkah pada *Trace Table* |
| **Bagian B — Live Coding Mandiri** | Implementasi program di komputer lab | **60%** | 75 Menit | Kebenaran logika, validasi input (*defensive coding*), efisiensi iterasi/array, dan kerapian kode |

::: warning ⚠️ Ketentuan Integritas Akademik (CPL08)
Seluruh kode harus merupakan hasil pemikiran mandiri. Segala bentuk penyalinan kode antar peserta atau penggunaan solusi otomatis tanpa otorisasi selama ujian berlangsung akan berakibat pembatalan nilai UTS (**Nilai E**).
:::

---

## 🧪 Paket Latihan & Simulasi Soal UTS

### Bagian A: Analisis Algoritma & Trace Table (40%)

1. **Flowchart & Pseudocode (Minggu 1 & 4):**
   Rancanglah **Flowchart standar ISO 5807** dan **Pseudocode** untuk menghitung tarif pengiriman paket logistik:
   - Berat `≤ 0` kg: tampilkan pesan error input tidak valid.
   - Berat `≤ 2` kg: tarif dasar `Rp 12.000`.
   - Berat `> 2` kg: `Rp 12.000 + (ceil(berat - 2) × Rp 5.000)`.
   - Jika tujuan luar pulau (`isLuarPulau == true`), tambahkan biaya asuransi `10%` dari tarif.

2. **Tipe Data, Overflow & Casting (Minggu 2 & 3):**
   Perhatikan cuplikan kode C++ berikut dan tentukan keluaran persisnya serta cara memperbaikinya:
   ```cpp
   int a = 7, b = 2;
   double hasil = a / b;
   unsigned char level = 255;
   level = level + 2;
   ```
   Jelaskan mengapa nilai `hasil` bukan `3.5` dan berapa nilai `level` setelah overflow terjadi.

3. **Hukum De Morgan & Short-Circuit (Minggu 3):**
   Sederhanakan kondisi berikut menggunakan Hukum De Morgan agar tidak memiliki negasi di luar tanda kurung:
   ```text
   !(usia >= 17 && punyaKTP)
   ```

4. **Trace Table Perulangan (Minggu 6):**
   Susun *Trace Table* langkah demi langkah (`i`, `j`, `akumulator`) untuk fragmen berikut hingga selesai:
   ```text
   akumulator <- 0
   for i <- 1 to 3 do
       for j <- 1 to i do
           if (i + j) mod 2 == 0 then
               akumulator <- akumulator + (i * j)
           endif
       endfor
   endfor
   ```

---

### Bagian B: Live Coding Mandiri di Lab (60%)

#### Studi Kasus: Sistem Rekapitulasi Kehadiran & Nilai Harian Mahasiswa
Buatlah program konsol (**C++ atau Python 3**) berbasis **menu interaktif (`switch-case` / `match-case` di dalam loop)** untuk mengolah array nilai kuis `N` mahasiswa (`1 ≤ N ≤ 50`):

1. **Menu 1 — Input Data Nilai (Validasi Berulang):**
   - Menerima `N` buah nilai kuis dalam rentang `0.0 – 100.0`.
   - Jika pengguna memasukkan nilai di luar rentang, tolak dengan pesan peringatan dan minta input ulang (*uncounted loop*).
2. **Menu 2 — Statistik Larik 1D (`O(n)`):**
   - Hitung dan tampilkan **Nilai Tertinggi (Max)**, **Nilai Terendah (Min)**, **Rata-Rata Kelas**, serta **Jumlah Mahasiswa yang Mendapat Nilai A (`≥ 80.0`)**.
3. **Menu 3 — Pembalikan & Filter Urutan (Two-Pointer):**
   - Tampilkan salinan urutan nilai secara terbalik tanpa membuat array bantu tambahan (*in-place reversal*), lalu hitung berapa banyak nilai berada di bawah batas kelulusan (`< 40.0`).
4. **Menu 0 — Keluar Program:**
   - Menutup program secara bersih.

::: tip 💡 Daftar Periksa Sebelum Mengumpulkan Kode UTS
- [ ] Seluruh pembagian bilangan bulat sudah di-cast ke `double`/`float` bila membutuhkan hasil desimal.
- [ ] Tidak ada akses array di luar batas indeks (`0` hingga `N - 1`).
- [ ] Setiap cabang `case` di C++ memiliki `break`, dan input invalid tertangani oleh `default`.
- [ ] Kode ditulis rapi dengan indentasi 4 spasi dan penamaan variabel yang bermakna.
:::
