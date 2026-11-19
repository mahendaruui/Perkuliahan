<template>
  <div class="dv-root" :class="{ 'is-drawer': drawerOpen }">
    <header class="dv-topbar">
      <button class="dv-menu-btn" type="button" aria-label="Buka daftar langkah" :aria-expanded="drawerOpen" @click="drawerOpen = true">
        <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5.5h14M3 10h14M3 14.5h9" /></svg>
      </button>

      <a class="dv-brand" :href="withBase('/pemrograman-oop-php/canvas')" aria-label="Kanvas OOP PHP — mulai dari langkah pertama" @click.prevent="goTo(0)">
        <svg class="dv-logo" viewBox="0 0 34 34" aria-hidden="true">
          <rect x="2.4" y="5.5" width="29.2" height="23" rx="6" fill="#fbf7f1" stroke="#1d1b18" stroke-width="1.8" />
          <path d="M17 7.2 27 13l-10 5.8L7 13Z" fill="#b2d491" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
          <path d="M7 13v8l10 5.8V18.8Z" fill="#e7ddf5" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
          <path d="M27 13v8l-10 5.8V18.8Z" fill="#fcdcbd" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
        </svg>
        <span class="dv-brand__name">Kanvas <span>OOP</span></span>
        <span class="dv-brand__sub">IFR214</span>
      </a>

      <nav class="dv-nav" aria-label="Navigasi kanvas">
        <button class="dv-nav__item is-active" type="button">Belajar</button>
        <a class="dv-nav__item" :href="withBase('/pemrograman-oop-php/')">Modul</a>
        <a class="dv-nav__item" :href="withBase('/presentasi/pertemuan-1-php')">Slide</a>
      </nav>

      <button class="dv-search" type="button" aria-label="Cari langkah dan konsep" :aria-expanded="searchOpen" @click="openSearch">
        <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
        <span class="dv-search__hint">Cari langkah &amp; konsep…</span>
        <kbd>⌘K</kbd>
      </button>

      <a class="dv-credit" :href="withBase('/pemrograman-oop-php/')">
        <span class="dv-credit__x" aria-hidden="true">
          <svg viewBox="0 0 18 18"><path d="M4 12.5 9 4l5 8.5M6.4 10h5.2" /></svg>
        </span>
        <span class="dv-credit__text"><small>kembali ke</small><b>Modul OOP PHP</b></span>
      </a>
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
          <div class="dv-crumb">OOP PHP <span>/</span> Kanvas interaktif</div>
          <div class="dv-lesson-head__row">
            <div class="dv-title-wrap">
              <h1 class="dv-title">Dasar OOP PHP</h1>
              <p class="dv-subtitle">Class, object, dan empat pilar — dari blueprint sampai perilaku.</p>
            </div>
            <div class="dv-tags">
              <span class="dv-tag dv-tag--sand">
                <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.6" /><path d="M8 4.8V8l2.2 1.4" /></svg>
                15 mnt
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
            <span><i class="dv-lg dv-lg--data"></i> state</span>
            <span><i class="dv-lg dv-lg--insight"></i> method</span>
            <span><i class="dv-lg dv-lg--noise"></i> object</span>
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

        <p class="dv-footnote">Materi dasar OOP PHP 8+. Kode disederhanakan untuk memperjelas konsep — bukan potongan produksi lengkap.</p>
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
              <span>Coba “class”, “constructor”, atau “inheritance”.</span>
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
  panelTitle: string
  panelMetric: string
  file: string
  classCount: string
  objectCount: string
  methodCount: string
  pillarCount: number
  code: string[]
}

interface Goal {
  text: string
  at: number
}

