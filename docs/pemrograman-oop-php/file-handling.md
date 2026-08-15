# Minggu 12: File Handling (I/O & Filesystem)

## 🎯 Capaian Pembelajaran (Sub-CPMK 4)
Setelah menyelesaikan materi ini, mahasiswa mampu:
1. Membaca dan menulis file teks menggunakan fungsi I/O PHP.
2. Mengolah data dalam format **CSV** dan **JSON**.
3. Menerapkan pola **Repository** sederhana untuk persistensi data berbasis file.

---

## 1. Menulis File Teks

```php
<?php

$namaFile = "mahasiswa.csv";

// Menulis file (mode 'w' = overwrite)
$file = fopen($namaFile, 'w');
fwrite($file, "NIM,Nama,IPK\n");
fwrite($file, "240101,Budi Santoso,3.85\n");
fwrite($file, "240102,Siti Aminah,3.90\n");
fwrite($file, "240103,Rian Ardianto,3.70\n");
fclose($file);

echo "✅ Data berhasil disimpan ke {$namaFile}\n";
```

### Menggunakan `file_put_contents()` (lebih singkat):
```php
$data = "NIM,Nama,IPK\n240101,Budi,3.85\n240102,Siti,3.90\n";
file_put_contents("mahasiswa.csv", $data);

// Append mode (menambahkan tanpa overwrite)
file_put_contents("log.txt", "[INFO] Aksi dilakukan\n", FILE_APPEND);
```

---

## 2. Membaca File Teks

```php
<?php

// Cara 1: Baca baris per baris
$file = fopen("mahasiswa.csv", 'r');
while (($baris = fgets($file)) !== false) {
    echo trim($baris) . "\n";
}
fclose($file);

// Cara 2: Baca seluruh file sekaligus
$isi = file_get_contents("mahasiswa.csv");
echo $isi;

// Cara 3: Baca menjadi array per baris
$baris = file("mahasiswa.csv", FILE_IGNORE_NEW_LINES);
foreach ($baris as $b) {
    echo $b . "\n";
}
```

---

## 3. Parsing CSV ke Objek

```php
<?php

class Mahasiswa
{
    public function __construct(
        public string $nim,
        public string $nama,
        public float $ipk
    ) {}
}

function bacaCSV(string $namaFile): array
{
    $daftar = [];
    $file = fopen($namaFile, 'r');
    fgetcsv($file); // Lewati header

    while (($data = fgetcsv($file)) !== false) {
        if (count($data) === 3) {
            $daftar[] = new Mahasiswa(
                nim: trim($data[0]),
                nama: trim($data[1]),
                ipk: (float) trim($data[2])
            );
        }
    }
    fclose($file);
    return $daftar;
}

$listMhs = bacaCSV("mahasiswa.csv");
foreach ($listMhs as $mhs) {
    echo "{$mhs->nim} | {$mhs->nama} | IPK: {$mhs->ipk}\n";
}
```

---

## 4. Bekerja dengan JSON

```php
<?php

// Menyimpan data ke JSON
$data = [
    ['nim' => '2401', 'nama' => 'Budi', 'ipk' => 3.85],
    ['nim' => '2402', 'nama' => 'Siti', 'ipk' => 3.90],
];
file_put_contents("data.json", json_encode($data, JSON_PRETTY_PRINT));

// Membaca data dari JSON
$json = file_get_contents("data.json");
$mahasiswa = json_decode($json, true); // true = return array

foreach ($mahasiswa as $mhs) {
    echo "{$mhs['nim']} - {$mhs['nama']}\n";
}
```

---

## 📝 Tugas Praktikum

1. Buat program **Catatan Harian (Diary Logger)** berbasis CLI.
2. Menu: (1) Tambah Catatan, (2) Lihat Semua Catatan, (3) Keluar.
3. Simpan ke file `catatan.json` agar data persisten (gunakan append/merge).
