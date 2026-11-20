<template>
  <div class="dv-root" :class="{ 'is-drawer': drawerOpen }">
    <header class="dv-topbar">
      <button class="dv-menu-btn" type="button" aria-label="Buka daftar tahap" :aria-expanded="drawerOpen" @click="drawerOpen = true">
        <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5.5h14M3 10h14M3 14.5h9" /></svg>
      </button>

      <a class="dv-brand" :href="withBase('/big-data/canvas-spark')" aria-label="Kanvas 3D Apache Spark & Optimasi ETL — mulai dari tahap pertama" @click.prevent="goTo(0)">
        <svg class="dv-logo" viewBox="0 0 34 34" aria-hidden="true">
          <rect x="2.4" y="5.5" width="29.2" height="23" rx="6" fill="#fbf7f1" stroke="#1d1b18" stroke-width="1.8" />
          <path d="M17 7.2 27 13l-10 5.8L7 13Z" fill="#b2d491" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
          <path d="M7 13v8l10 5.8V18.8Z" fill="#e7ddf5" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
          <path d="M27 13v8l-10 5.8V18.8Z" fill="#fcdcbd" stroke="#1d1b18" stroke-width="1.2" stroke-linejoin="round" />
        </svg>
        <span class="dv-brand__name">Kanvas <span>Spark</span></span>
        <span class="dv-brand__sub">Batch · Bagian 2</span>
      </a>

      <nav class="dv-nav" aria-label="Navigasi kanvas">
        <button class="dv-nav__item is-active" type="button">Belajar</button>
        <a class="dv-nav__item" :href="withBase('/big-data/')">Modul</a>
        <a class="dv-nav__item" :href="withBase('/presentasi/pertemuan-4-big-data')">Slide</a>
      </nav>

      <button class="dv-search" type="button" aria-label="Cari tahap dan konsep" :aria-expanded="searchOpen" @click="openSearch">
        <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
        <span class="dv-search__hint">Cari tahap &amp; konsep…</span>
        <kbd>⌘K</kbd>
      </button>

      <div class="dv-credit" role="note" title="Dosen Pengampu: Mahendar Dwi Payana, S.ST., M.T." aria-label="Dosen Pengampu: Mahendar Dwi Payana, S.ST., M.T.">
        <span class="dv-credit__x" aria-hidden="true">MDP</span>
        <span class="dv-credit__text"><small>Dosen Pengampu</small><b>Mahendar Dwi Payana, S.ST., M.T.</b></span>
      </div>
    </header>

    <div v-if="drawerOpen" class="dv-drawer-backdrop" @click="drawerOpen = false"></div>

    <div class="dv-body">
      <aside class="dv-sidebar" :class="{ 'is-open': drawerOpen }" aria-label="Daftar tahap">
        <div class="dv-tree-root">
          <svg class="dv-folder dv-folder--sand" viewBox="0 0 20 16" aria-hidden="true">
            <path class="dv-folder__back" d="M1.6 3.4c0-.8.6-1.4 1.4-1.4h5l1.6 1.8h7.4c.8 0 1.4.6 1.4 1.4v8.2c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V3.4Z" />
            <path class="dv-folder__front" d="M1.6 6.2h16.8v6.9c0 .8-.6 1.4-1.4 1.4H3c-.8 0-1.4-.6-1.4-1.4V6.2Z" />
          </svg>
          <span>Kurikulum</span>
          <span class="dv-tree-root__meta">{{ steps.length }} tahap</span>
          <button class="dv-drawer-close" type="button" aria-label="Tutup daftar tahap" @click="drawerOpen = false">
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
            <span>{{ current + 1 }} / {{ steps.length }} tahap</span>
            <span>{{ remainingLabel }}</span>
          </div>
        </div>
      </aside>

      <main class="dv-sheet">
        <div class="dv-lesson-head">
          <div class="dv-crumb">Big Data <span>/</span> Bagian 2 · Spark</div>
          <div class="dv-lesson-head__row">
            <div class="dv-title-wrap">
              <h1 class="dv-title dv-title--long">Dari Disk yang Lelah ke Memori yang Gesit</h1>
              <p class="dv-subtitle">Apache Spark dan optimasi ETL — dari I/O disk ke memori dan DAG.</p>
            </div>
            <div class="dv-tags">
              <span class="dv-tag dv-tag--sand">
                <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.6" /><path d="M8 4.8V8l2.2 1.4" /></svg>
                22 mnt
              </span>
              <span class="dv-tag dv-tag--mint">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 12.5V9.8h2.4v2.7ZM6.8 12.5V6.7h2.4v5.8ZM11.1 12.5V3.5h2.4v9Z" /></svg>
                Menengah
              </span>
              <span class="dv-tag dv-tag--violet">
                <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 4.5h10M3 8h10M3 11.5h6" /></svg>
                11 tahap
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
            <canvas ref="canvasEl" class="three-canvas" role="img" :aria-label="canvasLabel"></canvas>
          </div>

          <div class="three-caption" aria-hidden="true">
            <span class="three-caption__eyebrow">3D · TAHAP {{ current + 1 }} / {{ steps.length }}</span>
            <strong>{{ step.panelTitle }}</strong>
          </div>
          <div class="three-hint" aria-hidden="true">drag memutar · scroll zoom · double-click reset</div>

          <div v-if="threeLoading" class="three-loading">
            <span class="three-loader"></span>
            <span>Menyiapkan model 3D…</span>
          </div>
          <div v-if="threeError" class="three-fallback">{{ threeError }}</div>

          <div class="dv-stage__legend" aria-hidden="true">
            <span><i class="dv-lg dv-lg--data" style="background:#b7b1c2"></i> data mentah</span>
            <span><i class="dv-lg dv-lg--insight" style="background:#7fb4e3"></i> proses</span>
            <span><i class="dv-lg dv-lg--noise" style="background:#e6b94f"></i> hasil</span>
          </div>
        </div>

        <div class="dv-timeline">
          <div class="dv-timeline__head">
            <span class="dv-eyebrow">DI PELAJARAN INI</span>
            <span class="dv-timeline__count">Tahap {{ current + 1 }} dari {{ steps.length }}</span>
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

        <p class="dv-footnote">Model 3D low-poly untuk memperjelas alur Spark ETL. Warna: data mentah (abu), proses (biru), hasil (emas), bahaya (merah-oranye). Drag memutar, scroll zoom, double-click reset.</p>
        <p class="dv-sr-only" aria-live="polite">Tahap {{ current + 1 }} dari {{ steps.length }}: {{ step.title }}. {{ step.short }}.</p>
      </main>

      <aside class="dv-rail" aria-label="Penjelasan tahap">
        <section class="dv-card dv-guide">
          <div class="dv-guide__meta">
            <span class="dv-eyebrow">TAHAP {{ current + 1 }} / {{ steps.length }}</span>
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
            <kbd>←</kbd><kbd>→</kbd> tahap <span>·</span> <kbd>R</kbd> putar ulang <span>·</span> <kbd>Space</kbd> jeda
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
        <div class="dv-palette__dialog" role="dialog" aria-modal="true" aria-label="Cari tahap dan konsep">
          <div class="dv-palette__bar">
            <svg viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.8" cy="7.8" r="4.7" /><path d="m11.4 11.4 3.8 3.8" /></svg>
            <input ref="searchInput" v-model="searchQuery" class="dv-palette__input" type="search" placeholder="Cari tahap, konsep, atau kata kunci…" @keydown.enter="goToResult(0)" />
            <button class="dv-palette__esc" type="button" @click="closeSearch">esc</button>
          </div>
          <div class="dv-palette__list">
            <div class="dv-palette__group">
              <span>{{ searchQuery ? 'HASIL PENCARIAN' : 'SEMUA TAHAP' }}</span>
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
              <span>Coba “catalyst”, “shuffle”, atau “broadcast”.</span>
            </div>
          </div>
          <div class="dv-palette__foot">
            <span><kbd>↵</kbd> buka</span>
            <span><kbd>esc</kbd> tutup</span>
            <span class="dv-palette__count">{{ steps.length }} tahap</span>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import { createClayKit, CLAY } from './three/clay-kit'

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
  dataCount: string
  linkCount: string
  focus: string
}

