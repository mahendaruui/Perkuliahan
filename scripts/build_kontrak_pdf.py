#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pure Python PDF 1.4 Generator for Kontrak Kuliah OOP PHP 8+
Configured to 100% match Portal Siakad UUI evaluation components & grading scale.
"""

import os
import shutil

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "kontrak-kuliah"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
PDF_MAIN = os.path.join(OUTPUT_DIR, "Kontrak_Kuliah_OOP_PHP_IFR214_Mahendar_Dwi_Payana.pdf")
PDF_LATEST = os.path.join(OUTPUT_DIR, "Kontrak_Kuliah_OOP_PHP_IFR214_Latest.pdf")

class SimplePDF:
    def __init__(self):
        self.pages = []
        self.page_width = 595.28 # A4
        self.page_height = 841.89 # A4
        self.current_stream = []
        self.current_page_num = 0
        self.fonts = {"F1": "Helvetica", "F2": "Helvetica-Bold", "F3": "Helvetica-Oblique", "F4": "Times-Roman", "F5": "Times-Bold"}
        
    def new_page(self):
        if self.current_stream:
            self.pages.append(b"\n".join(self.current_stream))
            self.current_stream = []
        self.current_page_num += 1
        
        # Header line
        self.draw_line(40, 805, 555, 805, stroke_color=(0.8, 0.85, 0.9), width=0.5)
        self.draw_text("Universitas Ubudiyah Indonesia | Kontrak Perkuliahan PBO (IFR 214)", 40, 810, font="F3", size=8, color=(0.4, 0.45, 0.5))
        self.draw_text(f"Kelas A - Ganjil 2026", 470, 810, font="F3", size=8, color=(0.4, 0.45, 0.5))
        
        # Footer line
        self.draw_line(40, 40, 555, 40, stroke_color=(0.8, 0.85, 0.9), width=0.5)
        self.draw_text("Program Studi S1 Informatika - FST UUI", 40, 28, font="F3", size=8, color=(0.4, 0.45, 0.5))
        self.draw_text(f"Halaman {self.current_page_num}", 500, 28, font="F3", size=8, color=(0.4, 0.45, 0.5))

    def set_color(self, r, g, b, stroke=False):
        if stroke:
            self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG".encode("ascii"))
        else:
            self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg".encode("ascii"))

    def draw_rect(self, x, y, w, h, fill_color=None, stroke_color=None, width=1.0):
        self.current_stream.append(f"q".encode("ascii"))
        if fill_color:
            self.set_color(*fill_color, stroke=False)
        if stroke_color:
            self.set_color(*stroke_color, stroke=True)
            self.current_stream.append(f"{width:.2f} w".encode("ascii"))
        
        if fill_color and stroke_color:
            self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re B".encode("ascii"))
        elif fill_color:
            self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re f".encode("ascii"))
        elif stroke_color:
            self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re S".encode("ascii"))
        self.current_stream.append(f"Q".encode("ascii"))

    def draw_line(self, x1, y1, x2, y2, stroke_color=(0.1, 0.2, 0.5), width=1.0):
        self.current_stream.append(f"q".encode("ascii"))
        self.set_color(*stroke_color, stroke=True)
        self.current_stream.append(f"{width:.2f} w".encode("ascii"))
        self.current_stream.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S".encode("ascii"))
        self.current_stream.append(f"Q".encode("ascii"))

    def escape_text(self, text):
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    def draw_text(self, text, x, y, font="F1", size=10, color=(0.1, 0.1, 0.1)):
        safe_t = self.escape_text(text)
        self.current_stream.append(f"q".encode("ascii"))
        self.set_color(*color, stroke=False)
        self.current_stream.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe_t}) Tj ET".encode("latin1", errors="replace"))
        self.current_stream.append(f"Q".encode("ascii"))

    def close(self):
        if self.current_stream:
            self.pages.append(b"\n".join(self.current_stream))
            self.current_stream = []

    def get_pdf_bytes(self):
        self.close()
        objects = []
        objects.append(b"") # 0
        
        objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        
        font_obj_ids = {}
        next_id = 3
        for f_alias, f_name in self.fonts.items():
            font_obj_ids[f_alias] = next_id
            objects.append(f"<< /Type /Font /Subtype /Type1 /BaseFont /{f_name} /Encoding /WinAnsiEncoding >>".encode("ascii"))
            next_id += 1
            
        font_res_str = " ".join([f"/{k} {font_obj_ids[k]} 0 R" for k in self.fonts])
        
        page_obj_ids = []
        for i in range(len(self.pages)):
            page_id = next_id
            page_obj_ids.append(page_id)
            next_id += 2
            
        kids_str = " ".join([f"{pid} 0 R" for pid in page_obj_ids])
        pages_tree = f"<< /Type /Pages /Kids [ {kids_str} ] /Count {len(page_obj_ids)} /MediaBox [ 0 0 {self.page_width:.2f} {self.page_height:.2f} ] >>".encode("ascii")
        objects[2] = pages_tree
        
        for i, page_bytes in enumerate(self.pages):
            page_id = page_obj_ids[i]
            content_id = page_id + 1
            
            p_obj = f"<< /Type /Page /Parent 2 0 R /Resources << /Font << {font_res_str} >> >> /Contents {content_id} 0 R >>".encode("ascii")
            objects.append(p_obj)
            
            c_obj = f"<< /Length {len(page_bytes)} >>\nstream\n".encode("ascii") + page_bytes + b"\nendstream"
            objects.append(c_obj)
            
        out = []
        out.append(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = [0]
        curr_offset = len(out[0])
        
        for obj_idx in range(1, len(objects)):
            obj_data = objects[obj_idx]
            offsets.append(curr_offset)
            header = f"{obj_idx} 0 obj\n".encode("ascii")
            footer = b"\nendobj\n"
            out.append(header)
            out.append(obj_data)
            out.append(footer)
            curr_offset += len(header) + len(obj_data) + len(footer)
            
        xref_offset = curr_offset
        out.append(f"xref\n0 {len(objects)}\n".encode("ascii"))
        out.append(b"0000000000 65535 f \n")
        for obj_idx in range(1, len(objects)):
            out.append(f"{offsets[obj_idx]:010d} 00000 n \n".encode("ascii"))
            
        out.append(f"trailer\n<< /Size {len(objects)} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii"))
        return b"".join(out)

def build_pdf_document():
    print("-> Membangun Berkas Dokumen Kontrak Kuliah PDF Resmi (Sesuai Siakad)...")
    pdf = SimplePDF()
    
    # -------------------------------------------------------------
    # HALAMAN 1: KOP, IDENTITAS, MANFAAT, DESKRIPSI, CPL/CPMK
    # -------------------------------------------------------------
    pdf.new_page()
    
    # Header KOP Universitas
    pdf.draw_text("YAYASAN UBUDIYAH INDONESIA", 297.64 - 85, 775, font="F2", size=11, color=(0.12, 0.23, 0.54))
    pdf.draw_text("UNIVERSITAS UBUDIYAH INDONESIA", 297.64 - 105, 760, font="F2", size=12, color=(0.12, 0.23, 0.54))
    pdf.draw_text("FAKULTAS SAINS DAN TEKNOLOGI - PROGRAM STUDI S1 INFORMATIKA", 297.64 - 170, 746, font="F2", size=9.5, color=(0.01, 0.52, 0.78))
    pdf.draw_text("Jl. Alue Naga, Desa Tibang, Kec. Syiah Kuala, Kota Banda Aceh | Laman: https://uui.ac.id", 297.64 - 185, 734, font="F3", size=8, color=(0.4, 0.45, 0.5))
    pdf.draw_line(40, 725, 555, 725, stroke_color=(0.12, 0.23, 0.54), width=1.8)
    pdf.draw_line(40, 722, 555, 722, stroke_color=(0.01, 0.52, 0.78), width=0.8)
    
    # Judul Dokumen
    pdf.draw_text("KONTRAK PERKULIAHAN", 297.64 - 95, 698, font="F2", size=14, color=(0.12, 0.23, 0.54))
    pdf.draw_text("SEMESTER GANJIL TAHUN AKADEMIK 2026/2027", 297.64 - 130, 683, font="F2", size=10, color=(0.01, 0.52, 0.78))
    
    # Section I: Identitas MK
    pdf.draw_rect(40, 660, 515, 18, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("I. IDENTITAS MATA KULIAH", 48, 665, font="F2", size=9.5, color=(1, 1, 1))
    
    id_rows = [
        ("Nama Mata Kuliah", "Pemrograman Berorientasi Objek", "Kode MK / SKS", "IFR 214 / 3 SKS (T=2, P=1)"),
        ("Program Studi / Jenjang", "S1 - Informatika / Sarjana (S1)", "Semester / Periode", "Semester III / 2026 Ganjil"),
        ("Fakultas / Universitas", "Fakultas Sains dan Teknologi / UUI", "Nama Kelas / Sistem", "Kelas A / Reguler"),
        ("Kurikulum / Rumpun", "Kurikulum 2023 (OBE) / Wajib Prodi", "Kapasitas / Peserta", "60 Mahasiswa / 37 Mahasiswa"),
        ("Dosen Pengampu Utama", "Mahendar Dwi Payana, S.ST., M.T.", "Ruang Perkuliahan", "Lab. Rekayasa Perangkat Lunak UUI")
    ]
    
    y_id = 642
    for r1, v1, r2, v2 in id_rows:
        bg = (0.97, 0.98, 0.99) if (y_id % 30 < 15) else (1, 1, 1)
        pdf.draw_rect(40, y_id - 2, 515, 14, fill_color=bg, stroke_color=(0.9, 0.92, 0.95), width=0.5)
        pdf.draw_text(r1 + ":", 45, y_id + 1, font="F2", size=8, color=(0.2, 0.25, 0.35))
        pdf.draw_text(v1, 150, y_id + 1, font="F1", size=8, color=(0.05, 0.1, 0.15))
        pdf.draw_text(r2 + ":", 310, y_id + 1, font="F2", size=8, color=(0.2, 0.25, 0.35))
        pdf.draw_text(v2, 400, y_id + 1, font="F1", size=8, color=(0.05, 0.1, 0.15))
        y_id -= 14
        
    # Section II: Manfaat & Deskripsi
    y_sec = y_id - 8
    pdf.draw_rect(40, y_sec, 515, 18, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("II. MANFAAT DAN DESKRIPSI SINGKAT MATA KULIAH", 48, y_sec + 5, font="F2", size=9.5, color=(1, 1, 1))
    
    y_sec -= 16
    pdf.draw_text("Mata kuliah Pemrograman Berorientasi Objek (IFR 214) merupakan pilar utama dalam kurikulum S1 Informatika UUI untuk", 40, y_sec, font="F1", size=8.5, color=(0.1, 0.15, 0.2))
    y_sec -= 11
    pdf.draw_text("membentuk pola pikir modular, terstruktur, dan siap industri. Mahasiswa mempelajari implementasi konsep OOP pada PHP 8+", 40, y_sec, font="F1", size=8.5, color=(0.1, 0.15, 0.2))
    y_sec -= 11
    pdf.draw_text("modern (Strict Types, Constructor Promotion, 4 Pilar OOP, Interface, Trait, Exception Handling, SPL Collections, File I/O, PSR-4,", 40, y_sec, font="F1", size=8.5, color=(0.1, 0.15, 0.2))
    y_sec -= 11
    pdf.draw_text("5 Prinsip SOLID, dan Arsitektur Model-Service-Repository) untuk membangun sistem perangkat lunak yang aman dan teruji.", 40, y_sec, font="F1", size=8.5, color=(0.1, 0.15, 0.2))
    
    # Section III: CPL & CPMK
    y_sec -= 18
    pdf.draw_rect(40, y_sec, 515, 18, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("III. CAPAIAN PEMBELAJARAN LULUSAN & MATA KULIAH (CPL & CPMK)", 48, y_sec + 5, font="F2", size=9.5, color=(1, 1, 1))
    
    y_sec -= 15
    cpls = [
        ("CPL-P1 (Pengetahuan)", "Menguasai konsep, paradigma, prinsip, dan teknik OOP dalam rekayasa perangkat lunak modern."),
        ("CPL-KU1 (Keterampilan)", "Mampu berpikir kritis, logis, sistematis, dan solutif dalam merancang abstraksi perangkat lunak."),
        ("CPL-KK1 (Keahlian Khusus)", "Mampu merancang, mengimplementasikan, menguji, dan mendokumentasikan aplikasi OOP PHP 8+."),
        ("CPL-S1 (Sikap & Etika)", "Menunjukkan etika profesi rekayasa perangkat lunak, disiplin, kerja sama, dan anti-plagiarisme.")
    ]
    for code, desc in cpls:
        pdf.draw_text("• " + code + ":", 45, y_sec, font="F2", size=8, color=(0.12, 0.23, 0.54))
        pdf.draw_text(desc, 175, y_sec, font="F1", size=8, color=(0.1, 0.15, 0.2))
        y_sec -= 11
        
    y_sec -= 4
    cpmks = [
        ("CPMK-1: Paradigma OOP", "Mampu menganalisis paradigma OOP dan membandingkannya secara analitis dengan prosedural."),
        ("CPMK-2: Class & Object", "Mampu mengimplementasikan class, typed properties, constructor promotion, dan memory handle."),
        ("CPMK-3: 4 Pilar OOP", "Mampu menerapkan Enkapsulasi, Pewarisan, Polimorfisme, dan Abstraksi (Interface & Backed Enum)."),
        ("CPMK-4: Arsitektur Proyek", "Mampu mengelola Namespace PSR-4, Exception Handling, First-Class Collections, dan File I/O."),
        ("CPMK-5: Prinsip SOLID", "Mampu merancang kode bersih menggunakan 5 prinsip desain SOLID untuk mencegah Software Rot."),
        ("CPMK-6: Capstone Project", "Mampu merekayasa dan mendemokan Mini Project POS berbasis arsitektur Model-Service-Repository.")
    ]
    for code, desc in cpmks:
        pdf.draw_text("• " + code + ":", 45, y_sec, font="F2", size=8, color=(0.01, 0.52, 0.78))
        pdf.draw_text(desc, 175, y_sec, font="F1", size=8, color=(0.1, 0.15, 0.2))
        y_sec -= 11

    # -------------------------------------------------------------
    # HALAMAN 2: MATRIKS 16 PERTEMUAN (RPS PERKULIAHAN)
    # -------------------------------------------------------------
    pdf.new_page()
    
    pdf.draw_rect(40, 770, 515, 20, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("IV. MATRIKS RENCANA PERKULIAHAN (16 PERTEMUAN)", 48, 776, font="F2", size=10, color=(1, 1, 1))
    
    # Table Header
    y_tab = 745
    pdf.draw_rect(40, y_tab, 515, 16, fill_color=(0.01, 0.52, 0.78))
    pdf.draw_text("Prt", 45, y_tab + 4, font="F2", size=8, color=(1, 1, 1))
    pdf.draw_text("Kemampuan Akhir (Sub-CPMK)", 70, y_tab + 4, font="F2", size=8, color=(1, 1, 1))
    pdf.draw_text("Materi Pembelajaran Pokok", 220, y_tab + 4, font="F2", size=8, color=(1, 1, 1))
    pdf.draw_text("Metode & Bentuk", 410, y_tab + 4, font="F2", size=8, color=(1, 1, 1))
    pdf.draw_text("Evaluasi", 510, y_tab + 4, font="F2", size=8, color=(1, 1, 1))
    
    rps_pdf_rows = [
        ("1", "Memahami konsep dasar & paradigma OOP", "Kontrak Kuliah, Evolusi Paradigma, Ekosistem PHP 8+", "Ceramah & Diskusi", "Partisipatif"),
        ("2", "Mampu memodelkan class & object di memori", "Class, Object, Typed Properties, Object Handle vs Clone", "Praktikum Mandiri", "Tugas"),
        ("3", "Mampu mengelola siklus hidup & constructor", "Constructor Promotion, Destructor, Named Args, Static", "Praktikum Terbimbing", "Tugas"),
        ("4", "Mampu menerapkan prinsip enkapsulasi", "Visibility Modifiers, Tell Don't Ask, Readonly Class", "Praktikum Lab", "Quiz / Tugas"),
        ("5", "Mampu merekayasa pewarisan & trait", "Inheritance (extends), Parent Chaining, Trait, Final", "Praktikum & Analisis", "Tugas"),
        ("6", "Mampu mengimplementasikan polimorfisme", "Polymorphism, Dynamic Dispatch, Type Hinting", "Praktik & Kuis", "Quiz"),
        ("7", "Mampu merancang abstraksi kontrak sistem", "Abstract Class, Template Method, Interface, Backed Enum", "Praktik Kontrak", "Tugas"),
        ("8", "EVALUASI CAPAIAN PERTEMUAN 1 s.d. 7", "UJIAN TENGAH SEMESTER (UTS) - TEORI & LIVE CODING", "Ujian Lab Terjadwal", "UTS (30%)"),
        ("9", "Mampu mengorganisasi namespace & autoload", "Namespace Architecture, Composer Setup, Standar PSR-4", "Praktik Konfigurasi", "Tugas"),
        ("10", "Mampu merekayasa penanganan galat tangguh", "Exception Hierarchy, Multi-Catch, Custom Exceptions", "Praktik Robust Error", "Tugas"),
        ("11", "Mampu memanipulasi first-class collections", "First-Class Collections, SPL Interfaces, Map/Filter", "Praktik Koleksi Data", "Quiz / Tugas"),
        ("12", "Mampu mengelola persistensi berkas I/O", "File I/O Stream, SplFileObject, Race Condition & LOCK_EX", "Praktik Persistensi", "Tugas"),
        ("13", "Mampu menerapkan 5 prinsip desain SOLID", "Prinsip SOLID (SRP, OCP, LSP, ISP, DIP) pada PHP 8+", "Studi Kasus Desain", "Partisipatif"),
        ("14", "Mampu merancang arsitektur aplikasi bersih", "Arsitektur Model-Service-Repository & Domain Modeling", "Praktik Arsitektur", "Tugas Besar"),
        ("15", "Mampu merekayasa mini project terpadu", "Pengembangan Capstone Project: Sistem POS Enterprise", "PjBL & Asistensi", "Asistensi"),
        ("16", "EVALUASI CAPAIAN KOMPREHENSIF PROYEK", "UJIAN AKHIR SEMESTER (UAS) - DEMO PROYEK CAPSTONE", "Demo & Uji Program", "UAS (40%)")
    ]
    
    y_r = y_tab - 18
    for p_num, subc, mat, met, bot in rps_pdf_rows:
        is_hl = p_num in ["8", "16"]
        bg = (0.92, 0.96, 1.0) if is_hl else ((0.97, 0.98, 0.99) if int(p_num) % 2 == 1 else (1, 1, 1))
        pdf.draw_rect(40, y_r - 2, 515, 17, fill_color=bg, stroke_color=(0.88, 0.9, 0.93), width=0.5)
        
        f_type = "F2" if is_hl else "F1"
        c_text = (0.12, 0.23, 0.54) if is_hl else (0.1, 0.15, 0.2)
        
        pdf.draw_text(p_num, 48, y_r + 3, font="F2", size=8, color=c_text)
        pdf.draw_text(subc[:32], 70, y_r + 3, font=f_type, size=7.5, color=c_text)
        pdf.draw_text(mat[:40], 220, y_r + 3, font=f_type, size=7.5, color=c_text)
        pdf.draw_text(met[:20], 410, y_r + 3, font="F1", size=7.5, color=c_text)
        pdf.draw_text(bot, 508, y_r + 3, font="F2", size=7.5, color=c_text)
        y_r -= 18

    # -------------------------------------------------------------
    # HALAMAN 3: PENILAIAN SIAKAD, TATA TERTIB, PUSTAKA & PENGESAHAN
    # -------------------------------------------------------------
    pdf.new_page()
    
    # Section V: Kriteria Penilaian Sesuai Siakad UUI
    pdf.draw_rect(40, 770, 515, 18, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("V. KOMPONEN EVALUASI & SKALA PENILAIAN (PORTAL SIAKAD UUI)", 48, 775, font="F2", size=9.5, color=(1, 1, 1))
    
    # Table 1: Komponen Evaluasi Siakad
    y_ev = 750
    pdf.draw_rect(40, y_ev, 515, 14, fill_color=(0.04, 0.31, 0.54))
    pdf.draw_text("No.", 45, y_ev + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Metode Evaluasi", 70, y_ev + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Jenis Evaluasi", 180, y_ev + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Bobot Evaluasi", 430, y_ev + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Syarat Lulus", 505, y_ev + 3, font="F2", size=7.5, color=(1, 1, 1))
    
    eval_pdf_siakad = [
        ("1", "TUGAS", "Kognitif/Pengetahuan - Tugas", "20%", "-"),
        ("2", "QUIZ", "Kognitif/Pengetahuan - Quiz", "5%", "-"),
        ("3", "UTS", "Kognitif/Pengetahuan - Ujian Tengah Semester", "30%", "-"),
        ("4", "UAS", "Kognitif/Pengetahuan - Ujian Akhir Semester", "40%", "-"),
        ("5", "AKTIVITAS PARTISIPATIF", "Aktivitas Partisipatif", "5%", "-"),
        ("", "Total Persentase Komponen Evaluasi", "", "100%", "")
    ]
    
    y_ev -= 12
    for n, met, jen, bob, syr in eval_pdf_siakad:
        is_tot = "Total" in met
        bg = (0.9, 0.94, 0.98) if is_tot else ((0.97, 0.98, 0.99) if y_ev % 24 < 12 else (1, 1, 1))
        pdf.draw_rect(40, y_ev - 1, 515, 12, fill_color=bg, stroke_color=(0.88, 0.9, 0.93), width=0.5)
        pdf.draw_text(n, 48, y_ev + 2, font="F2", size=7.5, color=(0.1, 0.15, 0.2))
        pdf.draw_text(met, 70, y_ev + 2, font="F2" if is_tot else "F1", size=7.5, color=(0.1, 0.15, 0.2))
        pdf.draw_text(jen, 180, y_ev + 2, font="F1", size=7.5, color=(0.2, 0.25, 0.3))
        pdf.draw_text(bob, 440, y_ev + 2, font="F2", size=7.5, color=(0.12, 0.23, 0.54))
        pdf.draw_text(syr, 520, y_ev + 2, font="F1", size=7.5, color=(0.2, 0.25, 0.3))
        y_ev -= 12
        
    pdf.draw_text("Keterangan: Syarat Lulus Mata Kuliah adalah pemenuhan komponen nilai wajib. Mahasiswa tanpa komponen utama dinyatakan tidak lulus.", 40, y_ev, font="F3", size=7, color=(0.35, 0.4, 0.45))
    
    # Table 2: Mapping Grade Siakad
    y_gr = y_ev - 16
    pdf.draw_text("Tabel Mapping Konversi Grade Nilai Akhir Siakad UUI:", 40, y_gr + 4, font="F2", size=8, color=(0.12, 0.23, 0.54))
    y_gr -= 12
    pdf.draw_rect(40, y_gr, 515, 13, fill_color=(0.01, 0.52, 0.78))
    pdf.draw_text("Grade", 70, y_gr + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Bobot", 180, y_gr + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Nilai Bawah", 290, y_gr + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Nilai Atas", 400, y_gr + 3, font="F2", size=7.5, color=(1, 1, 1))
    pdf.draw_text("Status Kelulusan", 475, y_gr + 3, font="F2", size=7.5, color=(1, 1, 1))
    
    grades_siakad = [
        ("A", "4,00", "80,00", "100,00", "Sangat Memuaskan / Lulus"),
        ("B", "3,00", "60,00", "79,99", "Baik / Lulus"),
        ("C", "2,00", "40,00", "59,99", "Cukup (Batas Minimal Lulus)"),
        ("D", "1,00", "20,00", "39,99", "Kurang / Wajib Mengulang"),
        ("E", "0,00", "0,00", "19,99", "Gagal / Tidak Lulus")
    ]
    y_gr -= 11
    for grd, bbt, nb, na, stt in grades_siakad:
        bg = (0.97, 0.98, 0.99) if y_gr % 22 < 11 else (1, 1, 1)
        pdf.draw_rect(40, y_gr - 1, 515, 11, fill_color=bg, stroke_color=(0.88, 0.9, 0.93), width=0.5)
        pdf.draw_text(grd, 80, y_gr + 2, font="F2", size=7.5, color=(0.12, 0.23, 0.54))
        pdf.draw_text(bbt, 190, y_gr + 2, font="F1", size=7.5, color=(0.1, 0.15, 0.2))
        pdf.draw_text(nb, 305, y_gr + 2, font="F1", size=7.5, color=(0.1, 0.15, 0.2))
        pdf.draw_text(na, 415, y_gr + 2, font="F1", size=7.5, color=(0.1, 0.15, 0.2))
        pdf.draw_text(stt, 475, y_gr + 2, font="F1", size=7.0, color=(0.2, 0.25, 0.3))
        y_gr -= 11

    # Section VI: Tata Tertib Singkat
    y_sec = y_gr - 6
    pdf.draw_rect(40, y_sec, 515, 15, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("VI. TATA TERTIB & NORMA AKADEMIK PERKULIAHAN", 48, y_sec + 4, font="F2", size=8.5, color=(1, 1, 1))
    
    y_sec -= 12
    rules = [
        ("1. Toleransi Terlambat", "Maksimal 15 menit. Terlambat > 15 menit boleh masuk tetapi presensi alpa."),
        ("2. Batas Minimal Hadir", "Kehadiran minimal 75% (12 pertemuan riil) sebagai syarat mutlak mengikuti UAS."),
        ("3. Etika & Perlengkapan", "Berbusana rapi, sopan, berkerah, bersepatu. Membawa laptop dengan PHP 8.1+ & Composer."),
        ("4. Sanksi Plagiarisme", "Kecurangan akademik / copy-paste kode dikenakan pembatalan nilai (Nilai E otomatis).")
    ]
    for r_title, r_desc in rules:
        pdf.draw_text("• " + r_title + ":", 45, y_sec, font="F2", size=7.5, color=(0.12, 0.23, 0.54))
        pdf.draw_text(r_desc, 155, y_sec, font="F1", size=7.5, color=(0.1, 0.15, 0.2))
        y_sec -= 9.5

    # Section VII: Lembar Pengesahan
    y_sec -= 4
    pdf.draw_rect(40, y_sec, 515, 15, fill_color=(0.12, 0.23, 0.54))
    pdf.draw_text("VII. LEMBAR PENGESAHAN KONTRAK PERKULIAHAN", 48, y_sec + 4, font="F2", size=8.5, color=(1, 1, 1))
    
    y_sec -= 11
    pdf.draw_text("Banda Aceh, 1 September 2026", 410, y_sec, font="F1", size=8, color=(0.2, 0.25, 0.3))
    
    y_sec -= 13
    pdf.draw_text("Perwakilan Mahasiswa Kelas A,", 70, y_sec, font="F2", size=8, color=(0.12, 0.23, 0.54))
    pdf.draw_text("Dosen Pengampu Mata Kuliah,", 360, y_sec, font="F2", size=8, color=(0.12, 0.23, 0.54))
    
    y_sec -= 35
    pdf.draw_text("( _____________________________ )", 50, y_sec, font="F1", size=8, color=(0.1, 0.1, 0.1))
    pdf.draw_text("( Mahendar Dwi Payana, S.ST., M.T. )", 340, y_sec, font="F2", size=8, color=(0.1, 0.1, 0.1))
    
    y_sec -= 8
    pdf.draw_text("NPM. ............................................", 50, y_sec, font="F1", size=7.5, color=(0.4, 0.45, 0.5))
    pdf.draw_text("NIDN. 1331108701", 340, y_sec, font="F1", size=7.5, color=(0.4, 0.45, 0.5))
    
    y_sec -= 15
    pdf.draw_text("Mengetahui,", 275, y_sec, font="F1", size=8, color=(0.2, 0.25, 0.3))
    y_sec -= 9
    pdf.draw_text("Ketua Program Studi S1 Informatika UUI", 205, y_sec, font="F2", size=8, color=(0.12, 0.23, 0.54))
    y_sec -= 30
    pdf.draw_text("( ____________________________________ )", 200, y_sec, font="F1", size=8, color=(0.1, 0.1, 0.1))
    y_sec -= 8
    pdf.draw_text("NIDN. ....................................................", 200, y_sec, font="F1", size=7.5, color=(0.4, 0.45, 0.5))

    # Save PDF
    pdf_bytes = pdf.get_pdf_bytes()
    with open(PDF_MAIN, "wb") as f:
        f.write(pdf_bytes)
    shutil.copyfile(PDF_MAIN, PDF_LATEST)
    
    print(f"✅ Dokumen Kontrak Kuliah PDF berhasil diperbarui: {PDF_MAIN}")
    print(f"✅ Ukuran Berkas: {len(pdf_bytes) / 1024:.2f} KB (Batas Siakad: 2048 KB / 2 MB)")
    print(f"✅ Salinan rilis: {PDF_LATEST}")

if __name__ == "__main__":
    build_pdf_document()
