# RENCANA PEMBELAJARAN SEMESTER (RPS)
## MATA KULIAH: STRUKTUR DATA (IFR205) - OBE CURRICULUM

---

## 🏛️ IDENTITAS MATA KULIAH

| **Komponen** | **Keterangan / Rincian** |
| :--- | :--- |
| **Perguruan Tinggi** | Universitas Ubudiyah Indonesia (UUI) |
| **Fakultas** | Fakultas Sains dan Teknologi |
| **Program Studi** | S-1 Informatika |
| **Nama Mata Kuliah** | **Struktur Data** *(Data Structures & Algorithms)* |
| **Kode Mata Kuliah** | **IFR205** |
| **Bahan Kajian (BK)** | **BK12** (Data Structures, Algorithms and Complexity) |
| **Bobot SKS** | **3 SKS** (2 SKS Teori, 1 SKS Praktikum Laboratorium) |
| **Semester** | 2 (Genap) |
| **Mata Kuliah Prasyarat** | Algoritma dan Pemrograman (**IFR206**) |
| **Bahasa Pengantar Praktikum** | **Golang (Go)** & Pseudocode Standar |
| **Dosen Pengembang RPS** | Tim Dosen Rumpun Ilmu Komputasi & Rekayasa Perangkat Lunak UUI |
| **Koordinator Rumpun MK** | Mahendar Dwi Payana, S.ST., M.T. |
| **Ketua Program Studi** | M. Bayu Wibawa, S.Kom., MMSI |

---

## 📖 DESKRIPSI MATA KULIAH

Mata kuliah **Struktur Data (IFR205)** merupakan mata kuliah inti kompetensi keilmuan informatika yang mempelajari cara pengorganisasian, penyimpanan, dan manipulasi data di dalam memori komputer (*RAM*) secara efisien. Mata kuliah ini menggunakan pendekatan **Outcome-Based Education (OBE)** dengan penekanan kuat pada analisis kompleksitas algoritma (*Big-O Time & Space Complexity*) dan implementasi terapan menggunakan bahasa pemrograman **Golang (Go)**.

Golang dipilih sebagai bahasa pengantar praktikum modern karena memiliki sistem pengetikan ketat (*statically typed*), manajemen pointer memori eksplisit (`*` dan `&`), representasi memori *slice* dan *array*, *struct composition*, *garbage collection* berkecepatan tinggi, dan arsitektur konkurensi bawaan (*goroutine & channel*) yang sangat relevan untuk industri *software engineering* dan komputasi awan (*cloud native*).

Materi perkuliahan mencakup: Alokasi Memori Stack & Heap, Pointer Semantics & Struct, Struktur Data Linear (*Static Array, Dynamic Slice, Singly/Doubly Linked List, Stack LIFO, Queue FIFO, Circular Deque*), Struktur Data Non-Linear (*Binary Tree, Binary Search Tree (BST), AVL/B-Tree concept*), Graph (*Adjacency Matrix, Adjacency List, BFS, DFS, Shortest Path Dijkstra*), Algoritma Pencarian & Hash Table, serta Pembangunan Proyek Terpadu (*Capstone Project Based Learning*).

---

## 🎯 CAPAIAN PEMBELAJARAN

### A. Capaian Pembelajaran Lulusan (CPL) Prodi yang Dibebankan

| **Kode CPL** | **Deskripsi Capaian Pembelajaran Lulusan (CPL)** |
| :--- | :--- |
| **CPL01** | **Pengetahuan Dasar:** Memiliki pengetahuan komprehensif tentang teori, prinsip, dan konsep dasar informatika (struktur data, kompleksitas memori, dan komputasi). |
| **CPL08** | **Sikap & Nilai:** Memiliki komitmen terhadap prinsip dan nilai islami, etika akademik, integritas kode program, dan tanggung jawab profesional. |
| **CPL03** | **Keterampilan Kerja Umum:** Mampu beradaptasi terhadap penggunaan metode baru pada konteks permasalahan yang dinamis. |
| **CPL04** | **Keterampilan Khusus:** Mampu merancang dan menyajikan solusi rekayasa perangkat lunak berbasis struktur data yang optimal untuk dunia industri dan masyarakat. |