interface Goal {
  text: string
  at: number
}

const steps: Step[] = [
  {
    id: 'problem',
    short: 'Disk',
    title: 'Disk yang lelah bolak-balik',
    phase: 'MASALAH',
    tone: 'red',
    body: `<p>MapReduce menulis hasil antar-fase ke HDFS. Untuk ML iteratif atau ETL multi-tahap, pola <b>fase → HDFS → fase</b> membuat disk dan jaringan bekerja jauh lebih keras dari yang diperlukan.</p><p>Semakin banyak iterasi, semakin mahal I/O perantara.</p>`,
    idea: `Bottleneck Spark bukan selalu CPU; sering kali ia adalah disk dan jaringan yang menunggu.`,
    panelTitle: 'Masalah MapReduce',
    panelMetric: 'fase ↔ HDFS',
    nodeCount: '2',
    dataCount: '2',
    linkCount: '2',
    focus: 'disk I/O',
  },
  {
    id: 'memory',
    short: 'Memori',
    title: 'Data tinggal di memori',
    phase: 'SPARK',
    tone: 'green',
    body: `<p>Spark menyimpan data antar-transformasi di memori dan menyusun pekerjaan sebagai DAG. Hasil antara tidak harus selalu ditulis ke HDFS.</p><p>In-memory, lazy evaluation, dan unified engine mempercepat iterasi.</p>`,
    idea: `Spark cepat karena mengurangi perjalanan ke disk — bukan karena satu mesin menjadi ajaib.`,
    panelTitle: 'Spark hadir',
    panelMetric: 'in-memory · DAG',
    nodeCount: '1',
    dataCount: '4',
    linkCount: '1',
    focus: 'memori',
  },
  {
    id: 'architecture',
    short: 'Cluster',
    title: 'Driver mengatur, executor bekerja',
    phase: 'ARSITEKTUR',
    tone: 'blue',
    body: `<p><b>Driver</b> membuat SparkSession, menyusun DAG, dan mengirim task. <b>Cluster Manager</b> menyediakan executor; setiap <b>executor</b> menjalankan task dan menyimpan cache.</p><p>YARN, Kubernetes, dan Standalone dapat menjadi cluster manager.</p>`,
    idea: `Driver adalah komandan; executor adalah pekerja. Keduanya perlu sumber daya yang seimbang.`,
    panelTitle: 'Arsitektur Spark',
    panelMetric: 'driver → executor',
    nodeCount: '5',
    dataCount: '3',
    linkCount: '4',
    focus: 'cluster',
  },
  {
    id: 'dag',
    short: 'DAG',
    title: 'Transformasi diam, aksi menyalakan',
    phase: 'LAZY & DAG',
    tone: 'violet',
    body: `<p><code>select</code>, <code>filter</code>, dan <code>groupBy</code> bersifat <b>lazy</b>. Spark hanya menyusun rencana. Job baru berjalan saat sebuah <b>aksi</b> seperti <code>show()</code> atau <code>write()</code> dipanggil.</p><p>Lazy evaluation memberi optimizer ruang untuk memperbaiki rencana.</p>`,
    idea: `Transformasi adalah cetak biru; aksi adalah tombol eksekusi.`,
    panelTitle: 'Lazy & DAG',
    panelMetric: 'plan → action',
    nodeCount: '4',
    dataCount: '0',
    linkCount: '3',
    focus: 'lazy',
  },
  {
    id: 'catalyst',
    short: 'Catalyst',
    title: 'Optimizer memilah sebelum eksekusi',
    phase: 'OPTIMIZER',
    tone: 'amber',
    body: `<p><b>Catalyst</b> melewati analysis, logical optimization, physical planning, dan code generation. <b>Tungsten</b> menangani memori dan code generation agar eksekusi lebih efisien.</p><p>Predicate pushdown, column pruning, dan pemilihan join strategy terjadi sebelum data dibaca.</p>`,
    idea: `Rencana yang baik mengurangi data yang dibaca, bukan hanya mempercepat CPU.`,
    panelTitle: 'Catalyst & Tungsten',
    panelMetric: 'analysis → codegen',
    nodeCount: '5',
    dataCount: '0',
    linkCount: '4',
    focus: 'optimizer',
  },
  {
    id: 'narrowwide',
    short: 'Shuffle',
    title: 'Garis lurus vs pipa bersilang',
    phase: 'NARROW vs WIDE',
    tone: 'red',
    body: `<p><b>Narrow transformation</b> tidak memindahkan data antar-partisi; <b>wide transformation</b> membutuhkan shuffle. Shuffle adalah batas stage dan sumber biaya terbesar.</p><p>Setiap <code>groupBy</code>, <code>join</code>, atau <code>repartition</code> berpotensi memicu wide dependency.</p>`,
    idea: `Kurangi shuffle sebelum mengubah konfigurasi cluster; menambah mesin tidak menghilangkan biaya jaringan.`,
    panelTitle: 'Narrow vs wide',
    panelMetric: 'shuffle = stage boundary',
    nodeCount: '2',
    dataCount: '0',
    linkCount: '3',
    focus: 'shuffle',
  },
  {
    id: 'bronze',
    short: 'Silver',
    title: 'Bronze melewati saringan kualitas',
    phase: 'BRONZE → SILVER',
    tone: 'amber',
    body: `<p>JSON mentah masuk ke bronze. Sebelum menjadi silver, data melewati pemeriksaan null, tipe, nilai negatif, dan duplikat. Output ditulis sebagai Parquet dan dipartisi berdasarkan <code>dt</code>.</p><p>Saringan kualitas menjaga lapisan berikutnya tetap dapat dipercaya.</p>`,
    idea: `Data mentah boleh kotor; data yang dipakai untuk keputusan tidak boleh.`,
    panelTitle: 'Bronze → Silver',
    panelMetric: 'JSON → Parquet',
    nodeCount: '3',
    dataCount: '3',
    linkCount: '4',
    focus: 'quality',
  },
  {
    id: 'gold',
    short: 'Gold',
    title: 'Broadcast kecil, hasilkan emas',
    phase: 'SILVER → GOLD',
    tone: 'green',
    body: `<p>Tabel produk yang kecil dapat di-<b>broadcast</b> ke semua executor agar join tidak memicu shuffle besar. Data silver lalu diagregasi menjadi revenue dan conversion rate di lapisan gold.</p><p>Broadcast adalah strategi, bukan mantra: ukuran tabel harus benar-benar kecil.</p>`,
    idea: `Broadcast join menghindari shuffle dengan menyalin tabel kecil ke setiap executor.`,
    panelTitle: 'Silver → Gold',
    panelMetric: 'broadcast · revenue',
    nodeCount: '4',
    dataCount: '3',
    linkCount: '4',
    focus: 'broadcast',
  },
  {
    id: 'tuning',
    short: 'Tuning',
    title: 'Dari 200 partisi kosong ke 8 terisi',
    phase: 'TUNING',
    tone: 'blue',
    body: `<p><code>spark.sql.shuffle.partitions</code> yang terlalu besar menghasilkan banyak partisi kecil dan task overhead. <code>repartition</code> menambah partisi; <code>coalesce</code> menggabungkannya. AQE dapat menggabungkan partisi secara otomatis.</p><p>Target praktis: sekitar 100–200 MB data per partisi.</p>`,
    idea: `Partisi yang tepat membuat setiap task punya pekerjaan yang seimbang.`,
    panelTitle: 'Tuning partisi',
    panelMetric: '200 → 8 partisi',
    nodeCount: '2',
    dataCount: '14',
    linkCount: '1',
    focus: 'partisi',
  },
  {
    id: 'skewfiles',
    short: 'Skew',
    title: 'Raksasa dipecah, kecil dipres',
    phase: 'SKEW & FILES',
    tone: 'red',
    body: `<p>AQE skew join memecah partisi raksasa; salting menyebar key panas. Di sisi output, jutaan file kecil dipres menjadi beberapa file besar dengan target 128 MB–1 GB.</p><p>Skew dan small files sama-sama menyerang efisiensi, tetapi dari dua arah berbeda.</p>`,
    idea: `Satu partisi raksasa dan sejuta file kecil adalah dua bentuk masalah distribusi yang sama.`,
    panelTitle: 'Skew & small files',
    panelMetric: 'AQE · salting · compaction',
    nodeCount: '4',
    dataCount: '7',
    linkCount: '2',
    focus: 'skew',
  },
  {
    id: 'release',
    short: 'Rilis',
    title: 'Uji, ukur, lalu rilis',
    phase: 'UJI & RILIS',
    tone: 'green',
    body: `<p>Pipeline yang baik diuji dengan pytest dan CI, memakai fungsi murni yang mudah diuji. Bukti tuning disimpan sebagai metrik; output gold diverifikasi sebelum dirilis.</p><p>Rilis bukan akhir, melainkan awal observabilitas produksi.</p>`,
    idea: `Tanpa pengujian dan metrik, “tuning” hanyalah tebakan yang mahal.`,
    panelTitle: 'Uji & rilis',
    panelMetric: 'pytest · CI · gold',
    nodeCount: '3',
    dataCount: '3',
    linkCount: '2',
    focus: 'release',
  },
]

