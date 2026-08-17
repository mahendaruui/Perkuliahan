---
marp: true
theme: default
paginate: true
header: 'Pemrograman Berorientasi Objek — Pertemuan 1'
footer: 'Mahendar Dwi Payana, S.ST., M.T. • Universitas Ubudiyah Indonesia'
style: |
  section {
    background-color: #0f172a;
    color: #0f172a;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  h1 {
    color: #ef4444;
  }
  h2 {
    color: #475569;
  }
  th {
    background-color: #e2e8f0;
    color: #0f172a;
  }
  td {
    background-color: #0f172a;
    color: #334155;
  }
  code {
    background-color: #e2e8f0;
    color: #38bdf8;
  }
---

<!-- _class: lead -->
# Kontrak Perkuliahan & Pengantar Pemrograman Berorientasi Objek
### IFR 214 • Bobot 3 SKS (T=2, P=1)

**Dosen Pengampu:** Mahendar Dwi Payana, S.ST., M.T.  
Fakultas Sains dan Teknologi — Universitas Ubudiyah Indonesia

---

## 📍 Agenda Pertemuan 1

1. **Kontrak Perkuliahan & Asesmen OBE** (CPL, CPMK, Bobot Nilai)
2. **Apa itu Paradigma Pemrograman?**
3. **Pemrograman Prosedural vs Pemrograman Berorientasi Objek (OOP)**
4. **4 Pilar Fundamental OOP** (Encapsulation, Inheritance, Polymorphism, Abstraction)
5. **Memodelkan Objek Nyata** (Atribut/State & Method/Behavior)
6. **Keuntungan & Relevansi OOP di Industri**
7. **Tooling & Setup Lingkungan Praktikum** (Java / PHP 8+, IDE)
8. **Tanya Jawab & Penugasan Eksplorasi**

---

## ⚖️ Kontrak Perkuliahan & Penilaian OBE

| Komponen Penilaian | Bobot (%) | Keterangan |
| :--- | :---: | :--- |
| **Kehadiran & Partisipasi** | **10%** | Minimal kehadiran 75% |
| **Tugas Individu** | **15%** | Latihan mandiri & pemahaman konsep |
| **Tugas Kelompok / Kasus** | **20%** | Case-Based Learning (CBL) |
| **Kuis Teori & Praktik** | **10%** | Evaluasi berkala |
| **Ujian Tengah Semester (UTS)** | **20%** | Ujian tertulis & coding |
| **UAS / Proyek Akhir (Mini Project)** | **25%** | Project-Based Learning (PjBL) |
| **Total** | **100%** | |

---

## 🧠 Paradigma Pemrograman

### 1. Pemrograman Prosedural / Terstruktur
- Program dipandang sebagai urutan langkah instruksi / algoritma.
- Fokus pada **fungsi/prosedur** (*verbs* / aksi).
- **Data dan fungsi terpisah**: Data mengalir bebas di antara fungsi.
- Rentan efek samping (*side-effects*) pada proyek berskala besar.

### 2. Pemrograman Berorientasi Objek (OOP)
- Program dipandang sebagai **kumpulan objek mandiri** yang saling berinteraksi.
- Fokus pada **objek/entitas** (*nouns* / benda nyata).
- **Data dan perilaku dibungkus menjadi satu kesatuan utuh** (*Encapsulation*).
- Sangat modular, aman, dan mudah dikembangkan.

---

## ⚖️ Prosedural vs Berorientasi Objek

| Aspek | Pemrograman Prosedural | Pemrograman Berorientasi Objek |
| :--- | :--- | :--- |
| **Pusat Pendekatan** | Fungsi / Algoritma | Objek (Data + Perilaku) |
| **Struktur** | Top-Down | Bottom-Up |
| **Keamanan Data** | Rendah (Data global terbuka) | Tinggi (Encapsulation / Private) |
| **Reusability** | Terbatas pemanggilan fungsi | Sangat tinggi (Inheritance & Polymorphism) |
| **Maintenance** | Sulit pada ribuan baris kode | Sangat modular & terisolasi |
| **Model Masalah** | Alur logika instruksi | Model objek dunia nyata |

---

## 🏛️ 4 Pilar Utama OOP

1. **🔒 Encapsulation (Pembungkusan):**
   Membungkus data dan method menjadi satu unit serta menyembunyikan detail internal dari modifikasi luar langsung (*Information Hiding*).

2. **🧬 Inheritance (Pewarisan):**
   Mekanisme di mana subclass mewarisi sifat dan perilaku dari superclass tanpa perlu menduplikasi kode (*Code Reuse*).

3. **🎭 Polymorphism (Banyak Bentuk):**
   Kemampuan objek/method untuk merespons dengan cara yang berbeda sesuai tipe spesifiknya saat runtime (*Overriding & Overloading*).

4. **🧩 Abstraction (Abstraksi):**
   Menyembunyikan detail implementasi rumit dan hanya mengekspos antarmuka penting (*Interface & Abstract Class*).

---

## 🚗 Memodelkan Objek: "Mobil"

### 1. Atribut / State (Data)
- `merk` = "Toyota"
- `warna` = "Hitam"
- `kecepatan` = 60 km/jam

### 2. Perilaku / Method (Aksi)
- `gas(int akselerasi)`
- `rem()`
- `isiBensin(double liter)`

```java
public class Mobil {
    private String merk;
    private int kecepatan = 0;

    public Mobil(String merk) { this.merk = merk; }

    public void gas(int akselerasi) {
        this.kecepatan += akselerasi;
        System.out.println(merk + " melaju " + kecepatan + " km/jam");
    }
}
```

---

## 🚀 Keuntungan Utama OOP

- **🧱 Modularitas Tinggi:** Class mandiri mempermudah pencarian bug dan pengujian terisolasi.
- **🔄 Don't Repeat Yourself (DRY):** Mengurangi duplikasi kode secara drastis melalui inheritance.
- **🛡️ Keamanan & Integritas:** Atribut dilindungi dengan visibilitas `private` dan validasi setter.
- **📈 Skalabilitas Tim:** Memungkinkan banyak engineer mengerjakan modul berbeda secara simultan.
- **⚡ Standar Industri:** Prasyarat mutlak memahami Spring Boot, Laravel, NestJS, Flutter, dan Android.

---

## 💻 Persiapan Lab & Tooling

### 1. SDK / Runtime
- **Java:** JDK 17 LTS / JDK 21 LTS (`javac -version`)
- **PHP:** PHP 8.1+ / 8.2+ & Composer (`php -v`)

### 2. IDE & Editor
- **Visual Studio Code** + Extension Pack for Java / PHP Intelephense
- **IntelliJ IDEA** (Community / Ultimate)

### 3. Version Control
- **Git & GitHub** untuk pengumpulan tugas dan proyek akhir

---

<!-- _class: lead -->
# Sesi Tanya Jawab & Diskusi 💬

### 📝 Persiapan Pertemuan 2:
- Pastikan lingkungan pemrograman sudah terpasang di laptop.
- Kita akan langsung membuat **Class, Object, Instance Variable**, dan memahami memori **Stack vs Heap**.

**Portal Materi:**  
https://mahendar.github.io/Perkuliahan/
