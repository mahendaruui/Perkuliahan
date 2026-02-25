# Mengatur Navigasi / Pindah Halaman Aplikasi

Untuk mendaftarkan dan berpindah-pindah antar "Halaman / Layar" di aplikasi ponsel React Native, dibutuhkan pustaka dari pihak ketiga (tetapi menjadi standard framework) yaitu **`React Navigation`**.

Berbeda dengan antarmuka URL web standard (menggunakan *link* router `<a href="">`), perpindahan menu seluler (Aplikasi) didasarkan pada perilaku interaksi pergerakan layar Native Mobile asli (Gaya Tumpukan Navigasi, Tab, Drawer/Sisi).

## Instalasi Dependensi React Navigation

Skenario menggunakan CLI Expo (Ketik di Terminal Project dan tekan enter):

1. Install Core dasar navigasi:
```bash
npm install @react-navigation/native 
```
2. Install Ekosistem Komponen Dasar Expo Integrasi:
```bash
npx expo install react-native-screens react-native-safe-area-context
```

3. Install Skema Gaya Tumpukan Native (Native Stack Navigasi) [Transisi bergeser seperti pada UI Android/iOS]:
```bash
npm install @react-navigation/native-stack
```

## Konsep Jenis Navigasi

Terdapat 3 pola (Pattern) Router Mobile yang harus anda pahami saat mengarsiteksi Aplikasi React Navigation :
- **Stack Navigation**: Transisinya menumpuk per layer layos (Pindah ke layar A -> lalu ke B -> lalu ke Layar Detail -> Tombol Kembali Kembali menumpuk keluar *pop/back* Layos layaknya browser menu aplikasi Whatsapp dan sebagainya).
- **Tab Navigation**: Menu navigasi cepat di Barisan Bawah (seperti layout Menu feed/explore beranda pada Navigasi Bawah Instagram, Shopee). Tab Router.
- **Drawer Navigation**: Papan Hamburger/Sidebar menu geser tersembunyi berwujud garis susun 3 dideret samping sebelah kiri layar.

## 1. Implementasi Stack Navigation Dasar

Berikut adalah cara merakit sistem 2 Layar Aplikasi yang bisa berpindah (Halaman Home -> Ke Halaman Tentang Aplikasi).

Ubah isi `App.js` Anda :

```javascript
// 1. Import sistem Core
import React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

// 2. Registrasi Stack Root Mesin Konstruksi
const Stack = createNativeStackNavigator();

// 3. Buat File Screens Komponen Halaman Satu
function HomeScreen({ navigation }) {  // <-- Parameter ajaib 'navigation' di-inject oleh Router otomatis.
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text style={{ fontSize: 24, padding: 10 }}>Pusat Beranda</Text>
      
      <Button
        title="Menuju ke Profil (Buka Layar Baru)"
        // Action routing Stack: push layos.
        onPress={() => navigation.navigate('Profil_Screen')}
      />
    </View>
  );
}

// 4. Buat File Screens Komponen Halaman Detail Dua
function ProfilScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Ini Halaman Detail Tentang Saya</Text>
      
      {/* Action Route Kembali Membuang Top Level Tumpukan Layer Layar ini pergi. */}
      <Button 
         title="Kembali ke Layar Sebelumnya (Back)" 
         onPress={() => navigation.goBack()} 
      />
    </View>
  );
}

// 5. Susunan Root Utama Pembungkus
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home_Menu">
        
        {/* Daftarkan layar-layar disini dan beri Label ID Unik nama jalurnya (Name) */}
        <Stack.Screen 
           name="Home_Menu" 
           component={HomeScreen} 
           options={{ title: 'Dashboard Utama' }} // Konfigurasi Label Header Atas Actionbar Android/IOS
        />
        
        <Stack.Screen 
           name="Profil_Screen" 
           component={ProfilScreen} 
           options={{ title: 'Bio Profil Data' }} 
        />
      
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

## Melempar Parameter Data antar Screen di Stack (Params Passing)

Pada Route A:
Melempar Data (Memutar Objek ID atau Nama ke Routing B):
```javascript
<Button
  title="Buka Halaman Rincian Data Kucing"
  onPress={() => {
    navigation.navigate('DetailHewan_Route', {
      itemId: 86,
      namaPeliharaan: 'Brody Si Kucing',
    });
  }}
/>
```

Pada Route B (Layar Penerimanya):
Parameter Navigasi dititipkan (ditempel pada) pada **Props Route**: `({ route, navigation })`.
```javascript
function LayarDetail({ route, navigation }) {
  // Parsing tangkapan Data Props Destructuring Object
  const { itemId, namaPeliharaan } = route.params;

  return (
    <View>
      <Text>Tangkapan ID: {itemId}</Text>
      <Text>Profile Nama Binatang: {namaPeliharaan}</Text>
    </View>
  );
}
```

## Referensi Dokumentasi React Navigation Resmi
Pustaka Dokumentasi ini memiliki contoh rumit lengkap navigasi Nested Bersarang hingga Konfigurasi Style Tampilan Aplikasi (Header Toolbar, Hide Nav, Custom Menu):
https://reactnavigation.org/docs/getting-started/
