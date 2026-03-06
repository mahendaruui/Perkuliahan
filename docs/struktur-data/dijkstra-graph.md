# Minggu 13 — Graph Lanjutan: Algoritma Dijkstra

Pada minggu lalu (Pertemuan 12), kita sudah bisa memetakan Graph Topologi Kota menggunakan `map` Golang. Namun, kita belum memasukkan **Bobot/Harga/Jarak (Weight)** pada setiap *Edge* (Jalan Tol) tersebut.

Dalam kasus nyata, Google Maps tidak hanya peduli "Apakah Kota A terhubung ke Kota B?".
Mereka memproses: "Berapa Kilometer Jaraknya?", "Berapa lama Estimasi Waktu Tempuhnya?".
Inilah yang disebut dengan permasalahan **Shortest Path (Jalur Terpendek)**.

## 1. Algoritma Dijkstra
Ada banyak algoritma mencari jalur terpendek (Bellman-Ford, A* Search, Floyd-Warshall). Namun rajanya pencarian rute pada Graph dengan Bobot Positif (Tak ada yang minus jaraknya) adalah algoritma ciptaan Edsger W. Dijkstra tahun 1956.

Algoritma ini menggunakan **Pendekatan Greedy**. Artinya, ia beranggapan dengan selalu memilih tetangga terdekat yang paling logis di setiap langkah secara "rakus/cepat", pada akhirnya kita akan sampai ke tujuan dengan sisa ongkos *(Cost)* termurah secara keseluruhan.

### Aturan Main Dijkstra:
1. Mulai dari satu **Titik Awal** (Source Node). Catat Jarak ke diri sendiri adalah `0`.
2. Asumsikan jarak ke semua kota/simpul lain di peta adalah **Infinity (Tak Terhingga / 99999999)** karena kita belum pernah mengeksplorasinya sama sekali.
3. Gunakan **Priority Queue / Min-Heap** (Atau perulangan pengecekan jarak terendah) untuk menyorot kota yang paling mudah digapai di radius sekitar kita.
4. Kunjungi tetangganya satu per satu. Hitung: `(Jarak saat ini + Bobot/Jalan Tol ke tetangga)`. 
5.  **Jika Hasilnya LEBIH KECIL dari catatan jarak si Tetangga sebelumnya (yang mungkin Infinity/999), MAKA UPDATE catatannya jadi jarak baru yang lebih murah!**
6. Simpul yang sudah dieksplorasi (Visited), ditandai selesai agar tidak mutar-mutar tiada akhir *(Infinite Loop)*.
7. Ulangi Langkah 3 sampai semua kota *Visited*.

## 2. Implementasi Graph Berbobot (Weighted Graph) di Golang

Untuk mensimulasikan bobot, kita tidak bisa lagi menggunakan `map[string][]string`. 
Karena isi / valuonya bukan sekedar "Nama Tujuan", melainkan "Nama Tujuan + Ongkos Kilometer `(int)`". 
Kita revisi *(Struct Refactor)* desain minggu lalu menjadi:

```go
package main

import (
	"fmt"
	"math"
)

// Menugaskan Edge (Berisi Kota Tujuan & Berapa kilo Jaraknya)
type JalanTol struct {
	KeKota string
	Jarak  int
}

// Representasi Graph
type WeightedGraph struct {
	tetangga map[string][]JalanTol
}

// Inisialisasi Peta Kosong
func BuatPetaBumiBaru() *WeightedGraph {
	return &WeightedGraph{
		tetangga: make(map[string][]JalanTol),
	}
}

func (g *WeightedGraph) SetelRute(asal, tujuan string, hargaToll int) {
	// Undirected/Dua arah (Asal->Tujuan, Tujuan->Asal)
	g.tetangga[asal] = append(g.tetangga[asal], JalanTol{KeKota: tujuan, Jarak: hargaToll})
	g.tetangga[tujuan] = append(g.tetangga[tujuan], JalanTol{KeKota: asal, Jarak: hargaToll})
}
```

## 3. Eksekusi Pencarian Tercepat / Termurah Dijkstra

Disini kita membuat Hash Map untuk dua hal:
1. Papan Skor Sementara `daftarJarakTerpendek` untuk mencatat rekor "Paling Murah".
2. Tanda Selesai `kotaSudahDikunjungi` agar tak perlu dikunjungi ulang.

