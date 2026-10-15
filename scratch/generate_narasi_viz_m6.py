#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 6 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m6/slide-XX.mp3
- Menginjeksi array audioTranscripts ke dalam HTML presentasi.
"""
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-6-seaborn-statistik-distribusi.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m6"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan keenam mata kuliah Visualisasi Data IFR309. Hari ini kita masuk ke pustaka Seaborn, yaitu pustaka visualisasi statistik yang dibangun di atas Matplotlib dengan integrasi mendalam bersama Pandas. Jika pada pertemuan kelima kita belajar menggambar secara manual dengan presisi, maka hari ini kita akan belajar membaca bentuk data secara statistik. Fokus kita adalah distribusi: bagaimana data tersebar, apakah simetris, apakah ada dua puncak, dan apakah ada pencilan. Mari kita mulai.",
    "Pada pertemuan keenam ini, capaian pembelajaran kita adalah memahami arsitektur pustaka Seaborn dan membedakan fungsi tingkat figur dan tingkat sumbu, memvisualisasikan distribusi univariat dan bivariat dengan histogram, KDE, dan ECDF, membandingkan sebaran multi-kategori dengan box plot, boxen plot, violin plot, dan swarm plot, melakukan analisis multi-kondisi menggunakan FacetGrid, serta menginterpretasikan interval kepercayaan bootstrap sembilan puluh lima persen.",
    "Mari kita mulai dari Bagian Pertama: Arsitektur Pustaka Seaborn. Memahami arsitektur ini mencegah kita kebingungan memilih fungsi, karena Seaborn membagi fungsinya menjadi dua tingkat yang jelas.",
    "Seaborn membagi fungsinya menjadi dua kelompok. Pertama, fungsi Figure-level, yang mengelola seluruh kanvas dan otomatis membentuk FacetGrid multi-panel. Contohnya displot untuk distribusi, catplot untuk komparasi kategori, dan relplot untuk hubungan serta tren. Kedua, fungsi Axes-level, yang menggambar langsung pada objek ax dari Matplotlib. Contohnya histplot, kdeplot, ecdfplot, boxplot, violinplot, barplot, dan scatterplot. Fungsi Axes-level lebih fleksibel karena dapat digabungkan ke dalam plt.subplots. Aturan praktisnya, untuk eksplorasi awal gunakan Figure-level, dan untuk dashboard final dengan kustomisasi Tufte gunakan Axes-level.",
    "Kekuatan utama Seaborn terletak pada integrasinya dengan Pandas DataFrame. Kita tidak lagi berbicara tentang array mentah, melainkan tentang nama kolom. Parameter data, x, y, dan hue langsung memetakan ke nama kolom DataFrame. Perlu diingat, Seaborn mewajibkan data dalam format Tidy. Di sinilah fungsi melt dan pivot_table yang kita pelajari pada pertemuan keempat berperan penting sebelum plotting dilakukan.",
    "Kita masuk ke Bagian Kedua: Distribusi. Sebelum menyimpulkan apa pun dari data, kita harus memahami bentuk sebarannya terlebih dahulu.",
    "Untuk memilih plot distribusi yang tepat, gunakan pohon keputusan berikut. Pertama, jika hanya menganalisis satu variabel tunggal atau univariat, gunakan histplot dengan KDE untuk melihat bentuk kurva, atau ecdf plot untuk fungsi distribusi kumulatif yang bebas bias. Kedua, jika membandingkan banyak kategori dengan jumlah sampel sedang, di bawah seribu per grup, gunakan violin plot yang mampu mendeteksi bimodalitas. Ketiga, jika sampel sangat besar di atas sepuluh ribu, gunakan boxen plot untuk menampilkan kuantil ekstrem secara detail. Dan jika sampel kecil di bawah seratus, gunakan swarm plot yang menampilkan seluruh titik observasi asli. Ukuran sampel menentukan jenis plot, bukan selera.",
    "Histogram dengan KDE adalah plot distribusi paling intuitif. Kita membuat subplots, lalu memanggil sns.histplot dengan parameter kde sama dengan True dan bins dua puluh. Kita juga menambahkan rug plot untuk menampilkan titik observasi asli di sumbu X. Kelemahan histogram adalah sensitivitasnya terhadap lebar bin. Jika kita mengubah nilai bins, bentuk kurva bisa berubah. Karena itu, jangan pernah menyimpulkan distribusi hanya dari satu pengaturan bin.",
    "ECDF, atau Empirical Cumulative Distribution Function, menjawab kelemahan histogram. ECDF bersifat bebas seratus persen dari bias binning, karena ia menggambar fungsi kumulatif dari nol sampai seratus persen. Kita dapat membaca persentil secara langsung. Misalnya, berapa nilai tagihan di mana lima puluh persen data berada di bawahnya. Kita bisa membandingkan dua grup dengan parameter hue, dan menambahkan garis bantu pada median. Untuk perbandingan distribusi yang jujur, ECDF adalah pilihan terbaik.",
    "Kita masuk ke Bagian Ketiga: Komparasi Kategori. Ketika kita punya beberapa kelompok yang ingin dibandingkan sebarannya, Seaborn menyediakan empat senjata utama.",
    "Senjata pertama adalah Box Plot, yang diperkenalkan oleh Tukey. Box plot meringkas distribusi menjadi lima angka, yaitu minimum, kuartil pertama, median, kuartil ketiga, dan maksimum, plus pencilan. Whisker pada box plot adalah batas Tukey, yaitu kuartil pertama dikurangi satu koma lima kali IQR hingga kuartil ketiga ditambah satu koma lima kali IQR, persis seperti metode deteksi outlier yang kita pelajari di pertemuan keempat. Keunggulan box plot adalah ringkas dan efisien untuk membandingkan sepuluh kategori sekaligus. Namun ada batasan kritis. Box plot menyembunyikan distribusi bimodal. Data dengan dua puncak bisa terlihat seperti distribusi seragam yang membosankan. Jadi, jangan hanya percaya pada kotak.",
    "Senjata kedua adalah Violin Plot, yang menggabungkan box plot dengan estimasi kontur kepadatan KDE. Violin plot menampilkan bentuk kepadatan penuh, sehingga kita dapat melihat bimodalitas, ekor panjang, dan celah data yang tersembunyi. Parameter split sama dengan True memungkinkan kita membandingkan dua grup dalam satu violin. Kita juga bisa menambahkan strip plot dengan jitter untuk menampilkan titik data asli, sehingga ada transparansi penuh terhadap kepadatan sampel. Namun hati-hati, parameter smoothing dapat menciptakan ekor semu yang sebenarnya tidak ada di data. Gunakan cut sama dengan nol agar violin tidak melebihi rentang data riil.",
    "Senjata ketiga dan keempat disesuaikan dengan ukuran sampel. Untuk sampel besar, di atas sepuluh ribu, gunakan Boxen atau Letter-Value Plot. Plot ini menampilkan kuantil ekstrem secara detail, jauh lebih informatif dari box plot biasa untuk data masif. Untuk sampel kecil, di bawah seratus, gunakan Swarm atau Strip Plot yang menampilkan seluruh titik observasi asli tanpa tumpang tindih. Transparansi penuh, audiens melihat setiap data, bukan ringkasan. Kombinasi favorit adalah violin plot dengan strip plot: kontur KDE untuk bentuk distribusi, dan titik jitter untuk membuktikan kepadatan sampel nyata.",
    "Mari kita bandingkan keempat plot distribusi kunci. Histogram dan KDE mewakili densitas, modus, dan skewness, unggul karena intuitif, namun sensitif terhadap lebar bin. Box plot mewakili lima angka dan outlier, unggul karena ringkas, namun menyembunyikan bimodal. Violin plot mewakili box plus KDE, unggul karena menampilkan bimodalitas, namun smoothing bisa membuat ekor semu. Dan ECDF mewakili persentil kumulatif, unggul karena bebas bias binning, namun kurang intuitif bagi audiens awam. Kesimpulannya, tidak ada plot terbaik secara absolut. Ada plot yang tepat untuk pertanyaan analitis tertentu.",
    "Kita masuk ke Bagian Keempat: Facet dan Estimasi. Dua topik terakhir yang melengkapi kemampuan analisis distribusi kita.",
    "FacetGrid adalah implementasi Small Multiples versi Seaborn, yang tentu saja mengingatkan kita pada prinsip Tufte di pertemuan ketiga. Dengan fungsi displot yang bersifat Figure-level, kita cukup menentukan col untuk memisahkan panel per kategori, hue untuk mewarnai per sub-kategori, dan kind untuk jenis plot. Seaborn otomatis membentuk kisi-kisi grafik. Alternatifnya, kita bisa mengontrol manual menggunakan FacetGrid dan map_dataframe. Yang penting, pastikan skala sumbu seragam agar perbandingan antar panel tetap jujur.",
    "Topik terakhir adalah Bootstrap Confidence Interval. Fungsi barplot pada Seaborn secara otomatis menghitung rata-rata beserta interval kepercayaan sembilan puluh lima persen. Cara kerjanya, Seaborn mengambil ribuan resample acak dari data, menghitung rata-rata tiap resample, lalu mengambil rentang dua koma lima persen sampai sembilan puluh tujuh koma lima persen. Penting untuk tidak salah tafsir. Error bar ini bukan standar deviasi. Ia menunjukkan ketidakpastian estimasi rata-rata, bukan sebaran data mentah.",
    "Untuk praktikum, ada tiga skrip yang akan kita kerjakan. Pertama, analisis distribusi univariat, dengan histplot plus rug plot di panel kiri dan ecdf plot komparatif di panel kanan, membandingkan bentuk versus kumulatif. Kedua, komparasi kategorikal, menggunakan violin plot split dengan inner quart plus strip plot dodge dengan jitter, untuk melihat distribusi pengeluaran restoran berdasarkan hari dan status merokok. Ketiga, estimasi statistik dengan interval kepercayaan sembilan puluh lima persen, menggunakan barplot dengan errorbar ci sembilan puluh lima dan capsize, menampilkan rata-rata tip per hari dan gender.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, kapan memakai ECDF dibanding histogram? Saat ingin membandingkan distribusi tanpa bias lebar bin, dan membaca persentil secara langsung. Kedua, kenapa box plot bisa menyesatkan pada data bimodal? Karena box plot hanya meringkas lima angka, sehingga dua puncak bisa terlihat seperti distribusi seragam. Solusinya gunakan violin plot. Ketiga, apa arti error bar pada barplot dengan errorbar ci sembilan puluh lima? Itu adalah interval kepercayaan sembilan puluh lima persen hasil bootstrap resampling, bukan standar deviasi sampel. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan keenam ini. Kesimpulannya, memahami bentuk distribusi adalah cara paling jujur memahami data sebelum menyimpulkan apa pun. Kuasai pemilihan plot yang tepat sesuai ukuran sampel, manfaatkan ECDF untuk perbandingan bebas bias, dan gunakan FacetGrid untuk analisis multi-kondisi. Tugas praktikum enam sudah tersedia, termasuk analisis bimodalitas dataset penguins. Pada pertemuan ketujuh minggu depan, kita akan masuk ke visualisasi relasi dan multivariat. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
