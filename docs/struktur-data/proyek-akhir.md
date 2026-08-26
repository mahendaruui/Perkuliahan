# Minggu 14 - 16: Project-Based Learning (PjBL) & Evaluasi UAS

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 7)
- **CPMK Terkait:** CPMK0101 (Implementasi Struktur Data), CPMK0106 (Analisis Kompleksitas)
- **CPL Terkait:** CPL01 (Pengetahuan), CPL08 (Etika Akademik & Kejujuran Kode), CPL03 (Problem Solving), CPL04 (Solusi Rekayasa)
- **Indikator:** Mahasiswa secara berkelompok/mandiri mampu merancang, membangun, dan mempresentasikan Purwarupa Sistem In-Memory Berbasis Struktur Data Murni Golang tanpa menggunakan basis data SQL eksternal.
:::

---

## 🏛️ Ketentuan Mutlak Capstone Mini Project

1. **Bahasa Pemrograman:** Murni berbasis **Golang (Go)** standar.
2. **Kewajiban In-Memory Data Structures:** **DILARANG MENGGUNAKAN SQL / NoSQL External DB**. Seluruh penyimpanan data wajib direkayasa di RAM menggunakan kombinasi ADT:
   - *Linear:* Dynamic Slice, Singly/Doubly Linked List, Stack, Circular Queue.
   - *Non-Linear:* Binary Search Tree (BST), Trie, atau Weighted Graph.
   - *Lookup:* Hash Map / Custom Hash Table.
3. **Format Aplikasi:** Berbasis Terminal CLI Interaktif atau REST API Endpoint (`net/http`).

---

## 🎯 Pilihan Tema & Studi Kasus Rekayasa Industri

### Opsi 1: High-Performance In-Memory Key-Value Cache (Redis Clone)
- **Struktur Data:** Hash Table + Doubly Linked List (LRU Eviction) + Min-Heap (TTL Expiry).
- **Fitur:** `SET key val`, `GET key`, `DEL key`, `EXPIRE key ttl`, dan statistik hit/miss ratio.

### Opsi 2: Flight & Logistics Route Optimizer (Sistem Navigasi Logistik)
- **Struktur Data:** Weighted Directed Graph + Min-Heap Dijkstra + Priority Queue.
- **Fitur:** Pendaftaran bandara/kota, penentuan rute kargo tercepat & termurah, serta simulasi kendala cuaca.

### Opsi 3: Git Version Control Core Engine Mini
- **Struktur Data:** Directed Acyclic Graph (DAG) + Tree + Hash SHA-256 Map.
- **Fitur:** `init`, `commit`, `log` (Graph Traversal), `branch`, dan `checkout`.

---

## 📈 Rubrik Penilaian Akhir (UAS - Bobot 30%)

| Kriteria Penilaian | Bobot (%) | Indikator Ketercapaian |
| :--- | :---: | :--- |
| **Arsitektur & Pemilihan Struktur Data** | **30%** | Ketepatan pemilihan ADT sesuai karakteristik masalah dan efisiensi Big-O. |
| **Kualitas Kode & Standar Clean Code** | **25%** | Penerapan Go Generics, pointer safety, pencegahan memory leak, modularitas struct. |
| **Keandalan & Penanganan Error** | **20%** | Program tangguh terhadap input tidak valid dan tidak mengalami panic/crash. |
| **Demo Sistem & Penguasaan Teori (Live Coding)** | **25%** | Kemampuan menjelaskan trace memori dan menjawab pertanyaan dosen secara mandiri. |
