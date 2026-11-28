<template>
  <div class="dv-root dv-swiss" :class="{ 'is-drawer': drawerOpen }">
    <header class="dv-topbar">
      <button class="dv-menu-btn" type="button" aria-label="Buka daftar langkah" :aria-expanded="drawerOpen" @click="drawerOpen = true">
        <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5.5h14M3 10h14M3 14.5h9" /></svg>
      </button>

      <a class="dv-brand" :href="withBase('/visualisasi-data/canvas')" aria-label="Kanvas Visual — mulai dari langkah pertama" @click.prevent="goTo(0)">
        <span class="dv-logo dv-logo--uui" aria-hidden="true"><img :src="withBase('/uuifav.png')" alt="Logo UUI" /></span>
        <span class="dv-brand__name">Kanvas <span>Visual</span></span>
        <span class="dv-brand__sub">UUI · IFR309</span>
      </a>

      <nav class="dv-nav" aria-label="Navigasi kanvas">
        <button class="dv-nav__item is-active" type="button">Belajar</button>
        <a class="dv-nav__item" :href="withBase('/visualisasi-data/')">Modul</a>
        <a class="dv-nav__item" :href="withBase('/presentasi/pertemuan-2-visualisasi-data')">Slide</a>
      </nav>

      <button class="dv-search" type="button" aria-label="Cari langkah dan konsep" :aria-expanded="searchOpen" @click="openSearch">
        <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
        <span class="dv-search__hint">Cari langkah &amp; konsep…</span>
        <kbd>⌘K</kbd>
      </button>

      <div class="dv-credit" role="note" title="Universitas Ubudiyah Indonesia — Mahendar Dwi Payana, S.ST., M.T." aria-label="Universitas Ubudiyah Indonesia — Mahendar Dwi Payana, S.ST., M.T.">
        <span class="dv-credit__x" aria-hidden="true">UUI</span>
        <span class="dv-credit__text"><small>Universitas Ubudiyah Indonesia</small><b>Mahendar Dwi Payana, S.ST., M.T.</b></span>
      </div>
    </header>

    <div v-if="drawerOpen" class="dv-drawer-backdrop" @click="drawerOpen = false"></div>

    <div class="dv-body">
      <aside class="dv-sidebar" :class="{ 'is-open': drawerOpen }" aria-label="Daftar langkah">
        <div class="dv-tree-root">
          <svg class="dv-folder dv-folder--sand" viewBox="0 0 20 16" aria-hidden="true">
            <path class="dv-folder__back" d="M1.6 3.4c0-.8.6-1.4 1.4-1.4h5l1.6 1.8h7.4c.8 0 1.4.6 1.4 1.4v8.2c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V3.4Z" />
            <path class="dv-folder__front" d="M1.6 6.2h16.8v6.9c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V6.2Z" />
          </svg>
          <span>Kurikulum</span>
          <span class="dv-tree-root__meta">{{ steps.length }} langkah</span>
          <button class="dv-drawer-close" type="button" aria-label="Tutup daftar langkah" @click="drawerOpen = false">
            <svg viewBox="0 0 16 16"><path d="m4 4 8 8M12 4l-8 8" /></svg>
          </button>
        </div>

        <div class="dv-course">
          <section v-for="mod in modules" :key="mod.id" class="dv-mod" :class="{ 'is-open': openModules[mod.id] }">
            <button class="dv-mod__head" type="button" :aria-expanded="openModules[mod.id]" @click="toggleModule(mod.id)">
              <svg class="dv-chev" viewBox="0 0 12 12" aria-hidden="true"><path d="m4 2.5 3.5 3.5L4 9.5" /></svg>
              <svg class="dv-folder" :class="'dv-folder--' + mod.color" viewBox="0 0 20 16" aria-hidden="true">
                <path class="dv-folder__back" d="M1.6 3.4c0-.8.6-1.4 1.4-1.4h5l1.6 1.8h7.4c.8 0 1.4.6 1.4 1.4v8.2c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V3.4Z" />
                <path class="dv-folder__front" d="M1.6 6.2h16.8v6.9c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V6.2Z" />
              </svg>
              <span class="dv-mod__title">{{ mod.title }}</span>
              <span class="dv-mod__count">{{ mod.done }}/{{ mod.total }}</span>
            </button>
            <div class="dv-mod__body">
              <div class="dv-mod__clip">
                <ul class="dv-mod__lessons">
                  <li v-for="idx in mod.items" :key="idx" class="dv-lesson" :class="{ 'is-current': current === idx, 'is-done': current > idx }">
                    <button type="button" @click="goTo(idx)">
                      <span class="dv-lesson__mark">
                        <svg v-if="current > idx" viewBox="0 0 14 14" aria-hidden="true"><path d="m2.5 7.5 3 3 6-6.5" /></svg>
                        <span v-else class="dv-lesson__num">{{ String(idx + 1).padStart(2, '0') }}</span>
                      </span>
                      <span class="dv-lesson__title">{{ steps[idx].short }}</span>
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </section>
        </div>

        <div class="dv-progress">
          <div class="dv-progress__head">
            <span class="dv-eyebrow">KEMAJUAN</span>
            <span class="dv-progress__pct">{{ progressPct }}%</span>
          </div>
          <div class="dv-bar"><span :style="{ width: progressPct + '%' }"></span></div>
          <div class="dv-progress__foot">
            <span>{{ current + 1 }} / {{ steps.length }} langkah</span>
            <span>{{ remainingLabel }}</span>
          </div>
        </div>
      </aside>

      <main class="dv-sheet">
        <div class="dv-lesson-head">
          <div class="dv-crumb">01. Fondasi <span>/</span> Kanvas interaktif</div>
          <div class="dv-lesson-head__row">
            <div class="dv-title-wrap">
              <h1 class="dv-title">Dari Data ke Insight</h1>
              <p class="dv-subtitle">Angka menjadi bentuk — lalu keputusan.</p>
            </div>
            <div class="dv-tags">
              <span class="dv-tag dv-tag--sand">
                <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.6" /><path d="M8 4.8V8l2.2 1.4" /></svg>
                12 mnt
              </span>
              <span class="dv-tag dv-tag--mint">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 12.5V9.8h2.4v2.7ZM6.8 12.5V6.7h2.4v5.8ZM11.1 12.5V3.5h2.4v9Z" /></svg>
                Pemula
              </span>
              <span class="dv-tag dv-tag--violet">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 4.5h10M3 8h10M3 11.5h6" /></svg>
                10 langkah
              </span>
            </div>
          </div>
        </div>

        <div class="dv-stage" ref="stageEl">
          <div class="dv-stage__hud">
            <div v-for="chip in chips" :key="chip.label" class="dv-chip" :data-level="chip.level || undefined">
              <span class="dv-chip__label">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path :d="chip.path" /></svg>
                {{ chip.label }}
              </span>
              <span :key="chip.value" class="dv-chip__value">{{ chip.value }}</span>
            </div>
          </div>

          <div class="dv-stage__tools">
            <button class="dv-tool" type="button" title="Putar ulang animasi" @click="replay">
              <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 7a5.2 5.2 0 1 1 1.1 4.4M3 3.8V7h3.2" /></svg>
              <span>Putar ulang</span>
            </button>
            <button class="dv-tool" type="button" :class="{ 'is-on': !paused }" :title="paused ? 'Lanjutkan animasi' : 'Jeda animasi'" @click="togglePause">
              <svg v-if="paused" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.2 12.2 8 5 12.8Z" /></svg>
              <svg v-else viewBox="0 0 16 16" aria-hidden="true"><path d="M5.3 3v10M10.7 3v10" /></svg>
              <span>{{ paused ? 'Main' : 'Jeda' }}</span>
            </button>
            <button class="dv-tool dv-tool--icon" type="button" :title="isFullscreen ? 'Keluar layar penuh' : 'Layar penuh'" @click="toggleFullscreen">
              <svg v-if="isFullscreen" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 2v4H2M10 2v4h4M6 14v-4H2M10 14v-4h4" /></svg>
              <svg v-else viewBox="0 0 16 16" aria-hidden="true"><path d="M2 6V2h4M14 6V2h-4M2 10v4h4M14 10v4h-4" /></svg>
            </button>
          </div>

          <div class="dv-stage__canvas" ref="canvasWrap">
            <canvas ref="canvasEl" role="img" :aria-label="canvasLabel"></canvas>
          </div>

          <div class="dv-stage__legend" aria-hidden="true">
            <span><i class="dv-lg dv-lg--data"></i> data</span>
            <span><i class="dv-lg dv-lg--insight"></i> insight</span>
            <span><i class="dv-lg dv-lg--noise"></i> noise</span>
          </div>
                  <div class="dv-stage__uui" aria-hidden="true">
            <img :src="withBase('/uuifav.png')" alt="" />
            <span>UUI · FST</span>
          </div>
        </div>

        <div class="dv-timeline">
          <div class="dv-timeline__head">
            <span class="dv-eyebrow">DI PELAJARAN INI</span>
            <span class="dv-timeline__count">Langkah {{ current + 1 }} dari {{ steps.length }}</span>
          </div>
          <div class="dv-timeline__track" :style="{ '--n': steps.length }">
            <div class="dv-timeline__rail"><span :style="{ width: timelinePct + '%' }"></span></div>
            <ol class="dv-timeline__steps">
              <li v-for="(s, i) in steps" :key="s.id" :class="{ 'is-done': i < current, 'is-current': i === current }">
                <button type="button" :aria-current="i === current ? 'step' : undefined" :title="s.title" @click="goTo(i)">
                  <span class="dv-timeline__dot">
                    <svg v-if="i < current" viewBox="0 0 14 14" aria-hidden="true"><path d="m2.5 7.5 3 3 6-6.5" /></svg>
                    <template v-else>{{ i + 1 }}</template>
                  </span>
                  <span class="dv-timeline__label">{{ s.short }}</span>
                </button>
              </li>
            </ol>
          </div>
        </div>

        <p class="dv-footnote">Data ilustrasi: 1.000 transaksi ritel fiktif. Angka dipakai untuk melatih cara membaca bentuk, bukan klaim bisnis.</p>
        <p class="dv-sr-only" aria-live="polite">Langkah {{ current + 1 }} dari {{ steps.length }}: {{ step.title }}. {{ step.short }}.</p>
      </main>

      <aside class="dv-rail" aria-label="Penjelasan langkah">
        <section class="dv-card dv-guide">
          <div class="dv-guide__meta">
            <span class="dv-eyebrow">LANGKAH {{ current + 1 }} / {{ steps.length }}</span>
            <span class="dv-chapter" :class="'dv-chapter--' + step.tone">{{ step.phase }}</span>
          </div>

          <div ref="guideEl" class="dv-guide__content">
            <h2 class="dv-guide__title">{{ step.title }}</h2>
            <div class="dv-guide__body" v-html="step.body"></div>
            <div class="dv-callout dv-callout--insight">
              <div class="dv-callout__icon" aria-hidden="true">
                <svg viewBox="0 0 18 18"><path d="M9 2.1l1.7 5.2L16 9l-5.3 1.7L9 15.9l-1.7-5.2L2 9l5.3-1.7z" /></svg>
              </div>
              <div>
                <div class="dv-callout__title">IDE KUNCI</div>
                <p v-html="step.idea"></p>
              </div>
            </div>
          </div>

          <div class="dv-guide__nav">
            <button class="dv-btn-ghost" type="button" :disabled="current === 0" @click="prev">
              <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13 8H3M7 3.5 2.5 8 7 12.5" /></svg>
              Kembali
            </button>
            <button class="dv-btn-pop dv-btn-next" type="button" @click="next">
              <span class="dv-btn-next__label">{{ current === steps.length - 1 ? 'Selesai: ulang dari awal' : 'Berikutnya: ' + steps[current + 1].short }}</span>
              <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 3.5 13.5 8 9 12.5" /></svg>
            </button>
          </div>
          <div class="dv-guide__hint" aria-hidden="true">
            <kbd>←</kbd><kbd>→</kbd> langkah <span>·</span> <kbd>R</kbd> putar ulang <span>·</span> <kbd>Space</kbd> jeda
          </div>
        </section>

        <section class="dv-card dv-goals">
          <span class="dv-eyebrow">YANG AKAN KAMU PELAJARI</span>
          <ul>
            <li v-for="goal in goals" :key="goal.text" :class="{ 'is-hit': current + 1 >= goal.at }">
              <span class="dv-check" :class="{ 'is-on': current + 1 >= goal.at }" aria-hidden="true">
                <svg viewBox="0 0 14 14"><path d="m2.5 7.5 3 3 6-6.5" /></svg>
              </span>
              {{ goal.text }}
            </li>
          </ul>
        </section>
      </aside>
    </div>

    <Transition name="dv-fade">
      <div v-if="searchOpen" class="dv-palette" @click.self="closeSearch">
        <div class="dv-palette__dialog" role="dialog" aria-modal="true" aria-label="Cari langkah dan konsep">
          <div class="dv-palette__bar">
            <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
            <input ref="searchInput" v-model="searchQuery" class="dv-palette__input" type="search" placeholder="Cari langkah, konsep, atau kata kunci…" @keydown.enter="goToResult(0)" />
            <button class="dv-palette__esc" type="button" @click="closeSearch">esc</button>
          </div>
          <div class="dv-palette__list">
            <div class="dv-palette__group">
              <span>{{ searchQuery ? 'HASIL PENCARIAN' : 'SEMUA LANGKAH' }}</span>
              <span>{{ filteredSteps.length }} hasil</span>
            </div>
            <button v-for="(result, i) in filteredSteps" :key="result.step.id" type="button" class="dv-palette__item" :class="{ 'is-first': i === 0 }" @click="goTo(result.index)">
              <span class="dv-palette__num">{{ String(result.index + 1).padStart(2, '0') }}</span>
              <span class="dv-palette__main">
                <span class="dv-palette__title">{{ result.step.title }}</span>
                <span class="dv-palette__meta">{{ result.step.short }} <span>·</span> {{ result.step.phase }}</span>
              </span>
              <span class="dv-palette__chip" :class="'dv-chapter--' + result.step.tone">{{ result.index === current ? 'SEKARANG' : 'BUKA' }}</span>
            </button>
            <div v-if="!filteredSteps.length" class="dv-palette__empty">
              <strong>Tidak ada hasil.</strong>
              <span>Coba “encoding”, “distribusi”, atau “warna”.</span>
            </div>
          </div>
          <div class="dv-palette__foot">
            <span><kbd>↵</kbd> buka</span>
            <span><kbd>esc</kbd> tutup</span>
            <span class="dv-palette__count">{{ steps.length }} langkah</span>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'

type StepTone = 'sand' | 'blue' | 'green' | 'amber' | 'violet' | 'red'

interface Step {
  id: string
  short: string
  title: string
  phase: string
  tone: StepTone
  body: string
  idea: string
  chartTitle: string
  chartMetric: string
  rows: string
  channel: string
  ink: string
  inkPct: number
  insight: string
  insightN: number
}

interface Goal {
  text: string
  at: number
}