---

### B. Capaian Pembelajaran Mata Kuliah (CPMK)

| **Kode CPMK** | **Deskripsi Capaian Pembelajaran Mata Kuliah** | Terkait CPL |
| :--- | :--- | :--- |
| **CPMK0101** | **Mampu menjelaskan dan mengimplementasikan konsep struktur data linear dan non-linear** (Array, Slice, Struct, Pointer, Linked List, Stack, Queue, Tree, dan Graph) menggunakan kaidah pemrograman terstruktur dan efisien. | CPL01, CPL04 |
| **CPMK0106** | **Mampu menganalisis efisiensi memori (Space Complexity) dan waktu eksekusi (Time Complexity Big-O)** pada berbagai operasi struktur data serta memilih representasi struktur data yang tepat untuk menyelesaikan persoalan komputasi riil. | CPL01, CPL03, CPL08 |

---

### C. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK)

| **Sub-CPMK** | **Deskripsi Kemampuan Akhir Mahasiswa** | Terkait CPMK |
| :--- | :--- | :--- |
| **Sub-CPMK 1** | Mampu menguraikan klasifikasi struktur data linear vs non-linear, cara kerja alokasi memori komputer (*Stack vs Heap*), serta abstraksi data (*ADT*). | CPMK0101 |
| **Sub-CPMK 2** | Mampu mengimplementasikan tipe data bentukan (`struct`), *receiver methods*, serta manipulasi alamat memori dan pointer (`*` dan `&`) di Golang. | CPMK0101 |
| **Sub-CPMK 3** | Mampu merancang dan merekayasa struktur data Stack (*LIFO*) dan Queue (*FIFO / Circular Queue*) beserta analisis penerapannya pada *Undo/Redo* dan *Job Scheduling*. | CPMK0101, CPMK0106 |
| **Sub-CPMK 4** | Mampu membangun struktur data Singly, Doubly, dan Circular Linked List dinamis menggunakan representasi *Node & Pointer chaining* di Golang. | CPMK0101, CPMK0106 |
| **Sub-CPMK 5** | Mampu mengimplementasikan struktur data hierarkis Pohon Biner (*Binary Tree* & *Binary Search Tree / BST*), operasi penelusuran (*PreOrder, InOrder, PostOrder*), serta penyeimbangan dasar. | CPMK0101, CPMK0106 |
| **Sub-CPMK 6** | Mampu merancang struktur data Graph (*Adjacency List & Matrix*), algoritma penelusuran graf (*BFS & DFS*), dan penentuan rute terpendek (*Shortest Path Dijkstra*). | CPMK0101, CPMK0106 |
| **Sub-CPMK 7** | Mampu merancang, membangun, dan mempresentasikan Purwarupa Sistem Aplikasi Berbasis In-Memory Data Structures (PjBL) secara mandiri dan beretika akademik. | CPMK0101, CPMK0106, CPL08 |

---

## 📊 MATRIKS KORELASI CPL - CPMK - SUB-CPMK

| CPMK / Sub-CPMK | CPL01 | CPL03 | CPL04 | CPL08 |
| :--- | :---: | :---: | :---: | :---: |
| **CPMK0101** | ✅ | ➖ | ✅ | ➖ |
| **CPMK0106** | ✅ | ✅ | ➖ | ✅ |
| **Sub-CPMK 1 (Minggu 1)** | ✅ | ➖ | ✅ | ➖ |
| **Sub-CPMK 2 (Minggu 2)** | ✅ | ➖ | ✅ | ➖ |
| **Sub-CPMK 3 (Minggu 3-4)** | ✅ | ✅ | ✅ | ➖ |
| **Sub-CPMK 4 (Minggu 5-6)** | ✅ | ✅ | ✅ | ➖ |
| **Sub-CPMK 5 (Minggu 9-10)** | ✅ | ✅ | ✅ | ➖ |
| **Sub-CPMK 6 (Minggu 12-13)** | ✅ | ✅ | ✅ | ➖ |
| **Sub-CPMK 7 (Minggu 14-16)** | ✅ | ✅ | ✅ | ✅ |

