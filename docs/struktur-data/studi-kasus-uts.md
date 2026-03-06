# Minggu 7 & 8 — Studi Kasus Linear Data & Evaluasi UTS

Selamat! Anda telah sampai di pertengahan semester perkuliahan Struktur Data dasar.
Sebelum melangkah ke jenis data memori **Non-Linear (Tree & Graph)** di minggu ke-9, sangat disarankan mahasiswa mengulang kembali materi dan mematangkan logika implementasinya.

## 1. Topik Refleksi Utama
Pastikan Anda sudah menguasai:
1. Perbedaan mutlak Array statis Golang vs Slice Dinamis. Konsep `len()` vs `cap()`.
2. Penugasan Nilai vs Penugasan Referensi (Pointer `*` dan Address `&`).
3. Menggunakan Objek Abstract (`struct`).
4. Membangun Stack (LIFO).
5. Membangun Queue (FIFO) menggunakan Slice/Array (*termasuk kelemahannya*).
6. Merangkai Singly Linked List via Node & Next Pointer.

## 2. Studi Kasus Mingguan Terpadu
Kasus ini seringkali menjadi pertimbangan di ujian tertulis tengah semester (UTS):

### A. Evaluasi Penggunaan Stack vs Queue
Diberikan sebuah kondisi sistem: *Antrean Cetak Dokumen (Printer)*.
Jika 5 orang mengirim instruksi print berurutan (Dokumen A, B, C, D, E). 
- Manakah di antara Stack dan Queue yang paling tepat merepresentasikan sistem memori *Print Spooler*? 
- **Jawabannya:** Queue (FIFO). Karena sangat aneh jika Dokumen C yang belum lama disubmit, di-print duluan menimpa orang pertama (Dokumen A).
- Modifikasi masalah: *Akan tetapi Dosen punya dokumen Urgent (Dokumen F) yang harus mendahului antrean!*
- **Solusi Lanjutan:** Sistem Printer sejatinya menggunakan *Priority Queue*, modifikasi dari Queue yang meletakkan elemen di depan `Front` berdasarkan nilai urgensi pembobotan objek Struct.

### B. Evaluasi Penggunaan Linked List vs Array/Slice
Diberikan kasus: *Phonebook atau Kontak Handphone yang jumlahnya mencapai 10 Juta list Data, namun jarang ada orang yang dihapus di tengah-tengah.*
Jika Anda dituntut menghemat memori komputer:
- Lebih baik Array Slice atau Linked List?
- **Jawabannya:** Array/Slice. *(Ini menjebak!)* Array menghabiskan 1 slot blok memori mutlak. Sedangkan Linked List memakan 2 blok pada setiap kontaknya: `(1 blok untuk Teks Tlp/Nama)` + `(1 blok untuk Pointer *Next)`. 
Walaupun Linked List lebih efisien saat **Tambah/Hapus node di tengah**, ia boros memori penyimpanan diam (Idle Storage) karena atribut Pointernya memakan *storage/RAM memory footprint* yang besar.

---

### **Instruksi UTS (Ujian Tengah Semester - Pertemuan 8)**
1. Sifat: *Closed Book* Evaluasi Tertulis & Analisis Kasus di Kelas.
2. Prediksi Soal Praktikal: Anda mungkin diberikan secarik kertas, dan diminta menulis kode perakitan atau modifikasi *Node* kosong menjadi *Circular Linked List*, di mana simpul terakhir kembali memeluk *Alamat (Pointer)* si Kepalanya (`Tail.Next = Head`).
3. Siapkan pemahaman perbedaan sintaksis Golang vs bahasa Pemrograman C/Java. 

*Tetap semangat! Fase berikutnya lebih menantang (Data Hierarkis).*
