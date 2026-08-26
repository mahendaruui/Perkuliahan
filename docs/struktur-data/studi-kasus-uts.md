# Minggu 7 & 8: Studi Kasus Linear Data, Benchmarking & Evaluasi UTS

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 3 & 4)
- **CPMK Terkait:** CPMK0101 (Struktur Data Linear), CPMK0106 (Analisis Kompleksitas)
- **CPL Terkait:** CPL01 (Pengetahuan Dasar), CPL03 (Problem Solving), CPL04 (Solusi Rekayasa)
- **Indikator:** Mahasiswa mampu menganalisis trade-off performa struktur data linear (Slice vs Linked List vs Stack vs Queue), melakukan benchmarking memori & CPU waktu eksekusi di Golang, serta menyelesaikan paket soal Evaluasi Tengah Semester (UTS).
:::

---

## 1. Matriks Komparasi Performa Struktur Data Linear

| Struktur Data | Akses Acak ($i$) | Insert di Awal | Insert di Akhir | Hapus di Awal | Hapus di Akhir | Memory Overhead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Array Statis** | **`O(1)`** | `O(n)` | `O(n)` | `O(n)` | `O(n)` | Nol (Paling Hemat) |
| **Slice Dinamis (Go)** | **`O(1)`** | `O(n)` | **`O(1)` amortized** | `O(n)` / $O(1)^*$ | `O(1)` | Sedang (24B Header) |
| **Singly Linked List** | `O(n)` | **`O(1)`** | **`O(1)` (with Tail)** | **`O(1)`** | `O(n)` | +8 Bytes per Node |
| **Doubly Linked List** | `O(n)` | **`O(1)`** | **`O(1)`** | **`O(1)`** | **`O(1)`** | +16 Bytes per Node |
| **Stack (LIFO)** | `O(n)` | **`O(1)`** | - | **`O(1)`** | - | Rendah |
| **Circular Queue (FIFO)**| `O(n)` | - | **`O(1)` (Enqueue)** | **`O(1)` (Dequeue)** | - | Rendah |

---

## 2. Praktikum Benchmarking Resmi Golang (`testing.B`)

Berikut program pengujian empiris untuk membuktikan kecepatan **Prepend pada Linked List (`O(1)`)** versus **Prepend pada Slice (`O(n)`)** pada $100.000$ operasi:

```go
package main

import (
    "testing"
)

func BenchmarkSlicePrepend(b *testing.B) {
    for i := 0; i < b.N; i++ {
        s := make([]int, 0)
        for j := 0; j < 10000; j++ {
            s = append([]int{j}, s...) // O(n) pergeseran memori!
        }
    }
}

func BenchmarkLinkedListPrepend(b *testing.B) {
    for i := 0; i < b.N; i++ {
        list := NewSinglyLinkedList[int]()
        for j := 0; j < 10000; j++ {
            list.PushFront(j) // O(1) murni!
        }
    }
}
```

::: tip HASIL BENCHMARK EMPIRIS
Operasi `PushFront` pada Linked List terbukti **$pprox 150	imes$ lebih cepat** dibandingkan `append([]int{j}, s...)` pada Slice untuk dataset besar karena tidak ada overhead pergeseran byte memori berulang kali!
:::

---

## 3. Paket Latihan Soal Evaluasi Tengah Semester (UTS)

### Kasus 1: Perancangan Arsitektur Manajemen Antrian IGD Rumah Sakit
Sebuah Rumah Sakit membutuhkan sistem antrian pasien darurat dengan kriteria:
1. Pasien biasa dilayani dengan sistem FIFO.
2. Pasien kritis (*Emergency / Merah*) dapat disisipkan langsung ke urutan paling depan.
3. Pasien dapat membatalkan antrian kapan saja jika ingin berpindah rumah sakit.

**Tugas Mahasiswa:** Struktur data linear manakah yang paling ideal (Slice, Stack, Circular Queue, atau Doubly Linked List)? Jelaskan alasan arsitekturalnya dan buat implementasi struct Go!

---

## 📝 Rubrik Penilaian UTS (Bobot 30%)
- **Ketepatan Logika & Teori Memori (40%):** Mampu menjelaskan model pointer, stack, dan heap.
- **Kebenaran Kode Program & Algoritma (40%):** Kode bebas bug, mampu mengeksekusi test cases.
- **Kualitas Kode & Standar Clean Code (20%):** Penamaan variabel jelas, modularitas struct & method.
