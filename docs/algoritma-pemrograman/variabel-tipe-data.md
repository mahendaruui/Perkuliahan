# Variabel dan Tipe Data

## Apa itu Variabel?

**Variabel** adalah wadah atau tempat untuk menyimpan data di dalam memori komputer yang nilainya dapat berubah selama program berjalan.

### Analogi Variabel

Bayangkan variabel seperti kotak penyimpanan:

- **Nama variabel** = label pada kotak
- **Nilai variabel** = isi kotak
- **Tipe data** = jenis barang yang bisa disimpan

## Aturan Penamaan Variabel

### Yang Boleh ✅

- Dimulai dengan huruf atau underscore (`_`)
- Dapat berisi huruf, angka, dan underscore
- Case-sensitive (huruf besar dan kecil berbeda)

```python
# Contoh nama variabel yang valid
nama
nama_mahasiswa
NamaMahasiswa
_nilai
nilai1
```

### Yang Tidak Boleh ❌

- Dimulai dengan angka
- Menggunakan spasi
- Menggunakan karakter khusus (kecuali underscore)
- Menggunakan kata kunci bahasa pemrograman

```python
# Contoh nama variabel yang TIDAK valid
1nilai        # Dimulai dengan angka
nama mahasiswa # Ada spasi
nilai-ujian   # Ada karakter khusus
for           # Kata kunci bahasa
```

## Tipe Data Dasar

### 1. Integer (Bilangan Bulat)

Bilangan bulat tanpa desimal: ..., -2, -1, 0, 1, 2, ...

```python
# Python
umur = 20
jumlah_mahasiswa = 150
suhu = -5
```

```cpp
// C++
int umur = 20;
int jumlah_mahasiswa = 150;
int suhu = -5;
```

### 2. Float/Double (Bilangan Desimal)

Bilangan dengan titik desimal

```python
# Python
tinggi = 175.5
berat = 65.3
pi = 3.14159
```

```cpp
// C++
float tinggi = 175.5;
double berat = 65.3;
double pi = 3.14159;
```

### 3. String (Teks)

Kumpulan karakter atau teks

```python
# Python
nama = "Budi Santoso"
alamat = 'Jakarta'
pesan = """Ini adalah
teks multi-baris"""
```

```cpp
// C++
string nama = "Budi Santoso";
string alamat = "Jakarta";
```

### 4. Boolean (Logika)

Nilai logika: True (benar) atau False (salah)

```python
# Python
sudah_menikah = False
lulus = True
aktif = True
```

```cpp
// C++
bool sudah_menikah = false;
bool lulus = true;
bool aktif = true;
```

### 5. Character (Karakter Tunggal)

Satu karakter (biasanya dalam C/C++)

```cpp
// C++
char grade = 'A';
char jawaban = 'Y';
char simbol = '#';
```

## Deklarasi dan Inisialisasi

### Deklarasi

Membuat variabel tanpa memberikan nilai awal

```cpp
// C++
int umur;
float nilai;
string nama;
```

### Inisialisasi

Memberikan nilai awal saat membuat variabel

```cpp
// C++
int umur = 20;
float nilai = 85.5;
string nama = "Budi";
```

### Python (Dynamic Typing)

Python tidak perlu deklarasi tipe data secara eksplisit

```python
# Otomatis menentukan tipe data
umur = 20           # integer
nilai = 85.5        # float
nama = "Budi"       # string
lulus = True        # boolean
```

## Konversi Tipe Data (Type Casting)

### Python

```python
# String ke Integer
angka_str = "123"
angka_int = int(angka_str)

# Integer ke Float
nilai = 80
nilai_float = float(nilai)  # 80.0

# Float ke Integer (dibulatkan ke bawah)
nilai_float = 85.7
nilai_int = int(nilai_float)  # 85

# Integer/Float ke String
umur = 20
umur_str = str(umur)  # "20"

# String ke Boolean
nilai_str = "True"
nilai_bool = bool(nilai_str)
```

### C++

```cpp
// String ke Integer
string angka_str = "123";
int angka_int = stoi(angka_str);

// Integer ke Float
int nilai = 80;
float nilai_float = (float)nilai;

// Float ke Integer
float nilai_float = 85.7;
int nilai_int = (int)nilai_float;  // 85

// Integer ke String
int umur = 20;
string umur_str = to_string(umur);

// Char ke Integer (ASCII)
char huruf = 'A';
int kode_ascii = (int)huruf;  // 65
```

