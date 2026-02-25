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
        { text: 'Kompleksitas Algoritma', link: '/kompleksitas-algoritma/' },
        { text: 'Pemrograman Web', link: '/pemrograman-web/' },
        { text: 'Pemrograman Mobile', link: '/mobile-programming/' }
      ],

      sidebar: {
        '/algoritma-pemrograman/': [
          {
            text: 'Pendahuluan',
            collapsed: true,
            items: [
              { text: 'Daftar Materi', link: '/algoritma-pemrograman/' },
              { text: 'RPS (Rencana Pembelajaran Semester)', link: '/algoritma-pemrograman/RPS' },
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
        ],

        '/pemrograman-web/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/pemrograman-web/' }
            ]
          },
          {
            text: 'Frontend Dasar',
            collapsed: false,
            items: [
              { text: 'Minggu 1 — Pengenalan Web', link: '/pemrograman-web/minggu-1-pengenalan-web' },
              { text: 'Minggu 2-3 — HTML5 & CSS3', link: '/pemrograman-web/minggu-2-3-html-css' },
              { text: 'Minggu 4 — CSS Framework', link: '/pemrograman-web/minggu-4-css-framework' }
            ]
          },
          {
            text: 'JavaScript & API',
            collapsed: true,
            items: [
              { text: 'Minggu 5-6 — JavaScript & DOM', link: '/pemrograman-web/minggu-5-6-javascript' },
              { text: 'Minggu 7 — JSON & Fetch API', link: '/pemrograman-web/minggu-7-fetch-api' }
            ]
          },
          {
            text: 'Backend & Database',
            collapsed: true,
            items: [
              { text: 'Minggu 9-10 — PHP Server-Side', link: '/pemrograman-web/minggu-9-10-php' },
              { text: 'Minggu 11-12 — CRUD MySQL', link: '/pemrograman-web/minggu-11-12-database' }
            ]
          },
          {
            text: 'Framework & Deployment',
            collapsed: true,
            items: [
              { text: 'Minggu 13-14 — MVC Laravel', link: '/pemrograman-web/minggu-13-14-framework-mvc' },
              { text: 'Minggu 15 — Keamanan & Deploy', link: '/pemrograman-web/minggu-15-keamanan-deployment' }
            ]
          }
        ],

        '/mobile-programming/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/mobile-programming/' },
              { text: 'RPS (Rencana Pembelajaran Semester)', link: '/mobile-programming/RPS' },
              { text: 'Intro: Mobile Programming & React Native', link: '/mobile-programming/pengenalan' }
            ]
          },
          {
            text: 'Dasar-Dasar React Native',
            collapsed: false,
            items: [
              { text: 'Env Setup, JSX, Component, State', link: '/mobile-programming/dasar-react' },
              { text: 'React Hooks & Lifecycle', link: '/mobile-programming/hooks-lifecycle' },
              { text: 'Core Component', link: '/mobile-programming/core-component' }
            ]
          },
          {
            text: 'Desain dan Navigasi',
            collapsed: false,
            items: [
              { text: 'UI/UX & Styling', link: '/mobile-programming/ui-ux-styling' },
              { text: 'Navigasi Aplikasi', link: '/mobile-programming/navigasi' }
            ]
          },
          {
            text: 'Manajemen Data dan Integrasi',
            collapsed: false,
            items: [
              { text: 'Networking API', link: '/mobile-programming/networking-api' },
              { text: 'Local Storage', link: '/mobile-programming/local-storage' },
              { text: 'Library Peta & Lokasi', link: '/mobile-programming/peta-lokasi' }
            ]
          }
        ]
      },

      socialLinks: [
        { icon: 'github', link: 'https://github.com/mahendar/Perkuliahan' }
      ],

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
        prev: 'Halaman Sebelumnya',
        next: 'Halaman Selanjutnya'
      },

      // Outline
      outline: {
        level: [2, 3],
        label: 'Daftar Isi'
      },

      // Footer
      footer: {
        message: 'Dirilis di bawah Lisensi MIT.',
        copyright: 'Hak Cipta © 2024 Mahendar Dwi Payana'
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