const steps: Step[] = [
  {
    id: 'data',
    short: 'Data mentah',
    title: 'Seribu baris, nol makna',
    phase: 'EKSPLORASI',
    tone: 'sand',
    body: `<p>Bayangkan <b>1.000 transaksi</b> penjualan tersimpan rapi di spreadsheet. Setiap baris benar, setiap kolom lengkap — tetapi tidak ada satu pun perbandingan yang langsung terlihat.</p><p><span class="term">Tabel</span> menyimpan data; <span class="term">visualisasi</span> menerjemahkannya menjadi bentuk yang bisa dipindai mata dalam hitungan detik.</p>`,
    idea: `Mata tidak dirancang untuk membaca angka satu per satu. Ia sangat cepat menangkap posisi, panjang, dan perbedaan warna.`,
    chartTitle: 'Tabel mentah',
    chartMetric: '1.000 baris · 6 kolom',
    rows: '1.000',
    channel: '0',
    ink: '—',
    inkPct: 0,
    insight: '0/3',
    insightN: 0,
  },
  {
    id: 'encoding',
    short: 'Encoding',
    title: 'Pindahkan angka ke bentuk',
    phase: 'ENCODING',
    tone: 'blue',
    body: `<p><b>Encoding visual</b> adalah aturan yang menghubungkan nilai data ke properti visual. Nilai <b>72</b> bisa menjadi panjang batang 72%, posisi sebuah titik, atau tinggi sebuah garis.</p><p>Kualitas visualisasi bergantung pada seberapa jujur dan mudah dibaca terjemahan ini.</p>`,
    idea: `Setiap encoding adalah terjemahan. Pilih terjemahan yang paling jujur — jangan memotong sumbu atau melebih-lebihkan panjang.`,
    chartTitle: 'Encoding',
    chartMetric: 'nilai → panjang',
    rows: '1.000',
    channel: '1',
    ink: '12%',
    inkPct: 12,
    insight: '0/3',
    insightN: 0,
  },
  {
    id: 'marks',
    short: 'Marks & channels',
    title: 'Mark adalah bentuk, channel adalah sifat',
    phase: 'BAHASA VISUAL',
    tone: 'green',
    body: `<p><span class="term">Mark</span> adalah elemen dasar yang digambar: titik, garis, batang, atau area. <span class="term">Channel</span> adalah sifat mark yang membawa nilai: posisi, panjang, warna, ukuran, bentuk, dan sudut.</p><p>Setiap channel punya kekuatan berbeda. Posisi di sumbu paling akurat untuk angka; warna paling cepat menarik perhatian, tetapi paling kasar untuk nilai kuantitatif.</p>`,
    idea: `Pilih channel yang cocok dengan tipe data — posisi untuk kuantitatif, warna untuk kategorikal.`,
    chartTitle: 'Marks & channels',
    chartMetric: '4 channel aktif',
    rows: '1.000',
    channel: '4',
    ink: '18%',
    inkPct: 18,
    insight: '0/3',
    insightN: 0,
  },
  {
    id: 'choose',
    short: 'Pilih bentuk',
    title: 'Bentuk mengikuti pertanyaan',
    phase: 'PILIH BENTUK',
    tone: 'amber',
    body: `<p>Sebelum memilih chart, tulis dulu pertanyaannya. <b>Bandingkan kategori</b> → batang. <b>Lihat distribusi</b> → histogram. <b>Ikuti waktu</b> → garis. <b>Cari hubungan</b> → scatter.</p><p>Chart yang tepat bukan yang paling keren, melainkan yang paling cepat menjawab pertanyaan.</p>`,
    idea: `Mulai dari “pertanyaan apa yang harus dijawab”, bukan dari “chart apa yang ingin dipakai”.`,
    chartTitle: 'Pertanyaan → bentuk',
    chartMetric: '4 pilihan utama',
    rows: '1.000',
    channel: '4',
    ink: '24%',
    inkPct: 24,
    insight: '0/3',
    insightN: 0,
  },
  {
    id: 'distribution',
    short: 'Distribusi',
    title: 'Di mana data menggumpal?',
    phase: 'POLA',
    tone: 'violet',
    body: `<p>Rata-rata <b>68</b> bisa berasal dari data yang sangat berbeda. <b>Histogram</b> menunjukkan bentuk, pusat, sebaran, dan outlier — hal-hal yang disembunyikan oleh satu angka ringkasan.</p><p>Perhatikan ekor kanan: beberapa transaksi bernilai jauh di atas kebanyakan.</p>`,
    idea: `Rata-rata adalah satu angka; distribusi adalah ceritanya. Selalu periksa bentuk sebelum menyimpulkan.`,
    chartTitle: 'Distribusi omzet',
    chartMetric: 'rata-rata Rp 68 jt',
    rows: '1.000',
    channel: '2',
    ink: '46%',
    inkPct: 46,
    insight: '1/3',
    insightN: 1,
  },
  {
    id: 'comparison',
    short: 'Perbandingan',
    title: 'Urutkan, lalu bandingkan',
    phase: 'POLA',
    tone: 'green',
    body: `<p><b>Batang horizontal yang diurutkan</b> memudahkan peringkat. Panjang adalah channel paling akurat untuk nilai, dan urutan menghemat waktu pemindaian.</p><p>Pembaca tidak perlu membandingkan enam posisi secara acak — mereka langsung melihat siapa yang teratas.</p>`,
    idea: `Kalau pertanyaannya “siapa paling besar?”, urutkan. Kalau tidak, mata harus mencari sendiri.`,
    chartTitle: 'Omzet per kanal',
    chartMetric: '6 kategori',
    rows: '1.000',
    channel: '2',
    ink: '58%',
    inkPct: 58,
    insight: '1/3',
    insightN: 1,
  },
  {
    id: 'trend',
    short: 'Tren',
    title: 'Waktu memberi arah',
    phase: 'POLA',
    tone: 'blue',
    body: `<p><b>Line chart</b> menyambungkan observasi yang berurutan. Ia menonjolkan arah dan perubahan, bukan besaran satu per satu.</p><p>Garis menyiratkan urutan. Jangan menyambung kategori acak hanya karena garis terlihat rapi.</p>`,
    idea: `Gunakan garis untuk sesuatu yang memang berjalan dalam waktu — bukan untuk daftar kategori.`,
    chartTitle: 'Omzet bulanan',
    chartMetric: '12 bulan',
    rows: '1.000',
    channel: '2',
    ink: '62%',
    inkPct: 62,
    insight: '2/3',
    insightN: 2,
  },
  {
    id: 'correlation',
    short: 'Korelasi',
    title: 'Dua variabel, satu pola',
    phase: 'POLA',
    tone: 'amber',
    body: `<p><b>Scatter plot</b> memetakan dua variabel kuantitatif. Pola naik menandakan asosiasi positif; sebaran yang lebar berarti hubungan lemah.</p><p>Hati-hati: korelasi bukan kausalitas. Scatter menunjukkan pola, bukan sebab-akibat.</p>`,
    idea: `Dua hal bisa bergerak bersama tanpa saling menyebabkan. Cari mekanisme sebelum mengambil keputusan.`,
    chartTitle: 'Harga vs penjualan',
    chartMetric: 'r = 0,82',
    rows: '1.000',
    channel: '3',
    ink: '70%',
    inkPct: 70,
    insight: '2/3',
    insightN: 2,
  },
  {
    id: 'ink',
    short: 'Data-ink',
    title: 'Buang yang tidak bicara',
    phase: 'DESAIN',
    tone: 'violet',
    body: `<p>Setiap garis, bayangan, dan label harus membawa data atau membantu membacanya. Sisanya adalah <span class="term">chartjunk</span> yang menambah beban kognitif.</p><p>Prinsip Tufte: maksimalkan <b>data-ink ratio</b> — tinta yang benar-benar menyampaikan angka.</p>`,
    idea: `Data-ink ratio yang baik bukan soal minimalis, tetapi soal tidak ada tinta yang menganggur.`,
    chartTitle: 'Data-ink',
    chartMetric: '42% → 84%',
    rows: '1.000',
    channel: '3',
    ink: '84%',
    inkPct: 84,
    insight: '2/3',
    insightN: 2,
  },
  {
    id: 'insight',
    short: 'Insight',
    title: 'Akhiri dengan satu kalimat',
    phase: 'PESAN',
    tone: 'green',
    body: `<p>Visualisasi yang baik menuntun mata ke satu temuan. Tambahkan <b>anotasi</b>, judul yang menyatakan pesan, dan konteks yang cukup.</p><p>Jangan membuat pembaca menyimpulkan sendiri. Tulis insight-nya: <b>“Q4 naik 38% — dorong stok lebih awal.”</b></p>`,
    idea: `Satu grafik, satu pesan. Jika semuanya ditonjolkan, tidak ada yang menonjol.`,
    chartTitle: 'Insight Q4',
    chartMetric: '+38% vs Q3',
    rows: '1.000',
    channel: '3',
    ink: '88%',
    inkPct: 88,
    insight: '3/3',
    insightN: 3,
  },
]

const goals: Goal[] = [
  { text: 'Membedakan data, mark, dan channel', at: 3 },
  { text: 'Memilih bentuk sesuai pertanyaan', at: 4 },
  { text: 'Membaca distribusi, tren, dan korelasi', at: 8 },
  { text: 'Menghapus chartjunk & menghitung data-ink', at: 9 },
  { text: 'Menutup dengan anotasi dan insight', at: 10 },
]

const moduleDefs = [
  { id: 'm1', title: '01. Dari data ke bentuk', color: 'sand', items: [0, 1, 2] },
  { id: 'm2', title: '02. Membaca pola', color: 'green', items: [3, 4, 5, 6, 7] },
  { id: 'm3', title: '03. Desain & pesan', color: 'violet', items: [8, 9] },
]