const steps: Step[] = [
  {
    id: 'procedural',
    short: 'Fondasi',
    title: 'Data dan perilaku, akhirnya bersatu',
    phase: 'FONDASI',
    tone: 'sand',
    body: `<p>Di pemrograman prosedural, <b>data</b> dan <b>fungsi</b> hidup terpisah. Data mengalir bebas, dan siapa pun bisa mengubahnya.</p><p><span class="term">OOP</span> membungkus state dan perilaku menjadi satu unit: <b>object</b>.</p>`,
    idea: `Object bukan sekadar kumpulan variabel — ia membawa data dan cara mengolahnya sekaligus.`,
    panelTitle: 'Prosedural vs OOP',
    panelMetric: 'data + perilaku',
    file: 'prosedural.php',
    classCount: '0',
    objectCount: '0',
    methodCount: '0',
    pillarCount: 0,
    code: [
      '$luas = hitungLuas(10, 5);',
      '$bangun = new PersegiPanjang(10, 5);',
      'echo $bangun->luas();',
      '// 50',
    ],
  },
  {
    id: 'class',
    short: 'Class',
    title: 'Cetak biru, bukan rumah',
    phase: 'BLUEPRINT',
    tone: 'blue',
    body: `<p><span class="term">Class</span> adalah cetak biru. Di dalamnya kita mendefinisikan <b>property</b> (state) dan <b>method</b> (perilaku).</p><p>Class belum menjadi object sampai kita membuat instance dengan <code>new</code>.</p>`,
    idea: `Class adalah cetak biru; object adalah bangunan yang benar-benar ada di memori.`,
    panelTitle: 'Blueprint class',
    panelMetric: 'class Mahasiswa',
    file: 'Mahasiswa.php',
    classCount: '1',
    objectCount: '0',
    methodCount: '1',
    pillarCount: 0,
    code: [
      'class Mahasiswa {',
      '  public string $nama;',
      '  public function sapa(): string { ... }',
      '}',
    ],
  },
  {
    id: 'object',
    short: 'Object',
    title: 'Satu blueprint, banyak wujud',
    phase: 'OBJEK',
    tone: 'amber',
    body: `<p><span class="term">Object</span> adalah instance nyata dari class. Setiap object memiliki state sendiri, meskipun berasal dari blueprint yang sama.</p><p>Satu class bisa melahirkan banyak object dengan data berbeda.</p>`,
    idea: `Blueprint-nya satu, hasilnya bisa banyak — masing-masing membawa state sendiri.`,
    panelTitle: 'Instansiasi',
    panelMetric: 'new Mahasiswa()',
    file: 'instansiasi.php',
    classCount: '1',
    objectCount: '2',
    methodCount: '1',
    pillarCount: 0,
    code: [
      '$mhs1 = new Mahasiswa();',
      "$mhs1->nama = 'Ahmad';",
      '$mhs2 = new Mahasiswa();',
      "$mhs2->nama = 'Rina';",
    ],
  },
  {
    id: 'this',
    short: '$this',
    title: 'State, perilaku, dan “object saya”',
    phase: 'PERILAKU',
    tone: 'green',
    body: `<p><b>Property</b> menyimpan state; <b>method</b> mengolah state itu. Di dalam method, <span class="term">$this</span> merujuk ke object yang sedang aktif.</p><p>Operator <code>-&gt;</code> dipakai dari luar untuk mengakses property atau memanggil method.</p>`,
    idea: `$this adalah “object saya sendiri” saat sebuah method dijalankan.`,
    panelTitle: 'Anatomi object',
    panelMetric: '$this → object aktif',
    file: 'Mahasiswa.php',
    classCount: '1',
    objectCount: '2',
    methodCount: '2',
    pillarCount: 0,
    code: [
      "public string $nama = 'Ahmad';",
      'public function sapa(): string {',
      '  return "Halo, {$this->nama}";',
      '}',
    ],
  },
  {
    id: 'constructor',
    short: 'Constructor',
    title: 'Lahir dengan state yang valid',
    phase: 'SIKLUS',
    tone: 'violet',
    body: `<p><b>Constructor</b> <code>__construct()</code> dijalankan otomatis saat <code>new</code>. Gunakan untuk mengisi state awal dan menjaga object valid sejak lahir.</p><p>Dengan constructor promotion, property bisa dideklarasikan langsung di parameter.</p>`,
    idea: `Constructor adalah gerbang masuk object; jangan biarkan object lahir setengah jadi.`,
    panelTitle: 'Constructor',
    panelMetric: '__construct()',
    file: 'Mahasiswa.php',
    classCount: '1',
    objectCount: '2',
    methodCount: '3',
    pillarCount: 0,
    code: [
      'public function __construct(',
      '  public string $nama,',
      '  public float $ipk = 0.0',
      ') {}',
    ],
  },
  {
    id: 'encapsulation',
    short: 'Enkapsulasi',
    title: 'Sembunyikan state, buka perilaku',
    phase: 'PILAR 1',
    tone: 'green',
    body: `<p><span class="term">Encapsulation</span> menyembunyikan state internal dengan <code>private</code>, lalu membuka method publik yang tervalidasi.</p><p>Dunia luar memakai perilaku object, bukan mengubah datanya secara sembarangan.</p>`,
    idea: `Jangan izinkan saldo diubah langsung; sediakan setor() dan tarik() yang memeriksa aturan.`,
    panelTitle: 'Encapsulation',
    panelMetric: 'private state · public API',
    file: 'Rekening.php',
    classCount: '1',
    objectCount: '2',
    methodCount: '4',
    pillarCount: 1,
    code: [
      'private float $saldo = 0;',
      'public function setor(float $n): void {',
      '  $this->saldo += $n;',
      '}',
    ],
  },
  {
    id: 'inheritance',
    short: 'Warisan',
    title: 'Mewarisi yang sama, menambah yang khas',
    phase: 'PILAR 2',
    tone: 'blue',
    body: `<p><span class="term">Inheritance</span> membuat child class mewarisi property dan method parent melalui <code>extends</code>.</p><p>Gunakan hanya untuk relasi <b>is-a</b>: Mahasiswa adalah SivitasAkademika.</p>`,
    idea: `Warisi yang sama, tambahkan yang khas. Jangan mewarisi hanya karena ingin memakai ulang kode.`,
    panelTitle: 'Inheritance',
    panelMetric: 'extends · is-a',
    file: 'Mahasiswa.php',
    classCount: '3',
    objectCount: '2',
    methodCount: '5',
    pillarCount: 2,
    code: [
      'class Mahasiswa extends SivitasAkademika {',
      '  public function __construct(',
      '    string $nama, private string $nim',
      '  ) { parent::__construct($nama); }',
    ],
  },
  {
    id: 'polymorphism',
    short: 'Polimorfisme',
    title: 'Satu pesan, banyak jawaban',
    phase: 'PILAR 3',
    tone: 'amber',
    body: `<p><span class="term">Polymorphism</span> membuat object berbeda merespons method yang sama dengan caranya masing-masing.</p><p>Pemanggil cukup tahu kontraknya; detail perilaku ditentukan oleh object yang menerima pesan.</p>`,
    idea: `Satu perintah bersuara(), banyak hasil — tergantung object yang menerimanya.`,
    panelTitle: 'Polymorphism',
    panelMetric: 'satu method · banyak bentuk',
    file: 'Hewan.php',
    classCount: '4',
    objectCount: '3',
    methodCount: '6',
    pillarCount: 3,
    code: [
      'foreach ($hewan as $h) {',
      '  echo $h->bersuara();',
      '}',
      '// Meong · Guk · Kwek',
    ],
  },
  {
    id: 'abstraction',
    short: 'Abstraksi',
    title: 'Kontrak dulu, detail kemudian',
    phase: 'PILAR 4',
    tone: 'violet',
    body: `<p><span class="term">Abstraction</span> menetapkan kontrak tanpa memaksa detail implementasi. Interface dan abstract class adalah alatnya.</p><p>Class konkret wajib memenuhi kontrak tersebut dengan <code>implements</code> atau <code>extends</code>.</p>`,
    idea: `Abstraction menyembunyikan “bagaimana”, tetapi menegaskan “apa” yang harus bisa dilakukan.`,
    panelTitle: 'Abstraction',
    panelMetric: 'interface · kontrak',
    file: 'Pembayaran.php',
    classCount: '4',
    objectCount: '3',
    methodCount: '6',
    pillarCount: 4,
    code: [
      'interface Pembayaran {',
      '  public function bayar(float $n): void;',
      '}',
      'class QRIS implements Pembayaran { ... }',
    ],
  },
  {
    id: 'recap',
    short: 'Rekap',
    title: 'Empat pilar, satu object',
    phase: 'REKAP',
    tone: 'green',
    body: `<p>Class membentuk object; constructor menjaganya lahir valid; encapsulation menjaga state; inheritance berbagi perilaku; polymorphism memberi fleksibilitas; abstraction menetapkan kontrak.</p><p>Empat pilar bukan empat topik terpisah — mereka satu cara berpikir tentang object.</p>`,
    idea: `Mulai dari object yang kecil dan jelas; pilar-pilar akan mengikuti desainnya.`,
    panelTitle: 'Object utuh',
    panelMetric: '4 pilar · 1 object',
    file: 'rekap.php',
    classCount: '4',
    objectCount: '3',
    methodCount: '6',
    pillarCount: 4,
    code: [
      "$mhs = new Mahasiswa('Ahmad', '240101');",
      '$mhs->setorIpk(3.85);',
      'echo $mhs->sapa();',
      '// Halo, Ahmad',
    ],
  },
]

