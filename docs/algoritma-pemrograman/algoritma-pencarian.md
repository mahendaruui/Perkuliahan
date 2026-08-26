# Minggu 12: Algoritma Pencarian (Searching Algorithm)

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 6)
- **CPMK Terkait:** CPMK0106 (Konsep Matematika Informatika & Logika Algoritma)
- **CPL Terkait:** CPL01 (Pengetahuan Dasar), CPL03 (Problem Solving)
- **Indikator:** Mahasiswa mampu menganalisis mekanisme kerja algoritma Linear Search dan Binary Search, memahami syarat prasyarat keterurutan data, serta mengevaluasi perbandingan efisiensi kompleksitas waktu komputasi $O(n)$ versus $O(\log n)$.
:::

---

## 1. Konsep Dasar Pencarian Data

Pencarian (*Searching*) adalah proses menemukan lokasi atau posisi indeks suatu elemen data tertentu (*target key*) di dalam sekumpulan data (*dataset*).

```mermaid
graph TD
    Search[Algoritma Pencarian] --> LS[Linear Search / Sequential Search<br>Kompleksitas: O(n)<br>Syarat: Data Tidak Perlu Terurut]
    Search --> BS[Binary Search / Bagi Dua<br>Kompleksitas: O(log n)<br>Syarat Mutlak: Data Harus Terurut]
    style LS fill:#fef3c7,stroke:#d97706
    style BS fill:#dcfce7,stroke:#16a34a
```

---

## 2. Linear Search vs Binary Search

| Dimensi Analisis | Linear Search (Sekuensial) | Binary Search (Bagi Dua) |
| :--- | :--- | :--- |
| **Prasyarat Dataset** | Data boleh **acak / tidak terurut**. | Data **wajib terurut (*sorted*)**. |
| **Prinsip Kerja** | Membandingkan target dengan elemen satu per satu dari awal hingga akhir. | Membagi ruang pencarian menjadi 2 bagian secara berulang (*Divide and Conquer*). |
| **Worst-Case Complexity** | $O(n)$ (Jika data di ujung atau tidak ditemukan). | $O(\log_2 n)$ (Sangat cepat pada dataset besar). |
| **Contoh 1 Juta Data** | Butuh hingga $1.000.000$ operasi perbandingan. | Hanya butuh maksimal $\approx 20$ kali perbandingan! |

---

## 3. Implementasi Linear & Binary Search

::: code-group
```cpp [C++]
#include <iostream>
using namespace std;

// 1. Linear Search
int linearSearch(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) return i; // Ditemukan di indeks i
    }
    return -1; // Tidak ditemukan
}

// 2. Binary Search (Prasyarat: arr harus terurut)
int binarySearch(int arr[], int size, int key) {
    int kiri = 0;
    int kanan = size - 1;

    while (kiri <= kanan) {
        int tengah = kiri + (kanan - kiri) / 2;

        if (arr[tengah] == key) {
            return tengah;
        }
        if (arr[tengah] < key) {
            kiri = tengah + 1; // Cari di belahan kanan
        } else {
            kanan = tengah - 1; // Cari di belahan kiri
        }
    }
    return -1;
}

int main() {
    int dataTerurut[] = {12, 24, 35, 47, 58, 69, 73, 85, 96};
    int n = sizeof(dataTerurut) / sizeof(dataTerurut[0]);
    int cari = 73;

    int pos = binarySearch(dataTerurut, n, cari);
    if (pos != -1) {
        cout << "Data " << cari << " DITEMUKAN pada indeks: " << pos << endl;
    } else {
        cout << "Data " << cari << " TIDAK DITEMUKAN." << endl;
    }
    return 0;
}
```

```python [Python 3]
def binary_search(arr: list, target: int) -> int:
    kiri, kanan = 0, len(arr) - 1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
            
    return -1

data = [12, 24, 35, 47, 58, 69, 73, 85, 96]
target = 73
hasil = binary_search(data, target)

if hasil != -1:
    print(f"Data {target} DITEMUKAN pada indeks: {hasil}")
else:
    print(f"Data {target} TIDAK DITEMUKAN.")
```
:::

---

## 📝 Evaluasi & Latihan Mandiri (Sub-CPMK 6)

1. Jika terdapat array dengan $2.000.000$ elemen terurut, berapa jumlah perbandingan maksimum yang dilakukan Binary Search untuk memastikan sebuah angka tidak ada dalam array?
2. Modifikasi algoritma Binary Search agar dapat mengembalikan indeks pertama kemunculan data jika terdapat elemen duplikat!
