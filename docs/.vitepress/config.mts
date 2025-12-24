import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

// https://vitepress.dev/reference/site-config
export default withMermaid(
  defineConfig({
  title: "Bahan Ajar",
  description: "Dokumentasi Bahan Ajar Algoritma dan Pemrograman",
  lang: 'id-ID',

  // Base URL untuk GitHub Pages
  // Sesuaikan dengan nama repository Anda
  // Jika repository bernama 'Perkuliahan', gunakan '/Perkuliahan/'
  // Jika ini adalah user.github.io (root), gunakan '/'
  base: '/Perkuliahan/',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Beranda', link: '/' },
      { text: 'Algoritma & Pemrograman', link: '/algoritma-pemrograman/' }
    ],

    sidebar: {
      '/algoritma-pemrograman/': [
        {
          text: 'Pendahuluan',
          items: [
            { text: 'Daftar Materi', link: '/algoritma-pemrograman/' },
            { text: 'Pengenalan', link: '/algoritma-pemrograman/pengenalan' }
          ]
        },
        {
          text: 'Dasar-Dasar',
          collapsed: false,
          items: [
            { text: 'Variabel dan Tipe Data', link: '/algoritma-pemrograman/variabel-tipe-data' },
            { text: 'Operator', link: '/algoritma-pemrograman/operator' }
          ]
        },
        {
          text: 'Struktur Kontrol',
          collapsed: false,
          items: [
            { text: 'Percabangan', link: '/algoritma-pemrograman/percabangan' },
            { text: 'Perulangan', link: '/algoritma-pemrograman/perulangan' }
          ]
        },
        {
          text: 'Struktur Data Dasar',
          collapsed: true,
          items: [
            { text: 'Array', link: '/algoritma-pemrograman/array' },
            { text: 'String', link: '/algoritma-pemrograman/string' }
          ]
        },
        {
          text: 'Fungsi dan Prosedur',
          collapsed: true,
          items: [
            { text: 'Fungsi dan Prosedur', link: '/algoritma-pemrograman/fungsi-prosedur' },
            { text: 'Rekursi', link: '/algoritma-pemrograman/rekursi' }
          ]
        },
        {
          text: 'Algoritma Dasar',
          collapsed: true,
          items: [
            { text: 'Algoritma Pencarian', link: '/algoritma-pemrograman/algoritma-pencarian' },
            { text: 'Algoritma Pengurutan', link: '/algoritma-pemrograman/algoritma-pengurutan' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com' }
    ],

    footer: {
      message: 'Dokumentasi Bahan Ajar',
      copyright: 'Copyright © 2025'
    },

    // Search
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Cari',
            buttonAriaLabel: 'Cari'
          },
          modal: {
            noResultsText: 'Tidak ada hasil untuk',
            resetButtonTitle: 'Reset pencarian',
            footer: {
              selectText: 'untuk memilih',
              navigateText: 'untuk navigasi'
            }
          }
        }
      }
    },

    // Edit link
    editLink: {
      pattern: 'https://github.com/YOUR_USERNAME/YOUR_REPO/edit/main/docs/:path',
      text: 'Edit halaman ini di GitHub'
    },

    // Pagination
    docFooter: {
      prev: 'Sebelumnya',
      next: 'Selanjutnya'
    },

    // Outline
    outline: {
      label: 'Pada Halaman Ini',
      level: [2, 3]
    },

    // Last updated
    lastUpdated: {
      text: 'Terakhir diperbarui',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: 'short'
      }
    }
  },

  // Markdown configuration
  markdown: {
    lineNumbers: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  }
  })
)
