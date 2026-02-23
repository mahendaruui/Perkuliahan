# Minggu 7 — JSON & Fetch API (AJAX)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa dapat:
- Memahami format data **JSON** dan cara penggunaannya
- Mengambil data dari API menggunakan **Fetch API**
- Memahami konsep **Asynchronous JavaScript** (async/await, Promise)
- Menampilkan data dari *public API* secara dinamis di halaman web

---

## 1. JSON (JavaScript Object Notation)

**JSON** adalah format pertukaran data yang ringan, mudah dibaca manusia, dan mudah diproses mesin.

### Sintaks JSON

```json
{
  "nama": "Ahmad Mahasiswa",
  "nim": "21001234",
  "ipk": 3.75,
  "aktif": true,
  "alamat": null,
  "prodi": {
    "nama": "Teknik Informatika",
    "fakultas": "Fakultas Teknik"
  },
  "mataKuliah": [
    { "kode": "IF101", "nama": "Algoritma", "nilai": "A" },
    { "kode": "IF102", "nama": "Pemrograman Web", "nilai": "A-" }
  ]
}
```

### Aturan JSON

| Tipe Data | Valid | Tidak Valid |
|-----------|-------|-------------|
| String | `"teks"` | `'teks'` (tanda kutip tunggal) |
| Number | `42`, `3.14` | `NaN`, `Infinity` |
| Boolean | `true`, `false` | `True`, `False` |
| Null | `null` | `undefined`, `NULL` |
| Object | `{ "kunci": "nilai" }` | `{ kunci: "nilai" }` (kunci tanpa kutip) |
| Array | `[1, 2, 3]` | Koma di akhir: `[1, 2, 3,]` |

### JSON di JavaScript

```javascript
// 1. JSON.stringify() → Objek JS ke string JSON
const data = {
  nama: "Ahmad",
  nilai: [95, 87, 92],
  aktif: true
};
const jsonString = JSON.stringify(data, null, 2);
// '{\n  "nama": "Ahmad",\n  "nilai": [95, 87, 92],\n  "aktif": true\n}'

// 2. JSON.parse() → String JSON ke objek JS
const jsonStr = '{"nama":"Budi","usia":22}';
const objek = JSON.parse(jsonStr);
console.log(objek.nama); // "Budi"
console.log(objek.usia); // 22
```

---

## 2. Asynchronous JavaScript

JavaScript berjalan secara **single-threaded** — hanya mengeksekusi satu operasi dalam satu waktu. Untuk operasi lambat (network, disk), digunakan mekanisme **asynchronous**.

### Masalah: Callback Hell

```javascript
// ❌ Callback bertumpuk — sulit dibaca dan di-debug
ambilPengguna(id, function(pengguna) {
  ambilPostingan(pengguna.id, function(postingan) {
    ambilKomentar(postingan[0].id, function(komentar) {
      tampilkan(komentar);
    }, errorHandler);
  }, errorHandler);
}, errorHandler);
```

### Solusi 1: Promise

```javascript
// Promise — representasi nilai yang mungkin tersedia di masa depan
const janji = new Promise((resolve, reject) => {
  // Operasi async
  setTimeout(() => {
    const sukses = true;
    if (sukses) resolve("Data berhasil!");
    else reject(new Error("Gagal!"));
  }, 1000);
});

janji
  .then(data => console.log(data))  // "Data berhasil!"
  .catch(err => console.error(err));

// Promise chaining
ambilPengguna(id)
  .then(pengguna => ambilPostingan(pengguna.id))
  .then(postingan => ambilKomentar(postingan[0].id))
  .then(komentar => tampilkan(komentar))
  .catch(err => console.error("Error:", err));
```

### Solusi 2: async/await (Direkomendasikan)

```javascript
// async/await — menulis kode async seperti sync
async function muatDataPengguna(id) {
  try {
    const pengguna = await ambilPengguna(id);
    const postingan = await ambilPostingan(pengguna.id);
    const komentar = await ambilKomentar(postingan[0].id);
    tampilkan(komentar);
  } catch (error) {
    console.error("Terjadi kesalahan:", error.message);
  }
}
```

---

## 3. Fetch API

**Fetch API** adalah cara modern mengambil data dari server/API menggunakan JavaScript.

### Sintaks Dasar

```javascript
// GET Request (mengambil data)
async function ambilData(url) {
  try {
    const response = await fetch(url);
    
    // Cek apakah respons sukses
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json(); // Parse body sebagai JSON
    return data;
  } catch (error) {
    console.error("Gagal mengambil data:", error);
  }
}

// Pemanggilan
const pengguna = await ambilData("https://jsonplaceholder.typicode.com/users/1");
console.log(pengguna.name);
```

### POST Request (Mengirim Data)

```javascript
async function kirimData(url, data) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer token123"  // Jika perlu autentikasi
      },
      body: JSON.stringify(data)
    });
    
    if (!response.ok) throw new Error(`Error: ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error("Gagal mengirim:", error);
  }
}

