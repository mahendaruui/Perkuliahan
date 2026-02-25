# Env Setup, JSX, Component, Props, Event, State

## 1. Environment Setup (Persiapan Lingkungan Kerja)

Untuk memulai project React Native termudah bagi pemula, disarankan menggunakan **Expo CLI**. Buka terminal (CMD/Powershell/BASH) lalu jalankan perintah:

```bash
# Membuat project baru bernama 'AplikasiPertama'
npx create-expo-app AplikasiPertama

# Masuk ke direktori aplikasi
cd AplikasiPertama

# Menjalankan server development (Metro Bundler)
npx expo start
```

## 2. Mengenal JSX

JSX (JavaScript XML) adalah ekstensi sintaks (syntax extension) untuk JavaScript standar. Dengannya, Anda bisa menulis elemen HTML-like `<Elemen />` langsung di dalam kode JavaScript.

Bentuk dasar pada file `App.js`:

```javascript
import React from 'react';
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, backgroundColor: 'white', justifyContent: 'center' }}>
      <Text>Selamat datang di React Native JSX!</Text>
    </View>
  );
}
```

- Tag `<View>` sejajar dengan `<div>` di web.
- Tag `<Text>` sejajar dengan `<p>` atau `<span>` di web.

## 3. Komponen (Components)

Komponen ibarat "blok bangunan" UI (User Interface). Ada dua jenis komponen utama di React:
1. **Class Component** (Gaya lama)
2. **Functional Component** (Standar modern menggunakan `function`)

Contoh membuat komponen anak bernama `Header`:

```javascript
const Header = () => {
    return (
        <View style={{ backgroundColor: 'blue', padding: 20 }}>
            <Text style={{ color: 'white' }}>Ini Header</Text>
        </View>
    );
};

// Menggunakannya di App utama
export default function App() {
  return (
    <View>
      <Header />
      <Text>Konten Utama di bawah Header</Text>
    </View>
  );
}
```

## 4. Props (Properties)

Props adalah singkatan dari *Properties*. Digunakan untuk mengoper (passing) data dari **Komponen Induk** (Parent Component) ke **Komponen Anak** (Child Component). Sifatnya _read-only_ (tidak bisa diubah oleh komponen anak).

```javascript
import React from 'react';
import { View, Text } from 'react-native';

const Profil = ({ nama, umur }) => {
  return (
    <View>
      <Text>Nama: {nama}</Text>
      <Text>Umur: {umur} Tahun</Text>
    </View>
  );
};

export default function App() {
  return (
    <View>
      {/* Mengoper data menggunakan atribut JSX ke komponen Profil */}
      <Profil nama="Budianto" umur={20} />
      <Profil nama="Siti" umur={21} />
    </View>
  );
}
```

## 5. State (Pengelolaan Kondisi)

Jika Props adalah data yang dilempar, maka `State` adalah data internal komponen yang bisa berubah (mutative). Perubahan data State akan di-*re-render* secara otomatis oleh antarmuka (UI).

- Pada Functional Component (yang modern), cara membuat state adalah menggunakan Hooks bernama `useState`.

## 6. Event (Penanganan Aksi / Input)

Berbeda dengan antarmuka web yang menggunakan `onClick`, di React Native Anda menggunakan `onPress` seperti pada komponen `<Button>` atau `<TouchableOpacity>`.

Contoh Aplikasi Counter (Iterasi State + Event):

```javascript
import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';

export default function App() {
  // 'angka' bernilai awal 0. Gunakan setAngka untuk mengubah valuenya.
  const [angka, setAngka] = useState(0);

  const tambahAngka = () => {
      setAngka(angka + 1); // Mengubah state
  };

  return (
    <View style={{ flex:1, alignContent:'center', justifyContent: 'center', margin: 20 }}>
      <Text style={{ fontSize: 30, textAlign: 'center' }}>Isi Angka: {angka}</Text>
      
      {/* Tombol yang ketika ditekan akan memanggil function tambahAngka */}
      <Button title="Tambah Angka" onPress={tambahAngka} />
      
      <Button title="Reset Data" onPress={() => setAngka(0)} color="red" />
    </View>
  );
}
```