function readInitialStep() {
  if (typeof window === 'undefined') return 0
  const params = new URLSearchParams(window.location.search)
  const queryStep = Number(params.get('step'))
  if (Number.isFinite(queryStep) && queryStep >= 1 && queryStep <= steps.length) return queryStep - 1
  const hash = window.location.hash.match(/^#langkah-(\d+)$/)
  if (hash) {
    const hashStep = Number(hash[1])
    if (Number.isFinite(hashStep) && hashStep >= 1 && hashStep <= steps.length) return hashStep - 1
  }
  return 0
}

const current = ref(0)
const paused = ref(false)
const drawerOpen = ref(false)
const searchOpen = ref(false)
const searchQuery = ref('')
const searchInput = ref<HTMLInputElement | null>(null)
const stageEl = ref<HTMLElement | null>(null)
const guideEl = ref<HTMLElement | null>(null)
const canvasWrap = ref<HTMLElement | null>(null)
const canvasEl = ref<HTMLCanvasElement | null>(null)
const reducedMotion = ref(false)
const isFullscreen = ref(false)
const openModules = ref<Record<string, boolean>>(
  Object.fromEntries(moduleDefs.map((mod) => [mod.id, true])),
)

const step = computed(() => steps[current.value])
const progressPct = computed(() => Math.round(((current.value + 1) / steps.length) * 100))
const timelinePct = computed(() => (current.value / (steps.length - 1)) * 100)
const remainingLabel = computed(() => (current.value === steps.length - 1 ? 'selesai' : `${steps.length - current.value - 1} lagi`))
const canvasLabel = computed(() => `Visualisasi langkah ${current.value + 1}: ${step.value.title}. ${step.value.chartTitle}, ${step.value.chartMetric}.`)

const modules = computed(() =>
  moduleDefs.map((mod) => ({
    ...mod,
    done: mod.items.filter((idx) => idx < current.value).length,
    total: mod.items.length,
  })),
)

const chips = computed(() => {
  const s = step.value
  return [
    {
      label: 'BARIS DATA',
      value: s.rows,
      level: '',
      path: 'M2.5 4.5h11M2.5 8h11M2.5 11.5h7',
    },
    {
      label: 'CHANNEL',
      value: s.channel,
      level: 'good',
      path: 'M2 11c1.8-4.5 3.7-4.5 5.5 0s3.7 4.5 5.5 0',
    },
    {
      label: 'DATA-INK',
      value: s.ink,
      level: s.inkPct === 0 ? '' : s.inkPct < 50 ? 'warn' : 'good',
      path: 'M8 2.5v11M4 5.5h8M4 10.5h8',
    },
    {
      label: 'INSIGHT',
      value: s.insight,
      level: s.insightN === 3 ? 'good' : s.insightN > 0 ? 'warn' : '',
      path: 'M8 1.8l1.5 4.7L14.2 8l-4.7 1.5L8 14.2 6.5 9.5 1.8 8l4.7-1.5z',
    },
  ]
})

const filteredSteps = computed(() => {
  const query = searchQuery.value.trim().toLowerCase()
  const results = steps
    .map((s, index) => ({ step: s, index }))
    .filter(({ step: s }) => {
      if (!query) return true
      const plainBody = s.body.replace(/<[^>]*>/g, ' ')
      return `${s.title} ${s.short} ${s.phase} ${plainBody}`.toLowerCase().includes(query)
    })

  if (!query) return results

  const score = ({ step: s }: { step: Step }) => {
    const title = s.title.toLowerCase()
    const short = s.short.toLowerCase()
    const phase = s.phase.toLowerCase()
    let value = 0
    if (short === query) value += 8
    else if (short.includes(query)) value += 5
    if (title.includes(query)) value += 4
    if (phase.includes(query)) value += 2
    return value
  }

  return results.sort((a, b) => score(b) - score(a) || a.index - b.index)
})

function toggleModule(id: string) {
  openModules.value[id] = !openModules.value[id]
}

function goTo(index: number) {
  const next = Math.max(0, Math.min(steps.length - 1, index))
  current.value = next
  drawerOpen.value = false
  searchOpen.value = false
  nextTick(() => {
    guideEl.value?.scrollTo({ top: 0, behavior: 'smooth' })
  })
}

function prev() {
  if (current.value > 0) goTo(current.value - 1)
}

function next() {
  goTo(current.value === steps.length - 1 ? 0 : current.value + 1)
}

function openSearch() {
  searchOpen.value = true
}

function closeSearch() {
  searchOpen.value = false
  searchQuery.value = ''
}

function goToResult(index: number) {
  const result = filteredSteps.value[index]
  if (result) goTo(result.index)
}

/* ------------------------------------------------------------------ */
/* Canvas scene                                                        */
/* ------------------------------------------------------------------ */

const DW = 1000
const DH = 560
const C = {
  ink: '#111111',
  ink2: '#242320',
  muted: '#6f6961',
  muted2: '#8b847a',
  line: '#ddd3c5',
  lineSoft: '#e6ddd0',
  lineStrong: '#c6bbac',
  paper: '#f4f3ee',
  paper2: '#f7efe4',
  sheet: '#f9f2e8',
  card: '#f8f0e6',
  cream: '#ffffff',
  white: '#fffcf7',
  green: '#cfe3b2',
  green2: '#b2d491',
  green3: '#7fc278',
  greenTile: '#e8efd9',
  greenDark: '#2f8a43',
  violet: '#e7ddf5',
  violet2: '#b79ce6',
  violetDark: '#5a43a6',
  amber: '#efb041',
  amberSoft: '#fbe5bd',
  orange: '#fcdcbd',
  rust: '#d0683a',
  rustSoft: '#f8d5cf',
  red: '#c0392b',
  blue: '#2f86ce',
  blueSoft: '#d6e5f6',
  mint: '#dff0de',
}
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
const REV = [42, 48, 45, 61, 58, 72, 68, 79, 83, 96, 104, 118]
const CATS = [
  { label: 'Organik', value: 38 },
  { label: 'Berbayar', value: 27 },
  { label: 'Referral', value: 19 },
  { label: 'Email', value: 12 },
  { label: 'Sosial', value: 9 },
  { label: 'Langsung', value: 5 },
]
const HIST = [3, 7, 14, 22, 27, 19, 11, 6, 3]
const SCATTER_POINTS = (() => {
  const points: Array<{ x: number; y: number; size: number; color: string }> = []
  for (let i = 0; i < 30; i++) {
    const x = 0.08 + ((i * 37) % 88) / 100
    const jitter = (((i * 53) % 21) - 10) / 100
    const y = Math.max(0.06, Math.min(0.94, 0.12 + x * 0.68 + jitter))
    const colors = [C.amber, C.green2, C.violet2, C.orange]
    points.push({ x, y, size: 3.4 + (i % 4) * 1.45, color: colors[i % colors.length] })
  }
  return points
})()

const clamp = (v: number, min = 0, max = 1) => Math.max(min, Math.min(max, v))
const easeOut = (v: number) => 1 - Math.pow(1 - clamp(v), 3)
const lerp = (a: number, b: number, t: number) => a + (b - a) * t

function rr(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  const radius = Math.min(r, w / 2, h / 2)
  c.beginPath()
  c.moveTo(x + radius, y)
  c.arcTo(x + w, y, x + w, y + h, radius)
  c.arcTo(x + w, y + h, x, y + h, radius)
  c.arcTo(x, y + h, x, y, radius)
  c.arcTo(x, y, x + w, y, radius)
  c.closePath()
}

function fillRR(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number, fill: string, stroke?: string, lw = 1.5) {
  rr(c, x, y, w, h, r)
  c.fillStyle = fill
  c.fill()
  if (stroke) {
    c.lineWidth = lw
    c.strokeStyle = stroke
    c.stroke()
  }
}

function font(c: CanvasRenderingContext2D, size: number, weight: number | string = 500) {
  c.font = `${weight} ${size}px "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`
}

function txt(
  c: CanvasRenderingContext2D,
  value: string,
  x: number,
  y: number,
  size = 11,
  weight: number | string = 500,
  color = C.ink,
  align: CanvasTextAlign = 'left',
) {
  font(c, size, weight)
  c.fillStyle = color
  c.textAlign = align
  c.textBaseline = 'alphabetic'
  c.fillText(value, x, y)
}

function popBox(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number, fill: string, lw = 1.6, shadow = 3) {
  if (shadow) {
    fillRR(c, x + shadow, y + shadow + 1, w, h, r, C.ink)
  }
  fillRR(c, x, y, w, h, r, fill, C.ink, lw)
}

function pill(
  c: CanvasRenderingContext2D,
  value: string,
  x: number,
  y: number,
  opts: { size?: number; weight?: number; h?: number; pad?: number; fill?: string; dot?: string; shadow?: boolean } = {},
) {
  const size = opts.size ?? 11.5
  const weight = opts.weight ?? 700
  const h = opts.h ?? 28
  const pad = opts.pad ?? 11
  const dot = opts.dot
  font(c, size, weight)
  const textW = c.measureText(value).width
  const w = textW + pad * 2 + (dot ? 13 : 0)
  if (opts.shadow !== false) fillRR(c, x + 2, y + 3, w, h, h / 2, C.ink)
  fillRR(c, x, y, w, h, h / 2, opts.fill ?? C.cream, C.ink, 1.5)
  let tx = x + pad
  if (dot) {
    c.beginPath()
    c.arc(tx + 4, y + h / 2, 4.2, 0, Math.PI * 2)
    c.fillStyle = dot
    c.fill()
    c.strokeStyle = C.ink
    c.lineWidth = 1.1
    c.stroke()
    tx += 13
  }
  c.fillStyle = C.ink
  c.textAlign = 'left'
  c.textBaseline = 'middle'
  c.fillText(value, tx, y + h / 2 + 0.5)
  return w
}

function arrowHead(c: CanvasRenderingContext2D, x: number, y: number, angle: number, size = 6) {
  c.beginPath()
  c.moveTo(x, y)
  c.lineTo(x - Math.cos(angle - 0.5) * size, y - Math.sin(angle - 0.5) * size)
  c.lineTo(x - Math.cos(angle + 0.5) * size, y - Math.sin(angle + 0.5) * size)
  c.closePath()
  c.fillStyle = C.ink
  c.fill()
}

function drawPerspectiveFloor(
  c: CanvasRenderingContext2D,
  w: number,
  h: number,
  horizonRatio: number,
  lines: number,
  alpha: number,
) {
  const horizon = h * horizonRatio
  const nearY = h * 1.06
  const cols = Math.max(10, Math.round(lines))
  const rows = Math.max(7, Math.round(lines * 0.6))
  const point = (u: number, t: number) => {
    const y = lerp(horizon, nearY, t)
    const half = lerp(w * 0.1, w * 0.86, t)
    return [w / 2 + (u - 0.5) * 2 * half, y] as const
  }
  const depth = (r: number) => Math.pow(r / rows, 2.15)

  c.save()
  c.beginPath()
  c.rect(0, horizon - 2, w, h - horizon + 4)
  c.clip()
  c.lineWidth = 1

  for (let r = 0; r < rows; r++) {
    const t0 = depth(r)
    const t1 = depth(r + 1)
    for (let col = 0; col < cols; col++) {
      const u0 = col / cols
      const u1 = (col + 1) / cols
      const p0 = point(u0, t0)
      const p1 = point(u1, t0)
      const p2 = point(u1, t1)
      const p3 = point(u0, t1)
      c.beginPath()
      c.moveTo(p0[0], p0[1])
      c.lineTo(p1[0], p1[1])
      c.lineTo(p2[0], p2[1])
      c.lineTo(p3[0], p3[1])
      c.closePath()
      if ((r + col) % 2 === 0) {
        c.fillStyle = `rgba(80, 60, 35, ${alpha * 0.26})`
        c.fill()
      }
      c.strokeStyle = `rgba(80, 60, 35, ${alpha})`
      c.stroke()
    }
  }
  c.restore()

  // Let the far edge dissolve into the paper instead of ending in a hard line.
  const fade = c.createLinearGradient(0, horizon - 14, 0, horizon + (h - horizon) * 0.48)
  fade.addColorStop(0, 'rgba(252, 251, 249, 0.98)')
  fade.addColorStop(0.35, 'rgba(252, 251, 249, 0.66)')
  fade.addColorStop(1, 'rgba(252, 251, 249, 0)')
  c.fillStyle = fade
  c.fillRect(0, 0, w, h)
}

function drawBackdrop(c: CanvasRenderingContext2D, t: number) {
  const glow = c.createRadialGradient(625, 270, 30, 625, 270, 520)
  glow.addColorStop(0, 'rgba(255, 253, 248, 0.72)')
  glow.addColorStop(0.55, 'rgba(255, 253, 248, 0.24)')
  glow.addColorStop(1, 'rgba(255, 253, 248, 0)')
  c.fillStyle = glow
  c.fillRect(0, 0, DW, DH)

  drawPerspectiveFloor(c, DW, DH, 0.3, 20, 0.085)

  // Sparse accent marks.
  const dots = [
    [82, 130, C.amber],
    [932, 318, C.violet2],
    [900, 86, C.green2],
    [110, 330, C.rust],
    [675, 515, C.green2],
  ] as const
  dots.forEach(([x, y, color], i) => {
    const pulse = 0.7 + Math.sin(t * 1.2 + i) * 0.2
    c.globalAlpha = pulse
    c.beginPath()
    c.arc(x, y, 3.2, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.globalAlpha = 1
  })
}

function diamond(c: CanvasRenderingContext2D, cx: number, cy: number, hw: number, hh: number) {
  c.beginPath()
  c.moveTo(cx, cy - hh)
  c.lineTo(cx + hw, cy)
  c.lineTo(cx, cy + hh)
  c.lineTo(cx - hw, cy)
  c.closePath()
}

function slabPoint(cx: number, cy: number, hw: number, hh: number, u: number, v: number) {
  return [cx + (u + v) * hw, cy + (u - v) * hh]
}

function drawPlatform(c: CanvasRenderingContext2D, t: number) {
  const cx = 204
  const cy = 437 + Math.sin(t * 0.8) * 1.4
  const hw = 136
  const hh = 64
  const thickness = 19

  // floor shadow
  c.save()
  c.globalAlpha = 0.12
  c.fillStyle = C.ink
  c.beginPath()
  c.ellipse(cx, cy + hh + 28, hw * 0.92, 24, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()

  // side faces
  c.beginPath()
  c.moveTo(cx - hw, cy)
  c.lineTo(cx, cy + hh)
  c.lineTo(cx, cy + hh + thickness)
  c.lineTo(cx - hw, cy + thickness)
  c.closePath()
  c.fillStyle = '#dbcfc0'
  c.fill()
  c.lineWidth = 1.8
  c.strokeStyle = C.ink
  c.stroke()

  c.beginPath()
  c.moveTo(cx + hw, cy)
  c.lineTo(cx, cy + hh)
  c.lineTo(cx, cy + hh + thickness)
  c.lineTo(cx + hw, cy + thickness)
  c.closePath()
  c.fillStyle = '#e8ddd0'
  c.fill()
  c.stroke()

  // top
  diamond(c, cx, cy, hw, hh)
  c.fillStyle = C.cream
  c.fill()
  c.lineWidth = 2.2
  c.strokeStyle = C.ink
  c.stroke()

  // inset top
  diamond(c, cx, cy - 3, hw - 12, hh - 6)
  c.fillStyle = C.white
  c.fill()
  c.lineWidth = 1
  c.strokeStyle = C.lineStrong
  c.stroke()

  // data cells on an isometric grid
  const colors = [C.green2, C.amber, C.violet2, C.rust, C.green2, C.blue]
  const uMin = -0.37
  const vMin = -0.29
  const cellU = 0.172
  const cellV = 0.18
  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 4; col++) {
      const u0 = uMin + col * cellU
      const v0 = vMin + row * cellV
      const u1 = u0 + cellU * 0.78
      const v1 = v0 + cellV * 0.78
      const pts = [
        slabPoint(cx, cy - 3, hw - 12, hh - 6, u0, v0),
        slabPoint(cx, cy - 3, hw - 12, hh - 6, u1, v0),
        slabPoint(cx, cy - 3, hw - 12, hh - 6, u1, v1),
        slabPoint(cx, cy - 3, hw - 12, hh - 6, u0, v1),
      ]
      c.beginPath()
      c.moveTo(pts[0][0], pts[0][1])
      for (let i = 1; i < 4; i++) c.lineTo(pts[i][0], pts[i][1])
      c.closePath()
      c.fillStyle = colors[(row * 4 + col) % colors.length]
      c.globalAlpha = 0.82
      c.fill()
      c.globalAlpha = 1
      c.lineWidth = 0.8
      c.strokeStyle = 'rgba(29, 27, 24, 0.55)'
      c.stroke()
    }
  }

  // paper stack behind the tablet
  c.save()
  c.translate(102, 351)
  c.rotate(-0.09)
  fillRR(c, 8, -7, 76, 47, 4, '#e6ddd0', 'rgba(29,27,24,.45)', 1)
  fillRR(c, 2, -1, 76, 47, 4, C.cream, C.ink, 1.4)
  c.strokeStyle = 'rgba(29,27,24,.25)'
  c.lineWidth = 1
  for (let i = 0; i < 4; i++) {
    c.beginPath()
    c.moveTo(10, 10 + i * 8)
    c.lineTo(i === 3 ? 46 : 66, 10 + i * 8)
    c.stroke()
  }
  c.restore()

  // CSV tag
  pill(c, 'CSV', cx - 26, cy + hh + 27, { size: 9, h: 22, pad: 8, fill: C.amberSoft })
}

function drawFlow(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const p0 = [330, 419]
  const p1 = [365, 411]
  const p2 = [344, 353]
  const p3 = [374, 342]

  c.save()
  c.beginPath()
  c.moveTo(p0[0], p0[1])
  c.bezierCurveTo(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
  c.strokeStyle = stepIndex === 0 ? 'rgba(111,105,97,.28)' : 'rgba(111,105,97,.72)'
  c.lineWidth = 1.7
  c.setLineDash([5, 5])
  c.stroke()
  c.setLineDash([])
  const angle = Math.atan2(p3[1] - p2[1], p3[0] - p2[0])
  arrowHead(c, p3[0], p3[1], angle, 5.5)
  c.restore()

  if (stepIndex === 0) return

  const count = stepIndex >= 8 ? 2 : 4
  for (let i = 0; i < count; i++) {
    const raw = (t * 0.32 + i / count) % 1
    const progress = raw < 0.5 ? 2 * raw * raw : 1 - Math.pow(-2 * raw + 2, 2) / 2
    const q = bezierPoint(p0, p1, p2, p3, progress)
    const alpha = Math.sin(progress * Math.PI) * 0.95
    c.save()
    c.globalAlpha = Math.max(0, alpha)
    c.beginPath()
    c.arc(q[0], q[1], 6.2, 0, Math.PI * 2)
    c.fillStyle = i % 2 === 0 ? C.green2 : C.amber
    c.fill()
    c.lineWidth = 1.5
    c.strokeStyle = C.ink
    c.stroke()
    c.restore()
  }
}

function bezierPoint(p0: number[], p1: number[], p2: number[], p3: number[], t: number) {
  const mt = 1 - t
  const a = mt * mt * mt
  const b = 3 * mt * mt * t
  const c = 3 * mt * t * t
  const d = t * t * t
  return [a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]]
}

function drawInsightPill(c: CanvasRenderingContext2D, t: number, stepIndex: number, x = 623, y = 56, w = 260, h = 38) {
  fillRR(c, x + 2, y + 3, w, h, h / 2, C.ink)
  fillRR(c, x, y, w, h, h / 2, C.cream, C.ink, 1.6)

  // spark icon tile
  fillRR(c, x + 7, y + 7, 23, 23, 7, stepIndex === steps.length - 1 ? C.green2 : C.violet, C.ink, 1.2, 0)
  c.save()
  c.translate(x + 18.5, y + 18.5)
  c.fillStyle = C.ink
  c.beginPath()
  c.moveTo(0, -7)
  c.lineTo(2.2, -2.2)
  c.lineTo(7, 0)
  c.lineTo(2.2, 2.2)
  c.lineTo(0, 7)
  c.lineTo(-2.2, 2.2)
  c.lineTo(-7, 0)
  c.lineTo(-2.2, -2.2)
  c.closePath()
  c.fill()
  c.restore()

  txt(c, 'INSIGHT', x + 40, y + 23, 9.5, 800, C.muted)
  const value = steps[stepIndex].insightN
  const segX = x + 106
  for (let i = 0; i < 3; i++) {
    fillRR(c, segX + i * 32, y + 15, 25, 8, 4, i < value ? (i === 2 ? C.green3 : C.green2) : C.lineSoft, 'rgba(29,27,24,.35)', 0.8, 0)
  }
  txt(c, `${value}/3`, x + w - 16, y + 24, 11.5, 800, value === 3 ? C.greenDark : C.ink, 'right')

  if (stepIndex === steps.length - 1) {
    const pulse = 0.16 + Math.sin(t * 2.2) * 0.06
    rr(c, x - 3, y - 3, w + 6, h + 6, (h + 6) / 2)
    c.strokeStyle = `rgba(127,194,120,${pulse + 0.35})`
    c.lineWidth = 2
    c.stroke()
  }
}

function drawChartCard(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const x = 370
  const baseY = 116
  const y = baseY + Math.sin(t * 0.85 + 0.8) * 2
  const w = 560
  const h = 340
  const r = 17

  // floor shadow
  c.save()
  c.globalAlpha = 0.1
  c.fillStyle = C.ink
  c.beginPath()
  c.ellipse(x + w / 2, y + h + 22, w * 0.36, 20, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()

  fillRR(c, x + 6, y + 8, w, h, r, C.ink)
  fillRR(c, x, y, w, h, r, C.cream)

  // header
  c.save()
  rr(c, x, y, w, h, r)
  c.clip()
  c.fillStyle = C.paper
  c.fillRect(x, y, w, 40)
  c.restore()
  c.beginPath()
  c.moveTo(x + 1, y + 40)
  c.lineTo(x + w - 1, y + 40)
  c.strokeStyle = C.line
  c.lineWidth = 1.2
  c.stroke()

  // window dots
  const dotColors = [C.green3, C.amber, C.rust]
  dotColors.forEach((color, i) => {
    c.beginPath()
    c.arc(x + 18 + i * 12, y + 20, 3.5, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.strokeStyle = 'rgba(29,27,24,.7)'
    c.lineWidth = 0.8
    c.stroke()
  })
  txt(c, 'grafik.view', x + 58, y + 24, 11, 800)
  txt(c, 'penjualan.csv · 1.000 baris', x + w - 18, y + 24, 9.5, 600, C.muted, 'right')

  // card border on top of the header fill
  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 2.1
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.chartTitle.toUpperCase(), x + 26, y + 68, 9.5, 800, C.muted)
  txt(c, s.chartMetric, x + 26, y + 91, s.chartMetric.length > 22 ? 13.5 : 16, 800, C.ink)

  const ax = x + 26
  const ay = y + 108
  const aw = w - 52
  const ah = h - 132

  c.save()
  rr(c, x + 2, y + 44, w - 4, h - 46, 10)
  c.clip()
  drawChartBody(c, stepIndex, t, ax, ay, aw, ah)
  c.restore()
}

function drawChartBody(c: CanvasRenderingContext2D, stepIndex: number, t: number, x: number, y: number, w: number, h: number) {
  switch (stepIndex) {
    case 0:
      drawRawTable(c, t, x, y, w, h)
      break
    case 1:
      drawEncodingChart(c, t, x, y, w, h)
      break
    case 2:
      drawMarksChannels(c, t, x, y, w, h)
      break
    case 3:
      drawChooseChart(c, t, x, y, w, h)
      break
    case 4:
      drawHistogram(c, t, x, y, w, h)
      break
    case 5:
      drawBarChart(c, t, x, y, w, h)
      break
    case 6:
      drawLineChart(c, t, x, y, w, h, false)
      break
    case 7:
      drawScatterChart(c, t, x, y, w, h)
      break
    case 8:
      drawDataInk(c, t, x, y, w, h)
      break
    case 9:
      drawLineChart(c, t, x, y, w, h, true)
      break
  }
}

function drawRawTable(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const rows = [
    ['TRX-0421', 'Organik', '12 Feb', 'Rp 72 jt'],
    ['TRX-0422', 'Berbayar', '12 Feb', 'Rp 41 jt'],
    ['TRX-0423', 'Email', '13 Feb', 'Rp 18 jt'],
    ['TRX-0424', 'Organik', '13 Feb', 'Rp 88 jt'],
    ['TRX-0425', 'Referral', '14 Feb', 'Rp 33 jt'],
    ['TRX-0426', 'Sosial', '14 Feb', 'Rp 12 jt'],
    ['TRX-0427', 'Berbayar', '15 Feb', 'Rp 56 jt'],
  ]
  const headH = 22
  const rowH = Math.min(23, (h - 34) / rows.length)
  const col = [0, 0.29, 0.51, 0.77]
  const rowAlpha = (i: number) => easeOut(clamp((t - i * 0.045) / 0.5))

  c.save()
  c.globalAlpha = easeOut(clamp(t / 0.5))
  c.fillStyle = C.paper
  c.fillRect(x, y, w, headH)
  txt(c, 'ID', x + 8, y + 15, 9.3, 800, C.muted)
  txt(c, 'KANAL', x + w * col[1], y + 15, 9.3, 800, C.muted)
  txt(c, 'TANGGAL', x + w * col[2], y + 15, 9.3, 800, C.muted)
  txt(c, 'OMZET', x + w * col[3], y + 15, 9.3, 800, C.muted)
  c.restore()

  rows.forEach((row, i) => {
    const ry = y + headH + i * rowH
    const alpha = rowAlpha(i)
    c.save()
    c.globalAlpha = alpha
    if (i === 3) {
      c.fillStyle = C.greenTile
      c.fillRect(x, ry, w, rowH)
      c.strokeStyle = C.green3
      c.lineWidth = 1.2
      c.strokeRect(x + 0.5, ry + 0.5, w - 1, rowH - 1)
    } else if (i % 2 === 1) {
      c.fillStyle = 'rgba(244, 235, 224, 0.55)'
      c.fillRect(x, ry, w, rowH)
    }
    c.beginPath()
    c.moveTo(x, ry + rowH)
    c.lineTo(x + w, ry + rowH)
    c.strokeStyle = C.lineSoft
    c.lineWidth = 1
    c.stroke()
    txt(c, row[0], x + 8, ry + rowH - 6, 10.2, 600, i === 3 ? C.ink : C.ink2)
    txt(c, row[1], x + w * col[1], ry + rowH - 6, 10.2, 500, C.ink2)
    txt(c, row[2], x + w * col[2], ry + rowH - 6, 10.2, 500, C.ink2)
    txt(c, row[3], x + w * col[3], ry + rowH - 6, 10.2, i === 3 ? 800 : 600, i === 3 ? C.greenDark : C.ink2)
    c.restore()
  })

  const captionAlpha = easeOut(clamp((t - 0.55) / 0.6))
  c.save()
  c.globalAlpha = captionAlpha
  txt(c, 'Tidak ada bentuk untuk dibandingkan.', x, y + h - 3, 10, 600, C.muted)
  txt(c, '34 detik', x + w, y + h - 3, 10, 800, C.rust, 'right')
  c.restore()
}

function drawEncodingChart(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const values = [38, 48, 42, 72, 56]
  const labels = ['A', 'B', 'C', 'D', 'E']
  const maxV = 84
  const baseline = y + h - 26
  const maxH = h - 58
  const bw = compactScene ? 32 : 48
  const gap = compactScene ? 14 : 26
  const totalW = values.length * bw + (values.length - 1) * gap
  const startX = x + (w - totalW) / 2

  c.save()
  c.strokeStyle = C.lineStrong
  c.lineWidth = 1.2
  c.beginPath()
  c.moveTo(x, baseline + 0.5)
  c.lineTo(x + w, baseline + 0.5)
  c.stroke()

  // guide line for the highlighted value
  const guideY = baseline - maxH
  c.strokeStyle = 'rgba(111,105,97,.45)'
  c.setLineDash([4, 5])
  c.beginPath()
  c.moveTo(x + 4, guideY)
  c.lineTo(x + w - 4, guideY)
  c.stroke()
  c.setLineDash([])
  c.restore()

  values.forEach((v, i) => {
    const p = easeOut(clamp((t - i * 0.07) / 0.75))
    const bh = (v / maxV) * maxH * p
    const bx = startX + i * (bw + gap)
    const by = baseline - bh
    const active = i === 3
    fillRR(c, bx, by, bw, bh, 4, active ? C.green2 : i % 2 === 0 ? C.paper2 : C.mint, C.ink, active ? 1.8 : 1.2)
    if (active) {
      c.save()
      c.globalAlpha = easeOut(clamp((t - 0.5) / 0.7))
      txt(c, '72', bx + bw / 2, by - 10, 12, 800, C.greenDark, 'center')
      txt(c, 'nilai → tinggi', bx + bw / 2, by - 23, 8.8, 700, C.muted, 'center')
      c.restore()
    } else {
      txt(c, String(v), bx + bw / 2, by - 7, 9.5, 600, C.muted, 'center')
    }
    txt(c, labels[i], bx + bw / 2, baseline + 17, 10, 600, C.muted, 'center')
  })

  c.save()
  c.globalAlpha = easeOut(clamp((t - 0.7) / 0.7))
  txt(c, 'Skala 0–84 · sumbu dimulai dari nol', x, y + h - 3, 9.5, 500, C.muted)
  c.restore()
}

function drawMarksChannels(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const plotW = w * 0.61
  const plotH = h - 36
  const px = x + 4
  const py = y + 22

  c.save()
  c.strokeStyle = C.lineStrong
  c.lineWidth = 1.1
  c.beginPath()
  c.moveTo(px, py + plotH)
  c.lineTo(px + plotW, py + plotH)
  c.moveTo(px, py)
  c.lineTo(px, py + plotH)
  c.stroke()

  // mark legend
  txt(c, 'MARK', px + 8, y + 10, 9, 800, C.muted)
  // dot
  c.beginPath()
  c.arc(px + 55, y + 7, 3.6, 0, Math.PI * 2)
  c.fillStyle = C.amber
  c.fill()
  c.strokeStyle = C.ink
  c.lineWidth = 1
  c.stroke()
  // line
  c.beginPath()
  c.moveTo(px + 68, y + 8)
  c.lineTo(px + 80, y + 3)
  c.strokeStyle = C.ink
  c.lineWidth = 1.7
  c.stroke()
  // bar
  fillRR(c, px + 89, y + 2, 6, 10, 1, C.violet2, C.ink, 0.9, 0)

  for (let i = 0; i < 15; i++) {
    const p = easeOut(clamp((t - i * 0.035) / 0.65))
    const rx = 0.08 + ((i * 41) % 86) / 100
    const ry = 0.16 + ((i * 29) % 72) / 100
    const r = (3.6 + (i % 4) * 1.55) * p
    const color = [C.amber, C.green2, C.violet2, C.orange][i % 4]
    c.globalAlpha = p * 0.9
    c.beginPath()
    c.arc(px + 10 + rx * (plotW - 24), py + 10 + (1 - ry) * (plotH - 30), r, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.lineWidth = 1.1
    c.strokeStyle = C.ink
    c.stroke()
  }
  c.globalAlpha = 1
  txt(c, 'pendapatan →', px + plotW / 2, y + h - 4, 8.7, 600, C.muted, 'center')
  c.save()
  c.translate(px + 7, py + plotH / 2)
  c.rotate(-Math.PI / 2)
  txt(c, 'kepuasan →', 0, 0, 8.7, 600, C.muted, 'center')
  c.restore()
  c.restore()

  const panelX = x + plotW + 18
  const panelW = w - plotW - 20
  txt(c, 'CHANNEL', panelX, y + 10, 9, 800, C.muted)
  const channels = [
    ['posisi x', 'akurat', C.green2],
    ['posisi y', 'akurat', C.green2],
    ['ukuran', 'kasar', C.amber],
    ['warna', 'kategori', C.violet2],
  ]
  channels.forEach(([name, note, color], i) => {
    const p = easeOut(clamp((t - 0.15 - i * 0.08) / 0.6))
    c.save()
    c.globalAlpha = p
    const cy = y + 25 + i * 40
    fillRR(c, panelX, cy, panelW, 31, 7, C.paper2, C.lineStrong, 1)
    c.beginPath()
    c.arc(panelX + 13, cy + 15.5, 5, 0, Math.PI * 2)
    c.fillStyle = color as string
    c.fill()
    c.strokeStyle = C.ink
    c.lineWidth = 1
    c.stroke()
    txt(c, name as string, panelX + 25, cy + 13, 10, 700, C.ink)
    txt(c, note as string, panelX + 25, cy + 24, 8.5, 600, C.muted)
    c.restore()
  })
}

function drawChooseChart(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const gap = 10
  const tw = (w - gap) / 2
  const th = (h - gap) / 2
  const tiles = [
    { label: 'Bandingkan', fill: C.greenTile, kind: 'bars' },
    { label: 'Distribusi', fill: C.blueSoft, kind: 'hist' },
    { label: 'Tren', fill: C.violet, kind: 'line' },
    { label: 'Hubungan', fill: C.orange, kind: 'scatter' },
  ]

  tiles.forEach((tile, i) => {
    const p = easeOut(clamp((t - i * 0.08) / 0.6))
    const tx = x + (i % 2) * (tw + gap)
    const ty = y + Math.floor(i / 2) * (th + gap)
    c.save()
    c.globalAlpha = p
    fillRR(c, tx, ty, tw, th, 10, tile.fill as string, i === 0 ? C.ink : C.ink2, i === 0 ? 1.9 : 1.2)
    if (i === 0) {
      fillRR(c, tx + tw - 48, ty + 7, 40, 17, 8, C.green2, C.ink, 1, 0)
      txt(c, 'MULAI', tx + tw - 28, ty + 19, 7.5, 800, C.ink, 'center')
    }

    const gx = tx + 20
    const gy = ty + th - 22
    if (tile.kind === 'bars') {
      ;[0.45, 0.7, 0.55, 0.92].forEach((v, j) => {
        fillRR(c, gx + j * 17, gy - 42 * v, 10, 42 * v, 2, C.green3, C.ink, 1, 0)
      })
    } else if (tile.kind === 'hist') {
      ;[0.25, 0.45, 0.8, 0.6, 0.3].forEach((v, j) => {
        fillRR(c, gx + j * 14, gy - 42 * v, 9, 42 * v, 2, C.violet2, C.ink, 1, 0)
      })
    } else if (tile.kind === 'line') {
      c.beginPath()
      const pts = [
        [gx, gy - 8],
        [gx + 16, gy - 22],
        [gx + 31, gy - 16],
        [gx + 48, gy - 32],
        [gx + 63, gy - 40],
      ]
      pts.forEach(([px, py], j) => (j === 0 ? c.moveTo(px, py) : c.lineTo(px, py)))
      c.strokeStyle = C.ink
      c.lineWidth = 2
      c.stroke()
      pts.forEach(([px, py]) => {
        c.beginPath()
        c.arc(px, py, 3, 0, Math.PI * 2)
        c.fillStyle = C.cream
        c.fill()
        c.lineWidth = 1.2
        c.strokeStyle = C.ink
        c.stroke()
      })
    } else {
      for (let j = 0; j < 9; j++) {
        c.beginPath()
        c.arc(gx + 5 + ((j * 23) % 60), gy - 6 - ((j * 17) % 34), 3.1, 0, Math.PI * 2)
        c.fillStyle = j % 2 === 0 ? C.amber : C.rust
        c.fill()
        c.lineWidth = 1
        c.strokeStyle = C.ink
        c.stroke()
      }
    }

    txt(c, tile.label, tx + 14, ty + 22, 11, 800, C.ink)
    txt(c, 'pertanyaan ' + (i + 1), tx + 14, ty + 35, 8, 600, C.muted)
    c.restore()
  })
}

function drawHistogram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const maxV = 30
  const baseline = y + h - 26
  const maxH = h - 58
  const bw = (w - 30) / HIST.length

  // IQR band
  const bandX = x + 8 + bw * 3
  const bandW = bw * 4.3
  c.save()
  c.fillStyle = 'rgba(207, 227, 178, 0.45)'
  c.fillRect(bandX, y + 8, bandW, maxH + 16)
  c.restore()

  c.strokeStyle = C.lineStrong
  c.lineWidth = 1.1
  c.beginPath()
  c.moveTo(x, baseline + 0.5)
  c.lineTo(x + w, baseline + 0.5)
  c.stroke()

  HIST.forEach((v, i) => {
    const p = easeOut(clamp((t - i * 0.055) / 0.7))
    const bh = (v / maxV) * maxH * p
    const bx = x + 12 + i * bw
    const by = baseline - bh
    fillRR(c, bx, by, bw - 7, bh, 3, i >= 6 ? C.amber : C.violet2, C.ink, 1.2)
  })

  // mean line
  const mx = x + 12 + bw * 4.45
  c.save()
  c.strokeStyle = C.ink
  c.lineWidth = 1.5
  c.setLineDash([4, 4])
  c.beginPath()
  c.moveTo(mx, y + 12)
  c.lineTo(mx, baseline)
  c.stroke()
  c.setLineDash([])
  const labelW = 94
  fillRR(c, mx - labelW / 2, y + 3, labelW, 20, 10, C.cream, C.ink, 1.2, 0)
  txt(c, 'rata-rata 68', mx, y + 17, 9.5, 800, C.ink, 'center')
  c.restore()

  ;[0, 2, 4, 6, 8].forEach((i) => {
    txt(c, String(20 + i * 10), x + 12 + i * bw + (bw - 7) / 2, baseline + 16, 8.7, 600, C.muted, 'center')
  })

  c.save()
  c.globalAlpha = easeOut(clamp((t - 0.8) / 0.7))
  txt(c, 'ekor kanan →', x + w - 4, y + 20, 9, 700, C.rust, 'right')
  c.restore()
}

function drawBarChart(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const labelW = compactScene ? 66 : 82
  const valueW = compactScene ? 34 : 46
  const maxW = w - labelW - valueW - 18
  const rowH = Math.min(compactScene ? 24 : 28, (h - 22) / CATS.length)
  const maxV = CATS[0].value
  const top = y + 12

  CATS.forEach((cat, i) => {
    const p = easeOut(clamp((t - i * 0.07) / 0.7))
    const ry = top + i * rowH
    const bh = Math.min(16, rowH - 9)
    txt(c, cat.label, x, ry + bh + 1, 10, i === 0 ? 800 : 500, i === 0 ? C.ink : C.ink2)
    fillRR(c, x + labelW, ry, maxW, bh, 3, C.paper2, 'rgba(198,187,172,.7)', 0.8, 0)
    const bw = (cat.value / maxV) * maxW * p
    fillRR(c, x + labelW, ry, bw, bh, 3, i === 0 ? C.green2 : C.greenTile, C.ink, i === 0 ? 1.3 : 1, 0)
    txt(c, String(cat.value), x + labelW + bw + 7, ry + bh, 10, i === 0 ? 800 : 600, i === 0 ? C.greenDark : C.muted)
  })

  txt(c, 'omzet dalam juta rupiah', x, y + h - 3, 9, 500, C.muted)
}

function drawLineChart(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, annotated: boolean) {
  const padL = 26
  const padR = 14
  const padT = 26
  const padB = 24
  const plotW = w - padL - padR
  const plotH = h - padT - padB
  const minV = 30
  const maxV = 126
  const xAt = (i: number) => x + padL + (i / (REV.length - 1)) * plotW
  const yAt = (v: number) => y + padT + plotH - ((v - minV) / (maxV - minV)) * plotH
  const p = easeOut(clamp(t / 1.1))

  // Q4 band
  c.save()
  c.fillStyle = 'rgba(207, 227, 178, 0.42)'
  c.fillRect(xAt(9) - 6, y + padT - 4, xAt(11) - xAt(9) + 12, plotH + 8)
  txt(c, 'Q4', xAt(10), y + padT + 10, 8.5, 800, C.greenDark, 'center')
  c.restore()

  // whispers of horizontal grid
  for (let i = 0; i < 4; i++) {
    const gy = y + padT + (plotH / 3) * i
    c.beginPath()
    c.moveTo(x + padL, gy)
    c.lineTo(x + padL + plotW, gy)
    c.strokeStyle = 'rgba(198,187,172,.35)'
    c.lineWidth = 1
    c.setLineDash([3, 6])
    c.stroke()
    c.setLineDash([])
  }

  c.save()
  c.beginPath()
  c.rect(x + padL - 2, y + padT - 10, plotW * p + 4, plotH + 20)
  c.clip()

  const area = c.createLinearGradient(0, y + padT, 0, y + padT + plotH)
  area.addColorStop(0, 'rgba(178, 212, 145, 0.5)')
  area.addColorStop(1, 'rgba(178, 212, 145, 0.03)')
  c.beginPath()
  REV.forEach((v, i) => (i === 0 ? c.moveTo(xAt(i), yAt(v)) : c.lineTo(xAt(i), yAt(v))))
  c.lineTo(xAt(REV.length - 1), y + padT + plotH)
  c.lineTo(xAt(0), y + padT + plotH)
  c.closePath()
  c.fillStyle = area
  c.fill()

  c.beginPath()
  REV.forEach((v, i) => (i === 0 ? c.moveTo(xAt(i), yAt(v)) : c.lineTo(xAt(i), yAt(v))))
  c.strokeStyle = C.greenDark
  c.lineWidth = 2.4
  c.lineJoin = 'round'
  c.stroke()
  c.restore()

  REV.forEach((v, i) => {
    const q = easeOut(clamp((t - 0.15 - i * 0.035) / 0.55))
    if (q <= 0) return
    const last = i >= 9
    c.globalAlpha = q
    c.beginPath()
    c.arc(xAt(i), yAt(v), last ? 4 : 3.2, 0, Math.PI * 2)
    c.fillStyle = last ? C.amber : C.cream
    c.fill()
    c.lineWidth = 1.4
    c.strokeStyle = C.ink
    c.stroke()
    c.globalAlpha = 1
  })

  MONTHS.forEach((m, i) => {
    if (i % 2 !== 0) return
    txt(c, m, xAt(i), y + h - 4, 8.5, 600, C.muted, 'center')
  })

  if (annotated) {
    const boxW = compactScene ? 168 : 202
    const boxH = compactScene ? 58 : 64
    const bx = x + w - boxW - 4
    const by = y + 2
    const calloutP = easeOut(clamp((t - 0.9) / 0.7))
    c.save()
    c.globalAlpha = calloutP
    popBox(c, bx, by, boxW, boxH, 10, C.greenTile, 1.5, 2)
    txt(c, 'Q4 +38%', bx + 11, by + 22, compactScene ? 13 : 15, 800, C.ink)
    txt(c, 'vs Q3', bx + 11, by + 38, 9.1, 700, C.muted)
    txt(c, 'dorong stok lebih awal', bx + 11, by + 52, 9.1, 600, C.ink2)
    c.beginPath()
    c.moveTo(bx - 2, by + boxH - 1)
    c.lineTo(xAt(11), yAt(118) - 4)
    c.strokeStyle = 'rgba(29,27,24,.55)'
    c.lineWidth = 1.2
    c.setLineDash([3, 4])
    c.stroke()
    c.setLineDash([])
    const pulse = 4 + Math.sin(t * 3) * 1.5
    c.beginPath()
    c.arc(xAt(11), yAt(118), pulse + 4, 0, Math.PI * 2)
    c.strokeStyle = 'rgba(47,138,67,.45)'
    c.lineWidth = 1.5
    c.stroke()
    c.restore()
  } else {
    const p2 = easeOut(clamp((t - 0.7) / 0.6))
    c.save()
    c.globalAlpha = p2
    fillRR(c, x + w - 82, y + 2, 78, 24, 12, C.cream, C.ink, 1.2, 0)
    txt(c, 'Q4 +38%', x + w - 43, y + 18, 9.5, 800, C.greenDark, 'center')
    c.restore()
  }
}

function drawScatterChart(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const padL = 28
  const padR = 16
  const padT = 16
  const padB = 24
  const plotW = w - padL - padR
  const plotH = h - padT - padB
  const px = (v: number) => x + padL + v * plotW
  const py = (v: number) => y + padT + (1 - v) * plotH

  c.strokeStyle = C.lineStrong
  c.lineWidth = 1.1
  c.beginPath()
  c.moveTo(x + padL, y + padT)
  c.lineTo(x + padL, y + padT + plotH)
  c.lineTo(x + padL + plotW, y + padT + plotH)
  c.stroke()

  // regression hint
  c.save()
  c.strokeStyle = 'rgba(29,27,24,.5)'
  c.lineWidth = 1.3
  c.setLineDash([5, 5])
  c.beginPath()
  c.moveTo(px(0.06), py(0.16))
  c.lineTo(px(0.93), py(0.84))
  c.stroke()
  c.setLineDash([])
  c.restore()

  SCATTER_POINTS.forEach((point, i) => {
    const p = easeOut(clamp((t - i * 0.03) / 0.55))
    if (p <= 0) return
    c.save()
    c.globalAlpha = p * 0.9
    c.beginPath()
    c.arc(px(point.x), py(point.y), point.size * p, 0, Math.PI * 2)
    c.fillStyle = point.color
    c.fill()
    c.lineWidth = 1.1
    c.strokeStyle = C.ink
    c.stroke()
    c.restore()
  })

  // highlighted point
  const hp = easeOut(clamp((t - 0.7) / 0.6))
  if (hp > 0) {
    c.save()
    c.globalAlpha = hp
    c.beginPath()
    c.arc(px(0.78), py(0.84), 6.2, 0, Math.PI * 2)
    c.fillStyle = C.green2
    c.fill()
    c.lineWidth = 1.6
    c.strokeStyle = C.ink
    c.stroke()
    c.beginPath()
    c.arc(px(0.78), py(0.84), 11 + Math.sin(t * 2.4) * 2, 0, Math.PI * 2)
    c.strokeStyle = 'rgba(47,138,67,.4)'
    c.lineWidth = 1.3
    c.stroke()
    c.restore()
  }

  txt(c, 'belanja iklan →', x + padL + plotW / 2, y + h - 3, 8.7, 600, C.muted, 'center')
  c.save()
  c.translate(x + 9, y + padT + plotH / 2)
  c.rotate(-Math.PI / 2)
  txt(c, 'penjualan →', 0, 0, 8.7, 600, C.muted, 'center')
  c.restore()

  const pillP = easeOut(clamp((t - 0.8) / 0.6))
  c.save()
  c.globalAlpha = pillP
  fillRR(c, x + w - 134, y + 2, 130, 24, 12, C.rustSoft, C.ink, 1.2, 0)
  txt(c, 'korelasi ≠ kausalitas', x + w - 69, y + 18, 8.5, 800, C.red, 'center')
  fillRR(c, x + 4, y + 2, 80, 24, 12, C.cream, C.ink, 1.2, 0)
  txt(c, 'n = 30 titik', x + 44, y + 18, 8.8, 800, C.ink2, 'center')
  c.restore()
}

function drawDataInk(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const clean = easeOut(clamp((t - 1.05) / 2.5))
  const values = [42, 58, 51, 72, 88]
  const labels = ['A', 'B', 'C', 'D', 'E']
  const baseline = y + h - 26
  const maxH = h - 58
  const bw = compactScene ? 30 : 44
  const gap = compactScene ? 14 : 30
  const totalW = values.length * bw + (values.length - 1) * gap
  const startX = x + (w - totalW) / 2
  const junk = 1 - clean

  // chartjunk: gridlines and tick labels
  c.save()
  c.globalAlpha = junk
  for (let i = 0; i <= 4; i++) {
    const gy = baseline - (maxH / 4) * i
    c.beginPath()
    c.moveTo(x, gy)
    c.lineTo(x + w, gy)
    c.strokeStyle = 'rgba(29,27,24,.22)'
    c.lineWidth = i === 0 ? 1.5 : 1
    c.stroke()
    txt(c, String(i * 25), x + 2, gy - 3, 8.2, 600, C.muted2)
  }
  // decorative frame
  c.strokeStyle = 'rgba(29,27,24,.28)'
  c.lineWidth = 1
  c.strokeRect(x - 4, y - 4, w + 8, h + 8)
  c.restore()

  values.forEach((v, i) => {
    const bx = startX + i * (bw + gap)
    const bh = (v / 100) * maxH
    const by = baseline - bh
    c.save()
    c.globalAlpha = junk
    fillRR(c, bx + 7, by + 8, bw, bh, 3, 'rgba(29,27,24,.22)', undefined, 0)
    c.restore()
    fillRR(c, bx, by, bw, bh, 3, i === 4 ? C.green2 : C.greenTile, C.ink, 1.2)
    // always-useful direct label
    txt(c, String(v), bx + bw / 2, by - 8, 9.5, 800, i === 4 ? C.greenDark : C.ink2, 'center')
    txt(c, labels[i], bx + bw / 2, baseline + 16, 9.5, 600, C.muted, 'center')
    // chartjunk redundant labels
    c.save()
    c.globalAlpha = junk * 0.9
    txt(c, 'value', bx + bw / 2, baseline + 29, 7.2, 600, C.muted2, 'center')
    c.restore()
  })

  const meterP = easeOut(clamp(t / 0.8))
  const inkValue = Math.round(42 + clean * 42)
  c.save()
  c.globalAlpha = meterP
  fillRR(c, x + w - 160, y + 2, 160, 24, 12, clean > 0.6 ? C.greenTile : C.paper2, C.lineStrong, 1, 0)
  txt(c, `${inkValue}%`, x + w - 150, y + 19, 9.5, 800, clean > 0.6 ? C.greenDark : C.muted)
  fillRR(c, x + w - 108, y + 10, 96, 8, 4, C.lineSoft, undefined, 0)
  fillRR(c, x + w - 108, y + 10, 96 * (inkValue / 100), 8, 4, C.green2, undefined, 0)
  c.restore()
}

function drawCompactBackdrop(c: CanvasRenderingContext2D, t: number, w: number, h: number) {
  const glow = c.createRadialGradient(w * 0.5, h * 0.38, 20, w * 0.5, h * 0.38, Math.max(w, h) * 0.7)
  glow.addColorStop(0, 'rgba(255, 253, 248, 0.8)')
  glow.addColorStop(0.6, 'rgba(255, 253, 248, 0.2)')
  glow.addColorStop(1, 'rgba(255, 253, 248, 0)')
  c.fillStyle = glow
  c.fillRect(0, 0, w, h)

  drawPerspectiveFloor(c, w, h, 0.28, 15, 0.085)

  const dots = [
    [w * 0.06, h * 0.17, C.amber],
    [w * 0.94, h * 0.28, C.violet2],
    [w * 0.9, h * 0.82, C.green2],
    [w * 0.1, h * 0.78, C.rust],
  ] as const
  dots.forEach(([x, y, color], i) => {
    c.globalAlpha = 0.6 + Math.sin(t * 1.2 + i) * 0.2
    c.beginPath()
    c.arc(x, y, 2.8, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.globalAlpha = 1
  })
}

function drawCompactCard(c: CanvasRenderingContext2D, t: number, stepIndex: number, x: number, y: number, w: number, h: number) {
  const bob = Math.sin(t * 0.85 + 0.8) * 1.4
  y += bob
  const r = 13

  c.save()
  c.globalAlpha = 0.1
  c.fillStyle = C.ink
  c.beginPath()
  c.ellipse(x + w / 2, y + h + 12, w * 0.35, 13, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()

  fillRR(c, x + 5, y + 7, w, h, r, C.ink)
  fillRR(c, x, y, w, h, r, C.cream)

  c.save()
  rr(c, x, y, w, h, r)
  c.clip()
  c.fillStyle = C.paper
  c.fillRect(x, y, w, 36)
  c.restore()
  c.beginPath()
  c.moveTo(x + 1, y + 36)
  c.lineTo(x + w - 1, y + 36)
  c.strokeStyle = C.line
  c.lineWidth = 1.1
  c.stroke()

  ;[C.green3, C.amber, C.rust].forEach((color, i) => {
    c.beginPath()
    c.arc(x + 16 + i * 10, y + 18, 3, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.strokeStyle = 'rgba(29,27,24,.7)'
    c.lineWidth = 0.8
    c.stroke()
  })
  txt(c, 'grafik.view', x + 48, y + 22, 10, 800)
  txt(c, 'penjualan.csv', x + w - 14, y + 22, 8.5, 600, C.muted, 'right')

  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 1.9
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.chartTitle.toUpperCase(), x + 20, y + 58, 8.4, 800, C.muted)
  txt(c, s.chartMetric, x + 20, y + 80, s.chartMetric.length > 22 ? 12 : 14, 800, C.ink)

  const ax = x + 20
  const ay = y + 96
  const aw = w - 40
  const ah = h - 114

  c.save()
  rr(c, x + 2, y + 40, w - 4, h - 42, 9)
  c.clip()
  drawChartBody(c, stepIndex, t, ax, ay, aw, ah)
  c.restore()
}

function drawCompactScene(c: CanvasRenderingContext2D, t: number, stepIndex: number, w: number, h: number) {
  drawCompactBackdrop(c, t, w, h)
  const pillW = Math.min(260, w - 24)
  drawInsightPill(c, t, stepIndex, (w - pillW) / 2, 8, pillW, 36)
  drawCompactCard(c, t, stepIndex, 6, 55, w - 12, h - 60)
}

function drawScene(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  drawBackdrop(c, t)
  drawPlatform(c, t)
  drawFlow(c, t, stepIndex)
  drawChartCard(c, t, stepIndex)
  drawInsightPill(c, t, stepIndex)
  pill(c, '1.000 baris data', 84, 519, { size: 11.5, h: 30, dot: C.amber })
}

/* ------------------------------------------------------------------ */
/* Canvas lifecycle                                                    */
/* ------------------------------------------------------------------ */

let ctx: CanvasRenderingContext2D | null = null
let dpr = 1
let compactScene = false
let clock = 0
let lastTs = 0
let dirty = true
let raf = 0
let resizeObserver: ResizeObserver | null = null

function resizeCanvas() {
  const canvas = canvasEl.value
  const wrap = canvasWrap.value
  if (!canvas || !wrap) return
  const rect = wrap.getBoundingClientRect()
  if (rect.width < 2 || rect.height < 2) return
  dpr = Math.min(2, window.devicePixelRatio || 1)
  canvas.width = Math.round(rect.width * dpr)
  canvas.height = Math.round(rect.height * dpr)
  dirty = true
  drawCanvas()
}

function drawCanvas() {
  const canvas = canvasEl.value
  if (!canvas || !ctx) return
  const rect = canvas.getBoundingClientRect()
  const w = rect.width
  const h = rect.height
  if (w < 2 || h < 2) return
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  ctx.clearRect(0, 0, w, h)
  compactScene = w < 770
  if (compactScene) {
    drawCompactScene(ctx, clock, current.value, w, h)
    return
  }
  const scale = Math.min(w / DW, h / DH)
  const ox = (w - DW * scale) / 2
  const oy = (h - DH * scale) / 2
  ctx.save()
  ctx.translate(ox, oy)
  ctx.scale(scale, scale)
  drawScene(ctx, clock, current.value)
  ctx.restore()
}

function frame(ts: number) {
  const dt = lastTs ? Math.min(0.05, (ts - lastTs) / 1000) : 0.016
  lastTs = ts
  if (!paused.value && !reducedMotion.value) {
    clock += dt
    dirty = true
  }
  if (dirty) {
    drawCanvas()
    dirty = false
  }
  raf = requestAnimationFrame(frame)
}

const STATIC_CLOCK = 4.2

function resetClock() {
  clock = paused.value || reducedMotion.value ? STATIC_CLOCK : 0
  lastTs = 0
  dirty = true
  drawCanvas()
}

function replay() {
  if (paused.value && !reducedMotion.value) paused.value = false
  clock = reducedMotion.value ? STATIC_CLOCK : 0
  lastTs = 0
  dirty = true
  drawCanvas()
}

function togglePause() {
  paused.value = !paused.value
  if (!paused.value && reducedMotion.value) reducedMotion.value = false
  if (!paused.value && clock > 1.2) clock = 0.4
  lastTs = 0
  dirty = true
  drawCanvas()
}

async function toggleFullscreen() {
  const el = stageEl.value
  if (!el) return
  try {
    if (!document.fullscreenElement) await el.requestFullscreen()
    else await document.exitFullscreen()
  } catch {
    /* browser may refuse fullscreen; keep the page as-is */
  }
}

function onFullscreenChange() {
  isFullscreen.value = Boolean(document.fullscreenElement)
  requestAnimationFrame(resizeCanvas)
}

function onKeydown(event: KeyboardEvent) {
  const target = event.target instanceof Element ? (event.target as HTMLElement) : null
  const tag = target?.tagName?.toLowerCase()
  const typing = tag === 'input' || tag === 'textarea' || tag === 'select' || Boolean(target?.isContentEditable)

  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
    event.preventDefault()
    searchOpen.value ? closeSearch() : openSearch()
    return
  }

  if (searchOpen.value) {
    if (event.key === 'Escape') {
      event.preventDefault()
      closeSearch()
    }
    return
  }

  if (typing) return

  if (event.key === 'Escape') {
    if (drawerOpen.value) drawerOpen.value = false
    else if (document.fullscreenElement) document.exitFullscreen()
    return
  }

  if (event.key === 'ArrowRight') {
    event.preventDefault()
    next()
  } else if (event.key === 'ArrowLeft') {
    event.preventDefault()
    prev()
  } else if (event.key.toLowerCase() === 'r') {
    event.preventDefault()
    replay()
  } else if (event.code === 'Space' || event.key === ' ') {
    if (target?.closest('button, a, input, textarea')) return
    event.preventDefault()
    togglePause()
  }
}

watch(current, () => {
  resetClock()
  if (typeof window !== 'undefined') {
    const url = new URL(window.location.href)
    if (current.value === 0) url.searchParams.delete('step')
    else url.searchParams.set('step', String(current.value + 1))
    window.history.replaceState({}, '', url)
  }
  nextTick(() => {
    guideEl.value?.scrollTo({ top: 0, behavior: 'smooth' })
  })
})

watch(searchOpen, async (open) => {
  if (open) {
    searchQuery.value = ''
    await nextTick()
    searchInput.value?.focus()
  }
})

watch([drawerOpen, searchOpen], ([drawer, palette]) => {
  if (typeof document === 'undefined') return
  document.body.style.overflow = drawer || palette ? 'hidden' : ''
})

onMounted(() => {
  const canvas = canvasEl.value
  if (!canvas) return
  ctx = canvas.getContext('2d')

  const initialStep = readInitialStep()
  if (initialStep > 0) current.value = initialStep

  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reducedMotion.value) {
    paused.value = true
    clock = STATIC_CLOCK
  }

  resizeObserver = new ResizeObserver(() => resizeCanvas())
  if (canvasWrap.value) resizeObserver.observe(canvasWrap.value)
  resizeCanvas()
  drawCanvas()

  window.addEventListener('keydown', onKeydown)
  document.addEventListener('fullscreenchange', onFullscreenChange)

  if (document.fonts?.ready) {
    document.fonts.ready.then(() => {
      dirty = true
      drawCanvas()
    })
  }

  raf = requestAnimationFrame(frame)
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  resizeObserver?.disconnect()
  window.removeEventListener('keydown', onKeydown)
  document.removeEventListener('fullscreenchange', onFullscreenChange)
  document.body.style.overflow = ''
  ctx = null
})
</script>

<style scoped>
@font-face {
  font-family: "JetBrains Mono";
  src: url("/Perkuliahan/fonts/jetbrains-mono.woff2") format("woff2");
  font-weight: 100 800;
  font-style: normal;
  font-display: swap;
}

.dv-root {
  --paper: #f4ebe0;
  --paper-2: #f7efe4;
  --sheet: #f9f2e8;
  --card: #f8f0e6;
  --line: #ddd3c5;
  --line-soft: #e6ddd0;
  --line-strong: #c6bbac;
  --ink: #1d1b18;
  --ink-2: #34302b;
  --muted: #6f6961;
  --muted-2: #8b847a;
  --green: #cfe3b2;
  --green-2: #b2d491;
  --green-3: #7fc278;
  --green-tile: #e8efd9;
  --green-tile-line: #c9d6b3;
  --violet: #e7ddf5;
  --violet-tile: #ebe3f1;
  --violet-tile-line: #d5c8e2;
  --orange: #fcdcbd;
  --mint: #dff0de;
  --rust: #d0683a;
  --radius: 12px;
  --pop-shadow: 1.5px 2.5px 0 var(--ink);
  --card-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65), 0 1px 0 rgba(80, 60, 35, 0.05), 0 10px 22px -16px rgba(80, 60, 35, 0.35);
  position: fixed;
  inset: 0;
  z-index: 80;
  display: grid;
  grid-template-rows: 54px minmax(0, 1fr);
  overflow: hidden;
  background:
    radial-gradient(120% 80% at 50% 0%, rgba(255, 255, 255, 0.35), transparent 60%),
    var(--paper);
  color: var(--ink);
  font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 13px;
  line-height: 1.4;
  font-feature-settings: "calt" 0, "liga" 0;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

.dv-root::after {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 30;
  pointer-events: none;
  opacity: 0.05;
  mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.3 0 0 0 0 0.25 0 0 0 0 0.18 0 0 0 1 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.dv-root *,
.dv-root *::before,
.dv-root *::after {
  box-sizing: border-box;
}

.dv-root button,
.dv-root input {
  font: inherit;
  color: inherit;
}

.dv-root :where(button) {
  border: 0;
  background: none;
  padding: 0;
  cursor: pointer;
}

.dv-root a {
  color: inherit;
  text-decoration: none;
}

.dv-root :where(h1, h2, p, ul, ol) {
  margin: 0;
  padding: 0;
}

.dv-root :where(ul, ol) {
  list-style: none;
}

.dv-root svg {
  display: block;
  flex: none;
}

.dv-root :focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: 3px;
  border-radius: 4px;
}

.dv-root ::selection {
  background: rgba(178, 212, 145, 0.65);
  color: var(--ink);
}

.dv-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* ---------------- top bar ---------------- */

.dv-topbar {
  position: relative;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 0 18px 0 24px;
  border-bottom: 1px solid var(--line-strong);
  background: linear-gradient(rgba(255, 255, 255, 0.28), rgba(255, 255, 255, 0));
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.35), 0 8px 18px -16px rgba(80, 60, 35, 0.45);
}

.dv-menu-btn {
  display: none;
  width: 36px;
  height: 36px;
  flex: none;
  margin-right: 8px;
  border: 1.3px solid var(--line-strong);
  border-radius: 9px;
  background: rgba(250, 245, 238, 0.7);
  color: var(--ink-2);
  place-items: center;
}

.dv-menu-btn svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
}

