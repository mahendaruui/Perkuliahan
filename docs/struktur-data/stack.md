# Minggu 3 — Stack & Operasi Dasar

Stack (Tumpukan) adalah struktur data linear yang mengikuti prinsip **LIFO (Last In, First Out)**. Konsepnya sesederhana tumpukan buku: buku yang terakhir diletakkan di atas tumpukan akan menjadi buku pertama yang diambil ketika kita ingin mengambil buku dari tumpukan tersebut.

## 1. Karakteristik Stack
Stack hanya mengizinkan manipulasi data pada satu ujung, yang biasanya disebut sebagai **Top**.

Ada 3 operasi utama dalam Stack:
- **Push**: Menambahkan elemen ke puncak (Top) dari stack.
- **Pop**: Menghapus dan mengembalikan elemen yang ada di puncak stack.
- **Peek / Top**: Melihat elemen yang ada di puncak tanpa menghapusnya.
- **IsEmpty**: Mengecek apakah stack dalam keadaan kosong.

## 2. Penggunaan Stack di Dunia Nyata
Algoritma ini sangat berguna dalam pemrosesan fungsional dan aplikasi praktis:
1. **Mekanisme Undo/Redo** pada editor teks seperti Ms. Word atau Visual Studio Code.
2. **Riwayat Browser (Back Button)**: Menavigasi kembali ke halaman sebelumnya.
3. **Penyusunan Memory Sistem (Call Stack)**: Sistem operasi mengatur pemanggilan fungsi-(rekursif) menggunakan stack memori.
4. **Pengecekan Kurung Seimbang (*Balanced Parentheses*)** pada compiler dan linter bahasa pemrograman.

## 3. Implementasi Stack menggunakan *Slice* di Golang

Di bahasa pemrograman tingkat tinggi seperti Golang, kita dapat membangun Stack secara efisien menggunakan tipe data dinamis bawaan yaitu **Slice**.

Mari kita definisikan tipe bentukan (ADT) Stack menggunakan `struct` dan menjadikannya OOP-Friendly dengan `Receiver Method`.

### a. Membuat Struct `Stack`

```go
package main

import "fmt"

// Mendefinisikan Abstract Data Type (ADT) untuk Stack
type Stack struct {
	items []string
}
```

### b. Menambahkan Metode `Push`

Ingat materi minggu lalu! Karena kita memanipulasi atau mengubah bentuk array internalnya, kita harus menggunakan metode dengan *Pointer Receiver* (`*Stack`).

```go
// Menambahkan elemen ke atas Stack
func (s *Stack) Push(data string) {
	s.items = append(s.items, data)
	fmt.Printf("Pushed: %s\n", data)
}
```

### c. Menambahkan Metode `Pop` dan `Peek`

Pada `Pop`, elemen terakhir pada Slice akan dipisahkan, dikembalikan ke pemanggil, dan panjang slice akan dikurangi 1.

```go
// Mengambil dan menghapus elemen teratas dari Stack
func (s *Stack) Pop() (string, bool) {
	if len(s.items) == 0 {
		return "", false // Mengembalikan false jika stack kosong
	}
	
	lastIndex := len(s.items) - 1
	topElement := s.items[lastIndex]
	// Potong array hingga elemen ke-n dikurangi 1
	s.items = s.items[:lastIndex]
	
	return topElement, true
}

// Melihat elemen teratas tanpa menghapusnya
func (s *Stack) Peek() (string, bool) {
	if len(s.items) == 0 {
		return "", false
	}
	lastIndex := len(s.items) - 1
	return s.items[lastIndex], true
}

// Cek status Stack
func (s *Stack) IsEmpty() bool {
	return len(s.items) == 0
}
```

### d. Fungsi `main()` untuk Pengujian (Kasus Riwayat Browser)

```go
func main() {
	var riwayatBrowser Stack

	// Simulasi Navigasi Pengguna
	riwayatBrowser.Push("google.com")
	riwayatBrowser.Push("github.com/mahendar")
	riwayatBrowser.Push("golang.org/doc")

	// Melihat situs saat ini tanpa keluar
	currentSite, _ := riwayatBrowser.Peek()
	fmt.Println("Situs Tertinggi (Saat Ini):", currentSite) // Golang doc

	// Pengguna menekan tombol 'Back'
	kembali, adaSitus := riwayatBrowser.Pop()
	if !adaSitus {
		fmt.Println("Riwayat Kosong!")
	} else {
		fmt.Println("Meninggalkan:", kembali)
	}

	// Cek Situs Sekarang
	fmt.Println("Kembali dan Sedang Berjalan Di:", riwayatBrowser.items[len(riwayatBrowser.items)-1]) 
    // Hasil: github.com
}
```

## 4. Analisis Kompleksitas Stack (Big-O)

Bagi operasi menggunakan Slice dinamis seperti di atas (dan array normal), Kompleksitas Waktu untuk Push, Pop, dan Peek adalah mutlak konstanta yang sangat cepat:
- **Push**: `O(1)` - (Secara amartisasi, bila *capacity* internal slice membesar mungkin `O(N)` sesaat, bergantung dari alokasi OS).
- **Pop**: `O(1)`
- **Peek**: `O(1)`
- **Search**: `O(N)` - Pencarian isi stack tanpa Popping mengharuskan pemeriksaan linear penuh.

---
### **Praktikum Kelas**
Gunakan waktu kelas untuk menyusun kode stack yang mampu:
1. Membaca untaian string yang berisi kurung, contoh: `"(([]{}))"`
2. Lakukan iterasi (*looping*) tiap karakter; jika ketemu buka kurung `( { [`, lemparkan ke stack menggunakan cara `Push()`.
3. Jika bertemu kurung tutup, lihat stack yang *peek*, jika pasangan sesuai, keluarkan pakai `Pop()`. Cek apakah kode *error* jika tak seimbang!
