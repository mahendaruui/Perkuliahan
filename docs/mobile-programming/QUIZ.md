# Quiz Pemrograman Mobile (React Native)

> **Petunjuk**: Pilih satu jawaban yang paling tepat untuk setiap soal pilihan ganda. Untuk soal esai/kode, jawab dengan singkat dan jelas.

---

## Bagian 1: Pengenalan Mobile Programming (Minggu 1)

**1.** Pendekatan pengembangan aplikasi mobile yang menggunakan **satu basis kode** untuk berjalan di Android dan iOS disebut…

- A. Native App
- B. Web App
- C. Hybrid / Cross-Platform App ✅
- D. Server-Side App

---

**2.** Bahasa pemrograman **asli (native)** yang digunakan untuk mengembangkan aplikasi Android adalah…

- A. Swift dan Objective-C
- B. JavaScript dan TypeScript
- C. Java dan Kotlin ✅
- D. Dart dan Go

---

**3.** React Native dikembangkan oleh…

- A. Google
- B. Microsoft
- C. Apple
- D. Meta (Facebook) ✅

---

**4.** Bagian dari arsitektur React Native yang menghubungkan **JavaScript Thread** dengan **Native Thread** pada versi lama disebut…

- A. JSI (JavaScript Interface)
- B. The Bridge ✅
- C. Metro Bundler
- D. Fabric

---

**5.** Ketika Anda menulis `<View>` di React Native, framework akan menerjemahkannya menjadi apa di Android?

- A. `<div>`
- B. `UIView`
- C. `ViewGroup` ✅
- D. `LinearLayout`

---

**6.** Fitur React Native yang memungkinkan developer melihat perubahan kode secara langsung **tanpa rebuild** seluruh aplikasi disebut…

- A. Live Reload
- B. Hot Module Replacement
- C. Fast Refresh / Hot Reloading ✅
- D. Cold Boot

---

## Bagian 2: JSX, Component, Props, State (Minggu 2)

**7.** Apa kepanjangan dari **JSX**?

- A. Java Syntax Extension
- B. JavaScript XML ✅
- C. JSON XML Extension
- D. JavaScript XAML

---

**8.** Di React Native, tag `<View>` setara dengan tag apa di HTML?

- A. `<span>`
- B. `<section>`
- C. `<div>` ✅
- D. `<body>`

---

**9.** Perhatikan kode berikut:

```javascript
const Profil = ({ nama, umur }) => {
  return <Text>Nama: {nama}, Umur: {umur}</Text>;
};
```

Pada kode di atas, `nama` dan `umur` adalah…

- A. State
- B. Props ✅
- C. Hooks
- D. Context

---

**10.** Sifat **Props** dalam React Native adalah…

- A. Dapat diubah oleh komponen anak
- B. Hanya dapat digunakan di Class Component
- C. Bersifat *read-only* dan tidak dapat diubah oleh komponen anak ✅
- D. Selalu bertipe string

---

**11.** Manakah cara yang **benar** untuk membuat sebuah state `nama` dengan nilai awal `"Budi"` menggunakan Hooks?

- A. `const nama = useState("Budi")`
- B. `const [nama, setNama] = useState("Budi")` ✅
- C. `const {nama} = useState("Budi")`
- D. `let nama = useState("Budi")`

---

**12.** Pada React Native, teks **tidak boleh** diletakkan langsung di dalam komponen `<View>` tanpa dibungkus komponen…

- A. `<Span>`
- B. `<Label>`
- C. `<Text>` ✅
- D. `<Paragraph>`

---

**13.** Perintah untuk membuat proyek React Native baru menggunakan **Expo CLI** adalah…

- A. `npm init react-native`
- B. `react-native init MyApp`
- C. `npx create-expo-app MyApp` ✅
- D. `npx create-react-app MyApp`

---

## Bagian 3: React Hooks & Lifecycle (Minggu 3)

**14.** Hook `useEffect` dengan **array kosong `[]`** sebagai dependensi akan berjalan…