.dv-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: none;
  margin-right: 18px;
}

.dv-logo {
  width: 34px;
  height: 34px;
  filter: drop-shadow(1px 1.5px 0 rgba(29, 27, 24, 0.9));
}

.dv-brand__name {
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -0.03em;
  white-space: nowrap;
}

.dv-brand__name span {
  background: linear-gradient(transparent 56%, rgba(178, 212, 145, 0.8) 56%);
  padding: 0 1px;
}

.dv-brand__sub {
  padding-left: 10px;
  border-left: 1px solid var(--line-strong);
  color: var(--muted-2);
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.06em;
}

.dv-nav {
  display: flex;
  align-items: center;
  gap: 3px;
}

.dv-nav__item {
  display: inline-flex;
  align-items: center;
  height: 34px;
  padding: 0 17px;
  border: 1.5px solid transparent;
  border-radius: 8px;
  color: var(--ink-2);
  font-size: 13.5px;
  font-weight: 600;
  white-space: nowrap;
}

.dv-nav__item:hover {
  background: rgba(255, 255, 255, 0.35);
}

.dv-nav__item.is-active {
  padding: 0 24px;
  border-color: var(--ink);
  background: var(--green);
  color: var(--ink);
  box-shadow: var(--pop-shadow);
}

.dv-search {
  display: flex;
  align-items: center;
  gap: 9px;
  width: 310px;
  height: 34px;
  margin-left: auto;
  padding: 0 7px 0 12px;
  border: 1.3px solid var(--line-strong);
  border-radius: 9px;
  background: rgba(250, 245, 238, 0.7);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65), 0 1px 0 rgba(80, 60, 35, 0.05);
  color: var(--ink-2);
  text-align: left;
  transition: border-color 0.15s, background 0.15s;
}