```go
// Simulasi Algoritma Greedy Dijkstra
func (g *WeightedGraph) DijkstraRun(titikStart string) {
	// 1. Persiapan Papan Skor Jarak Termurah
	daftarJarakTerpendek := make(map[string]int)
	kotaSudahDikunjungi := make(map[string]bool)

	// Inisialisasi: Semua kota harganya "Infinity" Dulu (Sangat Penuh Asumsi)
	for kota := range g.tetangga {
		daftarJarakTerpendek[kota] = math.MaxInt32 // Angka paling maksimum di komputer
	}
	
	// Khusus Kota Start, karena kita sudah diam di sana, jaraknya 0 KM!
	daftarJarakTerpendek[titikStart] = 0

	// 2. Tinjau semua kota perlahan lahan untuk cari yang termurah dijangkau
	for i := 0; i < len(g.tetangga); i++ {
		
		// A. Ambil Kandidat Terdekat dari Antrean yang belum Visited! (Bisa Pakai Min-Queue untuk O(logV))
		kotaTerpilih := ""
		jarakTerendahSesaat := math.MaxInt32

		for kandidatKota, km := range daftarJarakTerpendek {
			// Periksa apakah belum Visited dan Ternyata Jaraknya Rendah
			if !kotaSudahDikunjungi[kandidatKota] && km < jarakTerendahSesaat {
				kotaTerpilih = kandidatKota
				jarakTerendahSesaat = km
			}
		}

		if kotaTerpilih == "" {
			break // Berhenti Jika sudah tidak ada yang bisa diselamatkan
		}

		// Tandai secara permanen Kota Ini! (Lulus dikunjungi)
		kotaSudahDikunjungi[kotaTerpilih] = true

		// B. (Inti Dijkstra) Update Jarak Rekor ke Semua anak cabang/tetangganya
		for _, jalurTollAnak := range g.tetangga[kotaTerpilih] {
			tetangga := jalurTollAnak.KeKota
			ongkos := jalurTollAnak.Jarak

			// Hitungan matematis: Jarak ke Kota Terpilih + Ongkos Kesana (Greedy)
			totalKalkulasiKmYgDitempuh := daftarJarakTerpendek[kotaTerpilih] + ongkos
			
			// Jika ternyata kalkulasi jalanan ini lebih murah dari rekor sebelumnya? UPDATE!
			if totalKalkulasiKmYgDitempuh < daftarJarakTerpendek[tetangga] {
				daftarJarakTerpendek[tetangga] = totalKalkulasiKmYgDitempuh
			}
		}
	}

	// 3. Cetak Fakta Jarak-Jarak Termurahnya
	fmt.Printf("\n--- HASIL GPS TERCEPAT DARI %s ---\n", titikStart)
	for d_kota, kemurahanKm := range daftarJarakTerpendek {
		fmt.Printf("--> Tujuan ke [%s] = Total %d KM\n", d_kota, kemurahanKm)
	}
}
```

### File Main Go Testing
```go
func main() {
	peta := BuatPetaBumiBaru()

	// Pemetaan Aceh
	peta.SetelRute("Banda Aceh", "Sigli", 110)
	peta.SetelRute("Sigli", "Bireuen", 100)
	peta.SetelRute("Bireuen", "Lhokseumawe", 50)
	peta.SetelRute("Banda Aceh", "Meulaboh", 240)
	peta.SetelRute("Bireuen", "Meulaboh", 350) // Jalur Perbukitan Tengah

	// Saya di Banda Aceh, berapa KM paling efisien menuju Lhokseumawe via Dijkstra?
	peta.DijkstraRun("Banda Aceh")
}
```
**Output Sistem akan secara ajaib menganalisis The Best Route**:
Banda Aceh ke Sigli (110) -> Bireuen (100) -> Lhokseumawe (50). Total = 260. *Lebih masuk akal dan termurah ketimbang memaksa lewat bukit Meulaboh*.

---

### **Diskusi Praktek O(N^2)**
Kode di atas menggunakan iterasi `for` standar dua kali untuk mencari kota Termurah dari sisa Map. Kompleksitasnya adalah **O(V^2)** (Vertex Kuadrat). Jika di Dunia Nyata Kota ada 5 Juta, Server akan *Hang*.
Diskusikan dengan tim kelas / Dosen: Bagaimana cara merombak Kode Pencari `kotaTerpilih` pada `titik // A.` di atas menggunakan struktur **Priority Queue** atau **Heap Tree** agar kecepatannya meroket menjadi logaritmik?
