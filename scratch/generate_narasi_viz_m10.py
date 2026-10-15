#!/usr/bin/env python3
"""Generate narasi audio (id-ID-ArdiNeural) untuk slide Pertemuan 10 Visualisasi Data.

- Menulis 20 MP3 ke docs/public/audio/visualisasi-data/m10/slide-XX.mp3
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
HTML = ROOT / "docs" / "public" / "presentasi" / "pertemuan-10-geospasial-folium.html"
AUDIO_DIR = ROOT / "docs" / "public" / "audio" / "visualisasi-data" / "m10"
VOICE = "id-ID-ArdiNeural"
RATE = "+0%"

TRANSCRIPTS = [
    "Selamat datang kembali rekan-rekan mahasiswa pada perkuliahan kesepuluh mata kuliah Visualisasi Data IFR309. Hari ini kita akan membahas visualisasi data geospasial dan pemetaan wilayah. Banyak data di dunia nyata memiliki dimensi lokasi, mulai dari sebaran fasilitas kesehatan, titik kecelakaan lalu lintas, hingga perbandingan indikator pembangunan antar provinsi. Peta adalah cara paling natural untuk menyampaikan informasi semacam ini, karena manusia memahami ruang secara intuitif. Hari ini kita akan belajar membuat peta interaktif dengan Folium. Mari kita mulai.",
    "Pada pertemuan kesepuluh ini, capaian pembelajaran kita adalah memahami konsep dasar data geospasial seperti sistem referensi koordinat WGS84 dan Web Mercator, geometri vektor, serta format GeoJSON; membangun peta interaktif berbasis web menggunakan pustaka Folium; menerapkan marker clustering, HTML popup, dan heatmap kepadatan spasial; merancang peta choropleth tematik yang menghubungkan data statistik dengan batas wilayah administratif; serta menggunakan GeoPandas untuk manipulasi data geospasial.",
    "Mari kita mulai dari Bagian Pertama: Fondasi Data Geospasial. Sebelum memetakan, kita harus memahami tiga hal dasar: geometri, sistem koordinat, dan format pertukaran data.",
    "Data geospasial dapat direpresentasikan dalam tiga geometri vektor utama. Pertama, Point atau titik nol dimensi, yaitu koordinat latitude dan longitude tunggal, contohnya lokasi rumah sakit, kampus, atau halte. Kedua, LineString atau garis satu dimensi, yaitu urutan titik yang terhubung membentuk jalur, contohnya jaringan jalan tol, jalur pipa gas, atau aliran sungai. Ketiga, Polygon atau area dua dimensi, yaitu area tertutup dengan cincin batas wilayah, contohnya batas administrasi provinsi, danau, atau zona rawan gempa. Prinsipnya, pilih geometri sesuai fenomena: titik untuk objek tunggal, garis untuk alur, dan area untuk wilayah.",
    "Selanjutnya, sistem referensi koordinat, atau CRS. Ada dua yang wajib kita bedakan. Pertama, Geographic CRS dengan standar WGS84 atau EPSG empat tiga dua enam, yang menggunakan satuan derajat sudut desimal, dari minus sembilan puluh sampai plus sembilan puluh untuk latitude, dan minus seratus delapan puluh sampai plus seratus delapan puluh untuk longitude. Ini adalah standar baku sensor GPS dan format GeoJSON. Kedua, Projected CRS dengan Web Mercator atau EPSG tiga delapan lima tujuh, yang memproyeksikan bola bumi ke bidang datar dua dimensi dalam satuan meter, dan digunakan oleh mesin tile peta web seperti OpenStreetMap, Google Maps, dan Leaflet. Jebakan klasiknya adalah menukar urutan latitude dan longitude. Folium menerima urutan latitude lalu longitude, sedangkan GeoJSON memakai longitude lalu latitude. Salah urutan, marker muncul di negara lain.",
    "Format pertukaran data spasial yang standar adalah GeoJSON. Ini adalah standar terbuka berbasis JSON yang dapat dibaca oleh hampir semua perangkat lunak. Strukturnya terdiri atas beberapa kunci utama. Pertama, type, yaitu jenis objek, misalnya FeatureCollection. Kedua, features, yaitu daftar fitur. Di dalam setiap fitur ada id yang berfungsi sebagai kunci penghubung ke data statistik, properties yang memuat atribut dan metadata, serta geometry yang mendefinisikan bentuk spasialnya. Kunci id inilah yang nantinya kita cocokkan dengan kolom kode wilayah pada DataFrame saat membuat peta choropleth.",
    "Kita masuk ke Bagian Kedua: Arsitektur Pustaka Folium. Folium adalah jembatan antara kemudahan Python dan kekuatan peta interaktif Leaflet.js.",
    "Cara kerja Folium terdiri atas tiga tahap. Pertama, sumber data spasial Python, bisa berupa Pandas DataFrame yang berisi kolom latitude dan longitude, GeoPandas GeoDataFrame, atau berkas GeoJSON. Kedua, mesin kompilasi Folium, yang menerjemahkan perintah Python kita menjadi kode JavaScript Leaflet.js di balik layar. Ketiga, peta interaktif Leaflet.js yang berjalan di browser, lengkap dengan tile layers, marker clustering, HTML popups, dan layer choropleth. Sama seperti Plotly pada pertemuan kesembilan, output Folium adalah berkas HTML mandiri yang bisa dibuka tanpa instalasi Python.",
    "Salah satu keputusan desain pertama adalah memilih latar peta, atau tile basemap. Ada tiga pilihan umum. CartoDB positron, yang minimalis dan terang, paling bersih untuk marker dan choropleth. CartoDB dark matter, yang gelap dan elegan, sangat cocok untuk heatmap kepadatan. Dan OpenStreetMap, dengan detail jalan, cocok untuk navigasi dan konteks lokasi. Pilihan latar peta menentukan seberapa jelas data kita terlihat di atasnya.",
    "Setelah peta dasar siap, kita menambahkan informasi melalui marker. Setiap marker dapat membawa tiga lapis informasi. Pertama, icon, yaitu warna dan simbol yang membedakan kategori, misalnya kampus berwarna ungu dan rumah sakit berwarna merah. Kedua, tooltip, yang muncul saat kursor diarahkan ke marker, biasanya berisi nama singkat. Ketiga, popup, yang muncul saat marker diklik, dan dapat berisi HTML lengkap dengan tabel atribut yang rapi. Perlu dicatat, penggunaan warna per kategori ini konsisten dengan prinsip hierarki saluran visual yang kita pelajari pada pertemuan ketujuh, yaitu warna sebagai saluran untuk identitas.",
    "Ketika jumlah titik bertambah banyak, peta akan menjadi penuh sesak dan lambat. Solusinya adalah Marker Clustering. Titik-titik yang berdekatan dikelompokkan menjadi satu lingkaran yang menampilkan jumlah titik di dalamnya. Ketika pengguna melakukan zoom, cluster akan memecah menjadi titik-titik individual secara otomatis. Aturan praktisnya, gunakan MarkerCluster bila jumlah titik melebihi lima puluh, agar performa browser tetap ringan dan peta tetap nyaman dilihat.",
    "Kita masuk ke Bagian Ketiga: Fitur Analitis. Kita beralih dari sekadar menampilkan titik, menuju analisis pola spasial dan perbandingan wilayah.",
    "HeatMap adalah teknik yang mengubah ribuan titik menjadi gradasi intensitas kepadatan. Kita menyiapkan daftar koordinat beserta bobotnya, lalu memanggil fungsi HeatMap dengan pengaturan radius, blur, dan max zoom. Kita juga menentukan gradien warna, dari biru untuk kepadatan rendah, hijau, oranye, hingga merah untuk kepadatan sangat tinggi. Untuk hasil maksimal, gunakan basemap gelap agar kontrasnya kuat. Heatmap sangat berguna untuk mengidentifikasi zona rawan kecelakaan, sebaran permintaan layanan, atau hotspot penyakit, yaitu pola-pola yang tidak terlihat dari tabel angka.",
    "Peta Choropleth adalah teknik mewarnai wilayah administratif berdasarkan data statistik. Kita memanggil fungsi Choropleth dengan parameter geo_data berupa batas wilayah GeoJSON, data berupa DataFrame statistik, columns untuk menentukan kolom kode wilayah dan nilai statistiknya, dan key_on yang menunjuk pada kunci penghubung di GeoJSON, misalnya feature.id. Kita juga menentukan palet warna dan legenda. Kunci keberhasilan peta choropleth terletak pada kecocokan persis antara nilai pada kolom identitas DataFrame dengan key_on GeoJSON. Jika ada perbedaan huruf besar kecil atau spasi tambahan, wilayah tersebut tidak akan terwarnai.",
    "Untuk membuat peta terasa profesional, ada dua plugin kecil yang sangat berguna. Pertama, MiniMap, yaitu peta mini di pojok yang memberikan konteks lokasi saat pengguna melakukan zoom, sehingga tidak kehilangan orientasi global. Kedua, LayerControl, yaitu panel untuk menyalakan atau mematikan layer seperti marker, heatmap, dan choropleth. Dengan LayerControl, kita bisa menyajikan banyak lapisan data dalam satu peta, dan pengguna bebas memilih lapisan mana yang ingin dilihat.",
    "Kita masuk ke Bagian Keempat: Hands-on. Ada tiga praktikum pemetaan yang akan kita kerjakan, semuanya menghasilkan berkas HTML interaktif.",
    "Praktikum pertama adalah membuat peta fasilitas publik di Banda Aceh. Kita membuat peta dengan pusat koordinat kota dan basemap CartoDB positron. Kita menambahkan MarkerCluster untuk mengelompokkan fasilitas, lalu melakukan perulangan untuk menambahkan setiap lokasi dengan popup HTML yang memuat tabel informasi, tooltip nama, serta ikon berbeda untuk tiap kategori. Kategori yang kita petakan meliputi kampus, rumah sakit, cagar budaya, dan museum. Hasilnya adalah berkas peta_fasilitas_aceh.html yang lengkap dengan clustering dan minimap.",
    "Praktikum kedua dan ketiga kita gabungkan dalam satu sesi. Pertama, peta kepadatan spasial. Kita menyimulasikan tiga ratus titik insiden lalu lintas atau permintaan layanan dengan distribusi normal di sekitar pusat kota, dan memberi bobot intensitas acak pada setiap titik. Data koordinat dan bobot ini dirender dengan fungsi HeatMap di atas basemap gelap, menghasilkan peta zona panas yang langsung menunjukkan area dengan kepadatan tertinggi. Kedua, peta choropleth tematik. Kita mendefinisikan GeoJSON sederhana untuk tiga provinsi, lalu menyiapkan DataFrame berisi skor Indeks Pembangunan Manusia atau IPM. Melalui fungsi Choropleth, kita menghubungkan kode provinsi pada GeoJSON dengan kode pada DataFrame, menggunakan palet YlGnBu dan menambahkan legenda, sehingga menghasilkan peta perbandingan wilayah yang dapat dibaca sekilas. Perhatikan insight gabungannya: heatmap menjawab pertanyaan di mana masalahnya padat, sedangkan choropleth menjawab wilayah mana yang tertinggal. Dua pertanyaan berbeda, dua peta berbeda.",
    "Mari kita uji pemahaman melalui tiga pertanyaan. Pertama, apa beda WGS84 dan Web Mercator? WGS84 adalah koordinat geografis dalam derajat desimal untuk GPS dan GeoJSON, sedangkan Web Mercator adalah proyeksi ke bidang datar bersatuan meter untuk tile peta web. Kedua, kapan perlu memakai MarkerCluster? Saat jumlah titik banyak, praktis di atas lima puluh, agar peta tetap ringan dan rapi. Ketiga, kenapa peta choropleth bisa gagal mewarnai wilayah? Karena ketidakcocokan kunci. Nilai kolom identitas di DataFrame harus cocok persis dengan key_on pada GeoJSON. Silakan klik setiap pertanyaan untuk memverifikasi jawaban Anda.",
    "Demikian perkuliahan kita pada pertemuan kesepuluh ini. Kesimpulannya, peta mengubah baris koordinat menjadi cerita tentang tempat, dan tempat selalu punya konteks. Kuasai fondasi sistem koordinat dan GeoJSON, manfaatkan Folium untuk peta interaktif, gunakan marker clustering untuk kepadatan, heatmap untuk pola spasial, dan choropleth untuk perbandingan wilayah. Tugas praktikum sembilan sudah tersedia, termasuk pemetaan fasilitas umum di kota domisili Anda dan eksplorasi GeoPandas. Pada pertemuan kesebelas minggu depan, kita akan masuk ke visualisasi data time series. Terima kasih, selamat belajar, dan sukses selalu untuk rekan-rekan mahasiswa sekalian.",
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
