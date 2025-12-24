# Array

## Apa itu Array?

**Array** adalah struktur data yang menyimpan kumpulan elemen dengan tipe data yang sama dalam satu variabel. Setiap elemen dapat diakses menggunakan indeks.

### Karakteristik Array

- Ukuran tetap (fixed size)
- Tipe data homogen (sama semua)
- Akses elemen menggunakan indeks (dimulai dari 0)
- Lokasi memori yang berurutan

### Ilustrasi Array

```
Index:  0    1    2    3    4
       ┌────┬────┬────┬────┬────┐
Array: │ 10 │ 20 │ 30 │ 40 │ 50 │
       └────┴────┴────┴────┴────┘
```

## Deklarasi dan Inisialisasi Array

### Python (List)

```python
# Deklarasi array kosong
angka = []

# Deklarasi dengan nilai awal
angka = [10, 20, 30, 40, 50]

# Array dengan ukuran tertentu (diisi 0)
angka = [0] * 5  # [0, 0, 0, 0, 0]

# Array multidimensi (2D)
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### C++

```cpp
// Deklarasi array dengan ukuran
int angka[5];

// Deklarasi dengan nilai awal
int angka[] = {10, 20, 30, 40, 50};
int angka[5] = {10, 20, 30, 40, 50};

// Array multidimensi (2D)
int matriks[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
```

## Operasi Dasar Array

### 1. Mengakses Elemen

```python
# Python
angka = [10, 20, 30, 40, 50]

# Akses elemen
print(angka[0])   # 10 (elemen pertama)
print(angka[2])   # 30 (elemen ketiga)
print(angka[-1])  # 50 (elemen terakhir)
```

```cpp
// C++
int angka[] = {10, 20, 30, 40, 50};

cout << angka[0] << endl;  // 10
cout << angka[2] << endl;  // 30
cout << angka[4] << endl;  // 50
```

### 2. Mengubah Elemen

```python
# Python
angka = [10, 20, 30, 40, 50]
angka[2] = 35  # Ubah elemen indeks 2
print(angka)   # [10, 20, 35, 40, 50]
```

```cpp
// C++
int angka[] = {10, 20, 30, 40, 50};
angka[2] = 35;
cout << angka[2] << endl;  // 35
```

### 3. Menambah Elemen (Python)

```python
# Python - list dinamis
angka = [10, 20, 30]

# Tambah di akhir
angka.append(40)  # [10, 20, 30, 40]

# Tambah di posisi tertentu
angka.insert(1, 15)  # [10, 15, 20, 30, 40]

# Gabung list
angka.extend([50, 60])  # [10, 15, 20, 30, 40, 50, 60]
```

### 4. Menghapus Elemen (Python)

```python
# Python
angka = [10, 20, 30, 40, 50]

# Hapus berdasarkan nilai
angka.remove(30)  # [10, 20, 40, 50]

# Hapus berdasarkan indeks
del angka[1]  # [10, 40, 50]

# Pop (hapus dan return nilai)
nilai = angka.pop()  # nilai = 50, angka = [10, 40]
```

## Flowchart: Operasi Array

### Flowchart Mencari Nilai dalam Array

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: array, nilai_cari/]
    Input --> Init[ketemu = False<br/>i = 0]
    Init --> Cek{i < panjang array?}
    Cek -->|Ya| Compare{array[i] == nilai_cari?}
    Compare -->|Ya| Found[ketemu = True<br/>index = i]
    Found --> End1[/Output: Ditemukan di index/]
    Compare -->|Tidak| Inc[i = i + 1]
    Inc --> Cek
    Cek -->|Tidak| Check{ketemu?}
    Check -->|Ya| End1
    Check -->|Tidak| End2[/Output: Tidak ditemukan/]
    End1 --> Stop([Selesai])
    End2 --> Stop
```

### Flowchart Menjumlahkan Elemen Array

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: array/]
    Input --> Init[total = 0<br/>i = 0]
    Init --> Cek{i < panjang array?}
    Cek -->|Ya| Add[total = total + array[i]]
    Add --> Inc[i = i + 1]
    Inc --> Cek
    Cek -->|Tidak| Output[/Output: total/]
    Output --> Stop([Selesai])
```

## Contoh Program Lengkap

### Program 1: Input dan Tampilkan Array

```python
# Python
def input_array():
    n = int(input("Masukkan jumlah elemen: "))
    array = []

    print("Masukkan elemen array:")
    for i in range(n):
        nilai = int(input(f"Elemen ke-{i+1}: "))
        array.append(nilai)

    return array

def tampilkan_array(array):
    print("\nIsi array:")
    for i in range(len(array)):
        print(f"Index {i}: {array[i]}")

# Main program
angka = input_array()
tampilkan_array(angka)

# Statistik
print(f"\nJumlah elemen: {len(angka)}")
print(f"Nilai terkecil: {min(angka)}")
print(f"Nilai terbesar: {max(angka)}")
print(f"Jumlah total: {sum(angka)}")
print(f"Rata-rata: {sum(angka)/len(angka):.2f}")
```

### Program 2: Mencari Nilai dalam Array

```cpp
// C++
#include <iostream>
using namespace std;