- A. Setiap kali komponen di-render ulang
- B. Hanya sekali, saat komponen pertama kali dimuat (mounting) ✅
- C. Setiap kali ada state yang berubah
- D. Tidak pernah berjalan

---

**15.** Perhatikan kode berikut:

```javascript
useEffect(() => {
  console.log("Count berubah: " + count);
}, [count]);
```

`useEffect` di atas akan dijalankan ketika…

- A. Aplikasi pertama kali dibuka saja
- B. Komponen di-unmount
- C. Nilai variabel `count` berubah ✅
- D. Setiap kali ada props baru

---

**16.** Fungsi yang dikembalikan (return) di dalam `useEffect` digunakan untuk…

- A. Memperbarui state
- B. Melakukan pembersihan (*cleanup*) saat komponen di-*unmount* ✅
- C. Mengambil data API
- D. Menavigasi ke halaman lain

---

**17.** Jika `useEffect` dipanggil **tanpa** argumen array dependensi kedua, ia akan berjalan…

- A. Hanya saat mounting
- B. Hanya saat unmounting
- C. Setiap kali komponen di-render (berpotensi infinite loop) ✅
- D. Tidak berjalan sama sekali

---

**18.** Hook yang digunakan untuk menyimpan dan memperbarui data reaktif dalam sebuah komponen adalah…

- A. `useRef`
- B. `useContext`
- C. `useEffect`
- D. `useState` ✅

---

## Bagian 4: Core Components (Minggu 4)

**19.** Komponen React Native yang paling tepat untuk menampilkan **daftar data panjang** secara efisien (hanya merender item yang terlihat di layar) adalah…

- A. `ScrollView`
- B. `FlatList` ✅
- C. `ListView`
- D. `View`

---

**20.** Pada komponen `<Image>` React Native, jika gambar diambil dari **URL internet**, cara penulisan `source` yang benar adalah…

- A. `source="https://example.com/img.png"`
- B. `source={require('https://example.com/img.png')}`
- C. <span v-pre>`source={{ uri: 'https://example.com/img.png' }}`</span> ✅
- D. `src="https://example.com/img.png"`

---

**21.** Perbedaan utama antara `ScrollView` dan `FlatList` adalah…

- A. `ScrollView` hanya bisa digunakan untuk teks
- B. `FlatList` tidak mendukung scroll
- C. `ScrollView` me-render semua konten sekaligus; `FlatList` me-render hanya item yang tampak (lazy rendering) ✅
- D. Keduanya identik, hanya berbeda nama

---

**22.** Props wajib pada komponen `FlatList` untuk mengekstrak *key* unik setiap item adalah…

- A. `itemKey`
- B. `keyExtractor` ✅
- C. `uniqueKey`
- D. `id`

---

**23.** Komponen `<TextInput>` digunakan untuk…

- A. Menampilkan teks biasa
- B. Membuat tombol
- C. Menerima input teks dari pengguna ✅
- D. Menampilkan gambar

---

## Bagian 5: UI/UX & Flexbox (Minggu 5)

**24.** Di React Native, nilai **default** dari properti `flexDirection` adalah…

- A. `row`
- B. `row-reverse`
- C. `column` ✅
- D. `column-reverse`

---

**25.** Properti Flexbox yang digunakan untuk **memusatkan elemen secara horizontal dan vertikal** sekaligus adalah kombinasi…

- A. `textAlign: 'center'`
- B. `justifyContent: 'center'` dan `alignItems: 'center'` ✅
- C. `margin: 'auto'`
- D. `position: 'center'`

---

**26.** Nama properti CSS `background-color` dalam StyleSheet React Native ditulis sebagai…

- A. `background-color`
- B. `background_color`
- C. `BackgroundColor`
- D. `backgroundColor` ✅

---

**27.** Pada kode berikut, berapa persen layar yang ditempati kotak **hijau**?

```javascript
<View style={{ flex: 1 }}>
  <View style={{ flex: 1, backgroundColor: 'red' }} />
  <View style={{ flex: 2, backgroundColor: 'blue' }} />
  <View style={{ flex: 3, backgroundColor: 'green' }} />
</View>
```

