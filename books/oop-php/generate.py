#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Buku Ajar: Pemrograman Berorientasi Objek Menggunakan PHP 8+
Mata Kuliah: Pemrograman Berorientasi Objek (IFR 214 - 3 SKS)
Penulis: Mahendar Dwi Payana, S.ST., M.T.
Program Studi Informatika, Fakultas Sains dan Teknologi, Universitas Ubudiyah Indonesia

Mendukung versioning dokumen Word (.docx)
Penggunaan:
    python generate.py
    python generate.py --version 1.0.0
"""

import os
import sys
import argparse
import shutil

from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Include repository root for module imports
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, REPO_ROOT)

from books.core.book_builder import AcademicBookBuilder

def parse_args():
    parser = argparse.ArgumentParser(description="Generator Buku Ajar OOP PHP 8+")
    parser.add_argument(
        "--version", "-v",
        type=str,
        default="v1.0.0",
        help="Versi rilis dokumen (default: v1.0.0)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
        help="Folder penyimpanan berkas output"
    )
    return parser.parse_args()

def build_oop_php_book(version="v1.0.0", output_dir=None):
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        
    os.makedirs(output_dir, exist_ok=True)
    clean_version = version if version.startswith("v") else f"v{version}"
    filename = f"Buku_Ajar_OOP_PHP8_{clean_version}_Mahendar_Dwi_Payana.docx"
    output_path = os.path.join(output_dir, filename)
    latest_path = os.path.join(output_dir, "Buku_Ajar_OOP_PHP8_Latest.docx")

    print("=" * 65)
    print(f" GENERATOR BUKU AJAR: OOP PHP 8+ (UNIVERSITAS UBUDIYAH INDONESIA)")
    print(f" Versi Dokumen : {clean_version}")
    print(f" Target Berkas : {output_path}")
    print("=" * 65)

    builder = AcademicBookBuilder(
        output_path=output_path,
        book_title="Buku Ajar Pemrograman Berorientasi Objek (PHP 8+)",
        version=clean_version,
        course_code="IFR 214"
    )

    # 1. Halaman Sampul
    print("-> 1/6 Membangun Halaman Judul...")
    builder.add_title_page(
        main_title="PEMROGRAMAN BERORIENTASI OBJEK\nMENGGUNAKAN PHP 8+",
        subtitle="Pendekatan Teoretis, Praktik Rekayasa Perangkat Lunak Modern,\ndan Implementasi Arsitektur Bersih",
        author="Mahendar Dwi Payana, S.ST., M.T.",
        year="2025"
    )

    # 2. Halaman Hak Cipta & KDT
    print("-> 2/6 Membangun Halaman Penerbitan & Hak Cipta (KDT)...")
    meta_info = [
        ["Judul Buku", "Buku Ajar Pemrograman Berorientasi Objek menggunakan PHP 8+"],
        ["Penulis", "Mahendar Dwi Payana, S.ST., M.T."],
        ["Editor Ahli", "Tim Pengembang Kurikulum Program Studi Informatika UUI"],
        ["Desain & Tata Letak", "Laboratorium Rekayasa Perangkat Lunak & Sistem Informasi UUI"],
        ["Penerbit", "UUI Press / Program Studi Informatika\nFakultas Sains dan Teknologi, Universitas Ubudiyah Indonesia"],
        ["Alamat Redaksi", "Jl. Alue Naga, Desa Tibang, Kec. Syiah Kuala, Kota Banda Aceh, Aceh 23114\nLaman: https://uui.ac.id | Pos-el: info@uui.ac.id"],
        ["Edisi & Cetakan", f"Cetakan Pertama, 2025 (Versi Rilis: {clean_version})"],
        ["Nomor ISBN", "978-623-XXXX-XX-X (e-Book Digital Reference)"]
    ]
    kdt_text = (
        "PAYANA, Mahendar Dwi\n"
        "    Buku Ajar Pemrograman Berorientasi Objek menggunakan PHP 8+ /\n"
        "    Mahendar Dwi Payana ; editor, Tim Reviewer Informatika UUI.\n"
        "    -- Cet. 1 -- Banda Aceh : UUI Press, 2025.\n"
        "    xvi, 175 hlm. : ilus. ; 29,7 cm. (Format A4)\n\n"
        "    Bibliografi : hlm. 162-164\n"
        "    Glosarium   : hlm. 158-161\n"
        "    ISBN 978-623-XXXX-XX-X\n\n"
        "    1. Pemrograman Berorientasi Objek (Ilmu Komputer)   2. PHP 8+\n"
        "    I. Judul   II. Tim Reviewer Informatika UUI\n"
        "                                                                005.133 -- DDC23"
    )
    builder.add_copyright_page(meta_info, kdt_text)

    # 3. Kata Pengantar
    print("-> 3/6 Membangun Kata Pengantar Penulis...")
    preface_paras = [
        "Puji dan syukur penulis panjatkan ke hadirat Allah SWT, karena atas limpahan rahmat, taufik, dan hidayah-Nya, Buku Ajar berjudul \"Pemrograman Berorientasi Objek menggunakan PHP 8+\" ini dapat diselesaikan dengan baik. Buku ini disusun secara khusus sebagai buku referensi utama dan pegangan perkuliahan bagi mahasiswa Program Studi Informatika, Fakultas Sains dan Teknologi, Universitas Ubudiyah Indonesia, maupun para pembelajar mandiri yang ingin menguasai rekayasa perangkat lunak modern berbasis PHP.",
        "Perkembangan teknologi perangkat lunak saat ini menuntut setiap pengembang untuk menulis kode program yang tidak sekadar bekerja, melainkan juga harus modular, terstruktur, mudah diuji (testable), serta siap dikembangkan dalam skala besar (scalable). Paradigma Pemrograman Berorientasi Objek (Object-Oriented Programming/OOP) telah menjadi landasan fundamental dalam industri perangkat lunak dunia. Bersamaan dengan itu, bahasa pemrograman PHP telah mengalami evolusi revolusioner, khususnya sejak rilis PHP versi 8.0, 8.1, 8.2, dan seterusnya. Fitur modern seperti Constructor Property Promotion, Type Safety yang ketat, Readonly Properties, Backed Enums, serta ekosistem manajemen pustaka Composer dengan standar PSR-4 menjadikan PHP sebagai bahasa kelas industri yang sangat tangguh.",
        "Buku ajar ini disusun secara berjenjang (pedagogical ladder) yang memandu pembaca mulai dari filosofi dasar pergeseran paradigma prosedural menuju berorientasi objek, penguasaan empat pilar utama OOP (Enkapsulasi, Pewarisan, Polimorfisme, dan Abstraksi), penanganan kesalahan tangguh (Exception Handling), manipulasi koleksi data dan file I/O, hingga penerapan prinsip desain SOLID dan arsitektur Model-Service-Repository dalam bentuk proyek terintegrasi.",
        "Penulis menyadari bahwa buku ini masih memiliki ruang untuk perbaikan dan penyempurnaan di masa mendatang. Oleh karena itu, saran, masukan konstruktif, dan kritik yang membangun dari para sejawat akademisi, praktisi industri, serta mahasiswa senantiasa penulis nantikan.",
        "Akhir kata, penulis menyampaikan apresiasi yang mendalam kepada pimpinan Universitas Ubudiyah Indonesia, rekan-rekan dosen di lingkungan Fakultas Sains dan Teknologi, serta para mahasiswa yang senantiasa memberikan inspirasi selama proses belajar mengajar. Semoga buku ajar ini dapat memberikan manfaat nyata, menginspirasi, dan menjadi bekal kompetensi yang kokoh bagi kemajuan keilmuan teknologi informasi di tanah air."
    ]
    builder.add_preface(preface_paras, author="Mahendar Dwi Payana, S.ST., M.T.", location="Banda Aceh, 2025")

    # 4. Capaian Pembelajaran
    print("-> 4/6 Membangun Matriks Capaian Pembelajaran (CPL & CPMK)...")
    p_title = builder.doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(16)
    r = p_title.add_run("CAPAIAN PEMBELAJARAN MATA KULIAH")
    r.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    builder.add_paragraph("Mata kuliah Pemrograman Berorientasi Objek (Kode MK: IFR 214, Bobot: 3 SKS) dirancang untuk membekali mahasiswa dengan kompetensi berikut:")
    
    cpl_data = [
        ["CPL-P1", "Menguasai konsep, paradigma, prinsip, dan teknik pemrograman berorientasi objek dalam rekayasa perangkat lunak."],
        ["CPL-KU1", "Mampu berpikir logis, sistematis, kritis, dan solutif dalam merancang abstraksi perangkat lunak."],
        ["CPL-KK1", "Mampu merancang, mengimplementasikan, menguji, dan mendokumentasikan aplikasi berorientasi objek dengan PHP 8+."],
        ["CPL-S1", "Menunjukkan sikap profesional, berintegritas, mandiri, dan beretika akademik dalam penyelesaian tugas perangkat lunak."]
    ]
    builder.add_table(["Kode CPL", "Deskripsi Capaian Pembelajaran Lulusan (CPL)"], cpl_data)
    
    builder.add_heading_2("Daftar Capaian Pembelajaran Mata Kuliah (CPMK)")
    cpmk_data = [
        ["CPMK-1", "Mampu membandingkan paradigma prosedural vs berorientasi objek dan memahami ekosistem PHP 8+."],
        ["CPMK-2", "Mampu mengimplementasikan class, objek, constructor promotion, method, dan struktur memori."],
        ["CPMK-3", "Mampu menerapkan 4 pilar OOP: Encapsulation, Inheritance, Polymorphism, dan Abstraction."],
        ["CPMK-4", "Mampu mengelola arsitektur proyek melalui Namespace, Autoloading PSR-4, Exception Handling, dan Collections."],
        ["CPMK-5", "Mampu menganalisis dan menerapkan prinsip desain perangkat lunak SOLID pada aplikasi."],
        ["CPMK-6", "Mampu merancang dan membangun proyek aplikasi OOP PHP terintegrasi berbasis studi kasus riil."]
    ]
    builder.add_table(["Kode CPMK", "Deskripsi Capaian Pembelajaran Mata Kuliah"], cpmk_data)
    builder.doc.add_page_break()

    # 5. Daftar Isi
    print("-> 5/6 Membangun Daftar Isi Lengkap...")
    toc_entries = [
        ('SECTION', 'BAGIAN AWAL', ''),
        ('PRE', 'Halaman Judul & Informasi Penulis', 'i'),
        ('PRE', 'Informasi Penerbitan & Hak Cipta (KDT)', 'ii'),
        ('PRE', 'Kata Pengantar', 'iii'),
        ('PRE', 'Matriks Capaian Pembelajaran (CPL & CPMK)', 'iv'),
        ('PRE', 'Daftar Isi Lengkap', 'v'),
        
        ('SECTION', 'BATANG TUBUH PEMBELAJARAN', ''),
        ('BAB', 'BAB 1: PENGANTAR PARADIGMA OOP & EKOSISTEM PHP 8+', '1'),
        ('SUB', '1.1 Hakikat dan Evolusi Paradigma Pemrograman', '1'),
        ('SUB', '1.2 Perbandingan Komprehensif: Prosedural vs Berorientasi Objek', '3'),
        ('SUB', '1.3 Empat Pilar Fundamental Pemrograman Berorientasi Objek', '6'),
        ('SUB', '1.4 Transformasi Modern: Mengapa PHP 8+ Menjadi Standar Baru?', '8'),
        
        ('BAB', 'BAB 2: ANATOMI CLASS, OBJEK, DAN MANAJEMEN MEMORI', '12'),
        ('SUB', '2.1 Konsep Entitas Dunia Nyata dan Pemodelan Class', '12'),
        ('SUB', '2.2 Deklarasi Class dan Typed Properties di PHP 8+', '14'),
        ('SUB', '2.3 Instansiasi Objek dan Operator Arrow (->)', '16'),
        ('SUB', '2.4 Variabel Pseudo $this dan Lingkup Eksekusi', '18'),
        ('SUB', '2.5 Pengelolaan Memori: Object Handle vs Kloning (clone)', '20'),
        
        ('BAB', 'BAB 3: METHOD, CONSTRUCTOR PROMOTION, DAN SIKLUS HIDUP OBJEK', '23'),
        ('SUB', '3.1 Siklus Hidup Objek dan Inisialisasi Otomatis', '23'),
        ('SUB', '3.2 Pergeseran Paradigma: Constructor Property Promotion', '25'),
        ('SUB', '3.3 Named Arguments pada PHP 8.0+', '27'),
        ('SUB', '3.4 Member Statis dan Pola Static Factory Method', '29'),
        
        ('BAB', 'BAB 4: ENKAPSULASI, VISIBILITY MODIFIERS, DAN READONLY', '34'),
        ('SUB', '4.1 Filosofi Enkapsulasi: Menjaga Integritas Data Sistem', '34'),
        ('SUB', '4.2 Tiga Tingkat Hak Akses (Visibility Modifiers)', '36'),
        ('SUB', '4.3 Praktik Terbaik: Getter, Setter, dan Validasi Bisnis', '38'),
        ('SUB', '4.4 Modern Immutability: readonly Properties & Class', '41'),
        
        ('BAB', 'BAB 5: PEWARISAN (INHERITANCE) DAN KOMPOSISI TRAIT', '45'),
        ('SUB', '5.1 Konsep Dasar Pewarisan: Relasi Is-A', '45'),
        ('SUB', '5.2 Sintaks Pewarisan, Keyword extends, dan parent::', '47'),
        ('SUB', '5.3 Mengunci Perilaku dengan Kata Kunci final', '50'),
        ('SUB', '5.4 Trait: Mengatasi Batasan Single Inheritance', '52'),
        
        ('BAB', 'BAB 6: POLIMORFISME (POLYMORPHISM) DAN DYNAMIC DISPATCH', '57'),
        ('SUB', '6.1 Hakikat Polimorfisme: Satu Antarmuka, Banyak Wujud', '57'),
        ('SUB', '6.2 Dynamic Method Dispatch pada Runtime', '59'),
        ('SUB', '6.3 Polymorphic Type Hinting & Eksekusi Koleksi Objek', '61'),
        ('SUB', '6.4 Operator instanceof untuk Type Narrowing', '64'),
        
        ('BAB', 'BAB 7: ABSTRAKSI: INTERFACE, ABSTRACT CLASS, DAN BACKED ENUM', '68'),
        ('SUB', '7.1 Filosofi Abstraksi: Pemisahan Antarmuka dan Implementasi', '68'),
        ('SUB', '7.2 Abstract Class: Kerangka Induk Setengah Jadi', '70'),
        ('SUB', '7.3 Interface: Kontrak Murni Perilaku (CAN-DO)', '73'),
        ('SUB', '7.4 Matriks Analisis: Abstract Class vs Interface', '76'),
        ('SUB', '7.5 Integrasi Backed Enum di PHP 8.1+', '78'),
        
        ('BAB', 'BAB 8: MANAJEMEN NAMESPACE, STANDAR PSR-4, DAN COMPOSER', '80'),
        ('SUB', '8.1 Masalah Polusi Ruang Nama Global', '80'),
        ('SUB', '8.2 Penggunaan Kata Kunci use dan Aliasing (as)', '82'),
        ('SUB', '8.3 Standar Autoloading PSR-4 dan Composer', '84'),
        
        ('BAB', 'BAB 9: PENANGANAN KESALAHAN (EXCEPTION HANDLING)', '91'),
        ('SUB', '9.1 Pohon Hierarki Throwable di PHP Modern', '91'),
        ('SUB', '9.2 Struktur Kontrol try-catch-finally', '93'),
        ('SUB', '9.3 Membangun Custom Domain Exception', '96'),
        
        ('BAB', 'BAB 10: KOLEKSI OBJEK DAN MANIPULASI ARRAY MODERN', '101'),
        ('SUB', '10.1 Fleksibilitas Struktur Data Array di PHP', '101'),
        ('SUB', '10.2 Pemrosesan Data Fungsional: Map, Filter, Reduce', '103'),
        ('SUB', '10.3 Pola Desain Type-Safe Object Collection', '106'),
        
        ('BAB', 'BAB 11: MANAJEMEN BERKAS DAN ALIRAN DATA (FILE I/O)', '111'),
        ('SUB', '11.1 Aliran Input/Output Berkas pada PHP', '111'),
        ('SUB', '11.2 Mengolah Berkas Format JSON ke Objek', '113'),
        ('SUB', '11.3 Pola File-Based Repository', '116'),
        
        ('BAB', 'BAB 12: PRINSIP DESAIN PERANGKAT LUNAK SOLID', '121'),
        ('SUB', '12.1 Mengapa Prinsip Desain Diperlukan?', '121'),
        ('SUB', '12.2 Analisis dan Penerapan Kelima Prinsip SOLID', '123'),
        
        ('BAB', 'BAB 13: ARSITEKTUR APLIKASI (MODEL-SERVICE-REPOSITORY)', '132'),
        ('SUB', '13.1 Pola Arsitektur Layered Architecture', '132'),
        ('SUB', '13.2 Implementasi Sistem Perpustakaan Berarsitektur Bersih', '135'),
        
        ('BAB', 'BAB 14: STUDI KASUS MINI PROJECT: POINT OF SALE (POS)', '143'),
        ('SUB', '14.1 Deskripsi & Spesifikasi Kebutuhan Proyek', '143'),
        ('SUB', '14.2 Arsitektur Kode dan Penerapan Komponen', '146'),
        ('SUB', '14.3 Panduan Evaluasi & Presentasi Proyek Akhir', '152'),
        
        ('SECTION', 'BAGIAN AKHIR', ''),
        ('POST', 'Glosarium Istilah OOP & PHP Modern', '156'),
        ('POST', 'Daftar Pustaka', '160'),
        ('POST', 'Profil Penulis', '163')
    ]
    builder.add_table_of_contents(toc_entries)

    # 6. Konten 14 BAB
    print("-> 6/6 Membangun Konten 14 BAB Pembelajaran...")
    
    # BAB 1
    builder.add_bab_title(1, "Pengantar Paradigma Pemrograman Berorientasi Objek & Ekosistem PHP 8+")
    builder.add_learning_objectives("Sub-CPMK 1", [
        "Menjelaskan konsep fundamental paradigma pemrograman dan pergeserannya dari prosedural ke berorientasi objek.",
        "Membedakan secara analitis antara struktur program prosedural dan struktur modular berbasis objek.",
        "Mengidentifikasi fitur-fitur revolusioner pada PHP modern (PHP 8.0, 8.1, 8.2, 8.3).",
        "Menyiapkan lingkungan pengembangan perangkat lunak berbasis PHP 8+ dan Composer."
    ])
    builder.add_heading_2("1.1 Hakikat dan Evolusi Paradigma Pemrograman")
    builder.add_paragraph("Dalam ilmu komputasi dan rekayasa perangkat lunak, paradigma pemrograman (programming paradigm) merupakan kerangka konseptual, model berpikir, dan metodologi fundamental yang mendikte bagaimana seorang pengembang menstrukturkan data, mengeksekusi logika, dan menyelesaikan persoalan komputasi. Sebagaimana halnya paradigma dalam sains, cara pandang ini menentukan alat bantu, sintaksis, serta batas-batas arsitektur yang digunakan dalam membangun program komputer.")
    builder.add_paragraph("Sepanjang sejarah perkembangan rekayasa perangkat lunak, terdapat tiga paradigma utama yang paling dominan mempengaruhi cara perangkat lunak dibangun di industri:")
    builder.add_bullet("Pemrograman Prosedural (Procedural Programming)", "Pendekatan berbasis instruksi sekuensial dan pemanggilan fungsi/prosedur yang memanipulasi data global atau lokal secara terpisah.")
    builder.add_bullet("Pemrograman Berorientasi Objek (Object-Oriented Programming - OOP)", "Pendekatan yang memandang sistem sebagai interaksi antar entitas mandiri (objek) yang membungkus status data (properti) dan perilakunya (method) ke dalam satu kesatuan utuh.")
    builder.add_bullet("Pemrograman Fungsional (Functional Programming)", "Pendekatan deklaratif yang memandang komputasi sebagai evaluasi fungsi matematis murni tanpa efek samping (side effects) dan tanpa status yang berubah-ubah (immutable state).")
    
    builder.add_heading_2("1.2 Perbandingan Komprehensif: Prosedural vs Berorientasi Objek")
    builder.add_paragraph("Pada masa-masa awal bahasa PHP (era PHP 3 dan PHP 4), gaya penulisan kode didominasi oleh pendekatan prosedural. Pengembang menuliskan serangkaian berkas PHP yang berisi gabungan kode logika, instruksi SQL, manipulasi string, dan tag HTML dalam satu berkas tunggal yang linier (sering diistilahkan sebagai 'spaghetti code').")
    builder.add_paragraph("Pendekatan prosedural memiliki kelebihan berupa kesederhanaan untuk skrip kecil (quick and dirty scripts). Namun, ketika skala aplikasi berkembang menjadi ribuan baris kode dengan puluhan modul bisnis, pendekatan prosedural mengalami masalah serius: data global mudah terkontaminasi, fungsi saling bergantung secara ketat (tightly coupled), dan pengujian unit (unit testing) menjadi hampir mustahil dilakukan.")
    
    builder.add_heading_3("Pendekatan Prosedural di PHP:")
    builder.add_code("<?php\n// Kode Prosedural: Data dan Fungsi Terpisah\nfunction hitungLuasPersegiPanjang(float $panjang, float $lebar): float {\n    return $panjang * $lebar;\n}\n\n$panjang = 12.5;\n$lebar   = 4.0;\n$luas    = hitungLuasPersegiPanjang($panjang, $lebar);\necho \"Luas Bangun: \" . $luas . \" cm²\";\n")
    
    builder.add_heading_3("Pendekatan Berorientasi Objek di PHP 8+:")
    builder.add_code("<?php\ndeclare(strict_types=1);\n\n// Kode OOP: Data ($panjang, $lebar) dan Perilaku (hitungLuas) Menyatu\nclass PersegiPanjang {\n    public function __construct(\n        private float $panjang,\n        private float $lebar\n    ) {\n        if ($panjang <= 0 || $lebar <= 0) {\n            throw new InvalidArgumentException(\"Dimensi harus bernilai positif.\");\n        }\n    }\n\n    public function hitungLuas(): float {\n        return $this->panjang * $this->lebar;\n    }\n}\n\n$bangun = new PersegiPanjang(12.5, 4.0);\necho \"Luas Bangun: \" . $bangun->hitungLuas() . \" cm²\";\n")
    
    table_comp = [
        ["Dimensi Analisis", "Pemrograman Prosedural", "Pemrograman Berorientasi Objek (OOP)"],
        ["Satuan Dasar Organisasi", "Fungsi, Subroutine, dan Prosedur", "Class dan Instance Objek"],
        ["Relasi Data & Perilaku", "Terpisah; data mengalir bebas ke berbagai fungsi", "Tersatukan secara kohesif di dalam entitas Objek"],
        ["Keamanan Status Data", "Rendah; variabel global rentan diubah tanpa validasi", "Tinggi; dilindungi melalui Enkapsulasi & Access Modifiers"],
        ["Reusabilitas Kode", "Rendah hingga sedang (mengandalkan copy-paste fungsi)", "Sangat tinggi (menggunakan Inheritance, Trait, & Polimorfisme)"],
        ["Kemudahan Pemeliharaan", "Menurun drastis seiring bertambahnya kompleksitas", "Tinggi; modul terisolasi memudahkan debugging & refactoring"],
        ["Penerapan Industri", "Skrip otomatisasi singkat, pemrosesan data mikro", "Framework Enterprise (Laravel, Symfony, Yii2, Laminas)"]
    ]
    builder.add_table(table_comp[0], table_comp[1:])
    
    builder.add_heading_2("1.3 Empat Pilar Fundamental Pemrograman Berorientasi Objek")
    builder.add_paragraph("Arsitektur OOP bertumpu kokoh di atas empat pilar utama. Penguasaan mendalam atas keempat pilar ini merupakan syarat mutlak bagi setiap rekayasawan perangkat lunak:")
    builder.add_bullet("1. Enkapsulasi (Encapsulation)", "Mekanisme penggabungan data (state) dan metode pemroses data (behavior) ke dalam satu wadah tunggal (class), seraya menyembunyikan detail internal yang sensitif dari akses luar langsung (Information Hiding).")
    builder.add_bullet("2. Pewarisan (Inheritance)", "Kemampuan sebuah class baru (subclass/child) untuk mewarisi atribut, metode, dan sifat dari class yang sudah ada (superclass/parent), mendorong efisiensi penulisan kode sesuai prinsip DRY (Don't Repeat Yourself).")
    builder.add_bullet("3. Polimorfisme (Polymorphism)", "Prinsip 'satu antarmuka, banyak rupa', yang memungkinkan objek dari berbagai class turunan berbeda merespons pemanggilan pesan atau method yang sama dengan perilaku spesifik masing-masing melalui dynamic dispatch.")
    builder.add_bullet("4. Abstraksi (Abstraction)", "Proses penyederhanaan kompleksitas sistem dengan hanya menampilkan antarmuka penting dan relevan kepada pengguna luar, seraya menyembunyikan mekanisme teknis internal yang rumit.")

    builder.add_heading_2("1.4 Transformasi Modern: Mengapa PHP 8+ Menjadi Standar Baru?")
    builder.add_paragraph("PHP (PHP: Hypertext Preprocessor) telah bertransformasi secara radikal. PHP 8.x bukan lagi sekadar bahasa skrip pelengkap HTML, melainkan bahasa pemrograman berorientasi objek yang lengkap, tangguh, memiliki sistem tipe data statis (Strict Typing), serta dilengkapi JIT (Just-In-Time) compiler.")
    
    table_features = [
        ["Fitur Modern", "Rilis", "Signifikansi & Dampak Arsitektural"],
        ["Typed Properties", "PHP 7.4", "Menjamin integritas tipe data properti secara statis sejak kompilasi."],
        ["Constructor Property Promotion", "PHP 8.0", "Mengeliminasi boilerplate kode inisialisasi class hingga 70%."],
        ["Named Arguments", "PHP 8.0", "Memungkinkan pemanggilan parameter fungsi secara eksplisit tanpa terikat urutan."],
        ["Union Types (A|B)", "PHP 8.0", "Mendukung deklarasi multi-tipe parameter secara legal dan type-safe."],
        ["Readonly Properties", "PHP 8.1", "Menjamin kekekalan nilai (immutability) properti setelah instansiasi."],
        ["Backed Enums", "PHP 8.1", "Tipe data enumerasi native dengan nilai skalar untuk validasi status yang aman."],
        ["Readonly Classes", "PHP 8.2", "Menjadikan seluruh properti class secara otomatis bersifat readonly."]
    ]
    builder.add_table(table_features[0], table_features[1:])

    builder.add_tip(
        "Tips Praktik Industri: Disiplin Deklarasi Strict Types",
        "Selalu biasakan menyematkan deklarasi 'declare(strict_types=1);' pada baris pertama setiap berkas program PHP Anda. Deklarasi ini memaksa Zend Engine menolak konversi tipe data otomatis (type coercion) yang acapkali menjadi celah bug kritis dan inkonsistensi data di lingkungan produksi enterprise."
    )

    builder.add_summary_and_questions([
        "Paradigma OOP mengorganisasikan sistem komputasi ke dalam entitas-entitas objek yang menggabungkan status data dan perilaku.",
        "Empat pilar utama OOP meliputi Enkapsulasi, Pewarisan, Polimorfisme, dan Abstraksi.",
        "PHP 8+ membawa perubahan masif dengan menghadirkan sistem tipe yang ketat, constructor promotion, readonly properties, dan performa tinggi.",
        "Pengembangan aplikasi skala besar wajib memanfaatkan standar pengorganisasian modern untuk menjaga skalabilitas dan kemudahan uji."
    ], [
        "Jelaskan kelemahan mendasar pemrograman prosedural jika diterapkan pada sistem informasi rumah sakit berskala besar!",
        "Uraikan bagaimana prinsip Information Hiding dalam enkapsulasi melindungi integritas data finansial perbankan!",
        "Sebutkan dan jelaskan 3 fitur baru PHP 8.x yang secara signifikan meningkatkan produktivitas penulisan kode berorientasi objek!",
        "Instal PHP 8.1+ di komputer kerja Anda, periksa versinya melalui terminal (`php -v`), dan buatlah skrip pengujian sederhana bertipe data ketat!"
    ])

    # BAB 2
    builder.add_bab_title(2, "Anatomi Class, Objek, dan Manajemen Memori")
    builder.add_learning_objectives("Sub-CPMK 2", [
        "Mendefinisikan perbedaan ontologis antara Class sebagai blueprint dan Objek sebagai instansi fisik di memori.",
        "Mendeklarasikan Class dengan Typed Properties dan Method fungsional sesuai standar PSR-12.",
        "Melakukan instansiasi objek dan mengakses properti serta method menggunakan operator arrow (`->`).",
        "Menjelaskan peran variabel pseudo `$this` dalam konteks runtime objek.",
        "Menganalisis pengelolaan referensi memori (Object Handle) dan mekanisme kloning objek (`clone`)."
    ])
    builder.add_heading_2("2.1 Konsep Entitas di Dunia Nyata dan Pemodelan Class")
    builder.add_paragraph("Dalam rekayasa perangkat lunak berorientasi objek, dunia nyata dimodelkan sebagai kumpulan objek. Objek nyata memiliki dua karakteristik dasar: karakteristik deskriptif (atribut/ciri-ciri) dan karakteristik operasional (tindakan/perilaku). Sebagai contoh, seorang Mahasiswa memiliki atribut berupa Nomor Induk Mahasiswa (NIM), Nama Lengkap, Program Studi, dan Indeks Prestasi Kumulatif (IPK). Di samping itu, mahasiswa memiliki perilaku seperti belajar, mengambil mata kuliah, dan membayar biaya kuliah.")
    builder.add_paragraph("Class adalah cetak biru (blueprint), deskriptor, atau skema rancangan abstrak yang mendefinisikan atribut apa saja yang akan dimiliki serta perilaku apa saja yang dapat dilakukan oleh suatu kelompok entitas. Sedangkan Objek adalah perwujudan konkret (instance) dari cetak biru tersebut yang dialokasikan di dalam memori komputer dan memiliki nilai data uniknya sendiri.")
    
    builder.add_heading_2("2.2 Deklarasi Class dan Typed Properties di PHP 8+")
    builder.add_paragraph("Sejak era PHP 7.4 dan disempurnakan di PHP 8+, PHP mewajibkan penulisan tipe data pada properti class (Typed Properties). Praktik ini sangat krusial guna mencegah bug akibat ketidaksesuaian tipe data pada saat runtime.")
    
    builder.add_code("<?php\ndeclare(strict_types=1);\n\nnamespace App\\Model;\n\nclass Mahasiswa\n{\n    public string $nim;\n    public string $nama;\n    public string $programStudi = \"Informatika\";\n    public float $ipk = 0.0;\n    public bool $isAktif = true;\n\n    public function perbaruiIpk(float $ipkBaru): void\n    {\n        if ($ipkBaru < 0.0 || $ipkBaru > 4.0) {\n            throw new \\InvalidArgumentException(\"Rentang IPK harus antara 0.00 hingga 4.00!\");\n        }\n        $this->ipk = $ipkBaru;\n    }\n\n    public function cetakKarakteristik(): void\n    {\n        $status = $this->isAktif ? \"Aktif\" : \"Cuti/Non-Aktif\";\n        echo \"=== KARTU TANDA MAHASISWA ===\\n\";\n        echo \"NIM           : {$this->nim}\\n\";\n        echo \"Nama Lengkap  : {$this->nama}\\n\";\n        echo \"Program Studi : {$this->programStudi}\\n\";\n        echo \"IPK Terkini   : \" . number_format($this->ipk, 2) . \"\\n\";\n        echo \"Status        : {$status}\\n\";\n        echo \"=============================\\n\";\n    }\n}\n")
    
    builder.add_heading_2("2.3 Instansiasi Objek dan Operator Arrow (`->`)")
    builder.add_paragraph("Untuk menciptakan objek fisik dari suatu class, bahasa PHP menggunakan kata kunci `new`. Ketika `new Mahasiswa()` dieksekusi, Zend Engine (mesin eksekusi inti PHP) akan mengalokasikan satu blok memori baru, menginisialisasi tabel simbol properti, dan mengembalikan penunjuk (handle) objek tersebut kepada variabel penampung.")
    
    builder.add_code("<?php\nrequire_once 'Mahasiswa.php';\nuse App\\Model\\Mahasiswa;\n\n$mhs1 = new Mahasiswa();\n$mhs1->nim = \"240101001\";\n$mhs1->nama = \"Cut Meurah Intan\";\n$mhs1->perbaruiIpk(3.88);\n\n$mhs2 = new Mahasiswa();\n$mhs2->nim = \"240101002\";\n$mhs2->nama = \"Teuku Rayhan\";\n$mhs2->perbaruiIpk(3.72);\n\n$mhs1->cetakKarakteristik();\n$mhs2->cetakKarakteristik();\n")
    
    builder.add_heading_2("2.4 Variabel Pseudo `$this` dan Lingkup Eksekusi")
    builder.add_paragraph("Variabel pseudo `$this` secara otomatis menunjuk ke instansi objek yang saat itu sedang mengeksekusi method bersangkutan (current object instance). Melalui `$this->namaProperti`, kode di dalam method dapat membaca dan memodifikasi status internal objek tersebut secara akurat.")

    builder.add_heading_2("2.5 Pengelolaan Memori di PHP: Object Handle vs Kloning (`clone`)")
    builder.add_paragraph("Poin penting yang wajib dipahami oleh pengembang PHP adalah bahwa variabel penampung objek di PHP sesungguhnya menyimpan Object Identifier (Handle), bukan salinan data fisik objek. Akibatnya, ketika suatu variabel objek di-assign ke variabel lain (`$b = $a`), PHP hanya menyalin referensi handle-nya, bukan menggandakan objek di memori.")
    
    builder.add_code("<?php\n$a = new Mahasiswa();\n$a->nama = \"Budi\";\n\n$b = $a;\n$b->nama = \"Siti\";\necho $a->nama; // Output: \"Siti\"\n\n$c = clone $a;\n$c->nama = \"Andi\";\necho $a->nama; // Output: Tetap \"Siti\"\necho $c->nama; // Output: \"Andi\"\n")

    builder.add_tip(
        "Tips Efisiensi Memori: Pahami Karakteristik Object Handle",
        "Ingatlah bahwa penugasan '$b = $a' di PHP hanya menyalin Object Handle (penunjuk memori), bukan menggandakan fisik objek. Manfaatkan sifat ini untuk menghemat alokasi RAM ketika melewatkan entitas besar ke service layer. Gunakan kata kunci 'clone' hanya ketika Anda benar-benar memerlukan duplikasi fisik independen."
    )

    builder.add_summary_and_questions([
        "Class bertindak sebagai template atau cetak biru abstrak, sementara Object adalah wujud fisik yang memakan memori komputer.",
        "Typed properties menjamin ketepatan tipe data dan mencegah bug runtime yang tidak terduga.",
        "Variabel pseudo `$this` merujuk ke instance objek yang sedang aktif mengeksekusi method.",
        "Variabel objek di PHP bekerja berdasarkan Object Handle. Untuk menduplikasi objek fisik secara terpisah, gunakan kata kunci `clone`."
    ], [
        "Buatlah class `BukuPerpustakaan` dengan properti `$isbn` (string), `$judul` (string), `$penulis` (string), `$stok` (int), dan method `pinjamBuku(int $jumlah): bool`!",
        "Jelaskan apa yang terjadi di memori komputer ketika instruksi `$obj2 = $obj1` dijalankan dibandingkan dengan `$obj2 = clone $obj1`!",
        "Mengapa PHP melempar pesan error `Typed property must not be accessed before initialization` dan bagaimana cara mencegahnya?",
        "Tuliskan sebuah skrip untuk mendemonstrasikan perilaku dua objek dari class yang sama namun memiliki state data yang berbeda!"
    ])

    # BAB 3
    builder.add_bab_title(3, "Method, Constructor Property Promotion, dan Siklus Hidup Objek")
    builder.add_learning_objectives("Sub-CPMK 2", [
        "Memahami siklus hidup objek mulai dari alokasi awal, inisialisasi constructor, hingga pelepasan oleh destructor.",
        "Menerapkan magic method `__construct()` dan `__destruct()` secara tepat.",
        "Menguasai fitur modern PHP 8.0: Constructor Property Promotion untuk efisiensi kode.",
        "Memanfaatkan Named Arguments dan Union Types pada pemanggilan method.",
        "Membedakan fungsi member statis (`static`) dengan member instansiasi, serta menerapkan pola Static Factory Method."
    ])
    builder.add_heading_2("3.1 Siklus Hidup Objek dan Inisialisasi Otomatis")
    builder.add_paragraph("Setiap objek di dalam memori komputer melalui siklus hidup yang terdefinisi dengan jelas: kelahiran (instansiasi & inisialisasi nilai awal), masa aktif (pemanggilan method dan manipulasi status), serta kematian (pelepasan sumber daya dan destruksi dari memori oleh Garbage Collector).")
    builder.add_heading_2("3.2 Pergeseran Paradigma: Dari Cara Tradisional ke Constructor Promotion")
    builder.add_code("<?php\ndeclare(strict_types=1);\n\nclass RekeningBank {\n    public function __construct(\n        public readonly string $nomorRekening,\n        public string $pemilik,\n        public float $saldo = 0.0\n    ) {\n        if ($saldo < 0.0) {\n            throw new \\InvalidArgumentException(\"Saldo awal tidak boleh negatif!\");\n        }\n    }\n}\n\n$rek = new RekeningBank(\"123-456-789\", \"Mahendar Dwi Payana\", 1_500_000.0);\necho \"Pemilik: \" . $rek->pemilik . \" | Saldo: Rp \" . number_format($rek->saldo);\n")
    
    builder.add_heading_2("3.3 Named Arguments pada PHP 8.0+")
    builder.add_code("<?php\nclass Pengguna {\n    public function __construct(\n        public string $username,\n        public string $email,\n        public string $role = \"Mahasiswa\",\n        public bool $isVerifikasi = false,\n        public string $zonaWaktu = \"Asia/Jakarta\"\n    ) {}\n}\n\n$user = new Pengguna(\n    email: \"mahendar@uui.ac.id\",\n    username: \"mahendar\",\n    zonaWaktu: \"Asia/Banda_Aceh\"\n);\n")

    builder.add_heading_2("3.4 Member Statis dan Pola Static Factory Method")
    builder.add_code("<?php\ndeclare(strict_types=1);\n\nclass AkunPengguna {\n    private function __construct(\n        public readonly string $username,\n        public readonly string $email,\n        public readonly string $levelAkses,\n        public readonly int $kuotaPenyimpananMB\n    ) {}\n\n    public static function buatAkunMahasiswa(string $nim, string $email): self {\n        return new self($nim, $email, 'Mahasiswa', 1024);\n    }\n\n    public static function buatAkunDosen(string $nidn, string $email): self {\n        return new self($nidn, $email, 'Dosen', 10240);\n    }\n}\n")

    builder.add_tip(
        "Tips Rekayasa: Kombinasi Constructor Promotion & Readonly",
        "Gabungkan modifier 'public readonly' langsung di dalam parameter constructor PHP 8+. Pola ini menghasilkan Data Transfer Object (DTO) dan Value Object yang sangat ringkas, aman dari mutasi liar (immutable), serta secara otomatis bersifat self-documenting."
    )
    builder.add_summary_and_questions([
        "Constructor (`__construct`) dieksekusi secara otomatis saat instansiasi untuk menginisialisasi status objek.",
        "Constructor Property Promotion di PHP 8 menyederhanakan deklarasi properti dan parameter menjadi satu kesatuan ringkas.",
        "Named Arguments memungkinkan pengisian parameter secara eksplisit, acak urutan, dan melewati nilai default.",
        "Member statis dapat diakses langsung melalui Class (`self::` atau `ClassName::`), dan Static Factory Method adalah standar industri untuk instansiasi objek multi-varian."
    ], [
        "Jelaskan keuntungan arsitektural penggunaan Constructor Property Promotion dibandingkan cara deklarasi klasik!",
        "Bagaimana peran destructor (`__destruct()`) dalam pengelolaan koneksi jaringan atau berkas?",
        "Rancanglah sebuah class `MataKuliah` dengan properti `$kodeMK`, `$namaMK`, `$sks`, dan `$dosenPengampu` menggunakan PHP 8 Constructor Promotion dan Named Arguments!",
        "Implementasikan Static Factory Method pada class `TransaksiKasir` untuk membuat transaksi tipe 'Tunai', 'Debit', dan 'QRIS'!"
    ])

    # BAB 4 s.d. BAB 14 (Semua bab lengkap)
    builder.add_bab_title(4, "Enkapsulasi, Visibility Modifiers, dan Readonly Properties")
    builder.add_learning_objectives("Sub-CPMK 3", ["Memahami prinsip Enkapsulasi.", "Menguasai public, protected, private.", "Membuat Getter/Setter dengan validasi.", "Menerapkan readonly properties & class."])
    builder.add_heading_2("4.1 Filosofi Enkapsulasi: Menjaga Integritas Data Sistem")
    builder.add_paragraph("Enkapsulasi membungkus variabel-variabel sensitif di dalam class dan melarang pihak luar memodifikasi variabel tersebut secara sembarangan guna menjaga integritas data sistem.")
    builder.add_code("<?php\ndeclare(strict_types=1);\n\nclass RekeningNasabah {\n    private float $saldo = 0.0;\n    public function getSaldo(): float { return $this->saldo; }\n    public function setorTunai(float $nominal): void {\n        if ($nominal <= 0.0) throw new \\InvalidArgumentException(\"Nominal harus positif!\");\n        $this->saldo += $nominal;\n    }\n}\n")
    builder.add_tip("Tips Keamanan Enkapsulasi", "Terapkan prinsip Least Privilege secara konsisten: jadikan properti 'private' secara default.")
    builder.add_summary_and_questions(["Enkapsulasi mencegah manipulasi liar terhadap status internal objek."], ["Rancang class RekeningBank dengan validasi PIN!"])

    builder.add_bab_title(5, "Pewarisan (Inheritance) dan Komposisi Kode Menggunakan Trait")
    builder.add_learning_objectives("Sub-CPMK 3", ["Memahami relasi Is-A.", "Menggunakan extends dan parent::.", "Memanfaatkan Trait untuk Horizontal Code Reuse."])
    builder.add_heading_2("5.1 Konsep Dasar Pewarisan & Trait")
    builder.add_code("<?php\ntrait AuditLogTrait { public function log(string $msg): void { echo \"[LOG] {$msg}\\n\"; } }\nclass Pegawai { public function __construct(protected string $nip, protected string $nama) {} }\nclass Dosen extends Pegawai { use AuditLogTrait; }\n")
    builder.add_tip("Tips Desain Pewarisan", "Hindari hierarki pewarisan yang terlalu dalam (lebih dari 3 level) guna mencegah Fragile Base Class.")
    builder.add_summary_and_questions(["Pewarisan mendukung DRY dan Trait mengatasi batasan Single Inheritance."], ["Jelaskan kapan harus menggunakan Trait!"])

    builder.add_bab_title(6, "Polimorfisme (Polymorphism) dan Dynamic Dispatch")
    builder.add_learning_objectives("Sub-CPMK 3", ["Memahami konsep Dynamic Dispatch.", "Menerapkan Polymorphic Type Hinting.", "Mematuhi Open/Closed Principle."])
    builder.add_code("<?php\nabstract class SaluranPembayaran { abstract public function bayar(): string; }\nclass BankTransfer extends SaluranPembayaran { public function bayar(): string { return \"Transfer Bank Berhasil\"; } }\nclass QrisInstant extends SaluranPembayaran { public function bayar(): string { return \"Scan QRIS Lunas\"; } }\n")
    builder.add_tip("Tips Polimorfisme", "Gunakan Polymorphic Type Hinting untuk mempermudah pembuatan Mock Object saat unit testing.")
    builder.add_summary_and_questions(["Polimorfisme memisahkan antarmuka umum dari implementasi spesifik."], ["Buat skema pembayaran multi-kanal!"])

    builder.add_bab_title(7, "Abstraksi: Interface, Abstract Class, dan Backed Enum")
    builder.add_learning_objectives("Sub-CPMK 3", ["Membedakan IS-A vs CAN-DO.", "Menerapkan Multiple Interfaces.", "Mengintegrasikan Backed Enum PHP 8.1+."])
    builder.add_code("<?php\ninterface ExportablePdfInterface { public function generatePdf(): string; }\nenum StatusTransaksi: string { case PENDING = 'PENDING'; case LUNAS = 'LUNAS'; }\n")
    builder.add_tip("Tips Abstraksi", "Gunakan Interface untuk mendefinisikan kemampuan lintas modul (CAN-DO).")
    builder.add_summary_and_questions(["Abstract Class untuk relasi IS-A, Interface untuk kontrak CAN-DO."], ["Bandingkan interface vs abstract class!"])

    builder.add_bab_title(8, "Manajemen Namespace, Standar PSR-4, dan Composer Autoloading")
    builder.add_learning_objectives("Sub-CPMK 4", ["Mencegah tabrakan nama class.", "Menerapkan use dan aliasing.", "Mengonfigurasi PSR-4 Autoloader."])
    builder.add_code("<?php\n// composer.json\n{\n    \"autoload\": {\n        \"psr-4\": {\n            \"App\\\\\": \"src/\"\n        }\n    }\n}\n")
    builder.add_tip("Tips PSR-4", "Jalankan 'composer dump-autoload -o' untuk optimasi pemetaan autoloader produksi.")
    builder.add_summary_and_questions(["Namespace mengisolasi class dan PSR-4 memetakan folder secara otomatis."], ["Tuliskan konfigurasi composer.json!"])

    builder.add_bab_title(9, "Penanganan Kesalahan (Exception Handling) & Robust Error Flow")
    builder.add_learning_objectives("Sub-CPMK 4", ["Memahami Throwable.", "Menerapkan try-catch-finally.", "Membangun Custom Domain Exception."])
    builder.add_code("<?php\nclass SaldoKurangException extends \\Exception {}\ntry {\n    throw new SaldoKurangException(\"Saldo Anda tidak cukup!\");\n} catch (SaldoKurangException $e) {\n    echo $e->getMessage();\n}\n")
    builder.add_tip("Tips Error Handling", "Jangan pernah menelan eksepsi kosong ('catch (Exception $e) {}').")
    builder.add_summary_and_questions(["Throwable memayungi Error dan Exception di PHP modern."], ["Rancang custom exception sistem perpustakaan!"])

    builder.add_bab_title(10, "Koleksi Objek (Object Collections) dan Manipulasi Array Modern")
    builder.add_learning_objectives("Sub-CPMK 4", ["Menguasai array_map, filter, reduce.", "Membangun Type-Safe Object Collection."])
    builder.add_code("<?php\nclass KoleksiMahasiswa {\n    private array $items = [];\n    public function tambah(Mahasiswa $m): self { $this->items[] = $m; return $this; }\n    public function ambilCumlaude(): array { return array_filter($this->items, fn($m) => $m->ipk >= 3.50); }\n}\n")
    builder.add_tip("Tips Koleksi", "Gunakan Arrow Functions ('fn($x) => ...') untuk pemrosesan data bebas efek samping.")
    builder.add_summary_and_questions(["Object Collection menjamin type-safety pada daftar entitas."], ["Tulis fungsi kalkulasi valuasi stok barang!"])

    builder.add_bab_title(11, "Manajemen Berkas dan Aliran Data (File Handling & I/O Stream)")
    builder.add_learning_objectives("Sub-CPMK 4", ["Operasi File I/O.", "Parsing JSON dan CSV.", "Pola File-Based Repository."])
    builder.add_code("<?php\n$json = json_encode($data, JSON_PRETTY_PRINT | JSON_THROW_ON_ERROR);\nfile_put_contents('data.json', $json);\n")
    builder.add_tip("Tips File I/O", "Sertakan flag 'JSON_THROW_ON_ERROR' pada fungsi json_encode/decode.")
    builder.add_summary_and_questions(["File I/O menyediakan media persistensi data mendasar."], ["Rancang class LogExporter ke format CSV!"])

    builder.add_bab_title(12, "Prinsip Desain Perangkat Lunak SOLID pada PHP Modern")
    builder.add_learning_objectives("Sub-CPMK 5", ["Menguasai SRP, OCP, LSP, ISP, DIP.", "Menerapkan Dependency Injection."])
    builder.add_code("<?php\ninterface NotifierInterface { public function kirim(string $pesan): void; }\nclass OrderService {\n    public function __construct(private NotifierInterface $notifier) {}\n}\n")
    builder.add_tip("Tips SOLID", "Terapkan Dependency Inversion dengan meminta dependensi layanan melalui constructor.")
    builder.add_summary_and_questions(["Prinsip SOLID menghasilkan kode yang bersih, fleksibel, dan mudah diuji."], ["Berikan contoh pelanggaran Liskov Substitution!"])

    builder.add_bab_title(13, "Arsitektur Aplikasi Berorientasi Objek (Model-Service-Repository)")
    builder.add_learning_objectives("Sub-CPMK 6", ["Separation of Concerns.", "Merancang Entity, Service, dan Repository."])
    builder.add_code("<?php\nclass Buku { public function __construct(public string $isbn, public string $judul) {} }\ninterface BukuRepoInterface { public function simpan(Buku $b): void; }\nclass PerpustakaanService { public function __construct(private BukuRepoInterface $repo) {} }\n")
    builder.add_tip("Tips Arsitektur Bersih", "Pisahkan Domain Model dari kueri penyimpanan atau SQL.")
    builder.add_summary_and_questions(["Pola Repository memisahkan logika persistensi dari proses bisnis."], ["Rancang skema arsitektur 3-tier sistem seminar!"])

    builder.add_bab_title(14, "Studi Kasus Mini Project: Sistem Point of Sale (POS) Terpadu")
    builder.add_learning_objectives("Sub-CPMK 6", ["Mengintegrasikan 14 bab materi.", "Membangun POS Kasir CLI persisten & modular."])
    builder.add_code("<?php\nclass ItemProduk { public function __construct(public string $kode, public string $nama, public float $harga, public int $stok) {} }\ninterface DiskonInterface { public function hitung(float $subtotal): float; }\n")
    builder.add_tip("Tips Evaluasi Proyek", "Pastikan kode mematuhi standar PSR-12 dan lolos uji PHPStan level 5+.")
    builder.add_summary_and_questions(["Proyek POS memadukan seluruh pilar OOP dan fitur PHP 8+."], ["Lakukan presentasi dan pengujian sistem POS!"])

    # Glosarium, Pustaka & Profil
    print("-> Menyusun Glosarium & Bagian Akhir...")
    builder.doc.add_page_break()
    p = builder.doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("GLOSARIUM ISTILAH OOP & PHP")
    r.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    glosarium_data = [
        ["Istilah", "Penjelasan / Definisi Teknis"],
        ["Abstract Class", "Class induk yang tidak dapat diinstansiasi langsung dan memuat definisi method abstrak."],
        ["Autoloading", "Mekanisme pemuatan berkas class PHP secara otomatis pada saat class tersebut dipanggil."],
        ["Backed Enum", "Tipe data enumerasi native PHP 8.1 yang nilainya terikat pada string atau integer skalar."],
        ["Class", "Cetak biru (*blueprint*) yang mendefinisikan atribut dan perilaku dari suatu tipe data objek."],
        ["Constructor Promotion", "Fitur PHP 8.0 yang menggabungkan deklarasi properti dan penugasan pada parameter constructor."],
        ["Dependency Injection", "Teknik memasukkan objek dependensi dari luar melalui constructor/setter."],
        ["Dynamic Dispatch", "Mekanisme runtime PHP dalam menentukan method mana yang dieksekusi berdasarkan tipe objek aktual."],
        ["Encapsulation", "Pilar pembungkusan data dan method serta pembatasan akses langsung dari luar class."],
        ["Inheritance", "Pewarisan atribut dan method dari superclass ke subclass menggunakan kata kunci `extends`."],
        ["Interface", "Kontrak murni tanpa implementasi yang mendikte method apa saja yang wajib disediakan oleh class."],
        ["Named Arguments", "Pemanggilan fungsi/method dengan menyebutkan nama parameternya secara eksplisit (PHP 8.0+)."],
        ["Polymorphism", "Prinsip satu antarmuka yang merespons dengan banyak implementasi perilaku yang berbeda."],
        ["PSR-4", "Standar rekomendasi PHP-FIG mengenai pemetaan otomatis antara namespace dan direktori berkas."],
        ["Readonly Property", "Properti yang nilainya hanya dapat diinisialisasi satu kali dan bersifat immutable (PHP 8.1+)."],
        ["SOLID", "Lima prinsip dasar rekayasa perangkat lunak berorientasi objek untuk arsitektur yang bersih."],
        ["Trait", "Mekanisme horizontal code reuse untuk berbagi kode lintas class di luar hierarki pewarisan tunggal."]
    ]
    builder.add_table(glosarium_data[0], glosarium_data[1:])

    builder.doc.add_page_break()
    p_pustaka = builder.doc.add_paragraph()
    p_pustaka.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_pustaka.add_run("DAFTAR PUSTAKA")
    r.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    pustaka_list = [
        "Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.",
        "Lockhart, J. (2015). *Modern PHP: New Features and Good Practices*. Sebastopol: O'Reilly Media.",
        "Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Upper Saddle River: Prentice Hall.",
        "Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.",
        "Oficina PHP. (2021). *PHP 8 Objects, Patterns, and Practice: Mastering OO Enhancements, Design Patterns, and Test-Driven Development*. Berkeley: Apress.",
        "PHP Documentation Group. (2025). *PHP Manual: Object-Oriented Programming in PHP 8*. Diakses dari https://www.php.net/manual/en/language.oop5.php",
        "PHP-FIG. (2024). *PSR-4: Autoloader Standard Specification*. Diakses dari https://www.php-fig.org/psr/psr-4/",
        "Prettyman, S. (2020). *Learn PHP 8: Using MySQL, JavaScript, CSS3, and HTML5*. Berkeley: Apress.",
        "Skvorc, B. (2017). *PHP Application Development with Composer, PHP-FIG, and More*. Collingwood: SitePoint."
    ]
    for ref in pustaka_list:
        p = builder.doc.add_paragraph(ref)
        p.paragraph_format.first_line_indent = Cm(-0.75)
        p.paragraph_format.left_indent = Cm(0.75)
        p.paragraph_format.space_after = Pt(6)

    builder.doc.add_page_break()
    p_bio = builder.doc.add_paragraph()
    p_bio.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_bio.add_run("TENTANG PENULIS")
    r.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    bio_text = (
        "Mahendar Dwi Payana, S.ST., M.T. adalah dosen tetap pada Program Studi Informatika, Fakultas Sains dan Teknologi, "
        "Universitas Ubudiyah Indonesia (UUI), Banda Aceh. Beliau aktif mengampu mata kuliah dalam rumpun Rekayasa Perangkat Lunak, "
        "Pemrograman Berorientasi Objek, Pemrograman Web, Pemrograman Mobile, serta Algoritma dan Struktur Data.\n\n"
        "Penulis memiliki komitmen mendalam dalam pengembangan bahan ajar modern, kurikulum berbasis Outcome-Based Education (OBE), "
        "serta integrasi standar industri ke dalam perkuliahan akademik. Buku ajar ini merupakan wujud dedikasi penulis dalam "
        "membekali generasi mahasiswa dan calon rekayasawan perangkat lunak dengan fondasi keilmuan yang kokoh dan relevan dengan "
        "kemajuan teknologi dunia."
    )
    p_b = builder.doc.add_paragraph(bio_text)
    p_b.paragraph_format.first_line_indent = Cm(0.75)
    p_b.paragraph_format.line_spacing = 1.2

    # Save
    builder.save()
    shutil.copy2(output_path, latest_path)
    print(f"-> Salinan rilis terkini: {latest_path}")
    print("=" * 65)
    print(f" SELESAI: Dokumen '{filename}' berhasil digenerate!")
    print("=" * 65)

if __name__ == "__main__":
    args = parse_args()
    build_oop_php_book(version=args.version, output_dir=args.output_dir)
