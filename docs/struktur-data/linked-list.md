# Minggu 5 — Singly Linked List

Pada materi variabel Array dan Slice yang kita bahas sebelumnya (Minggu 2), pengalokasian memori berjalan secara "contiguous" (menyatu/berdampingan) di dalam sel memori (RAM). Meski mudah dibaca, hal ini sangat memberatkan CPU ketika Anda menghapus data di tengah rentetan array karena tiap sisa blok data harus Anda geser *satu-per-satu* menutupi lubang yang kosong.

Inilah mengapa struktur data **Linked List** (Senarai Berantai) hadir.

## 1. Konsep Linked List

Bayangkan sebuah permainan "Berburu Harta Karun" menggunakan petunjuk kertas. 
- Anda menemukan Kertas 1 (Simpul pertama). Kertas 1 menyimpan isi (Misal harta karun bernilai 10) beserta alamat rahasia (*ptr*) di mana petunjuk Kertas 2 disembunyikan.
- Anda mendatangi alamat Kertas 2. Di sana terdapat isinya (Nilai 50) dan alamat lagi mencari Kertas 3.
- ... Dan seterusnya hingga bertemu kertas terakhir (*Tail*) yang memiliki petunjuk menunjuk pada kehampaan (Atau disebut `nil` / *NULL*).

Inilah kerangka dasar **Singly Linked List**. Kita sebut setiap petunjuk ini adalah **Node**.

**Karakteristik Singly Linked List:**
1. Memori tidak berdekatan. Mereka acak menyebar di memori Heap. Mereka hanya terhubung dengan Pointer.
2. Panjang data sifatnya **sepenuhnya fleksibel**. Selama kapasitas RAM di Operating System Anda tidak merah, linked list bisa bertambah jutaan Node terus tanpa perlu mengosongkan Array.
3. Node adalah bongkahan objek (Ingat `struct`) yang isinya adalah: **Data** + **Pointer Ke Next Node**.
4. Hanya bisa bergerak **satu arah**, layaknya lintasan jalan satu arah (Maju ke depan mencari *Next*). Anda tidak bisa tiba-tiba mundur ke memori sebelumnya di *Singly Linked List* standar.

## 2. Struktur Memori di Golang (Pointer `*`)

Berikut kita persiapkan blok structnya:

```go
package main

import "fmt"

// 1. Membuat Wadah Bongkahan Objek: Node
type Node struct {
	Data int         // Isi dari Simpul
	Next *Node       // Petunjuk (*Pointer) mencari Node selanjutnya
}

// 2. Head & Ekosistem List
type LinkedList struct {
	Head *Node       // Pointer pertama. Akar/gerbang masuk menuju rantai!
}
```

Bisa Anda perhatikan bahwa variabel `Next` tipenya adalah Pointer tipe ke bongkahan node berikutnya `*Node`. Ciri khas Singly Linked List ada pada properti ini.

## 3. Implementasi Traversal (Menelusuri Rantai)

Untuk menunjukkan bahwa rantai tersebut terhubung, kita dapat membuat *method receiver* pada struct `LinkedList` bernama `PrintList()`. Ia berjalan mulai dari Kepala (Head) sampai ekor yang bernilai `nil`.

```go
// Menampilkan seluruh isi rantai
func (ll *LinkedList) PrintList() {
	if ll.Head == nil {
		fmt.Println("Linked List Kosong!")
		return
	}

	currentNode := ll.Head // Dimulai dari Pintu Gerbang
	
	for currentNode != nil {
		fmt.Printf("[%d] -> ", currentNode.Data)
		currentNode = currentNode.Next // Pindah langkah ke memori Node sebelahnya
	}
	fmt.Println("nil")
}
```

## 4. Implementasi Menambah Antrean (Insert Node Baru Secara Instan)

Mari kita masukkan `InsertAtFront`, memasukkannya ke paling depan dari rantai saat ini. Injeksi *(Insertion)* pada Linked list punya **Kompleksitas O(1) alias seketika**, ini berbanding terbalik dari array *Slice* milik Golang yang memakan O(N) untuk menduplikasi array di latar belakang.

```go
// Menambahkan Elemen dari ujung Depan
func (ll *LinkedList) InsertAtFront(newData int) {
	// Buat Objek Kertas baru 
	newNode := &Node{
        Data: newData,
        Next: nil,
    }

	if ll.Head == nil {
		// Jika Belum pernah ada data apa-apa: Kertas baru adalah Kepala utamanya
		ll.Head = newNode
		return
	}

	// Kertas baru, tunjukkan pointernya menembak ke Kepala List lama
	newNode.Next = ll.Head 

	// Rebut tahkta! Kepala List utamanya sekarang merujuk ke Kertas Baru
	ll.Head = newNode
}
```

## 5. Main Test Program

Satu-satukan function di atas dengan Main:

```go
func main() {
    // Siapkan List-nya
	myList := LinkedList{}

	fmt.Println("Menyimpan Elemen-elemen...")
	myList.InsertAtFront(10)
	myList.InsertAtFront(20)
	myList.InsertAtFront(30)
    
    // Mari telusuri
	// Kondisi Head asli ada di angka 30, yang pointernya ke 20 lalu ke 10.
	myList.PrintList()
    // Hasil terminal: [30] -> [20] -> [10] -> nil
}
```

---
### Evaluasi Teori Singkat
1. Kenapa jika `InsertAtFront`, `newNode.Next` harus direferensikan *(ditembakkan)* ke `ll.Head` terdahulu, bukannya tiba-tiba me-replace nilai head secara langsung?
2. Jika ada `Singly Linked List`, maka ada saudaranya bernama *Doubly Linked List*! Apakah bedanya? 

*(Pekan depan kita akan membahas manipulasi operasi List yang kompleks di tengah-tengah rentetan rantai!)*
