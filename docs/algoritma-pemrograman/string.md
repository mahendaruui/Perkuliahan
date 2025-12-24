# String

## Apa itu String?

**String** adalah tipe data yang merepresentasikan urutan karakter (teks). String dapat berisi huruf, angka, simbol, dan spasi.

### Karakteristik String

- Urutan karakter
- Immutable di beberapa bahasa (Python)
- Dapat diakses menggunakan indeks
- Mendukung berbagai operasi teks

## Deklarasi String

### Python

```python
# Single quote
nama = 'Budi'

# Double quote
alamat = "Jakarta"

# Triple quote (multi-line)
bio = """Nama: Budi
Umur: 20
Kota: Jakarta"""

# Raw string (ignore escape)
path = r"C:\Users\nama\file.txt"

# F-string (formatted)
umur = 20
pesan = f"Umur saya {umur} tahun"
```

### C++

```cpp
// C-style string (array of char)
char nama[50] = "Budi";

// C++ string class
#include <string>
string alamat = "Jakarta";

// Multi-line
string bio = "Nama: Budi\n"
             "Umur: 20\n"
             "Kota: Jakarta";
```

## Operasi Dasar String

### 1. Akses Karakter

```python
# Python
nama = "Budi"

print(nama[0])   # 'B' (karakter pertama)
print(nama[2])   # 'd'
print(nama[-1])  # 'i' (karakter terakhir)

# Slicing
print(nama[0:2])   # 'Bu'
print(nama[1:])    # 'udi'
print(nama[:3])    # 'Bud'
```

```cpp
// C++
string nama = "Budi";

cout << nama[0] << endl;     // 'B'
cout << nama[2] << endl;     // 'd'
cout << nama.at(0) << endl;  // 'B' (with bounds checking)
```

### 2. Panjang String

```python
# Python
nama = "Budi Santoso"
print(len(nama))  # 12
```

```cpp
// C++
string nama = "Budi Santoso";
cout << nama.length() << endl;  // 12
cout << nama.size() << endl;    // 12
```

### 3. Konkatenasi (Penggabungan)

```python
# Python
nama_depan = "Budi"
nama_belakang = "Santoso"

# Operator +
nama_lengkap = nama_depan + " " + nama_belakang

# Method join
nama_lengkap = " ".join([nama_depan, nama_belakang])

# F-string
nama_lengkap = f"{nama_depan} {nama_belakang}"
```

```cpp
// C++
string nama_depan = "Budi";
string nama_belakang = "Santoso";

// Operator +
string nama_lengkap = nama_depan + " " + nama_belakang;

// append()
nama_depan.append(" ");
nama_depan.append(nama_belakang);
```

### 4. Perulangan pada String

```python
# Python
kata = "Python"

# Iterasi karakter
for huruf in kata:
    print(huruf)

# Dengan index
for i in range(len(kata)):
    print(f"{i}: {kata[i]}")
```

```cpp
// C++
string kata = "Python";

// Iterasi karakter
for (int i = 0; i < kata.length(); i++) {
    cout << kata[i] << endl;
}

// Range-based loop
for (char huruf : kata) {
    cout << huruf << endl;
}
```

## Flowchart: Operasi String

### Flowchart Membalik String

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: string/]
    Input --> Init[hasil = ''<br/>i = panjang - 1]
    Init --> Cek{i >= 0?}
    Cek -->|Ya| Tambah[hasil = hasil + string[i]]
    Tambah --> Dec[i = i - 1]
    Dec --> Cek
    Cek -->|Tidak| Output[/Output: hasil/]
    Output --> Stop([Selesai])
```

### Flowchart Menghitung Vokal

```mermaid
flowchart TD
    Start([Mulai]) --> Input[/Input: string/]
    Input --> Init[jumlah = 0<br/>i = 0<br/>vokal = 'aeiouAEIOU']
    Init --> Cek{i < panjang?}
    Cek -->|Ya| IsVokal{string[i] dalam vokal?}
    IsVokal -->|Ya| Inc1[jumlah = jumlah + 1]
    IsVokal -->|Tidak| Inc2[i = i + 1]
    Inc1 --> Inc2
    Inc2 --> Cek
    Cek -->|Tidak| Output[/Output: jumlah/]
    Output --> Stop([Selesai])
