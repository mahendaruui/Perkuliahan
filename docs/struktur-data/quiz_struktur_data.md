# Quiz UAS Struktur Data (Golang)

> **Petunjuk**: Pilih satu jawaban yang paling tepat untuk setiap soal pilihan ganda. 

---

## Soal Pilihan Ganda (1–20)

**1.** Di bahasa pemrograman Golang, perbedaan mendasar antara **Array** dan **Slice** adalah…

- A. Array memiliki ukuran dinamis, sedangkan Slice memiliki ukuran statis.
- B. Array dialokasikan di heap, sedangkan Slice selalu dialokasikan di stack.
- C. Array memiliki ukuran tetap (statis) yang ditentukan saat deklarasi, sedangkan Slice bersifat dinamis dan ukurannya dapat berubah. ✅
- D. Array dideklarasikan menggunakan tanda kurung siku `[]` tanpa ukuran, sedangkan Slice harus menyertakan panjangnya.

---

**2.** Perhatikan potongan kode Golang berikut:

```go
var x int = 10
var p *int = &x
*p = 20
fmt.Println(x)
```

Output dari kode di atas adalah…

- A. 10
- B. 20 ✅
- C. Alamat memori dari `x`
- D. Error kompilasi karena pointer tidak bisa diubah langsung

---

**3.** Saat kita melewatkan sebuah `struct` yang berukuran besar ke sebuah fungsi di Golang, pendekatan terbaik untuk menghindari penyalinan seluruh data (overhead memori) adalah…

- A. Melewatkan struct tersebut sebagai *Value* (pass-by-value).
- B. Mengubah struct tersebut menjadi Array terlebih dahulu.
- C. Melewatkan struct tersebut menggunakan *Pointer* (`*structName`). ✅
- D. Menggunakan keyword `defer` saat pemanggilan fungsi.

---

**4.** Representasi sebuah Node dalam implementasi **Singly Linked List** di Golang yang benar adalah…

- A. 
  ```go
  type Node struct {
      Value int
      Next  Node
  }
  ```
- B. 
  ```go
  type Node struct {
      Value int
      Next  *Node
  }
  ``` ✅
- C. 
  ```go
  type Node struct {
      Value int
      Prev  *Node
  }
  ```
- D. 
  ```go
  type Node struct {
      Value *int
      Next  int
  }
  ```

---

**5.** Kompleksitas waktu terburuk (worst-case time complexity) untuk mencari suatu elemen pada **Singly Linked List** dengan $N$ elemen adalah…

- A. $O(1)$
- B. $O(\log N)$
- C. $O(N)$ ✅
- D. $O(N \log N)$

---

**6.** Kelebihan utama **Double Linked List** dibandingkan dengan **Singly Linked List** adalah…

- A. Penggunaan memori yang lebih sedikit.
- B. Kemampuan melakukan traversal ke arah depan maupun belakang secara langsung karena memiliki pointer `prev` dan `next`. ✅
- C. Struktur kode yang jauh lebih sederhana dan mudah diimplementasikan.
- D. Tidak membutuhkan *Garbage Collector* untuk menghapus node.

---

**7.** Pada struktur data **Stack (Tumpukan)**, operasi yang digunakan untuk melihat elemen teratas tanpa menghapusnya dari tumpukan disebut…

- A. Pop
- B. Push
- C. Peek / Top ✅
- D. Dequeue

---

**8.** Dalam implementasi **Stack** menggunakan Slice di Golang, jika `stack` adalah slice bertipe `[]int`, kode yang tepat untuk melakukan operasi **Pop** (menghapus dan mengambil elemen teratas) adalah…

- A. 
  ```go
  top := stack[0]
  stack = stack[1:]
  ```
- B. 
  ```go
  top := stack[len(stack)-1]
  stack = stack[:len(stack)-1]
  ``` ✅
- C. 
  ```go
  top := &stack[len(stack)-1]
  ```
- D. 
  ```go
  stack = append(stack, value)
  ```

---

**9.** Keunggulan utama dari penggunaan **Circular Queue** dibandingkan dengan **Linear Queue** biasa yang diimplementasikan menggunakan array statis adalah…

- A. Circular Queue memiliki kapasitas tak terbatas.
- B. Circular Queue tidak memerlukan pointer depan (`front`) dan belakang (`rear`).
- C. Circular Queue dapat memanfaatkan kembali ruang memori kosong di bagian depan yang telah ditinggalkan oleh elemen yang di-dequeue. ✅
- D. Proses pencarian elemen pada Circular Queue berjalan dalam waktu $O(1)$.

---

**10.** Dalam pemrograman konkuren Golang, komunikasi antar goroutine melalui **buffered channel** bertingkah laku mirip dengan struktur data…

- A. Stack (LIFO)
- B. Tree (Non-linear)
- C. Queue (FIFO) ✅
- D. Graph (Adjacency)

