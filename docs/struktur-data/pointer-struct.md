# Minggu 2 — Array, Slice, Struct & Pointer

Di pertemuan kedua ini, Anda akan mempelajari fondasi Golang yang esensial dalam membuat tipe data bentukan sendiri (ADT). Kemampuan Anda membuat "wadah" untuk tipe data ini adalah bekal mutlak sebelum merakit struktur logik seperti Stack maupun Linked List.

## 1. Array vs Slice
Bahasa Go sangat tegas dalam mengatur kapasitas memori sejak awal.

### **Array**
- Bersifat **statis** (ukurannya harus ditentukan saat deklarasi dan tidak bisa diubah).
- Dikompilasi dan ditetapkan secara pasti ke dalam *Memory Stack*.

```go
func main() {
    var numbers [5]int // Hanya bisa menampung 5 elemen (indeks 0 - 4)
    numbers[0] = 10    // Assign nilai
    fmt.Println(numbers) // [10 0 0 0 0] default value tipe int adalah 0
}
```

### **Slice**
- Bersifat **dinamis** seolah Array tak berujung layaknya list biasa di bahasa tingkat tinggi (PHP/JS).
- Memanfaatkan fungsi bawaan `append` yang bekerja secara otomatis. 
- Struktur internal slice secara abstrak memiliki tiga aspek: `Pointer ke underlying array`, `length` (jumlah saat ini), dan `capacity` (maksimal). Jika batas array tersentuh, Go otomatis menggandakan batasnya.

```go
func main() {
    // Membuat sebuah slice menggunakan make
    var antrian = make([]string, 0, 5) // panjang = 0, tetapi memori yang direservasi = 5
    
    antrian = append(antrian, "Andi")
    antrian = append(antrian, "Budi")
    fmt.Printf("Len: %d, Cap: %d, Value: %v\n", len(antrian), cap(antrian), antrian)
}
```

## 2. Pointers (Referensi Memori)
Golang secara fundamental bersifat **Pass-By-Value** dalam fungsi. 
Artinya, ketika Anda mengirimkan lemparan variabel ke sebuah fungsi (misal data berkapasitas 2 Megabyte), maka Go *menduplikasi/meng-copy* data tersebut. 

Apa yang terjadi kalau Anda ingin mengubah langsung nilai aslinya, atau mengurangi komputasi memori? Muncullah **Pointer**.
- Pointer merupakan operator untuk mendapatkan *alamat ruang memori hexadesimal* dari variabel.
- Gunakan ampersand `&` untuk menjadikan nilainya menjadi memori *Address*.
- Gunakan asterisk `*` untuk mengurai kembali memori ke *Value*.

**Contoh Kasus Pass by Reference:**
```go
package main

import "fmt"

func updateNilaiStatis(val int) {
    val = 100 // Ini tidak akan berguna untuk program utama
}

func updateDenganAksebilitasPointer(val *int) {
    *val = 100 // Akses ke rumah aslinya dan ganti isinya dengan 100
}

func main() {
    var angka int = 10
    
    updateNilaiStatis(angka)
    fmt.Println("Gagal diganti:", angka) // Akan tetap mencetak 10

    // Kini lempar alamat memorinya saja
    updateDenganAksebilitasPointer(&angka)
    fmt.Println("Sukses diganti:", angka) // Akan mencirikan 100
}
```

## 3. Abstract Data Type dengan `Struct`
Karena program kita tidak hanya mengorganisir sederet angka saja, tetapi data riil seperti *User*, *Siswa*, *Kendaraan*, *Edge*, *Node*. Go menggunakan `struct` untuk membuat object-oriented design yang fleksibel karena *class* tidak ada pada bahasa Go.

### **Pembuatan User Data Type**
Grup data dari beberapa var.
```go
// Definisi Struct User
type Mahasiswa struct {
    NIM  string
    Nama string
    IPK  float64
}

func main() {
    // Instalasi Konstruktor
    mhs1 := Mahasiswa{
        NIM:  "12345",
        Nama: "Siti Rahma",
        IPK:  3.89,
    }
    fmt.Println("Data Nama Mhs:", mhs1.Nama)
}
```

## 4. Method (Fungsi Receiver)
Go menyediakan Receiver untuk menempelkan perilaku *(behavior)* ke *Struct*. Inilah yang dinamakan Getter dan Setter. Perhatikan bahwa Anda HARUS menempelkan tipe Pointer pada Struct jika ingin mengubah isinya *(Setter)*.

```go
// ... dari struct Mahasiswa yang dibuat di atas

// Getter: Ambil data (Terdapat receiver (m Mahasiswa))
func (m Mahasiswa) GetGelar() string {
    return m.Nama + ", S.Kom."
}

// Setter: Update data (Terdapat receiver (m *Mahasiswa) <--- Tambah Bintang/*)
func (m *Mahasiswa) UpdateIPK(ipkBaru float64) {
    m.IPK = ipkBaru // Mutator
}

func main() {
    m1 := Mahasiswa{Nama: "Budi", IPK: 3.0}
    
    // Pemanggilan Method seperti Class pada OOP Standard
    m1.UpdateIPK(3.99)
    fmt.Println(m1.GetGelar())
    fmt.Println("IPK Update:", m1.IPK)
}
```

Inilah bekal dasar yang akan banyak dipakai untuk membuat Stack, Linked List dan Tree ke depannya.

---
### **Praktikum Kelas**
Gunakan waktu di sesi Laboratorium komputer untuk:
1. Membuat `struct` bertipe **Buku** dengan atribut Title, Stock, Author.
2. Definisikan receiver setter bernama `function Meminjam()` yang akan mengurangi *Stock* sebanyak `1`.
3. Demonstrasikan *Print Line* sebelum dan sesudah metode `Meminjam()` dijalankan. Cek dengan teliti apabila stok gagal berkurang (masalah Pointer vs Nilai).
