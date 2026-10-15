#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 9 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m9/slide-XX.mp3
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
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-9-plotly-interaktif.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m9"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan kesembilan mata kuliah Visualisasi Data IFR309. Hari ini kita masuk ke babak baru, yaitu visualisasi interaktif dan web-ready menggunakan Plotly. Sampai saat ini, grafik yang kita buat dengan Matplotlib dan Seaborn bersifat statis. Hari ini kita akan membuat grafik yang dapat dijelajahi audiens, dengan zoom, hover, animasi, dan kontrol interaktif langsung di browser. Inilah kemampuan yang membedakan visualisasi data profesional di era web. Mari kita mulai.",
    "Pada pertemuan kesembilan ini, capaian pembelajaran kita adalah memahami arsitektur pustaka Plotly dan membedakan Plotly Express dengan Graph Objects, merancang kustomisasi interaksi pengguna seperti custom hover tooltip, zoom, pan, dan seleksi data, membangun visualisasi dinamis berbasis waktu dengan slider dan tombol pemutar, mengintegrasikan komponen UI internal seperti dropdown menus dan range slider, serta membangun dashboard multi-subplot dan mengekspornya ke format HTML mandiri.",
    "Mari kita mulai dari Bagian Pertama: Arsitektur Pustaka Plotly. Memahami arsitektur ini penting karena Plotly memiliki dua antarmuka dengan tingkat abstraksi yang berbeda.",
    "Plotly menyediakan dua antarmuka. Pertama, Plotly Express, disingkat px, yaitu high-level API yang cepat dan ringkas, sering hanya satu baris kode, dan otomatis terintegrasi dengan Pandas Tidy DataFrame. Antarmuka ini ideal untuk eksplorasi analitis cepat dan pembuatan chart standar. Kedua, Plotly Graph Objects, disingkat go, yaitu low-level API dengan objek go.Figure yang memberi kendali presisi atas hierarki JSON, data traces, dan layout. Antarmuka ini wajib digunakan untuk multi-subplot kustom, dual Y-axis, dan kontrol antarmuka internal. Aturan praktisnya, mulai dengan px untuk eksplorasi, lalu naik ke go saat butuh kontrol penuh.",
    "Secara internal, setiap objek grafik Plotly pada dasarnya adalah struktur data pohon kamus JSON. Di dalamnya ada kunci data yang berisi daftar traces, dan kunci layout yang mengatur judul, sumbu, serta komponen antarmuka seperti updatemenus. Spesifikasi JSON ini kemudian dikirim ke browser dan dirender oleh D3.js untuk grafik vektor, atau WebGL untuk jutaan titik data. Karena itulah grafik Plotly bersifat native interaktif, tanpa memerlukan server backend tambahan. Memahami struktur JSON ini berarti memahami cara mengontrol Plotly sampai level terdalam.",
    "Kita masuk ke Bagian Kedua: Fitur Interaktivitas Web-Ready. Inilah keunggulan utama Plotly yang membuatnya berbeda dari pustaka statis.",
    "Yang menarik, sebagian besar interaktivitas sudah kita dapatkan secara gratis. Tanpa satu baris kode tambahan, pengguna sudah bisa melakukan zoom untuk memperbesar area tertentu, pan untuk menggeser kanvas, hover untuk melihat nilai persis tiap titik, dan box select untuk memilih sekumpulan titik. Fitur zoom dan seleksi ini menyelesaikan masalah overplotting dengan cara yang elegan. Data ribuan baris yang saling menumpuk di grafik statis menjadi bisa dijelajahi, tanpa perlu membuang atau mengagregasi data. Integritas data tetap terjaga, sesuai prinsip yang kita pelajari di pertemuan ketiga.",
    "Fitur berikutnya adalah custom hover tooltip menggunakan parameter hovertemplate. Kita dapat mengganti tooltip bawaan dengan template teks berformat HTML, tebal, dan pemformatan angka atau mata uang profesional. Perhatikan polanya. Untuk tanggal, gunakan format persen d x pipe persen d spasi persen b spasi persen Y. Untuk angka dengan pemisah ribuan dan dua desimal, gunakan format persen y titik dua koma titik dua f. Dan untuk menghapus label seri yang mengganggu, gunakan tag extra kosong. Hasilnya adalah tooltip yang bersih dan profesional, misalnya menampilkan tanggal lima belas Maret dua ribu dua puluh empat dengan harga satu juta lima ratus ribu rupiah.",
    "Fitur ketiga adalah animasi temporal, yang populer dengan sebutan gaya Hans Rosling. Kita dapat menganimasikan evolusi data dari tahun ke tahun secara mulus menggunakan parameter animation_frame untuk sumbu waktu slider, dan animation_group untuk menjaga konsistensi identitas objek antar frame. Contohnya pada dataset gapminder, kita memetakan PDB per kapita ke sumbu X dengan skala logaritmik, angka harapan hidup ke sumbu Y, populasi ke ukuran bubble, benua ke warna, dan animasi_frame ke tahun. Hasilnya adalah visualisasi empat dimensi plus dimensi waktu, yang menceritakan perkembangan global selama lima dekade.",
    "Fitur keempat adalah kontrol UI internal, yaitu updatemenus. Kita dapat menambahkan tombol dropdown atau toggle button langsung di dalam canvas grafik, tanpa membutuhkan server backend. Caranya, tambahkan beberapa traces sekaligus tetapi hanya satu yang visible sama dengan True. Kemudian buat dropdown dengan tiga tombol, di mana setiap tombol mengubah kombinasi visible plus judul dan label sumbu. Ini memberi pengalaman dashboard sesungguhnya. Selain updatemenus, Plotly juga menyediakan rangeslider dan rangeselector, semuanya berjalan di browser tanpa server.",
    "Kita masuk ke Bagian Ketiga: Dashboard dan Ekspor. Setelah menguasai interaktivitas, kita menyusun beberapa panel menjadi dashboard utuh, lalu mengekspornya.",
    "Untuk membangun dashboard multi-subplot, kita menggunakan fungsi make_subplots. Kita menentukan jumlah baris dan kolom, mengaktifkan shared_xaxes untuk menyelaraskan sumbu X antar panel, dan mengatur row_heights untuk proporsi tinggi. Misalnya, panel satu berisi line chart tren harga saham dengan tinggi tujuh puluh persen, dan panel dua berisi bar chart volume transaksi dengan tinggi tiga puluh persen. Kita lalu menambahkan tiap trace dengan menentukan row dan col. Ini adalah versi interaktif dari teknik tata letak GridSpec yang kita pelajari pada pertemuan kelima.",
    "Keunggulan terbesar Plotly adalah output HTML mandiri. Dengan memanggil fig.write_html, kita menghasilkan satu berkas HTML yang sudah menyertakan pustaka JavaScript Plotly di dalamnya. Berkas ini dapat dibuka di komputer mana pun tanpa instalasi Python, cukup satu file yang siap dibagikan, dan interaktivitasnya tetap berjalan penuh. Untuk berkas yang lebih ringan, kita bisa memakai opsi include_plotlyjs sama dengan cdn, dengan catatan audiens memiliki koneksi internet.",
    "Kita masuk ke Bagian Keempat: Hands-on. Ada tiga praktikum interaktif yang akan kita kerjakan.",
    "Praktikum pertama adalah animasi temporal empat dimensi gaya gapminder. Kita memuat dataset gapminder, lalu membuat scatter dengan animation_frame tahun, animation_group negara, ukuran populasi, dan warna benua. Kita juga menambahkan hover_name agar nama negara muncul di header tooltip, dan mengaktifkan log_x untuk skala logaritmik sumbu X. Hasilnya diekspor ke berkas gapminder_animated.html, sebuah presentasi interaktif yang memukau.",
    "Praktikum kedua adalah dashboard multi-subplot interaktif dengan hovertemplate kustom. Kita membuat subplot dua baris satu kolom dengan shared_xaxes. Panel atas menampilkan tren harga saham harian dalam bentuk line chart dengan custom hovertemplate yang memformat rupiah, sedangkan panel bawah menampilkan volume transaksi dalam bentuk bar chart. Karena sumbu X tersinkronisasi, melakukan zoom pada satu panel akan ikut menggeser panel lainnya. Ini adalah versi interaktif dari konsep twin axes.",
    "Praktikum ketiga adalah kontrol UI dropdown menus tanpa server. Kita membuat satu figur dengan tiga traces, yaitu pendapatan, jumlah order, dan pelanggan baru, di mana awalnya hanya trace pertama yang terlihat. Lalu kita menambahkan updatemenus berisi tiga tombol. Ketika pengguna memilih satu metrik, kombinasi visible berubah, begitu pula judul dan label sumbu secara instan di browser. Hasilnya diekspor sebagai dropdown_metric_selector.html.",
    "Mari kita rangkum menjadi resep lima langkah Plotly web-ready. Langkah pertama, siapkan Tidy Data dari pertemuan keempat. Langkah kedua, mulai dengan Plotly Express untuk eksplorasi cepat. Langkah ketiga, tingkatkan ke Graph Objects dan make_subplots saat butuh multi-panel atau kontrol UI. Langkah keempat, kustomisasi interaksi dengan hovertemplate, updatemenus, animation_frame, dan rangeselector. Langkah kelima, ekspor HTML mandiri dengan write_html. Pola ini dapat dipakai ulang untuk setiap visualisasi interaktif.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, kapan beralih dari px ke go? Saat butuh kontrol presisi, seperti multi-subplot kustom, dual Y-axis, atau kontrol UI internal. Kedua, bagaimana Plotly mengatasi overplotting? Melalui interaktivitas zoom, pan, dan box select, tanpa perlu membuang data. Ketiga, kenapa hasil write_html disebut mandiri? Karena berkas HTML tersebut sudah menyertakan pustaka JavaScript Plotly, sehingga bisa dibuka di komputer mana pun tanpa instalasi Python. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan kesembilan ini. Kesimpulannya, visualisasi terbaik memberi audiens kendali untuk menemukan wawasannya sendiri. Kuasai perbedaan px dan go, manfaatkan hovertemplate untuk tooltip profesional, bangun animasi temporal, dan ekspor hasilnya sebagai HTML mandiri yang siap dibagikan. Tugas praktikum delapan sudah tersedia, termasuk animasi mandiri dan dropdown perubahan tema warna. Pada pertemuan kesepuluh minggu depan, kita akan masuk ke pemetaan geospasial dengan Folium. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
