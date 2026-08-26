# 🎓 Modul 16: Evaluasi Akhir Semester (UAS)

## 🎯 Sasaran Evaluasi Akhir
Evaluasi Akhir Semester (UAS) merupakan puncak penilaian berbasis OBE yang menguji pencapaian menyeluruh dari **CPMK 1, CPMK 2, CPMK 3, dan CPMK 4**.

---

## 📋 Format Evaluasi UAS (Bobot: 20% dari Total Nilai Akhir)

| Komponen Asesmen | Bobot Sesi | Keterangan |
| :--- | :---: | :--- |
| **1. Demonstrasi Live Dashboard Streamlit** | **40%** | Kelancaran interaktivitas dashboard, responsivitas filter, dan visualisasi tanpa galat runtime di hadapan dosen penguji. |
| **2. Presentasi & Data Storytelling** | **30%** | Kualitas penyampaian wawasan (*insight*), penerapan etika Tufte, eliminasi clutter, dan kejelasan solusi yang ditawarkan. |
| **3. Tanya Jawab Teknis & Pertanggungjawaban Kode** | **30%** | Penguasaan kode sumber (*Python, Pandas, Plotly, Streamlit*), pemahaman arsitektur data pipeline, dan orisinalitas karya. |

---

## 🏆 Rubrik Standar Penilaian UAS Capstone UUI

```mermaid
flowchart TD
    Root["🏆 <b>EVALUASI AKHIR SEMESTER (UAS): PROYEK CAPSTONE</b><br>Total Bobot Penilaian: 100 Poin (20% Nilai Akhir Perkuliahan)"]
    
    subgraph Grid[" "]
        direction TB
        subgraph Row1[" "]
            direction LR
            B["🌐 <b>1. Fungsionalitas Dashboard (30 Poin)</b><br>• Kecepatan & responsivitas widget filter<br>• Multi-page web layout Streamlit<br>• Bebas galat/crash saat demonstrasi live"]
            C["💡 <b>2. Insight & Storytelling (25 Poin)</b><br>• Ketajaman wawasan analitis bisnis<br>• Alur narasi runtut (Awal-Konflik-Solusi)<br>• Eliminasi beban kognitif audiens"]
        end
        subgraph Row2[" "]
            direction LR
            D["📊 <b>3. Desain Visual & Tufte (25 Poin)</b><br>• Rasio Data-Ink tinggi & bebas chartjunk<br>• Kesesuaian tipe chart dengan tipe data<br>• Palet warna ramah buta warna"]
            E["💻 <b>4. Kerapian Kode & Repositori (20 Poin)</b><br>• Kepatuhan kaidah Clean Code & modular<br>• Kelengkapan dokumentasi README.md<br>• Struktur repositori Git & requirements"]
        end
    end

    Root --> Row1
    Row1 --> Row2

    style Root fill:#fef08a,stroke:#ca8a04,stroke-width:2px
    style Grid fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px
    style Row1 fill:none,stroke:none
    style Row2 fill:none,stroke:none
    style B fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style C fill:#faf5ff,stroke:#9333ea,stroke-width:2px
    style D fill:#ecfdf5,stroke:#059669,stroke-width:2px
    style E fill:#f1f5f9,stroke:#475569,stroke-width:2px
```