# Pengenalan Pemrograman Mobile & React Native

## Apa itu Pemrograman Mobile?

Pemrograman Mobile (Mobile Programming) adalah proses pengembangan perangkat lunak yang ditujukan secara spesifik untuk aplikasi pada perangkat bergerak (mobile devices) seperti smartphone dan tablet.

Secara umum, terdapat 3 pendekatan utama dalam pengembangan aplikasi mobile:

1. **Native App**: Aplikasi yang dikembangkan secara spesifik untuk satu platform menggunakan bahasa pemrograman aslinya (mis: Java/Kotlin untuk Android, Swift/Objective-C untuk iOS).
2. **Web App**: Aplikasi web yang didesain agar responsif dan terlihat seperti aplikasi mobile saat dibuka di browser (mis: PWA).
3. **Hybrid / Cross-Platform App**: Aplikasi yang menggunakan satu basis kode (codebase) yang dapat dijalankan di berbagai platform (Android dan iOS). Contoh: React Native, Flutter.

## Apa itu React Native?

React Native adalah kerangka kerja (framework) open-source yang dibuat oleh Meta (sebelumnya Facebook) yang memungkinkan developer membangun aplikasi seluler secara native menggunakan JavaScript dan React.

### Mengapa React Native?

- **Lintas Platform (Cross-Platform)**: Menulis satu kode (Write once) untuk Android dan iOS.
- **Kinerja Hampir Native**: React Native me-render komponen menggunakan UI native, bukan tampilan web (WebView), sehingga performanya sangat cepat.
- **Hot Reloading / Fast Refresh**: Melihat perubahan kode secara langsung di emulator/perangkat tanpa perlu compile ulang (rebuild) seluruh aplikasi.
- **Komunitas Besar**: Karena berbasis JavaScript dan React, komunitasnya sangat besar dengan ribuan rujukan dan pustaka (library) pihak ketiga.

## Arsitektur React Native

Pada level tinggi, arsitektur React Native terdiri dari 3 bagian utama:

1. **Native Thread**: Berjalan di platform (Android/iOS) menggunakan bahasa aslis (Java/Kotlin/Swift/Objective-C) untuk me-render UI.
2. **JavaScript Thread**: Tempat logika aplikasi Anda yang ditulis menggunakan JavaScript berjalan.
3. **The Bridge (Jembatan)**: Inti dari React Native versi lama yang menghubungkan komunikasi antara Native Thread dan JavaScript Thread (mulai bergeser ke arsitektur JSI/Fabric pada versi baru).

Ketika Anda menulis komponen `<View>` di React Native, framework akan menerjemahkannya menjadi `ViewGroup` di Android atau `UIView` di iOS melalui *bridge*.

## Persiapan Pembelajaran

Sebelum kita mulai coding pada pertemuan selanjutnya, pastikan Anda telah menyiapkan:

- **Node.js**: Environment runtime JavaScript.
- **Bowed IDE / Code Editor**: Rekomendasi: Visual Studio Code.
- **Android Studio** (untuk simulator Android) atau **Xcode** (hanya di macOS, untuk simulator iOS).
- [Alternatif] **Expo Go**: Aplikasi mobile yang bisa Anda install di HP Anda secara langsung untuk menjalankan kode React Native dari Node.js (via Expo CLI) tanpa perlu menginstall Android Studio/Xcode yang berat.

---

**Navigasi:**
- Lanjut ke materi berikutnya: [Dasar-Dasar React Native: Env Setup, JSX, Component, State](./dasar-react.md)
