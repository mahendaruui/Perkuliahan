# Algoritma Pencarian

## Pengenalan

**Algoritma pencarian** adalah algoritma untuk menemukan elemen tertentu dalam kumpulan data. Pencarian adalah operasi fundamental dalam pemrograman yang digunakan dalam berbagai aplikasi.

### Jenis-Jenis Pencarian

1. **Linear Search** (Sequential Search)
2. **Binary Search** (Pencarian Biner)
3. **Jump Search**
4. **Interpolation Search**

## 1. Linear Search (Pencarian Linier)

### Konsep

Mencari elemen dengan memeriksa setiap elemen array satu per satu dari awal hingga akhir.

### Flowchart Linear Search

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: array, nilai_cari/]
    Input --> Init[i = 0]
    Init --> Cek{i < panjang array?}
    Cek -->|Ya| Compare{array[i] == nilai_cari?}
    Compare -->|Ya| Found[/Output: Ditemukan<br/>di index i/]
    Compare -->|Tidak| Inc[i = i + 1]
    Inc --> Cek
    Cek -->|Tidak| NotFound[/Output:<br/>Tidak ditemukan/]
    Found --> Stop([Selesai])
    NotFound --> Stop
```

### Implementasi

```python
# Python
def linear_search(arr, x):
    """
    Linear Search
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Ditemukan, return index
    return -1  # Tidak ditemukan

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
nilai_cari = 22

hasil = linear_search(data, nilai_cari)

if hasil != -1:
    print(f"Nilai {nilai_cari} ditemukan di index {hasil}")
else:
    print(f"Nilai {nilai_cari} tidak ditemukan")
```

```cpp
// C++
#include <iostream>
using namespace std;

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i;  // Ditemukan
        }
    }
    return -1;  // Tidak ditemukan
}

int main() {
    int data[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(data) / sizeof(data[0]);
    int nilai_cari = 22;

    int hasil = linearSearch(data, n, nilai_cari);

    if (hasil != -1) {
        cout << "Nilai " << nilai_cari << " ditemukan di index " << hasil << endl;
    } else {
        cout << "Nilai " << nilai_cari << " tidak ditemukan" << endl;
    }

    return 0;
}
```

### Karakteristik Linear Search

- ✅ **Kelebihan**:
  - Sederhana dan mudah diimplementasikan
  - Bekerja pada data yang tidak terurut
  - Cocok untuk dataset kecil
- ❌ **Kekurangan**:
  - Lambat untuk dataset besar
  - Time Complexity: O(n)

## 2. Binary Search (Pencarian Biner)

### Konsep

Mencari elemen dengan membagi array menjadi dua bagian secara berulang. **Syarat: Array harus sudah terurut.**

### Flowchart Binary Search

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: array terurut,<br/>nilai_cari/]
    Input --> Init[low = 0<br/>high = panjang - 1]
    Init --> Cek{low <= high?}
    Cek -->|Ya| CalcMid[mid = low + high / 2]
    CalcMid --> CompMid{array[mid] == nilai_cari?}
    CompMid -->|Ya| Found[/Output: Ditemukan<br/>di index mid/]
    CompMid -->|Tidak| CompLess{array[mid] < nilai_cari?}
    CompLess -->|Ya| UpdateLow[low = mid + 1]
    CompLess -->|Tidak| UpdateHigh[high = mid - 1]
    UpdateLow --> Cek
    UpdateHigh --> Cek
    Cek -->|Tidak| NotFound[/Output:<br/>Tidak ditemukan/]
    Found --> Stop([Selesai])
    NotFound --> Stop
```

### Visualisasi Binary Search

Mencari nilai 31 dalam array [3, 7, 12, 15, 19, 24, 31, 45, 67, 89]:

```
Iterasi 1: [3, 7, 12, 15, 19, 24, 31, 45, 67, 89]
                            ^
                           mid=19 (< 31) → cari di kanan

Iterasi 2: [24, 31, 45, 67, 89]
                ^
               mid=45 (> 31) → cari di kiri

Iterasi 3: [24, 31]
                ^
               mid=31 (== 31) → DITEMUKAN!
```

### Implementasi Iteratif

```python
# Python
def binary_search(arr, x):
    """
    Binary Search (Iteratif)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Cek apakah x ada di tengah
        if arr[mid] == x:
            return mid
        # Jika x lebih besar, abaikan setengah kiri
        elif arr[mid] < x:
            low = mid + 1
        # Jika x lebih kecil, abaikan setengah kanan
        else:
            high = mid - 1

    return -1  # Tidak ditemukan

# Contoh
data = [3, 7, 12, 15, 19, 24, 31, 45, 67, 89]
nilai_cari = 31

hasil = binary_search(data, nilai_cari)

if hasil != -1:
    print(f"Nilai {nilai_cari} ditemukan di index {hasil}")
else:
    print(f"Nilai {nilai_cari} tidak ditemukan")
```

### Implementasi Rekursif

```cpp
// C++
#include <iostream>
using namespace std;

int binarySearchRecursive(int arr[], int low, int high, int x) {
    if (low > high) {
        return -1;  // Tidak ditemukan
    }

    int mid = low + (high - low) / 2;

    if (arr[mid] == x) {
        return mid;  // Ditemukan
    } else if (arr[mid] < x) {
        return binarySearchRecursive(arr, mid + 1, high, x);
    } else {
        return binarySearchRecursive(arr, low, mid - 1, x);
    }
}