const goals: Goal[] = [
  { text: 'Menjelaskan masalah I/O MapReduce', at: 1 },
  { text: 'Membedakan lazy transformation dan action', at: 4 },
  { text: 'Membaca Catalyst & narrow/wide', at: 6 },
  { text: 'Menerapkan medallion dan broadcast join', at: 8 },
  { text: 'Melakukan tuning partisi, skew, dan rilis', at: 11 },
]

const moduleDefs = [
  { id: 'm1', title: '01. Masalah & memori', color: 'sand', items: [0, 1] },
  { id: 'm2', title: '02. Arsitektur & optimizer', color: 'blue', items: [2, 3, 4] },
  { id: 'm3', title: '03. Shuffle & medallion', color: 'green', items: [5, 6, 7] },
  { id: 'm4', title: '04. Tuning & rilis', color: 'violet', items: [8, 9, 10] },
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
const canvasLabel = computed(() => `Tahap ${current.value + 1}: ${step.value.title}. ${step.value.panelTitle}, ${step.value.panelMetric}.`)

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
      label: 'NODE',
      value: s.nodeCount,
      level: 'good',
      path: 'M8 2.2 13 5v6l-5 2.8L3 11V5z M3 5l5 2.8L13 5M8 7.8v6',
    },
    {
      label: 'BLOK DATA',
      value: s.dataCount,
      level: s.dataCount === '0' ? '' : 'good',
      path: 'M4 4h8v8H4z M4 8h8M8 4v8',
    },
    {
      label: 'KONEKSI',
      value: s.linkCount,
      level: 'good',
      path: 'M3 5.5h4M9 10.5h4M7 5.5l4 5',
    },
    {
      label: 'FOKUS',
      value: s.focus,
      level: 'warn',
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

const COLORS = {
  ink: 0x1d1b18,
  ink2: 0x34302b,
  muted: 0x6f6961,
  paper: 0xf4ebe0,
  cream: 0xfbf7f1,
  green: 0xcfe3b2,
  green2: 0xb2d491,
  green3: 0x7fc278,
  greenTile: 0xe8efd9,
  violet: 0xe7ddf5,
  violet2: 0xb79ce6,
  amber: 0xefb041,
  amberSoft: 0xfbe5bd,
  orange: 0xfcdcbd,
  rust: 0xd0683a,
  blue: 0x2f86ce,
  blueSoft: 0xd6e5f6,
  mint: 0xdff0de,
}

const threeLoading = ref(true)
const threeError = ref('')
let THREE: any = null
let renderer: any = null
let scene: any = null
let camera: any = null
let stageGroup: any = null
let kit: any = null
let clock: any = null
let raf = 0
let elapsed = 0
let stageStart = 0
let threeReady = false
let nodes: any[] = []
let packets: any[] = []
let resizeObserver: ResizeObserver | null = null
let threePromise: Promise<any> | null = null

const cameraState = {
  yaw: 0,
  pitch: 0.52,
  radius: 13.5,
  baseRadius: 13.5,
  target: { x: 0, y: -1.5, z: 0 },
}
const pointer = { down: false, x: 0, y: 0 }
const STAGE_EXTENT = [3.4, 2.8, 4.2, 3.8, 3.9, 4.2, 3.8, 4.4, 4.2, 4.2, 3.6]

function fitCamera(index: number) {
  if (!camera || !THREE) return
  const aspect = camera.aspect || 1.7
  const extent = STAGE_EXTENT[index] ?? 4
  const fov = THREE.MathUtils.degToRad(31 / 2)
  const base = Math.max(10, (extent + 0.55) / (Math.tan(fov) * aspect))
  cameraState.baseRadius = base
  cameraState.radius = base
  updateCamera()
}

function loadThree() {
  const win = window as any
  if (win.THREE) return Promise.resolve(win.THREE)
  if (!threePromise) {
    threePromise = new Promise((resolve, reject) => {
      const script = document.createElement('script')
      script.src = withBase('/vendor/three.min.js')
      script.async = true
      script.onload = () => resolve((window as any).THREE)
      script.onerror = () => reject(new Error('Three.js gagal dimuat'))
      document.head.appendChild(script)
    })
  }
  return threePromise
}

function v3(x: number, y: number, z: number) {
  return new THREE.Vector3(x, y, z)
}

function clampValue(value: number, min: number, max: number) {
  return Math.max(min, Math.min(max, value))
}

function easeOutCubic(value: number) {
  const t = clampValue(value, 0, 1)
  return 1 - Math.pow(1 - t, 3)
}

function updateCamera() {
  if (!camera) return
  const { yaw, pitch, radius, target } = cameraState
  camera.position.set(
    target.x + radius * Math.sin(yaw) * Math.cos(pitch),
    target.y + radius * Math.sin(pitch),
    target.z + radius * Math.cos(yaw) * Math.cos(pitch),
  )
  camera.lookAt(target.x, target.y, target.z)
}

function resizeRenderer() {
  if (!renderer || !camera) return
  const wrap = canvasWrap.value
  if (!wrap) return
  const rect = wrap.getBoundingClientRect()
  if (rect.width < 2 || rect.height < 2) return
  renderer.setSize(rect.width, rect.height, false)
  camera.aspect = rect.width / rect.height
  camera.updateProjectionMatrix()
  fitCamera(current.value)
  renderer.render(scene, camera)
}

function initThree() {
  const canvas = canvasEl.value
  if (!canvas) throw new Error('Canvas tidak ditemukan')
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' })
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1))
  renderer.setClearColor(0x000000, 0)
  renderer.outputEncoding = THREE.sRGBEncoding
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap

  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(31, 1, 0.1, 120)
  cameraState.radius = 13.5
  cameraState.baseRadius = 13.5
  updateCamera()

  scene.add(new THREE.AmbientLight(0xffffff, 0.78))
  const key = new THREE.DirectionalLight(0xfff3df, 0.82)
  key.position.set(5, 9, 7)
  key.castShadow = true
  key.shadow.mapSize.width = 1024
  key.shadow.mapSize.height = 1024
  key.shadow.camera.left = -10
  key.shadow.camera.right = 10
  key.shadow.camera.top = 10
  key.shadow.camera.bottom = -10
  key.shadow.camera.near = 1
  key.shadow.camera.far = 30
  scene.add(key)
  const fill = new THREE.DirectionalLight(0xcbd8ff, 0.32)
  fill.position.set(-7, 4, 6)
  scene.add(fill)
  const rim = new THREE.DirectionalLight(0xffe6c4, 0.2)
  rim.position.set(0, 5, -7)
  scene.add(rim)

  const shadowPlane = new THREE.Mesh(
    new THREE.PlaneGeometry(30, 30),
    new THREE.ShadowMaterial({ color: COLORS.ink, opacity: 0.12 }),
  )
  shadowPlane.rotation.x = -Math.PI / 2
  shadowPlane.position.y = -2.9
  shadowPlane.receiveShadow = true
  scene.add(shadowPlane)

  const grid = new THREE.GridHelper(28, 28, 0xc6bbac, 0xddd3c5)
  grid.position.y = -2.89
  const gridMat = grid.material as any
  gridMat.transparent = true
  gridMat.opacity = 0.72
  scene.add(grid)

  const dustGeo = new THREE.BufferGeometry()
  const dustPositions: number[] = []
  for (let i = 0; i < 70; i++) {
    dustPositions.push((Math.random() - 0.5) * 18, Math.random() * 5 - 2.4, (Math.random() - 0.5) * 8 - 1)
  }
  dustGeo.setAttribute('position', new THREE.Float32BufferAttribute(dustPositions, 3))
  const dust = new THREE.Points(
    dustGeo,
    new THREE.PointsMaterial({ color: COLORS.green2, size: 0.035, transparent: true, opacity: 0.45 }),
  )
  scene.add(dust)

  stageGroup = new THREE.Group()
  scene.add(stageGroup)
  kit = createClayKit({ THREE, stageGroup, nodes, label: makeSpriteLabel, beam: makeBeam })

  resizeObserver = new ResizeObserver(() => resizeRenderer())
  if (canvasWrap.value) resizeObserver.observe(canvasWrap.value)
  resizeRenderer()

  canvas.addEventListener('pointerdown', onPointerDown)
  canvas.addEventListener('pointermove', onPointerMove)
  canvas.addEventListener('pointerup', onPointerUp)
  canvas.addEventListener('pointercancel', onPointerUp)
  canvas.addEventListener('wheel', onWheel, { passive: false })
  canvas.addEventListener('dblclick', resetView)
}