- A. 33%
- B. 25%
- C. 50% ✅
- D. 60%

---

**28.** Properti `justifyContent: 'space-between'` akan…

- A. Meratakan semua elemen ke tengah
- B. Memberikan jarak yang sama di sekeliling setiap elemen
- C. Menempatkan elemen di sisi awal dan akhir dengan ruang kosong di antara ✅
- D. Merentangkan elemen untuk memenuhi kontainer

---

## Bagian 6: Navigasi (Minggu 6)

**29.** Library pihak ketiga yang menjadi standar untuk navigasi antar layar di React Native adalah…

- A. React Router DOM
- B. React Navigation ✅
- C. Vue Router
- D. Navigation Native

---

**30.** Perintah npm untuk menginstall **paket inti** React Navigation adalah…

- A. `npm install react-navigation`
- B. `npm install @react-navigation/router`
- C. `npm install @react-navigation/native` ✅
- D. `npm install navigation-react-native`

---

**31.** Pola navigasi yang menyerupai antarmuka **Instagram atau Shopee** dengan menu di bagian bawah layar adalah…

- A. Stack Navigation
- B. Drawer Navigation
- C. Tab Navigation ✅
- D. Modal Navigation

---

**32.** Untuk berpindah ke layar bernama `"Profil"` menggunakan Stack Navigation, perintah yang digunakan adalah…

- A. `navigation.push('Profil')`
- B. `navigation.go('Profil')`
- C. `navigation.open('Profil')`
- D. `navigation.navigate('Profil')` ✅

---

**33.** Komponen pembungkus utama yang **wajib** ada agar sistem navigasi React Navigation berfungsi adalah…

- A. `<StackContainer>`
- B. `<NavigationContainer>` ✅
- C. `<RouterProvider>`
- D. `<NavigationProvider>`

---

**34.** Untuk kembali ke layar sebelumnya pada Stack Navigation, perintah yang digunakan adalah…

- A. `navigation.back()`
- B. `navigation.pop()`
- C. `navigation.goBack()` ✅
- D. `navigation.previous()`

---

## Bagian 7: Networking & API (Minggu 7)

**35.** Format data yang paling umum digunakan saat berkomunikasi antara aplikasi mobile dan backend server melalui REST API adalah…

- A. XML
- B. CSV
- C. JSON ✅
- D. HTML

---

**36.** Perhatikan kode berikut:

```javascript
const response = await fetch('https://api.example.com/data');
const data = await response.json();
```

Apa fungsi dari `response.json()`?

- A. Mengkonversi respons ke format XML
- B. Mengirim data ke server
- C. Mem-parsing body respons HTTP menjadi objek JavaScript ✅
- D. Menyimpan data ke AsyncStorage

---

**37.** Blok `finally` pada pola `try-catch-finally` dalam pemanggilan API dieksekusi…

- A. Hanya jika terjadi error
- B. Hanya jika berhasil
- C. Selalu dieksekusi, baik berhasil maupun gagal ✅
- D. Tidak pernah dieksekusi

---

**38.** Komponen React Native yang digunakan untuk menampilkan **animasi loading** saat data sedang diambil dari API adalah…

- A. `<Loading />`
- B. `<Spinner />`
- C. `<ActivityIndicator />` ✅
- D. `<ProgressBar />`

---

**39.** Untuk melakukan request HTTP **POST** menggunakan Fetch API, konfigurasi tambahan yang perlu disertakan adalah…

- A. `method: 'POST'`, `headers`, dan `body` ✅
- B. Hanya URL yang berbeda
- C. Parameter `post: true`
- D. Import pustaka tambahan khusus POST

---

**40.** Pustaka pihak ketiga populer sebagai alternatif Fetch API yang menyederhanakan konfigurasi request HTTP adalah…

- A. Superagent
- B. Request
- C. Axios ✅
- D. HttpClient

---

## Bagian 8: Local Storage & AsyncStorage (Minggu 9–10)

**41.** Mengapa data yang disimpan di **State** React Native akan hilang saat aplikasi ditutup?

