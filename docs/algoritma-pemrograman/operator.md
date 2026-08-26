# Minggu 3: Operator dan Ekspresi Logika

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 2)
- **CPMK Terkait:** CPMK0101 (Konsep Dasar Pemrograman)
- **CPL Terkait:** CPL01 (Pengetahuan Dasar Informatika), CPL04 (Solusi Komputasi)
- **Indikator:** Mahasiswa mampu menganalisis hierarki presedensi operator, menyusun ekspresi aritmatika dan logika majemuk menggunakan tabel kebenaran, serta mengimplementasikan operator bitwise dan assignment.
:::

---

## 1. Klasifikasi Operator Pemrograman

**Operator** adalah simbol khusus yang menginstruksikan kompilator/interpreter untuk melakukan operasi matematis, relasional, atau manipulasi logika tertentu terhadap satu atau lebih operan (*operand*).

```mermaid
graph TD
    OP[Operator Pemrograman] --> ARIT[Aritmatika (+, -, *, /, %)]
    OP --> REL[Relasional (==, !=, <, >, <=, >=)]
    OP --> LOG[Logika Boolean (AND, OR, NOT)]
    OP --> ASS[Penugasan / Assignment (=, +=, -=, dll)]
    OP --> BIT[Bitwise (&, |, ^, ~, <<, >>)]
    style OP fill:#f1f5f9,stroke:#475569
    style ARIT fill:#e0f2fe,stroke:#0284c7
    style REL fill:#fef3c7,stroke:#d97706
    style LOG fill:#dcfce7,stroke:#16a34a
```

---

## 2. Operator Aritmatika & Pembagian Bulat vs Riil

| Operator | Operasi | Contoh Ekspresi | Hasil ($a=17, b=5$) |
| :---: | :--- | :---: | :---: |
| `+` | Penjumlahan | `a + b` | `22` |
| `-` | Pengurangan | `a - b` | `12` |
| `*` | Perkalian | `a * b` | `85` |
| `/` | Pembagian Riil / Bulat | `a / b` (dalam C++ integer: `17 / 5`) | `3` (C++) / `3.4` (Python) |
| `%` | Modulo (Sisa Bagi) | `a % b` (`17 % 5`) | `2` |

::: warning PERHATIAN PENTING: OPERASI MODULO
Operator modulo (`%`) **hanya berlaku pada bilangan bulat (integer)**. Modulo sangat berguna untuk:
- Mengecek bilangan ganjil/genap: `n % 2 == 0`
- Mengecek kelipatan: `tahun % 400 == 0`
- Membatasi rentang indeks melingkar (*circular index*): `indeks = (indeks + 1) % KAPASITAS`
:::

---

## 3. Operator Relasional & Logika Boolean

### Tabel Kebenaran Operator Logika

| Kondisi $A$ | Kondisi $B$ | $A \land B$ (`AND` / `&&`) | $A \lor B$ (`OR` / `\|\|`) | $\neg A$ (`NOT` / `!`) |
| :---: | :---: | :---: | :---: | :---: |
| **`true`** | **`true`** | **`true`** | **`true`** | **`false`** |
| **`true`** | **`false`** | **`false`** | **`true`** | **`false`** |
| **`false`** | **`true`** | **`false`** | **`true`** | **`true`** |
| **`false`** | **`false`** | **`false`** | **`false`** | **`true`** |

### Evaluasi Sirkuit Pendek (*Short-Circuit Evaluation*)
Pada operasi `A && B`, jika `A` bernilai `false`, maka `B` **tidak akan dievaluasi** karena hasilnya sudah pasti `false`. Begitu pula pada `A || B`, jika `A` bernilai `true`, `B` tidak akan dievaluasi.

---

## 4. Presedensi & Urutan Evaluasi Operator

Jika sebuah ekspresi memiliki banyak operator, kompilator mengevaluasi berdasarkan tingkatan prioritas (*precedence*):

1. Tanda Kurung: `( )` (Prioritas Tertinggi)
2. Operator Unary: `++`, `--`, `!`, `+`, `-`
3. Perkalian & Pembagian: `*`, `/`, `%`
4. Penjumlahan & Pengurangan: `+`, `-`
5. Operator Relasional: `<`, `<=`, `>`, `>=`
6. Kesetaraan: `==`, `!=`
7. Logika AND: `&&`
8. Logika OR: `||`
9. Assignment: `=`, `+=`, `-=`, `*=` (Prioritas Terendah)

---

## 5. Contoh Implementasi Kasus Tahun Kabisat

Sebuah tahun dinyatakan sebagai **Tahun Kabisat (*Leap Year*)** jika:
- Habis dibagi 400, **ATAU**
- Habis dibagi 4 dan tidak habis dibagi 100.

::: code-group
```cpp [C++]
#include <iostream>
using namespace std;

int main() {
    int tahun;
    cout << "Masukkan tahun: ";
    cin >> tahun;

    bool isKabisat = (tahun % 400 == 0) || (tahun % 4 == 0 && tahun % 100 != 0);

    if (isKabisat) {
        cout << tahun << " adalah TAHUN KABISAT (366 hari)." << endl;
    } else {
        cout << tahun << " BUKAN tahun kabisat (365 hari)." << endl;
    }
    return 0;
}
```

```python [Python 3]
tahun = int(input("Masukkan tahun: "))
is_kabisat = (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0)

if is_kabisat:
    print(f"{tahun} adalah TAHUN KABISAT (366 hari).")
else:
    print(f"{tahun} BUKAN tahun kabisat (365 hari).")
```
:::

---

## 📝 Evaluasi & Latihan Mandiri (Sub-CPMK 2)

1. Hitunglah hasil akhir dari ekspresi berikut secara manual:
   ```cpp
   int x = 5, y = 10, z = 15;
   bool hasil = (x + y * 2 > z) && !(y % 3 == 0) || (z / x == 3);
   ```
2. Buatlah program untuk menentukan kelayakan beasiswa mahasiswa dengan kriteria:
   - IPK $\ge 3.50$ **DAN** Penghasilan Orang Tua $< \text{Rp } 5.000.000$, **ATAU**
   - Mahasiswa memiliki prestasi nasional (Status Prestasi = `true`).