```

## Metode String Python

### Case Conversion

```python
teks = "Belajar Python"

print(teks.upper())       # BELAJAR PYTHON
print(teks.lower())       # belajar python
print(teks.capitalize())  # Belajar python
print(teks.title())       # Belajar Python
print(teks.swapcase())    # bELAJAR pYTHON
```

### Pencarian

```python
teks = "Belajar Python Programming"

# Cek substring
print("Python" in teks)           # True
print(teks.startswith("Belajar")) # True
print(teks.endswith("ing"))       # True

# Cari posisi
print(teks.find("Python"))        # 8
print(teks.index("Python"))       # 8
print(teks.count("a"))            # 3
```

### Modifikasi

```python
teks = "  Belajar Python  "

# Hapus spasi
print(teks.strip())   # "Belajar Python"
print(teks.lstrip())  # "Belajar Python  "
print(teks.rstrip())  # "  Belajar Python"

# Replace
print(teks.replace("Python", "Java"))  # "  Belajar Java  "

# Split
kata = "Budi,20,Jakarta"
data = kata.split(",")  # ['Budi', '20', 'Jakarta']
```

### Validasi

```python
teks1 = "12345"
teks2 = "Python"
teks3 = "Python123"

print(teks1.isdigit())      # True
print(teks2.isalpha())      # True
print(teks3.isalnum())      # True
print(teks2.islower())      # False
print("PYTHON".isupper())   # True
```

## Metode String C++

```cpp
#include <string>
#include <algorithm>
#include <cctype>

string teks = "Belajar C++";

// Panjang
int panjang = teks.length();

// Substring
string sub = teks.substr(0, 7);  // "Belajar"

// Find
size_t pos = teks.find("C++");   // 8

// Replace
teks.replace(8, 3, "Python");    // "Belajar Python"

// Insert
teks.insert(7, " untuk");        // "Belajar untuk Python"

// Erase
teks.erase(7, 6);               // Hapus 6 karakter dari index 7

// Compare
int hasil = teks.compare("Belajar");  // 0 jika sama

// Transform to uppercase
transform(teks.begin(), teks.end(), teks.begin(), ::toupper);

// Transform to lowercase
transform(teks.begin(), teks.end(), teks.begin(), ::tolower);
```

## Contoh Program Lengkap

### Program 1: Membalik String

```python
# Python
def balik_string(s):
    hasil = ""
    for i in range(len(s) - 1, -1, -1):
        hasil += s[i]
    return hasil

# Atau menggunakan slicing
def balik_string_v2(s):
    return s[::-1]

# Contoh
kata = input("Masukkan kata: ")
print(f"Kata dibalik: {balik_string(kata)}")
```

### Program 2: Cek Palindrome

```cpp
// C++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isPalindrome(string s) {
    string s_reversed = s;
    reverse(s_reversed.begin(), s_reversed.end());
    return s == s_reversed;
}

int main() {
    string kata;
    cout << "Masukkan kata: ";
    cin >> kata;

    if (isPalindrome(kata)) {
        cout << kata << " adalah palindrome" << endl;
    } else {
        cout << kata << " bukan palindrome" << endl;
    }

    return 0;
}
```

### Program 3: Hitung Huruf Vokal dan Konsonan

```python
# Python
def hitung_vokal_konsonan(teks):
    vokal = "aeiouAEIOU"
    jumlah_vokal = 0
    jumlah_konsonan = 0

    for char in teks:
        if char.isalpha():
            if char in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1

    return jumlah_vokal, jumlah_konsonan

# Contoh
teks = input("Masukkan teks: ")
vokal, konsonan = hitung_vokal_konsonan(teks)

print(f"Jumlah vokal: {vokal}")
print(f"Jumlah konsonan: {konsonan}")
```

### Program 4: Menghitung Frekuensi Karakter

```python
# Python
def hitung_frekuensi(teks):
    frekuensi = {}

    for char in teks:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1

    return frekuensi

