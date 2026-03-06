# Minggu 11 — Algoritma Pencarian

Searching atau pencarian adalah salah satu studi kasus dasar *(Case Method)* dalam merajut struktur data. Kita ditantang untuk menemukan "Sebuah Data Tertentu (Target/Key)" di dalam lautan data. 

Cepat lambatnya Anda "menemukan jarum dalam tumpukan jerami", akan berdampak sangat parah jika data yang Anda cari mencapai jutaan baris (Big Data). 

## 1. Linear Search (Pencarian Linier)
Algoritma purba yang sering dipakai oleh programmer pemula dalam menyusuri `Array` maupun `Singly Linked List`.
Linear search hanya memiliki satu hukum: **Cari dari Awal (indeks 0 atau Head) berurutan sampai Data Ketemu**.

```go
package main

import "fmt"

func LinearSearch(dataSlice []int, target int) int {
	// Loop sederhana dari awal hingga akhir batas (N)
	for indeks, elemen := range dataSlice {
		if elemen == target {
			return indeks // Data Ketemu! Kembalikan No Kursi/Indeksnya
		}
	}
	return -1 // Artinya Gagal Ketemu sampai tuntas!
}

func main() {
	var databaseNilai = []int{54, 23, 70, 11, 89, 43} // Array tak perlu diurutkan

	if pos := LinearSearch(databaseNilai, 89); pos != -1 {
		fmt.Printf("Ketemu di posisi index ke-%d\n", pos) // Hasil: Ke-4
	}
}
```

*Kelebihan*: Sangat fleksibel bisa dipakai pada data apa saja (Acak, tidak berurut, tipe teks maupun angka).
*Kelemahan*: Lambat sekali **O(N)**. Bayangkan jika target berada di indeks ke 999 Juta!

## 2. Binary Search (Pencarian Bagi-Dua)

Di sinilah **Binary Search Tree** *(Pertemuan 10)* atau **Array yang sudah diurutkan (Sorted)** memainkan pedangnya secara mematikan. Algoritma ini memotong target pencarian menjadi 2 Blok Besar secara eksponensial.

Syarat Mutlak: **Datanya Wajib Terurut (Ascending/Descending)**. 

### A. Konteks Binary Search dalam Array
Bagaimana jika kita cari Angka `7` dalam urutan `[1, 3, 5, 7, 9, 11, 15]`
- Langkah 1: Teropong angka TENGAH array-nya. Ia mendapat angka `7`. **BOOM KETEMU! Cuma 1 kali iterasi!**
- Bagaimana kalau cari angka `11`? Teropong angka tengah `7`. Pakai if: "Ternyata target 11 lebih BESAR dari 7". Maka Coret semua angka di kiri angka 7! Fokus ke sayap Kanan `[9, 11, 15]`.
- Langkah 2: Teropong lagi separuhnya. Dapat `11`.

Kompleksitas Asimtotik (Big-O Notasi): **O(log N)**. Sebanyak 10 Miliar Tumpukan Data hanya butuh Maksimal **34 kali** langkah Coret untuk ketemu!

Berikut fungsi Binary Search di slice/array Golang tanpa rekursi *Tree*:

```go
func CariSecaraBinarySlice(berbarisRapi []int, target int) int {
	kiri := 0                  // Penunjuk Pagar depan
	kanan := len(berbarisRapi) - 1 // Penunjuk Pagar belakang

	// Lakukan perputaran selagi batas pagar valid
	for kiri <= kanan {
		nilaiTengahKursi := (kiri + kanan) / 2          // Cari Pivot/Tengahnya
		elemenDipojok := berbarisRapi[nilaiTengahKursi]

		// Jika Target tepat di sasaran Tengah!
		if elemenDipojok == target {
			return nilaiTengahKursi
		}

		// Geser Pagar jika angka di Tengah terlalu Kecil
		if elemenDipojok < target {
			kiri = nilaiTengahKursi + 1 // Coret blok di sebelah Kirinya (Buang)
		} else {
			kanan = nilaiTengahKursi - 1 // Coret blok Kanan
		}
	}

	return -1 // Tak Berada di Garis
}
```

### B. Konteks Binary Search Pada BST (Pointer Biner)

Jika Anda sudah menggunakan Tree, tidak butuh lagi membuat batas Pagar Kiri dan Pagar Kanan! Rekursi memotong 50% pekerjaan ke depan. 

Kombinasi inilah yang dipatenkan Google dan RDBMS MySQL untuk mencari data di sistem mereka. Ia secepat kilat: Bukannya me-Loop 1 juta simpul pointer dalam *Linked List*, Tree hanya mengeksekusi iterasi sedalam jumlah Levelnya. 

```go
// Terapkan ke dalam Codeblock Minggu ke 10 kita:
func (n *TreeNode) CariDiPohon(target int) bool {
    // 1. Kasus Mentok: Sampai ke daun tak ada (Atau Tree Kosong)
	if n == nil {
		return false
	}
    // 2. Ketemu!
	if n.Nilai == target {
		return true
	}

    // 3. Logika Bagi-Dua Eksekusi / Devide-and-Conquer
	if target < n.Nilai {
		// Nilai minus, telusuri Anak Kirinya Rekursif 
		// (Abaikan jutaan anak cabang Kanan milik Induknya!!)
		return n.Kiri.CariDiPohon(target) 
	} else {
		// Telusuri Anak Kanan
		return n.Kanan.CariDiPohon(target)
	}
}

// Di file main(): 
// ketemuCepat := MyTree.Root.CariDiPohon(25) // Output true
```

## 3. Interpolation Search

*(Materi Tambahan)*:
Digunakan jika Anda tahu secara absolut rentang sebaran angka tersebut "Seragam & Linear/Mulus" peningkatannya. Interpolasi bekerja bak membongkar Buku Kamus Alfabetik langsung main tebak perkirakan huruf 'Z' ada di persentase margin buku mana. Berbeda dengan Binary yang saklek "Pasti bagi 2 rata tengah". Walaupun keren, interpolasi akan jeblok perfomanya ke *O(N)* jika penyebaran angkanya terlalu melompat jauh secara acak *(Misal Array isi `1`, sebelahnya `1000`)*.

---

### **Review Pencarian Kelas Praktikum**
Untuk penugasan, rancanglah program komparasi sederhana:
1. Siapkan sebuah *Slice* berisi **Satu Juta Angka Linear Terurut 1 - 1000000** menggunakan perulangan *(Loop).*
2. Golang memiliki *pkg time module* bawaan `time.Now()` dan `.Since()`.
3. Jalankan `LinearSearch(SejutaData, 999990)` dan tangkap kecepatannya (Millisecond!).  
4. Jalankan `BinarySearchSlice(SejutaData, 999990)` dan komparasikan waktunya dengan Linear. Diskusikan fenomena ini di kelas.