function disposeObject(object: any) {
  object.traverse((child: any) => {
    if (child.geometry) child.geometry.dispose()
    if (child.material) {
      const mats = Array.isArray(child.material) ? child.material : [child.material]
      mats.forEach((mat: any) => {
        if (mat.map) mat.map.dispose()
        mat.dispose()
      })
    }
  })
}

function clearStage() {
  if (!stageGroup) return
  for (const child of [...stageGroup.children]) {
    stageGroup.remove(child)
    disposeObject(child)
  }
  nodes = []
  packets = []
}

function makeServer(opts: {
  x: number
  y?: number
  z?: number
  title: string
  accent?: number
  height?: number
  slots?: number
  failed?: boolean
  active?: boolean
  label?: boolean
  labelScale?: number
}) {
  const group = new THREE.Group()
  const baseY = opts.y ?? -2.85
  const h = opts.height ?? 1.6
  const w = 0.95
  const d = 0.72
  group.position.set(opts.x, baseY, opts.z ?? 0)
  group.userData.baseY = baseY
  group.userData.noBob = true

  const bodyColor = opts.failed ? 0x5a2b28 : COLORS.ink2
  const body = new THREE.Mesh(
    new THREE.BoxGeometry(w, h, d),
    new THREE.MeshStandardMaterial({ color: bodyColor, roughness: 0.82, metalness: 0.08 }),
  )
  body.position.y = h / 2
  body.castShadow = true
  body.receiveShadow = true
  group.add(body)

  const panel = new THREE.Mesh(
    new THREE.BoxGeometry(w * 0.82, h * 0.78, 0.035),
    new THREE.MeshStandardMaterial({ color: opts.failed ? 0xebbcb3 : COLORS.cream, roughness: 0.9 }),
  )
  panel.position.set(0, h / 2, d / 2 + 0.02)
  group.add(panel)

  const edge = new THREE.LineSegments(
    new THREE.EdgesGeometry(new THREE.BoxGeometry(w, h, d)),
    new THREE.LineBasicMaterial({ color: COLORS.ink, transparent: true, opacity: 0.85 }),
  )
  edge.position.y = h / 2
  group.add(edge)

  fillServerSlots(group, h, w, d, opts.slots ?? 4, opts.failed ? COLORS.rust : opts.accent ?? COLORS.green2, opts.failed)

  const top = new THREE.Mesh(
    new THREE.BoxGeometry(w * 0.9, 0.06, d * 0.9),
    new THREE.MeshBasicMaterial({ color: opts.failed ? COLORS.rust : opts.accent ?? COLORS.green2 }),
  )
  top.position.set(0, h + 0.03, 0)
  group.add(top)

  if (opts.label !== false) {
    const label = makeSpriteLabel(opts.title, opts.failed ? 0xf8d5cf : opts.active ? COLORS.greenTile : COLORS.cream, opts.failed ? 0x8f2a22 : COLORS.ink2)
    if (label) {
      label.position.set(0, h + 0.45, 0)
      label.scale.set(opts.labelScale ?? 1.75, 0.43, 1)
      group.add(label)
    }
  }
  if (opts.failed) {
    const fail = makeSpriteLabel('FAILED', 0xf8d5cf, 0x8f2a22)
    if (fail) {
      fail.position.set(0, h + 0.95, 0.2)
      fail.scale.set(1.6, 0.4, 1)
      group.add(fail)
    }
  }
  stageGroup.add(group)
  return group
}

