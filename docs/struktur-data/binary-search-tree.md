# Minggu 10 — Binary Search Tree (BST)

Dalam pertemuan 9, Anda telah melihat bahwa memuat Node ganda sangat tidak efektif jika dijalankan manual (`akar.Kiri.Kiri.Kanan`).

**Binary Search Tree (BST)** adalah aplikasi nyata dari pohon biner. Ini bukan sembarang pohon: BST punya **Aturan Tertulis (Invariant)** saat Anda ingin memasukkan nilai baru (Insert) agar pencariannya kelak menjadi sangat instan tanpa harus keliling seluruh cabang (Search).

Aturan BST:
1. Setiap cabang biner (Parent) memiliki angka x. 
2. Semua Node anak cabangnya di sebelah **KIRI**, **HARUS LEBIH KECIL dari BAPAKNYA (X)**.
3. Semua Node anak cabangnya di sebelah **KANAN**, **PUNYA NILAI LEBIH BESAR ATAU SAMA DENGAN BAPAKNYA (X)**.
4. Karena aturan perbandingan matematis ini, struktur biner tidak bisa diisi gabungan integer dan string sekaligus yang tak bisa dibanding. Harus seragam.

## 1. Menyisipkan Nilai Biner dengan BST

Untuk menyelesaikan tantangan *Insert* yang berjenjang tanpa limit (Tree Kedalaman Ratusan), Node menggunakan kekuatan *Call Stack* atau bahasa kita: **Rekursi (Memanggil Fungsinya Sendiri)**.

```go
package main

import "fmt"

type TreeNode struct {
	Nilai int
	Kiri  *TreeNode
	Kanan *TreeNode
}

// 1. Rekursi Insert
// Menerima akar sub-tree dan nilai yang ingin dicangkokkan
func (node_terpilih *TreeNode) InsertBst(dataBaru int) {
	// Jika angka bawaan lebih kecil, bergeser atau berotasi ke Sayap KIRI
	if dataBaru < node_terpilih.Nilai {
		if node_terpilih.Kiri == nil {
			node_terpilih.Kiri = &TreeNode{Nilai: dataBaru}
		} else {
			// Rekursi! Jika terisi penuh cabangnya, perintahkan anaknya turun kebawah!
			node_terpilih.Kiri.InsertBst(dataBaru)
		}
	} else if dataBaru > node_terpilih.Nilai {
		// Jika lebih besar, bergeser berotasi ke Sayap KANAN
		if node_terpilih.Kanan == nil {
			node_terpilih.Kanan = &TreeNode{Nilai: dataBaru}
		} else {
			// Jalankan diri kembali untuk mengorek sisi Kanan Node selanjutnya
			node_terpilih.Kanan.InsertBst(dataBaru)
		}
	}
}

// 2. Pembungkus BST Tree agar Rapih
type BinarySearchTree struct {
	Root *TreeNode
}

// Pembungkus insert Bst
func (tree *BinarySearchTree) Insert(data int) {
	if tree.Root == nil {
		tree.Root = &TreeNode{Nilai: data} // Data Pertama sebagai Akar Utamanya
	} else {
		tree.Root.InsertBst(data)         // Panggil Rekursi Traversal
	}
}

func main() {
    MyTree := BinarySearchTree{}
	// Buat BST secara terstruktur dan tertata
	MyTree.Insert(50)  // Rootnya

	// Anak-anak otomatis berjalan sendirinya 
	MyTree.Insert(30)  // Nilai 30 < 50 (Sayap Kiri)
	MyTree.Insert(100) // Nilai 100 > 50 (Sayap Kanan)
	MyTree.Insert(25)  // Nilai 25 < 50 (Ke Kiri) Tapi 25 < 30 (Ke Kiri lagi cucunya 30)
}
```

## 2. Tree Traversal (Menelusuri & Menampilkan Data)

Menelusuri semua nilai dalam Linear Array mudah `(for i:=0; i<len; i++)`. Tetapi dalam hirarki struktur yang sangat acak (Non-Linear), bagaimana caranya agar tidak ada yang terlewat? 

Sekali lagi kita berterima kasih pada Go *Recursion Feature*.

### A. PreOrder Traversal 
*(Akar -> Kiri -> Kanan)*
Tampilkan *Root*-nya, lalu segera babat seluruh cabangnya per-rekursi. Cocok untuk meng-*clone* atau menyalin struktur BST utuh.

### B. InOrder Traversal
*(Kiri -> Akar -> Kanan)*
Berkebalikan, datangi terdalam ujung Daun Paling Kiri *(Ingat: Aturan BST kiri adalah angka terkecil kan?)* Lalu tampilkan Akar aslinya, lalu ke Kanannya.
Tujuan **InOrder**: Menghasilkan daftar Array Angka yang **Sangat Presisi Terurut (Soeted Ascending / Naing)** secara otomatis!

```go
// Tampilkan Dalam Urutan Naik Paling Efisien!!
func InOrder(node *TreeNode) {
	if node != nil {
		InOrder(node.Kiri)            // Ekstrak Sampai Daun Kiri Habis!
		fmt.Printf("%d ", node.Nilai) // Cetak Nilai Aslinya (Lantai terendah duluan)
		InOrder(node.Kanan)           // Ekstrak anak kanannya
	}
}
```

### C. PostOrder Traversal
*(Kiri -> Kanan -> Akar)*
Sapu semua anak-cucunya lebih dulu sebelum menelusuri orang tuanya. Cocok digunakan saat operasi pembersihan *Garbage Memory* (`Delete Tree`). Jadi orang tua tak akan terhapus jika anaknya masih ngutang nyantol di memori.

---

### **Diskusi Praktek**
1. Eksekusi kode InOrder pada variabel `MyTree` di function Main! Anda akan melihat Angka 30, 25, 50, dan 100 tercetak secara *Magic* membentuk barisan rapi: **25, 30, 50, 100**.

Bisa dibayangkan apa jadinya jika kita memilik puluhan juta file *B-Tree Database Index* pada SQL *(Semua Database MySQL menggunakan B-Tree dan BST di dalam engine-nya untuk kecepatan)*.

*(Hal inilah yang akan dievaluasi saat membahas Pencarian di Pertemuan 11).*