int main() {
    int data[] = {3, 7, 12, 15, 19, 24, 31, 45, 67, 89};
    int n = sizeof(data) / sizeof(data[0]);
    int nilai_cari = 31;

    int hasil = binarySearchRecursive(data, 0, n - 1, nilai_cari);

    if (hasil != -1) {
        cout << "Nilai " << nilai_cari << " ditemukan di index " << hasil << endl;
    } else {
        cout << "Nilai " << nilai_cari << " tidak ditemukan" << endl;
    }

    return 0;
}
```

### Karakteristik Binary Search

- ✅ **Kelebihan**:
  - Sangat cepat: O(log n)
  - Efisien untuk dataset besar
- ❌ **Kekurangan**:
  - Hanya bekerja pada data terurut
  - Lebih kompleks dari linear search

## 3. Jump Search

### Konsep

Melompati beberapa elemen (block jumping) kemudian melakukan linear search dalam block.

### Flowchart Jump Search

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: array terurut,<br/>nilai_cari/]
    Input --> Init[step = √n<br/>prev = 0]
    Init --> Jump{prev < n DAN<br/>arr[min prev + step, n] < nilai_cari?}
    Jump -->|Ya| UpdatePrev[prev = prev + step]
    UpdatePrev --> Jump
    Jump -->|Tidak| Linear[Linear search<br/>dari prev hingga<br/>min prev + step, n]
    Linear --> Check{Ditemukan?}
    Check -->|Ya| Found[/Output: index/]
    Check -->|Tidak| NotFound[/Output: -1/]
    Found --> Stop([Selesai])
    NotFound --> Stop
```

### Implementasi

```python
# Python
import math

def jump_search(arr, x):
    """
    Jump Search
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jumping blocks
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search dalam block
    while prev < n and arr[prev] < x:
        prev += 1

    # Cek apakah ditemukan
    if prev < n and arr[prev] == x:
        return prev

    return -1

# Contoh
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nilai_cari = 11

hasil = jump_search(data, nilai_cari)

if hasil != -1:
    print(f"Nilai {nilai_cari} ditemukan di index {hasil}")
else:
    print(f"Nilai {nilai_cari} tidak ditemukan")
```

## Perbandingan Algoritma Pencarian

| Algoritma                | Time Complexity                  | Space Complexity                    | Syarat               | Best Use Case                     |
| ------------------------ | -------------------------------- | ----------------------------------- | -------------------- | --------------------------------- |
| **Linear Search**        | O(n)                             | O(1)                                | Tidak ada            | Dataset kecil, data tidak terurut |
| **Binary Search**        | O(log n)                         | O(1) iteratif<br/>O(log n) rekursif | Data terurut         | Dataset besar terurut             |
| **Jump Search**          | O(√n)                            | O(1)                                | Data terurut         | Dataset sedang terurut            |
| **Interpolation Search** | O(log log n) best<br/>O(n) worst | O(1)                                | Data terurut uniform | Data terdistribusi merata         |

## Program Lengkap: Perbandingan Algoritma

```python
# Python
import time
import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def test_algoritma():
    # Generate data
    n = 100000
    data = sorted([random.randint(1, 1000000) for _ in range(n)])
    nilai_cari = data[random.randint(0, n-1)]  # Ambil nilai yang pasti ada

    print(f"Dataset size: {n}")
    print(f"Mencari nilai: {nilai_cari}\n")

    # Test Linear Search
    start = time.time()
    hasil = linear_search(data, nilai_cari)
    waktu_linear = time.time() - start
    print(f"Linear Search:")
    print(f"  - Hasil: Index {hasil}")
    print(f"  - Waktu: {waktu_linear:.6f} detik")

    # Test Binary Search
    start = time.time()
    hasil = binary_search(data, nilai_cari)
    waktu_binary = time.time() - start
    print(f"\nBinary Search:")
    print(f"  - Hasil: Index {hasil}")
    print(f"  - Waktu: {waktu_binary:.6f} detik")

    # Perbandingan
    print(f"\nBinary Search {waktu_linear/waktu_binary:.2f}x lebih cepat")

test_algoritma()
```

## Latihan

1. **Modified Binary Search**

   - Cari elemen pertama yang >= x
   - Cari elemen terakhir yang <= x

2. **Count Occurrences**

   - Hitung berapa kali nilai x muncul dalam array terurut
   - Gunakan binary search

3. **Find Peak Element**

   - Cari elemen yang lebih besar dari tetangganya
   - Contoh: [1, 3, 20, 4, 1] → 20 adalah peak

4. **Search in Rotated Array**

   - Cari elemen dalam array terurut yang dirotasi
   - Contoh: [4, 5, 6, 7, 0, 1, 2], cari 0

5. **Find Missing Number**

   - Array berisi 1 hingga n dengan satu angka hilang
   - Cari angka yang hilang

6. **Closest Number**
   - Cari nilai yang paling dekat dengan x
   - Dalam array terurut

## Rangkuman

- **Linear Search**: Sederhana, O(n), untuk data tidak terurut
- **Binary Search**: Efisien, O(log n), untuk data terurut
- **Jump Search**: Kompromi, O(√n), untuk data terurut
- Pilih algoritma sesuai karakteristik data dan kebutuhan
- Binary Search paling efisien untuk dataset besar terurut
- Gunakan built-in functions jika tersedia (bisect di Python)

---

**Sebelumnya**: [Rekursi](./rekursi.md) | **Selanjutnya**: [Algoritma Pengurutan](./algoritma-pengurutan.md)
