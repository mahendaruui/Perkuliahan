# Komponen Utama (Core Components) React Native

Aplikasi React Native dibangun menggunakan sejumlah komponen dasar yang disediakan oleh framework. Komponen-komponen ini setara dengan elemen-elemen HTML di pengembangan web.

## 1. View

Komponen fundamental untuk membangun user interface (mirip dengan `<div>` di HTML). Mendukung tata letak (layout) menggunakan Flexbox, elemen style, event (touch handling), dan kontrol aksesibilitas (accessibility controls).

- Dapat bersarang (nested) di dalam View lainnya (mengelompokkan children layout).
- Bisa memuat hampir semua jenis elemen anak.

```javascript
import React from 'react';
import { View, Text } from 'react-native';

const App = () => (
  // View membungkus 2 element Text
  <View style={{ flex: 1, backgroundColor: 'blue' }}>
    <Text>Halo!</Text>
    <Text>React Native!</Text>
  </View>
);
```

## 2. Text

Komponen tunggal untuk menampilkan teks (mirip `<p>` atau `<h1>`). Di React Native, Anda **tidak boleh** meletakkan sebuah teks langsung di dalam `<View>` tanpa dibungkus komponen `<Text>`.

```javascript
<Text style={{ fontSize: 20, color: 'black', fontWeight: 'bold' }}>
   Ini judul halaman
</Text>

// Text di dalam Text (untuk menyisipkan format inline, misal Bold)
<Text style={{ fontStyle: 'italic' }}>
  Teks biasa <Text style={{fontWeight: 'bold'}}>dan ini teks tebal</Text>.
</Text>
```

## 3. Image

Digunakan untuk menampilkan gambar dari beragam sumber (lokal project, internet / server eksternal URI, ataupun format base-64).

1. Menampilkan gambar internal proyek (pakai format path `require`):
```javascript
import { View, Image } from 'react-native';

<Image source={require('./assets/logo-buku.png')} />
```

2. Menampilkan gambar daring/API (pakai format JSON Object `{ uri: URL }`):
```javascript
<Image
  source={{ uri: 'https://reactjs.org/logo-og.png' }}
  style={{ width: 400, height: 400 }} 
/>
// Wajib menyematkan style dimensi W dan H pada url/uri, jika tidak, gambar tidak akan muncul.
```

## 4. ScrollView

Secara default di React Native, komponen UI tidak bisa di-scroll ke bawah layaknya browser web ketika kontennya berlebih. `ScrollView` menyertakan kontainer gulir vertikal maupun vertikal-horizontal yang mengeksekusi scroll terhadap anak di dalamnya.

```javascript
import { ScrollView, Text, View } from 'react-native';

<ScrollView style={{ padding: 20 }}>
    <Text style={{ fontSize: 30 }}>Baris 1</Text>
    <View style={{ height: 100, backgroundColor: 'red' }} />
    <View style={{ height: 500, backgroundColor: 'blue' }} />
    <View style={{ height: 800, backgroundColor: 'green' }} />
    <Text style={{ fontSize: 30 }}>Baris Bawah</Text>
</ScrollView>
```
Catatan: Semua data yang ada di dalam Scroll View akan secara langsung di-*render* semua dalam satu memory. Cocok untuk halaman konten terstruktur dan data sedikit.

## 5. FlatList (Mengenal List View Dinamis)

Berbeda dari `ScrollView`, `FlatList` dioptimasi secara dinamis untuk menangani List Array (Data Tumpukan Besar seperti Daftar Kontak, Riwayat Pembelian) secara performatif. Ia hanya "merender baris elemen" yang terlihat di layar gadget saat itu, dan mendaur ulangnya saat bergulir ke atas/bawah untuk melestarikan/hemat Memory RAM HP.

Fungsi krusial dari *Flatlist*:
1. `data`: Variabel State/Array data sebenarnya
2. `keyExtractor`: Kunci ID Unik untuk identifier loop (mempercepat identifikasi update item list)
3. `renderItem`: Menggembalikan satu buah Komponen View Barisan (menggambar barisan per array loopnya)

```javascript
import React, { useState } from 'react';
import { FlatList, Text, View, StyleSheet } from 'react-native';

export default function AppList() {
  const dataBuku = [
    { id: '1', judul: 'Laskar Pelangi', penulis: 'Andrea Hirata' },
    { id: '2', judul: 'Bumi Manusia', penulis: 'Pramoedya Ananta Toer' },
    { id: '3', judul: 'Cantik Itu Luka', penulis: 'Eka Kurniawan' }
  ];

  /* Membuat Komponen Sub-Baris untuk Flatlist */
  const BarisanItemBuku = ({ title, author }) => (
    <View style={styles.item}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.caption}>Oleh: {author}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Penggambaran Flatlist List Builder */}
      <FlatList
        data={dataBuku}                             
        keyExtractor={(item) => item.id}           
        renderItem={({ item }) => (                  
          <BarisanItemBuku title={item.judul} author={item.penulis} />
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, paddingTop: 50 },
  item: { backgroundColor: '#f9c2ff', padding: 20, marginVertical: 8, marginHorizontal: 16 },
  title: { fontSize: 32 },
  caption: { fontSize: 14 }
});
```

---

Menguasai 5 Core Komponen ini merupakan modal terbesar untuk membuat lay-out (desain antarmuka) mobile yang rumit karena seluruh elemen kompleks dibangun di atas kumpulan dasar-dasar ini.
