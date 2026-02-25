# Manajemen Integrasi Lanjut: Library Lokasi Geografis & Peta (Maps)

Fitur pencarian LBS (Location Based System) berbasis sensor koordinat GPS, sering menjadi nilai fungsi utama (vital) pada banyak program populer seluler moden, misalnya Ojek Online driver-rider App tracking, Fitness Activity Tracker Langkah Jarak Lari, dan sebagainya.

Untuk mengakses Modul Perangkat Keras GPS Handphone (koordinat satelit `Lat`, `Lng`), kita butuh melakukan **Ekslporasi integrasi Sistem Permission Hak Akses (Izin)** sistem OS Android & iOS, dan memvisualisasikannya di sebuah Widget Map Kartograf (SDK Google Maps atau Mapkit Apple).

## 1. Expo-Location (Mengambil Sensor Titik Kordinat User Hardware)

Instalasi Sensor Library Bawaan Expo Ecosystem:
```bash
npx expo install expo-location
```
Modul API Eksternal ini memungkinkan Anda membaca geolokasi terkini ponsel, memantau *geofencing/Background tracking live*, ataupun konversi nama jalan tempat titik kota ke sebuah koordinat (Geocoding-Reverse Geocoding Map).

### Contoh Flow Konsep Memanggil Permintaan Posisi HP

1. Harus melakukan cek validitas status Izinkan Tracking GPS terlebih dahulu pada layar HP. Jika Anda langsung melibas meminta data Hardware Coordinate Sensor Satellit ke OS Ponsel tanpa minta Permohonan Persetujuan Security Layar Depan Izin, App akan *Crash / Force Close / Access Denied!*
2. Jika pengguna meng-GRANTS/Setuju "Allow Once" / "Allow All the time", Ambil datanya.
3. Tunggu respon Koordinat. Set result di State Object Komponen Utama.

Kode Penggunaan Request Standard `expo-location`:

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';

// Module API Periperal External (Hardware System Bindings)
import * as ModuleGPSLokasi from 'expo-location'; 

export default function PetaTrackingAplikasi() {
  const [dataPosisiku, setPosisiku] = useState(null);
  const [kalimatStatusSistem, setKalimatPesan] = useState('Menginisialisasi sistem radar gps satelit...');

  useEffect(() => {
    // Fungsi Anonymous IIFE di hook Async Langsung:
    (async () => {
      // #Langkah 1 Hak Akses Security Minta Izin
      let hakAksesTanyaUser = await ModuleGPSLokasi.requestForegroundPermissionsAsync();
      
      // Jika pengguna hp menge-klik Tombol Layar Popup Tolak "Deny Permission GPS", Block!!
      if (hakAksesTanyaUser.status !== 'granted') {
        setKalimatPesan('Dilarang/Permintaan Izin Akses Sensor Lokasi Ponsel di Tolak oleh Pemilik.');
        return; 
      }

      setKalimatPesan('Meminta Koneksi Sensor Detik ini...');

      // #Langkah 2: Proses memanen Koordinat Kalkulasi presisi Medium/Best Satelit.
      let koordinatPosisiResultRaw = await ModuleGPSLokasi.getCurrentPositionAsync({
           // Opsional Tuning Sensitivitas Akurasi (Low/Highest/BestForNavigations) (Hati-Hati, Tinggi = HP cepat Habis Baterai).
           accuracy: ModuleGPSLokasi.Accuracy.High 
      });

      // Update View React dengan Result Variable yang terdeteksi
      setPosisiku(koordinatPosisiResultRaw.coords); 
    })(); 
  }, []); // Run lifecycle once per Open Screen Module.

  // Render teks Kondisi Loading Waiter
  let layarPesanAkhirInfo = kalimatStatusSistem;
  
  if (dataPosisiku) {
    // Parsing String JSON Hasil Data Sensor Koordinat yang Panjang Menjadi Tulisan Cantik Titik Sumbu Bumi:
    layarPesanAkhirInfo = `TITIK POTENSI DITEMUKAN PADA KORDINAT MAPS \n LINTANG (Latitude): ${dataPosisiku.latitude} \n BUJUR (Longitude): ${dataPosisiku.longitude} \n KEPADATAN POSISI METER: ${Math.round(dataPosisiku.accuracy)} M`;
  }

  return (
    <View style={stylerefer.containerLayout}>
      <Text style={stylerefer.fontInfoSensor}>{layarPesanAkhirInfo}</Text>
    </View>
  );
}

