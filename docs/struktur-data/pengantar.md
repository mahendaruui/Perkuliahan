# Minggu 1 — Pengantar Struktur Data

## Apa itu Struktur Data?

**Struktur Data** adalah cara mengatur, menyimpan, dan mengelola data di dalam komputer sedemikian rupa sehingga data tersebut dapat digunakan secara efisien. Memilih struktur data yang tepat akan sangat berpengaruh pada performa komputasional sebuah aplikasi, terutama jika dipadukan dengan Algoritma yang efisien.

Secara garis besar, Struktur Data dibedakan menjadi dua berdasarkan organisasinya:
1. **Linear Data Structure**:
   - Diatur secara berurutan dan linier. Elemen di dalamnya sejajar satu sama lain.
   - Bersifat efisien untuk iterasi sederhana namun memiliki keterbatasan memori.
   - Contoh: Array, List, Stack, Queue.
   
2. **Non-Linear Data Structure**:
   - Diatur secara hierarkis atau terhubung ke banyak node secara kompleks.
   - Memudahkan pencarian data kompleks menggunakan *Traversal*, dan pengelompokan secara logik.
   - Contoh: Tree (BST, B-Tree, dll), Graph.

## Mengapa Menggunakan Golang?

Dalam perkuliahan ini, kita menggunakan ekosistem **Go (Golang)** yang memiliki karakteristik berikut:
- **Compiled & Fast:** Tidak butuh mesin virtual seperti Java (JVM) untuk tereksekusi, menjadikannya secepat bahasa C.
- **Memory Management via Pointers:** Walaupun memiliki *Garbage Collection* otomatis, Go menawarkan kontrol penuh melalui **Pointer (`*&`)** kepada Programmer layaknya bahasa C dan C++. Hal ini sangat esensial ketika kita berbicara tentang **Linked List** dan **Tree** yang memerlukan pemahaman relasi letak memori (alamat).
- **Concurrency Default (Goroutines):** Mengembangkan Queue yang multi-threading sudah masuk ke dalam desain Go itu sendiri.

Bagi Anda yang terbiasa menggunakan PHP atau Javascript, ini adalah batu loncatan awal untuk memahami bagaimana bahasa tingkat lebih rendah / performa tinggi menyusun memori saat dieksekusi (*Memory Layout*).

## Karakteristik Data Linear
### 1. Array & Slice
*Array* dalam Golang memiliki panjang (*length*) yang kaku. Sedang *Slice* memiliki *length* (elemen tersedia) dan *capacity* (batas memori yang dialokasikan sebelum perlu menyalin memori baru).
Contoh singkat deklarasi Slice di Go:
```go
// Menyiapkan slice linear dengan panjang kaku
var antrian = make([]int, 0, 5) // {kapasitas 5}

// Anda bisa mengisi datanya linear:
antrian = append(antrian, 1) // masuk ke indeks 0
antrian = append(antrian, 2) // masuk ke indeks 1
```

### 2. Memori Referensi & Garis Besar Pointer
Karakteristik penting data saling berhubungan secara linear di C/Go adalah berawal dari variabel yang menyimpan **Alamat Memori**. 

| Variabel | Tipe Data Asal | Tipe Pointer | Cara Mengisi |
| :-- | :-- | :-- | :-- |
| `a := 10` | `int` | `*int` | `pointerT := &a` |

Pointer ini akan menjadi gerbang ke Materi Minggu Ke-2 dan Ke-5 terkait *Node* pada **Linked List**.

## Karakteristik Data Non-Linear
### 1. Root & Cabang (Tree)
Berbeda dengan urutan baris, kita melihat Node sebagai Entitas yang mempunyai rujukan lain ke banyak arah.
Sebagai contoh "File Directory" pada *Operating System* Anda: 
- Root: `C:/`
   - Child 1: `Program Files/`
   - Child 2: `Windows/`
     - System32/

Struktur Data ini sangat cocok jika data saling bergantungan satu sama lain dan membentuk hierarki tak terbatas di setiap batangnya.

### 2. Jaringan Bebas (Graph)
Mirip seperti Peta / Map dari kota A ke Kota B. Satu entitas saling terhubung bebas dengan seutas garis tanpa melihat mana yang Root dan mana yang Cabang. Ini seringkali diterapkan di Graph Relasional seperti relasi pertemanan *(Friendship / Followers)* pada Media Sosial.

---
### Tugas Refleksi
1. Pastikan Golang (`go version`) sudah terpasang di komputer Anda. 
2. Carilah perbedaan fundamental tentang bagaimana bahasa Python / NodeJs menyimpan variabel ke memori jika dibandingkan dengan Golang atau bahasa C.

*(Lanjut ke Materi Minggu-2)*
