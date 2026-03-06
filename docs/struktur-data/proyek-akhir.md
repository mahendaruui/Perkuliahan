# Minggu 14 - 16 — Pengimplementasian PjBL & Evaluasi Akhir (UAS)

Berdasarkan silabus **Outcome-Based Education (OBE)**, kita dituntut tidak hanya menghapal algoritma pada saat ujian tertulis. Seorang *Software Engineer* juga harus bisa membuat **Purwarupa / Prototype** sistem dengan mempertimbangkan batas performa struktur datanya. 

Selama Pertemuan ke-14 hingga ke-16, kelas akan berfokus pada:
1. Pembentukan Tim & Penentuan Topik.
2. Konsultasi dan Presentasi Progres Sistem CLI (Minggu 14).
3. Finalisasi Kode Rangkaian Logika (Minggu 15).
4. **Ujian Akhir Semester / UAS**: Demo Proyek & Analisis Kompleksitas Final (Minggu 16).

## A. Syarat Pengerjaan Mini Proyek

1. **Bahasa Pemrograman:** Mutlak berbasis `Golang`. Anda bisa menggunakan CLI *(Command Line Interface)* di terminal, atau bisa menggunakan `net/http` untuk merendernya menjadi *REST API Endpoint* *(Opsional namun disarankan)* yang berhadapan dengan *Postman*.
2. **Kewajiban Penggunaan Teori:** Sistem **DILARANG KERAS** menggunakan modul SQL Database seperti MySQL atau PostgreSQL. Penyimpanan harus **In-Memory** murni menggunakan kumpulan variabel bertipe `struct` custom dari:
   - Salah satu Jenis *List / Stack / Queue*.
   - ATAU: Salah satu jenis Hierarkis (*Tree / Graph*).

Semakin kompleks Struktur Data Utama yang Anda panggul secara *manual (Linked List)*, nilai implementasinya (*PBL bobot 20%*) akan semakin memuaskan.

---

## B. Referensi Topik & Case Method Akhir

Jika Anda kebingungan, tim Dosen membebaskan Anda mengelaborasi topik berikut:

### Topik 1: "Sistem Manajemen Gudang & Retur Barang dengan Stack / Queue"
- Menerapkan **Stack (LIFO)** untuk barang masuk logistik (*Barang yang terakhir masuk di rak yang akan pertama dikeluarkan lagi karena terpalang masuk*).
- Menambahkan **Queue (FIFO)** untuk jalur antrean kurir ekspedisi di gudang tersebut yang menunggu jatah pengambilan paket. 
- *Challenge Tambahan:* Modulo atau *Circular Queue* saat gudang penuh.

### Topik 2: "Engine Auto-Complete (Saran Kata) Pada Fitur Pencarian dengan Tree/Trie"
- Susun jutaan kosa kata (*Dictionary*) struktur teks menjadi susunan **Trie Tree** (Salah satu jenis N-ary Tree).
- Implementasi algoritma untuk memprediksi suku kata selanjutnya saat *user* baru mengetikkan awalan kata: `"m-a... (mahasiswa, makan, macet)"`.
- Lakukan rekursif traversal mencari Child Node paling ujung dari awalan tersebut untuk mengembalikan list string prediksi ke layar.

### Topik 3: "Sistem Jaringan Pertemanan Sosial & Suggestion (Graph BFS/DFS)"
- Menerapkan **Undirected Adjacency Map Graph** untuk relasi siapa _follow_ siapa. 
- Implementasi algoritma **Breadth-First Search (BFS)** menggunakan Queue untuk merekomendasikan: *"Orang yang mungkin Anda kenal"* *(Mutual Friends level 2 atau teman dari teman Anda).*  

### Topik 4: "Mini Router Jaringan Komputer / Transportasi Jarak Terpendek (Dijkstra)"
- Seperti materi Minggu 13, perbagus fitur *Dijkstra Graph* agar mampu tidak hanya mencetak *Berapa Costnya*, tetapi **RUTENYA MENGGUNAKAN APA SAJA (Misal: A->F->J->C)**. Hal ini menuntut Anda menambah struktur *PrevNode Table Dictionary* selain dari *Distance Dictionary*.
- Siapkan skenario *Edge/Node Putus*: Modifikasi bobot peta otomatis ketika server "Sedang Banjir/Traffic Tinggi" atau jalanan ditutup.

---

## C. Kriteria Pengujian Evaluasi Akhir (UAS)

Berdasarkan pedoman OBE yang tertera pada *CPMK-15* dan *CPMK-16*: "Kemampuan menganalisis hasil dan pemecahan masalah (Bobot total evaluasi ini 30%)":

1. **Akurasi Struktur Eksekusi (10%)**
   - Apakah program *Compile Error*? *Panic Nil Pointer*? 
   - Apakah membuang *array* memicu *Garbage Collector Leak* karena penggunaan *Slice* dibandingkan manuver *Linked List Pointer* `&` yang efisien?
2. **Justifikasi Algoritma / Pertanyaan Analisis Teoritikal (10%)**
   - Saat Dosen menanyakan: "Kenapa Anda tidak menggunakan *Linear Search Array* saja alih-alih capek membangun *Binary Search Tree Database*?" Anda harus mampu menjawabnya menggunakan metrik **Big O Notation** (Misal: *Karena O(log N) membelah eksponensial ketimbang keliling satu juta barikade O(N) linier pak!*).
3. **Penyajian UI/CLI dan Kerja Tim (10%)**
   - Rapi tidaknya cetakan terminal antarmuka.

> *Selamat bereksplorasi di Laboratorium Komputasi. Pemrograman bukan sekadar menulis bahasa asing, ia adalah memecah masalah secara logis. Happy Coding!*