.dv-search:hover {
  border-color: var(--muted-2);
  background: rgba(255, 252, 247, 0.9);
}

.dv-search svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.4;
  stroke-linecap: round;
}

.dv-search__hint {
  flex: 1;
  min-width: 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--muted-2);
  font-size: 12.5px;
}

.dv-search kbd,
.dv-palette kbd,
.dv-guide__hint kbd {
  padding: 2px 6px;
  border: 1px solid var(--line-strong);
  border-radius: 5px;
  background: var(--paper-2);
  color: var(--muted);
  font-family: inherit;
  font-size: 10px;
  font-weight: 700;
  line-height: 1.2;
}

.dv-credit {
  display: flex;
  align-items: center;
  gap: 9px;
  flex: none;
  margin-left: 14px;
  padding: 3px 4px 3px 3px;
  border-radius: 9px;
}

.dv-credit:hover .dv-credit__x {
  transform: rotate(-7deg) scale(1.05);
}

.dv-credit__x {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border: 1.5px solid var(--ink);
  border-radius: 8px;
  background: var(--ink);
  color: var(--cream, #fbf7f1);
  box-shadow: 1.5px 2px 0 rgba(29, 27, 24, 0.22);
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dv-credit__x svg {
  width: 17px;
  height: 17px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-credit__text {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.dv-credit__text small {
  color: var(--muted);
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.dv-credit__text b {
  font-size: 12px;
  font-weight: 800;
  white-space: nowrap;
}

.dv-credit__text b span {
  background: linear-gradient(transparent 58%, rgba(178, 212, 145, 0.8) 58%);
}

/* ---------------- layout ---------------- */

.dv-body {
  position: relative;
  display: grid;
  grid-template-columns: 252px minmax(0, 1fr) 344px;
  min-height: 0;
}

.dv-sidebar {
  display: flex;
  flex-direction: column;
  min-height: 0;
  padding: 23px 12px 13px 22px;
}

.dv-tree-root {
  display: flex;
  align-items: center;
  gap: 9px;
  padding-right: 6px;
  font-size: 15px;
  font-weight: 800;
}

.dv-tree-root .dv-folder {
  width: 20px;
  height: 16px;
}

.dv-tree-root__meta {
  margin-left: auto;
  color: var(--muted);
  font-size: 10.5px;
  font-weight: 600;
}

.dv-drawer-close {
  display: none;
  width: 30px;
  height: 30px;
  margin-left: 6px;
  place-items: center;
  border: 1.3px solid var(--line-strong);
  border-radius: 8px;
  color: var(--ink-2);
}

.dv-drawer-close svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
}

.dv-course {
  flex: 1;
  min-height: 0;
  margin: 12px -6px 12px 0;
  padding-right: 6px;
  overflow-y: auto;
  scrollbar-width: thin;
}

.dv-course::-webkit-scrollbar,
.dv-guide__content::-webkit-scrollbar,
.dv-palette__list::-webkit-scrollbar {
  width: 7px;
}

.dv-course::-webkit-scrollbar-thumb,
.dv-guide__content::-webkit-scrollbar-thumb,
.dv-palette__list::-webkit-scrollbar-thumb {
  border-radius: 99px;
  background: var(--line-strong);
}

.dv-mod__head {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 34px;
  padding: 3px 0;
  color: var(--ink);
  text-align: left;
  font-size: 13.5px;
  font-weight: 700;
}

.dv-chev {
  width: 12px;
  height: 12px;
  margin-right: 7px;
  fill: none;
  stroke: var(--ink-2);
  stroke-width: 1.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform 0.3s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-mod.is-open .dv-chev {
  transform: rotate(90deg);
}

.dv-folder {
  width: 19px;
  height: 15px;
  margin-right: 9px;
}

.dv-folder__back,
.dv-folder__front {
  stroke-width: 0.8;
  stroke: rgba(29, 27, 24, 0.55);
}

.dv-folder--sand .dv-folder__back { fill: #c9a670; }
.dv-folder--sand .dv-folder__front { fill: #e0c28d; }
.dv-folder--green .dv-folder__back { fill: #2f8a43; }
.dv-folder--green .dv-folder__front { fill: #5fae57; }
.dv-folder--violet .dv-folder__back { fill: #5a43a6; }
.dv-folder--violet .dv-folder__front { fill: #8b79c9; }

.dv-mod__title {
  display: -webkit-box;
  overflow: hidden;
  min-width: 0;
  line-height: 1.25;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.dv-mod__count {
  flex: none;
  margin-left: auto;
  padding-left: 8px;
  color: var(--muted-2);
  font-size: 10.5px;
  font-weight: 600;
}

.dv-mod__body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.32s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-mod.is-open .dv-mod__body {
  grid-template-rows: 1fr;
}

.dv-mod__clip {
  min-height: 0;
  overflow: hidden;
}

.dv-mod__lessons {
  position: relative;
  margin: 1px 4px 8px 20px;
  padding-left: 0;
  opacity: 0;
  transform: translateY(-5px);
  transition: opacity 0.22s, transform 0.32s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-mod.is-open .dv-mod__lessons {
  opacity: 1;
  transform: none;
  transition-delay: 35ms;
}

.dv-mod__lessons::before {
  content: "";
  position: absolute;
  top: -2px;
  bottom: 14px;
  left: 0;
  border-left: 1px solid #aba294;
}

.dv-lesson {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 30px;
  padding-left: 15px;
  font-size: 12.5px;
  font-weight: 500;
}

.dv-lesson::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  width: 12px;
  border-top: 1px solid #aba294;
}

.dv-lesson button {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 27px;
  margin-left: -7px;
  padding: 3px 8px;
  border: 1.5px solid transparent;
  border-radius: 8px;
  color: var(--ink);
  text-align: left;
  transition: background-color 0.25s, border-color 0.25s, box-shadow 0.25s;
}

.dv-lesson button:hover {
  background: rgba(255, 255, 255, 0.38);
}

.dv-lesson__mark {
  display: inline-flex;
  align-items: center;
  justify-content: flex-start;
  width: 24px;
  flex: none;
  color: var(--muted-2);
}

.dv-lesson__mark svg {
  width: 13px;
  height: 13px;
  fill: none;
  stroke: var(--green-dark, #2f8a43);
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-lesson__num {
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.dv-lesson.is-current button {
  border-color: var(--ink);
  background: var(--green);
  box-shadow: 1.5px 2.5px 0 var(--ink);
  font-weight: 800;
}

.dv-lesson.is-current .dv-lesson__mark {
  color: var(--ink);
}

.dv-lesson.is-current .dv-lesson__num {
  font-size: 10px;
}

.dv-lesson.is-done .dv-lesson__mark {
  color: var(--green-dark, #2f8a43);
}

.dv-lesson__title {
  min-width: 0;
  overflow: hidden;
  line-height: 1.3;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.dv-progress {
  flex: none;
  margin-top: 4px;
  padding: 10px 13px 11px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--paper-2);
}

.dv-progress__head {
  display: flex;
  align-items: center;
  gap: 8px;
}

.dv-progress__pct {
  margin-left: auto;
  color: var(--ink-2);
  font-size: 11px;
  font-weight: 800;
}

.dv-bar {
  position: relative;
  height: 9px;
  margin-top: 8px;
  overflow: hidden;
  border: 1.2px solid #5d564e;
  border-radius: 6px;
  background: #fbf6ef;
}

.dv-bar span {
  position: absolute;
  inset: 0 auto 0 0;
  border-right: 1.2px solid #5d564e;
  border-radius: 0 5px 5px 0;
  background: linear-gradient(#bddb9e, var(--green-2));
  transition: width 0.6s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-progress__foot {
  display: flex;
  justify-content: space-between;
  margin-top: 7px;
  color: var(--muted);
  font-size: 9.5px;
  font-weight: 600;
}

/* ---------------- sheet ---------------- */

.dv-sheet {
  display: flex;
  flex-direction: column;
  min-height: 0;
  margin: 12px 0 14px 2px;
  padding: 0 16px 13px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: linear-gradient(rgba(255, 255, 255, 0.22), rgba(255, 255, 255, 0) 220px), var(--sheet);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8), 0 1px 0 rgba(80, 60, 35, 0.05), 0 18px 40px -30px rgba(80, 60, 35, 0.35);
}

.dv-lesson-head {
  flex: none;
  padding: 17px 2px 0;
}

.dv-crumb {
  color: var(--ink-2);
  font-size: 12px;
  font-weight: 500;
}

.dv-crumb span {
  margin: 0 4px;
  color: var(--muted-2);
}

.dv-lesson-head__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-top: 6px;
}

.dv-title-wrap {
  min-width: 0;
}

.dv-title {
  overflow: hidden;
  color: var(--ink);
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -0.015em;
  line-height: 1.12;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.dv-subtitle {
  margin-top: 6px;
  overflow: hidden;
  color: var(--muted);
  font-size: 12.5px;
  line-height: 1.4;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.dv-tags {
  display: flex;
  flex: none;
  gap: 8px;
}

.dv-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 25px;
  padding: 0 10px 0 9px;
  border: 1.3px solid var(--ink-2);
  border-radius: 13px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35), 0 1.5px 0 var(--ink-2);
  font-size: 10.5px;
  font-weight: 700;
  white-space: nowrap;
}

.dv-tag svg {
  width: 13px;
  height: 13px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.4;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-tag--sand { background: #f6e6c9; }
.dv-tag--mint { background: var(--mint); }
.dv-tag--violet { background: var(--violet); }

/* ---------------- stage ---------------- */

.dv-stage {
  position: relative;
  flex: 1;
  min-height: 360px;
  margin-top: 12px;
  overflow: hidden;
  background: #faf3e9;
}

.dv-stage:fullscreen {
  width: 100vw;
  height: 100vh;
  margin: 0;
  background: #faf3e9;
}

.dv-stage:fullscreen .dv-stage__canvas {
  inset: 76px 18px 44px;
}

.dv-stage__hud {
  position: absolute;
  top: 12px;
  right: 210px;
  left: 12px;
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  pointer-events: none;
}

.dv-chip {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 105px;
  padding: 5px 10px 6px 11px;
  border: 1px solid var(--line-strong);
  border-radius: 9px;
  background: rgba(251, 247, 241, 0.92);
  box-shadow: 0 1px 0 rgba(80, 60, 35, 0.06);
}

.dv-chip::before {
  content: "";
  position: absolute;
  top: 8px;
  bottom: 8px;
  left: -1px;
  width: 3px;
  border-radius: 0 3px 3px 0;
  background: transparent;
  transition: background 0.35s;
}

.dv-chip[data-level="good"]::before { background: #4caf50; }
.dv-chip[data-level="warn"]::before { background: #e8a33a; }

.dv-chip__label {
  display: flex;
  align-items: center;
  gap: 4px;
  color: var(--muted);
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.04em;
  white-space: nowrap;
}

.dv-chip__label svg {
  width: 11px;
  height: 11px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-chip__value {
  overflow: hidden;
  font-size: 13.5px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  animation: dv-value-in 0.4s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-chip[data-level="warn"] .dv-chip__value { color: #a5650c; }
.dv-chip[data-level="good"] .dv-chip__value { color: var(--ink); }

@keyframes dv-value-in {
  from { opacity: 0; transform: translateY(4px); }
}

.dv-stage__tools {
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 3;
  display: flex;
  gap: 7px;
}

.dv-tool {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 30px;
  padding: 0 10px;
  border: 1.3px solid var(--ink-2);
  border-radius: 8px;
  background: #fbf7f1;
  box-shadow: 0 1.5px 0 var(--ink-2);
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
}

.dv-tool:hover {
  background: #fff;
}

.dv-tool:active {
  transform: translateY(1px);
  box-shadow: 0 0.5px 0 var(--ink-2);
}

.dv-tool.is-on {
  background: var(--green);
}

.dv-tool svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-tool--icon {
  width: 32px;
  justify-content: center;
  padding: 0;
}

.dv-stage__canvas {
  position: absolute;
  inset: 64px 10px 36px;
}

.dv-stage__canvas canvas {
  display: block;
  width: 100%;
  height: 100%;
}

.dv-stage__legend {
  position: absolute;
  bottom: 10px;
  left: 14px;
  z-index: 2;
  display: flex;
  gap: 15px;
  color: var(--muted);
  font-size: 10.5px;
  font-weight: 500;
}

.dv-stage__legend span {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.dv-lg {
  display: inline-grid;
  place-items: center;
  width: 9px;
  height: 9px;
  border: 1.4px solid var(--ink);
  border-radius: 50%;
}

.dv-lg--data { background: #efb041; }
.dv-lg--insight { background: #9fd28f; }
.dv-lg--noise {
  width: 10px;
  height: 10px;
  border-radius: 2px;
  background: #e8834d;
}

/* ---------------- timeline ---------------- */

.dv-timeline {
  flex: none;
  margin-top: 11px;
  padding: 10px 14px 9px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  box-shadow: var(--card-shadow);
}

.dv-timeline__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.dv-timeline__count {
  color: var(--muted);
  font-size: 10.5px;
  font-weight: 600;
}

.dv-timeline__track {
  position: relative;
  margin-top: 7px;
}

.dv-timeline__rail {
  position: absolute;
  top: 12px;
  right: calc(100% / var(--n) / 2);
  left: calc(100% / var(--n) / 2);
  height: 1.3px;
  background: #b9b0a3;
}

.dv-timeline__rail span {
  position: absolute;
  inset: -1px auto -1px 0;
  background: var(--ink);
  transition: width 0.65s cubic-bezier(0.65, 0, 0.35, 1);
}

.dv-timeline__steps {
  position: relative;
  display: grid;
  grid-template-columns: repeat(var(--n), minmax(0, 1fr));
}

.dv-timeline__steps li {
  position: relative;
}

.dv-timeline__steps button {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 0 2px;
}

.dv-timeline__dot {
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border: 1.3px solid #5f584f;
  border-radius: 50%;
  background: var(--card);
  font-size: 11px;
  font-weight: 700;
  transition: background 0.3s, transform 0.3s;
}

.dv-timeline__dot svg {
  width: 12px;
  height: 12px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-timeline__steps button:hover .dv-timeline__dot {
  background: #fff;
  transform: translateY(-1px);
}

.dv-timeline__steps li.is-done .dv-timeline__dot {
  border-color: var(--ink-2);
  background: #e7efd9;
}

.dv-timeline__steps li.is-current .dv-timeline__dot {
  border: 1.5px solid var(--ink);
  background: var(--green);
  box-shadow: 1.5px 2.5px 0 var(--ink);
  transform: scale(1.06);
}

.dv-timeline__label {
  display: -webkit-box;
  overflow: hidden;
  min-height: 2.55em;
  margin-top: 5px;
  color: var(--muted);
  text-align: center;
  font-size: 10px;
  line-height: 1.28;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.dv-timeline__steps li.is-done .dv-timeline__label { color: var(--ink-2); }
.dv-timeline__steps li.is-current .dv-timeline__label { color: var(--ink); font-weight: 800; }

.dv-footnote {
  flex: none;
  margin: 7px 4px 0;
  color: var(--muted-2);
  font-size: 9.5px;
  line-height: 1.4;
}

.dv-eyebrow {
  color: var(--ink);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

/* ---------------- right rail ---------------- */

.dv-rail {
  display: flex;
  flex-direction: column;
  gap: 13px;
  min-height: 0;
  padding: 12px 14px 14px;
}

.dv-card {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--paper-2);
  box-shadow: var(--card-shadow);
}

.dv-guide {
  display: flex;
  flex: 1;
  flex-direction: column;
  min-height: 0;
  padding: 14px 15px 11px;
}

.dv-guide__meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px 12px;
}

.dv-guide__meta .dv-eyebrow {
  font-size: 11.5px;
}

.dv-chapter {
  display: inline-flex;
  align-items: center;
  height: 22px;
  padding: 0 10px;
  border: 1.3px solid var(--ink-2);
  border-radius: 11px;
  box-shadow: 0 1.5px 0 var(--ink-2);
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  white-space: nowrap;
}

.dv-chapter--sand { background: #f6e6c9; }
.dv-chapter--blue { background: #d6e5f6; }
.dv-chapter--green { background: var(--green); }
.dv-chapter--amber { background: #fbe5bd; }
.dv-chapter--violet { background: var(--violet); }
.dv-chapter--red { background: #f8d5cf; }

.dv-guide__content {
  flex: 1;
  min-height: 0;
  margin: 0 -7px;
  padding: 0 7px;
  overflow-y: auto;
  scrollbar-width: thin;
}

.dv-guide__title {
  margin: 13px 0 10px;
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -0.01em;
  line-height: 1.25;
}

.dv-guide__body p {
  margin-bottom: 10px;
  color: var(--ink-2);
  font-size: 12.4px;
  line-height: 1.65;
}

.dv-guide__body p:last-child {
  margin-bottom: 0;
}

.dv-guide__body :deep(b) {
  color: var(--ink);
}

.dv-guide__body :deep(.term) {
  background: linear-gradient(transparent 58%, rgba(178, 212, 145, 0.6) 58%);
  color: var(--ink);
  font-weight: 800;
}

.dv-callout {
  display: flex;
  gap: 10px;
  margin-top: 12px;
  padding: 10px 11px 11px;
  border: 1px solid var(--violet-tile-line);
  border-radius: 10px;
  background: var(--violet-tile);
}

.dv-callout__icon {
  display: grid;
  place-items: center;
  width: 27px;
  height: 27px;
  flex: none;
  border: 1.3px solid var(--ink-2);
  border-radius: 8px;
  background: #fbf7f1;
}

.dv-callout__icon svg {
  width: 15px;
  height: 15px;
  fill: none;
  stroke: var(--ink);
  stroke-width: 1.3;
  stroke-linejoin: round;
}

.dv-callout__title {
  margin-bottom: 3px;
  color: var(--muted);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.dv-callout p {
  color: var(--ink-2);
  font-size: 11.9px;
  line-height: 1.55;
}

.dv-callout p :deep(b),
.dv-callout p :deep(.term) {
  color: var(--ink);
}

.dv-guide__nav {
  display: flex;
  gap: 10px;
  margin-top: 13px;
}

.dv-btn-ghost {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  height: 38px;
  padding: 0 13px;
  border: 1.3px solid var(--ink-2);
  border-radius: 8px;
  background: #fbf7f1;
  box-shadow: 0 1.5px 0 var(--ink-2);
  font-size: 12px;
  font-weight: 700;
}

.dv-btn-ghost:disabled {
  opacity: 0.4;
  cursor: default;
}

.dv-btn-ghost:not(:disabled):active {
  transform: translate(1px, 1.5px);
  box-shadow: none;
}

.dv-btn-ghost svg,
.dv-btn-pop svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-btn-pop {
  border: 1.5px solid var(--ink);
  border-radius: 8px;
  background: var(--green);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45), var(--pop-shadow);
  font-weight: 800;
}

.dv-btn-pop:active {
  transform: translate(1px, 1.5px);
  box-shadow: none;
}

.dv-btn-next {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  min-width: 0;
  height: 38px;
  padding: 0 13px 0 14px;
  font-size: 11.5px;
  text-align: left;
}

.dv-btn-next__label {
  display: -webkit-box;
  overflow: hidden;
  line-height: 1.18;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.dv-guide__hint {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  margin-top: 9px;
  color: var(--muted-2);
  font-size: 9.5px;
}

.dv-guide__hint span {
  margin: 0 1px;
}

.dv-goals {
  flex: none;
  padding: 12px 15px 11px;
}

.dv-goals .dv-eyebrow {
  font-size: 11.5px;
}

.dv-goals ul {
  margin-top: 8px;
}

.dv-goals li {
  display: flex;
  align-items: flex-start;
  padding: 3.5px 0;
  color: var(--muted);
  font-size: 11.3px;
  line-height: 1.45;
  transition: color 0.3s;
}

.dv-goals li.is-hit {
  color: var(--ink);
}

.dv-check {
  display: grid;
  place-items: center;
  width: 16px;
  height: 16px;
  flex: none;
  margin-top: 1px;
  margin-right: 9px;
  border: 1.3px solid #8f877c;
  border-radius: 3px;
  background: #fbf7f1;
  color: transparent;
  transition: background 0.3s, border-color 0.3s, color 0.3s;
}

.dv-check svg {
  width: 11px;
  height: 11px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.dv-check.is-on {
  border-color: #1f3b1c;
  background: #a6d38b;
  color: #12240f;
}

/* ---------------- search palette ---------------- */

.dv-palette {
  position: fixed;
  inset: 0;
  z-index: 90;
  display: grid;
  place-items: start center;
  padding-top: min(10vh, 80px);
  background: rgba(58, 44, 28, 0.4);
  backdrop-filter: blur(2px) saturate(0.9);
}

.dv-palette__dialog {
  display: flex;
  flex-direction: column;
  width: min(640px, calc(100vw - 32px));
  max-height: min(640px, 76vh);
  overflow: hidden;
  border: 1.5px solid var(--ink);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 3px 4px 0 var(--ink), 0 30px 60px -28px rgba(60, 40, 20, 0.55);
}

.dv-palette__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 58px;
  flex: none;
  padding: 0 18px 0 19px;
  border-bottom: 1.3px solid var(--line-strong);
  background: linear-gradient(rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0));
}

.dv-palette__bar > svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: var(--ink-2);
  stroke-width: 1.4;
  stroke-linecap: round;
}

.dv-palette__input {
  flex: 1;
  min-width: 0;
  height: 100%;
  border: 0;
  outline: 0;
  background: transparent;
  color: var(--ink);
  font-size: 15px;
  font-weight: 600;
}

.dv-palette__input::placeholder {
  color: #9a9286;
  font-weight: 500;
}

.dv-palette__input::-webkit-search-cancel-button {
  display: none;
}

.dv-palette__esc {
  padding: 0 7px;
  height: 22px;
  border: 1px solid var(--line-strong);
  border-radius: 5px;
  background: var(--paper-2);
  color: var(--muted);
  font-size: 10px;
  font-weight: 700;
}

.dv-palette__list {
  flex: 1;
  min-height: 0;
  padding: 3px 9px 8px;
  overflow-y: auto;
}

.dv-palette__group {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 12px 11px 6px;
  color: var(--muted);
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.dv-palette__group span:last-child {
  letter-spacing: 0.02em;
  text-transform: none;
  color: var(--muted-2);
  font-weight: 600;
}

.dv-palette__item {
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 8px 10px;
  border: 1.3px solid transparent;
  border-radius: 10px;
  text-align: left;
}

.dv-palette__item:hover,
.dv-palette__item:focus-visible {
  border-color: var(--line-strong);
  background: rgba(244, 235, 224, 0.75);
  outline: 0;
}

.dv-palette__num {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border: 1.3px solid var(--ink-2);
  border-radius: 8px;
  background: #fbf7f1;
  font-size: 10px;
  font-weight: 800;
}

.dv-palette__main {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.dv-palette__title {
  overflow: hidden;
  color: var(--ink);
  font-size: 12.8px;
  font-weight: 800;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.dv-palette__meta {
  color: var(--muted);
  font-size: 10.5px;
  font-weight: 500;
}

.dv-palette__meta span {
  margin: 0 3px;
  color: var(--muted-2);
}

.dv-palette__chip {
  display: inline-flex;
  align-items: center;
  height: 20px;
  padding: 0 8px;
  border: 1.2px solid var(--ink-2);
  border-radius: 10px;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.05em;
}

.dv-palette__empty {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 32px 24px 38px;
  color: var(--muted);
  text-align: center;
  font-size: 11.5px;
}

.dv-palette__empty strong {
  color: var(--ink);
  font-size: 13px;
}

.dv-palette__foot {
  display: flex;
  align-items: center;
  gap: 16px;
  height: 40px;
  flex: none;
  padding: 0 17px;
  border-top: 1px solid var(--line);
  background: var(--paper-2);
  color: var(--muted);
  font-size: 10px;
}

.dv-palette__foot span {
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.dv-palette__count {
  margin-left: auto;
  font-weight: 600;
}

.dv-fade-enter-active,
.dv-fade-leave-active {
  transition: opacity 0.16s;
}

.dv-fade-enter-active .dv-palette__dialog,
.dv-fade-leave-active .dv-palette__dialog {
  transition: transform 0.22s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.dv-fade-enter-from,
.dv-fade-leave-to {
  opacity: 0;
}

.dv-fade-enter-from .dv-palette__dialog,
.dv-fade-leave-to .dv-palette__dialog {
  transform: translateY(-8px) scale(0.99);
}

/* ---------------- drawer ---------------- */

.dv-drawer-backdrop {
  display: none;
}

/* ---------------- responsive ---------------- */

@media (max-width: 1340px) {
  .dv-search {
    width: 250px;
  }
  .dv-credit__text {
    display: none;
  }
  .dv-credit {
    margin-left: 8px;
  }
}

@media (max-width: 1180px) {
  .dv-body {
    grid-template-columns: minmax(0, 1fr) 338px;
  }
  .dv-menu-btn {
    display: grid;
  }
  .dv-sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 55;
    width: min(318px, 88vw);
    padding: 18px 12px 14px 18px;
    border-right: 1.5px solid var(--ink);
    background: var(--paper);
    box-shadow: 0 0 60px -18px rgba(80, 60, 35, 0.65);
    transform: translateX(-104%);
    visibility: hidden;
    transition: transform 0.32s cubic-bezier(0.2, 0.7, 0.2, 1), visibility 0s linear 0.32s;
  }
  .dv-sidebar.is-open {
    transform: none;
    visibility: visible;
    transition: transform 0.32s cubic-bezier(0.2, 0.7, 0.2, 1);
  }
  .dv-drawer-close {
    display: grid;
  }
  .dv-drawer-backdrop {
    position: fixed;
    inset: 0;
    z-index: 50;
    display: block;
    background: rgba(58, 44, 28, 0.38);
    backdrop-filter: blur(1.5px);
  }
  .dv-nav {
    display: none;
  }
  .dv-search {
    width: min(330px, 32vw);
  }
  .dv-brand {
    margin-right: 12px;
  }
  .dv-stage__hud {
    right: 12px;
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: none;
  }
  .dv-stage__hud::-webkit-scrollbar {
    display: none;
  }
  .dv-stage__tools {
    top: auto;
    right: 10px;
    bottom: 8px;
  }
  .dv-tool {
    width: 32px;
    justify-content: center;
    padding: 0;
  }
  .dv-tool span {
    display: none;
  }
  .dv-stage__canvas {
    bottom: 46px;
  }
}

@media (max-width: 1120px) {
  .dv-timeline__label {
    display: none;
  }
  .dv-timeline__steps {
    padding-bottom: 20px;
  }
  .dv-timeline__steps li.is-current .dv-timeline__label {
    position: absolute;
    top: 32px;
    left: 50%;
    display: block;
    width: max-content;
    max-width: 130px;
    padding: 2px 6px;
    border-radius: 5px;
    background: var(--green-tile);
    transform: translateX(-50%);
    font-size: 9px;
  }
}

@media (max-width: 980px) {
  .dv-root {
    position: relative;
    height: auto;
    min-height: 100dvh;
    grid-template-rows: 54px auto;
    overflow: visible;
  }
  .dv-root::after {
    position: absolute;
  }
  .dv-body {
    display: block;
    padding-bottom: 18px;
  }
  .dv-sheet {
    min-height: auto;
    margin: 10px 10px 0;
    padding: 0 10px 11px;
  }
  .dv-lesson-head {
    padding: 14px 4px 0;
  }
  .dv-lesson-head__row {
    flex-wrap: wrap;
    align-items: flex-start;
    gap: 9px 14px;
  }
  .dv-title {
    white-space: normal;
    font-size: clamp(23px, 6vw, 30px);
  }
  .dv-subtitle {
    white-space: normal;
  }
  .dv-tags {
    flex-wrap: wrap;
    gap: 6px;
  }
  .dv-stage {
    flex: none;
    height: clamp(440px, 65vw, 640px);
    min-height: 0;
  }
  .dv-stage__hud {
    right: 10px;
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: none;
  }
  .dv-stage__hud::-webkit-scrollbar {
    display: none;
  }
  .dv-chip {
    flex: none;
    min-width: 0;
    padding: 5px 9px 6px 10px;
  }
  .dv-chip__label {
    font-size: 8px;
  }
  .dv-chip__value {
    font-size: 12.5px;
  }
  .dv-stage__tools {
    top: auto;
    right: 8px;
    bottom: 8px;
  }
  .dv-tool span {
    display: none;
  }
  .dv-tool {
    width: 32px;
    justify-content: center;
    padding: 0;
  }
  .dv-stage__canvas {
    inset: 60px 6px 46px;
  }
  .dv-stage__legend {
    bottom: 14px;
    left: 10px;
    gap: 12px;
    font-size: 9.5px;
  }
  .dv-timeline {
    padding: 9px 10px 8px;
  }
  .dv-timeline__label {
    display: none;
  }
  .dv-timeline__label {
    min-height: 0;
  }
  .dv-timeline__steps li.is-current .dv-timeline__label {
    position: absolute;
    top: 32px;
    left: 50%;
    display: block;
    width: max-content;
    max-width: 130px;
    min-height: 0;
    padding: 2px 6px;
    border-radius: 5px;
    background: var(--green-tile);
    transform: translateX(-50%);
    font-size: 9px;
  }
  .dv-timeline__steps {
    padding-bottom: 22px;
  }
  .dv-footnote {
    padding: 0 4px;
  }
  .dv-rail {
    display: block;
    padding: 10px 10px 0;
  }
  .dv-guide {
    display: block;
    padding: 14px 15px 13px;
  }
  .dv-guide__content {
    overflow: visible;
  }
  .dv-guide__title {
    font-size: 21px;
  }
  .dv-guide__body p {
    font-size: 13px;
  }
  .dv-goals {
    margin-top: 10px;
  }
  .dv-guide__nav {
    padding-top: 10px;
  }
}

@media (max-width: 720px) {
  .dv-topbar {
    padding: 0 10px;
  }
  .dv-brand__sub {
    display: none;
  }
  .dv-brand__name {
    font-size: 17px;
  }
  .dv-logo {
    width: 30px;
    height: 30px;
  }
  .dv-search {
    width: 36px;
    margin-left: auto;
    justify-content: center;
    padding: 0;
  }
  .dv-search__hint,
  .dv-search kbd {
    display: none;
  }
  .dv-credit {
    display: none;
  }
  .dv-stage {
    height: clamp(440px, 118vw, 540px);
  }
  .dv-stage__hud {
    gap: 5px;
  }
  .dv-chip {
    padding: 4px 8px 5px 9px;
  }
  .dv-chip__label {
    font-size: 7.5px;
  }
  .dv-chip__label svg {
    display: none;
  }
  .dv-chip__value {
    font-size: 11.5px;
  }
  .dv-stage__canvas {
    inset: 58px 2px 44px;
  }
  .dv-timeline__label {
    display: none !important;
  }
  .dv-timeline__steps {
    padding-bottom: 2px;
  }
  .dv-timeline__dot {
    width: 22px;
    height: 22px;
    font-size: 9.5px;
  }
  .dv-timeline__rail {
    top: 10px;
  }
  .dv-guide__nav {
    gap: 7px;
  }
  .dv-btn-ghost {
    padding: 0 10px;
    font-size: 11px;
  }
  .dv-btn-next {
    padding: 0 10px;
    font-size: 10.5px;
  }
  .dv-guide__hint {
    display: none;
  }
  .dv-palette {
    padding-top: 10px;
  }
  .dv-palette__dialog {
    width: calc(100vw - 16px);
    max-height: calc(100dvh - 20px);
  }
  .dv-palette__item {
    grid-template-columns: 30px minmax(0, 1fr);
  }
  .dv-palette__chip {
    display: none;
  }
}

@media (max-width: 380px) {
  .dv-stage__legend {
    display: none;
  }
}

@media (max-height: 760px) and (min-width: 981px) {
  .dv-goals {
    display: none;
  }
  .dv-stage {
    min-height: 310px;
  }
  .dv-lesson-head {
    padding-top: 13px;
  }
  .dv-title {
    font-size: 27px;
  }
  .dv-timeline__label {
    min-height: 1.3em;
    -webkit-line-clamp: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dv-root *,
  .dv-root *::before,
  .dv-root *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}

/* identity credit */
.dv-credit__x {
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: -0.05em;
  line-height: 1;
}

@media (min-width: 860px) {
  .dv-credit__text {
    display: flex !important;
  }
}

@media (max-width: 800px) {
  .dv-credit {
    display: flex;
    margin-left: 8px;
  }
  .dv-credit__text {
    display: none;
  }
}
</style>