# Contoh
teks = "Belajar Python"
freq = hitung_frekuensi(teks)

print("Frekuensi karakter:")
for char, jumlah in sorted(freq.items()):
    print(f"'{char}': {jumlah}")
```

### Program 5: Validasi Password

```python
# Python
def validasi_password(password):
    """
    Password valid jika:
    - Minimal 8 karakter
    - Ada huruf besar
    - Ada huruf kecil
    - Ada angka
    - Ada simbol
    """
    if len(password) < 8:
        return False, "Password minimal 8 karakter"

    ada_besar = any(c.isupper() for c in password)
    ada_kecil = any(c.islower() for c in password)
    ada_angka = any(c.isdigit() for c in password)
    ada_simbol = any(not c.isalnum() for c in password)

    if not ada_besar:
        return False, "Password harus ada huruf besar"
    if not ada_kecil:
        return False, "Password harus ada huruf kecil"
    if not ada_angka:
        return False, "Password harus ada angka"
    if not ada_simbol:
        return False, "Password harus ada simbol"

    return True, "Password valid"

# Contoh
password = input("Masukkan password: ")
valid, pesan = validasi_password(password)

if valid:
    print("✓", pesan)
else:
    print("✗", pesan)
```

### Program 6: Format Nama

```cpp
// C++
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
using namespace std;

string capitalize(string word) {
    if (!word.empty()) {
        word[0] = toupper(word[0]);
        for (size_t i = 1; i < word.length(); i++) {
            word[i] = tolower(word[i]);
        }
    }
    return word;
}

string formatNama(string nama) {
    stringstream ss(nama);
    string word, result;

    while (ss >> word) {
        if (!result.empty()) {
            result += " ";
        }
        result += capitalize(word);
    }

    return result;
}

int main() {
    string nama;
    cout << "Masukkan nama: ";
    getline(cin, nama);

    cout << "Nama terformat: " << formatNama(nama) << endl;

    return 0;
}
```

## String Formatting

### Python F-String

```python
nama = "Budi"
umur = 20
nilai = 85.5

# F-string
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Nilai: {nilai:.2f}")

# Alignment
print(f"{'Nama':<10} | {'Nilai':>5}")
print(f"{nama:<10} | {nilai:>5.1f}")

# Format angka
angka = 1234567.89
print(f"{angka:,.2f}")  # 1,234,567.89
```

### C++ Format

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    string nama = "Budi";
    int umur = 20;
    double nilai = 85.5;

    cout << "Nama: " << nama << endl;
    cout << "Umur: " << umur << " tahun" << endl;
    cout << fixed << setprecision(2);
    cout << "Nilai: " << nilai << endl;

    return 0;
}
```

## Latihan

1. **Program Anagram**

   - Cek apakah dua kata adalah anagram
   - Contoh: "listen" dan "silent"

2. **Program Caesar Cipher**

   - Enkripsi teks dengan menggeser huruf
   - Contoh: "ABC" shift 1 → "BCD"

3. **Program Kata Terpanjang**

   - Input kalimat
   - Cari kata terpanjang

4. **Program Reverse Words**

   - Input: "Belajar Python"
   - Output: "Python Belajar"

5. **Program Remove Duplicates**

   - Hapus karakter duplikat dari string
   - Input: "programming"
   - Output: "progamin"

6. **Program Word Count**
   - Hitung jumlah kata, karakter, dan baris dalam teks

## Rangkuman

- **String** adalah urutan karakter
- **Indeks** untuk akses karakter (dimulai dari 0)
- **Immutable** di Python (tidak bisa diubah langsung)
- **Metode string** untuk manipulasi teks
- **Slicing** untuk mengambil substring (Python)
- **Konkatenasi** untuk menggabungkan string
- **Format string** untuk output yang rapi

---

**Sebelumnya**: [Array](./array.md) | **Selanjutnya**: [Fungsi dan Prosedur](./fungsi-prosedur.md)
