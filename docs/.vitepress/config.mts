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
    ignoreDeadLinks: true,

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
            },
            {
              text: 'Sains Data & Visualisasi',
              items: [
                { text: '📊 Visualisasi Data (Python)', link: '/visualisasi-data/' },
                { text: '🗄️ Big Data (IFR229)', link: '/big-data/' },
                { text: '🏛️ Data Warehouse (IFR237)', link: '/datawarehouse/' }
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
            { text: '☕ Pemrograman OOP (Java)', link: '/presentasi/pertemuan-1-java' },
            { text: '📊 Visualisasi Data (Python)', link: '/presentasi/pertemuan-1-visualisasi-data' },
            { text: '🗄️ Big Data (IFR229)', link: '/presentasi/pertemuan-1-big-data' },
            { text: '🏛️ Data Warehouse (IFR237)', link: '/presentasi/pertemuan-1-datawarehouse' }
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
              { text: 'Pertemuan 6: Larik (Array 1D)', link: '/presentasi/pertemuan-6-algoritma' },
              { text: 'Pertemuan 7: Matriks 2D & String', link: '/presentasi/pertemuan-7-algoritma' }
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
          },
          {
            text: '📊 Visualisasi Data (Python)',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Hakikat & Epistemologi', link: '/presentasi/pertemuan-1-visualisasi-data' },
              { text: 'Pertemuan 2: Persepsi Visual & Gestalt', link: '/presentasi/pertemuan-2-visualisasi-data' },
              { text: 'Pertemuan 3: Prinsip Tufte & Munzner', link: '/presentasi/pertemuan-3-visualisasi-data' },
              { text: 'Pertemuan 4: Data Wrangling & EDA Pandas', link: '/presentasi/pertemuan-4-visualisasi-data' },
              { text: 'Pertemuan 5: Matplotlib Fundamental OO', link: '/presentasi/pertemuan-5-visualisasi-data' },
              { text: 'Pertemuan 6: Seaborn Statistik & Distribusi', link: '/presentasi/pertemuan-6-visualisasi-data' },
              { text: 'Pertemuan 7: Visualisasi Relasi & Multivariat', link: '/presentasi/pertemuan-7-visualisasi-data' },
              { text: 'Pertemuan 9: Visualisasi Interaktif Plotly', link: '/presentasi/pertemuan-9-visualisasi-data' },
              { text: 'Pertemuan 10: Pemetaan Geospasial Folium', link: '/presentasi/pertemuan-10-visualisasi-data' },
              { text: 'Pertemuan 11: Visualisasi Deret Waktu & Finansial', link: '/presentasi/pertemuan-11-visualisasi-data' }
            ]
          },
          {
            text: '🗄️ Big Data (IFR229)',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Fondasi & Lanskap Big Data', link: '/presentasi/pertemuan-1-big-data' },
              { text: 'Pertemuan 2: Arsitektur & Penyimpanan', link: '/presentasi/pertemuan-2-big-data' },
              { text: 'Pertemuan 3: Hadoop, MapReduce & Hive', link: '/presentasi/pertemuan-3-big-data' },
              { text: 'Pertemuan 4: Apache Spark & Optimasi ETL', link: '/presentasi/pertemuan-4-big-data' },
              { text: 'Pertemuan 5: NoSQL, Kafka & Streaming', link: '/presentasi/pertemuan-5-big-data' },
              { text: 'Pertemuan 6: Pipeline, Orkestrasi & Kualitas', link: '/presentasi/pertemuan-6-big-data' },
              { text: 'Pertemuan 7: Analitik & ML Terdistribusi', link: '/presentasi/pertemuan-7-big-data' },
              { text: 'Pertemuan 8: Capstone, Tata Kelola & Biaya', link: '/presentasi/pertemuan-8-big-data' }
            ]
          },
          {
            text: '🏛️ Data Warehouse (IFR237)',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Data Warehouse & BI', link: '/presentasi/pertemuan-1-datawarehouse' },
              { text: 'Pertemuan 2: Arsitektur & Pemodelan', link: '/presentasi/pertemuan-2-datawarehouse' },
              { text: 'Pertemuan 3: Fact, Dimension & Star', link: '/presentasi/pertemuan-3-datawarehouse' },
              { text: 'Pertemuan 4: Snowflake, Galaxy & SCD', link: '/presentasi/pertemuan-4-datawarehouse' },
              { text: 'Pertemuan 5: ETL & Kualitas Data', link: '/presentasi/pertemuan-5-datawarehouse' },
              { text: 'Pertemuan 6: OLAP & SQL Analytics', link: '/presentasi/pertemuan-6-datawarehouse' },
              { text: 'Pertemuan 7: Implementasi & Optimasi', link: '/presentasi/pertemuan-7-datawarehouse' },
              { text: 'Pertemuan 8: Capstone, Tata Kelola & UAS', link: '/presentasi/pertemuan-8-datawarehouse' }
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
            text: 'Ruang Praktik',
            collapsed: false,
            items: [
              { text: '🧩 Kanvas: Dasar OOP PHP', link: '/pemrograman-oop-php/canvas' },
              { text: '🧊 Kanvas 3D: Inheritance & Trait', link: '/pemrograman-oop-php/canvas-inheritance' }
            ]
          },
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
            text: 'Evaluasi Tengah Semester',
            collapsed: false,
            items: [
              { text: 'UTS — Tugas Proyek Kelompok (8 Kelompok)', link: '/pemrograman-oop-php/UTS' }
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
              { text: 'Minggu 13-14 — Algoritma Pengurutan (Sorting)', link: '/algoritma-pemrograman/algoritma-pengurutan' }
            ]
          },
          {
            text: 'Integrasi Proyek & Evaluasi',
            collapsed: false,
            items: [
              { text: 'Minggu 15 — Integrasi Proyek Mini & Clean Code', link: '/algoritma-pemrograman/proyek-mini' },
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
        ],
        '/visualisasi-data/': [
          {
            text: 'Ruang Praktik',
            collapsed: false,
            items: [
              { text: '🎨 Kanvas: Dari Data ke Insight', link: '/visualisasi-data/canvas' }
            ]
          },
          {
            text: 'Informasi Mata Kuliah',
            collapsed: false,
            items: [
              { text: '📊 Silabus & RPS OBE', link: '/visualisasi-data/' },
              { text: '📋 Dokumen RPS Resmi', link: '/visualisasi-data/RPS' }
            ]
          },
          {
            text: 'Bagian 1: Fondasi Teori & Persepsi',
            collapsed: false,
            items: [
              { text: 'Minggu 1: Hakikat & Sejarah Visualisasi', link: '/visualisasi-data/01-pengantar-visualisasi-data' },
              { text: 'Minggu 2: Persepsi Visual & Teori Gestalt', link: '/visualisasi-data/02-persepsi-visual-gestalt' },
              { text: 'Minggu 3: Prinsip Desain Tufte & Munzner', link: '/visualisasi-data/03-prinsip-tufte-munzner' }
            ]
          },
          {
            text: 'Bagian 2: Data Wrangling & Visualisasi Statis',
            collapsed: false,
            items: [
              { text: 'Minggu 4: Data Wrangling & EDA Pandas', link: '/visualisasi-data/04-data-wrangling-eda-pandas' },
              { text: 'Minggu 5: Matplotlib Fundamental OO', link: '/visualisasi-data/05-matplotlib-fundamental' },
              { text: 'Minggu 6: Seaborn Statistik & Distribusi', link: '/visualisasi-data/06-seaborn-statistik-distribusi' },
              { text: 'Minggu 7: Visualisasi Relasi & Multivariat', link: '/visualisasi-data/07-visualisasi-relasi-multivariat' }
            ]
          },
          {
            text: 'Evaluasi Tengah Semester',
            collapsed: false,
            items: [
              { text: 'Minggu 8: Evaluasi Tengah Semester (UTS)', link: '/visualisasi-data/08-evaluasi-tengah-semester' }
            ]
          },
          {
            text: 'Bagian 3: Visualisasi Interaktif & Geospasial',
            collapsed: false,
            items: [
              { text: 'Minggu 9: Visualisasi Interaktif Plotly', link: '/visualisasi-data/09-visualisasi-interaktif-plotly' },
              { text: 'Minggu 10: Pemetaan Geospasial Folium', link: '/visualisasi-data/10-visualisasi-geospasial-folium' },
              { text: 'Minggu 11: Visualisasi Data Time Series', link: '/visualisasi-data/11-visualisasi-time-series' }
            ]
          },
          {
            text: 'Bagian 4: AI Viz, Dashboarding & Storytelling',
            collapsed: false,
            items: [
              { text: 'Minggu 12: Visualisasi AI & Machine Learning', link: '/visualisasi-data/12-visualisasi-ai-machine-learning' },
              { text: 'Minggu 13: Dashboard Interaktif Streamlit', link: '/visualisasi-data/13-dashboard-streamlit' },
              { text: 'Minggu 14: Seni Data Storytelling', link: '/visualisasi-data/14-data-storytelling' },
              { text: 'Minggu 15: Capstone Project Terpadu', link: '/visualisasi-data/15-capstone-project' }
            ]
          },
          {
            text: 'Evaluasi Akhir Semester',
            collapsed: false,
            items: [
              { text: 'Minggu 16: Evaluasi Akhir Semester (UAS)', link: '/visualisasi-data/16-evaluasi-akhir-semester' }
            ]
          }
        ],

        '/big-data/': [
          {
            text: 'Ruang Praktik',
            collapsed: false,
            items: [
              { text: '🕸️ Kanvas: Alur Big Data', link: '/big-data/canvas' }
            ]
          },
          {
            text: 'Informasi Mata Kuliah',
            collapsed: false,
            items: [
              { text: '🗄️ Silabus & Peta Materi', link: '/big-data/' },
              { text: '📋 Dokumen RPS OBE', link: '/big-data/RPS' },
              { text: '📘 Buku Teori RPL', link: '/big-data/TEORI-RPL' }
            ]
          },
          {
            text: 'Bagian 1: Fondasi & Arsitektur',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Fondasi & Lanskap Big Data', link: '/big-data/01-pengantar-big-data' },
              { text: 'Pertemuan 2: Arsitektur Terdistribusi & Penyimpanan', link: '/big-data/02-arsitektur-terdistribusi-penyimpanan' }
            ]
          },
          {
            text: 'Bagian 2: Pemrosesan Batch',
            collapsed: false,
            items: [
              { text: 'Pertemuan 3: Hadoop, MapReduce & Hive', link: '/big-data/03-hadoop-mapreduce-hive' },
              { text: 'Pertemuan 4: Apache Spark & Optimasi ETL', link: '/big-data/04-apache-spark' }
            ]
          },
          {
            text: 'Bagian 3: NoSQL & Streaming',
            collapsed: false,
            items: [
              { text: 'Pertemuan 5: NoSQL, Kafka & Event Streaming', link: '/big-data/05-nosql-kafka-streaming' }
            ]
          },
          {
            text: 'Bagian 4: Operasional & Analitik',
            collapsed: false,
            items: [
              { text: 'Pertemuan 6: Pipeline, Orkestrasi & Kualitas Data', link: '/big-data/06-pipeline-orkestrasi-kualitas' },
              { text: 'Pertemuan 7: Analitik & ML Terdistribusi', link: '/big-data/07-analitik-ml-terdistribusi' }
            ]
          },
          {
            text: 'Bagian 5: Capstone & Tata Kelola',
            collapsed: false,
            items: [
              { text: 'Pertemuan 8: Proyek Akhir, Tata Kelola & Biaya', link: '/big-data/08-proyek-akhir-tata-kelola' }
            ]
          }
        ],

        '/datawarehouse/': [
          {
            text: 'Informasi Mata Kuliah',
            collapsed: false,
            items: [
              { text: '🏛️ Silabus & Peta Materi', link: '/datawarehouse/' },
              { text: '📋 Dokumen RPS OBE', link: '/datawarehouse/RPS' },
              { text: '📘 Buku Teori RPL', link: '/datawarehouse/TEORI-RPL' }
            ]
          },
          {
            text: 'Bagian 1: Fondasi & Arsitektur',
            collapsed: false,
            items: [
              { text: 'Pertemuan 1: Data Warehouse & BI', link: '/datawarehouse/01-pengantar-dw-bi' },
              { text: 'Pertemuan 2: Arsitektur & Pemodelan', link: '/datawarehouse/02-arsitektur-pemodelan' }
            ]
          },
          {
            text: 'Bagian 2: Pemodelan Dimensional',
            collapsed: false,
            items: [
              { text: 'Pertemuan 3: Fact, Dimension & Star Schema', link: '/datawarehouse/03-dimensional-modeling' },
              { text: 'Pertemuan 4: Snowflake, Galaxy & SCD', link: '/datawarehouse/04-snowflake-scd' }
            ]
          },
          {
            text: 'Bagian 3: Implementasi & Analitik',
            collapsed: false,
            items: [
              { text: 'Pertemuan 5: ETL & Kualitas Data', link: '/datawarehouse/05-etl-kualitas-data' },
              { text: 'Pertemuan 6: OLAP & SQL Analytics', link: '/datawarehouse/06-olap-sql-analytics' },
              { text: 'Pertemuan 7: Implementasi & Optimasi', link: '/datawarehouse/07-implementasi-optimasi' }
            ]
          },
          {
            text: 'Bagian 4: Capstone & Tata Kelola',
            collapsed: false,
            items: [
              { text: 'Pertemuan 8: Proyek Akhir & UAS', link: '/datawarehouse/08-capstone-tata-kelola' }
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
