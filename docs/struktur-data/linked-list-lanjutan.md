# Minggu 6 — Operasi Insert/Delete pada Linked List

Melanjutkan materi sebelumnya di Singular Linked List, kita sudah bisa meng-*insert* atau menyisipkan elemen pada *"Head"* list kita (Paling Depan).

Tapi bagaimana jika data yang kita sisipkan perlu diletakkan di tengah-tengah rentetan alamat pointer? Bagaimana cara mencabut *(Delete)* sebuah simpul (Node) tanpa memutuskan dan menghancurkan seluruh memori yang ada setelahnya?

## 1. Menyisipkan Data ke Ujung Belakang (Append/Tail)

Penyisipan *(Insertion)* di akhir Node bisa dibilang mudah tetapi menuntut kita menelusuri Linked List dari akar Kepala *(Head)* satu per satu sampai ketemu Pucuknya bernilai `nil`.

Perhatikan Implementasi dari Method Receiver `InsertAtEnd`:

```go
package main

import "fmt"

func (ll *LinkedList) InsertAtEnd(newData int) {
	newNode := &Node{
        Data: newData,
        Next: nil,
    }

	// Kasus ekstrim: Jika List awal kita kosongan
	if ll.Head == nil {
		ll.Head = newNode
		return
	}

	// 1. Bergerak dari ujung Kepala (Iterasi menelusuri) mencari ekor (Tail)
	currentNode := ll.Head
	for currentNode.Next != nil {
		// Looping tak ada henti selama masih ada surat yang menunjuk alamat selanjutnya
		currentNode = currentNode.Next 
	}

	// 2. Sekarang kita sudah di pucuk (Tail). Tembakkan alamat Pucuk (Next yang tadinya nil) ke Surat yang baru.
	currentNode.Next = newNode
}
```

Kompleksitas Asimtotik dari Pencarian Node terakhir adalah **O(N)**. Walaupun menyisipkannya tetap **O(1)**. Hal ini bisa diperbaiki jika Anda menambahkan property baru ke Object `LinkedList` yakni mendata pointer *Tail*-nya (contoh: `type LinkedList struct { Head *Node; Tail *Node }`. Anda bisa memikirkan trik hemat memori ini!

## 2. Kesaktian Linked List: Insert Di Tengah Seketika

Inilah kelebihan Linked List dari *Array* standard. 
Jika kita ingin *Insert* (Tambah node) misal sesudah data Kertas bernilai [20]. Kita cukup mengambil Pointer Kertas [20] tersebut dan mengarahkan Pointernya ke **Surat Baru**.

Satu hal yang terancam **PENTING**: Alamat Kertas berikutnya *(Next lama)* dari Kertas [20] harus Anda rekat dulu pada **Surat Baru**. Jika keliru, memori di depannya akan bocor / terputus!

Langkah:
- Ciptakan Objek Node Baru `NewNode`
- *NewNode.Next* mengarah ke simpul berikutnya setelah Simpul Acuan (Posisi insert). `NewNode.Next = Target.Next`
- Barulah Simpul Acuan memutus alamatnya, ia sekarang mengarah ke Objek Baru tadi. `Target.Next = NewNode`

```go
func (ll *LinkedList) InsertAfter(targetNode *Node, newData int) {
	// Cegat jika targetNode-nya kosong
	if targetNode == nil {
		fmt.Println("Error: Target memori tak ada!")
		return
	}

	// Kertas Simpul Baru
	newNode := &Node{
		Data: newData,
		Next: targetNode.Next, // PENTING: selamatkan referensi anak-anak di depan
	}

	// Berbelok: Target merujuk jalannya ke arah Simpul Baru.
	targetNode.Next = newNode
}
```

## 3. Mencabut Node Penuh Resiko (Deletion)

Proses Delete di Single Linked List merupakan operasi yang memotong jalur pointer simpul agar tidak lagi terekam dalam sirkuit `Head` ke `Tail`, sehingga **Go Garbage Collector** kelak akan menyapu memori yang tidak memiliki pointer penunjuk kepadanya (membebaskan RAM OS Anda otomatis!).

Sama mekanismenya jika Anda mendatangi jalinan kertas:
`[11] -> [22] -> [33] -> nil`

Jika Anda ingin membuang angka `22`, Anda harus berdiri di simpul `11`, merubah penunjuk '*Next*' dari si `11` melompati `22` dan menunjuk langsung ke `33`.
Sehingga struktur logik akan menjadi: 
`[11] -> [33] -> nil`.  `(Angka 22 lenyap dan akan disapu Go)`

```go
func (ll *LinkedList) DeleteByNilai(dataYangDibuang int) {
	if ll.Head == nil {
		return
	}

	// Kasus ekstrim: Kalau yang dicabut itu Kepalanya sendiri
	if ll.Head.Data == dataYangDibuang {
		ll.Head = ll.Head.Next // Kepala baru dimundurkan ke orang kedua
		return
	}

	// Iterasi untuk mencari siapa Kertas 'Sebelum' orang yang dicabut!
	currentNode := ll.Head
	for currentNode.Next != nil && currentNode.Next.Data != dataYangDibuang {
		// Melangkah Maju
		currentNode = currentNode.Next
	}

	// Setelah Loop Tembus: Apakah orang tersebut ketebak / ketemu?
	if currentNode.Next == nil {
		fmt.Println("Angka gaet-cabut tidak ditemukan dalam Linked List.")
		return
	}

	// Ditemukan! currentNode sekarang di KERTAS SEBELUM angka incaran.
	// Hancurkan Jembatannya, lompat dua kali!
	currentNode.Next = currentNode.Next.Next
}
```

## 4. Circular Linked List

Jika Single Linked List mempatok `Pucuk Node` bernilai `nil`. Maka pada List ini, Pucuk Node menembakkan alamat pointernya ke **Head Node**! Ia berputar secara terus menerus bagaikan cincin, tanpa ujung (Circular).
Sering dipakai untuk *Round-Robin CPU Scheduler* agar men-distribusi CPU secara gantian dari atas s/d bawah tak henti-henti.
  
---

### **Praktikum / Mini PBL (Problem-Based Learning)**
Pada Go, struktur List ini tidak secara bawaan (*Built-in*) sekomplit ini, melainkan harus anda susun sendiri. Cobalah ketik kode `LinkedList` lengkap pada IDE Anda:
1. Panggil *InsertAtFront(40)* dan *InsertAtFront(99)*
2. Panggil *InsertAtEnd(15)*
3. Lalu implementasikan fungsi *PrintList()* di akhir untuk memastikan outputnya di layarsudah serasi!
4. Mainkan fungsi *DeleteByValue(40)*, Print kembali daftar Linked List Anda, dan saksikan perbedaannya.
