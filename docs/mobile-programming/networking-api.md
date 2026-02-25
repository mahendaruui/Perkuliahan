# Bekerja Dengan Jaringan Data / Integrasi Networking (API)

Aplikasi mobile masa kini (seperti Instagram, Tokopedia, Gojek) tidak berdiri sendiri, mereka mengambil feed, meng-upload, dan melakukan *authentication/login* dengan berbicara kepada program back-end internet yang terpusat. Komunikasi perangkat seluler Anda dengan Basis Data Web Server Backend dilakukan dengan jembatan JSON API.

## 1. Fetch API (Standard Asli Browser Native)

React Native mendukung `Fetch API` bawaan Javascript Vanilla, persis dengan web development, untuk mengeksekusi request HTTP (REST). Konsep yang dipakai biasanya terbungkus dengan _Promises Object Javascript Async-Await_ dan format `JSON`.

**Bentuk dasar request HTTP GET Paling Ringkas:**
```javascript
// Memanggil daftar array public Users pada placeholder server testing JSON Placeholder.
const ambilDaftarMember = () => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json()) // Parsing Body JSON Format
      .then(jsonResult => {
           console.log(jsonResult);        // Output ke Terminal / Metro log Expo.
           // setResultState(jsonResult)  // Simpan JSON dalam State Flatlist Di Sini.
      })
      .catch((error) => console.error("API Error: ", error)); // Tangani status gagal Error HTTP Code / Timeout / No Internet.
}
```

## 2. Implementasi Pola `Async-Await` yang Baik

Dibandingkan menggunakan metode `.then()` berangkai (promise chaning) yang bisa menyebabkan *callback-hell* apabila terdapat banyak API saling bergantungan, lebih direkomendasikan mengkonversi pemanggilan ke bentuk eksekusi beruntun **Async / Await**.

```javascript
import React, { useEffect, useState } from 'react';
import { FlatList, Text, View, ActivityIndicator } from 'react-native';

export default function DaftarKontak() {
  const [loadingBar, setLoading] = useState(true);   // Loader layar
  const [userList, setUserList] = useState([]);       // Tempat penyimpanan daftar Server Data

  const dapatkanDataInternet = async () => {          // Function dideklarasi pakai mode Asynchronous
    try {
      // Tunggu Eksekusi 1: Pengambilan respon Web Server (Loading)
      const koneksiApi = await fetch('https://jsonplaceholder.typicode.com/users');
      // Tunggu Eksekusi 2: Olah respon Web JSON-ify Parser
      const jsonValid = await koneksiApi.json();    
      
      setUserList(jsonJsonValid);                     // Kirim state
    } catch (errorPesan) {
      alert("Uh-oh.. Koneksi Request Gagal Terjadi: " + errorPesan); // Error Exception Block
    } finally {
      setLoading(false); // Blok ini tereksekusi ketika baris proses Try atau Catch telah selesai seluruhnya (Tutup logo memuat layos data).  
    }
  };

  // Panggil eksekusi di Lifecycle Mounting komponen
  useEffect(() => {      
    dapatkanDataInternet();                 
  }, []);                                    

  // Loading Tampilan jika var UI Load berjalan
  if (loadingBar) {
     return <ActivityIndicator size="large" color="#0000ff" />; 
  }

  return (
    <View style={{ flex: 1, padding: 24 }}>
      <FlatList
        data={userList}
        keyExtractor={({ id }) => id.toString()}  // Standar unique string ID List item object JSON
        renderItem={({ item }) => (
          <Text style={{ fontSize:15 }}>
            Nama : {item.name}, Kota: {item.address.city}, Email : {item.email}
          </Text>
        )}
      />
    </View>
  );
}
```

## 3. Melakukan Metode Permintaan Lain (POST / PUT / DELETE API)

Seringkali di sistem (seperti Form Register, Log in, Menambah List Item Tugas Baru To-do, Menghapus Transaksi), request tidak hanya sekedar Get Reading Data Saja, namun memutasikan data Base server (Menulis Modifikasi DB). Paramater opsional kedua object Fetch (berisikan konfgiurasi header dan payload format objek Body) disertakan.

```javascript
  // Metod POST Form data submit baru
  const tambahPenggunaMobile Baru = async () => {
    try {
      const responseBack = await fetch('https://jsonplaceholder.typicode.com/users', {
        method: 'POST',                    // Request Type Form Add.
        headers: {
          Accept: 'application/json',      // Konfimasti tipe data penerima valid
          // Header penting tipe pengiriman Form tipe JSON Object Standard.
          'Content-Type': 'application/json',    
          
          // Token Authorization (seperti Auth Bearer Token/JWT untuk mengotentifikasi akses endpoint User VIP Session Login)
          // 'Authorization': 'Bearer asd-xyz-12345-api-token-rahasia'
        },
        body: JSON.stringify({             // Mengkonversi format variable input JSON menjadi Format Stringified Data yang Web Pahami Semburkan via internet..
           name: 'Agus Subiyakto',
           email: 'agus@gmail.com',
         })
      });

      const responseJSON_Terkonfirmasi = await responseBack.json();
      console.log('Status Terdaftar di ID Web Number : ', responseJSON_Terkonfirmasi.id);
    } catch(err) {
      console.error(err);
    }
}
```

## 4. Keuntungan Pihak Ke-Tiga: Axios (Lanjutan Alternatif Pilihan)

React native developer profesional lebih sering beralih kepada paket external bernama `Axios`. Axios adalah sistem Request HTTP canggih yang membalut perinting API *Promises Ajax Promise*.

**Keunggulan Axios ketimbang bawaan standar React Native Fetch:**
1. Anda bebas membungus *Base Root API Urlnya* ke interceptors modular (jika punya ratusan sistem service point Endpoint / API Server berbeda di perusahaan yang harus login otomatis re-fresh Token Bearer secara sinkron latar diam-diam aplikasi saat Expired Token).
2. Mendukung pembatalan Request Download Network Request / Timeout error custom setting lebih ringkas dan protektif .
3. Cukup singkat penulisannya karena dia mengotomatisasi konversi parameter menjadi tipe `.json()` dan Object Form data yang ribet tanpa `JSON.Stringify()`.

**Penggunaan Axios di Mobile Native:**
```bash
npm install axios
```
```javascript
import axios from 'axios';

// Pemanggilan Axios
const loadKatalogProduk = async () => {
    try {
        const responseKatalog = await axios.get("https://api.toko-abc.com/api/v1/produk");
        // Tanpa response JSON parsing!,  data asli object JSON ada di atribut: .data.
        console.log(responseKatalog.data.results);
    } catch(errAxios) {
         // Axios memiliki tipe pesan terstruktur errAxios.response | errAxios.message
    }
}
```
