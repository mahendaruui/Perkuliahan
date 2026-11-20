<template>
  <div class="dv-root" :class="{ 'is-drawer': drawerOpen }">
    <header class="dv-topbar">
      <button class="dv-menu-btn" type="button" aria-label="Buka daftar langkah" :aria-expanded="drawerOpen" @click="drawerOpen = true">
        <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5.5h14M3 10h14M3 14.5h9" /></svg>
      </button>

      <a class="dv-brand" :href="withBase('/big-data/canvas')" aria-label="Kanvas Big Data — mulai dari langkah pertama" @click.prevent="goTo(0)">
        <svg class="dv-logo" viewBox="0 0 34 34" aria-hidden="true">
          <rect x="2.4" y="5.5" width="29.2" height="23" rx="6" fill="#fbf7f1" stroke="#1d1b18" stroke-width="1.8" />
          <path d="M9 22.5 15.5 12l9.5 6.5" fill="none" stroke="#1d1b18" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" />
          <circle cx="9" cy="22.5" r="3" fill="#b2d491" stroke="#1d1b18" stroke-width="1.1" />
          <circle cx="15.5" cy="12" r="3" fill="#e7ddf5" stroke="#1d1b18" stroke-width="1.1" />
          <circle cx="25" cy="18.5" r="3" fill="#fcdcbd" stroke="#1d1b18" stroke-width="1.1" />
        </svg>
        <span class="dv-brand__name">Kanvas <span>Big Data</span></span>
        <span class="dv-brand__sub">IFR229</span>
      </a>

      <nav class="dv-nav" aria-label="Navigasi kanvas">
        <button class="dv-nav__item is-active" type="button">Belajar</button>
        <a class="dv-nav__item" :href="withBase('/big-data/')">Modul</a>
        <a class="dv-nav__item" :href="withBase('/presentasi/pertemuan-1-big-data')">Slide</a>
      </nav>

      <button class="dv-search" type="button" aria-label="Cari langkah dan konsep" :aria-expanded="searchOpen" @click="openSearch">
        <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
        <span class="dv-search__hint">Cari langkah &amp; konsep…</span>
        <kbd>⌘K</kbd>
      </button>

      <div class="dv-credit" role="note" title="Dosen Pengampu: Mahendar Dwi Payana, S.ST., M.T." aria-label="Dosen Pengampu: Mahendar Dwi Payana, S.ST., M.T.">
        <span class="dv-credit__x" aria-hidden="true">MDP</span>
        <span class="dv-credit__text"><small>Dosen Pengampu</small><b>Mahendar Dwi Payana, S.ST., M.T.</b></span>
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
          <div class="dv-crumb">Big Data <span>/</span> Kanvas interaktif</div>
          <div class="dv-lesson-head__row">
            <div class="dv-title-wrap">
              <h1 class="dv-title">Alur Big Data</h1>
              <p class="dv-subtitle">Dari event mentah ke insight — satu pipeline yang bisa digambar.</p>
            </div>
            <div class="dv-tags">
              <span class="dv-tag dv-tag--sand">
                <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.6" /><path d="M8 4.8V8l2.2 1.4" /></svg>
                18 mnt
              </span>
              <span class="dv-tag dv-tag--mint">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 12.5V9.8h2.4v2.7ZM6.8 12.5V6.7h2.4v5.8ZM11.1 12.5V3.5h2.4v9Z" /></svg>
                Menengah
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
            <span><i class="dv-lg dv-lg--data"></i> source</span>
            <span><i class="dv-lg dv-lg--insight"></i> flow</span>
            <span><i class="dv-lg dv-lg--noise"></i> process</span>
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

        <p class="dv-footnote">Diagram arsitektur disederhanakan untuk memperjelas alur. Implementasi produksi membutuhkan detail keamanan, biaya, dan operasi.</p>
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
              <span>Coba “kafka”, “hdfs”, atau “spark”.</span>
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
  nodeCount: string
  linkCount: string
  mode: string
  modeLevel: string
}

interface Goal {
  text: string
  at: number
}

