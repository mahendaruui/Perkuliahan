# Local Storage (Perbedaan RAM dengan Persistensi HP Memory Storage) 

Ketika Anda keluar dari aplikasi React Native (menutup aplikasi dengan men-*swipe* buang dari RAM Multitasking di handphone), semua state (Variabel Data List, User Form Profil Session Active Name) yang berjalan di komponen-komponen HP tersebut akan mati, sirna total, ter-reset karena ia terikat sebatas _Virtual Live Memory_.

Agar status "Pengguna Sudah Login", atau "Preferensi Tema (Dark/Light)", "Item Favorit Belanja", bisa terpasang permanen pada gadget ketika esok hari aplikasi kembali dibuka (App Restart), dibutuhkan tempat **Persistensi Data**.

Di pengembangan React Native Mobile, tool dasar yang menyimpan data teks persistensi permanen lokal handphone adalah layanan utilitas memori yaitu **`AsyncStorage`**.

## AsyncStorage: Penyimpanan Offline Native Sandboxed Internal

Async Storage bisa dipahami sebagai sebuah loker memori kecil (kapasitas teks MB kecil, non-SQLLite / relasional DB), sistem _Key-Value Store_ Asinkronus murni.
Format persis menyerupai sistem **LocalStorage / SessionStorage yang ada di web** namun bedanya, eksekusinya menggunakan tipe `Asynchronous/Promise` non-blocking UI (agar frame layar tidak lag nge-freeze karena operasi storage hardware penulisan flash I/O yang berat secara komputasional hardware layer).
Data akan terenkripsi Sandboxed, aplikasi ponsel lain tidak dapat memeriksa data storage private aplikasi Anda ini.

## Pemasangan Native AsyncStorage Package
Mulai update React Native versi 0.60+ The Facebook core module melepas penyimpanan storage ini menjadi ekstrak komunitas paket mandiri bernama _Community Package_.

Buka console CMD:
```bash
## Via command expo package cli:
npx expo install @react-native-async-storage/async-storage
```

## Memulai Sintaks Import Dasar 
```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';
```

### Operasi 1: SETTING DATA (Menyimpan Kunci Nilai)

Untuk menyimpan format string biasa / ID session Authentication Key / Pengaturan aplikasi:
```javascript
const simpanStatusLoginSistem = async (tokenApiDataSesiUser) => {
  try {
    // Fungsi ini mengeksekusi tulis / overwrite (Timpal nilai data)
    await AsyncStorage.setItem('@ID_SesiTokenLoginAplikasi', tokenApiDataSesiUser);
    console.log("SUKSES!: Token Berhasil terpasang Permanen!");
  } catch (errorIOMemoryPenulisan) {
    console.log("Memory Internal HP Penuh/Korupsi atau User Menolak Permintaan File Hak Akses (Error Write)", errorIOMemoryPenulisan);
  }
};
```
_Ingat_: Di AsyncStorage standar, paramater `(KunciNama/KeyIdentifier , Value/Pesan)` **WAJIB berbentuk STRING TEXT**. Jika Anda ingin menyimpan Array Keranjang Belanjaan / Format Obyek Daftar Nama Rumit, gunakan metode JSON.stringify Converter penguraian terlebih dahulu.

```javascript
/* Contoh Set Array Complex JSON Object Ke Local HP Memori DB */
const objCartProduct = [ { namabarang: 'Tas Emas', harga: 50 }, {namabarang: 'Sepatu', harga: 20} ];
// Di Parse Tulis...
await AsyncStorage.setItem('@cart_belanja_saya', JSON.stringify(objCartProduct));
```

### Operasi 2: MENGAMBIL / MEMBACA DATA (Get Item Key)

```javascript
const panggilKembaliPengaturanTemaGelap = async () => {
  try {
    // Cari data berdasar Kunci Text String nya
    const hasTheValueDataString = await AsyncStorage.getItem('@Pengaturan_ThemeGelapAktif');
    
    // Periksa kondisi apakah Kunci Teks itu sebelumnya pernah tertulis. (Bukan instalasi hp baru Pertama).
    if(hasTheValueDataString !== null) {    
      console.log("Nilainya Tema Gelap Tersimpan adalah: ", hasTheValueDataString);
      // Terapkan logik ke Komponen Layar disini!! State Update atau Navigasi pindah Layar Skip Login
    } else {
        console.log("User HP Ini belum pernah mengatur preferensi sama sekali di Handphone ini..");
    }
  } catch(errorIOBacaErorMemory) {
     console.error("Device Eror", errorIOBacaErorMemory);
  }
};
```
*Mengurai Kebalikan Ketinggian JSON Objek (Get Array Parser) :*
```javascript
const strCartBarang = await AsyncStorage.getItem('@cart_belanja_saya');
if(strCartBarang != null){
   const myArrDataHidupObjJson = JSON.parse(strCartBarang); // Uraikan/Revive Teks Kembali Jadi Variable JS
   console.log(myArrDataHidupObjJson[0].namabarang); // "Tas Emas"
}
```


### Operasi 3 & 4 (Hapus & Membersihkan Kosong Total Wiped!)

Fitur ini untuk Logout Membersihkan Session User atau Fitur Hancurkan Cart Storage Aplikasi:
```javascript
// A. Menghapus 1 Buah Nilai Kunci Saja
await AsyncStorage.removeItem('@ID_SesiTokenLoginAplikasi'); // Clear token saja.
```

```javascript
// B. Fitur Reset Menghapus KESELURUHAN Cache Seluruh Kunci Pada App ini di Memori Hardisk :
await AsyncStorage.clear();
```

*Note:* Peringatkan pengguna apabila membuat button dengan fitur fungsi `clear()`, KARENA akan menghancurkan semua record pengaturan personalisasi Local Storage yg pengguna pakai sebelumnya.