function fillServerSlots(group: any, h: number, w: number, d: number, slots: number, ledColor: number, failed?: boolean) {
  const usable = h * 0.62
  const slotH = 0.07
  for (let i = 0; i < slots; i++) {
    const y = h * 0.27 + (usable / slots) * i
    const slot = new THREE.Mesh(
      new THREE.BoxGeometry(w * 0.6, slotH, 0.02),
      new THREE.MeshBasicMaterial({ color: 0x1d1b18 }),
    )
    slot.position.set(-w * 0.08, y, d / 2 + 0.045)
    group.add(slot)
    const led = new THREE.Mesh(
      new THREE.BoxGeometry(0.055, 0.055, 0.02),
      new THREE.MeshBasicMaterial({ color: failed && i === 1 ? COLORS.rust : ledColor }),
    )
    led.position.set(w * 0.32, y, d / 2 + 0.055)
    group.add(led)
  }
}

function makeDisk(opts: { x: number; y?: number; z?: number; title?: string; accent?: number; scale?: number }) {
  const group = new THREE.Group()
  const baseY = opts.y ?? -2.85
  group.position.set(opts.x, baseY, opts.z ?? 0)
  group.userData.noBob = true
  const base = new THREE.Mesh(
    new THREE.BoxGeometry(1.0, 0.22, 0.9),
    new THREE.MeshStandardMaterial({ color: COLORS.ink2, roughness: 0.85 }),
  )
  base.position.y = 0.11
  base.castShadow = true
  base.receiveShadow = true
  group.add(base)
  const platter = new THREE.Mesh(
    new THREE.CylinderGeometry(0.36, 0.36, 0.07, 28),
    new THREE.MeshStandardMaterial({ color: 0xc6bbac, roughness: 0.32, metalness: 0.55 }),
  )
  platter.position.y = 0.27
  platter.castShadow = true
  group.add(platter)
  const spindle = new THREE.Mesh(
    new THREE.CylinderGeometry(0.065, 0.065, 0.1, 16),
    new THREE.MeshStandardMaterial({ color: COLORS.ink, roughness: 0.6 }),
  )
  spindle.position.y = 0.32
  group.add(spindle)
  const arm = new THREE.Mesh(
    new THREE.BoxGeometry(0.48, 0.035, 0.055),
    new THREE.MeshStandardMaterial({ color: COLORS.ink, roughness: 0.5 }),
  )
  arm.position.set(0.16, 0.34, 0)
  arm.rotation.z = -0.12
  group.add(arm)
  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(0.36, 0.018, 8, 32),
    new THREE.MeshBasicMaterial({ color: opts.accent ?? COLORS.amber }),
  )
  ring.rotation.x = Math.PI / 2
  ring.position.y = 0.31
  group.add(ring)
  if (opts.title) {
    const label = makeSpriteLabel(opts.title, COLORS.ink, COLORS.cream)
    if (label) {
      label.position.set(0, 0.85, 0)
      label.scale.set(1.45, 0.36, 1)
      group.add(label)
    }
  }
  if (opts.scale) group.scale.setScalar(opts.scale)
  stageGroup.add(group)
  return group
}

function makeBlock(opts: { x: number; y: number; z?: number; size?: number; color: number; label?: string; bob?: boolean }) {
  const size = opts.size ?? 0.34
  const group = new THREE.Group()
  group.position.set(opts.x, opts.y, opts.z ?? 0)
  group.userData.baseY = opts.y
  group.userData.phase = Math.random() * Math.PI * 2
  const cube = new THREE.Mesh(
    new THREE.BoxGeometry(size, size, size),
    new THREE.MeshStandardMaterial({ color: opts.color, roughness: 0.62, metalness: 0.05 }),
  )
  cube.castShadow = true
  cube.receiveShadow = true
  group.add(cube)
  const edges = new THREE.LineSegments(
    new THREE.EdgesGeometry(new THREE.BoxGeometry(size, size, size)),
    new THREE.LineBasicMaterial({ color: COLORS.ink, transparent: true, opacity: 0.8 }),
  )
  group.add(edges)
  if (opts.label) {
    const label = makeSpriteLabel(opts.label, COLORS.cream, COLORS.ink2)
    if (label) {
      label.position.set(0, size * 0.9, 0)
      label.scale.set(1.0, 0.25, 1)
      group.add(label)
    }
  }
  stageGroup.add(group)
  if (opts.bob !== false) nodes.push(group)
  return group
}

function makeBucket(opts: { x: number; y?: number; z?: number; title?: string; accent?: number }) {
  const group = new THREE.Group()
  const baseY = opts.y ?? -2.85
  group.position.set(opts.x, baseY, opts.z ?? 0)
  group.userData.noBob = true
  const bucket = new THREE.Mesh(
    new THREE.CylinderGeometry(0.9, 0.68, 1.15, 28, 1, true),
    new THREE.MeshStandardMaterial({
      color: opts.accent ?? COLORS.amberSoft,
      roughness: 0.8,
      metalness: 0.05,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.92,
    }),
  )
  bucket.position.y = 0.58
  bucket.castShadow = true
  group.add(bucket)
  const bottom = new THREE.Mesh(
    new THREE.CylinderGeometry(0.68, 0.68, 0.06, 28),
    new THREE.MeshStandardMaterial({ color: opts.accent ?? COLORS.amber, roughness: 0.8 }),
  )
  bottom.position.y = 0.03
  group.add(bottom)
  const rim = new THREE.Mesh(
    new THREE.TorusGeometry(0.9, 0.035, 8, 36),
    new THREE.MeshBasicMaterial({ color: COLORS.ink }),
  )
  rim.rotation.x = Math.PI / 2
  rim.position.y = 1.15
  group.add(rim)
  if (opts.title) {
    const label = makeSpriteLabel(opts.title, COLORS.cream, COLORS.ink2)
    if (label) {
      label.position.set(0, 1.55, 0)
      label.scale.set(2.35, 0.46, 1)
      group.add(label)
    }
  }
  stageGroup.add(group)
  return group
}

function makeWall() {
  const wall = new THREE.Mesh(
    new THREE.BoxGeometry(0.06, 2.5, 4.2),
    new THREE.MeshBasicMaterial({ color: COLORS.rust, transparent: true, opacity: 0.16, side: THREE.DoubleSide }),
  )
  wall.position.set(0, -1.4, 0)
  stageGroup.add(wall)
  const line = new THREE.Mesh(
    new THREE.BoxGeometry(0.02, 2.6, 0.035),
    new THREE.MeshBasicMaterial({ color: COLORS.rust }),
  )
  line.position.set(0, -1.4, 0)
  stageGroup.add(line)
  const label = makeSpriteLabel('NETWORK PARTITION', 0xf8d5cf, 0x8f2a22)
  if (label) {
    label.position.set(0, 0.45, 0.3)
    label.scale.set(2.6, 0.48, 1)
    stageGroup.add(label)
  }
}