const stylerefer = StyleSheet.create({
  containerLayout: { flex: 1, backgroundColor:"#fff", alignItems: 'center', justifyContent: 'center', margin: 25 },
  fontInfoSensor: { fontSize: 18, color:"blue", fontWeight:"bold", textAlign: "center" }
});
```


## 2. Rendering UI Modul Map Interaktif Peta Bumi: React-Native-Maps (Opsional Advanced)

Untuk menggambar komponen Kartografis Modul Peta Navigasi interaktif mirip App Google Map (Dengan dukungan Pin Markers, Polygons Rute Arsitektur, Tampilan Satelit):
Standard yang dipakai adalah dependensi `react-native-maps` SDK yang disupport oleh komunitas AirBnb dan React Group secara kuat.

Instalasi untuk base library:
```bash
npm install react-native-maps
```
**Catatan Modul Berat:** Library ini meng-implement *bridging code native* berat. (Jika menggunakan instalasi Expo Web CLI Biasa mungkin ada konfigurasi plugin ekstras. Paling stabil digunakan di Bare Workflow `React Native CLI Murni` atau sistem Development Build EXPO EAS.)

Komponen Render Map Interaktif Dasar dengan Tagging Komponen Markernya:
```javascript
import MapView, { Marker } from 'react-native-maps';
import { StyleSheet, View, Text } from 'react-native';

export default function PetaModulAplikasi() {
  // Sumbu tengah layar titik Jakarta Monas Default Konfigurasi Lensa Satelit
  const baseTengahanJakarta = {
    latitude: -6.1751,
    longitude: 106.8272,
    latitudeDelta: 0.0922,   // Setting Skala Level Zoom Lensa Vertikal Bawah Atap Peta
    longitudeDelta: 0.0421,  // Level Horisontal 
  };

  return (
    <View style={styles.container}>
      {/* Penggambaran Parent Layer SDK Native Google/Apple Maps Engine Core Modul Engine Canvas */}
      <MapView 
         style={styles.layolengMapeSistemAbsolute} 
         initialRegion={baseTengahanJakarta}
         showsUserLocation={true}    // Fitur Built in Marker Pin Biru titik Pengguna sendiri (GPS Required Permisson aktif!)
      >
          {/* Membuat Komponen Sub-Marker Pin Merah Custom Di Suatu Tempat */}
          <Marker
             coordinate={{ latitude: -6.1754, longitude: 106.8276 }}
             title="Monumen Nasional"
             description="Simbol Kebanggaan Jakarta."
             pinColor="red"  // Gaya opsi Warna marker standar bawaan 
          />
      </MapView>
      
      <View style={styles.bubbleStatusCardTengahAtas}>
         <Text>Aplikasi Pemandu LOKASI Wisata</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,  
  },
  bubbleStatusCardTengahAtas: { position:"absolute", top: 50, left: 30, right:30, padding: 15, elevation:10, backgroundColor: "white", borderRadius:10 , alignItems:"center"},
  layolengMapeSistemAbsolute: {
    width: '100%',
    height: '100%',   // Melebarkan Full Layar Canvas Rendering Peta Lensa!
  },
});
```

*Prasyarat Server Key Google Cloud Billing API Maps Production*: Apabila sistem dirilis ke Aplikasi App Store Apple / Playstore Google, Maps Native ini mewajibkan anda mengatur key token SDK Native `AndroidManifest.xml API KEY Map` dari Dashboard Google Cloud Platform Developer! Kegagalan integrasi Google Key menyebabkan peta akan Blank Putih kosong / Error layar Render Frame Abu-Abu!