- A. Karena state disimpan di server
- B. Karena state bersifat *volatile* dan hanya ada di memori RAM selama aplikasi berjalan ✅
- C. Karena state hanya bisa menyimpan string
- D. Karena state tidak mendukung penyimpanan data

---

**42.** Perintah untuk menginstall AsyncStorage di proyek Expo adalah…

- A. `npm install async-storage`
- B. `npm install @react-native-community/async-storage`
- C. `npx expo install @react-native-async-storage/async-storage` ✅
- D. `expo add storage`

---

**43.** AsyncStorage menyimpan data dalam format…

- A. SQL Relasional
- B. Binary / File
- C. Key-Value Store (pasangan kunci-nilai) ✅
- D. XML Database

---

**44.** Untuk menyimpan **objek JavaScript** (bukan string) ke AsyncStorage, langkah yang diperlukan adalah…

- A. Langsung menyimpannya karena AsyncStorage mendukung semua tipe data
- B. Mengkonversi objek ke string menggunakan `JSON.stringify()` terlebih dahulu ✅
- C. Menggunakan `Object.toString()`
- D. Menyimpan setiap properti secara terpisah

---

**45.** Method AsyncStorage untuk **membaca** data berdasarkan kunci adalah…

- A. `AsyncStorage.readItem(key)`
- B. `AsyncStorage.fetchItem(key)`
- C. `AsyncStorage.loadItem(key)`
- D. `AsyncStorage.getItem(key)` ✅

---

**46.** Method AsyncStorage untuk **menghapus** sebuah item berdasarkan kunci adalah…

- A. `AsyncStorage.delete(key)`
- B. `AsyncStorage.clear(key)`
- C. `AsyncStorage.removeItem(key)` ✅
- D. `AsyncStorage.destroy(key)`

---

**47.** Saat membaca data dari AsyncStorage yang sebelumnya belum pernah disimpan, nilai yang dikembalikan adalah…

- A. `undefined`
- B. `0`
- C. `""` (string kosong)
- D. `null` ✅

---

## Bagian 9: Studi Kasus & Analisis Kode

**48.** Perhatikan komponen berikut:

```javascript
const [items, setItems] = useState([]);

useEffect(() => {
  fetch('https://jsonplaceholder.typicode.com/todos')
    .then(res => res.json())
    .then(data => setItems(data));
}, []);
```

Apa yang akan terjadi jika array dependensi `[]` **dihapus**?

- A. Kode tidak akan berfungsi sama sekali
- B. Data tidak akan pernah diambil
- C. `useEffect` akan terus memanggil API secara berulang tanpa henti (infinite loop) ✅
- D. Tidak ada perubahan

---

**49.** Perhatikan struktur navigasi berikut:

```javascript
<NavigationContainer>
  <Stack.Navigator>
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="Detail" component={DetailScreen} />
  </Stack.Navigator>
</NavigationContainer>
```

Layar mana yang akan tampil **pertama** saat aplikasi dibuka?

- A. `DetailScreen`
- B. Layar terakhir yang didefinisikan
- C. `HomeScreen` karena didefinisikan pertama ✅
- D. Ditentukan secara acak

---

**50.** Manakah pernyataan yang **BENAR** mengenai perbedaan Native App dan React Native?

- A. React Native menggunakan WebView sehingga performanya setara aplikasi web
- B. Native App dapat berjalan di Android dan iOS dengan satu kodebase
- C. React Native me-render komponen menggunakan UI native asli (bukan WebView), sehingga performa mendekati Native App ✅
- D. Native App lebih mudah dikembangkan karena satu kodebase

---

## Bagian 10: Soal Esai Singkat

**51.** Jelaskan perbedaan antara **`Props`** dan **`State`** dalam React Native! Kapan sebaiknya menggunakan masing-masing?

> **Jawaban Model:** Props adalah data yang dikirim dari komponen induk ke komponen anak dan bersifat *read-only* (tidak bisa diubah oleh komponen anak). State adalah data internal milik sebuah komponen yang dapat berubah dan menyebabkan komponen tersebut di-render ulang saat nilainya berubah. Gunakan Props untuk komunikasi data dari luar komponen; gunakan State untuk data yang berubah seiring interaksi pengguna dalam komponen itu sendiri.