// Contoh penggunaan
const mahasiswaBaru = { nama: "Ahmad", nim: "21001234", prodi: "Informatika" };
const hasil = await kirimData("/api/mahasiswa", mahasiswaBaru);
```

---

## 4. Contoh Lengkap: Kartu Pengguna dari API

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daftar Pengguna</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f1f5f9; padding: 32px 20px; }
    h1   { text-align: center; color: #1e293b; margin-bottom: 32px; }
    
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; max-width: 900px; margin: 0 auto; }
    
    .kartu { background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s; }
    .kartu:hover { transform: translateY(-4px); }
    
    .avatar { width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6, #8b5cf6); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: bold; margin-bottom: 12px; }
    .kartu h3 { color: #1e293b; margin-bottom: 4px; }
    .kartu .username { color: #64748b; font-size: 0.9rem; margin-bottom: 12px; }
    .kartu .info  { font-size: 0.85rem; color: #475569; margin: 4px 0; }
    .kartu .info span { font-weight: 600; }
    
    .loading { text-align: center; padding: 60px; color: #64748b; font-size: 1.1rem; }
    .error   { text-align: center; padding: 40px; color: #ef4444; background: #fee2e2; border-radius: 12px; }
  </style>
</head>
<body>
  <h1>👥 Daftar Pengguna</h1>
  <div id="output" class="loading">⏳ Memuat data...</div>

  <script>
    const API_URL = "https://jsonplaceholder.typicode.com/users";

    function buatKartu(pengguna) {
      const inisial = pengguna.name.split(" ").map(n => n[0]).join("").slice(0, 2);
      return `
        <div class="kartu">
          <div class="avatar">${inisial}</div>
          <h3>${pengguna.name}</h3>
          <p class="username">@${pengguna.username}</p>
          <p class="info">📧 <span>${pengguna.email}</span></p>
          <p class="info">📞 <span>${pengguna.phone}</span></p>
          <p class="info">🌐 <span>${pengguna.website}</span></p>
          <p class="info">🏢 <span>${pengguna.company.name}</span></p>
          <p class="info">📍 <span>${pengguna.address.city}</span></p>
        </div>
      `;
    }

    async function muatPengguna() {
      const output = document.getElementById("output");
      
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        
        const pengguna = await response.json();
        
        output.className = "grid";
        output.innerHTML = pengguna.map(buatKartu).join("");
        
      } catch (error) {
        output.className = "error";
        output.innerHTML = `
          <h3>❌ Gagal memuat data</h3>
          <p>${error.message}</p>
          <button onclick="muatPengguna()">Coba Lagi</button>
        `;
      }
    }

    muatPengguna();
  </script>
</body>
</html>
```

---

## 5. Contoh: Pencarian dengan Debounce

```javascript
// Debounce — tunda eksekusi hingga pengguna berhenti mengetik
function debounce(fungsi, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fungsi.apply(this, args), delay);
  };
}

// Pencarian dengan debounce
const inputCari = document.getElementById("input-cari");
const hasilCari = document.getElementById("hasil-cari");

const cariPengguna = debounce(async (query) => {
  if (!query.trim()) {
    hasilCari.innerHTML = "";
    return;
  }
  
  hasilCari.innerHTML = "⏳ Mencari...";
  
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users`);
    const semua = await response.json();
    
    const hasil = semua.filter(u => 
      u.name.toLowerCase().includes(query.toLowerCase()) ||
      u.email.toLowerCase().includes(query.toLowerCase())
    );
    
    hasilCari.innerHTML = hasil.length
      ? hasil.map(u => `<div class="item">${u.name} — ${u.email}</div>`).join("")
      : `<p>Tidak ada hasil untuk "<strong>${query}</strong>"</p>`;
    
  } catch (e) {
    hasilCari.innerHTML = "❌ Gagal mencari. Coba lagi.";
  }
}, 400); // Tunggu 400ms setelah pengguna berhenti mengetik

inputCari.addEventListener("input", (e) => cariPengguna(e.target.value));
```

---

## 6. Public API untuk Praktikum

| API | URL | Data |
|-----|-----|------|
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com` | User, Post, Comment (dummy) |
| **PokeAPI** | `https://pokeapi.co/api/v2/pokemon` | Data Pokémon |
| **Open Meteo** | `https://api.open-meteo.com` | Cuaca |
| **REST Countries** | `https://restcountries.com/v3.1/all` | Data negara |
| **TheCatAPI** | `https://api.thecatapi.com/v1/images/search` | Foto kucing |
| **Quotes API** | `https://api.quotable.io/random` | Kutipan motivasi |

---

## 🏋️ Latihan

1. Ambil data dari `https://restcountries.com/v3.1/all` dan tampilkan kartu untuk 20 negara pertama (nama, bendera, populasi, wilayah).
2. Buat fitur pencarian negara berdasarkan nama dengan debounce.
3. Buat aplikasi cuaca mini menggunakan **Open Meteo API** (masukkan koordinat kota, tampilkan suhu dan kondisi cuaca).
4. Buat galeri foto dari **PokeAPI** — klik pada Pokémon untuk melihat detail (stats, type, ability).

---

## 📚 Referensi

- [MDN Web Docs — Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [MDN Web Docs — async/await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
- [javascript.info — Fetch](https://javascript.info/fetch)
- Nixon, R. (2021). *Learning PHP, MySQL & JavaScript*. O'Reilly. — Bab JavaScript
