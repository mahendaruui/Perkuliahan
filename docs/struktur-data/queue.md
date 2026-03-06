# Minggu 4 — Queue FIFO & Implementasinya

Antrean (Queue) adalah struktur data linear yang bekerja dengan prinsip keterbalikan dari Stack, yaitu berkonsep **FIFO (First In, First Out)**. 

Bagaikan pelanggan yang sedang mengantre di kasir swalayan: orang pertama yang mengantri (bergabung ke barisan antrean), pasti akan menjadi orang pertama pula yang dilayani dan meninggalkan barisan.

## 1. Karakteristik Queue
Queue umumnya memelihara dua poin alamat/indeks referensi yang terus bertransisi: depan (*Front* atau *Head*) dan belakang (*Rear* atau *Tail*).

### Konsep Transaksi Operasi Dasar:
- **Enqueue (Add)**: Menyisipkan atau menambahkan elemen data ke bagian *belakang (Tail/Rear)* queue.
- **Dequeue (Remove)**: Mengambil dan menghapus elemen dari bagian *depan (Head/Front)* queue.
- **Front (Peek)**: Meninjau elemen yang paling awal dari queue, namun tidak membuangnya.
- **Rear**: Meninjau elemen yang berada di paling akhir tanpa pemrosesan pembuangan.

## 2. Implementasi Algoritma Linear Queue

Secara pemrograman Go, Queue dapat dibuat mudah mengandalkan Slice bawaannya.

```go
package main

import "fmt"

type LayananAntrean struct {
    Items []int
}

// Enqueue - Masukkan ke Belakang
func (q *LayananAntrean) Enqueue(pelangganID int) {
    q.Items = append(q.Items, pelangganID)
    fmt.Printf("Pelanggan %d bergabung ke dalam antrean.\n", pelangganID)
}

// Dequeue - Layani dan Hapus dari Depan
func (q *LayananAntrean) Dequeue() (int, bool) {
    if len(q.Items) == 0 {
        return -1, false // Jika kosong, tolak
    }

    orangPertama := q.Items[0]    // Tangkap data antrean pertama
    q.Items = q.Items[1:]        // Iris slice agar membuang isi indeks ke-0 (Hati-hati, ada konsekuensi memory leak di slice!)
    return orangPertama, true
}

func main() {
    bankAntrean := LayananAntrean{}
    bankAntrean.Enqueue(1001) // Datang jam 08.00
    bankAntrean.Enqueue(1002) // Datang jam 08.05
    bankAntrean.Enqueue(1005) // Datang jam 08.10

    orang, ok := bankAntrean.Dequeue()
    if ok {
        fmt.Println("Melayani pelanggan ID:", orang) // Bakal melayani 1001
    }

    fmt.Println("Sisa antrean:", bankAntrean.Items) // Menyisakan [1002, 1005]
}
```

## 3. Jenis-Jenis Queue
Pada Queue model dasar (Sederhana), jika kita memanfaatkan array yang ukurannya terpatok mati *(Fixed Size Array)*, apabila elemen `Rear` menyentuh batas ujung `Capacity`, maka tak ada data baru yang bisa ditambah walaupun di depan kita (*Front*) sudah banyak yang dilayani. Oleh karena itu kita butuh teknik lainnya:

### A. Circular Queue (Antrean Melingkar)
Circular Queue memanipulasi alamat *pointer* Front dan Rear menggunakan modulus aritmatika (Sisa Bagi). Sehingga apabila antrean bagian blakang sudah mentok, *Rear* bisa memutar indeksnya ulang ke depan mengisi slot awal yang sudah dialokasikan kosong sebelum antrean ditolak oleh sistem `Queue Is Full()`.

*Rumus Enqueue Circular*: `Rear = (Rear + 1) % Kapasitas`
*Rumus Dequeue Circular*: `Front = (Front + 1) % Kapasitas`

### B. Double-Ended Queue (Deque)
Adalah tipe struktur hibrid antara *Stack* dan *Queue*. 
Elemen bisa di-masukkan (*Insert*) secara dua arah (Bisa di depan *maupun* di belakang), begitu juga dihapus (*Remove*) di depan atau belakang.
Contoh penerapannya ada pada **Aplikasi Penjadwalan Multi-Level (*OS Schedulers*)**.

## 4. Keunggulan dan Kompleksitas Algoritma

**Asymptotic Analysis (Notasi Big-O)**
- Operasi Enqueue (tambah baru): `O(1)` Konstanta konstan.
- Operasi Dequeue (ambil bagian depan): Tergantung implementasi. Jika memakai Singly Linked List bersimbolkan `head`, ini `O(1)`. Namun pada implementasi irisan `Slice` dasar bawaan golang seperti kode di atas (`q.Items[1:]`), setiap elemen dalam *background* di-*copy* satu slot ke depan oleh compiler, maka kompleksitasnya secara tersembunyi dapat menjadi **O(N)**.
  
Ini adalah alasan kuat kenapa Queue skala besar *(Production Level)* disarankan dibangun menggunakan kombinasi node pointer (Singly Linked List) ketimbang Slice/Array biasa.

---
### **Tugas Kajian Mandiri (Case Method)**
Pada tugas kuliah asinkron minggu ini:
1. Golang memiliki keunikan **Concurrency** yang menggunakan `Channel`. Channel pada sejatinya berperilaku layaknya **Queue Multi-akses Sinkronisasi**. Pelajari bagaimana syntax dasar channel pada `goroutines` bekerja secara FIFO.
2. Buatlah struktur *Queue* antrian pelanggan (mis. pembelian tiket bioskop) di mana hanya melayani pembeli tiket jika batas maksimal gedung bioskop tak terpenuhi. Jika terpenuhi kirim "Full/Batal".
