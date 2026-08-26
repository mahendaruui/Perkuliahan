# Bank Soal & Quiz UAS Struktur Data (Golang)

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 1 - 7)
- **CPMK Terkait:** CPMK0101 (Konsep Struktur Data), CPMK0106 (Analisis Kompleksitas)
- **CPL Terkait:** CPL01 (Pengetahuan Teori), CPL08 (Etika & Sikap Profesional)
- **Indikator:** Evaluasi komprehensif kemampuan mahasiswa dalam menelaah konsep memori, pointer, ADT linear, tree, graph, serta trace kode Golang.
:::

---

## 📝 Soal Pilihan Ganda & Analisis Algoritma (1 - 10)

### 1. Model Memori Golang
Di bahasa pemrograman Golang, perbedaan mendasar antara **Array** dan **Slice** adalah:
- A. Array memiliki ukuran dinamis di Heap, sedangkan Slice statis di Stack.
- B. Array berukuran tetap (*fixed-size*) yang menjadi bagian dari tipe datanya, sedangkan Slice adalah header struct 24 bytes yang mereferensikan underlying array secara dinamis. ✅
- C. Array dialokasikan menggunakan `make()`, sedangkan Slice dideklarasikan dengan `var a [5]int`.
- D. Array diteruskan ke fungsi sebagai referensi pointer, sedangkan Slice disalin seluruh datanya.

---

### 2. Semantik Pointer
Perhatikan potongan kode Golang berikut:
```go
func modify(ptr *int) {
    *ptr = *ptr * 2
}
func main() {
    a := 15
    modify(&a)
    fmt.Println(a)
}
```
Luaran yang dicetak di terminal adalah:
- A. `15`
- B. `0`
- C. `30` ✅
- D. Alamat memori `0xc000014080`

---

### 3. Operasi Stack LIFO
Diberikan urutan operasi pada sebuah stack kosong:  
`Push(5)`, `Push(8)`, `Pop()`, `Push(12)`, `Push(4)`, `Pop()`, `Peek()`.  
Nilai yang dikembalikan oleh operasi `Peek()` terakhir adalah:
- A. `5`
- B. `8`
- C. `12` ✅
- D. `4`

---

### 4. Circular Queue
Pada sebuah Circular Queue dengan kapasitas $K = 6$, posisi `Front = 4` dan `Rear = 5`. Jika dilakukan satu kali operasi `Enqueue()`, maka posisi `Rear` berikutnya adalah:
- A. `6`
- B. `0` (karena $(5 + 1) \% 6 = 0$) ✅
- C. `1`
- D. Terjadi *Queue Overflow*

---

### 5. Linked List vs Slice Prepend
Mengapa operasi penyisipan elemen di awal (*Prepend*) pada Singly Linked List berkinerja $O(1)$, sedangkan pada Slice dinamis berkinerja $O(n)$?
- A. Karena Linked List tidak perlu menggeser elemen memori yang sudah ada, melainkan cukup menghubungkan pointer `newNode.Next = head`. ✅
- B. Karena Linked List disimpan di cache CPU register.
- C. Karena Slice selalu menggandakan kapasitasnya setiap kali ada elemen baru.
- D. Karena Linked List memiliki ukuran tetap.

---

### 6. Binary Search Tree (BST)
Penelusuran (*Traversal*) manakah pada sebuah Binary Search Tree yang **selalu menghasilkan data dalam urutan terurut naik (*sorted ascending*)**?
- A. Pre-Order Traversal (DLR)
- B. In-Order Traversal (LDR) ✅
- C. Post-Order Traversal (LRD)
- D. Level-Order Traversal (BFS)

---

### 7. Kompleksitas Algoritma Searching
Berapakah jumlah perbandingan maksimum yang dibutuhkan oleh algoritma **Binary Search** untuk mencari angka pada array terurut dengan $1.048.576$ elemen ($2^{20}$)?
- A. $1.048.576$ kali
- B. $1.000$ kali
- C. $20$ kali (karena $\log_2(2^{20}) = 20$) ✅
- D. $2$ kali

---

### 8. Hash Collision
Teknik penanganan tabrakan hash di mana setiap bucket menampung sebuah linked list dinamis disebut:
- A. Linear Probing
- B. Double Hashing
- C. Separate Chaining ✅
- D. Quadratic Probing

---

### 9. Algoritma Graf Dijkstra
Algoritma Dijkstra digunakan untuk mencari rute terpendek dengan syarat utama:
- A. Graf tidak boleh memiliki siklus (*must be DAG*).
- B. Graf tidak boleh memiliki bobot sisi yang bernilai negatif. ✅
- C. Graf harus berukuran kurang dari 100 simpul.
- D. Semua simpul harus memiliki derajat yang sama.

---

### 10. LRU Cache
Struktur data gabungan yang paling efisien untuk membangun sistem **LRU Cache** dengan operasi `Get` dan `Put` dalam waktu $O(1)$ adalah:
- A. Array + Binary Tree
- B. Hash Map + Doubly Linked List ✅
- C. Stack + Circular Queue
- D. Binary Search Tree + Min-Heap
