#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 3 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m3/slide-XX.mp3
- Menginjeksi array audioTranscripts ke dalam HTML presentasi.
"""
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-3-prinsip-tufte-munzner.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m3"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan ketiga mata kuliah Visualisasi Data IFR309. Hari ini kita akan mendalami dua tokoh raksasa dalam bidang desain visualisasi, yaitu Edward Tufte dengan prinsip desain minimalisnya, dan Tamara Munzner dengan kerangka kerja bertingkatnya. Jika pertemuan sebelumnya kita belajar bagaimana otak manusia memproses informasi visual, maka hari ini kita akan belajar bagaimana merancang grafik yang jujur, efisien, dan tepat guna. Mari kita mulai.",
    "Pada pertemuan ketiga ini, capaian pembelajaran kita adalah menghitung dan mengoptimalkan Data-Ink Ratio, mengidentifikasi dan mengeliminasi berbagai bentuk Chartjunk, mengkalkulasi nilai Lie Factor untuk menjamin integritas grafis, serta merancang visualisasi menggunakan kerangka kerja Nested Model dari Tamara Munzner. Alur kita terbagi dua bagian besar: fondasi desain Edward Tufte, lalu rekayasa pemetaan visual Tamara Munzner, dan diakhiri praktikum Python.",
    "Mari kita masuki Bagian Pertama: Fondasi Desain Edward Tufte. Beliau adalah profesor dari Universitas Yale yang pada tahun 1983 menerbitkan buku legendaris berjudul The Visual Display of Quantitative Information. Buku ini dianggap sebagai kitab suci desain grafis analitis yang meletakkan standar filosofis dan etika tertinggi dalam menampilkan data kuantitatif.",
    "Tufte merumuskan empat pilar utama desain analitis. Pertama, maksimalkan Data-Ink Ratio dengan menghapus elemen non-data. Kedua, jaga integritas grafis agar Lie Factor mendekati satu koma nol. Ketiga, eliminasi Chartjunk secara total, termasuk efek tiga dimensi semu dan arsir yang bergetar. Dan keempat, terapkan teknik Small Multiples untuk data multivariat. Filosofi intinya satu: tunjukkan data di atas segalanya.",
    "Sekarang kita masuk ke metrik yang paling terkenal dari Tufte, yaitu Data-Ink Ratio. Tufte mendefinisikan bahwa setiap tetes tinta pada kertas, atau setiap piksel pada layar, harus didedikasikan untuk menampilkan informasi substantif data. Nilai idealnya mendekati satu koma nol. Jika rasionya di bawah nol koma lima, berarti grafik Anda dipenuhi dekorasi yang tidak penting. Ada lima aturan Tufte: tunjukkan data, maksimalkan rasio, hapus tinta non-data, hapus tinta data yang redundan, dan revisi berulang.",
    "Mari kita lihat contoh nyata transformasi gaya Tufte. Di sebelah kiri, grafik batang dengan latar abu-abu gelap, garis kisi merah yang tebal, arsir diagonal yang bergetar, dan bingkai hitam. Data latensi server tertimbun oleh semua dekorasi itu. Di sebelah kanan, versi Tufte-nya: batang horizontal biru yang diurutkan, tanpa garis bingkai, tanpa gridline, dan label langsung di ujung batang. Datanya persis sama, namun versi kanan langsung terbaca dalam sekejap. Inilah ergonomi kognitif.",
    "Chartjunk adalah elemen visual dekoratif yang tidak mengandung informasi analitis namun membebani kognisi audiens. Ada empat jenis utama. Pertama, Moiré Vibration, yaitu pola arsir diagonal yang bergetar di mata. Kedua, Heavy Gridlines, garis kisi yang terlalu tebal hingga menutupi data. Ketiga, Pseudo-3D Perspective, efek tiga dimensi pada diagram dua dimensi yang mendistorsi perbandingan angka. Keempat, Cute Graphics atau Ducks, yaitu ikon kartun yang mendominasi bidang data. Semua ini menaikkan beban kognitif eksternal yang harus dibasmi.",
    "Integritas grafis dijaga melalui metrik yang disebut Lie Factor. Rumusnya adalah besar efek pada grafik dibagi besar efek pada data riil, keduanya dalam persen. Nilai Lie Factor antara nol koma sembilan lima sampai satu koma nol lima berarti grafik jujur. Jika lebih dari satu koma nol lima, grafik melebih-lebihkan atau overstatement. Jika kurang dari nol koma sembilan lima, grafik justru menyamarkan perubahan yang sebenarnya signifikan atau understatement.",
    "Mari kita hitung sebuah studi kasus. Sebuah iklan melaporkan laba naik dari sepuluh miliar menjadi dua puluh miliar rupiah, artinya naik seratus persen. Namun, tinggi batang pada grafik digambar naik dari dua sentimeter menjadi delapan sentimeter, artinya naik tiga ratus persen. Maka Lie Factor-nya adalah tiga ratus dibagi seratus, sama dengan tiga koma nol. Karena jauh di atas satu koma nol lima, grafik ini tergolong misleading. Efek visualnya tiga kali lipat lebih dramatis daripada kenyataan. Ini pelanggaran integritas grafis.",
    "Teknik keempat Tufte adalah Small Multiples. Idenya adalah memecah satu grafik yang padat menjadi kisi-kisi grafik kecil dengan skala sumbu yang identik. Mata manusia dapat membandingkan pola antar panel secara instan. Aturan emasnya, skala sumbu wajib sama di semua panel agar perbandingan tetap jujur. Kebalikan dari teknik ini adalah memaksakan semua kelompok ke dalam satu grafik, yang menghasilkan spaghetti chart dengan garis saling bertumpuk dan tidak terbaca.",
    "Kita masuk ke Bagian Kedua: Kerangka Kerja Tamara Munzner. Beliau adalah profesor dari Universitas British Columbia yang merumuskan Nested Model, yaitu kerangka kerja bertingkat untuk merancang dan memvalidasi visualisasi data analitis. Model ini memastikan kita tidak melompat langsung ke kode sebelum memahami masalah dan data dengan benar.",
    "Nested Model Munzner terdiri dari empat tingkat. Tingkat pertama, Domain Problem Characterization, yaitu siapa pengguna dan apa masalah riilnya. Tingkat kedua, Data and Task Abstraction, yang menjawab pertanyaan What dan Why. Tingkat ketiga, Visual Encoding and Interaction Design, yang menjawab pertanyaan How, bagaimana data dipetakan ke marks dan channels. Tingkat keempat, Algorithm Design and Implementation, yaitu bagaimana kode merender visualisasi secara efisien.",
    "Mari kita bedah tingkat kedua, dimulai dari pertanyaan What atau tipe data. Ada tiga tipe kunci. Categorical atau nominal, yaitu kategori tanpa urutan seperti nama kota atau merek. Ordered atau ordinal, yaitu data yang punya urutan namun jarak antar nilainya tidak pasti, seperti tingkat pendidikan rendah, sedang, tinggi. Dan Quantitative, yaitu nilai numerik yang bisa dihitung, seperti suhu, pendapatan, atau latensi. Selain tipe, ada juga struktur dataset: tables, networks, fields, dan geometry.",
    "Selanjutnya pertanyaan Why, yaitu abstraksi task. Kita pisahkan antara Actions, yaitu tindakan yang dilakukan, dan Targets, yaitu apa yang ingin ditemukan. Actions meliputi Discover untuk mencari pola baru, Present untuk menyajikan insight, Locate untuk menemukan titik tertentu, dan Compare untuk membandingkan entitas. Targets meliputi Trend atau arah perubahan, Outlier atau pencilan ekstrem, Distribution atau bentuk sebaran, dan Correlation atau keterkaitan antar variabel.",
    "Pertanyaan How berkaitan dengan marks dan channels. Marks adalah tanda geometris: point untuk nol dimensi, line untuk satu dimensi, area untuk dua dimensi, dan volume untuk tiga dimensi yang jarang dipakai karena berisiko distorsi. Channels adalah saluran pengontrol properti marks, seperti posisi, panjang, sudut, luas, bentuk, rona warna, kecerahan, dan transparansi. Inti rekayasa visual adalah memilih pasangan marks dan channels yang paling akurat, bukan yang paling meriah.",
    "Munzner menegaskan adanya hierarki akurasi saluran visual. Untuk data kuantitatif atau magnitude, urutan dari yang paling akurat adalah posisi pada sumbu bersama, lalu posisi sumbu terpisah, lalu panjang batang, lalu sudut, lalu luas area, dan terakhir kecerahan warna. Untuk data kategorikal atau identity, yang paling efektif adalah posisi wilayah spasial dan rona warna, lalu bentuk ikon, dan terakhir pola isian. Aturan emasnya: angka gunakan posisi atau panjang, kategori gunakan warna atau bentuk. Jangan pernah ditukar.",
    "Dua prinsip Munzner yang menyaring keputusan desain adalah Expressiveness dan Effectiveness. Expressiveness Principle menyatakan saluran visual harus mengekspresikan hanya informasi yang ada di data, jangan menambah atribut yang tidak dimiliki data. Effectiveness Principle menyatakan gunakan saluran paling akurat untuk informasi terpenting. Uji cepatnya: jika data penting dipindah ke saluran yang lebih lemah dan insight-nya hilang, berarti desain Anda salah memilih saluran.",
    "Sekarang saatnya praktikum Python. Ada tiga praktikum menggunakan Matplotlib. Pertama, transformasi gaya Tufte: membandingkan grafik Before yang penuh chartjunk dengan grafik After yang minimalis, dengan menghapus semua spine, gridline, dan arsir, serta memakai direct labeling. Kedua, kalkulasi Lie Factor secara numerik. Ketiga, implementasi Small Multiples dengan grid dua kali dua, memakai sharex dan sharey, serta garis konteks abu-abu sebagai pembanding antar wilayah.",
    "Mari kita uji pemahaman melalui tiga pertanyaan reflektif. Pertama, jika laba naik lima puluh persen tetapi luas lingkaran digambar naik empat ratus persen, berapa Lie Factor-nya? Jawabannya delapan, jauh di atas batas dan tergolong misleading. Kedua, kenapa warna tidak boleh dipakai untuk menyandikan angka? Karena warna ada di dasar hierarki akurasi, hanya cocok untuk identitas. Ketiga, kapan kita boleh menulis kode pada level empat Nested Model? Setelah tiga tingkat sebelumnya selesai. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan ketiga ini. Kesimpulannya, desain grafis yang baik harus jujur secara matematis melalui Data-Ink Ratio dan Lie Factor, serta dirancang secara sistematis melalui Nested Model What-Why-How dari Munzner. Tugas praktikum tiga sudah tersedia di modul laboratorium. Pada pertemuan keempat minggu depan, kita akan masuk ke Data Wrangling dan Exploratory Data Analysis menggunakan Pandas. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