---

**11.** Aturan penempatan node baru pada **Binary Search Tree (BST)** adalah…

- A. Nilai node baru diletakkan acak untuk menjaga keseimbangan tree.
- B. Nilai yang lebih kecil dari root diletakkan di subtree kiri, dan nilai yang lebih besar diletakkan di subtree kanan. ✅
- C. Nilai yang lebih kecil dari root diletakkan di subtree kanan, dan nilai yang lebih besar diletakkan di subtree kiri.
- D. Node baru selalu diletakkan pada level terdalam sebelah kiri.

---

**12.** Traversal pohon biner yang mengunjungi node dengan urutan: **Subtree Kiri, Root, Subtree Kanan** disebut traversal…

- A. PreOrder
- B. PostOrder
- C. InOrder ✅
- D. LevelOrder

---

**13.** Jika sebuah Binary Search Tree (BST) ditelusuri menggunakan traversal **InOrder**, maka urutan data yang dihasilkan akan…

- A. Terurut secara menurun (descending).
- B. Terurut secara menaik (ascending). ✅
- C. Tidak terurut (acak).
- D. Berkelompok berdasarkan genap dan ganjil.

---

**14.** Perhatikan BST berikut:
```text
      8
     / \
    3   10
   / \    \
  1   6   14
```
Hasil penelusuran secara **PostOrder** (Left, Right, Root) dari pohon di atas adalah…

- A. 1, 6, 3, 14, 10, 8 ✅
- B. 8, 3, 1, 6, 10, 14
- C. 1, 3, 6, 8, 10, 14
- D. 1, 3, 6, 14, 10, 8

---

**15.** Syarat mutlak agar kita dapat menjalankan algoritma **Binary Search** pada sekumpulan data di dalam array adalah…

- A. Array tidak boleh kosong.
- B. Array harus memiliki jumlah elemen genap.
- C. Elemen-elemen di dalam array harus sudah dalam kondisi terurut (sorted). ✅
- D. Array harus diimplementasikan menggunakan linked list.

---

**16.** Algoritma **Interpolation Search** bekerja lebih efisien dibandingkan dengan Binary Search biasa pada kondisi…

- A. Elemen data bertipe string dan terurut acak.
- B. Data terurut dan nilainya tersebar merata (uniformly distributed). ✅
- C. Jumlah data sangat kecil (kurang dari 10 elemen).
- D. Data tidak terurut dan memiliki banyak nilai duplikat.

---

**17.** Di Golang, cara paling fleksibel untuk merepresentasikan **Adjacency List** dari sebuah Graph dengan node yang ditandai oleh bilangan bulat (integer) adalah menggunakan tipe data…

- A. `type Graph []int`
- B. `type Graph map[int][]int` ✅
- C. `type Graph [100][100]int`
- D. `type Graph struct { node int }`

---

**18.** Algoritma penelusuran Graph yang menggunakan struktur data **Queue** untuk menjelajahi tetangga terdekat terlebih dahulu secara horizontal sebelum melangkah lebih dalam disebut…

- A. Depth-First Search (DFS)
- B. Breadth-First Search (BFS) ✅
- C. Dijkstra Algorithm
- D. Binary Search

---

**19.** Algoritma **Dijkstra** digunakan untuk menyelesaikan permasalahan…

- A. Menemukan MST (Minimum Spanning Tree) dengan bobot terkecil.
- B. Menemukan jalur terpendek dari satu titik asal ke semua titik lain (Single-Source Shortest Path) pada graph berbobot non-negatif. ✅
- C. Menelusuri seluruh node graph tanpa kembali ke node awal.
- D. Melakukan pengurutan topologi (Topological Sort) pada Directed Acyclic Graph (DAG).

---

**20.** Pada optimasi algoritma Dijkstra untuk graph berukuran besar, struktur data yang paling tepat digunakan untuk mengambil vertex dengan jarak minimum tercepat ($O(1)$ atau $O(\log V)$) adalah…

- A. Stack
- B. Linked List
- C. Priority Queue (biasanya diimplementasikan dengan Min-Heap) ✅
- D. Hash Map standar

---

## Kunci Jawaban

| No | Jawaban | No | Jawaban |
|:--:|:-------:|:--:|:-------:|
| 1  | C       | 11 | B       |
| 2  | B       | 12 | C       |
| 3  | C       | 13 | B       |
| 4  | B       | 14 | A       |
| 5  | C       | 15 | C       |
| 6  | B       | 16 | B       |
| 7  | C       | 17 | B       |
| 8  | B       | 18 | B       |
| 9  | C       | 19 | B       |
| 10 | C       | 20 | C       |

---

*Quiz ini mencakup materi keseluruhan (Struktur Data Linear dan Non-Linear) berbasis Golang untuk Evaluasi Akhir Semester (UAS).*
