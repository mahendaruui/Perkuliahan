# React Hooks & Lifecycle

Konsep siklus hidup (Lifecycle) mengatur apa yang terjadi pada sebuah komponen React Native mulai dari saat komponen tersebut dirender ke layar, saat data state-nya berubah, hingga komponen tersebut dihancurkan (unmount) atau pindah ke halaman lain. 

Pada paradigma (konvensi) modern (Functional Component), eksekusi event lifecycle ini dikontrol dan diakses melalui **React Hooks**, di mana salah satu hook utamanya adalah `useEffect`.

## 1. Mengenal `useEffect`

Hook `useEffect` memungkinkan kita untuk menjalankan "efek samping" (Side Effects) dalam function component seperti (contoh: mengambil data API, modifikasi DOM/tampilan timer berjalan, langganan API sockets).

**Sintaks dasar useEffect:**
```javascript
useEffect(() => {
    // 1. Eksekusi program di sini
    
    return () => {
        // 2. Fungsi pembersihan opsional (dijalankan saat unmount/destroy)
    }
}, [
   /** 3. Array Dependensi (Opsional) **/
]);
```

## 2. Fase-Fase Lifecycle di Hooks

### Fase 1: Mounting (Komponen Dibuat/Dijalankan Pertama Kali)

Jika Anda memberikan **Array Kosong** `[]` sebagai argumen kedua, ia akan berperilaku layaknya `componentDidMount` (hanya berjalan satu kali saja saat aplikasi atau halaman dibuka pertama kali).

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';

export default function App() {
  const [data, setData] = useState("Memuat...");

  useEffect(() => {
    // Akan dipanggil sekali saat layar muncul pertama kali
    console.log("Aplikasi sedang mulai dijalankan...");
    
    // Anggap simulasi load data internet 3 detik
    setTimeout(() => {
      setData("Data Selesai Dimuat!");
    }, 3000);
  }, []); // <--- Array kosong (sangat penting untuk mencegah infinity loop render)

  return (
    <View style={{ flex: 1, padding: 50 }}>
      <Text>{data}</Text>
    </View>
  );
}
```

### Fase 2: Updating (Komponen Memperbarui View Karena State/Prop Berubah)

Jika Anda menyisipkan variabel referensi (states/props) ke dalam Array Ketergantungan, useEffect akan otomatis dieksekusi **hanya** ketika nama variabel di bracket tersebut nilainya berubah. Ini mirip fungsi `componentDidUpdate`.

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';

export default function TimerApp() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // Ini berjalan setiap kali tombol diklik / variabel 'count' berganti nilai
    console.log(`Nilai Count Telah Berubah Menjadi: ${count}`);
  }, [count]); // <--- Efek berjalan setiap var `count` diobservasi berubah

  return (
    <View>
      <Text>Anda menekan {count} kali</Text>
      <Button onPress={() => setCount(count + 1)} title="Klik Aku!" />
    </View>
  );
}
```

### Fase 3: Unmounting (Komponen Ditutup/Hancur)

Anda memanfaatkan *return statement* (Clean Up / Bersih-bersih) di akhir fungsi di dalam Use Effect. Ini berguna saat komponen ditinggalkan untuk mencegah memory-leak, layaknya `componentWillUnmount`.

```javascript
useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer detak 1 detik..');
    }, 1000);

    // Ini dipanggil sebelum komponen unmount
    return () => {
      clearInterval(timer); // Membersihkan cache aplikasi!
      console.log('Komponen telah ditutup, memory telah dibebaskan.');
    };
}, []);
```

## 3. Aturan Main Menulis Hooks

Meskipun terlihat mudah, Hooks (semua fungsi yang berawalan `use...`) memiliki batasan ketat dari React Native:

1. **Top-Level**: Anda hanya boleh memanggil Hook di baris atas fungsional komponen anda (segelum perintah return JSX dilontarkan/rendered).
2. **Jangan Dipanggil di Luar Component**: Use Effect & Use State hanya bisa hidup di dalam suatu Komponen React Native/JS, tidak berfungsi di fungsi murni javascript biasa ataupun di _Nested Conditionals_ atau _Loops_ (`if`, `for`, `while`).