const goals: Goal[] = [
  { text: 'Membedakan gaya prosedural dan OOP', at: 1 },
  { text: 'Membedakan class dan object', at: 3 },
  { text: 'Memakai new, ->, dan $this', at: 5 },
  { text: 'Menerapkan encapsulation & inheritance', at: 7 },
  { text: 'Memahami polymorphism & abstraction', at: 9 },
]

const moduleDefs = [
  { id: 'm1', title: '01. Object & perilaku', color: 'sand', items: [0, 1, 2, 3] },
  { id: 'm2', title: '02. Siklus object', color: 'violet', items: [4] },
  { id: 'm3', title: '03. Empat pilar', color: 'green', items: [5, 6, 7, 8] },
  { id: 'm4', title: '04. Rekap', color: 'amber', items: [9] },
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
const openModules = ref<Record<string, boolean>>({ m1: true, m2: true, m3: true })

const step = computed(() => steps[current.value])
const progressPct = computed(() => Math.round(((current.value + 1) / steps.length) * 100))
const timelinePct = computed(() => (current.value / (steps.length - 1)) * 100)
const remainingLabel = computed(() => (current.value === steps.length - 1 ? 'selesai' : `${steps.length - current.value - 1} lagi`))
const canvasLabel = computed(() => `Langkah ${current.value + 1}: ${step.value.title}. ${step.value.panelTitle}, ${step.value.panelMetric}.`)

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
      label: 'CLASS',
      value: s.classCount,
      level: s.classCount === '0' ? '' : 'good',
      path: 'M8 2.2 13 5v6l-5 2.8L3 11V5z M3 5l5 2.8L13 5M8 7.8v6',
    },
    {
      label: 'OBJECT',
      value: s.objectCount,
      level: s.objectCount === '0' ? '' : 'good',
      path: 'M4 4h8v8H4z M4 8h8M8 4v8',
    },
    {
      label: 'METHOD',
      value: s.methodCount,
      level: s.methodCount === '0' ? '' : 'good',
      path: 'M4 4.5h8M4 8h8M4 11.5h5',
    },
    {
      label: 'PILAR OOP',
      value: `${s.pillarCount}/4`,
      level: s.pillarCount === 4 ? 'good' : s.pillarCount > 0 ? 'warn' : '',
      path: 'M8 2.2 13 5v6l-5 2.8L3 11V5z',
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
  ink: '#1d1b18',
  ink2: '#34302b',
  muted: '#6f6961',
  muted2: '#8b847a',
  line: '#ddd3c5',
  lineSoft: '#e6ddd0',
  lineStrong: '#c6bbac',
  paper: '#f4ebe0',
  paper2: '#f7efe4',
  sheet: '#f9f2e8',
  card: '#f8f0e6',
  cream: '#fbf7f1',
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

const clamp = (v: number, min = 0, max = 1) => Math.max(min, Math.min(max, v))
const easeOut = (v: number) => 1 - Math.pow(1 - clamp(v), 3)
const lerp = (a: number, b: number, t: number) => a + (b - a) * t

function rr(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  if (!Number.isFinite(w) || !Number.isFinite(h) || w <= 0 || h <= 0) {
    c.beginPath()
    return
  }
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
  if (!Number.isFinite(w) || !Number.isFinite(h) || w <= 0 || h <= 0) return
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
  fade.addColorStop(0, 'rgba(250, 243, 233, 0.98)')
  fade.addColorStop(0.35, 'rgba(250, 243, 233, 0.66)')
  fade.addColorStop(1, 'rgba(250, 243, 233, 0)')
  c.fillStyle = fade
  c.fillRect(0, 0, w, h)
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

function drawBackdrop(c: CanvasRenderingContext2D, t: number) {
  const glow = c.createRadialGradient(625, 270, 30, 625, 270, 520)
  glow.addColorStop(0, 'rgba(255, 253, 248, 0.72)')
  glow.addColorStop(0.55, 'rgba(255, 253, 248, 0.24)')
  glow.addColorStop(1, 'rgba(255, 253, 248, 0)')
  c.fillStyle = glow
  c.fillRect(0, 0, DW, DH)

  drawPerspectiveFloor(c, DW, DH, 0.3, 20, 0.085)

  const dots = [
    [82, 130, C.amber],
    [932, 318, C.violet2],
    [900, 86, C.green2],
    [110, 330, C.rust],
    [675, 515, C.green2],
  ] as const
  dots.forEach(([x, y, color], i) => {
    c.globalAlpha = 0.7 + Math.sin(t * 1.2 + i) * 0.2
    c.beginPath()
    c.arc(x, y, 3.2, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.globalAlpha = 1
  })
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

function platformLabel(stepIndex: number) {
  if (stepIndex === 5) return 'class Rekening'
  if (stepIndex === 7) return 'class Hewan'
  if (stepIndex === 8) return 'interface Pembayaran'
  return 'class Mahasiswa'
}

function drawClassPlatform(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const cx = 204
  const cy = 437 + Math.sin(t * 0.8) * 1.4
  const hw = 136
  const hh = 64
  const thickness = 19

  c.save()
  c.globalAlpha = 0.12
  c.fillStyle = C.ink
  c.beginPath()
  c.ellipse(cx, cy + hh + 28, hw * 0.92, 24, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()

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

  diamond(c, cx, cy, hw, hh)
  c.fillStyle = C.cream
  c.fill()
  c.lineWidth = 2.2
  c.strokeStyle = C.ink
  c.stroke()

  diamond(c, cx, cy - 3, hw - 12, hh - 6)
  c.fillStyle = C.white
  c.fill()
  c.lineWidth = 1
  c.strokeStyle = C.lineStrong
  c.stroke()

  // A small 3D “class cube” sitting on the platform.
  const cubeX = cx
  const cubeY = cy - 27
  const cube = 30
  c.save()
  c.translate(cubeX, cubeY)
  c.beginPath()
  c.moveTo(0, -cube / 2)
  c.lineTo(cube, 0)
  c.lineTo(0, cube / 2)
  c.lineTo(-cube, 0)
  c.closePath()
  c.fillStyle = C.green2
  c.fill()
  c.strokeStyle = C.ink
  c.lineWidth = 1.4
  c.stroke()
  c.beginPath()
  c.moveTo(-cube, 0)
  c.lineTo(0, cube / 2)
  c.lineTo(0, cube / 2 + 17)
  c.lineTo(-cube, 17)
  c.closePath()
  c.fillStyle = '#d9cdbd'
  c.fill()
  c.stroke()
  c.beginPath()
  c.moveTo(cube, 0)
  c.lineTo(0, cube / 2)
  c.lineTo(0, cube / 2 + 17)
  c.lineTo(cube, 17)
  c.closePath()
  c.fillStyle = '#e6dbcf'
  c.fill()
  c.stroke()
  c.restore()

  // Floating blueprint sheet.
  c.save()
  c.translate(103, 349)
  c.rotate(-0.09)
  fillRR(c, 8, -6, 128, 79, 5, '#e6ddd0', 'rgba(29,27,24,.45)', 1)
  fillRR(c, 2, 0, 128, 79, 5, C.cream, C.ink, 1.4)
  txt(c, platformLabel(stepIndex), 12, 17, 8.6, 800, C.ink)
  c.strokeStyle = 'rgba(29,27,24,.28)'
  c.lineWidth = 1
  ;[0, 1, 2].forEach((i) => {
    c.beginPath()
    c.moveTo(12, 29 + i * 11)
    c.lineTo(i === 1 ? 94 : 116, 29 + i * 11)
    c.stroke()
  })
  fillRR(c, 92, 8, 28, 12, 4, C.violet, C.ink, 0.9, 0)
  txt(c, 'PHP', 106, 17, 6.4, 800, C.ink, 'center')
  c.restore()

  pill(c, platformLabel(stepIndex), 84, 519, { size: 11.5, h: 30, dot: C.amber })
}

function bezierPoint(p0: number[], p1: number[], p2: number[], p3: number[], t: number) {
  const mt = 1 - t
  const a = mt * mt * mt
  const b = 3 * mt * mt * t
  const c = 3 * mt * t * t
  const d = t * t * t
  return [a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]]
}

function drawFlow(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const p0 = [330, 419]
  const p1 = [365, 411]
  const p2 = [344, 353]
  const p3 = [358, 342]

  c.save()
  c.beginPath()
  c.moveTo(p0[0], p0[1])
  c.bezierCurveTo(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
  c.strokeStyle = stepIndex === 0 ? 'rgba(111,105,97,.25)' : 'rgba(111,105,97,.65)'
  c.lineWidth = 1.7
  c.setLineDash([5, 5])
  c.stroke()
  c.setLineDash([])
  const angle = Math.atan2(p3[1] - p2[1], p3[0] - p2[0])
  arrowHead(c, p3[0], p3[1], angle, 5.5)
  c.restore()

  if (stepIndex === 0) return

  const tokens = stepIndex >= 2 ? ['A', 'R'] : ['C']
  tokens.forEach((letter, i) => {
    const raw = (t * 0.32 + i / tokens.length) % 1
    const progress = raw < 0.5 ? 2 * raw * raw : 1 - Math.pow(-2 * raw + 2, 2) / 2
    const q = bezierPoint(p0, p1, p2, p3, progress)
    const alpha = Math.sin(progress * Math.PI) * 0.95
    c.save()
    c.globalAlpha = Math.max(0, alpha)
    fillRR(c, q[0] - 7, q[1] - 7, 14, 14, 4, i === 0 ? C.green2 : C.amber, C.ink, 1.3, 0)
    txt(c, letter, q[0], q[1] + 2.6, 8, 800, C.ink, 'center')
    c.restore()
  })

  if (stepIndex >= 2) {
    c.save()
    c.globalAlpha = 0.85
    fillRR(c, 347, 371, 27, 16, 8, C.cream, C.ink, 1, 0)
    txt(c, 'new', 360.5, 382, 7.8, 800, C.ink, 'center')
    c.restore()
  }
}

function drawPilarPill(c: CanvasRenderingContext2D, t: number, stepIndex: number, x = 650, y = 52, w = 250, h = 38) {
  fillRR(c, x + 2, y + 3, w, h, h / 2, C.ink)
  fillRR(c, x, y, w, h, h / 2, C.cream, C.ink, 1.6)

  fillRR(c, x + 7, y + 7, 23, 23, 7, stepIndex === steps.length - 1 ? C.green2 : C.violet, C.ink, 1.2, 0)
  c.save()
  c.translate(x + 18.5, y + 18.5)
  c.strokeStyle = C.ink
  c.lineWidth = 1.3
  c.beginPath()
  c.moveTo(0, -7)
  c.lineTo(7, -3.5)
  c.lineTo(7, 3.5)
  c.lineTo(0, 7)
  c.lineTo(-7, 3.5)
  c.lineTo(-7, -3.5)
  c.closePath()
  c.stroke()
  c.beginPath()
  c.moveTo(-7, -3.5)
  c.lineTo(0, 0)
  c.lineTo(7, -3.5)
  c.moveTo(0, 0)
  c.lineTo(0, 7)
  c.stroke()
  c.restore()

  txt(c, 'PILAR OOP', x + 39, y + 23, 9, 800, C.muted)
  const count = steps[stepIndex].pillarCount
  const segX = x + 110
  for (let i = 0; i < 4; i++) {
    fillRR(c, segX + i * 24, y + 15, 18, 8, 4, i < count ? C.green2 : C.lineSoft, 'rgba(29,27,24,.35)', 0.8, 0)
  }
  txt(c, `${count}/4`, x + w - 15, y + 24, 11.2, 800, count === 4 ? C.greenDark : C.ink, 'right')

  if (stepIndex === steps.length - 1) {
    rr(c, x - 3, y - 3, w + 6, h + 6, (h + 6) / 2)
    c.strokeStyle = `rgba(127,194,120,${0.32 + Math.sin(t * 2.2) * 0.06})`
    c.lineWidth = 2
    c.stroke()
  }
}

function drawMiniCard(
  c: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  title: string,
  rows: string[],
  opts: { fill?: string; accent?: string; titleColor?: string; rowSize?: number; shadow?: boolean } = {},
) {
  if (opts.shadow !== false) fillRR(c, x + 2.4, y + 3.4, w, h, 7, C.ink)
  fillRR(c, x, y, w, h, 7, opts.fill ?? C.cream, C.ink, 1.3)
  if (opts.accent) {
    fillRR(c, x + 5, y + 5, 3, h - 10, 1.5, opts.accent, undefined, 0)
  }
  txt(c, title, x + 11, y + 15, 10.2, 800, opts.titleColor ?? C.ink)
  const rowSize = opts.rowSize ?? 9
  rows.forEach((row, i) => {
    const ry = y + 26 + i * (rowSize + 2.5)
    if (ry > y + h - 5) return
    c.beginPath()
    c.arc(x + 11, ry - 2.2, 1.7, 0, Math.PI * 2)
    c.fillStyle = opts.accent ?? C.green3
    c.fill()
    txt(c, row, x + 17, ry, rowSize, 500, C.ink2)
  })
}

function drawArrow(
  c: CanvasRenderingContext2D,
  x1: number,
  y1: number,
  x2: number,
  y2: number,
  label?: string,
  dashed = false,
  color = C.ink,
) {
  c.save()
  c.strokeStyle = color
  c.lineWidth = 1.3
  if (dashed) c.setLineDash([3, 4])
  c.beginPath()
  c.moveTo(x1, y1)
  c.lineTo(x2, y2)
  c.stroke()
  c.setLineDash([])
  const angle = Math.atan2(y2 - y1, x2 - x1)
  arrowHead(c, x2, y2, angle, 4.5)
  if (label) {
    const mx = (x1 + x2) / 2
    const my = (y1 + y2) / 2
    font(c, 7.4, 800)
    const tw = c.measureText(label).width
    fillRR(c, mx - tw / 2 - 4, my - 8, tw + 8, 13, 6, C.cream, C.ink, 0.9, 0)
    txt(c, label, mx, my + 2, 7.4, 800, C.ink, 'center')
  }
  c.restore()
}

function drawTag(c: CanvasRenderingContext2D, text: string, x: number, y: number, fill = C.cream) {
  font(c, 8, 800)
  const w = c.measureText(text).width + 12
  fillRR(c, x, y, w, 16, 8, fill, C.ink, 0.9, 0)
  txt(c, text, x + 6, y + 11, 8, 800, C.ink)
  return w
}

function drawCodeLine(c: CanvasRenderingContext2D, line: string, x: number, y: number, maxX: number) {
  const pattern = /(\/\/.*$)|('(?:[^'\\]|\\.)*')|("(?:[^"\\]|\\.)*")|(\$[A-Za-z_]\w*)|(\b(?:class|public|private|protected|function|new|extends|implements|interface|return|echo|foreach|as|void|string|float|int|bool|use)\b)|(\b\d+(?:\.\d+)?\b)|(\s+)|([^\s]+)/g
  const tokens = line.match(pattern) ?? [line]
  let cx = x
  for (const token of tokens) {
    let color = '#efe6d6'
    let weight: number | string = 500
    if (token.startsWith('//')) color = '#8b847a'
    else if (token.startsWith("'") || token.startsWith('"')) color = '#a6d38b'
    else if (token.startsWith('$')) color = '#fbe5bd'
    else if (/^(class|public|private|protected|function|new|extends|implements|interface|return|echo|foreach|as|void|string|float|int|bool|use)$/.test(token)) {
      color = '#c9b6f0'
      weight = 700
    } else if (/^\d+(\.\d+)?$/.test(token)) color = '#efb041'
    font(c, compactScene ? 9.4 : 11, weight)
    const tw = c.measureText(token).width
    if (cx + tw > maxX) break
    c.fillStyle = color
    c.textAlign = 'left'
    c.textBaseline = 'alphabetic'
    c.fillText(token, cx, y)
    cx += tw
  }
}

function drawCodeStrip(c: CanvasRenderingContext2D, stepIndex: number, x: number, y: number, w: number, h: number) {
  fillRR(c, x + 2, y + 3, w, h, 7, 'rgba(29,27,24,.28)')
  fillRR(c, x, y, w, h, 7, '#1d1b18', C.ink, 1.2)
  const lines = steps[stepIndex].code
  const lineH = Math.min(14, (h - 10) / lines.length)
  lines.forEach((line, i) => {
    const ly = y + 10 + i * lineH
    txt(c, String(i + 1), x + 8, ly, compactScene ? 7.6 : 8.2, 600, '#8b847a', 'right')
    drawCodeLine(c, line, x + 17, ly, x + w - 7)
  })
  fillRR(c, x + w - 35, y + 4, 30, 12, 4, '#34302b', 'rgba(255,255,255,.14)', 0.7, 0)
  txt(c, 'PHP', x + w - 20, y + 12, 6.4, 800, '#b2d491', 'center')
}

function drawProceduralDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const colW = (w - 14) / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, x, y, colW, h, 'PROSEDURAL', ['$panjang = 10', '$lebar = 5', 'hitungLuas()'], {
    fill: C.paper2,
    accent: C.amber,
  })
  drawMiniCard(c, x + colW + 14, y, colW, h, 'OOP', ['$panjang 10', '$lebar 5', 'luas()'], {
    fill: C.greenTile,
    accent: C.green3,
    titleColor: C.greenDark,
  })
  drawTag(c, 'terpisah', x + 10, y + h - 18, C.amberSoft)
  drawTag(c, 'satu object', x + colW + 24, y + h - 18, C.green)
  c.restore()
}

function drawBlueprintDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  c.save()
  c.globalAlpha = p
  const bx = x + 12
  const by = y + 5
  const bw = w - 24
  const bh = h - 10
  fillRR(c, bx, by, bw, bh, 8, C.cream)
  rr(c, bx, by, bw, bh, 8)
  c.strokeStyle = C.ink
  c.lineWidth = 1.5
  c.setLineDash([6, 5])
  c.stroke()
  c.setLineDash([])
  txt(c, 'class Mahasiswa', bx + 14, by + 22, 11, 800, C.ink)
  txt(c, 'BLUEPRINT', bx + bw - 12, by + 21, 8, 800, C.violetDark, 'right')
  c.beginPath()
  c.moveTo(bx + 12, by + 32)
  c.lineTo(bx + bw - 12, by + 32)
  c.strokeStyle = C.line
  c.lineWidth = 1
  c.stroke()

  if (compactScene) {
    ;['$nim : string', '$nama : string', '$ipk : float', 'sapa() : string'].forEach((row, i) => {
      txt(c, row, bx + 14, by + 48 + i * 14, 8.2, i === 3 ? 700 : 500, i === 3 ? C.greenDark : C.ink2)
    })
  } else {
    txt(c, 'PROPERTI', bx + 14, by + 50, 7.2, 800, C.muted)
    txt(c, 'METHOD', bx + bw / 2 + 10, by + 50, 7.2, 800, C.muted)
    ;['$nim', '$nama', '$ipk'].forEach((row, i) => txt(c, row, bx + 14, by + 64 + i * 14, 8.2, 500, C.ink2))
    ;['sapa()', 'cetakInfo()'].forEach((row, i) => txt(c, row, bx + bw / 2 + 10, by + 64 + i * 14, 8.2, 700, C.greenDark))
  }
  drawTag(c, 'belum ada instance', bx + 14, by + bh - 22, C.paper2)
  c.restore()
}

function drawInstantiationDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const leftW = compactScene ? 82 : 112
  const rightX = x + leftW + (compactScene ? 18 : 30)
  const rightW = x + w - rightX
  const cardH = (h - 8) / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, x, y + h / 2 - 31, leftW, 62, 'Mahasiswa', ['blueprint'], { fill: C.violet, accent: C.violet2, rowSize: 7.5 })
  drawArrow(c, x + leftW + 3, y + h / 2, rightX - 4, y + h / 2, 'new', false, C.ink)
  drawMiniCard(c, rightX, y, rightW, cardH - 4, 'Ahmad', ['nama: Ahmad', 'ipk: 3.85'], { fill: C.greenTile, accent: C.green3 })
  drawMiniCard(c, rightX, y + cardH + 4, rightW, cardH - 4, 'Rina', ['nama: Rina', 'ipk: 3.92'], { fill: C.violet, accent: C.violet2 })
  c.restore()
}

function drawThisDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const cardX = x + (compactScene ? 40 : 62)
  const cardW = w - (compactScene ? 44 : 70)
  const cardH = Math.min(h - 10, compactScene ? 108 : 124)
  const cardY = y + (h - cardH) / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, cardX, cardY, cardW, cardH, 'Object Mahasiswa', ['$nama = "Ahmad"', '$ipk = 3.85', 'sapa() { ... }'], {
    fill: C.cream,
    accent: C.green3,
    rowSize: compactScene ? 7.3 : 8,
  })
  drawTag(c, '$mhs', x + 3, cardY + 24, C.amberSoft)
  drawArrow(c, x + 36, cardY + 32, cardX - 3, cardY + 37, '->', false, C.ink)
  drawTag(c, '$this', cardX + cardW - 42, cardY + cardH - 22, C.violet)
  drawArrow(c, cardX + cardW - 22, cardY + cardH - 25, cardX + cardW - 58, cardY + 56, '', true, C.violetDark)
  c.restore()
}

function drawConstructorDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.9))
  const gap = compactScene ? 10 : 24
  const bw = (w - gap * 2) / 3
  const bh = Math.min(h - 24, 98)
  const by = y + (h - bh) / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, x, by, bw, bh, 'new', ["Mahasiswa('Ahmad',", '3.85)'], { fill: C.amberSoft, accent: C.amber, rowSize: 7.2 })
  drawMiniCard(c, x + bw + gap, by, bw, bh, '__construct', ['$nama = Ahmad', '$ipk = 3.85'], { fill: C.violet, accent: C.violet2, rowSize: 7.2 })
  drawMiniCard(c, x + (bw + gap) * 2, by, bw, bh, 'Object', ['Ahmad', 'ipk 3.85'], { fill: C.greenTile, accent: C.green3, rowSize: 7.2 })
  drawArrow(c, x + bw + 2, y + h / 2, x + bw + gap - 3, y + h / 2, '', false, C.ink)
  drawArrow(c, x + bw * 2 + gap + 2, y + h / 2, x + (bw + gap) * 2 - 3, y + h / 2, '', false, C.ink)
  font(c, 7.5, 800)
  const autoW = c.measureText('otomatis').width + 12
  drawTag(c, 'otomatis', x + bw + gap + bw / 2 - autoW / 2, y + 2, C.cream)
  c.restore()
}

function drawEncapsulationDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const capsuleW = compactScene ? w * 0.56 : w * 0.6
  c.save()
  c.globalAlpha = p
  fillRR(c, x + 2, y + 3, capsuleW, h - 6, 11, C.ink)
  fillRR(c, x, y, capsuleW, h - 6, 11, C.greenTile, C.ink, 1.5)
  txt(c, 'OBJECT REKENING', x + 12, y + 17, 8.2, 800, C.greenDark)
  fillRR(c, x + 12, y + 26, capsuleW - 24, h - 54, 8, C.cream, C.ink, 1.2)
  txt(c, 'PRIVATE STATE', x + 21, y + 39, 7, 800, C.muted)
  txt(c, '$saldo = 0', x + 21, y + 52, 8.2, 700, C.ink2)
  txt(c, '$pin = "••••"', x + 21, y + 64, 8.2, 700, C.ink2)
  // lock
  c.strokeStyle = C.ink
  c.lineWidth = 1.4
  c.beginPath()
  c.arc(x + capsuleW - 28, y + 37, 5, Math.PI, 0)
  c.stroke()
  fillRR(c, x + capsuleW - 36, y + 37, 16, 12, 3, C.amber, C.ink, 1.1, 0)
  drawTag(c, 'setor()', x + 18, y + h - 24, C.green)
  drawTag(c, 'tarik()', x + 66, y + h - 24, C.green)
  drawTag(c, 'getSaldo()', x + 112, y + h - 24, C.green)
  txt(c, 'PUBLIC API', x + 18, y + h - 31, 6.8, 800, C.muted)
  c.restore()

  const vx = x + capsuleW + 14
  const vw = x + w - vx
  const rows = [
    ['PUBLIC', 'bebas diakses', C.green2],
    ['PROTECTED', 'class + child', C.amber],
    ['PRIVATE', 'hanya class', C.rust],
  ]
  c.save()
  c.globalAlpha = p
  rows.forEach(([name, note, color], i) => {
    const ry = y + 5 + i * ((h - 10) / 3)
    const rh = (h - 10) / 3 - 5
    fillRR(c, vx, ry, vw, rh, 6, C.cream, C.lineStrong, 1)
    fillRR(c, vx + 6, ry + 6, 3, rh - 12, 1.5, color as string, undefined, 0)
    txt(c, name as string, vx + 15, ry + 15, 7.2, 800, C.ink)
    txt(c, note as string, vx + 15, ry + 26, 6.6, 500, C.muted)
  })
  c.restore()
}

function drawInheritanceDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const parentW = compactScene ? w * 0.62 : w * 0.48
  const childW = (w - 14) / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, x + (w - parentW) / 2, y, parentW, 50, 'SivitasAkademika', ['$nama', '$email'], { fill: C.violet, accent: C.violet2, rowSize: 7.2 })
  drawMiniCard(c, x, y + h - 62, childW, 58, 'Mahasiswa', ['$nim', 'ambilMK()'], { fill: C.greenTile, accent: C.green3, rowSize: 7.2 })
  drawMiniCard(c, x + childW + 14, y + h - 62, childW, 58, 'Dosen', ['$nidn', 'ajar()'], { fill: C.blueSoft, accent: C.blue, rowSize: 7.2 })
  drawArrow(c, x + w / 2 - 30, y + 51, x + childW / 2, y + h - 65, 'extends', false, C.ink)
  drawArrow(c, x + w / 2 + 30, y + 51, x + childW + 14 + childW / 2, y + h - 65, 'extends', false, C.ink)
  c.restore()
}

function drawPolymorphismDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const gap = compactScene ? 6 : 10
  const bw = (w - gap * 2) / 3
  const topW = compactScene ? w * 0.5 : w * 0.38
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, x + (w - topW) / 2, y, topW, 48, 'Hewan', ['bersuara()'], { fill: C.violet, accent: C.violet2, rowSize: 7.2 })
  const items = [
    ['Kucing', 'Meong', C.amberSoft, C.amber],
    ['Anjing', 'Guk', C.greenTile, C.green3],
    ['Bebek', 'Kwek', C.blueSoft, C.blue],
  ] as const
  items.forEach(([name, sound, fill, accent], i) => {
    const bx = x + i * (bw + gap)
    drawMiniCard(c, bx, y + h - 62, bw, 58, name, [`"${sound}"`], { fill, accent, rowSize: 8 })
    drawArrow(c, x + w / 2, y + 49, bx + bw / 2, y + h - 65, '', true, C.ink)
  })
  drawTag(c, '$hewan->bersuara()', x + 2, y + 2, C.cream)
  c.restore()
}

function drawAbstractionDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const gap = compactScene ? 6 : 10
  const bw = (w - gap * 2) / 3
  const topW = compactScene ? w * 0.56 : w * 0.4
  c.save()
  c.globalAlpha = p
  fillRR(c, x + (w - topW) / 2, y, topW, 50, 7, C.violet, C.ink, 1.3)
  txt(c, '<<interface>>', x + w / 2, y + 13, 6.8, 700, C.violetDark, 'center')
  txt(c, 'Pembayaran', x + w / 2, y + 25, 9.2, 800, C.ink, 'center')
  txt(c, 'bayar(float $n)', x + w / 2, y + 39, 7.2, 600, C.ink2, 'center')
  const items = [
    ['Transfer', 'bayar()', C.greenTile, C.green3],
    ['QRIS', 'bayar()', C.blueSoft, C.blue],
    ['E-Wallet', 'bayar()', C.amberSoft, C.amber],
  ] as const
  items.forEach(([name, method, fill, accent], i) => {
    const bx = x + i * (bw + gap)
    drawMiniCard(c, bx, y + h - 60, bw, 56, name, [method], { fill, accent, rowSize: 7.8 })
    drawArrow(c, x + w / 2, y + 51, bx + bw / 2, y + h - 63, i === 1 ? 'implements' : '', true, C.ink)
  })
  c.restore()
}

