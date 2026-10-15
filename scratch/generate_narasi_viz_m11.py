#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 11 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m11/slide-XX.mp3
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
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-11-time-series.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m11"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan kesebelas mata kuliah Visualisasi Data IFR309. Hari ini kita akan membahas visualisasi data deret waktu dan finansial. Banyak fenomena di dunia nyata dicatat secara berurutan sepanjang waktu, mulai dari suhu harian, penjualan bulanan, hingga harga saham setiap hari. Data semacam ini menyimpan pola yang khas, dan hari ini kita akan belajar mengungkap pola tersebut secara visual. Mari kita mulai.",
    "Pada pertemuan kesebelas ini, capaian pembelajaran kita adalah memahami empat komponen fundamental data deret waktu, yaitu tren, musiman, siklus, dan residu; melakukan manipulasi indeks temporal serta pemulusan data menggunakan Moving Average sederhana dan eksponensial; melakukan dan menginterpretasikan dekomposisi deret waktu dengan model aditif dan multiplikatif menggunakan Statsmodels; membangun visualisasi finansial profesional berupa Candlestick chart dan volume subplot berbasis Plotly; serta mengidentifikasi pola musiman dan autokorelasi.",
    "Mari kita mulai dari Bagian Pertama: Empat Komponen Fundamental. Setiap deret waktu sebenarnya adalah campuran dari beberapa komponen yang dapat kita pisahkan.",
    "Data deret waktu adalah urutan pengamatan yang dicatat secara kronologis pada interval waktu yang seragam. Ia terdiri atas empat komponen. Pertama, Tren, yaitu kecenderungan arah pergerakan data jangka panjang, apakah naik, turun, atau stasioner. Kedua, Musiman atau Seasonality, yaitu pola fluktuasi periodik yang berulang pada interval waktu tetap, misalnya harian, mingguan, atau bulanan. Ketiga, Siklus atau Cycle, yaitu gelombang naik-turun jangka panjang tanpa durasi periode yang kaku, misalnya siklus ekonomi. Dan keempat, Residu atau Noise, yaitu variasi acak tak berpola yang tersisa setelah komponen tren dan musiman dihilangkan. Perlu diperhatikan, perbedaan utama musiman dan siklus adalah musiman memiliki periode tetap yang dapat diprediksi, sedangkan siklus panjangnya tidak kaku.",
    "Komponen-komponen ini digabungkan melalui dua model matematis. Pertama, model aditif, yang dinyatakan sebagai Y sama dengan T ditambah S ditambah C ditambah I. Model ini digunakan jika fluktuasi musiman bernilai relatif konstan dan tidak dipengaruhi oleh perubahan level tren data. Contohnya suhu ruangan atau penjualan es krim yang selisih puncaknya tetap sepanjang tahun. Kedua, model multiplikatif, yang dinyatakan sebagai Y sama dengan T dikali S dikali C dikali I. Model ini digunakan jika amplitudo variasi musiman membesar atau mengecil secara proporsional seiring kenaikan nilai tren. Contohnya penjualan ritel yang tumbuh sepuluh persen setiap bulan Desember, setiap tahun. Cara cepat menentukannya, jika grafik mekar atau amplitudo makin lebar saat tren naik, gunakan multiplikatif. Jika lebarnya seragam, gunakan aditif.",
    "Kita masuk ke Bagian Kedua: Manipulasi dan Pemulusan. Langkah pertama dalam analisis deret waktu adalah memastikan indeks waktunya benar, lalu memuluskan data untuk memisahkan sinyal dari derau.",
    "Manipulasi indeks temporal dilakukan melalui resampling, yaitu mengubah granularitas waktu. Kita mengubah indeks menjadi DatetimeIndex, lalu menurunkan frekuensi, misalnya dari harian ke mingguan dengan resample W, bulanan dengan ME, atau tahunan dengan YE. Perhatikan bahwa menurunkan frekuensi harus disertai fungsi agregasi seperti mean atau sum. Sebaliknya, menaikkan frekuensi atau upsample membutuhkan interpolasi untuk mengisi celah waktu yang tidak memiliki data.",
    "Setelah indeks siap, kita melakukan pemulusan data dengan Moving Average. Ada dua jenis utama. Pertama, Simple Moving Average atau SMA, yaitu rata-rata sederhana n periode terakhir, di mana semua titik berbobot sama. SMA menghasilkan garis yang halus, tetapi lambat merespons perubahan. Kedua, Exponential Moving Average atau EMA, yang memberi bobot lebih besar pada data terkini, sehingga lebih responsif terhadap perubahan terbaru. EMA adalah favorit dalam analisis finansial. Pada praktiknya, kita sering menampilkan beberapa window sekaligus, misalnya SMA tujuh hari untuk responsivitas dan SMA tiga puluh hari untuk melihat tren utama. Window kecil menghasilkan garis responsif namun berisik, sedangkan window besar lebih halus namun lambat.",
    "Selain garis tren, kita juga dapat menambahkan pita volatilitas atau confidence band. Kita menghitung standar deviasi bergulir, lalu menggambar area antara tren dikurangi satu standar deviasi dan tren ditambah satu standar deviasi. Pita yang melebar menandakan data sedang volatil, dan pita yang menyempit menandakan data stabil. Konsep ini sejalan dengan interval kepercayaan yang kita pelajari pada pertemuan Seaborn, yaitu menampilkan ketidakpastian, bukan hanya nilai tengah.",
    "Kita masuk ke Bagian Ketiga: Dekomposisi dan Pola. Di sini kita membongkar deret waktu menjadi komponen-komponennya secara otomatis.",
    "Pustaka Statsmodels menyediakan fungsi seasonal_decompose yang dapat memisahkan deret menjadi empat bagian dalam satu perintah. Kita menentukan model, apakah aditif atau multiplikatif, dan period, yaitu berapa observasi dalam satu siklus musiman. Misalnya, periode empat untuk data mingguan yang siklusnya bulanan. Fungsi ini mengembalikan empat atribut, yaitu observed atau data asli, trend atau komponen tren, seasonal atau komponen musiman, dan resid atau residu. Syaratnya, data harus memiliki indeks waktu berupa DatetimeIndex.",
    "Hasil dekomposisi ditampilkan dalam empat panel. Panel pertama, observed, menampilkan data asli apa adanya. Panel kedua, trend, menampilkan arah jangka panjang yang sudah halus. Panel ketiga, seasonal, menampilkan pola berulang yang diekstraksi. Dan panel keempat, residual, menampilkan sisa acak setelah tren dan musiman dihilangkan. Residu yang ideal tersebar acak di sekitar nol tanpa pola. Jika residu masih berpola, berarti ada komponen yang belum tertangkap oleh model, dan analisis kita perlu diperdalam.",
    "Untuk mengonfirmasi pola musiman secara kuantitatif, ada dua alat lanjutan. Pertama, Seasonal Subseries Plot, yang memecah data per unit musiman, misalnya tiap bulan, lalu memplot distribusinya berdampingan. Bulan dengan puncak yang konsisten menandakan peak season, sangat berguna untuk perencanaan stok. Kedua, Autocorrelation atau ACF, yang mengukur korelasi deret dengan versi tergeser dari dirinya sendiri. Puncak berulang pada lag tertentu mengonfirmasi periode musiman, dan alat ini menjadi fondasi untuk model peramalan. Menariknya, ACF pada dasarnya adalah matriks korelasi antara deret dan dirinya yang tergeser waktu, seperti konsep korelasi pada pertemuan ketujuh.",
    "Kita masuk ke Bagian Keempat: Visualisasi Finansial. Di sini kita menerapkan semua konsep deret waktu pada data pasar modal.",
    "Standar industri pasar modal adalah grafik Candlestick. Satu batang candlestick meringkas empat titik harga dalam satu periode, yaitu Open atau harga pembukaan, High atau harga tertinggi, Low atau harga terendah, dan Close atau harga penutupan. Bagian badan candlestick merepresentasikan rentang antara pembukaan dan penutupan, sedangkan sumbu atau wick merepresentasikan rentang tertinggi dan terendah. Ketika harga penutupan lebih tinggi dari pembukaan, candle berwarna hijau dan disebut bullish. Sebaliknya, ketika penutupan lebih rendah dari pembukaan, candle berwarna merah dan disebut bearish. Candlestick memberikan gambaran volatilitas intraday yang jauh lebih kaya dibandingkan grafik garis harga penutupan biasa.",
    "Untuk dashboard finansial yang lengkap, kita membangun dua panel menggunakan make_subplots dari Plotly. Panel pertama, dengan tinggi tujuh puluh lima persen, menampilkan candlestick beserta garis moving average dua puluh periode sebagai indikator tren. Panel kedua, dengan tinggi dua puluh lima persen, menampilkan batang volume transaksi, yang diwarnai hijau atau merah mengikuti arah candle hari itu. Karena sumbu X tersinkronisasi, melakukan zoom pada satu panel akan mengikuti panel lainnya. Ini adalah versi interaktif dari teknik multi-subplot yang kita pelajari pada pertemuan kesembilan.",
    "Untuk praktikum, ada tiga skrip Python yang akan kita kerjakan. Pertama, pemulusan data dengan Moving Average, menggunakan data sensor IoT selama tiga ratus enam puluh lima hari yang terdiri atas tren, musiman, dan noise. Kita menghitung SMA tujuh hari, SMA tiga puluh hari, serta pita volatilitas satu standar deviasi. Kedua, dekomposisi dengan Statsmodels, memanggil seasonal_decompose dengan model aditif dan periode empat, lalu menampilkan empat panel observed, trend, seasonal, dan residual. Ketiga, candlestick finansial interaktif dengan Plotly, menyimulasikan enam puluh hari bursa, lalu menambahkan candlestick, garis MA dua puluh, dan bar volume, kemudian mengekspornya ke berkas HTML interaktif.",
    "Mari kita rangkum menjadi resep lima langkah analisis deret waktu. Langkah pertama, siapkan indeks waktu dengan to_datetime dan set_index. Langkah kedua, lakukan resampling sesuai kebutuhan agar pola musiman stabil. Langkah ketiga, lakukan pemulusan dengan rolling mean untuk SMA dan ewm mean untuk EMA. Langkah keempat, dekomposisi dengan seasonal_decompose untuk memisahkan komponen. Langkah kelima, visualisasikan sesuai tujuan, Matplotlib untuk publikasi dan Plotly Candlestick untuk dashboard finansial interaktif.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, kapan memilih model dekomposisi multiplikatif? Ketika amplitudo fluktuasi musiman membesar atau mengecil secara proporsional dengan level tren, atau saat grafik terlihat mekar. Kedua, apa beda SMA dan EMA? SMA memberi bobot sama pada semua titik dalam window sehingga lebih halus namun lambat, sedangkan EMA memberi bobot lebih besar pada data terkini sehingga lebih responsif. Ketiga, apa yang ditunjukkan candlestick yang tidak ditunjukkan garis penutupan biasa? Yaitu volatilitas intraday, karena candlestick memuat empat harga, bukan hanya nilai akhirnya. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan kesebelas ini. Kesimpulannya, deret waktu adalah cerita yang berjalan sepanjang waktu, dan tugas kita adalah memisahkan sinyal dari derau agar ceritanya terbaca. Kuasai empat komponen dasar, manfaatkan Moving Average untuk pemulusan, gunakan dekomposisi Statsmodels untuk membongkar pola, dan kuasai candlestick untuk analisis finansial. Tugas praktikum sepuluh sudah tersedia, termasuk analisis peak season dan penambahan indikator Bollinger Bands. Pada pertemuan keduabelas minggu depan, kita akan masuk ke visualisasi untuk AI dan Machine Learning. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