const steps: Step[] = [
  {
    id: 'landscape',
    short: '5V',
    title: 'Banyak data, belum tentu big data',
    phase: 'FONDASI',
    tone: 'sand',
    body: `<p><b>Big Data</b> bukan hanya soal ukuran. Lima karakteristik <span class="term">5V</span> — volume, velocity, variety, veracity, dan value — menjelaskan mengapa sistemnya harus dirancang berbeda.</p><p>Yang membuatnya berharga bukan tumpukan datanya, melainkan keputusan yang bisa dihasilkan darinya.</p>`,
    idea: `Data besar tidak berharga karena ukurannya, tetapi karena keputusan yang bisa dihasilkan.`,
    panelTitle: 'Lanskap Big Data',
    panelMetric: '5V · banyak sumber',
    nodeCount: '6',
    linkCount: '5',
    mode: '—',
    modeLevel: '',
  },
  {
    id: 'ingestion',
    short: 'Ingest',
    title: 'Dari sumber yang tersebar ke satu aliran',
    phase: 'SUMBER',
    tone: 'amber',
    body: `<p>Aplikasi, database, log, dan sensor menghasilkan data dengan bentuk dan kecepatan berbeda. <span class="term">Ingestion</span> mengubah aliran itu menjadi event yang rapi dan bisa diproses.</p><p>Tanpa ingestion yang andal, pipeline yang mahal tetap membaca data yang terlambat atau hilang.</p>`,
    idea: `Sumber boleh banyak dan berantakan; ingestion harus membuatnya konsisten.`,
    panelTitle: 'Sumber → ingestion',
    panelMetric: 'event masuk',
    nodeCount: '6',
    linkCount: '5',
    mode: 'Hybrid',
    modeLevel: 'warn',
  },
  {
    id: 'storage',
    short: 'Storage',
    title: 'Simpan besar, tetap tahan kegagalan',
    phase: 'PENYIMPANAN',
    tone: 'violet',
    body: `<p><span class="term">Penyimpanan terdistribusi</span> membagi file menjadi blok dan mereplikasinya ke beberapa node. HDFS mengutamakan throughput untuk file besar; object storage populer di cloud.</p><p>Replikasi menukar ruang dengan ketahanan; partisi menukar kompleksitas dengan skalabilitas.</p>`,
    idea: `Anggap kegagalan node sebagai hal normal: replikasi dan partisi adalah cara sistem tetap hidup.`,
    panelTitle: 'Penyimpanan',
    panelMetric: 'HDFS · replikasi',
    nodeCount: '5',
    linkCount: '6',
    mode: 'Batch',
    modeLevel: '',
  },
  {
    id: 'batch',
    short: 'MapReduce',
    title: 'Pecah pekerjaan, gabungkan hasil',
    phase: 'BATCH',
    tone: 'green',
    body: `<p><b>MapReduce</b> memecah pekerjaan besar: split → map → shuffle &amp; sort → reduce. Setiap tahap bekerja paralel di banyak node.</p><p><span class="term">Shuffle</span> adalah biaya terbesar karena memindahkan data antar node.</p>`,
    idea: `Move compute to data: kirim pekerjaan ke tempat data berada, bukan data ke pekerjaan.`,
    panelTitle: 'Batch processing',
    panelMetric: 'map → shuffle → reduce',
    nodeCount: '8',
    linkCount: '10',
    mode: 'Batch',
    modeLevel: '',
  },
  {
    id: 'spark',
    short: 'Spark',
    title: 'Satu DAG, banyak executor',
    phase: 'PROCESSING',
    tone: 'blue',
    body: `<p><b>Apache Spark</b> menyimpan data antar-transformasi di memori dan menyusun pekerjaan sebagai <span class="term">DAG</span>. Driver mengatur task; executor menjalankannya secara paralel.</p><p>Lazy evaluation memberi optimizer kesempatan menggabungkan pekerjaan sebelum dieksekusi.</p>`,
    idea: `Spark cepat karena mengurangi I/O antar-tahap — bukan karena satu mesin menjadi ajaib.`,
    panelTitle: 'Apache Spark',
    panelMetric: 'DAG · in-memory',
    nodeCount: '5',
    linkCount: '7',
    mode: 'Batch',
    modeLevel: '',
  },
  {
    id: 'kafka',
    short: 'Kafka',
    title: 'Event mengalir tanpa menunggu batch',
    phase: 'STREAMING',
    tone: 'amber',
    body: `<p><b>Kafka</b> menampung event sebagai log terpartisi. Producer menulis ke topic; consumer group membaca partisi secara paralel.</p><p>Event streaming membuat data tersedia saat terjadi, bukan menunggu jadwal batch berikutnya.</p>`,
    idea: `Streaming mengubah pertanyaan dari “apa yang terjadi kemarin?” menjadi “apa yang sedang terjadi?”.`,
    panelTitle: 'Kafka streaming',
    panelMetric: 'producer → topic → consumer',
    nodeCount: '6',
    linkCount: '5',
    mode: 'Stream',
    modeLevel: 'good',
  },
  {
    id: 'lakehouse',
    short: 'Lakehouse',
    title: 'Bersihkan data bertahap',
    phase: 'LAKEHOUSE',
    tone: 'green',
    body: `<p><span class="term">Medallion architecture</span> membersihkan data secara bertahap: bronze menyimpan data mentah, silver membersihkan dan menstandarkan, gold menyiapkan data siap bisnis.</p><p>Setiap lapisan punya kontrak dan kualitasnya sendiri.</p>`,
    idea: `Jangan campur data mentah dengan data siap pakai; setiap lapisan harus bisa diaudit.`,
    panelTitle: 'Lakehouse',
    panelMetric: 'bronze → silver → gold',
    nodeCount: '5',
    linkCount: '4',
    mode: 'Hybrid',
    modeLevel: 'warn',
  },
  {
    id: 'airflow',
    short: 'Airflow',
    title: 'Pipeline adalah produk',
    phase: 'ORCHESTRATION',
    tone: 'violet',
    body: `<p><b>Airflow</b> menyusun task sebagai <span class="term">DAG</span>: extract, validate, transform, load, publish. Retry, timeout, dan quality gate menjaga pipeline tetap dapat dipercaya.</p><p>Pipeline yang baik punya jadwal, tes, alert, versi, dan pemilik.</p>`,
    idea: `Pipeline bukan skrip sekali pakai; ia produk yang harus dirawat seperti aplikasi.`,
    panelTitle: 'Orkestrasi',
    panelMetric: 'DAG · retry · quality gate',
    nodeCount: '5',
    linkCount: '5',
    mode: 'Batch',
    modeLevel: '',
  },
  {
    id: 'serving',
    short: 'Serving',
    title: 'Data yang dipakai, bukan hanya disimpan',
    phase: 'INSIGHT',
    tone: 'blue',
    body: `<p>Setelah data siap di <b>gold layer</b>, query engine dan model ML menyajikannya ke dashboard, API, atau keputusan operasional.</p><p>Di sinilah nilai big data terlihat: ketika data mengubah tindakan.</p>`,
    idea: `Nilai sistem data terlihat saat data dipakai, bukan saat tersimpan rapi di danau data.`,
    panelTitle: 'Serving & analitik',
    panelMetric: 'query → dashboard',
    nodeCount: '4',
    linkCount: '3',
    mode: 'Hybrid',
    modeLevel: 'warn',
  },
  {
    id: 'endtoend',
    short: 'End-to-end',
    title: 'Dari event mentah ke keputusan',
    phase: 'REKAP',
    tone: 'green',
    body: `<p>Sumber → ingestion → storage → processing → serving → observability. Satu pipeline utuh menghubungkan event mentah dengan keputusan yang bisa dipertanggungjawabkan.</p><p>Setiap panah punya kontrak, biaya, latency, dan SLA.</p>`,
    idea: `Arsitektur yang baik bisa dijelaskan sebagai alur; kalau tidak bisa digambar, mungkin belum dipahami.`,
    panelTitle: 'Pipeline utuh',
    panelMetric: 'source → insight',
    nodeCount: '6',
    linkCount: '6',
    mode: 'Hybrid',
    modeLevel: 'warn',
  },
]

const goals: Goal[] = [
  { text: 'Menjelaskan karakteristik 5V', at: 1 },
  { text: 'Membedakan batch, stream, dan hybrid', at: 6 },
  { text: 'Memahami storage & pemrosesan terdistribusi', at: 5 },
  { text: 'Menjelaskan lakehouse, orkestrasi, dan kualitas', at: 8 },
  { text: 'Membaca pipeline end-to-end', at: 10 },
]