function drawRecapDiagram(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const p = easeOut(clamp(t / 0.8))
  const cw = compactScene ? Math.min(150, w * 0.55) : 190
  const ch = compactScene ? 62 : 72
  const cx = x + w / 2
  const cy = y + h / 2
  c.save()
  c.globalAlpha = p
  drawMiniCard(c, cx - cw / 2, cy - ch / 2, cw, ch, 'Mahasiswa', ['$nama', '$ipk', 'sapa()'], { fill: C.greenTile, accent: C.green3, rowSize: 7.6 })
  const badges = [
    ['ENCAPS', C.green2, -1, -1],
    ['INHERIT', C.blueSoft, 1, -1],
    ['POLY', C.amberSoft, -1, 1],
    ['ABSTRACT', C.violet, 1, 1],
  ] as const
  badges.forEach(([label, fill, dx, dy]) => {
    const bx = dx < 0 ? x + 2 : x + w - (compactScene ? 62 : 78)
    const by = dy < 0 ? y + 2 : y + h - 22
    fillRR(c, bx, by, compactScene ? 60 : 76, 20, 10, fill as string, C.ink, 1)
    txt(c, label as string, bx + (compactScene ? 30 : 38), by + 13.5, compactScene ? 6.4 : 7, 800, C.ink, 'center')
    c.beginPath()
    c.moveTo(dx < 0 ? bx + (compactScene ? 60 : 76) : bx, by + 10)
    c.lineTo(cx + dx * cw * 0.45, cy + dy * ch * 0.4)
    c.strokeStyle = 'rgba(29,27,24,.35)'
    c.lineWidth = 1
    c.setLineDash([3, 3])
    c.stroke()
    c.setLineDash([])
  })
  c.restore()
}

function drawDiagram(c: CanvasRenderingContext2D, stepIndex: number, t: number, x: number, y: number, w: number, h: number) {
  switch (stepIndex) {
    case 0:
      drawProceduralDiagram(c, t, x, y, w, h)
      break
    case 1:
      drawBlueprintDiagram(c, t, x, y, w, h)
      break
    case 2:
      drawInstantiationDiagram(c, t, x, y, w, h)
      break
    case 3:
      drawThisDiagram(c, t, x, y, w, h)
      break
    case 4:
      drawConstructorDiagram(c, t, x, y, w, h)
      break
    case 5:
      drawEncapsulationDiagram(c, t, x, y, w, h)
      break
    case 6:
      drawInheritanceDiagram(c, t, x, y, w, h)
      break
    case 7:
      drawPolymorphismDiagram(c, t, x, y, w, h)
      break
    case 8:
      drawAbstractionDiagram(c, t, x, y, w, h)
      break
    case 9:
      drawRecapDiagram(c, t, x, y, w, h)
      break
  }
}

function drawEditorCard(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const x = 360
  const y = 106 + Math.sin(t * 0.85 + 0.8) * 2
  const w = 580
  const h = 380
  const r = 17

  c.save()
  c.globalAlpha = 0.1
  c.fillStyle = C.ink
  c.beginPath()
  c.ellipse(x + w / 2, y + h + 22, w * 0.36, 20, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()

  fillRR(c, x + 6, y + 8, w, h, r, C.ink)
  fillRR(c, x, y, w, h, r, C.cream)

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

  ;[C.green3, C.amber, C.rust].forEach((color, i) => {
    c.beginPath()
    c.arc(x + 18 + i * 12, y + 20, 3.5, 0, Math.PI * 2)
    c.fillStyle = color
    c.fill()
    c.strokeStyle = 'rgba(29,27,24,.7)'
    c.lineWidth = 0.8
    c.stroke()
  })
  txt(c, 'editor.view', x + 58, y + 24, 11, 800)
  txt(c, `${steps[stepIndex].file} · PHP 8.4`, x + w - 18, y + 24, 9.2, 600, C.muted, 'right')

  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 2.1
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.panelTitle.toUpperCase(), x + 26, y + 68, 9.5, 800, C.muted)
  txt(c, s.panelMetric, x + 26, y + 91, s.panelMetric.length > 22 ? 13.5 : 16, 800, C.ink)

  const ax = x + 26
  const ay = y + 108
  const aw = w - 52
  const ah = h - 132
  const codeH = 64
  const gap = 8
  const diagramH = ah - codeH - gap

  c.save()
  rr(c, x + 2, y + 44, w - 4, h - 46, 10)
  c.clip()
  drawDiagram(c, stepIndex, t, ax, ay, aw, diagramH)
  drawCodeStrip(c, stepIndex, ax, ay + diagramH + gap, aw, codeH)
  c.restore()
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
  txt(c, 'editor.view', x + 48, y + 22, 10, 800)
  txt(c, steps[stepIndex].file, x + w - 14, y + 22, 8.2, 600, C.muted, 'right')

  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 1.9
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.panelTitle.toUpperCase(), x + 20, y + 56, 8, 800, C.muted)
  txt(c, s.panelMetric, x + 20, y + 77, s.panelMetric.length > 22 ? 11.5 : 13.5, 800, C.ink)

  const ax = x + 20
  const ay = y + 94
  const aw = w - 40
  const ah = h - 112
  const codeH = ah > 160 ? 52 : 48
  const gap = 6
  const diagramH = ah - codeH - gap

  c.save()
  rr(c, x + 2, y + 40, w - 4, h - 42, 9)
  c.clip()
  drawDiagram(c, stepIndex, t, ax, ay, aw, diagramH)
  drawCodeStrip(c, stepIndex, ax, ay + diagramH + gap, aw, codeH)
  c.restore()
}

function drawScene(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  drawBackdrop(c, t)
  drawClassPlatform(c, t, stepIndex)
  drawFlow(c, t, stepIndex)
  drawEditorCard(c, t, stepIndex)
  drawPilarPill(c, t, stepIndex)
  pill(c, platformLabel(stepIndex), 84, 519, { size: 11.5, h: 30, dot: C.amber })
}

function drawCompactScene(c: CanvasRenderingContext2D, t: number, stepIndex: number, w: number, h: number) {
  drawCompactBackdrop(c, t, w, h)
  const pillW = Math.min(260, w - 24)
  drawPilarPill(c, t, stepIndex, (w - pillW) / 2, 8, pillW, 36)
  drawCompactCard(c, t, stepIndex, 6, 55, w - 12, h - 60)
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
</style>
