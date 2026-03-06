# Minggu 12 — Graph: Konsep Dasar & Representasinya

Kita sebelumnya telah membahas *Tree*. Tahukan Anda bahwa Tree sebenarnya adalah bentuk istimewa dari sebuah Graph? Hanya saja Tree dilarang untuk *looping* kembali ke bapaknya. Sedangkan **Graph** sama sekali tidak kenal kompromi dan batasan aturan.

Semua node dalam graph bebas terhubung dengan simpul lain.
Penerapan nyatanya sangat masif: **Jaringan Topologi Jaringan Komputer**, **Peta Google Maps (Jalanan Kota)**, hingga relasi sosial seperti jaringan pertemanan **Facebook** atau **LinkedIn**.

## 1. Terminologi Graph
1. **Vertex (Simpul / Node):** Entitas utamanya. Contoh: Stasiun Kereta, atau Nama Kota.
2. **Edge (Garis/Sisi):** Garis penghubung yang merekatkan atau menghubungkan kedua Vertex. Contoh: Jalan Tol/Rel Kereta yang menghubungkan dua kota.
3. **Directed Graph (Berdarah Tunggal):** Edge yang bersifat satu arah (one-way street). Instagram *Followers* adalah contoh *Directed*: Anda *Follow* artis A (Anda -> Artis A), artis A tidak men-follow Anda otomatis. 
4. **Undirected Graph (Dua Arah / Mutual):** Garis yang bolak-balik serasi. Misalnya, di Twitter jika A membalas DM B, itu adalah jalur dua arah. Atau di Facebook jika berteman.
5. **Weighted Edge (Garis Berbobot):** Setiap garis tol biasanya dibebankan harga atau *Jarak Kilometer*. Bobot inilah yang nanti dihitung Algoritma Rute Terpendek!

## 2. Cara Menyimpan Jaringan Acak ke Memori Array

Jika ditanya, memori komputer kan berbentuk *Linear / Berbaris*. Bagaimana kita memaksa bentuk jaringan kompleks ini masuk ke kode program Golang kita secara presisi matematis?
Ada dua solusi paling populer: **Adjacency Matrix** dan **Adjacency List**.

### A. Adjacency Matrix (Matriks Keterhubungan Bertetangga)
Berupa tabel 2-Dimensi atau di Golang adalah `Array[][] / Slice[][]`.

Jika ada N Simpul, berarti ia butuh tabel memori seukur `N x N` blok. Sangat boros. Jika simpulnya (0,1,2,3). Garis koneksi dilambangkan dengan angka 1 (Jika ada rute) dan 0 (Jika buntu).
Sangat tidak ramah efisiensi jika Edge sedikit namun Vertex ribuan *(Sparse Graph)*.

| | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 0 | 1 | 0 | 0 |
| **1** | 1 | 0 | 1 | 1 |
| **2** | 0 | 1 | 0 | 0 |
| **3** | 0 | 1 | 0 | 0 | 

### B. Adjacency List (Daftar Tetangga)
Metode populer yang **Paling Hemat Memori**. Biasanya mengkombinasikan *Array* dengan *Linked List*. Namun karena *Golang* canggih, **kita bisa memadukan Tipe Data `Map` dengan `Slice`!**

Di Golang, `map` (Hash Table bawaan C yang sangat kencang) akan menyimpan Label/Nama Node-nya. Lalu nilai valuenya adalah `Slice` *(array tak terbatas)* yang isinya daftar anak yang terhubung kepadanya.

```go
package main

import "fmt"

// Struktur Pengelola Topologi Perkotaan (Graph Kosong)
type GraphPerkotaan struct {
	// Peta ajaib: (Key = Nama Kota/Huruf) -> (Value = Daftar tetangga tersambung)
	tetangga map[string][]string 
}

// 1. Inisialisasi Kota Baru (Tanpa relasi jalanan satupun awalnya)
func (g *GraphPerkotaan) TambahKota(namaKota string) {
	// Cegat jika kota sudah pernah dipetakan oleh Pemda
	if _, sudahAda := g.tetangga[namaKota]; !sudahAda {
		// Buat petak kosong
		g.tetangga[namaKota] = []string{}
	}
}

// 2. Tambah Jalur Jalan Tol (Edge) Dua Arah! (Undirected)
func (g *GraphPerkotaan) BikinJalanTol(kotaAsal string, kotaTujuan string) {
	// A ke B bisa dilalui
	g.tetangga[kotaAsal] = append(g.tetangga[kotaAsal], kotaTujuan)
	// B ke A harus diketuk juga
	g.tetangga[kotaTujuan] = append(g.tetangga[kotaTujuan], kotaAsal)
}

// Fungsi Pencetak Visual Terminal
func (g *GraphPerkotaan) TampilkanPetaGoogle() {
	for originKota, jalanCabang := range g.tetangga {
		fmt.Printf("Kota %v Terakses ke -> %v\n", originKota, jalanCabang)
	}
}

func main() {
	// Setel Pemetaan ke Memori! 
	PeminjamanMemori := &GraphPerkotaan{
		tetangga: make(map[string][]string), // (WAJIB) Make() mengaktifkan memory Hash Map Golang
	}

	// 1. Bangun Perumahannya
	PeminjamanMemori.TambahKota("Banda Aceh") // A
	PeminjamanMemori.TambahKota("Sigli")      // S
	PeminjamanMemori.TambahKota("Bireuen")    // B
	PeminjamanMemori.TambahKota("Meulaboh")   // M

	// 2. Proyek Jalan Tol
	PeminjamanMemori.BikinJalanTol("Banda Aceh", "Sigli") // Terhubung!
	PeminjamanMemori.BikinJalanTol("Sigli", "Bireuen")
	PeminjamanMemori.BikinJalanTol("Banda Aceh", "Meulaboh")

	PeminjamanMemori.TampilkanPetaGoogle()
}
```

Output di terminal akan sangat akurat dengan Realita Topologi Provinsi Aceh:
```bash
Kota Bireuen Terakses ke   -> [Sigli]
Kota Banda Aceh Terakses ke-> [Sigli Meulaboh]
Kota Sigli Terakses ke     -> [Banda Aceh Bireuen]
Kota Meulaboh Terakses ke  -> [Banda Aceh]
```

## 3. Kehebatan Map + Slice pada Golang
Jika di bahasa C standard Anda harus pontang panting merangkai Struct Struct Struct LinkedList hanya demi menyusun relasi Adjacency List, **Golang** memberikan Anda sintaks tingkat tinggi *Hashtable Dictionary* `(map[key]value)`. Ini sangat sangat menghemat waktu pemrograman dan mencegah keborosan Pointer di OS.
*(Minggu depan: Rute Terpendek! Bagaimana jika masing-masing Tol ini diberi harga / Jarak Tempuh).*
