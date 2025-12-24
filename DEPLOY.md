# Cara Deploy ke GitHub Pages

## Langkah-langkah Setup

### 1. Push ke GitHub

```bash
# Inisialisasi git repository
git init

# Tambahkan semua file
git add .

# Commit
git commit -m "Initial commit: VitePress documentation"

# Tambahkan remote repository (ganti dengan URL repo Anda)
git remote add origin https://github.com/USERNAME/REPOSITORY.git

# Push ke GitHub
git branch -M main
git push -u origin main
```

### 2. Konfigurasi GitHub Pages

1. Buka repository Anda di GitHub
2. Pergi ke **Settings** → **Pages**
3. Di bagian **Source**, pilih **GitHub Actions**
4. Workflow akan otomatis berjalan setiap kali ada push ke branch `main`

### 3. Update Base URL di VitePress Config

Jika repository Anda bernama `bahan-ajar`, edit file `docs/.vitepress/config.mts`:

```typescript
export default defineConfig({
  // ...
  base: "/bahan-ajar/", // Ganti dengan nama repository Anda
  // ...
});
```

Jika menggunakan custom domain atau GitHub Pages root (username.github.io), gunakan:

```typescript
base: '/',
```

### 4. Akses Website

Setelah workflow selesai, website Anda akan tersedia di:

- `https://USERNAME.github.io/REPOSITORY/` (jika menggunakan base dengan nama repo)
- `https://USERNAME.github.io/` (jika menggunakan root GitHub Pages)

## Troubleshooting

### Assets tidak ter-load (404)

Pastikan `base` di `config.mts` sesuai dengan nama repository Anda.

### Workflow gagal

1. Cek tab **Actions** di GitHub untuk melihat error
2. Pastikan permissions untuk GitHub Actions sudah diaktifkan
3. Pastikan `package.json` sudah ter-commit

### Update tidak muncul

1. Tunggu beberapa menit untuk cache clear
2. Hard refresh browser (Ctrl+Shift+R atau Cmd+Shift+R)
3. Clear cache browser

## Development Lokal

```bash
# Install dependencies
npm install

# Run development server
npm run docs:dev

# Build untuk production
npm run docs:build

# Preview build
npm run docs:preview
```

## Update Konten

Setiap kali Anda push perubahan ke branch `main`, GitHub Actions akan otomatis rebuild dan redeploy website.

```bash
# Setelah edit file markdown
git add .
git commit -m "Update konten"
git push
```
