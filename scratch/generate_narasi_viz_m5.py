#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 5 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m5/slide-XX.mp3
- Menginjeksi array audioTranscripts ke dalam HTML presentasi.
"""
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-5-matplotlib-fundamental.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m5"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan kelima mata kuliah Visualisasi Data IFR309. Hari ini kita masuk ke bagian yang sangat praktis, yaitu Matplotlib Fundamental dengan pendekatan berorientasi objek. Matplotlib adalah pustaka visualisasi paling fundamental di ekosistem Python. Menguasainya berarti Anda memegang kendali penuh atas setiap elemen grafik, dari kanvas terluar hingga anotasi terkecil. Mari kita mulai.",
    "Pada pertemuan kelima ini, capaian pembelajaran kita adalah memahami perbedaan antarmuka prosedural pyplot dan antarmuka berorientasi objek, menguasai hierarki anatomi grafik Matplotlib, membangun visualisasi multi-panel asimetris dengan GridSpec serta sumbu ganda, dan menerapkan kustomisasi berstandar publikasi akademik, termasuk resolusi tinggi dan ekspor vektor.",
    "Mari kita mulai dari Bagian Pertama: Arsitektur Objek Matplotlib. Memahami arsitektur ini adalah kunci untuk menulis kode visualisasi yang bersih, modular, dan mudah dipelihara, terutama ketika grafik Anda menjadi kompleks.",
    "Matplotlib menyediakan dua pendekatan pemrograman. Pertama, antarmuka prosedural atau pyplot, yang bergaya MATLAB. Anda memanggil plt.plot, plt.title, dan plt.xlabel secara berurutan. Pendekatan ini memakai status global tersembunyi sehingga sulit dikendalikan ketika membuat multi-panel atau kustomisasi kompleks. Kedua, antarmuka berorientasi objek, di mana Anda menulis fig, ax sama dengan plt.subplots, lalu memanggil ax.plot dan ax.set_title. Pendekatan ini eksplisit, modular, dan menjadi standar wajib dalam riset akademik serta aplikasi industri.",
    "Untuk menguasai antarmuka berorientasi objek, kita harus memahami anatomi objek grafik Matplotlib sebagai sebuah pohon. Lapisan terluar adalah Figure, yaitu kanvas yang mengatur ukuran dan resolusi. Di atas Figure terdapat Axes, yaitu bidang koordinat tempat data dirender. Di dalam Axes terdapat Axis atau sumbu X dan Y, lalu Spines atau empat garis bingkai, visual primitives seperti garis dan batang, legend, colorbar, serta annotation. Ingat, Figure bukanlah Axes. Satu Figure dapat memuat banyak Axes, misalnya grid dua kali dua berarti empat Axes.",
    "Sekarang kita bahas cara membuat Figure dan Axes. Ada tiga pola dasar. Pertama, satu Axes dengan fig, ax sama dengan plt.subplots, lengkap dengan figsize dan dpi. Kedua, grid Axes dua kali dua yang mengembalikan array, sehingga kita akses axes dengan indeks baris dan kolom. Ketiga, penggunaan sharex dan sharey untuk berbagi sumbu. Parameter share ini sangat penting, khususnya untuk teknik small multiples yang kita pelajari pada pertemuan ketiga, agar perbandingan antar panel tetap jujur dan seragam.",
    "Kita masuk ke Bagian Kedua: Tata Letak. Dashboard profesional jarang berbentuk simetris. Sering kali kita membutuhkan satu grafik utama berukuran besar dan beberapa grafik ringkasan berukuran kecil. Untuk itu, Matplotlib menyediakan GridSpec dan Twin Axes.",
    "GridSpec memungkinkan kita memecah kanvas menjadi matriks grid yang fleksibel. Perhatikan contohnya. Kita membuat figure, lalu mendefinisikan GridSpec dua baris tiga kolom dengan width_ratios untuk mengatur proporsi lebar kolom. Panel utama di sebelah kiri menggunakan span seluruh baris dan kolom nol, ditulis gs titik dua koma nol. Panel kanan atas menggunakan baris nol dan kolom satu sampai tiga dengan notasi slice. Sedangkan dua panel kanan bawah masing-masing menempati baris satu kolom satu dan baris satu kolom dua. Dengan GridSpec, tata letak asimetris menjadi sangat mudah diatur.",
    "Fitur berikutnya adalah Twin Axes, yang berguna ketika kita ingin menampilkan dua metrik dengan skala berbeda dalam satu bidang. Contohnya volume produksi dalam satuan ton dan biaya per ton dalam satuan juta rupiah. Kita buat Axes pertama dengan plt.subplots, lalu memanggil ax1.twinx untuk membuat Axes kedua yang berbagi sumbu X namun memiliki sumbu Y sendiri di sisi kanan. Sumbu kiri menampilkan batang volume, dan sumbu kanan menampilkan garis biaya. Pastikan warna label setiap sumbu disamakan dengan warna serinya, dan berikan narasi yang jelas agar pembaca tidak salah tafsir.",
    "Kita masuk ke Bagian Ketiga: Estetika Publikasi. Grafik yang siap terbit ke jurnal atau skripsi memiliki standar tersendiri yang membedakannya dari grafik sekadar jadi.",
    "Ada empat langkah menyulap grafik standar menjadi publikasi-ready. Pertama, judul dan label harus berstruktur, dengan judul yang menyampaikan insight, bukan sekadar nama variabel. Kedua, buang spines non-data, khususnya garis bingkai atas dan kanan, sebagai penerapan langsung prinsip Tufte. Ketiga, gunakan grid tipis bermotif titik agar tidak mengganggu pola data. Keempat, legend tanpa kotak dengan frameon sama dengan False. Checklist ini memastikan grafik Anda bersih, profesional, dan mudah dibaca.",
    "Selain estetika, anotasi adalah alat untuk memberi makna pada grafik. Fungsi ax.annotate memungkinkan kita menunjuk titik tertentu dengan panah melengkung disertai kotak teks. Parameter xy menentukan titik tujuan panah, xytext menentukan posisi teks, dan arrowprops mengatur gaya panah. Dengan anotasi, grafik berubah dari sekadar menampilkan data menjadi menyampaikan temuan. Audiens langsung tahu ke mana harus melihat, tanpa harus mencari sendiri titik pentingnya.",
    "Kita masuk ke Bagian Keempat: Hands-on. Ada tiga praktikum Python yang akan kita kerjakan, semuanya menggunakan antarmuka berorientasi objek.",
    "Praktikum pertama adalah publication-ready line plot dengan confidence interval. Kita membandingkan konvergensi akurasi dua model AI selama lima puluh epoch. Model utama digambar dengan garis biru, dan rentang ketidakpastiannya ditampilkan menggunakan fungsi fill_between dengan transparansi rendah. Model baseline digambar dengan garis putus-putus berwarna abu-abu. Hasilnya diekspor sebagai PNG dengan dpi tiga ratus dan bbox_inches tight, sehingga siap dimasukkan ke jurnal atau skripsi.",
    "Praktikum kedua adalah dashboard multi-panel asimetris menggunakan GridSpec. Kita membangun satu kanvas berisi empat grafik berbeda. Panel utama di sebelah kiri menampilkan line chart tren pendapatan. Panel kanan atas menampilkan bar chart produk terlaris. Sedangkan dua panel bawah menampilkan histogram distribusi transaksi dan bar chart indeks kepuasan pelanggan. Judul tingkat figure diberikan melalui plt.suptitle, sementara setiap panel memiliki judulnya sendiri melalui set_title.",
    "Praktikum ketiga adalah dual-axis chart menggunakan twinx. Di sini kita menampilkan volume produksi sebagai diagram batang pada sumbu kiri, dan biaya produksi per ton sebagai grafik garis pada sumbu kanan. Kedua metrik memiliki satuan yang berbeda namun saling berkaitan. Melalui visualisasi ini, kita dapat menunjukkan bahwa peningkatan kapasitas pabrik ternyata mendorong penurunan biaya per unit, sebuah wawasan efisiensi yang penting bagi pengambil keputusan.",
    "Sekarang mari kita bahas format ekspor. Pilih format sesuai tujuannya. Untuk publikasi jurnal atau skripsi, gunakan format vektor seperti SVG atau PDF, karena tetap tajam pada segala resolusi. Untuk slide presentasi atau web, gunakan PNG dengan dpi tiga ratus. Hindari dpi rendah untuk hasil final. Selalu ekspor dari objek figure, bukan dari plt, dan gunakan parameter bbox_inches tight untuk memangkas margin kosong yang tidak perlu.",
    "Mari kita rangkum menjadi resep lima langkah grafik berorientasi objek. Langkah pertama, buat kanvas dengan fig, ax sama dengan plt.subplots, sertakan figsize dan dpi. Langkah kedua, gambar data dengan ax.plot, ax.bar, atau ax.scatter, dan sebutkan label tiap seri. Langkah ketiga, kustomisasi gaya Tufte. Langkah keempat, tambahkan anotasi dan legend. Langkah kelima, ekspor grafik ke format yang tepat. Pola ini dapat dipakai ulang untuk grafik apa pun.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, apa beda Figure dan Axes? Figure adalah kanvas terluar, Axes adalah bidang koordinat tempat data dirender. Kedua, kenapa sharex dan sharey penting untuk small multiples? Agar semua panel memakai skala yang identik sehingga perbandingan tidak menipu. Ketiga, kapan memakai twinx? Saat menampilkan dua metrik dengan skala berbeda dalam satu bidang. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan kelima ini. Kesimpulannya, antarmuka berorientasi objek memberi Anda kendali presisi atas setiap elemen grafik, GridSpec dan Twin Axes memperluas kemungkinan tata letak, dan kustomisasi berstandar publikasi memastikan grafik Anda layak terbit. Tugas praktikum lima sudah tersedia, termasuk grouped bar chart dan eksplorasi GridSpec. Pada pertemuan keenam minggu depan, kita akan masuk ke Seaborn untuk visualisasi statistik dan distribusi. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
