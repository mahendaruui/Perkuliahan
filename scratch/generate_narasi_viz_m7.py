#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 7 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m7/slide-XX.mp3
- Menginjeksi array audioTranscripts ke dalam HTML presentasi.
"""
import asyncio
import json
import socket
import subprocess
from pathlib import Path

import edge_tts


def _patch_dns() -> None:
    """Workaround: resolver sistem gagal me-resolve host TTS, padahal `dig` berhasil."""
    host = "speech.platform.bing.com"
    try:
        out = subprocess.check_output(["dig", "+short", host], text=True)
        ips = [l.strip() for l in out.splitlines()
               if l.strip() and l.strip()[0].isdigit() and ":" not in l]
    except Exception:
        ips = []
    if not ips:
        print("[dns-patch] dilewati (dig tidak mengembalikan IPv4)")
        return
    ip = ips[0]
    real = socket.getaddrinfo

    def patched(h, p, *a, **k):
        if h == host:
            return real(ip, p, *a, **k)
        return real(h, p, *a, **k)

    socket.getaddrinfo = patched
    print(f"[dns-patch] {host} -> {ip}")


_patch_dns()

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-7-visualisasi-relasi-multivariat.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m7"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan ketujuh mata kuliah Visualisasi Data IFR309. Hari ini kita akan membahas visualisasi korelasi, matriks, dan multivariat. Jika pertemuan sebelumnya kita fokus pada satu atau dua variabel, hari ini kita akan melihat hubungan antar banyak variabel sekaligus. Topik ini sangat penting karena pertanyaan analitis paling berharga biasanya berbentuk hubungan, bukan angka tunggal. Mari kita mulai.",
    "Pada pertemuan ketujuh ini, capaian pembelajaran kita adalah menganalisis dan memvisualisasikan korelasi antar variabel menggunakan matriks korelasi dengan arsitektur triangular mask, membangun visualisasi dimensi tinggi menggunakan bubble chart, pair plot, dan parallel coordinates plot, menyajikan struktur hierarkis dan aliran menggunakan treemap dan sankey diagram, serta memahami tiga jebakan statistik kritis yaitu Anscombe's Quartet, korelasi semu, dan paradoks Simpson.",
    "Mari kita mulai dari Bagian Pertama: Korelasi dan Matriks Multivariat. Korelasi mengukur kekuatan sekaligus arah hubungan antara dua variabel acak. Memahaminya adalah fondasi untuk setiap analisis multivariat.",
    "Koefisien korelasi Pearson dilambangkan dengan r, dan nilainya berkisar dari minus satu sampai plus satu. Nilai plus satu berarti korelasi positif linear sempurna, artinya kedua variabel naik bersama-sama. Nilai nol berarti tidak ada hubungan linear, namun hati-hati, bisa jadi ada hubungan non-linear yang tidak tertangkap. Nilai minus satu berarti korelasi negatif linear sempurna, artinya satu naik saat yang lain turun. Contoh positif sempurna adalah tinggi badan dengan berat badan, dan contoh negatif adalah harga dengan permintaan.",
    "Ada tiga metode korelasi yang perlu kita kuasai. Pertama, Pearson, untuk data numerik kontinu yang berdistribusi normal dan memiliki hubungan linear. Kedua, Spearman, yang bersifat non-parametrik dan mengukur hubungan monotonik, cocok ketika data memiliki outlier ekstrem atau hubungan melengkung. Ketiga, Kendall, yang berbasis pasangan konkordan dan diskordan, cocok untuk sampel kecil dengan banyak nilai peringkat yang sama. Jebakan umum adalah memakai Pearson untuk data yang memiliki outlier ekstrem, karena hasilnya akan menyesatkan.",
    "Setelah memahami korelasi, kita perlu memvisualisasikannya dalam sebuah matriks. Namun, matriks korelasi penuh bersifat simetris, artinya segitiga atas menduplikasi informasi segitiga bawah. Ini melanggar prinsip Data-Ink Ratio Tufte. Solusinya adalah triangular masking, yaitu memotong segitiga atas menggunakan fungsi np.triu. Kita kemudian memanggil sns.heatmap dengan parameter mask, palet divergen vlag yang berpusat netral di nol, serta vmin minus satu dan vmax satu. Hasilnya adalah heatmap korelasi yang bersih, informatif, dan ber-Data-Ink tinggi.",
    "Kita masuk ke Bagian Kedua: Visualisasi Dimensi Tinggi. Tantangannya adalah menampilkan data berdimensi empat atau lima pada layar dua dimensi, tanpa kekacauan visual.",
    "Bubble chart adalah cara menampilkan empat dimensi sekaligus. Posisi X untuk dimensi pertama, posisi Y untuk dimensi kedua, ukuran bubble untuk dimensi ketiga, dan warna untuk dimensi keempat. Contohnya pada dataset gapminder, kita memetakan PDB per kapita ke sumbu X, angka harapan hidup ke sumbu Y, populasi ke ukuran bubble, dan benua ke warna. Namun ingat hierarki akurasi saluran dari pertemuan ketiga, bahwa luas area adalah saluran yang lemah. Jadi jangan mengandalkan ukuran bubble untuk perbandingan angka yang presisi.",
    "Pair plot adalah alat eksplorasi cepat yang menampilkan matriks scatter untuk semua pasangan variabel. Diagonal menampilkan distribusi tiap variabel, sedangkan bagian luar diagonal menampilkan scatter tiap pasangan. Parameter corner sama dengan True membuat kita hanya menampilkan segitiga bawah, menghindari duplikasi, dan konsisten dengan prinsip triangular mask. Pair plot sangat berguna untuk menemukan fitur mana yang paling memisahkan kelas, misalnya spesies pada dataset iris.",
    "Untuk data dengan lebih dari empat atau lima fitur, parallel coordinates adalah pilihan tepat. Setiap sumbu vertikal mewakili satu fitur, dan setiap garis mewakili satu observasi. Jika pola garis menyilang secara jelas memisahkan kelas, berarti fitur tersebut diskriminatif. Kita bisa membuatnya dengan plotly express menggunakan parameter color untuk kelas target. Alat ini sangat berguna untuk menentukan fitur mana yang paling mampu memisahkan kelas target secara visual, misalnya pada dataset wine atau iris.",
    "Kita masuk ke Bagian Ketiga: Jebakan Statistik. Bagian ini mungkin yang paling penting hari ini, karena membahas bagaimana statistik bisa menyesatkan kita jika tidak disertai inspeksi visual.",
    "Jebakan pertama adalah Anscombe's Quartet, yang dirumuskan oleh Francis Anscombe pada tahun 1973. Ini adalah empat dataset berbeda yang memiliki statistik deskriptif yang identik, yaitu rata-rata X sembilan, rata-rata Y tujuh koma lima, variansi yang sama, korelasi Pearson nol koma delapan satu enam, dan garis regresi yang sama. Namun, pola datanya bertolak belakang. Dataset satu adalah hubungan linear normal. Dataset dua adalah hubungan non-linear berbentuk kurva. Dataset tiga adalah linear sempurna dengan satu outlier ekstrem. Dan dataset empat adalah sebaran vertikal konstan dengan satu titik pengungkit. Pelajarannya jelas, jangan pernah mempercayai ringkasan angka statistik sebelum melihat visualisasi sebarannya.",
    "Jebakan kedua adalah korelasi semu, atau spurious correlation, dan hubungannya dengan kausalitas. Korelasi yang kuat antara dua variabel tidak membuktikan hubungan sebab-akibat. Kadang korelasinya hanya kebetulan, kadang karena keduanya dipengaruhi variabel ketiga yang disebut confounder. Contoh klasiknya, penjualan es krim dan angka kejahatan sama-sama naik saat musim panas, tetapi bukan berarti es krim menyebabkan kejahatan. Sebagai analis, kita harus selalu bertanya, apa variabel ketiga yang mungkin menjelaskan keduanya, sebelum menyimpulkan sebab-akibat.",
    "Jebakan ketiga adalah paradoks Simpson. Ini adalah fenomena di mana tren pada data agregat berbalik arah ketika data dipecah per kelompok. Contohnya pada data penerimaan mahasiswa baru, secara agregat pria tampak memiliki tingkat penerimaan lebih tinggi. Namun ketika data dipecah per jurusan, wanita justru memiliki tingkat penerimaan lebih tinggi di hampir semua jurusan. Ini terjadi karena adanya variabel lurking, di sini tingkat selektivitas jurusan. Solusinya, selalu disagregasi data per kelompok yang relevan, dan visualisasikan keduanya, baik agregat maupun per kelompok, secara bersamaan.",
    "Kita masuk ke Bagian Keempat: Hierarki dan Aliran. Dua bentuk visualisasi yang jarang diajarkan namun sangat kuat dalam praktik analitis.",
    "Treemap membagi ruang dua dimensi menjadi persegi panjang bersarang. Luas area merepresentasikan besaran kuantitatif, sedangkan warna menunjukkan metrik performa kedua. Kita bisa membuatnya dengan plotly express, menentukan path untuk hierarki, misalnya kontinen lalu negara, values untuk luas area populasi, dan color untuk angka harapan hidup. Treemap sangat tepat untuk struktur part-to-whole yang hierarkis, ketika kita ingin menunjukkan kontribusi tiap bagian terhadap keseluruhan.",
    "Sankey diagram menggambarkan aliran atau perpindahan kuantitas antar simpul tahapan proses. Contohnya funnel penjualan, dari pengunjung web, masuk keranjang, checkout, hingga pembayaran berhasil. Manfaat utamanya adalah mengidentifikasi titik drop-off terbesar. Dari contoh, dari sepuluh ribu pengunjung menjadi tiga ribu lima ratus yang masuk keranjang, artinya ada kebocoran sebesar enam ribu lima ratus, dan inilah titik yang perlu diperbaiki. Sankey melengkapi analisis funnel dari pertemuan keempat.",
    "Untuk praktikum, ada tiga eksperimen Python. Pertama, heatmap korelasi multivariat ber-masking segitiga, menggunakan dataset penguins dan palet divergen vlag. Kedua, pembuktian Anscombe's Quartet, membuat grid dua kali dua dengan sharex dan sharey, lalu memplot regplot tanpa interval kepercayaan untuk tiap dataset, sambil menampilkan nilai korelasinya. Ketiga, visualisasi hierarki multivariat berupa treemap dengan plotly, menggunakan dataset gapminder tahun dua ribu tujuh, memetakan kontinen dan negara sebagai hierarki, populasi sebagai luas, dan angka harapan hidup sebagai warna.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, kenapa memakai np.triu untuk mask pada heatmap korelasi? Karena matriks korelasi simetris, sehingga segitiga atas menduplikasi informasi segitiga bawah, dan memotongnya meningkatkan Data-Ink Ratio. Kedua, apa pelajaran utama Anscombe's Quartet? Bahwa statistik deskriptif bisa identik untuk dataset dengan pola yang sangat berbeda, jadi wajib inspeksi visual. Ketiga, apa itu paradoks Simpson? Fenomena di mana tren agregat berbalik ketika data dipecah per kelompok, akibat adanya variabel lurking. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan ketujuh ini. Kesimpulannya, visualisasi multivariat yang baik mengungkap hubungan antar variabel, sekaligus melindungi kita dari kesimpulan yang salah. Kuasai matriks korelasi ber-masking, visualisasi dimensi tinggi, serta waspadai tiga jebakan statistik, yaitu Anscombe, korelasi semu, dan paradoks Simpson. Tugas praktikum tujuh sudah tersedia, termasuk analisis paradoks Simpson dan implementasi parallel coordinates. Pertemuan berikutnya adalah Evaluasi Tengah Semester. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
]


async def generate() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    for i, text in enumerate(TRANSCRIPTS):
        num = str(i + 1).zfill(2)
        out = AUDIO_DIR / f"slide-{num}.mp3"
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(str(out))
        print(f"[{i+1:02d}/{len(TRANSCRIPTS)}] {out.name}  ({out.stat().st_size/1024:.0f} KB)")


def inject_transcripts() -> None:
    html = HTML.read_text(encoding="utf-8")
    payload = json.dumps(TRANSCRIPTS, ensure_ascii=False)
    declaration = "const audioTranscripts=" + payload + ";\n"
    if "/*__TRANSCRIPTS__*/" in html:
        html = html.replace("const audioTranscripts=[/*__TRANSCRIPTS__*/];", declaration.strip())
    else:
        start = html.index("const audioTranscripts=")
        end = html.index("const audioPlayer=", start)
        html = html[:start] + declaration + html[end:]
    HTML.write_text(html, encoding="utf-8")
    print(f"Transcripts injected -> {HTML}")


if __name__ == "__main__":
    asyncio.run(generate())
    inject_transcripts()
