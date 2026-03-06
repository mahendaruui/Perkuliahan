# Rencana Pembelajaran Semester (RPS) Berbasis OBE
**Mata Kuliah: Struktur Data (Golang)**

Berikut ini adalah Rencana Pembelajaran Semester untuk materi Struktur Data, di mana seluruh implementasi menggunakan bahasa kompilasi Golang demi penekanan manajemen memori (pointer), efisiensi eksekusi (Big-O Notation), dan pola struktural modern.

---

### **Capaian Pembelajaran Lulusan (CPL)**
- **Sikap:** Menunjukkan sikap bertanggung jawab dan logis dalam pemrograman.  
- **Pengetahuan:** Menguasai tata cara kerja memori komputer, linear, dan non-linear data.
- **Keterampilan:** Mampu merancang sistem dan efisien menggunakan resource sesuai karakteristik masalah dunia nyata.

### **Capaian Pembelajaran Mata Kuliah (CPMK)**
1. Mahasiswa dapat menjelaskan tipe data dan struktur data 80% akurat.
2. Mahasiswa dapat menjelaskan logika dan instruksi pemrograman Stack, Queue, Hashmap, dan Linked List.
3. Mahasiswa bisa membuat konstruksi OOP (Struct/Receiver) dalam Golang dan mengamankannya via memori `*Pointer`.
4. Mahasiswa mampu menganalisis kebutuhan Graph & Tree dan melakukan iterasi ke dalamnya.

---

## **Matriks Rencana Pembelajaran Mingguan**

| Minggu | Capaian Pembelajaran (CPMK) | Materi Pokok (Fokus Golang) | Metode Pembelajaran | Bobot (%) |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Mahasiswa menjelaskan karakteristik data linear dan non-linear dengan 80% akurat | **Pengantar Struktur Data**: <br>- Data linear vs non-linear<br>- Pengantar cara kerja memori | Mendengarkan, memahami, tanya jawab | - |
| **2** | Mahasiswa dapat menjelaskan tipe data dan struktur data 80% akurat | **Array, Pointer, dan Memory Layout**: <br>- Tipe data Golang, *Slice* vs *Array*<br>- *User data type* (`struct`)<br>- *Abstract data type* dan *Method* (Receiver di Golang) | Ceramah, Small Group Discussion, PBL | 10% |
| **3** | Mahasiswa dapat menjelaskan logika pemrograman pada struktur data stack secara akurat 80% | **Stack & Operasi Dasar**: <br>- Konsep LIFO (*Push, Pop, Peek*)<br>- Implementasi menggunakan *Slice* di Golang | Praktikum Terbimbing, Diskusi, Tanya Jawab | 5% |
| **4** | Mahasiswa mampu menjelaskan Algoritma Queue | **Queue FIFO & Implementasi**: <br>- *Linear, Circular, dan Double Ended Queue* (Deque)<br>- Implementasi Queue dengan *Slice* / *Struct* | Praktikum Terbimbing, Diskusi, Tanya Jawab | 5% |
| **5** | Mahasiswa mampu menerapkan Algoritma Linked List | **Singly Linked List**: <br>- Konsep, *Pointer* (`*T`), dan *representasi rantai*<br>- Membuat struct `Node` dan struct `LinkedList` | Praktikum Terbimbing, Diskusi, Tanya Jawab | 7% |
| **6** | Mahasiswa mampu menerapkan operasi insert/delete pada Linked List | **Linked List Lanjutan**: <br>- *Linear* dan *Circular Linked List*<br>- Manajemen pembersihan memori (otomatis lewat *Garbage Collector* Golang) | Praktikum Terbimbing, Diskusi, Tanya Jawab | 7% |
| **7** | Mahasiswa mampu menganalisis permasalahan dan memanfaatkan struktur data untuk penyelesaian masalah | **Studi Kasus Real Use Case**: <br>- Kasus Stack: Fitur Undo/Redo<br>- Kasus Queue: Sistem antrian *goroutine/channel* | Studi Kasus, Diskusi Kelompok | - |
| **8** | **Evaluasi Tengah Semester (UTS)** | **Materi Minggu 1-7**: Ujian Tertulis / Coding Dasar | Ujian Tertulis/Analisis | 10% |
| **9** | Mahasiswa dapat menjelaskan logika pemrograman pada struktur data binary tree secara akurat 80% | **Tree**: <br>- *Binary Search Tree* (BST) dan B-Tree<br>- Membuat struct `TreeNode` (*Left*, *Right*, *Value*) | Mendengarkan, memahami, tanya jawab | 5% |
| **10** | Mahasiswa dapat membuat konstruksi struktur data untuk kasus yang diberikan dengan benar 100% | **Tree Lanjutan**: <br>- Studi Kasus BST (Traversal: InOrder, PreOrder, PostOrder menggunakan fungsi rekursif Go) | Praktikum, Small Group Discussion, Teamwork | 5% |
| **11** | Mahasiswa mampu menerapkan Algoritma Searching | **Searching**: <br>- *Binary Search* dan *Interpolation Search*<br>- Menyiapkan data numerik/struct dan mencarinya | Praktikum Terbimbing, Diskusi | 13% |
| **12** | Mahasiswa dapat menjelaskan logika pemrograman struktur data graph secara akurat 80% | **Graph**: <br>- Konsep dasar dan representasi (Vertex & Edge)<br>- *Adjacency List* menggunakan `map[int][]int` Golang | Praktikum, Mendengarkan, Tanya Jawab | 5% |
| **13** | Mahasiswa memahami masalah yang bisa diselesaikan dengan algoritma pencarian/Greedy | **Graph Lanjutan**: <br>- Algoritma Dijkstra dan Jalur Terpendek<br>- Menelusuri graph (*BFS* / *DFS*) | Simulasi Visual, Coding | 10% |
| **14** | Mahasiswa mampu mempresentasikan ide dan solusi yang dibuat | **Presentasi Tugas Besar (Progress)**: Proposal & Progres Implementasi Golang API / CLI | Presentasi, Tanya Jawab | 5% |
| **15** | Mahasiswa mampu mengimplementasikan kebutuhan computing dengan sistematis | **Proyek Mini Final**: <br>- Pengembangan sistem terpadu (Struktur data murni Golang) | Project Based Learning (PBL) | 20% |
| **16** | **Evaluasi Akhir Semester (UAS)** | **Materi Minggu 9-15**: <br>- Presentasi dan *Code Review* Final Project | Evaluasi/Project Akhir | 10% |
