# Operator

## Apa itu Operator?

**Operator** adalah simbol khusus yang digunakan untuk melakukan operasi pada variabel dan nilai.

## Jenis-Jenis Operator

### 1. Operator Aritmatika

Digunakan untuk operasi matematika dasar.

| Operator | Deskripsi                | Contoh    | Hasil      |
| -------- | ------------------------ | --------- | ---------- |
| `+`      | Penjumlahan              | `5 + 3`   | `8`        |
| `-`      | Pengurangan              | `5 - 3`   | `2`        |
| `*`      | Perkalian                | `5 * 3`   | `15`       |
| `/`      | Pembagian                | `10 / 3`  | `3.333...` |
| `//`     | Pembagian bulat (Python) | `10 // 3` | `3`        |
| `%`      | Modulus (sisa bagi)      | `10 % 3`  | `1`        |
| `**`     | Pangkat (Python)         | `2 ** 3`  | `8`        |

#### Contoh Program (Python)

```python
# Operator Aritmatika
a = 10
b = 3

print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} * {b} = {a * b}")
print(f"Pembagian: {a} / {b} = {a / b}")
print(f"Pembagian Bulat: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Pangkat: {a} ** {b} = {a ** b}")
```

#### Contoh Program (C++)

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a = 10;
    int b = 3;

    cout << "Penjumlahan: " << a << " + " << b << " = " << (a + b) << endl;
    cout << "Pengurangan: " << a << " - " << b << " = " << (a - b) << endl;
    cout << "Perkalian: " << a << " * " << b << " = " << (a * b) << endl;
    cout << "Pembagian: " << a << " / " << b << " = " << (a / b) << endl;
    cout << "Modulus: " << a << " % " << b << " = " << (a % b) << endl;
    cout << "Pangkat: " << a << " ^ " << b << " = " << pow(a, b) << endl;

    return 0;
}
```

### 2. Operator Penugasan (Assignment)

Digunakan untuk memberikan nilai ke variabel.

| Operator | Contoh   | Ekuivalen dengan |
| -------- | -------- | ---------------- |
| `=`      | `x = 5`  | `x = 5`          |
| `+=`     | `x += 3` | `x = x + 3`      |
| `-=`     | `x -= 3` | `x = x - 3`      |
| `*=`     | `x *= 3` | `x = x * 3`      |
| `/=`     | `x /= 3` | `x = x / 3`      |
| `%=`     | `x %= 3` | `x = x % 3`      |

#### Contoh

```python
x = 10
print(f"Nilai awal: {x}")

x += 5  # x = x + 5
print(f"Setelah x += 5: {x}")

x -= 3  # x = x - 3
print(f"Setelah x -= 3: {x}")

x *= 2  # x = x * 2
print(f"Setelah x *= 2: {x}")

x /= 4  # x = x / 4
print(f"Setelah x /= 4: {x}")
```

### 3. Operator Perbandingan (Relasional)

Digunakan untuk membandingkan dua nilai. Hasilnya adalah boolean (True/False).

| Operator | Deskripsi                    | Contoh   | Hasil   |
| -------- | ---------------------------- | -------- | ------- |
| `==`     | Sama dengan                  | `5 == 5` | `True`  |
| `!=`     | Tidak sama dengan            | `5 != 3` | `True`  |
| `>`      | Lebih besar                  | `5 > 3`  | `True`  |
| `<`      | Lebih kecil                  | `5 < 3`  | `False` |
| `>=`     | Lebih besar atau sama dengan | `5 >= 5` | `True`  |
| `<=`     | Lebih kecil atau sama dengan | `3 <= 5` | `True`  |

#### Contoh Program

```python
a = 10
b = 5

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
print(f"{a} >= {b}: {a >= b}")  # True
print(f"{a} <= {b}: {a <= b}")  # False
```

### 4. Operator Logika

Digunakan untuk operasi logika boolean.

| Operator      | Deskripsi                 | Contoh           | Hasil   |
| ------------- | ------------------------- | ---------------- | ------- |
| `and` / `&&`  | DAN (keduanya harus True) | `True and False` | `False` |
| `or` / `\|\|` | ATAU (salah satu True)    | `True or False`  | `True`  |
| `not` / `!`   | TIDAK (membalik nilai)    | `not True`       | `False` |

#### Tabel Kebenaran AND

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

#### Tabel Kebenaran OR

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

#### Contoh Program (Python)

```python
# Contoh: Cek kelayakan beasiswa
nilai_ipk = 3.5
kehadiran = 85
aktif_organisasi = True

