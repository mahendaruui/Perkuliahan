# Struktur Data (IFR205) — Implementasi Golang

Selamat datang di repositori materi perkuliahan **Struktur Data** (Kode MK: **IFR205**, Bobot: **3 SKS**) Program Studi S-1 Informatika, Fakultas Sains dan Teknologi, Universitas Ubudiyah Indonesia (UUI).

Materi ini diselenggarakan berbasis kurikulum **Outcome-Based Education (OBE)** dengan penekanan pada efisiensi alokasi memori (*Stack & Heap*), notasi *Big-O Complexity*, dan implementasi berbasis bahasa pemrograman performa tinggi **Golang (Go)**.

---

## 🎓 Informasi Mata Kuliah

::: info METADATA KURIKULUM OBE
- **Kode Mata Kuliah:** IFR205
- **Bahan Kajian (BK):** BK12 (Data Structures, Algorithms and Complexity)
- **Bobot SKS:** 3 SKS (2 SKS Teori, 1 SKS Praktikum Laboratorium)
- **Semester:** 2 (Genap)
- **Mata Kuliah Prasyarat:** Algoritma dan Pemrograman (IFR206)
- **Bahasa Implementasi Praktikum:** Golang (Go) & Pseudocode
- **CPL yang Dibebankan:** 
  - **CPL01:** Pengetahuan komprehensif teori & konsep dasar informatika.
  - **CPL08:** Komitmen terhadap etika akademik, integritas kode, dan nilai profesional.
  - **CPL03:** Kemampuan adaptasi dan pemecahan masalah (*problem solving*) dinamis.
  - **CPL04:** Rekayasa solusi komputasi yang optimal untuk industri dan masyarakat.
- **CPMK Utama:**
  - **CPMK0101:** Mampu merekayasa struktur data linear dan non-linear di Golang.
  - **CPMK0106:** Mampu menganalisis kompleksitas memori (*Space*) dan waktu (*Time Big-O*).
:::

---

## 📋 Struktur Materi Perkuliahan Mingguan

### 🔹 Bagian 1: Fondasi Memori, Pointer & Struct
* **[Rencana Pembelajaran Semester (RPS)](./RPS.md)** — Silabus Resmi OBE 16 Minggu, Matriks CPL/CPMK & Rubrik Evaluasi
* **[Minggu 1: Pengantar Struktur Data, Linear vs Non-Linear](./pengantar.md)** — Abstraksi ADT, Alokasi Memori Stack vs Heap, Paradigma Data Structures *(Sub-CPMK 1)*
* **[Minggu 2: Array, Slice, Struct & Pointer di Golang](./pointer-struct.md)** — Dereference `*`, Address-of `&`, Receiver Method, Slice Internals *(Sub-CPMK 2)*

### 🔹 Bagian 2: Struktur Data Linear (Stack, Queue, Linked List)
* **[Minggu 3: Stack LIFO (Tumpukan Data)](./stack.md)** — Push, Pop, Peek, IsEmpty, Evaluasi Ekspresi & Balanced Parentheses *(Sub-CPMK 3)*
* **[Minggu 4: Queue FIFO (Antrean Data)](./queue.md)** — Linear Queue, Circular Queue, Deque, Simulasi Antrian Bank *(Sub-CPMK 3)*
* **[Minggu 5: Singly Linked List (Senarai Berantai)](./linked-list.md)** — Representasi Node & Pointer Next, Operasi Insert & Delete Dinamis *(Sub-CPMK 4)*
* **[Minggu 6: Linked List Lanjutan & Circular List](./linked-list-lanjutan.md)** — Doubly Linked List (Prev/Next), Circular List & Garbage Collection *(Sub-CPMK 4)*
* **[Minggu 7 & 8: Studi Kasus Linear Data & Evaluasi UTS](./studi-kasus-uts.md)** — Komparasi Kinerja Memori, Benchmarking & Ujian Tengah Semester *(Sub-CPMK 3, 4)*

### 🔹 Bagian 3: Struktur Data Hierarkis & Non-Linear (Tree & BST)
* **[Minggu 9: Struktur Data Pohon (Binary Tree)](./binary-tree.md)** — Konsep Root, Parent, Child, Height, Depth, Struct TreeNode di Go *(Sub-CPMK 5)*
* **[Minggu 10: Binary Search Tree (BST) & Traversal](./binary-search-tree.md)** — Properti BST, PreOrder, InOrder, PostOrder & Operasi Hapus Node *(Sub-CPMK 5)*
* **[Minggu 11: Algoritma Pencarian & Hash Table](./searching.md)** — Linear Search, Binary Search, Interpolation Search & Hash Collision *(Sub-CPMK 5, 6)*

### 🔹 Bagian 4: Jaringan Graf, Rute Terpendek & Capstone Project
* **[Minggu 12: Struktur Data Graf (Graph Network)](./graph.md)** — Vertex, Edge, Adjacency Matrix vs Adjacency List di Golang *(Sub-CPMK 6)*
* **[Minggu 13: Algoritma Dijkstra & Rute Terpendek](./dijkstra-graph.md)** — BFS, DFS, Jalur Terpendek Dijkstra & Analisis Bobot Graf *(Sub-CPMK 6)*
* **[Minggu 14 - 16: Proyek Akhir Berbasis Proyek (PjBL) & UAS](./proyek-akhir.md)** — Purwarupa Sistem In-Memory Golang, Demo Live Coding & Evaluasi UAS *(Sub-CPMK 7)*
* **[Bank Soal & Quiz UAS Struktur Data](./quiz_struktur_data.md)** — Bank Soal Pilihan Ganda & Analisis Trace Table Go *(Sub-CPMK 1-7)*

---

## 🚀 Mengapa Golang untuk Struktur Data?

Golang menghadirkan keseimbangan terbaik antara **kontrol memori tingkat rendah** (seperti C/C++) dan **keamanan sintaksis modern** (seperti Java/Python):
1. **Explicit Pointer Semantics:** Mahasiswa memahami secara nyata bagaimana alamat memori dialokasikan dan dimanipulasi tanpa kerumitan *pointer arithmetic* manual.
2. **Zero Value & Type Safety:** Mengurangi bug *null pointer* yang tidak terduga.
3. **High Performance & Concurrency:** Struktur data yang dirancang siap diintegrasikan dengan *goroutine & channel* untuk sistem komputasi modern.
