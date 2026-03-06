# Minggu 9 — Pengenalan Tree & Binary Tree

Setelah membahas tuntas struktur linear di mana elemen disusun satu demi satu ke belakang. Sekarang kita akan mengubah paradigma pemrograman ke **Arah Hierarkis**: Struktur Data *Tree* (Pohon).

## 1. Konsep Data Tree

Bayangkan seperti susunan silsilah keluarga, struktur folder pada OS Anda (`/var/www/html/...`), atau organisasi sebuah perusahaan (Dari CEO -> Manager -> Staff). 
Itu semua adalah entitas berbentuk **Tree**, di mana satu puncak (*Root*) memilki banyak turunan cabang *(Child nodes)*, dan setiap cabang memiliki cabang lain.

**Karakteristik & Terminologi:**
1. **Root (Akar)**: Node tertinggi / pucuk paling atas (level 0). Jika root kosong, tak ada hierarki memori.
2. **Node (Simpul)**: Entitas penyimpan data / folder.
3. **Edge / Link**: Garis rujukan pointer yang mengarah ke Child node.
4. **Child**: Turunan dari satu simpul bapaknya.
5. **Parent**: Simpul tunggal yang memegang Child.
6. **Leaf (Daun)**: Node yang mandul / letaknya paling ujung bawah dan tak punya Child sama sekali (Node yang bernilai `nil` di ujung pointer cabangnya).

## 2. Definisi Binary Tree

Dari sekian banyak varian Tree (misal N-ary tree yang anaknya bebas tidak ada batas), ada bentuk terpopuler dan terlaris untuk komputasional cepat: **Binary Tree (Pohon Biner)**.
   
Di dalam Golang (atau bahasa lain):
**Satu Binary Node, MAKSIMAL hanya boleh memiliki DUA anak (`Left` dan `Right`)**. Titik! Tidak boleh ada anak tengah.

Jika node hanya punya anak `Left` atau `Right` saja (1 anak) tidak menyalahi aturan.
Bahkan tidak punya anak (Leaf) tetap sah dinamakan Binary Tree.

## 3. Implementasi Struct Node Biner Golang

Pada dasarnya, ini mirip merakit *Linked List*. Hanya bedanya: *Linked List* punya 1 Pointer `Next`... sedangkan *Binary Tree* menyewa Pointernya ganda untuk Bercabang/Terbelah jadi dua (Satu menunjuk ke `*Node` Kiri, satu lagi `*Node` Kanan).

```go
package main

import "fmt"

// 1. ADT Node Pohon Ganda
type TreeNode struct {
	Nilai  int
	Kiri   *TreeNode // Pointer menuju Anak cabang Kiri
	Kanan  *TreeNode // Pointer menuju Anak cabang Kanan
}

// Opsional: Untuk Manajemen Akar (Root) seperti LinkedList.Head
type BinaryTree struct {
	Root   *TreeNode
}

// 2. Fungsi inisialisasi / Buat Simpul Baru
func PembangunanNodeBaru(data int) *TreeNode {
	return &TreeNode{
		Nilai:  data,
		Kiri:   nil, // Secara standar dia adalah daun yang belum beranak
		Kanan:  nil, 
	}
}
```

## 4. Membangun Silsilah secara Manual

Kita hubungkan pointer Golang kita membentuk piramid (Pohon yang membesar di bawah):

```go
func main() {
	// A. Akarnya
	akarUtama := PembangunanNodeBaru(10)
	
	// B. Anaknya: Angka 5 diletakkan di Sayap Kiri, Angka 15 di Sayap Kanan
	akarUtama.Kiri = PembangunanNodeBaru(5)
	akarUtama.Kanan = PembangunanNodeBaru(15)

	// C. Anak-cucu: Angka 5 beranak Kiri (Angka 2), Angka 15 beranak Kanan (Angka 20)
	akarUtama.Kiri.Kiri = PembangunanNodeBaru(2)
	akarUtama.Kanan.Kanan = PembangunanNodeBaru(20)

	// D. Menjelajah Nilainya:
	fmt.Printf("Saya berdiri di akar: %d\n", akarUtama.Nilai)
	fmt.Printf("Saya berdiri di cucu sayap kiri terdalam: %d\n", akarUtama.Kiri.Kiri.Nilai)
	fmt.Printf("Saya berdiri di cabang kanan: %d\n", akarUtama.Kanan.Nilai)
	
    // Apabila saya paksakan Panggil Cucu dari Cabang Kanan yang kosong (akarUtama.Kanan.Kiri):
    // Akan terjadi 'Nil Pointer Dereference' Alias Error System Panic! Karena dia Daun berjarum hampa (NIL)
    // fmt.Printf("Error: %d\n", akarUtama.Kanan.Kiri.Nilai) <--- Segfault
}
```
*Sistem memori sekarang sudah berbentuk hurf "A" atau Piramida V terbalik, tidak tegak lurus sebaris panjang seperti List.*

---
### **Praktikum Pendalaman Logika**
Secara teori, bayangkan Tree ini memiliki Level dan Kedalaman (Height). 
1. Susunlah Tree di atas sehingga Anda tak perlu lagi capek memanggil `node.kiri.kiri.kanan.kiri`, melainkan terotomatisasi secara Rekursif!
2. Jika semua angka kecil dialokasikan ke Kiri, dan Angka Lebih Besar di sebelah Kanan, **Apakah Anda menyadari ini akan mempermudah program dalam MENCARI sebuah nilai dengan sangat cepat?**

*(Inilah yang akan kita kupas di Pertemuan 10: Binary Search Tree).*