# Syarat beasiswa:
# IPK >= 3.0 DAN Kehadiran >= 80%
layak_akademik = (nilai_ipk >= 3.0) and (kehadiran >= 80)

# Syarat tambahan:
# Layak akademik ATAU Aktif organisasi
layak_beasiswa = layak_akademik or aktif_organisasi

print(f"IPK: {nilai_ipk}")
print(f"Kehadiran: {kehadiran}%")
print(f"Aktif Organisasi: {aktif_organisasi}")
print(f"Layak Beasiswa: {layak_beasiswa}")
```

#### Contoh Program (C++)

```cpp
#include <iostream>
using namespace std;

int main() {
    float nilai_ipk = 3.5;
    int kehadiran = 85;
    bool aktif_organisasi = true;

    // Syarat beasiswa
    bool layak_akademik = (nilai_ipk >= 3.0) && (kehadiran >= 80);
    bool layak_beasiswa = layak_akademik || aktif_organisasi;

    cout << "IPK: " << nilai_ipk << endl;
    cout << "Kehadiran: " << kehadiran << "%" << endl;
    cout << "Aktif Organisasi: " << (aktif_organisasi ? "Ya" : "Tidak") << endl;
    cout << "Layak Beasiswa: " << (layak_beasiswa ? "Ya" : "Tidak") << endl;

    return 0;
}
```

### 5. Operator Increment dan Decrement

Digunakan untuk menambah atau mengurangi nilai sebesar 1.

| Operator | Deskripsi            | Contoh           |
| -------- | -------------------- | ---------------- |
| `++`     | Increment (tambah 1) | `x++` atau `++x` |
| `--`     | Decrement (kurang 1) | `x--` atau `--x` |

#### Pre-increment vs Post-increment

```cpp
// C++
int x = 5;

// Post-increment: gunakan nilai, baru tambah
int y = x++;  // y = 5, x = 6

// Pre-increment: tambah dulu, baru gunakan nilai
int z = ++x;  // x = 7, z = 7
```

```python
# Python (tidak ada ++ dan --)
x = 5
x += 1  # Sama dengan x++
```

### 6. Operator Bitwise (Opsional)

Operasi pada level bit (binary).

| Operator | Deskripsi   | Contoh          |
| -------- | ----------- | --------------- |
| `&`      | AND         | `5 & 3` = `1`   |
| `\|`     | OR          | `5 \| 3` = `7`  |
| `^`      | XOR         | `5 ^ 3` = `6`   |
| `~`      | NOT         | `~5` = `-6`     |
| `<<`     | Left Shift  | `5 << 1` = `10` |
| `>>`     | Right Shift | `5 >> 1` = `2`  |

## Prioritas Operator (Operator Precedence)

Urutan evaluasi operator dari yang tertinggi ke terendah:

1. `()` - Tanda kurung
2. `**` - Pangkat (Python)
3. `*`, `/`, `//`, `%` - Perkalian, Pembagian
4. `+`, `-` - Penjumlahan, Pengurangan
5. `<`, `<=`, `>`, `>=` - Perbandingan
6. `==`, `!=` - Kesamaan
7. `not` - Logika NOT
8. `and` - Logika AND
9. `or` - Logika OR

### Contoh

```python
hasil = 2 + 3 * 4
print(hasil)  # 14, bukan 20

hasil = (2 + 3) * 4
print(hasil)  # 20

hasil = 10 > 5 and 3 < 7
print(hasil)  # True
```

## Studi Kasus: Kalkulator Sederhana

### Python

