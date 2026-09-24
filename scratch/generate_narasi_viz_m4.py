#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 4 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m4/slide-XX.mp3
- Menginjeksi array audioTranscripts ke dalam HTML presentasi.
"""
import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-4-data-wrangling-eda-pandas.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m4"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan keempat mata kuliah Visualisasi Data IFR309. Hari ini kita masuk ke bagian yang paling menyita waktu seorang praktisi data, yaitu Data Wrangling dan Exploratory Data Analysis menggunakan Pandas. Sebuah studi menyebutkan bahwa sekitar delapan puluh persen waktu seorang data scientist dihabiskan untuk membersihkan dan menyiapkan data, jauh sebelum grafik pertama dibuat. Hari ini kita akan menguasai keahlian krusial tersebut. Mari kita mulai.",
    "Pada pertemuan keempat ini, capaian pembelajaran kita adalah memahami prinsip Tidy Data serta perbedaan format Wide dan Long, melakukan data cleaning untuk missing values, duplikasi, dan inkonsistensi tipe data, mendeteksi outlier menggunakan Z-Score dan Interquartile Range, serta melakukan agregasi dan reshaping dengan groupby, pivot table, melt, dan crosstab. Alur kita terbagi empat bagian besar, ditutup dengan praktikum alur EDA lengkap.",
    "Mari kita mulai dari Bagian Pertama: Tidy Data. Sebelum data dapat divisualisasikan oleh pustaka modern seperti Seaborn atau Plotly, data harus berada dalam struktur yang benar. Dr. Hadley Wickham merumuskan tiga aturan baku yang menjadi fondasi dari Grammar of Graphics. Aturan-aturan ini sederhana, namun pelanggarannya adalah penyebab paling umum grafik yang gagal dibuat.",
    "Tiga aturan Tidy Data adalah sebagai berikut. Pertama, aturan kolom: setiap variabel statistik membentuk satu kolom. Kedua, aturan baris: setiap unit observasi unik membentuk satu baris. Ketiga, aturan tabel: setiap jenis entitas observasi membentuk satu tabel tersendiri. Uji cepatnya, jika satu kolom berisi campuran dua makna, misalnya nama bulan dan tahun digabung, maka data tersebut belum tidy, dan fungsi hue atau color di Seaborn akan kesulitan memetakannya.",
    "Sekarang kita bandingkan format Wide dan format Long. Perhatikan tabel yang sama. Pada format Wide, bulan Januari, Februari, dan Maret dijadikan nama kolom terpisah. Format ini nyaman untuk laporan manual, tetapi menyulitkan pemetaan visual. Pada format Long atau Tidy, kolom Bulan dan Penjualan berdiri sendiri sebagai variabel. Satu baris mewakili satu observasi. Untuk mengubah dari Wide ke Long, kita gunakan fungsi pd.melt. Sebaliknya, untuk kembali dari Long ke Wide, kita gunakan pivot table. Keduanya saling berkebalikan.",
    "Kita masuk ke Bagian Kedua: Data Cleaning. Prinsipnya adalah garbage in, garbage out. Data yang kotor akan menghasilkan wawasan yang palsu, sebagus apa pun grafiknya. Ada tiga hal utama yang harus kita tangani: nilai hilang atau missing values, duplikasi data, dan inkonsistensi tipe atau format.",
    "Mari kita klasifikasikan missing values. Ada tiga tipe. Pertama, MCAR atau Missing Completely at Random, yaitu data hilang murni karena kebetulan acak, misalnya gangguan transmisi sensor. Data seperti ini aman untuk di-drop jika jumlahnya di bawah lima persen, atau diimputasi dengan mean dan median. Kedua, MAR atau Missing at Random, yaitu pola hilang berkaitan dengan variabel lain yang teramati. Contohnya, responden wanita cenderung tidak mengisi kolom berat badan. Solusinya adalah imputasi berbasis grup. Ketiga, MNAR atau Missing Not at Random, yaitu data hilang berkaitan langsung dengan nilainya sendiri, misalnya nasabah dengan utang macet sengaja tidak mengisi pendapatan. Tipe ini membutuhkan pemodelan khusus.",
    "Setelah mendiagnosis, kita pilih strategi imputasi yang tepat. Untuk data hilang di bawah lima persen dan bersifat MCAR, kita bisa drop dengan dropna. Untuk kategori yang hilang, kita isi dengan konstanta seperti Other. Untuk data numerik, kita bisa isi dengan median. Dan yang paling kontekstual, untuk kasus MAR, kita imputasi berdasarkan median per grup menggunakan groupby dan transform. Perhatikan contoh kode. Kita mengisi kolom Revenue berdasarkan median per Kategori, lalu jika masih ada sisa nilai kosong, kita isi dengan median global.",
    "Ada musuh yang tidak terlihat dalam data teks, yaitu spasi tersembunyi dan kapitalisasi yang tidak konsisten. Perhatikan contoh ini. Banda Aceh dengan spasi di depan dan belakang, dan banda aceh dengan huruf kecil semua, dianggap sebagai dua kota yang berbeda oleh Pandas. Ini adalah bug senyap, karena tidak menimbulkan error, tetapi total penjualan menjadi terpecah dan ranking menjadi salah. Solusinya, bersihkan string dengan str.strip untuk menghapus spasi, dan str.title untuk menyeragamkan kapitalisasi. Untuk tanggal dengan format campuran, gunakan pd.to_datetime dengan parameter format mixed.",
    "Kita masuk ke Bagian Ketiga: Deteksi Outlier. Satu angka ekstrem, misalnya transaksi senilai lima ratus juta rupiah di tengah data ratusan ribu, bisa merusak seluruh skala grafik Anda. Semua batang lain akan terlihat rata dan tidak informatif. Karena itu, kita harus mendeteksi dan menangani pencilan sebelum membuat visualisasi.",
    "Metode pertama dan paling direkomendasikan untuk data tidak normal adalah Interquartile Range, atau IQR, yang juga dikenal sebagai Tukey's Fences. Rumusnya, IQR sama dengan Q3 dikurangi Q1. Batas bawah adalah Q1 dikurangi satu koma lima kali IQR. Batas atas adalah Q3 ditambah satu koma lima kali IQR. Sebuah titik dinyatakan sebagai pencilan jika nilainya kurang dari batas bawah atau lebih dari batas atas. Pada diagram kotak, kotak mewakili lima puluh persen data tengah, whisker menunjukkan satu koma lima kali IQR, dan titik di luar whisker adalah pencilan.",
    "Bagaimana memilih antara Z-Score dan IQR? Z-Score cocok untuk data yang berdistribusi normal, dengan ambang nilai absolut z lebih besar dari tiga. Sedangkan IQR bersifat non-parametrik dan tidak mengasumsikan distribusi tertentu. Fakta pahitnya, Z-Score dihitung menggunakan mean dan standar deviasi, yang justru ikut terdistorsi oleh outlier itu sendiri. Akibatnya, Z-Score bisa menyembunyikan pencilan ekstrem. Untuk data transaksi finansial yang kotor dan miring, IQR jauh lebih aman.",
    "Setelah mendeteksi outlier, jangan langsung menghapusnya. Ada tiga pilihan perlakuan. Pertama, drop atau filter, yang merapikan skala tetapi berisiko membuang kejadian langka yang justru penting, seperti indikasi fraud. Kedua, capping atau winsorizing, yaitu mengganti nilai di luar batas dengan nilai batasnya, sehingga skala tetap terjaga. Ketiga, pertahankan nilai asli tetapi tambahkan kolom penanda is_outlier, sehingga analisis dan visualisasi tetap transparan. Pilihan ini yang paling aman untuk audit.",
    "Kita masuk ke Bagian Keempat: Agregasi dan Reshaping. Setelah data bersih, kita perlu merangkum dan membentuk ulang data agar siap dianalisis dan divisualisasikan. Ada tiga senjata utama: groupby, pivot table, dan melt.",
    "Senjata pertama adalah groupby dengan multi-agregasi. Pola pikirnya adalah split, apply, combine. Pertama, pecah data berdasarkan kategori. Kedua, terapkan fungsi agregasi pada setiap grup, seperti sum, mean, dan count. Ketiga, gabungkan hasilnya menjadi tabel ringkas. Perhatikan bahwa kita bisa menghitung beberapa ringkasan sekaligus dalam satu perintah agg. Jangan lupa memanggil reset_index agar index grup berubah menjadi kolom biasa, sehingga siap untuk diplot.",
    "Senjata kedua adalah pivot table. Fungsi ini membuat tabulasi silang dua dimensi kategori menjadi sebuah matriks. Parameter index menentukan baris, columns menentukan kolom, values menentukan angka yang diagregasi, dan aggfunc menentukan cara merangkumnya. Parameter fill_value berguna untuk mengisi sel kosong dengan nol. Ingat, pivot table menghasilkan format Wide yang bagus untuk laporan, tetapi perlu di-melt sebelum diplot.",
    "Senjata ketiga adalah pd.melt, atau unpivot. Fungsi ini mengubah kolom menjadi baris, mengembalikan data dari format Wide ke format Long yang tidy. Ada tiga parameter penting. id_vars adalah kolom yang tetap sebagai identitas. var_name adalah nama kolom baru hasil peleburan nama-nama kolom. Dan value_name adalah nama kolom baru yang menampung nilainya. Dengan ini, alur lengkap kita menjadi: data kotor, dibersihkan, di-pivot untuk laporan, lalu di-melt untuk divisualisasikan.",
    "Mari kita rangkum menjadi alur EDA empat langkah yang bisa dipakai ulang untuk dataset apa pun. Langkah pertama, cleaning dan standarisasi: strip, title, dan parsing tanggal. Langkah kedua, imputasi missing values: modus untuk kategori dan median per grup untuk numerik. Langkah ketiga, deteksi dan capping outlier menggunakan fungsi IQR. Langkah keempat, agregasi dan reshaping dengan groupby, pivot table, dan melt. Pada praktikum, kita akan menerapkan keempat langkah ini pada dataset transaksi e-commerce kotor yang berisi outlier lima ratus juta rupiah dan missing values.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, kapan memakai melt dan kapan pivot table? Jawabannya, melt untuk Wide ke Long yang siap plot, dan pivot table untuk Long ke Wide sebagai tabulasi laporan. Kedua, kenapa IQR lebih aman daripada Z-Score untuk data kotor? Karena IQR berbasis kuartil dan tidak terdistorsi outlier. Ketiga, apa akibat spasi dan kapitalisasi yang tidak konsisten? Data akan dianggap sebagai dua entitas berbeda. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan keempat ini. Kesimpulannya, data yang rapi dan bersih adalah setengah jalan menuju visualisasi yang meyakinkan. Kuasai Tidy Data, bersihkan missing values dan outlier dengan benar, serta kuasai groupby, pivot table, dan melt. Tugas praktikum empat sudah tersedia, termasuk eksplorasi dataset Titanic. Pada pertemuan kelima minggu depan, kita akan masuk ke Matplotlib Fundamental dengan pendekatan berorientasi objek. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