const moduleDefs = [
  { id: 'm1', title: '01. Fondasi & sumber', color: 'sand', items: [0, 1] },
  { id: 'm2', title: '02. Simpan & proses', color: 'green', items: [2, 3, 4] },
  { id: 'm3', title: '03. Stream & lakehouse', color: 'blue', items: [5, 6] },
  { id: 'm4', title: '04. Operasi & insight', color: 'violet', items: [7, 8, 9] },
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
      label: 'TAHAP',
      value: `${current.value + 1}/10`,
      level: current.value === steps.length - 1 ? 'good' : '',
      path: 'M2.5 8h11M9.5 3.5 14 8l-4.5 4.5',
    },
    {
      label: 'NODE',
      value: s.nodeCount,
      level: 'good',
      path: 'M8 2.2 13 5v6l-5 2.8L3 11V5z M3 5l5 2.8L13 5M8 7.8v6',
    },
    {
      label: 'KONEKSI',
      value: s.linkCount,
      level: 'good',
      path: 'M3 5.5h4M9 10.5h4M7 5.5l4 5',
    },
    {
      label: 'MODE',
      value: s.mode,
      level: s.modeLevel,
      path: 'M2 11c1.8-4.5 3.7-4.5 5.5 0s3.7 4.5 5.5 0',
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

function slabPoint(cx: number, cy: number, hw: number, hh: number, u: number, v: number) {
  return [cx + (u + v) * hw, cy + (u - v) * hh]
}

function diamond(c: CanvasRenderingContext2D, cx: number, cy: number, hw: number, hh: number) {
  c.beginPath()
  c.moveTo(cx, cy - hh)
  c.lineTo(cx + hw, cy)
  c.lineTo(cx, cy + hh)
  c.lineTo(cx - hw, cy)
  c.closePath()
}

function drawTag(c: CanvasRenderingContext2D, text: string, x: number, y: number, fill = C.cream) {
  font(c, 7.7, 800)
  const w = c.measureText(text).width + 12
  fillRR(c, x, y, w, 16, 8, fill, C.ink, 0.9, 0)
  txt(c, text, x + 6, y + 11, 7.7, 800, C.ink)
  return w
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

const STAGES = ['sumber', 'ingestion', 'storage', 'batch', 'spark', 'streaming', 'lakehouse', 'orchestration', 'serving', 'end-to-end']
function stageLabel(stepIndex: number) {
  return STAGES[stepIndex] ?? 'pipeline'
}

function drawDataPlatform(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
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

  // A stack of event records on the platform.
  for (let i = 2; i >= 0; i--) {
    const sx = cx - 45 + i * 5
    const sy = cy - 26 + i * 5
    fillRR(c, sx, sy, 92, 34, 5, i === 0 ? C.cream : '#f1e7db', C.ink, 1)
    c.beginPath()
    c.moveTo(sx + 9, sy + 10)
    c.lineTo(sx + 55, sy + 10)
    c.moveTo(sx + 9, sy + 17)
    c.lineTo(sx + 73, sy + 17)
    c.strokeStyle = 'rgba(29,27,24,.25)'
    c.lineWidth = 1
    c.stroke()
  }
  fillRR(c, cx + 45, cy - 46, 24, 16, 4, C.green2, C.ink, 1, 0)
  txt(c, 'e', cx + 57, cy - 35, 7.5, 800, C.ink, 'center')

  // Floating pipeline sheet.
  c.save()
  c.translate(96, 348)
  c.rotate(-0.08)
  fillRR(c, 8, -6, 138, 80, 5, '#e6ddd0', 'rgba(29,27,24,.45)', 1)
  fillRR(c, 2, 0, 138, 80, 5, C.cream, C.ink, 1.4)
  txt(c, 'pipeline', 12, 16, 9, 800, C.ink)
  txt(c, stageLabel(stepIndex), 12, 29, 7.4, 700, C.greenDark)
  c.strokeStyle = 'rgba(29,27,24,.26)'
  c.lineWidth = 1
  ;[42, 53, 64].forEach((yy) => {
    c.beginPath()
    c.moveTo(12, yy)
    c.lineTo(116, yy)
    c.stroke()
  })
  // mini node-link glyph
  c.strokeStyle = C.violetDark
  c.lineWidth = 1.2
  c.beginPath()
  c.moveTo(92, 50)
  c.lineTo(106, 44)
  c.lineTo(118, 56)
  c.stroke()
  ;[ [92,50], [106,44], [118,56] ].forEach(([px,py]) => {
    c.beginPath()
    c.arc(px,py,3.2,0,Math.PI*2)
    c.fillStyle = C.green2
    c.fill()
    c.strokeStyle = C.ink
    c.lineWidth = 0.9
    c.stroke()
  })
  c.restore()

  pill(c, `pipeline · ${stageLabel(stepIndex)}`, 64, 519, { size: 10.5, h: 30, dot: C.amber })
}

function bezierPoint(p0: number[], p1: number[], p2: number[], p3: number[], t: number) {
  const mt = 1 - t
  const a = mt * mt * mt
  const b = 3 * mt * mt * t
  const c = 3 * mt * t * t
  const d = t * t * t
  return [a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]]
}

function drawSceneFlow(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  const p0 = [330, 419]
  const p1 = [365, 411]
  const p2 = [344, 353]
  const p3 = [358, 342]

  c.save()
  c.beginPath()
  c.moveTo(p0[0], p0[1])
  c.bezierCurveTo(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
  c.strokeStyle = 'rgba(111,105,97,.65)'
  c.lineWidth = 1.7
  c.setLineDash([5, 5])
  c.stroke()
  c.setLineDash([])
  arrowHead(c, p3[0], p3[1], Math.atan2(p3[1] - p2[1], p3[0] - p2[0]), 5.5)
  c.restore()

  if (stepIndex === 0) return
  const label = steps[stepIndex].mode === 'Batch' ? 'b' : 'e'
  for (let i = 0; i < 2; i++) {
    const raw = (t * 0.32 + i / 2) % 1
    const progress = raw < 0.5 ? 2 * raw * raw : 1 - Math.pow(-2 * raw + 2, 2) / 2
    const q = bezierPoint(p0, p1, p2, p3, progress)
    const alpha = Math.sin(progress * Math.PI) * 0.95
    c.save()
    c.globalAlpha = Math.max(0, alpha)
    fillRR(c, q[0] - 7, q[1] - 7, 14, 14, 4, i === 0 ? C.green2 : C.amber, C.ink, 1.3, 0)
    txt(c, label, q[0], q[1] + 2.6, 7.8, 800, C.ink, 'center')
    c.restore()
  }
}

function drawStagePill(c: CanvasRenderingContext2D, t: number, stepIndex: number, x = 650, y = 52, w = 250, h = 38) {
  fillRR(c, x + 2, y + 3, w, h, h / 2, C.ink)
  fillRR(c, x, y, w, h, h / 2, C.cream, C.ink, 1.6)

  fillRR(c, x + 7, y + 7, 23, 23, 7, stepIndex === steps.length - 1 ? C.green2 : C.blueSoft, C.ink, 1.2, 0)
  c.save()
  c.translate(x + 18.5, y + 18.5)
  c.strokeStyle = C.ink
  c.lineWidth = 1.25
  c.beginPath()
  c.moveTo(-7, 4)
  c.lineTo(-1, -5)
  c.lineTo(7, 2)
  c.stroke()
  ;[[-7,4],[-1,-5],[7,2]].forEach(([px,py]) => {
    c.beginPath()
    c.arc(px,py,2.8,0,Math.PI*2)
    c.fillStyle = C.green2
    c.fill()
    c.strokeStyle = C.ink
    c.lineWidth = 0.9
    c.stroke()
  })
  c.restore()

  txt(c, 'ALUR DATA', x + 39, y + 23, 9, 800, C.muted)
  const filled = Math.min(5, Math.floor(stepIndex / 2) + 1)
  for (let i = 0; i < 5; i++) {
    fillRR(c, x + 108 + i * 16, y + 15, 11, 8, 4, i < filled ? C.green2 : C.lineSoft, 'rgba(29,27,24,.35)', 0.8, 0)
  }
  txt(c, `${stepIndex + 1}/10`, x + w - 14, y + 24, 10.5, 800, stepIndex === steps.length - 1 ? C.greenDark : C.ink, 'right')

  if (stepIndex === steps.length - 1) {
    rr(c, x - 3, y - 3, w + 6, h + 6, (h + 6) / 2)
    c.strokeStyle = `rgba(127,194,120,${0.32 + Math.sin(t * 2.2) * 0.06})`
    c.lineWidth = 2
    c.stroke()
  }
}

function nodeFill(kind: string) {
  if (kind === 'source') return C.amberSoft
  if (kind === 'storage') return C.violet
  if (kind === 'sink') return C.greenTile
  if (kind === 'observe') return C.blueSoft
  if (kind === 'stream') return C.mint
  return C.cream
}

function drawNode(
  c: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  title: string,
  sub: string,
  accent: string,
  kind = 'process',
  detail = '',
) {
  if (w <= 2 || h <= 2) return
  fillRR(c, x + 1.6, y + 2.6, w, h, 7, 'rgba(29,27,24,.9)')
  fillRR(c, x, y, w, h, 7, nodeFill(kind), C.ink, 1.25)
  fillRR(c, x + 5, y + 5, 3, Math.max(4, h - 10), 1.5, accent, undefined, 0)
  const titleSize = w < 62 ? 7.3 : w < 80 ? 8.1 : 8.9
  if (h < 33) {
    txt(c, title, x + 12, y + h / 2 + 2.8, titleSize, 800, C.ink)
  } else {
    txt(c, title, x + 12, y + 15, titleSize, 800, C.ink)
    if (sub) txt(c, sub, x + 12, y + 27, w < 62 ? 6.3 : 6.9, 500, C.ink2)
    if (detail && h >= 56) {
      c.beginPath()
      c.moveTo(x + 11, y + h - 19)
      c.lineTo(x + w - 11, y + h - 19)
      c.strokeStyle = 'rgba(29,27,24,.16)'
      c.lineWidth = 0.9
      c.stroke()
      txt(c, detail, x + 12, y + h - 7, w < 70 ? 6.1 : 6.6, 600, C.muted)
    }
  }
}

function pointOnPath(points: number[][], p: number) {
  const lengths: number[] = []
  let total = 0
  for (let i = 1; i < points.length; i++) {
    const dx = points[i][0] - points[i - 1][0]
    const dy = points[i][1] - points[i - 1][1]
    const l = Math.hypot(dx, dy)
    lengths.push(l)
    total += l
  }
  let target = Math.max(0, Math.min(1, p)) * total
  for (let i = 0; i < lengths.length; i++) {
    if (target <= lengths[i] || i === lengths.length - 1) {
      const r = lengths[i] === 0 ? 0 : target / lengths[i]
      return [
        lerp(points[i][0], points[i + 1][0], r),
        lerp(points[i][1], points[i + 1][1], r),
      ]
    }
    target -= lengths[i]
  }
  return points[points.length - 1]
}

function drawLink(
  c: CanvasRenderingContext2D,
  points: number[][],
  t: number,
  opts: { color?: string; dashed?: boolean; width?: number; packets?: number; speed?: number; packetColor?: string; offset?: number } = {},
) {
  if (points.length < 2) return
  const color = opts.color ?? C.ink
  c.save()
  c.strokeStyle = color
  c.lineWidth = opts.width ?? 1.35
  if (opts.dashed) {
    c.setLineDash([5, 5])
    c.lineDashOffset = -(t * 18) % 10
  }
  c.beginPath()
  c.moveTo(points[0][0], points[0][1])
  for (let i = 1; i < points.length; i++) c.lineTo(points[i][0], points[i][1])
  c.stroke()
  c.setLineDash([])
  const last = points[points.length - 1]
  const prev = points[points.length - 2]
  arrowHead(c, last[0], last[1], Math.atan2(last[1] - prev[1], last[0] - prev[0]), 4.4)

  const count = opts.packets ?? 1
  const speed = opts.speed ?? 0.24
  for (let i = 0; i < count; i++) {
    const p = (t * speed + i / count + (opts.offset ?? 0)) % 1
    const q = pointOnPath(points, p)
    c.beginPath()
    c.arc(q[0], q[1], 3.9, 0, Math.PI * 2)
    c.fillStyle = opts.packetColor ?? C.green2
    c.fill()
    c.lineWidth = 1
    c.strokeStyle = C.ink
    c.stroke()
  }
  c.restore()
}

function drawPillars5V(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const centerW = compactScene ? w - 124 : 154
  const centerH = compactScene ? 76 : 64
  const centerX = compactScene ? x + 120 : x + w / 2 - centerW / 2
  const centerY = compactScene ? y + h / 2 - centerH / 2 : y + h / 2 - centerH / 2
  drawNode(c, centerX, centerY, centerW, centerH, 'BIG DATA', '5V · sistem data', C.violet2, 'storage')

  const items = [
    ['VOLUME', 'banyak', C.amber],
    ['VELOCITY', 'cepat', C.blue],
    ['VARIETY', 'beragam', C.violet2],
    ['VERACITY', 'terpercaya', C.green3],
    ['VALUE', 'bernilai', C.rust],
  ] as const
  if (compactScene) {
    items.forEach(([title, sub, color], i) => {
      const ny = y + 4 + i * 33
      drawNode(c, x + 2, ny, 108, 26, title, '', color, 'source')
      drawLink(c, [[x + 110, ny + 13], [centerX, centerY + 12 + i * 8]], t, {
        color: C.muted,
        dashed: true,
        packets: 1,
        speed: 0.2,
        offset: i * 0.15,
        packetColor: color,
      })
    })
  } else {
    const positions = [
      [x + w / 2 - 55, y + 2, 110, 34],
      [x + 3, y + h / 2 - 20, 100, 40],
      [x + w - 103, y + h / 2 - 20, 100, 40],
      [x + w / 2 - 112, y + h - 38, 100, 34],
      [x + w / 2 + 12, y + h - 38, 100, 34],
    ] as const
    items.forEach(([title, sub, color], i) => {
      const [nx, ny, nw, nh] = positions[i]
      drawNode(c, nx, ny, nw, nh, title, sub, color, 'source')
      const sx = nx < centerX ? nx + nw : nx > centerX ? nx : nx + nw / 2
      const sy = ny < centerY ? ny + nh : ny > centerY ? ny : ny + nh / 2
      const ex = nx < centerX ? centerX : nx > centerX ? centerX + centerW : centerX + centerW / 2
      const ey = ny < centerY ? centerY : ny > centerY ? centerY + centerH : centerY + centerH / 2
      drawLink(c, [[sx, sy], [ex, ey]], t, {
        color: C.muted,
        dashed: true,
        packets: 2,
        speed: 0.2,
        offset: i * 0.14,
        packetColor: color,
      })
    })
  }
}

function drawIngestion(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  if (compactScene) {
    const sources = [
      ['App', 'events'],
      ['DB', 'rows'],
      ['Logs', 'files'],
    ] as const
    const colors = [C.amber, C.blue, C.violet2]
    const ingX = x + 102
    const ingY = y + h / 2 - 27
    sources.forEach(([title, sub], i) => {
      const ny = y + 8 + i * 48
      drawNode(c, x + 2, ny, 84, 34, title, sub, colors[i], 'source')
      drawLink(c, [[x + 86, ny + 17], [ingX, ingY + 18 + i * 4]], t, {
        color: C.muted,
        dashed: true,
        packets: 1,
        speed: 0.25,
        offset: i * 0.2,
        packetColor: colors[i],
      })
    })
    drawNode(c, ingX, ingY, 74, 54, 'Ingest', 'Kafka / API', C.green3, 'stream')
    drawNode(c, x + w - 68, ingY, 66, 54, 'Storage', 'lake', C.violet2, 'storage')
    drawLink(c, [[ingX + 74, ingY + 27], [x + w - 68, ingY + 27]], t, { packets: 2, packetColor: C.green2 })
    return
  }

  const midY = y + h / 2
  const sources = [
    [x + 3, midY - 52, 'Aplikasi', 'API · user events', C.amber],
    [x + 3, midY - 2, 'Database', 'transaksi', C.blue],
    [x + 111, midY - 52, 'Log', 'server · app', C.violet2],
    [x + 111, midY - 2, 'Sensor', 'IoT · telemetry', C.rust],
  ] as const
  const ingX = x + 244
  const ingY = midY - 34
  sources.forEach(([sx, sy, title, sub, color], i) => {
    drawNode(c, sx, sy, 100, 44, title as string, sub as string, color as string, 'source')
    drawLink(c, [[sx + 100, sy + 22], [ingX, ingY + 24 + i * 4]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.22,
      offset: i * 0.18,
      packetColor: color as string,
    })
  })
  drawNode(c, ingX, ingY, 112, 64, 'INGESTION', 'Kafka Connect / API', C.green3, 'stream')
  drawNode(c, x + w - 118, ingY, 112, 64, 'STORAGE', 'lake / HDFS', C.violet2, 'storage')
  drawLink(c, [[ingX + 112, ingY + 32], [x + w - 118, ingY + 32]], t, { packets: 2, packetColor: C.green2 })
}

function drawStorage(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  if (compactScene) {
    const clientX = x + w / 2 - 48
    const nnX = x + w / 2 - 65
    drawNode(c, clientX, y + 2, 96, 30, 'Client', '', C.amber, 'source')
    drawNode(c, nnX, y + 52, 130, 34, 'NameNode', 'metadata blok', C.violet2, 'storage')
    const dnW = (w - 16) / 3
    const dnY = y + h - 36
    drawLink(c, [[clientX + 48, y + 32], [nnX + 65, y + 50]], t, { packets: 2, packetColor: C.amber })
    for (let i = 0; i < 3; i++) {
      const dx = x + 2 + i * (dnW + 6)
      drawNode(c, dx, dnY, dnW, 34, `DN ${i + 1}`, 'blok', C.green3, 'storage')
      drawLink(c, [[nnX + 30 + i * 35, y + 86], [dx + dnW / 2, dnY]], t, {
        color: C.muted,
        dashed: true,
        packets: 1,
        speed: 0.2,
        offset: i * 0.2,
        packetColor: C.violet2,
      })
    }
    drawLink(c, [[x + 2 + dnW, dnY + 17], [x + 2 + dnW + 6, dnY + 17]], t, { dashed: true, packets: 1, speed: 0.4, color: C.muted })
    drawLink(c, [[x + 2 + dnW * 2 + 6, dnY + 17], [x + 2 + dnW * 2 + 12, dnY + 17]], t, { dashed: true, packets: 1, speed: 0.4, color: C.muted })
    return
  }

  const clientX = x + 6
  const clientY = y + h / 2 - 26
  drawNode(c, clientX, clientY, 92, 52, 'Client', 'baca / tulis', C.amber, 'source')
  const nnX = x + w / 2 - 65
  drawNode(c, nnX, y + 5, 130, 50, 'NameNode', 'metadata blok', C.violet2, 'storage')
  drawLink(c, [[clientX + 92, clientY + 26], [nnX, y + 30]], t, { packets: 2, packetColor: C.amber })
  const dnW = 100
  const dnY = y + h - 58
  const starts = [x + w / 2 - 160, x + w / 2 - 50, x + w / 2 + 60]
  starts.forEach((dx, i) => {
    drawNode(c, dx, dnY, dnW, 54, `DataNode ${i + 1}`, 'blok A/B/C', C.green3, 'storage')
    drawLink(c, [[nnX + 35 + i * 30, y + 55], [dx + dnW / 2, dnY]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.2,
      offset: i * 0.15,
      packetColor: C.violet2,
    })
  })
  drawLink(c, [[starts[0] + dnW, dnY + 27], [starts[1], dnY + 27]], t, { dashed: true, packets: 1, speed: 0.35, color: C.muted })
  drawLink(c, [[starts[1] + dnW, dnY + 27], [starts[2], dnY + 27]], t, { dashed: true, packets: 1, speed: 0.35, color: C.muted })
}

function drawMapReduce(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  if (compactScene) {
    drawNode(c, x + 2, y + 4, 86, 36, 'Input', 'split', C.amber, 'source')
    drawNode(c, x + 98, y + 4, w - 100, 36, 'MAP ×3', 'paralel', C.green3, 'process')
    drawNode(c, x + w / 2 - 86, y + h / 2 - 18, 172, 36, 'SHUFFLE', 'group by key', C.violet2, 'process')
    drawNode(c, x + 2, y + h - 40, 132, 36, 'REDUCE ×2', 'agregasi', C.greenTile, 'process')
    drawNode(c, x + w - 82, y + h - 40, 80, 36, 'Output', 'HDFS', C.blueSoft, 'sink')
    drawLink(c, [[x + 88, y + 22], [x + 98, y + 22]], t, { packets: 1, packetColor: C.amber })
    drawLink(c, [[x + w / 2, y + 40], [x + w / 2, y + h / 2 - 18]], t, { packets: 2, packetColor: C.green2 })
    drawLink(c, [[x + w / 2 - 30, y + h / 2 + 18], [x + 70, y + h - 40]], t, { packets: 2, packetColor: C.violet2 })
    drawLink(c, [[x + 134, y + h - 22], [x + w - 82, y + h - 22]], t, { packets: 1, packetColor: C.green2 })
    return
  }

  const inputW = 64
  const inputX = x + 4
  const midY = y + h / 2
  drawNode(c, inputX, midY - 24, inputW, 48, 'Input', 'HDFS split', C.amber, 'source')
  const mapX = x + 90
  const mapW = 80
  const mapH = 42
  const mapGap = 9
  const mapStart = y + (h - (mapH * 3 + mapGap * 2)) / 2
  for (let i = 0; i < 3; i++) {
    const my = mapStart + i * (mapH + mapGap)
    drawNode(c, mapX, my, mapW, mapH, `Map ${i + 1}`, 'map()', C.green3, 'process')
    drawLink(c, [[inputX + inputW, midY], [mapX, my + mapH / 2]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.25,
      offset: i * 0.2,
      packetColor: C.amber,
    })
  }
  const shuffleX = x + 214
  const shuffleW = 84
  drawNode(c, shuffleX, midY - 36, shuffleW, 72, 'Shuffle', 'sort · group', C.violet2, 'process')
  for (let i = 0; i < 3; i++) {
    const my = mapStart + i * (mapH + mapGap)
    drawLink(c, [[mapX + mapW, my + mapH / 2], [shuffleX, midY - 20 + i * 20]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.22,
      offset: i * 0.15,
      packetColor: C.green2,
    })
  }
  const reduceX = x + 320
  const reduceW = 80
  const reduceH = 48
  const reduceStart = y + (h - (reduceH * 2 + 10)) / 2
  for (let i = 0; i < 2; i++) {
    const ry = reduceStart + i * (reduceH + 10)
    drawNode(c, reduceX, ry, reduceW, reduceH, `Reduce ${i + 1}`, 'agregasi', C.greenTile, 'process')
    drawLink(c, [[shuffleX + shuffleW, midY - 12 + i * 24], [reduceX, ry + reduceH / 2]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.23,
      offset: i * 0.2,
      packetColor: C.violet2,
    })
  }
  const outputX = x + w - 74
  drawNode(c, outputX, midY - 24, 70, 48, 'Output', 'HDFS', C.blueSoft, 'sink')
  for (let i = 0; i < 2; i++) {
    const ry = reduceStart + i * (reduceH + 10)
    drawLink(c, [[reduceX + reduceW, ry + reduceH / 2], [outputX, midY - 12 + i * 24]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.23,
      offset: i * 0.25,
      packetColor: C.green2,
    })
  }
}

function drawSpark(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  if (compactScene) {
    drawNode(c, x + w / 2 - 58, y + 2, 116, 34, 'Driver', 'SparkSession', C.amber, 'process')
    drawNode(c, x + w / 2 - 62, y + 60, 124, 34, 'Cluster Manager', 'YARN / K8s', C.violet2, 'process')
    const exW = (w - 16) / 3
    const exY = y + h - 40
    drawLink(c, [[x + w / 2, y + 36], [x + w / 2, y + 60]], t, { packets: 2, packetColor: C.amber })
    for (let i = 0; i < 3; i++) {
      const exX = x + 2 + i * (exW + 6)
      drawNode(c, exX, exY, exW, 36, `Exec ${i + 1}`, 'task', C.green3, 'process')
      drawLink(c, [[x + w / 2 - 20 + i * 20, y + 94], [exX + exW / 2, exY]], t, {
        color: C.muted,
        dashed: true,
        packets: 1,
        speed: 0.22,
        offset: i * 0.2,
        packetColor: C.green2,
      })
    }
    return
  }
  const driverX = x + 6
  const driverY = y + h / 2 - 38
  drawNode(c, driverX, driverY, 104, 76, 'Driver', 'SparkSession · DAG', C.amber, 'process')
  const cmX = x + w / 2 - 70
  drawNode(c, cmX, y + 4, 140, 46, 'Cluster Manager', 'YARN / K8s', C.violet2, 'process')
  drawLink(c, [[driverX + 104, driverY + 18], [cmX, y + 27]], t, { packets: 2, packetColor: C.amber })
  const exW = 92
  const exH = 44
  const exX = x + w - exW - 4
  const exStart = y + (h - (exH * 3 + 16)) / 2
  for (let i = 0; i < 3; i++) {
    const ey = exStart + i * (exH + 8)
    drawNode(c, exX, ey, exW, exH, `Executor ${i + 1}`, 'task · cache', C.green3, 'process')
    drawLink(c, [[cmX + 140, y + 27], [exX, ey + exH / 2]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.2,
      offset: i * 0.2,
      packetColor: C.violet2,
    })
    drawLink(c, [[driverX + 104, driverY + 50], [exX, ey + exH - 8]], t, {
      color: C.muted,
      dashed: true,
      packets: 1,
      speed: 0.24,
      offset: i * 0.18,
      packetColor: C.amber,
    })
  }
}

function drawKafka(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const compact = compactScene
  const prodW = compact ? 72 : 100
  const prodH = compact ? 32 : 40
  const prodX = x + 2
  const startY = compact ? y + 8 : y + (h - (prodH * 3 + 18)) / 2
  const gap = compact ? 10 : 9
  const colors = [C.amber, C.blue, C.violet2]
  const topicX = compact ? x + 92 : x + 162
  const topicW = compact ? 84 : 148
  const topicY = y + 6
  const topicH = h - 12
  const consX = x + w - (compact ? 70 : 104)
  const consW = compact ? 66 : 100
  const consH = compact ? 34 : 48
  const consY = [compact ? y + 42 : y + 52, compact ? y + 102 : y + 142]

  drawNode(c, topicX, topicY, topicW, topicH, 'TOPIC orders', '', C.green3, 'stream')
  const partH = compact ? 24 : 34
  const partY0 = topicY + (compact ? 24 : 34)
  for (let i = 0; i < 3; i++) {
    fillRR(c, topicX + 8, partY0 + i * (partH + 6), topicW - 16, partH, 4, i === 1 ? C.green : C.paper2, C.ink, 1, 0)
    txt(c, `P${i}`, topicX + 16, partY0 + i * (partH + 6) + partH - 8, 7.4, 800, C.ink2)
  }

  for (let i = 0; i < 3; i++) {
    const py = startY + i * (prodH + gap)
    drawNode(c, prodX, py, prodW, prodH, `Producer ${i + 1}`, compact ? '' : 'events', colors[i], 'source')
    drawLink(c, [[prodX + prodW, py + prodH / 2], [topicX, partY0 + i * (partH + 6) + partH / 2]], t, {
      color: C.muted,
      dashed: true,
      packets: 2,
      speed: 0.25,
      offset: i * 0.18,
      packetColor: colors[i],
    })
  }
  for (let i = 0; i < 2; i++) {
    drawNode(c, consX, consY[i], consW, consH, `Consumer ${i + 1}`, compact ? '' : 'group A', C.greenTile, 'sink')
    drawLink(c, [[topicX + topicW, partY0 + (i === 0 ? partH / 2 : partH * 1.5 + 8)], [consX, consY[i] + consH / 2]], t, {
      color: C.muted,
      dashed: true,
      packets: 2,
      speed: 0.22,
      offset: i * 0.2,
      packetColor: C.green2,
    })
  }
}

function drawLakehouse(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const items = [
    ['SOURCE', 'raw events', C.amber, 'source', 'Kafka · files'],
    ['BRONZE', 'mentah', C.rust, 'storage', 'JSON · CSV'],
    ['SILVER', 'bersih', C.violet2, 'storage', 'Parquet'],
    ['GOLD', 'siap bisnis', C.green3, 'storage', 'star schema'],
    ['SERVE', 'BI · ML', C.blue, 'sink', 'dashboard'],
  ] as const
  if (compactScene) {
    const nw = w - 36
    const nh = 26
    const gap = 6
    const startY = y + (h - (nh * 5 + gap * 4)) / 2
    items.forEach(([title, sub, color, kind, detail], i) => {
      const ny = startY + i * (nh + gap)
      drawNode(c, x + 18, ny, nw, nh, title, '', color as string, kind, detail as string)
      if (i > 0) {
        drawLink(c, [[x + 18 + nw / 2, ny - gap], [x + 18 + nw / 2, ny]], t, {
          packets: 1,
          speed: 0.3,
          offset: i * 0.15,
          packetColor: color as string,
        })
      }
    })
    return
  }
  const nw = (w - 4 * 12) / 5
  const nh = 72
  const ny = y + h / 2 - nh / 2
  items.forEach(([title, sub, color, kind, detail], i) => {
    const nx = x + i * (nw + 12)
    drawNode(c, nx, ny, nw, nh, title, sub, color as string, kind, detail as string)
    if (i > 0) {
      drawLink(c, [[nx - 12, ny + nh / 2], [nx, ny + nh / 2]], t, {
        packets: 2,
        speed: 0.3,
        offset: i * 0.18,
        packetColor: color as string,
      })
    }
  })
  drawTag(c, 'quality gate', x + w / 2 - 40, y + 2, C.greenTile)
}

function drawAirflow(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const items = [
    ['Extract', 'API / DB', C.amber, 'retry 3×'],
    ['Validate', 'schema', C.violet2, 'quality gate'],
    ['Transform', 'clean', C.green3, 'dbt / SQL'],
    ['Load', 'silver/gold', C.blue, 'overwrite'],
    ['Publish', 'dashboard', C.greenTile, 'SLA · alert'],
  ] as const
  if (compactScene) {
    const nw = w - 54
    const nh = 26
    const gap = 6
    const startY = y + (h - (nh * 5 + gap * 4)) / 2
    items.forEach(([title, sub, color, detail], i) => {
      const ny = startY + i * (nh + gap)
      drawNode(c, x + 4, ny, nw, nh, title, '', color as string, 'process', detail as string)
      if (i > 0) {
        drawLink(c, [[x + 4 + nw / 2, ny - gap], [x + 4 + nw / 2, ny]], t, {
          packets: 1,
          speed: 0.3,
          offset: i * 0.15,
          packetColor: color as string,
        })
      }
    })
    drawLink(c, [[x + 4 + nw, startY + nh * 3 + gap * 3 + nh / 2], [x + w - 8, startY + nh * 3 + gap * 3 + nh / 2], [x + w - 8, startY + nh / 2], [x + 4 + nw, startY + nh / 2]], t, {
      color: C.rust,
      dashed: true,
      packets: 1,
      speed: 0.34,
      packetColor: C.rust,
    })
    drawTag(c, 'retry', x + w - 48, startY + 34, C.rustSoft)
    return
  }
  const nw = (w - 4 * 10) / 5
  const nh = 70
  const ny = y + h / 2 - nh / 2 - 8
  items.forEach(([title, sub, color, detail], i) => {
    const nx = x + i * (nw + 10)
    drawNode(c, nx, ny, nw, nh, title, sub, color as string, 'process', detail as string)
    if (i > 0) {
      drawLink(c, [[nx - 10, ny + nh / 2], [nx, ny + nh / 2]], t, {
        packets: 2,
        speed: 0.3,
        offset: i * 0.16,
        packetColor: color as string,
      })
    }
  })
  const loopY = y + h - 18
  drawLink(c, [[x + (nw + 10) * 3 + nw / 2, ny + nh], [x + (nw + 10) * 3 + nw / 2, loopY], [x + nw / 2, loopY], [x + nw / 2, ny + nh]], t, {
    color: C.rust,
    dashed: true,
    packets: 2,
    speed: 0.22,
    packetColor: C.rust,
  })
  drawTag(c, 'retry', x + w / 2 - 30, loopY - 8, C.rustSoft)
  drawTag(c, 'DAG', x + w - 38, y + 1, C.violet)
}

function drawServing(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  if (compactScene) {
    drawNode(c, x + 2, y + h / 2 - 28, 82, 56, 'GOLD', 'data', C.green3, 'storage')
    drawNode(c, x + 96, y + h / 2 - 28, 90, 56, 'Query', 'SQL / BI', C.violet2, 'process')
    drawNode(c, x + w - 78, y + 18, 74, 40, 'Dashboard', '', C.blue, 'sink')
    drawNode(c, x + w - 78, y + h - 58, 74, 40, 'ML / API', '', C.amber, 'sink')
    drawLink(c, [[x + 84, y + h / 2], [x + 96, y + h / 2]], t, { packets: 2, packetColor: C.green2 })
    drawLink(c, [[x + 186, y + h / 2 - 12], [x + w - 78, y + 38]], t, { packets: 2, packetColor: C.blue })
    drawLink(c, [[x + 186, y + h / 2 + 6], [x + w - 78, y + h - 38]], t, { packets: 2, packetColor: C.amber })
    return
  }
  const lakeX = x + 6
  const lakeY = y + h / 2 - 30
  drawNode(c, lakeX, lakeY, 112, 60, 'GOLD', 'data siap', C.green3, 'storage', 'star schema')
  const qX = x + w / 2 - 67
  drawNode(c, qX, lakeY, 134, 60, 'Query Engine', 'SQL · BI', C.violet2, 'process', 'cache · optimizer')
  const dashX = x + w - 106
  drawNode(c, dashX, y + 28, 100, 52, 'Dashboard', 'BI', C.blue, 'sink', 'KPI')
  drawNode(c, dashX, y + h - 82, 100, 52, 'ML / API', 'model', C.amber, 'sink', 'scoring')
  drawLink(c, [[lakeX + 112, lakeY + 30], [qX, lakeY + 30]], t, { packets: 2, packetColor: C.green2 })
  drawLink(c, [[qX + 134, lakeY + 18], [dashX, y + 54]], t, { packets: 2, packetColor: C.blue })
  drawLink(c, [[qX + 134, lakeY + 44], [dashX, y + h - 56]], t, { packets: 2, packetColor: C.amber })
}

function drawEndToEnd(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number) {
  const items = [
    ['Source', 'apps · DB · IoT', C.amber, 'source', 'event stream'],
    ['Ingest', 'Kafka / API', C.green3, 'stream', 'schema registry'],
    ['Store', 'lake · HDFS', C.violet2, 'storage', 'bronze layer'],
    ['Process', 'Spark · batch', C.greenTile, 'process', 'silver → gold'],
    ['Serve', 'BI · ML', C.blue, 'sink', 'API · dashboard'],
    ['Observe', 'log · quality', C.blueSoft, 'observe', 'SLA · lineage'],
  ] as const
  if (compactScene) {
    const nw = (w - 14) / 2
    const nh = 34
    const positions = [
      [x + 2, y + 8],
      [x + 2 + nw + 10, y + 8],
      [x + 2, y + 62],
      [x + 2 + nw + 10, y + 62],
      [x + 2, y + h - 44],
      [x + 2 + nw + 10, y + h - 44],
    ] as const
    items.forEach(([title, sub, color, kind, detail], i) => {
      const [nx, ny] = positions[i]
      drawNode(c, nx, ny, nw, nh, title, sub, color as string, kind, detail as string)
      if (i > 0) {
        const [px, py] = positions[i - 1]
        drawLink(c, [[px + nw / 2, py + nh / 2], [nx + nw / 2, ny + nh / 2]], t, {
          packets: 1,
          speed: 0.26,
          offset: i * 0.12,
          packetColor: color as string,
        })
      }
    })
    drawLink(c, [[x + 2 + nw / 2, y + h - 10], [x + 2 + nw / 2, y + 42], [x + 2, y + 42]], t, {
      color: C.rust,
      dashed: true,
      packets: 1,
      speed: 0.3,
      packetColor: C.rust,
    })
    return
  }
  const nw = (w - 5 * 8) / 6
  const nh = 72
  const ny = y + h / 2 - nh / 2
  items.forEach(([title, sub, color, kind, detail], i) => {
    const nx = x + i * (nw + 8)
    drawNode(c, nx, ny, nw, nh, title, sub, color as string, kind, detail as string)
    if (i > 0) {
      drawLink(c, [[nx - 8, ny + nh / 2], [nx, ny + nh / 2]], t, {
        packets: 2,
        speed: 0.3,
        offset: i * 0.14,
        packetColor: color as string,
      })
    }
  })
  drawLink(c, [[x + w - nw / 2, ny + nh], [x + w - nw / 2, y + h - 16], [x + nw / 2, y + h - 16], [x + nw / 2, ny + nh]], t, {
    color: C.rust,
    dashed: true,
    packets: 2,
    speed: 0.22,
    packetColor: C.rust,
  })
  drawTag(c, 'feedback · quality', x + w / 2 - 46, y + h - 23, C.rustSoft)
}

function drawDiagram(c: CanvasRenderingContext2D, stepIndex: number, t: number, x: number, y: number, w: number, h: number) {
  switch (stepIndex) {
    case 0:
      drawPillars5V(c, t, x, y, w, h)
      break
    case 1:
      drawIngestion(c, t, x, y, w, h)
      break
    case 2:
      drawStorage(c, t, x, y, w, h)
      break
    case 3:
      drawMapReduce(c, t, x, y, w, h)
      break
    case 4:
      drawSpark(c, t, x, y, w, h)
      break
    case 5:
      drawKafka(c, t, x, y, w, h)
      break
    case 6:
      drawLakehouse(c, t, x, y, w, h)
      break
    case 7:
      drawAirflow(c, t, x, y, w, h)
      break
    case 8:
      drawServing(c, t, x, y, w, h)
      break
    case 9:
      drawEndToEnd(c, t, x, y, w, h)
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
  txt(c, 'flow.view', x + 58, y + 24, 11, 800)
  txt(c, 'pipeline.flow · IFR229', x + w - 18, y + 24, 9.2, 600, C.muted, 'right')

  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 2.1
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.panelTitle.toUpperCase(), x + 26, y + 68, 9.5, 800, C.muted)
  txt(c, s.panelMetric, x + 26, y + 91, s.panelMetric.length > 24 ? 13.5 : 16, 800, C.ink)

  const ax = x + 26
  const ay = y + 108
  const aw = w - 52
  const ah = h - 132

  c.save()
  rr(c, x + 2, y + 44, w - 4, h - 46, 10)
  c.clip()
  drawDiagram(c, stepIndex, t, ax, ay, aw, ah)
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
  txt(c, 'flow.view', x + 48, y + 22, 10, 800)
  txt(c, 'pipeline.flow', x + w - 14, y + 22, 8.2, 600, C.muted, 'right')

  rr(c, x, y, w, h, r)
  c.strokeStyle = C.ink
  c.lineWidth = 1.9
  c.stroke()

  const s = steps[stepIndex]
  txt(c, s.panelTitle.toUpperCase(), x + 20, y + 56, 8, 800, C.muted)
  txt(c, s.panelMetric, x + 20, y + 77, s.panelMetric.length > 24 ? 11.5 : 13.5, 800, C.ink)

  const ax = x + 20
  const ay = y + 94
  const aw = w - 40
  const ah = h - 112

  c.save()
  rr(c, x + 2, y + 40, w - 4, h - 42, 9)
  c.clip()
  drawDiagram(c, stepIndex, t, ax, ay, aw, ah)
  c.restore()
}

function drawScene(c: CanvasRenderingContext2D, t: number, stepIndex: number) {
  drawBackdrop(c, t)
  drawDataPlatform(c, t, stepIndex)
  drawSceneFlow(c, t, stepIndex)
  drawEditorCard(c, t, stepIndex)
  drawStagePill(c, t, stepIndex)
  pill(c, `pipeline · ${stageLabel(stepIndex)}`, 64, 519, { size: 10.5, h: 30, dot: C.amber })
}

function drawCompactScene(c: CanvasRenderingContext2D, t: number, stepIndex: number, w: number, h: number) {
  drawCompactBackdrop(c, t, w, h)
  const pillW = Math.min(260, w - 24)
  drawStagePill(c, t, stepIndex, (w - pillW) / 2, 8, pillW, 36)
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