```python
def kalkulator():
    print("=== KALKULATOR SEDERHANA ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Modulus (%)")
    print("6. Pangkat (**)")

    pilihan = input("\nPilih operasi (1-6): ")

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = angka1 + angka2
        operator = '+'
    elif pilihan == '2':
        hasil = angka1 - angka2
        operator = '-'
    elif pilihan == '3':
        hasil = angka1 * angka2
        operator = '*'
    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            operator = '/'
        else:
            print("Error: Tidak bisa membagi dengan nol!")
            return
    elif pilihan == '5':
        hasil = angka1 % angka2
        operator = '%'
    elif pilihan == '6':
        hasil = angka1 ** angka2
        operator = '**'
    else:
        print("Pilihan tidak valid!")
        return

    print(f"\n{angka1} {operator} {angka2} = {hasil}")

# Jalankan kalkulator
kalkulator()
```

### C++

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int pilihan;
    double angka1, angka2, hasil;

    cout << "=== KALKULATOR SEDERHANA ===" << endl;
    cout << "1. Penjumlahan (+)" << endl;
    cout << "2. Pengurangan (-)" << endl;
    cout << "3. Perkalian (*)" << endl;
    cout << "4. Pembagian (/)" << endl;
    cout << "5. Modulus (%)" << endl;
    cout << "6. Pangkat (^)" << endl;

    cout << "\nPilih operasi (1-6): ";
    cin >> pilihan;

    cout << "Masukkan angka pertama: ";
    cin >> angka1;

    cout << "Masukkan angka kedua: ";
    cin >> angka2;

    switch(pilihan) {
        case 1:
            hasil = angka1 + angka2;
            cout << angka1 << " + " << angka2 << " = " << hasil << endl;
            break;
        case 2:
            hasil = angka1 - angka2;
            cout << angka1 << " - " << angka2 << " = " << hasil << endl;
            break;
        case 3:
            hasil = angka1 * angka2;
            cout << angka1 << " * " << angka2 << " = " << hasil << endl;
            break;
        case 4:
            if (angka2 != 0) {
                hasil = angka1 / angka2;
                cout << angka1 << " / " << angka2 << " = " << hasil << endl;
            } else {
                cout << "Error: Tidak bisa membagi dengan nol!" << endl;
            }
            break;
        case 5:
            hasil = (int)angka1 % (int)angka2;
            cout << angka1 << " % " << angka2 << " = " << hasil << endl;
            break;
        case 6:
            hasil = pow(angka1, angka2);
            cout << angka1 << " ^ " << angka2 << " = " << hasil << endl;
            break;
        default:
            cout << "Pilihan tidak valid!" << endl;
    }

    return 0;
}
```

## Latihan

1. **Program Konversi Nilai**

   - Input: nilai 0-100
   - Output: grade (A, B, C, D, E)
   - A: >= 85, B: >= 70, C: >= 60, D: >= 50, E: < 50

2. **Program Cek Bilangan**

   - Input: sebuah bilangan
   - Cek apakah bilangan tersebut:
     - Genap atau ganjil
     - Positif, negatif, atau nol
     - Kelipatan 5 atau bukan

3. **Program Diskon Belanja**

   - Input: total belanja
   - Aturan diskon:
     - < Rp 100.000: tidak ada diskon
     - Rp 100.000 - Rp 500.000: diskon 10%
     - > Rp 500.000: diskon 20%
   - Output: total yang harus dibayar

4. **Program Tahun Kabisat**
   - Input: tahun
   - Cek apakah tahun tersebut kabisat
   - Aturan:
     - Habis dibagi 4 DAN tidak habis dibagi 100, ATAU
     - Habis dibagi 400

## Rangkuman

- **Operator Aritmatika**: `+`, `-`, `*`, `/`, `%`, `**`
- **Operator Penugasan**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- **Operator Perbandingan**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Operator Logika**: `and`, `or`, `not`
- **Operator Increment/Decrement**: `++`, `--`
- Perhatikan prioritas operator dalam ekspresi
- Gunakan tanda kurung untuk mengubah urutan evaluasi

---

**Sebelumnya**: [Variabel dan Tipe Data](./variabel-tipe-data.md) | **Selanjutnya**: [Percabangan](./percabangan.md)
