import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

// https://vitepress.dev/reference/site-config
export default withMermaid(
  defineConfig({
    title: "Bahan Ajar UUI",
    description: "Portal Dokumentasi Bahan Ajar Perkuliahan - Mahendar Dwi Payana",
    lang: 'id-ID',

    lastUpdated: true,
    cleanUrls: true,
    metaChunk: true,

    // Base URL untuk GitHub Pages
    base: '/Perkuliahan/',

    head: [
      ['link', { rel: 'icon', type: 'image/png', href: '/Perkuliahan/uuifav.png' }],
      ['meta', { name: 'author', content: 'Mahendar Dwi Payana' }],
      ['meta', { property: 'og:title', content: 'Bahan Ajar Perkuliahan - Universitas Ubudiyah Indonesia' }],
      ['meta', { property: 'og:description', content: 'Portal Dokumentasi Bahan Ajar Perkuliahan yang Diampu oleh Mahendar Dwi Payana, S.ST., M.T.' }],
    ],

    themeConfig: {
      // Logo
      logo: '/uuilogo.png',
      siteTitle: 'Bahan Ajar UUI',

      nav: [
        { text: 'Beranda', link: '/' },
        {
          text: '📚 Daftar Mata Kuliah',
          items: [
            {
              text: 'Pengembangan Perangkat Lunak',
              items: [
                { text: '☕ Pemrograman OOP (Java)', link: '/pemrograman-oop/' },
                { text: '🐘 Pemrograman OOP (PHP)', link: '/pemrograman-oop-php/' },
                { text: '🌐 Pemrograman Web', link: '/pemrograman-web/' },
                { text: '📱 Pemrograman Mobile', link: '/mobile-programming/' }
              ]
            },
            {
              text: 'Algoritma & Struktur Data',
              items: [
                { text: '🔷 Struktur Data (Golang)', link: '/struktur-data/' },
                { text: '⚡ Algoritma & Pemrograman', link: '/algoritma-pemrograman/' },
                { text: '📊 Kompleksitas Algoritma', link: '/kompleksitas-algoritma/' }
              ]
            }
          ]
        },
        {
          text: '📽️ Slide Presentasi',
          items: [
            { text: '📋 Daftar Seluruh Slide', link: '/presentasi/' },
            { text: '⚡ Algoritma & Pemrograman', link: '/presentasi/pertemuan-1-algoritma' },
            { text: '🐘 Pemrograman OOP (PHP)', link: '/presentasi/pertemuan-1-php' },
            { text: '☕ Pemrograman OOP (Java)', link: '/presentasi/pertemuan-1-java' }
          ]
        }
      ],

      sidebar: {
        '/presentasi/': [
          {
            text: 'Ikhtisar',
            collapsed: false,
            items: [
              { text: '📋 Daftar Seluruh Slide', link: '/presentasi/' }
            ]
          },
          {
            text: '⚡ Algoritma & Pemrograman',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Kontrak & Pengantar', link: '/presentasi/pertemuan-1-algoritma' },
              { text: 'Pertemuan 2: Variabel & Tipe Data', link: '/presentasi/pertemuan-2-algoritma' },
              { text: 'Pertemuan 3: Operator & Ekspresi', link: '/presentasi/pertemuan-3-algoritma' },
              { text: 'Pertemuan 4: Struktur Percabangan', link: '/presentasi/pertemuan-4-algoritma' },
              { text: 'Pertemuan 5: Struktur Perulangan', link: '/presentasi/pertemuan-5-algoritma' },
              { text: 'Pertemuan 6: Larik (Array 1D)', link: '/presentasi/pertemuan-6-algoritma' }
            ]
          },
          {
            text: '🐘 Pemrograman OOP (PHP)',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Kontrak & Pengantar', link: '/presentasi/pertemuan-1-php' },
              { text: 'Pertemuan 2: Class & Object', link: '/presentasi/pertemuan-2-php' },
              { text: 'Pertemuan 3: Constructor & Method', link: '/presentasi/pertemuan-3-php' },
              { text: 'Pertemuan 4: Encapsulation & Readonly', link: '/presentasi/pertemuan-4-php' },
              { text: 'Pertemuan 5: Inheritance & Trait', link: '/presentasi/pertemuan-5-php' },
              { text: 'Pertemuan 6: Polymorphism', link: '/presentasi/pertemuan-6-php' },
              { text: 'Pertemuan 7: Abstraction & Interface', link: '/presentasi/pertemuan-7-php' },
              { text: 'Pertemuan 9: Namespace & PSR-4', link: '/presentasi/pertemuan-9-php' },
              { text: 'Pertemuan 10: Exception Handling', link: '/presentasi/pertemuan-10-php' },
              { text: 'Pertemuan 11: Collections & Array', link: '/presentasi/pertemuan-11-php' },
              { text: 'Pertemuan 12: File Handling & Streams', link: '/presentasi/pertemuan-12-php' },
              { text: 'Pertemuan 13: Prinsip SOLID', link: '/presentasi/pertemuan-13-php' },
              { text: 'Pertemuan 14: Model-Service-Repo', link: '/presentasi/pertemuan-14-php' },
              { text: 'Pertemuan 15: Capstone Mini Project', link: '/presentasi/pertemuan-15-php' }
            ]
          },
          {
            text: '☕ Pemrograman OOP (Java)',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Kontrak & Pengantar', link: '/presentasi/pertemuan-1-java' }
            ]
          }
        ],
        '/pemrograman-oop/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/pemrograman-oop/' },
              { text: 'RPS (Rencana Pembelajaran)', link: '/pemrograman-oop/RPS' },
              { text: 'Minggu 1 — Pengantar OOP', link: '/pemrograman-oop/pengantar-oop' }
            ]
          },
          {
            text: 'Dasar Objek & Kelas',
            collapsed: false,
            items: [
              { text: 'Minggu 2 — Class dan Object', link: '/pemrograman-oop/class-dan-object' },
              { text: 'Minggu 3 — Constructor & Method', link: '/pemrograman-oop/constructor-method' }
            ]
          },
          {
            text: 'Pilar-Pilar OOP',
            collapsed: false,
            items: [
              { text: 'Minggu 4 — Encapsulation', link: '/pemrograman-oop/encapsulation' },
              { text: 'Minggu 5 — Inheritance', link: '/pemrograman-oop/inheritance' },
              { text: 'Minggu 6 — Polymorphism', link: '/pemrograman-oop/polymorphism' },
              { text: 'Minggu 7 — Abstraction & Interface', link: '/pemrograman-oop/interface-abstract' }
            ]
          },
          {
            text: 'OOP Lanjutan & Libraries',
            collapsed: false,
            items: [
              { text: 'Minggu 9 — Package Management', link: '/pemrograman-oop/package' },
              { text: 'Minggu 10 — Exception Handling', link: '/pemrograman-oop/exception-handling' },
              { text: 'Minggu 11 — Collection Framework', link: '/pemrograman-oop/collection' },
              { text: 'Minggu 12 — File Handling (I/O)', link: '/pemrograman-oop/file-handling' }
            ]
          },
          {
            text: 'Desain & Proyek',
            collapsed: false,
            items: [
              { text: 'Minggu 13 — Dasar SOLID Principle', link: '/pemrograman-oop/solid-principle' },
              { text: 'Minggu 14 — Implementasi Aplikasi OOP', link: '/pemrograman-oop/aplikasi-oop' },
              { text: 'Minggu 15 — Mini Project OOP', link: '/pemrograman-oop/mini-project' },
              { text: 'Minggu 16 — Evaluasi & Presentasi UAS', link: '/pemrograman-oop/evaluasi-akhir' }
            ]
          }
        ],
        '/pemrograman-oop-php/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/pemrograman-oop-php/' },
              { text: 'RPS (Rencana Pembelajaran)', link: '/pemrograman-oop-php/RPS' },
              { text: 'Minggu 1 — Pengantar OOP', link: '/pemrograman-oop-php/pengantar-oop' }
            ]
          },
          {
            text: 'Dasar Objek & Kelas',
            collapsed: false,
            items: [
              { text: 'Minggu 2 — Class dan Object', link: '/pemrograman-oop-php/class-dan-object' },
              { text: 'Minggu 3 — Constructor & Method', link: '/pemrograman-oop-php/constructor-method' }
            ]
          },
          {
            text: 'Pilar-Pilar OOP',
            collapsed: false,
            items: [
              { text: 'Minggu 4 — Encapsulation', link: '/pemrograman-oop-php/encapsulation' },
              { text: 'Minggu 5 — Inheritance & Trait', link: '/pemrograman-oop-php/inheritance' },
              { text: 'Minggu 6 — Polymorphism', link: '/pemrograman-oop-php/polymorphism' },
              { text: 'Minggu 7 — Abstraction & Interface', link: '/pemrograman-oop-php/interface-abstract' }
            ]
          },
          {
            text: 'OOP Lanjutan & Libraries',
            collapsed: false,
            items: [
              { text: 'Minggu 9 — Namespace & Composer', link: '/pemrograman-oop-php/namespace' },
              { text: 'Minggu 10 — Exception Handling', link: '/pemrograman-oop-php/exception-handling' },
              { text: 'Minggu 11 — Collections & Array', link: '/pemrograman-oop-php/collection' },
              { text: 'Minggu 12 — File Handling (I/O)', link: '/pemrograman-oop-php/file-handling' }
            ]
          },
          {
            text: 'Desain & Proyek',
            collapsed: false,
            items: [
              { text: 'Minggu 13 — Dasar SOLID Principle', link: '/pemrograman-oop-php/solid-principle' },
              { text: 'Minggu 14 — Implementasi Aplikasi OOP', link: '/pemrograman-oop-php/aplikasi-oop' },
              { text: 'Minggu 15 — Mini Project OOP', link: '/pemrograman-oop-php/mini-project' },
              { text: 'Minggu 16 — Evaluasi & Presentasi UAS', link: '/pemrograman-oop-php/evaluasi-akhir' }
            ]
          }
        ],
        '/algoritma-pemrograman/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/algoritma-pemrograman/' },
              { text: 'RPS (Rencana Pembelajaran)', link: '/algoritma-pemrograman/RPS' },
              { text: 'Minggu 1 — Pengenalan Algoritma & Pemrograman', link: '/algoritma-pemrograman/pengenalan' }
            ]
          },
          {
            text: 'Dasar-Dasar Pemrograman',
            collapsed: false,
            items: [
              { text: 'Minggu 2 — Variabel dan Tipe Data', link: '/algoritma-pemrograman/variabel-tipe-data' },
              { text: 'Minggu 3 — Operator & Ekspresi', link: '/algoritma-pemrograman/operator' }
            ]
          },
          {
            text: 'Struktur Kontrol Alur',
            collapsed: false,
            items: [
              { text: 'Minggu 4 — Percabangan (If-Else, Switch)', link: '/algoritma-pemrograman/percabangan' },
              { text: 'Minggu 5 — Perulangan (For, While, Do-While)', link: '/algoritma-pemrograman/perulangan' }
            ]
          },
          {
            text: 'Struktur Data Dasar',
            collapsed: false,
            items: [
              { text: 'Minggu 7 — Array (Larik)', link: '/algoritma-pemrograman/array' },
              { text: 'Minggu 9 — String & Operasi Teks', link: '/algoritma-pemrograman/string' }
            ]
          },
          {
            text: 'Modularisasi & Rekursi',
            collapsed: false,
            items: [
              { text: 'Minggu 10 — Fungsi dan Prosedur', link: '/algoritma-pemrograman/fungsi-prosedur' },
              { text: 'Minggu 11 — Rekursi', link: '/algoritma-pemrograman/rekursi' }
            ]
          },
          {
            text: 'Algoritma Searching & Sorting',
            collapsed: false,
            items: [
              { text: 'Minggu 12 — Algoritma Pencarian (Searching)', link: '/algoritma-pemrograman/algoritma-pencarian' },
              { text: 'Minggu 13-14 — Algoritma Pengurutan (Sorting)', link: '/algoritma-pemrograman/algoritma-pengurutan' },
              { text: 'Minggu 16 — Bank Soal & Evaluasi UAS', link: '/algoritma-pemrograman/SOAL_UAS' }
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
        ],

        '/struktur-data/': [
          {
            text: 'Pendahuluan',
            collapsed: false,
            items: [
              { text: 'Daftar Materi', link: '/struktur-data/' },
              { text: 'RPS (Rencana Pembelajaran Semester)', link: '/struktur-data/RPS' },
              { text: 'Minggu 1 - Pengantar Struktur Data', link: '/struktur-data/pengantar' }
            ]
          },
          {
            text: 'Dasar Memori & Golang',
            collapsed: false,
            items: [
              { text: 'Minggu 2 - Array, Slice, Struct & Pointer', link: '/struktur-data/pointer-struct' }
            ]
          },
          {
            text: 'Struktur Data Linear',
            collapsed: false,
            items: [
              { text: 'Minggu 3 - Stack (LIFO)', link: '/struktur-data/stack' },
              { text: 'Minggu 4 - Queue (FIFO)', link: '/struktur-data/queue' },
              { text: 'Minggu 5 - Singly Linked List', link: '/struktur-data/linked-list' },
              { text: 'Minggu 6 - Opsi LinkedList Lanjutan', link: '/struktur-data/linked-list-lanjutan' },
              { text: 'Minggu 7 & 8 - Studi Kasus & UTS', link: '/struktur-data/studi-kasus-uts' }
            ]
          },
          {
            text: 'Struktur Hierarki & Pencarian',
            collapsed: false,
            items: [
              { text: 'Minggu 9 - Pengenalan Tree', link: '/struktur-data/binary-tree' },
              { text: 'Minggu 10 - Binary Search Tree', link: '/struktur-data/binary-search-tree' },
              { text: 'Minggu 11 - Algoritma Searching', link: '/struktur-data/searching' }
            ]
          },
          {
            text: 'Jaringan Grafik & Evaluasi',
            collapsed: false,
            items: [
              { text: 'Minggu 12 - Pengenalan Graph', link: '/struktur-data/graph' },
              { text: 'Minggu 13 - Rute Terpendek Dijkstra', link: '/struktur-data/dijkstra-graph' },
              { text: 'Minggu 14,15,16 - Proyek Akhir (UAS)', link: '/struktur-data/proyek-akhir' }
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