---

## 🗓️ RANCANGAN PEMBELAJARAN MINGGUAN (16 MINGGU)

| **Mg** | **Sub-CPMK** | **Bahan Kajian (Materi Pokok)** | **Bentuk & Metode Pembelajaran** | **Estimasi Waktu** | **Pengalaman Belajar Mahasiswa** | **Kriteria & Bentuk Penilaian** | **Bobot (%)** |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **1** | Sub-CPMK 1 | **Kontrak Kuliah & Pengantar Struktur Data**: Klasifikasi linear vs non-linear, abstraksi data (ADT), cara kerja alokasi memori RAM (Stack vs Heap), dan paradigma Golang. | Kuliah Interaktif, Diskusi, Analisis Komparasi | TM: 2x50' <br>BT: 2x60' <br>BM: 2x60' <br>P: 1x170' | Menganalisis perbedaan performa struktur statis vs dinamis serta memetakan struktur data ke memori. | Partisipasi aktif & kuis pengantar struktur data | 3% |
| **2** | Sub-CPMK 2 | **Memori, Pointer, Struct & Slice di Golang**: Representasi byte, operator dereference (`*`) dan address-of (`&`), pass by value vs reference, struct receiver methods, slice internal (pointer, len, cap). | Live Coding, Praktikum Lab Terbimbing | TM: 2x50' <br>P: 1x170' | Menulis kode struct dan method receiver di Go serta membuktikan manipulasi memori pointer langsung. | Kelancaran implementasi pointer struct & slice (Tugas 1) | 5% |
| **3** | Sub-CPMK 3 | **Struktur Data Linear: Stack (LIFO)**: Konsep *Last-In First-Out*, operasi `Push`, `Pop`, `Peek`, `IsEmpty`, implementasi Stack berbasis Slice & Pointer di Golang, studi kasus *Balanced Parentheses* dan evaluasi postfix. | Problem-Based Learning, Praktikum Lab | TM: 2x50' <br>P: 1x170' | Membangun ADT Stack di Go dan menyelesaikan algoritma pengecekan validitas tag HTML / kurung kurawal. | Kebenaran algoritma Stack & clean error handling (Tugas 2) | 5% |
| **4** | Sub-CPMK 3 | **Struktur Data Linear: Queue (FIFO)**: Konsep *First-In First-Out*, operasi `Enqueue`, `Dequeue`, `Front`, `Rear`, kelemahan linear queue, implementasi *Circular Queue* dan *Double-Ended Queue (Deque)*. | Praktikum Lab, Studi Kasus Antrian | TM: 2x50' <br>P: 1x170' | Merekayasa simulasi antrian layanan nasabah bank / print spooler berbasis Circular Queue. | Ketepatan perputaran indeks Circular Queue (Tugas 3) | 5% |
| **5** | Sub-CPMK 4 | **Singly Linked List**: Konsep rantai memori dinamis (*Node* & *Pointer Next*), keunggulan atas array, operasi `InsertHead`, `InsertTail`, `DeleteHead`, `DeleteValue`, dan `Traversal`. | Demonstrasi Visual, Live Coding Lab | TM: 2x50' <br>P: 1x170' | Merangkai struct Node berantai di Golang dan menganalisis efisiensi traversal `O(n)` vs insert `O(1)`. | Ketepatan manipulasi pointer rantai Node (Tugas 4) | 6% |
| **6** | Sub-CPMK 4 | **Linked List Lanjutan**: Doubly Linked List (*Pointer Prev & Next*), Circular Linked List, operasi *Reverse Linked List*, serta manajemen *Garbage Collection* di Go. | Praktikum Intensif, Problem Solving | TM: 2x50' <br>P: 1x170' | Membangun Doubly Linked List untuk riwayat pemutar musik (*Music Playlist Prev/Next*). | Kemampuan navigasi dua arah pointer (Tugas 5) | 6% |
| **7** | Sub-CPMK 3, 4 | **Studi Kasus Integrasi & Review Linear Data**: Analisis komparasi performa Array vs Slice vs Linked List vs Stack vs Queue untuk berbagai skenario industri. | Case-Based Learning, Diskusi Kelompok | TM: 2x50' <br>P: 1x170' | Melakukan benchmarking kecepatan waktu eksekusi operasi data linear pada dataset 100.000 elemen. | Laporan analisis komparasi benchmark | 5% |
| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | **Ujian Tengah Semester (Teori Pemahaman Memori & Live Coding Linear Data)** | Ujian Tertulis & Live Coding Mandiri | 120 Menit | Menyelesaikan problem set alokasi memori, pointer struct, stack, queue, dan linked list secara mandiri. | Rubrik Ujian Tengah Semester Bebas Plagiarisme | **30%** |
| **9** | Sub-CPMK 5 | **Struktur Data Non-Linear: Tree & Binary Tree**: Konsep hierarki (*Root, Parent, Child, Leaf, Height, Depth*), representasi struct `TreeNode` (Left, Right, Data), Full vs Complete vs Perfect Binary Tree. | Kuliah Interaktif, Simulasi Grafis | TM: 2x50' <br>P: 1x170' | Menggambar struktur pohon dan menyusun kode representasi Node Tree di Golang. | Kejelasan representasi struktur pohon | 4% |
| **10** | Sub-CPMK 5 | **Binary Search Tree (BST) & Algoritma Traversal**: Properti BST ($L < Root < R$), operasi `Insert`, `Search`, `Delete Node` (3 kasus penghapusan), penelusuran rekursif *PreOrder*, *InOrder*, dan *PostOrder*. | Praktikum Lab, Simulasi Rekursif | TM: 2x50' <br>P: 1x170' | Membangun BST di Go, melakukan traversal untuk mengurutkan data (*Tree Sort*), dan menghapus node. | Kebenaran logika rekursi BST (Tugas 6) | 6% |
| **11** | Sub-CPMK 5, 6 | **Pencarian Lanjut & Tabel Hash (Hash Table)**: Interpolation Search, Konsep Hashing (*Hash Function, Key-Value mapping, Collision Resolution: Chaining vs Open Addressing*), Built-in Go `map`. | Lab Coding, Eksperimen Algoritma | TM: 2x50' <br>P: 1x170' | Merancang Hash Table sederhana dengan penanganan tabrakan hash (*collision chaining*). | Efisiensi akses data `O(1)` pada hash table (Tugas 7) | 5% |
| **12** | Sub-CPMK 6 | **Struktur Data Graph**: Definisi Graf (*Vertex, Edge, Directed vs Undirected, Weighted*), representasi graf: *Adjacency Matrix* vs *Adjacency List* menggunakan `map[string][]Edge` di Go. | Diskusi Konseptual, Praktikum Lab | TM: 2x50' <br>P: 1x170' | Memodelkan jaringan rute penerbangan atau pertemanan media sosial menggunakan Adjacency List. | Ketepatan representasi Graf di Go (Tugas 8) | 5% |
| **13** | Sub-CPMK 6 | **Algoritma Penelusuran Graf & Shortest Path**: Breadth-First Search (*BFS* menggunakan Queue), Depth-First Search (*DFS* menggunakan Stack/Rekursi), Algoritma Dijkstra (Rute Terpendek). | Simulasi Algoritma, Live Coding | TM: 2x50' <br>P: 1x170' | Menerapkan algoritma Dijkstra untuk mencari rute jalan tercepat antar kota di Aceh/Indonesia. | Kebenaran perhitungan bobot minimum (Tugas 9) | 5% |
| **14** | Sub-CPMK 7 | **Asistensi & Desain Arsitektur Capstone Project (PjBL)**: Perancangan purwarupa sistem aplikasi berbasis struktur data in-memory terpadu (CLI / REST API Go). | Workshop Proyek, Asistensi Teknis | TM: 2x50' <br>P: 1x170' | Merancang arsitektur data struktur in-memory dan pembagian modul sistem tim. | Progres rancangan arsitektur & kelengkapan ADT | 5% |
| **15** | Sub-CPMK 7 | **Finalisasi & Uji Coba Capstone Project**: Uji ketahanan memori (*memory leak check*), validasi edge-cases, dan dokumentasi teknis sistem. | Laboratorium Mandiri & Code Review | TM: 2x50' <br>P: 1x170' | Melakukan refactoring kode berstandar *Clean Code* dan pengujian skenario ekstrem. | Kerapian kode & keandalan eksekusi | 5% |
| **16** | **EVALUASI AKHIR SEMESTER (UAS)** | **Ujian Akhir Semester & Presentasi Demo Capstone Project** | Ujian Tertulis, Demo Live System & Tanya Jawab | 150 Menit | Mempresentasikan sistem in-memory Golang, mendemonstrasikan algoritma kompleksitas, dan menjawab uji kode. | Rubrik Capstone Project PjBL & Tes Komprehensif | **30%** |