int main() {
    int n, nilai_cari, index = -1;

    cout << "Masukkan jumlah elemen: ";
    cin >> n;

    int array[n];

    cout << "Masukkan elemen array:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Elemen ke-" << (i+1) << ": ";
        cin >> array[i];
    }

    cout << "\nMasukkan nilai yang dicari: ";
    cin >> nilai_cari;

    // Pencarian
    for (int i = 0; i < n; i++) {
        if (array[i] == nilai_cari) {
            index = i;
            break;
        }
    }

    // Output
    if (index != -1) {
        cout << "Nilai " << nilai_cari << " ditemukan di index " << index << endl;
    } else {
        cout << "Nilai " << nilai_cari << " tidak ditemukan" << endl;
    }

    return 0;
}
```

### Program 3: Membalik Array

```python
# Python
def balik_array(array):
    n = len(array)
    for i in range(n // 2):
        # Tukar elemen
        temp = array[i]
        array[i] = array[n - 1 - i]
        array[n - 1 - i] = temp
    return array

# Contoh penggunaan
angka = [10, 20, 30, 40, 50]
print("Array awal:", angka)

angka = balik_array(angka)
print("Array setelah dibalik:", angka)

# Atau menggunakan slicing Python
angka_rev = angka[::-1]
print("Menggunakan slicing:", angka_rev)
```

### Program 4: Mencari Nilai Maksimum dan Minimum

```cpp
// C++
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Masukkan jumlah elemen: ";
    cin >> n;

    int array[n];

    cout << "Masukkan elemen array:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Elemen ke-" << (i+1) << ": ";
        cin >> array[i];
    }

    // Inisialisasi min dan max dengan elemen pertama
    int min = array[0];
    int max = array[0];

    // Cari min dan max
    for (int i = 1; i < n; i++) {
        if (array[i] < min) {
            min = array[i];
        }
        if (array[i] > max) {
            max = array[i];
        }
    }

    cout << "\nNilai minimum: " << min << endl;
    cout << "Nilai maksimum: " << max << endl;

    return 0;
}
```

## Array Multidimensi (2D)

### Deklarasi dan Akses

```python
# Python - Array 2D (Matrix)
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Akses elemen
print(matriks[0][0])  # 1 (baris 0, kolom 0)
print(matriks[1][2])  # 6 (baris 1, kolom 2)

# Iterasi
for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        print(matriks[i][j], end=" ")
    print()
```

```cpp
// C++ - Array 2D
int matriks[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Akses elemen
cout << matriks[0][0] << endl;  // 1
cout << matriks[1][2] << endl;  // 6

// Iterasi
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        cout << matriks[i][j] << " ";
    }
    cout << endl;
}
```

### Program: Penjumlahan Matriks

```python
# Python
def jumlah_matriks(A, B):
    baris = len(A)
    kolom = len(A[0])

    C = [[0 for j in range(kolom)] for i in range(baris)]

    for i in range(baris):
        for j in range(kolom):
            C[i][j] = A[i][j] + B[i][j]

    return C

def cetak_matriks(matriks):
    for baris in matriks:
        for elemen in baris:
            print(f"{elemen:3}", end=" ")
        print()

# Contoh
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

print("Matriks A:")
cetak_matriks(A)

print("\nMatriks B:")
cetak_matriks(B)

C = jumlah_matriks(A, B)
print("\nMatriks C (A + B):")
cetak_matriks(C)
```

## Metode Array di Python

```python
# List methods
angka = [10, 30, 20, 40, 50]

# append() - tambah di akhir
angka.append(60)

# insert() - tambah di posisi tertentu
angka.insert(1, 15)

# remove() - hapus nilai tertentu
angka.remove(30)

# pop() - hapus dan return
nilai = angka.pop()

# index() - cari index nilai
idx = angka.index(20)

# count() - hitung kemunculan
jumlah = angka.count(10)

# sort() - urutkan
angka.sort()

# reverse() - balik
angka.reverse()

# clear() - hapus semua
angka.clear()
```

## Latihan

1. **Program Statistik Array**

   - Input array dari user
   - Hitung: min, max, rata-rata, median

2. **Program Duplikat**

   - Cari dan tampilkan elemen yang duplikat dalam array

3. **Program Merge Array**

   - Gabungkan dua array terurut menjadi satu array terurut

4. **Program Rotasi Array**

   - Rotasi array ke kanan sebanyak n posisi
   - Contoh: [1,2,3,4,5] rotasi 2 → [4,5,1,2,3]

5. **Program Transpose Matriks**

   - Input matriks m×n
   - Output transpose (n×m)

6. **Program Diagonal Matriks**
   - Tampilkan elemen diagonal utama dan diagonal sekunder

## Rangkuman

- **Array** adalah struktur data untuk menyimpan kumpulan elemen dengan tipe sama
- **Indeks** dimulai dari 0
- **Array Python** (list) bersifat dinamis, bisa bertambah/berkurang
- **Array C++** bersifat statis, ukuran tetap
- **Array 2D** untuk representasi matriks/tabel
- Operasi umum: akses, ubah, tambah, hapus, cari

---

**Sebelumnya**: [Perulangan](./perulangan.md) | **Selanjutnya**: [String](./string.md)
