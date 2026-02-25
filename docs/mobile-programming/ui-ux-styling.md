# UI/UX & Styling: Merancang Responsivitas menggunakan Flexbox

React Native menggunakan sintaks `style` (Javascript objek / StyleSheet) mirip CSS, namun semua prop (nama style) di-*convert* atau ditulis ke dalam standard format camelCase, misalnya di CSS ia dipanggil `background-color`, di React Native menjadi `backgroundColor`.

Semua komponen UI React Native secara bawaan menggunakan paradigma (mesin) layout yang dikenal di dunia design web, yakni **Flexbox**.

## Pengenalan Flexbox Component

Flexbox didesain untuk menyusun posisi letak / lebar (lebar tinggi responsif layout flex) konten, menjaga posisinya tetap baik (rapi) pada semua rasio perangkat ukuran HP tanpa hard-code piksel.

### 1. Perintah flexDirection (Arah Kotak)

Secara bawaan di React Native `flexDirection` adalah `'column'` (Menurun ke Bawah Vertikal). Berbeda dengan web yang defaultnya adalah `row`.

*   **column (default)**: Anak kolom ditumpuk dari Atas Ke Bawah.
*   **row**: Anak baris disusun berjajar dari Kiri Ke Kanan horisontal.
*   *column-reverse & row-reverse* (kombinasi opsional untuk membalikan urutan elemen di UI)

```javascript
/* Contoh Baris Memanjang Horisontal (ROW Array) */
<View style={{flex: 1, flexDirection: 'row'}}>
  <View style={{width: 50, height: 50, backgroundColor: 'tomato'}} />
  <View style={{width: 50, height: 50, backgroundColor: 'orange'}} />
  <View style={{width: 50, height: 50, backgroundColor: 'black'}} />
</View>
```

### 2. Perintah justifyContent (Rata Konten Sumbu Utama Axis)

Bergantung pada `flexDirection` yang berlaku:

*   `flex-start`: (Default) Rata Pinggir Awal/Atas
*   `flex-end`: Rata Ujung Belakang/Bawah
*   `center`: Rata Tengah Persis
*   `space-between`: Menjarak elemen sisi ke-sisi, kosong di tengah
*   `space-around`: Elemen mendapat ruang sama rata disekitarnya.

### 3. Perintah alignItems (Sumbu Lintas Axis Rata Samping)

Penyejejeran Rata Posisi. Misalkan Row = Sumbu ke Lintang Atas Kiri. Column = Sumbu Kiri Kanan Baris.

*   `flex-start`
*   `flex-end`
*   `center`
*   `stretch`: (Default jika kotak tidak punya lebar/tinggi absolute piksel). Anak akan memuai penuh menyesuaikan layar / induk Parent.

## 4. Konsep "Flex" Dimensi Pecahan Relatif

Daripada mematok tinggi lebar dalam piksel (width: 200, height: 500) yang bahaya pecah rasio jika pengguna punya HP berbeda, kita pakai rasio `flex: number` sebagai skala pembagi ruang proporsi layar yang dinamis dihitung berdasarkan persentase.

```javascript
<View style={{ flex: 1 }}> {/* Mengambil keseleruhan layar penuh flex 1 */}
  <View style={{ flex: 1, backgroundColor: 'red' }} />    {/* 1/6 area layar */}
  <View style={{ flex: 2, backgroundColor: 'darkorange' }} /> {/* 2/6 area layar */}
  <View style={{ flex: 3, backgroundColor: 'green' }} />  {/* 3/6 area layar (Setengah) */}
</View>
```

---
## Penggunaan Helper React Native `StyleSheet`

StyleSheet di sediakan untuk melarikan gaya style komponen-komponen agar terorganisir ke satu variabel objek, dan juga memberikan optimalisasi ID Caching ke Native Environment di sistem bawah (*under the hood* memory React Native). 

Penggunaan In-Line styling secara terus menerus sangat tidak direkomendasikan pada level Production, kecuali untuk *testing*.

```javascript
// BEST PRACTICE REACT NATIVE STYLING
import { StyleSheet, Text, View } from 'react-native';

const BerandaLayout = () => {
    return (
        <View style={mystyle.container}>
            <Text style={mystyle.judulUtama}>Sistem Perpustakaan</Text>
            <View style={mystyle.kartuBuku}>
                <Text style={mystyle.titleBuku}>React Untuk Mobile Modern</Text>
            </View>
        </View>
    );
};

const mystyle = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f5fcff',
        justifyContent: 'center',    // vertikal tengah
        alignItems: 'center',        // sumbu horisontal tengah
        padding: 10
    },
    judulUtama: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#128C7E',            // Warna Kustom Hexadecimal
        marginBottom: 20              // Margin renggang ke bawah komponen lain
    },
    kartuBuku: {
        width: '90%',                // Layout lebar 90% Relatif
        backgroundColor: 'white',
        borderRadius: 15,            // Lengkungan Elemen Radius Edge Kotak
        padding: 20,
        // Properti Drop Shadow Modern (Bayangan pada Card) 
        elevation: 5,                // Bayangan HP Android (Elevation)
        shadowColor: '#000',         // Bayangan HP iOS (Format Spesifik Shadow iOS)
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        shadowRadius: 3.84
    },
    titleBuku: {
        fontSize: 16,
        color: 'gray'
    }
});
```

*Tips:* Untuk membuat Desain (Card/Kartu material-design) komponen modern di atas, gunakan parameter `borderRadius`, serta `shadow`/`elevation` pada kotak kontainer/`View`.