---

## 📈 SISTEM EVALUASI & PENILAIAN OBE

| **Komponen Evaluasi** | **Metode Asesmen** | **Bobot (%)** | **Pemetaan CPMK** |
| :--- | :--- | :---: | :--- |
| **Tugas Coding Praktikum Lab** | Tugas Modul 1 s.d. 9 (Implementasi Go & Analisis) | **20%** | CPMK0101, CPMK0106 |
| **Kuis & Studi Kasus Mingguan** | Kuis Logika Memori, Pointer Trace Table | **10%** | CPMK0101, CPMK0106 |
| **Tugas Besar / Capstone Project (PjBL)** | Sistem Aplikasi In-Memory Murni Go & Dokumentasi | **10%** | CPMK0101, CPMK0106, CPL08 |
| **Ujian Tengah Semester (UTS)** | Ujian Teori & Praktikum Live Coding (Sesi 1-7) | **30%** | CPMK0101, CPMK0106 |
| **Ujian Akhir Semester (UAS)** | Ujian Komprehensif Teori & Demo Capstone (Sesi 9-15) | **30%** | CPMK0101, CPMK0106, CPL08 |
| **TOTAL** | | **100%** | |

### Konversi Nilai Huruf Standar Akademik UUI

| **Nilai Angka** | **Nilai Huruf** | **Bobot Mutu** | **Kualifikasi Kompetensi** |
| :---: | :---: | :---: | :--- |
| **85.00 – 100.00** | **A** | **4.00** | Istimewa / Sangat Kompeten |
| **80.00 – 84.99** | **A-** | **3.75** | Sangat Baik |
| **75.00 – 79.99** | **B+** | **3.50** | Baik Sekali |
| **70.00 – 74.99** | **B** | **3.00** | Baik / Kompeten |
| **65.00 – 69.99** | **B-** | **2.75** | Cukup Baik |
| **60.00 – 64.99** | **C+** | **2.50** | Cukup |
| **55.00 – 59.99** | **C** | **2.00** | Lulus Standar Minimum |
| **45.00 – 54.99** | **D** | **1.00** | Kurang (Wajib Mengulang) |
| **0.00 – 44.99** | **E** | **0.00** | Gagal / Tidak Lulus |

---

## 📚 DAFTAR PUSTAKA ACUAN UTAMA

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2022). *Introduction to Algorithms* (4th ed.). Cambridge, MA: MIT Press.
2. **Donovan, A. A., & Kernighan, B. W.** (2015). *The Go Programming Language*. New York: Addison-Wesley.
3. **Drozdek, A.** (2012). *Data Structures and Algorithms in C++* (4th ed.). Boston: Cengage Learning.
4. **Goodrich, M. T., Tamassia, R., & Goldwasser, M. H.** (2014). *Data Structures and Algorithms in Java* (6th ed.). Hoboken: John Wiley & Sons.
5. **Sedgewick, R., & Wayne, K.** (2014). *Algorithms* (4th ed.). Upper Saddle River: Addison-Wesley.
6. **Tsoukalos, M.** (2021). *Mastering Go: Harness the power of Go to build high-performance systems* (3rd ed.). Birmingham: Packt Publishing.
