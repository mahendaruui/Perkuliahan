# Minggu 7: Struktur Data Larik (Array 1 Dimensi)

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 4)
- **CPMK Terkait:** CPMK0101 (Konsep Dasar Pemrograman)
- **CPL Terkait:** CPL01 (Pengetahuan Dasar Informatika), CPL04 (Solusi Rekayasa Komputasi)
- **Indikator:** Mahasiswa mampu menjelaskan karakteristik alokasi memori array yang kontigu, mengindeks elemen larik, melakukan operasi traversal, pencarian nilai ekstrem (minimum/maksimum), dan kalkulasi statistik.
:::

---

## 1. Konsep Array & Alokasi Memori Kontigu

**Array (Larik)** adalah struktur data dasar yang menyimpan sekumpulan elemen **bertipe data seragam** (*homogeneous*) di dalam blok memori yang **bersebelahan secara fisik (*contiguous memory allocation*)**.

```mermaid
graph LR
    subgraph Array di RAM (Tipe int: 4 Bytes per elemen)
        A["Indeks [0]<br>Alamat: 0x100<br>Nilai: 85"]
        B["Indeks [1]<br>Alamat: 0x104<br>Nilai: 90"]
        C["Indeks [2]<br>Alamat: 0x108<br>Nilai: 78"]
        D["Indeks [3]<br>Alamat: 0x10C<br>Nilai: 92"]
        E["Indeks [4]<br>Alamat: 0x110<br>Nilai: 88"]
    end
    style A fill:#e0f2fe,stroke:#0284c7
    style B fill:#e0f2fe,stroke:#0284c7
    style C fill:#e0f2fe,stroke:#0284c7
    style D fill:#e0f2fe,stroke:#0284c7
    style E fill:#e0f2fe,stroke:#0284c7
```

Rumus akses alamat memori elemen ke-$i$ (*Direct Access in $O(1)$*):
$$\text{Alamat}(A[i]) = \text{Base Address} + (i \times \text{Ukuran Tipe Data})$$

---

## 2. Operasi-Operasi Fundamental pada Array

1. **Traversal (Penjelajahan):** Mengunjungi setiap elemen dari indeks 0 hingga $N-1$.
2. **Insertion (Penyisipan):** Menambahkan elemen baru ke posisi tertentu.
3. **Deletion (Penghapusan):** Menghapus elemen pada indeks tertentu dan menggeser elemen lainnya.
4. **Search (Pencarian Nilai Min / Max / Rata-Rata):** Memindai seluruh larik untuk mendapatkan parameter statistik.

---

## 3. Studi Kasus: Pengolahan Statistik Nilai Mahasiswa

::: code-group
```cpp [C++]
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int MAX_MHS = 5;
    double nilai[MAX_MHS] = {82.5, 90.0, 68.5, 95.0, 77.5};

    double total = 0.0;
    double nilaiMin = nilai[0];
    double nilaiMax = nilai[0];

    cout << "=== DATA NILAI MAHASISWA ===" << endl;
    for (int i = 0; i < MAX_MHS; i++) {
        cout << "Mahasiswa ke-" << (i + 1) << " : " << nilai[i] << endl;
        total += nilai[i];

        if (nilai[i] < nilaiMin) nilaiMin = nilai[i];
        if (nilai[i] > nilaiMax) nilaiMax = nilai[i];
    }

    double rataRata = total / MAX_MHS;

    cout << fixed << setprecision(2);
    cout << "\n=== STATISTIK KELAS ===" << endl;
    cout << "Total Nilai : " << total << endl;
    cout << "Rata-Rata   : " << rataRata << endl;
    cout << "Nilai Terendah : " << nilaiMin << endl;
    cout << "Nilai Tertinggi: " << nilaiMax << endl;

    return 0;
}
```

```python [Python 3]
nilai = [82.5, 90.0, 68.5, 95.0, 77.5]

print("=== DATA NILAI MAHASISWA ===")
for i, n in enumerate(nilai, 1):
    print(f"Mahasiswa ke-{i} : {n:.2f}")

total = sum(nilai)
rata_rata = total / len(nilai)
nilai_min = min(nilai)
nilai_max = max(nilai)

print("\n=== STATISTIK KELAS ===")
print(f"Total Nilai : {total:.2f}")
print(f"Rata-Rata   : {rata_rata:.2f}")
print(f"Nilai Terendah : {nilai_min:.2f}")
print(f"Nilai Tertinggi: {nilai_max:.2f}")
```
:::

---

## 📝 Evaluasi & Latihan Mandiri (Sub-CPMK 4)

1. Tuliskan program untuk membalik urutan elemen dalam array (*reverse array*) tanpa membuat array baru (menggunakan teknik pertukaran dua pointer).
2. Buatlah program untuk menghitung frekuensi kemunculan setiap angka dalam sebuah array yang berisi 10 bilangan bulat.