function makeSource(opts: { x: number; z?: number; title?: string }) {
  const group = new THREE.Group()
  group.position.set(opts.x, -2.85, opts.z ?? 0)
  group.userData.noBob = true
  const base = new THREE.Mesh(
    new THREE.BoxGeometry(1.25, 0.16, 0.9),
    new THREE.MeshStandardMaterial({ color: COLORS.ink2, roughness: 0.8 }),
  )
  base.position.y = 0.08
  base.castShadow = true
  group.add(base)
  ;[COLORS.amber, COLORS.blue, COLORS.violet2].forEach((color, i) => {
    const cube = new THREE.Mesh(
      new THREE.BoxGeometry(0.3, 0.3, 0.3),
      new THREE.MeshStandardMaterial({ color, roughness: 0.6 }),
    )
    cube.position.set(-0.32 + i * 0.32, 0.34, 0)
    cube.castShadow = true
    group.add(cube)
  })
  if (opts.title) {
    const label = makeSpriteLabel(opts.title, COLORS.cream, COLORS.ink2)
    if (label) {
      label.position.set(0, 0.95, 0)
      label.scale.set(1.6, 0.36, 1)
      group.add(label)
    }
  }
  stageGroup.add(group)
  return group
}

function makeSpriteLabel(text: string, color = COLORS.cream, textColor = COLORS.ink2) {
  const canvas = document.createElement('canvas')
  canvas.width = 420
  canvas.height = 104
  const ctx = canvas.getContext('2d')
  if (!ctx) return null
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  const fill = `#${color.toString(16).padStart(6, '0')}`
  const ink = `#${textColor.toString(16).padStart(6, '0')}`
  ctx.beginPath()
  const x = 10
  const y = 18
  const w = 400
  const h = 68
  const r = 34
  ctx.moveTo(x + r, y)
  ctx.arcTo(x + w, y, x + w, y + h, r)
  ctx.arcTo(x + w, y + h, x, y + h, r)
  ctx.arcTo(x, y + h, x, y, r)
  ctx.arcTo(x, y, x + w, y, r)
  ctx.closePath()
  ctx.fillStyle = fill
  ctx.fill()
  ctx.lineWidth = 3
  ctx.strokeStyle = '#1d1b18'
  ctx.stroke()
  ctx.fillStyle = ink
  ctx.font = "800 27px 'JetBrains Mono', ui-monospace, monospace"
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(text, 210, 53)
  const texture = new THREE.CanvasTexture(canvas)
  texture.encoding = THREE.sRGBEncoding
  texture.minFilter = THREE.LinearFilter
  const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: texture, transparent: true, depthTest: false }))
  sprite.scale.set(2.1, 0.52, 1)
  sprite.renderOrder = 20
  return sprite
}

function makeBeam(
  start: any,
  end: any,
  options: {
    color?: number
    dashed?: boolean
    packets?: number
    packetColor?: number
    mid?: any
    label?: string
    labelColor?: number
    speed?: number
    offset?: number
    arrow?: boolean
  } = {},
) {
  const mid = options.mid ?? v3((start.x + end.x) / 2, Math.max(start.y, end.y) + 0.45, Math.min(start.z, end.z) - 0.25)
  const curve = new THREE.QuadraticBezierCurve3(start, mid, end)
  const geometry = new THREE.BufferGeometry().setFromPoints(curve.getPoints(52))
  const material = options.dashed
    ? new THREE.LineDashedMaterial({
        color: options.color ?? COLORS.ink2,
        dashSize: 0.14,
        gapSize: 0.1,
        transparent: true,
        opacity: 0.8,
      })
    : new THREE.LineBasicMaterial({ color: options.color ?? COLORS.ink2, transparent: true, opacity: 0.78 })
  const line = new THREE.Line(geometry, material)
  if (options.dashed) line.computeLineDistances()
  line.position.z = -0.12
  stageGroup.add(line)

  if (options.arrow !== false) {
    const tangent = curve.getTangent(1).normalize()
    const arrow = new THREE.Mesh(
      new THREE.ConeGeometry(0.075, 0.22, 8),
      new THREE.MeshBasicMaterial({ color: options.color ?? COLORS.ink2 }),
    )
    arrow.position.copy(end)
    arrow.position.z = -0.1
    arrow.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), tangent)
    stageGroup.add(arrow)
  }

  const count = options.packets ?? 2
  const packetColor = options.packetColor ?? COLORS.green2
  for (let i = 0; i < count; i++) {
    const mesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.058, 8, 8),
      new THREE.MeshBasicMaterial({ color: packetColor }),
    )
    stageGroup.add(mesh)
    packets.push({
      mesh,
      curve,
      speed: options.speed ?? 0.24,
      offset: (options.offset ?? 0) + i / count,
    })
  }

  if (options.label) {
    const sprite = makeSpriteLabel(options.label, options.labelColor ?? COLORS.cream)
    if (sprite) {
      const p = curve.getPoint(0.5)
      sprite.position.set(p.x, p.y + 0.16, 0.35)
      stageGroup.add(sprite)
    }
  }
  return curve
}

function badge(text: string, x: number, y: number, z = 0, fill = CLAY.cream, scale = 2.0) {
  if (!kit) return
  const sprite = kit.label(text, fill, CLAY.ink)
  if (!sprite) return
  sprite.position.set(x, y, z)
  sprite.scale.set(scale, 0.46, 1)
  stageGroup.add(sprite)
}