---

**52.** Sebutkan **3 pola navigasi** utama di React Navigation beserta contoh aplikasi nyata yang menggunakannya!

> **Jawaban Model:**
> 1. **Stack Navigation** – Layar menumpuk seperti tumpukan buku; contoh: aplikasi WhatsApp (masuk ke chat detail, lalu kembali).
> 2. **Tab Navigation** – Menu tab di bawah layar; contoh: Instagram (Feed, Explore, Reels, Shop, Profile).
> 3. **Drawer Navigation** – Menu laci yang muncul dari sisi layar; contoh: Gmail (menu sidebar kiri).

---

**53.** Tuliskan kode React Native untuk menampilkan daftar nama dari array berikut menggunakan `FlatList`:

```javascript
const data = [
  { id: '1', nama: 'Andi' },
  { id: '2', nama: 'Budi' },
  { id: '3', nama: 'Cici' },
];
```

> **Jawaban Model:**
> ```javascript
> <FlatList
>   data={data}
>   keyExtractor={(item) => item.id}
>   renderItem={({ item }) => <Text>{item.nama}</Text>}
> />
> ```

---

**54.** Mengapa `AsyncStorage` menggunakan model **asynchronous** (async/await) dan bukan synchronous? Jelaskan!

> **Jawaban Model:** Operasi baca/tulis ke media penyimpanan (flash storage) memerlukan waktu dan bisa lambat. Jika dilakukan secara *synchronous*, operasi tersebut akan memblokir JavaScript Thread sehingga UI aplikasi menjadi tidak responsif / "freeze". Dengan model asynchronous, operasi storage dijalankan di background thread, sedangkan UI tetap berjalan lancar.

---

**55.** Seorang mahasiswa menulis kode berikut untuk menyimpan data keranjang belanja:

```javascript
const keranjang = [{ nama: 'Buku', harga: 50000 }];
await AsyncStorage.setItem('@keranjang', keranjang);
```

**Apa yang salah** dari kode di atas? Bagaimana cara memperbaikinya?

> **Jawaban Model:** Kesalahan: AsyncStorage hanya menerima nilai bertipe **string**, sementara `keranjang` adalah sebuah Array (objek). Perbaikan: konversikan array ke string JSON terlebih dahulu menggunakan `JSON.stringify()`:
> ```javascript
> await AsyncStorage.setItem('@keranjang', JSON.stringify(keranjang));
> ```
> Dan saat membacanya kembali, gunakan `JSON.parse()`:
> ```javascript
> const data = await AsyncStorage.getItem('@keranjang');
> const keranjang = JSON.parse(data);
> ```

---

## Kunci Jawaban

| No | Jawaban | No | Jawaban | No | Jawaban |
|:--:|:-------:|:--:|:-------:|:--:|:-------:|
| 1  | C | 11 | B | 21 | C |
| 2  | C | 12 | C | 22 | B |
| 3  | D | 13 | C | 23 | C |
| 4  | B | 14 | B | 24 | C |
| 5  | C | 15 | C | 25 | B |
| 6  | C | 16 | B | 26 | D |
| 7  | B | 17 | C | 27 | C |
| 8  | C | 18 | D | 28 | C |
| 9  | B | 19 | B | 29 | B |
| 10 | C | 20 | C | 30 | C |

| No | Jawaban | No | Jawaban | No | Jawaban |
|:--:|:-------:|:--:|:-------:|:--:|:-------:|
| 31 | C | 38 | C | 45 | D |
| 32 | D | 39 | A | 46 | C |
| 33 | B | 40 | C | 47 | D |
| 34 | C | 41 | B | 48 | C |
| 35 | C | 42 | C | 49 | C |
| 36 | C | 43 | C | 50 | C |
| 37 | C | 44 | B | 51–55 | (Esai) |

---

*Quiz ini mencakup materi Minggu 1–10 sesuai RPS Pemrograman Mobile.*
