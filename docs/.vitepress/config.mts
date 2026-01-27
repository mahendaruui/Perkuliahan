import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

// https://vitepress.dev/reference/site-config
export default withMermaid(
  defineConfig({
  title: "Bahan Ajar",
  description: "Dokumentasi Bahan Ajar Algoritma dan Pemrograman - Mahendar Dwi Payana",
  lang: 'id-ID',

  lastUpdated: true,
  cleanUrls: true,
  metaChunk: true,

  // Base URL untuk GitHub Pages
  // Sesuaikan dengan nama repository Anda
  // Jika repository bernama 'Perkuliahan', gunakan '/Perkuliahan/'
  // Jika ini adalah user.github.io (root), gunakan '/'
  base: '/Perkuliahan/',

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/Perkuliahan/uuifav.png' }],
    ['meta', { name: 'author', content: 'Mahendar Dwi Payana' }],
    ['meta', { property: 'og:title', content: 'Bahan Ajar - Universitas Ubudiyah Indonesia' }],
    ['meta', { property: 'og:description', content: 'Dokumentasi Bahan Ajar Algoritma dan Pemrograman' }],
  ],

  themeConfig: {
    // Logo
    logo: '/uuilogo.png',
    siteTitle: 'Bahan Ajar UUI',

    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Beranda', link: '/' },
      { text: 'Algoritma & Pemrograman', link: '/algoritma-pemrograman/' },
      { text: 'Kompleksitas Algoritma', link: '/kompleksitas-algoritma/' }
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
      ],

      '/kompleksitas-algoritma/': [
        {
          text: 'Pendahuluan',
          items: [
            { text: 'Daftar Materi', link: '/kompleksitas-algoritma/' },
            { text: 'Pengenalan Kompleksitas', link: '/kompleksitas-algoritma/pengenalan' }
          ]
        },
        {
          text: 'Analisis Kompleksitas',
          collapsed: false,
          items: [
            { text: 'Notasi Big O', link: '/kompleksitas-algoritma/big-o' },
            { text: 'Time Complexity', link: '/kompleksitas-algoritma/time-complexity' },
            { text: 'Space Complexity', link: '/kompleksitas-algoritma/space-complexity' }
          ]
        },
        {
          text: 'Analisis Algoritma',
          collapsed: false,
          items: [
            { text: 'Best, Average, Worst Case', link: '/kompleksitas-algoritma/best-average-worst' },
            { text: 'Asymptotic Analysis', link: '/kompleksitas-algoritma/asymptotic-analysis' }
          ]
        },
        {
          text: 'Studi Kasus',
          collapsed: true,
          items: [
            { text: 'Analisis Algoritma Pencarian', link: '/kompleksitas-algoritma/analisis-pencarian' },
            { text: 'Analisis Algoritma Sorting', link: '/kompleksitas-algoritma/analisis-sorting' },
            { text: 'Optimasi Algoritma', link: '/kompleksitas-algoritma/optimasi' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/mahendar/Perkuliahan' }
    ],

    sidebar: {
      '/algoritma-pemrograman/': [
        {
          text: 'Pendahuluan',
          collapsed: true,
          items: [
            { text: 'Daftar Materi', link: '/algoritma-pemrograman/' },
            { text: 'Pengenalan', link: '/algoritma-pemrograman/pengenalan' }
          ]
        },
        {
          text: 'Dasar-Dasar',
          collapsed: true,
          items: [
            { text: 'Variabel dan Tipe Data', link: '/algoritma-pemrograman/variabel-tipe-data' },
            { text: 'Operator', link: '/algoritma-pemrograman/operator' }
          ]
        },
        {
          text: 'Struktur Kontrol',
          collapsed: true,
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
      ],

      '/kompleksitas-algoritma/': [
        {
          text: 'Pendahuluan',
          collapsed: true,
          items: [
            { text: 'Daftar Materi', link: '/kompleksitas-algoritma/' },
            { text: 'Pengenalan Kompleksitas', link: '/kompleksitas-algoritma/pengenalan' }
          ]
        },
        {
          text: 'Analisis Kompleksitas',
          collapsed: true,
          items: [
            { text: 'Notasi Big O', link: '/kompleksitas-algoritma/big-o' },
            { text: 'Time Complexity', link: '/kompleksitas-algoritma/time-complexity' },
            { text: 'Space Complexity', link: '/kompleksitas-algoritma/space-complexity' }
          ]
        },
        {
          text: 'Analisis Algoritma',
          collapsed: true,
          items: [
            { text: 'Best, Average, Worst Case', link: '/kompleksitas-algoritma/best-average-worst' },
            { text: 'Asymptotic Analysis', link: '/kompleksitas-algoritma/asymptotic-analysis' }
          ]
        },
        {
          text: 'Studi Kasus',
          collapsed: true,
          items: [
            { text: 'Analisis Algoritma Pencarian', link: '/kompleksitas-algoritma/analisis-pencarian' },
            { text: 'Analisis Algoritma Sorting', link: '/kompleksitas-algoritma/analisis-sorting' },
            { text: 'Optimasi Algoritma', link: '/kompleksitas-algoritma/optimasi' }
          ]
        }
      ]
    },

    // Appearance
    appearance: true,

    // Last updated
    lastUpdated: {
      text: 'Terakhir diperbarui',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: 'short'
      }
    },

    // Edit link
    editLink: {
      pattern: 'https://github.com/mahendar/Perkuliahan/edit/main/docs/:path',
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
    
    // Footer
    footer: {
      message: 'Dirilis di bawah Lisensi MIT.',
      copyright: 'Hak Cipta © 2024 Mahendar Dwi Payana'
    },

    outline: {
      level: [2, 3],
      label: 'Daftar Isi'
    },
    
    docFooter: {
      prev: 'Halaman Sebelumnya',
      next: 'Halaman Selanjutnya'
    },

    lastUpdated: {
      text: 'Terakhir diperbarui',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'short'
      }
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