function buildStage(index: number) {
  if (!stageGroup || !kit) return
  clearStage()
  stageStart = elapsed

  switch (index) {
    case 0: {
      kit.disk({ x: -2.7, y: -2.85, z: 0, title: 'Fase 1', color: CLAY.raw, tired: true })
      kit.disk({ x: 2.7, y: -2.85, z: 0, title: 'Fase 2', color: CLAY.raw, tired: true })
      kit.beam(v3(-1.8, -1.4, 0), v3(1.8, -1.4, 0), { color: CLAY.danger, dashed: true, packets: 2, packetColor: CLAY.danger, label: 'tulis HDFS' })
      kit.beam(v3(1.8, -2.1, 0), v3(-1.8, -2.1, 0), { color: CLAY.danger, dashed: true, packets: 2, packetColor: CLAY.raw, offset: 0.4 })
      badge('I/O antar-fase mahal', 0, 0.75, 0.4, CLAY.redSoft, 3.0)
      break
    }
    case 1: {
      kit.chip({ x: 0, y: -2.85, z: 0, title: 'SPARK · in-memory' })
      for (let i = 0; i < 4; i++) {
        kit.block({ x: -1.2 + i * 0.8, y: -0.7 + (i % 2) * 0.25, z: 0.3, size: 0.28, color: [CLAY.raw, CLAY.process, CLAY.output, CLAY.violet][i] })
      }
      break
    }
    case 2: {
      kit.tower({ x: -3.2, y: -2.85, z: 0, title: 'Driver', color: CLAY.process, height: 1.8 })
      ;[0, 1.6, 3.2].forEach((x, i) => {
        kit.server({ x, y: -2.85, z: 0.2, title: `Executor ${i + 1}`, height: 1.4, slots: 3, color: CLAY.inkSoft, active: i === 1 })
        kit.beam(v3(-2.6, -1.5, 0), v3(x, -1.5, 0.2), { color: CLAY.inkSoft, dashed: true, packets: 2, packetColor: CLAY.process, offset: i * 0.15 })
      })
      badge('YARN / K8s / Standalone', 0, 0.7, 0.4, CLAY.blueSoft, 3.0)
      break
    }
    case 3: {
      ;[-3, -1, 1, 3].forEach((x, i) => {
        kit.block({ x, y: -1.7, z: 0.2, size: 0.45, color: i === 3 ? CLAY.green : CLAY.process, label: ['read', 'filter', 'groupBy', 'show()'][i] })
      })
      for (let i = 0; i < 3; i++) {
        kit.beam(v3(-2.7 + i * 2, -1.7, 0.2), v3(-1.3 + i * 2, -1.7, 0.2), { color: CLAY.inkSoft, dashed: true, packets: 1, packetColor: CLAY.process, offset: i * 0.2 })
      }
      badge('ACTION → job berjalan', 2.8, 0.2, 0.4, CLAY.greenTile, 2.7)
      break
    }
    case 4: {
      kit.prism({ x: 0, y: -2.85, z: 0, title: 'Catalyst' })
      ;[-3, -1, 1, 3].forEach((x, i) => {
        kit.block({ x, y: -1.1, z: 0.2, size: 0.32, color: [CLAY.raw, CLAY.process, CLAY.violet, CLAY.output][i], label: ['Analysis', 'Logical', 'Physical', 'Codegen'][i] })
        kit.beam(v3(0, -1.1, 0.1), v3(x, -1.1, 0.2), { color: CLAY.violet, dashed: true, packets: 1, packetColor: CLAY.violet, offset: i * 0.15 })
      })
      break
    }
    case 5: {
      kit.block({ x: -3.4, y: -1.4, z: 0.2, size: 0.5, color: CLAY.process, label: 'Stage 1' })
      kit.block({ x: 3.4, y: -1.4, z: 0.2, size: 0.5, color: CLAY.output, label: 'Stage 2' })
      kit.beam(v3(0, -2.8, 0.35), v3(0, 0.15, 0.35), { color: CLAY.danger, dashed: true, packets: 0, arrow: false })
      badge('stage boundary', 0, -2.55, 0.45, CLAY.redSoft, 2.2)
      kit.beam(v3(-3.0, -0.7, 0.2), v3(3.0, -0.7, 0.2), { color: CLAY.process, packets: 2, packetColor: CLAY.process, label: 'narrow · tanpa shuffle', labelColor: CLAY.blueSoft })
      kit.beam(v3(-3.0, -2.0, 0.2), v3(3.0, -2.0, 0.2), { color: CLAY.danger, dashed: true, packets: 2, packetColor: CLAY.danger, label: 'wide · shuffle', labelColor: CLAY.redSoft, mid: v3(0, -2.55, 0.3) })
      break
    }
    case 6: {
      kit.block({ x: -3.1, y: -1.5, z: 0.2, size: 0.55, color: CLAY.raw, label: 'Bronze' })
      kit.filter({ x: 0, y: -2.85, z: 0, title: 'null · tipe · negatif · duplikat' })
      kit.block({ x: 3.1, y: -1.5, z: 0.2, size: 0.55, color: CLAY.process, label: 'Silver' })
      kit.folder({ x: 2.7, y: -2.85, z: 0, title: 'dt=2026-09-01', color: CLAY.process })
      kit.beam(v3(-2.5, -1.5, 0.2), v3(-0.8, -1.4, 0.2), { packets: 2, packetColor: CLAY.raw })
      kit.beam(v3(0.8, -1.4, 0.2), v3(2.5, -1.5, 0.2), { packets: 2, packetColor: CLAY.process })
      break
    }
    case 7: {
      kit.block({ x: -3.2, y: -1.5, z: 0.2, size: 0.5, color: CLAY.process, label: 'Silver' })
      kit.tower({ x: -0.8, y: -2.85, z: 0, title: 'Broadcast', color: CLAY.output, height: 1.5 })
      kit.block({ x: 2.9, y: -1.5, z: 0.2, size: 0.55, color: CLAY.output, label: 'Gold' })
      kit.server({ x: 0.8, y: -2.85, z: 0.4, title: 'Exec 1', height: 1.1, slots: 2, color: CLAY.inkSoft })
      kit.server({ x: 2.0, y: -2.85, z: 0.4, title: 'Exec 2', height: 1.1, slots: 2, color: CLAY.inkSoft })
      kit.beam(v3(-0.1, -0.8, 0.2), v3(0.8, -1.4, 0.4), { color: CLAY.output, dashed: true, packets: 2, packetColor: CLAY.output, label: 'tabel kecil', labelColor: CLAY.goldSoft })
      kit.beam(v3(-0.1, -0.8, 0.2), v3(2.0, -1.4, 0.4), { color: CLAY.output, dashed: true, packets: 2, packetColor: CLAY.output, offset: 0.25 })
      kit.beam(v3(-2.5, -1.5, 0.2), v3(2.4, -1.5, 0.2), { color: CLAY.green, packets: 2, packetColor: CLAY.green, label: 'revenue', labelColor: CLAY.greenTile })
      break
    }
    case 8: {
      kit.gauge({ x: 0, y: -2.85, z: 0, title: 'shuffle partitions' })
      const emptyColors = [CLAY.raw, CLAY.rawDark, CLAY.raw]
      for (let i = 0; i < 6; i++) {
        kit.block({ x: -3.5 + (i % 3) * 0.42, y: -2.4 + Math.floor(i / 3) * 0.36, z: 0.2, size: 0.22, color: emptyColors[i % 3], bob: false })
      }
      for (let i = 0; i < 8; i++) {
        kit.block({ x: 1.8 + (i % 4) * 0.4, y: -2.4 + Math.floor(i / 4) * 0.38, z: 0.2, size: 0.25, color: i % 2 ? CLAY.process : CLAY.output, bob: false })
      }
      kit.beam(v3(-2.4, -1.5, 0.2), v3(0.5, -1.5, 0.2), { color: CLAY.process, packets: 2, packetColor: CLAY.process })
      kit.beam(v3(0.5, -1.5, 0.2), v3(2.4, -1.5, 0.2), { color: CLAY.output, packets: 2, packetColor: CLAY.output })
      badge('200 partisi kosong → 8 terisi', 0, 0.6, 0.4, CLAY.blueSoft, 3.2)
      break
    }
    case 9: {
      kit.block({ x: -3.3, y: -1.4, z: 0.2, size: 1.0, color: CLAY.danger, label: 'Skew 80%' })
      ;[-0.6, 0.2, 1.0].forEach((x, i) => {
        kit.block({ x, y: -1.6, z: 0.2, size: 0.4, color: CLAY.process, label: `AQE ${i + 1}` })
        kit.beam(v3(-2.8, -1.4, 0.2), v3(x, -1.6, 0.2), { color: CLAY.danger, dashed: true, packets: 1, packetColor: CLAY.danger, offset: i * 0.18 })
      })
      ;[2.6, 3.4].forEach((x, i) => {
        kit.folder({ x, y: -2.85, z: 0, title: i === 0 ? '128 MB' : '512 MB', color: CLAY.output })
      })
      kit.beam(v3(1.4, -2.2, 0.2), v3(2.5, -2.2, 0.2), { color: CLAY.output, dashed: true, packets: 1, packetColor: CLAY.output, label: 'compact' })
      badge('skew join · small files', 0.2, 0.7, 0.4, CLAY.redSoft, 3.0)
      break
    }
    case 10: {
      kit.testTube({ x: -2.8, y: -2.85, z: 0, title: 'pytest ✓' })
      kit.shield({ x: 0, y: -1.5, z: 0, title: 'CI · release' })
      kit.block({ x: 2.8, y: -1.7, z: 0.2, size: 0.55, color: CLAY.output, label: 'Gold' })
      kit.beam(v3(-2.2, -1.2, 0.2), v3(-0.7, -1.5, 0.2), { packets: 2, packetColor: CLAY.green })
      kit.beam(v3(0.7, -1.5, 0.2), v3(2.2, -1.7, 0.2), { packets: 2, packetColor: CLAY.output })
      break
    }
  }
  fitCamera(index)
  renderer?.render(scene, camera)
}