## Contoh Program Lengkap

### Program Biodata (Python)

```python
# Program Biodata Mahasiswa

# Input data
print("=== BIODATA MAHASISWA ===")
nama = input("Nama: ")
nim = input("NIM: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi badan (cm): "))
sudah_menikah = False

# Hitung tahun lahir (asumsi tahun sekarang 2024)
tahun_sekarang = 2024
tahun_lahir = tahun_sekarang - umur

# Output
print("\n=== DATA ANDA ===")
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Umur: {umur} tahun")
print(f"Tahun Lahir: {tahun_lahir}")
print(f"Tinggi: {tinggi} cm")
print(f"Status: {'Menikah' if sudah_menikah else 'Belum Menikah'}")
```

### Program Menghitung Nilai Akhir (C++)

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Deklarasi variabel
    string nama;
    float nilai_tugas, nilai_uts, nilai_uas;
    float nilai_akhir;
    char grade;

    // Input data
    cout << "=== HITUNG NILAI AKHIR ===" << endl;
    cout << "Nama: ";
    getline(cin, nama);

    cout << "Nilai Tugas (0-100): ";
    cin >> nilai_tugas;

    cout << "Nilai UTS (0-100): ";
    cin >> nilai_uts;

    cout << "Nilai UAS (0-100): ";
    cin >> nilai_uas;

    // Hitung nilai akhir
    // Bobot: Tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4);

    // Tentukan grade
    if (nilai_akhir >= 85) {
        grade = 'A';
    } else if (nilai_akhir >= 70) {
        grade = 'B';
    } else if (nilai_akhir >= 60) {
        grade = 'C';
    } else if (nilai_akhir >= 50) {
        grade = 'D';
    } else {
        grade = 'E';
    }

    // Output
    cout << "\n=== HASIL ===" << endl;
    cout << "Nama: " << nama << endl;
    cout << "Nilai Akhir: " << nilai_akhir << endl;
    cout << "Grade: " << grade << endl;

    return 0;
}
```

## Scope Variabel

### Variabel Lokal

Variabel yang dideklarasikan di dalam fungsi dan hanya bisa diakses di dalam fungsi tersebut

```python
def hitung_luas():
    panjang = 10  # Variabel lokal
    lebar = 5     # Variabel lokal
    luas = panjang * lebar
    return luas
```

### Variabel Global

Variabel yang dideklarasikan di luar fungsi dan bisa diakses dari mana saja

```python
pi = 3.14159  # Variabel global

def hitung_luas_lingkaran(r):
    luas = pi * r * r  # Mengakses variabel global
    return luas
```

## Tips Best Practice

1. **Gunakan nama yang deskriptif**

   ```python
   # Buruk
   x = 20

   # Baik
   umur_mahasiswa = 20
   ```

2. **Konsisten dengan konvensi penamaan**

   - Python: `snake_case` (huruf kecil dengan underscore)
   - C++/Java: `camelCase` atau `PascalCase`

3. **Inisialisasi variabel sebelum digunakan**

4. **Gunakan konstanta untuk nilai tetap**
   ```python
   PI = 3.14159
   GRAVITASI = 9.8
   ```

## Latihan

1. Buatlah program untuk menghitung luas dan keliling lingkaran!

   - Input: jari-jari
   - Output: luas dan keliling

2. Buatlah program konversi suhu dari Celsius ke Fahrenheit!

   - Rumus: F = (C × 9/5) + 32

3. Buatlah program untuk menghitung IPK dari 5 mata kuliah!

   - Input: nilai 5 mata kuliah
   - Output: IPK (rata-rata)

4. Buatlah program untuk menghitung total belanja dengan diskon!
   - Input: harga barang, jumlah barang, persentase diskon
   - Output: total harga setelah diskon

## Rangkuman

- **Variabel** adalah tempat menyimpan data yang nilainya dapat berubah
- **Tipe data dasar**: Integer, Float, String, Boolean, Character
- **Deklarasi**: membuat variabel
- **Inisialisasi**: memberikan nilai awal
- **Type Casting**: mengubah tipe data
- **Scope**: lokal (dalam fungsi) atau global (di luar fungsi)
- Gunakan nama variabel yang deskriptif dan ikuti konvensi penamaan

---

**Sebelumnya**: [Pengenalan](./pengenalan.md) | **Selanjutnya**: [Operator](./operator.md)