function animate() {
  raf = requestAnimationFrame(animate)
  if (!renderer || !scene || !camera) return
  const delta = Math.min(0.05, clock.getDelta())
  if (!paused.value && !reducedMotion.value) elapsed += delta
  const t = reducedMotion.value ? 2.4 : elapsed

  nodes.forEach((group, i) => {
    const intro = easeOutCubic((t - stageStart) / 0.6)
    const base = group.userData.baseY
    group.position.y = base + Math.sin(t * 1.1 + group.userData.phase) * 0.045
    group.scale.setScalar(0.92 + intro * 0.08)
    if (group.userData.glow) group.userData.glow.opacity = 0.1 + Math.sin(t * 2.2 + i) * 0.035
  })
  packets.forEach((packet) => {
    const p = (t * packet.speed + packet.offset) % 1
    const point = packet.curve.getPoint(p)
    packet.mesh.position.copy(point)
    packet.mesh.position.z = -0.05
    const pulse = 1 + Math.sin(t * 6 + packet.offset * 10) * 0.12
    packet.mesh.scale.setScalar(pulse)
  })
  renderer.render(scene, camera)
}

function onPointerDown(event: PointerEvent) {
  pointer.down = true
  pointer.x = event.clientX
  pointer.y = event.clientY
  const canvas = canvasEl.value
  if (canvas) canvas.setPointerCapture(event.pointerId)
}

function onPointerMove(event: PointerEvent) {
  if (!pointer.down) return
  const dx = event.clientX - pointer.x
  const dy = event.clientY - pointer.y
  pointer.x = event.clientX
  pointer.y = event.clientY
  cameraState.yaw = clampValue(cameraState.yaw - dx * 0.006, -1.0, 1.0)
  cameraState.pitch = clampValue(cameraState.pitch - dy * 0.004, 0.08, 0.68)
  updateCamera()
}

function onPointerUp(event: PointerEvent) {
  pointer.down = false
  const canvas = canvasEl.value
  if (canvas && canvas.hasPointerCapture(event.pointerId)) canvas.releasePointerCapture(event.pointerId)
}

function onWheel(event: WheelEvent) {
  event.preventDefault()
  cameraState.radius = clampValue(
    cameraState.radius + event.deltaY * 0.012,
    cameraState.baseRadius * 0.8,
    cameraState.baseRadius * 1.55,
  )
  updateCamera()
}

function resetView() {
  cameraState.yaw = 0
  cameraState.pitch = 0.52
  cameraState.radius = cameraState.baseRadius
  updateCamera()
}

function replay() {
  if (paused.value && !reducedMotion.value) paused.value = false
  buildStage(current.value)
}

function togglePause() {
  paused.value = !paused.value
  if (!paused.value && reducedMotion.value) reducedMotion.value = false
  clock?.getDelta()
}

async function toggleFullscreen() {
  const el = stageEl.value
  if (!el) return
  try {
    if (!document.fullscreenElement) await el.requestFullscreen()
    else await document.exitFullscreen()
  } catch {
    /* browser may refuse */
  }
}

function onFullscreenChange() {
  isFullscreen.value = Boolean(document.fullscreenElement)
  requestAnimationFrame(resizeRenderer)
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
  if (typeof window !== 'undefined') {
    const url = new URL(window.location.href)
    if (current.value === 0) url.searchParams.delete('step')
    else url.searchParams.set('step', String(current.value + 1))
    window.history.replaceState({}, '', url)
  }
  if (threeReady) buildStage(current.value)
  nextTick(() => guideEl.value?.scrollTo({ top: 0, behavior: 'smooth' }))
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

onMounted(async () => {
  const initial = readInitialStep()
  if (initial > 0) current.value = initial
  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reducedMotion.value) paused.value = true

  window.addEventListener('keydown', onKeydown)
  document.addEventListener('fullscreenchange', onFullscreenChange)

  try {
    THREE = await loadThree()
    await document.fonts.ready
    initThree()
    buildStage(current.value)
    clock = new THREE.Clock()
    threeReady = true
    threeLoading.value = false
    raf = requestAnimationFrame(animate)
  } catch (error) {
    threeError.value = 'Model 3D tidak dapat dimuat di browser ini. Coba aktifkan WebGL atau gunakan browser terbaru.'
    threeLoading.value = false
    console.error(error)
  }
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  resizeObserver?.disconnect()
  window.removeEventListener('keydown', onKeydown)
  document.removeEventListener('fullscreenchange', onFullscreenChange)
  const canvas = canvasEl.value
  if (canvas) {
    canvas.removeEventListener('pointerdown', onPointerDown)
    canvas.removeEventListener('pointermove', onPointerMove)
    canvas.removeEventListener('pointerup', onPointerUp)
    canvas.removeEventListener('pointercancel', onPointerUp)
    canvas.removeEventListener('wheel', onWheel)
    canvas.removeEventListener('dblclick', resetView)
  }
  if (stageGroup) disposeObject(stageGroup)
  renderer?.dispose()
  renderer = null
  scene = null
  camera = null
  document.body.style.overflow = ''
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

.three-canvas {
  cursor: grab;
  touch-action: none;
}

.three-canvas:active {
  cursor: grabbing;
}

.three-caption {
  position: absolute;
  bottom: 35px;
  left: 50%;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 5px 12px 6px;
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  background: rgba(251, 247, 241, 0.88);
  box-shadow: 0 1px 0 rgba(80, 60, 35, 0.06);
  pointer-events: none;
  transform: translateX(-50%);
  backdrop-filter: blur(3px);
}

.three-caption__eyebrow {
  color: var(--muted);
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.three-caption strong {
  color: var(--ink);
  font-size: 12px;
  font-weight: 800;
  white-space: nowrap;
}

.three-hint {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 2;
  color: var(--muted-2);
  font-size: 9px;
  pointer-events: none;
  transform: translateX(-50%);
  white-space: nowrap;
}

.three-loading {
  position: absolute;
  inset: 0;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: rgba(250, 243, 233, 0.8);
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
  backdrop-filter: blur(2px);
}

.three-loader {
  width: 22px;
  height: 22px;
  border: 2px solid var(--line-strong);
  border-top-color: var(--green-dark, #2f8a43);
  border-radius: 50%;
  animation: three-spin 0.8s linear infinite;
}

@keyframes three-spin {
  to { transform: rotate(360deg); }
}

.three-fallback {
  position: absolute;
  inset: 0;
  z-index: 6;
  display: grid;
  place-items: center;
  padding: 24px;
  background: rgba(250, 243, 233, 0.94);
  color: var(--ink-2);
  text-align: center;
  font-size: 12px;
  line-height: 1.6;
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
  .three-caption, .three-hint {
    display: none;
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

.dv-title--long {
  white-space: normal;
  font-size: 25px;
  line-height: 1.15;
}
</style>
