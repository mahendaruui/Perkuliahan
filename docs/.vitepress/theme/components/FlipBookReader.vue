<template>
  <ClientOnly>
    <div class="flipbook-wrapper" ref="wrapperRef" :class="{ 'is-fullscreen': isFullscreen }">
      <!-- Top Header Bar -->
      <div class="flipbook-header">
        <div class="book-info">
          <div class="book-badge">E-BOOK INTERAKTIF 3D</div>
          <h2 class="book-title">{{ title }}</h2>
          <span class="book-subtitle">{{ subtitle }}</span>
        </div>
        <div class="header-actions">
          <button class="btn-tool" @click="toggleTOC" :class="{ active: showTOC }" title="Daftar Isi Lengkap">
            <span class="icon">📑</span>
            <span class="btn-label">Daftar Isi</span>
          </button>
          <button class="btn-tool" @click="toggleThumbnails" :class="{ active: showThumbnails }" title="Pratinjau Thumbnail">
            <span class="icon">🖼️</span>
            <span class="btn-label">Thumbnail</span>
          </button>
          <a :href="pdfDownloadUrl" download class="btn-tool btn-download" title="Unduh Berkas PDF">
            <span class="icon">📥</span>
            <span class="btn-label">Unduh PDF</span>
          </a>
          <button class="btn-tool" @click="toggleFullscreen" title="Layar Penuh (Fullscreen)">
            <span class="icon">{{ isFullscreen ? '🗗' : '⛶' }}</span>
          </button>
        </div>
      </div>

      <!-- Main Stage -->
      <div class="flipbook-stage" :style="{ transform: `scale(${zoomLevel})` }">
        <!-- Navigation Prev Button -->
        <button
          class="nav-edge nav-prev"
          @click="prevPage"
          :disabled="currentPage <= 1"
          title="Halaman Sebelumnya (Panah Kiri)"
        >
          <span>‹</span>
        </button>

        <!-- The 3D Book Container -->
        <div
          class="book-container"
          :class="{
            'is-spread': isSpreadMode,
            'is-single': !isSpreadMode,
            'is-cover': isSpreadMode && (currentPage === 1 || currentPage === totalPages)
          }"
          @touchstart="handleTouchStart"
          @touchend="handleTouchEnd"
        >
          <!-- SPREAD MODE (Double Page) -->
          <template v-if="isSpreadMode">
            <!-- Left Page -->
            <div
              class="page-sheet page-left"
              :class="{ 'page-blank': !leftPageNumber }"
              @click="prevPage"
            >
              <img
                v-if="leftPageNumber"
                :src="getPageUrl(leftPageNumber)"
                :alt="`Halaman ${leftPageNumber}`"
                loading="eager"
                class="page-img"
              />
              <div v-if="leftPageNumber" class="page-number-pill left-pill">
                {{ formatPageNum(leftPageNumber) }}
              </div>
              <div class="spine-shadow left-spine"></div>
            </div>

            <!-- Book Spine Middle Crease -->
            <div class="book-spine-crease"></div>

            <!-- Right Page -->
            <div
              class="page-sheet page-right"
              :class="{ 'page-blank': !rightPageNumber }"
              @click="nextPage"
            >
              <img
                v-if="rightPageNumber"
                :src="getPageUrl(rightPageNumber)"
                :alt="`Halaman ${rightPageNumber}`"
                loading="eager"
                class="page-img"
              />
              <div v-if="rightPageNumber" class="page-number-pill right-pill">
                {{ formatPageNum(rightPageNumber) }}
              </div>
              <div class="spine-shadow right-spine"></div>
            </div>
          </template>

          <!-- SINGLE PAGE MODE -->
          <template v-else>
            <div class="page-sheet page-single">
              <img
                :src="getPageUrl(currentPage)"
                :alt="`Halaman ${currentPage}`"
                loading="eager"
                class="page-img"
              />
              <div class="page-number-pill single-pill">
                {{ formatPageNum(currentPage) }} / {{ totalPages }}
              </div>
            </div>
          </template>
        </div>

        <!-- Navigation Next Button -->
        <button
          class="nav-edge nav-next"
          @click="nextPage"
          :disabled="currentPage >= totalPages"
          title="Halaman Selanjutnya (Panah Kanan / Spasi)"
        >
          <span>›</span>
        </button>
      </div>

      <!-- Bottom Control Toolbar -->
      <div class="flipbook-toolbar">
        <div class="toolbar-section">
          <button class="btn-ctrl" @click="goToPage(1)" :disabled="currentPage <= 1" title="Halaman Pertama">
            ⇤
          </button>
          <button class="btn-ctrl" @click="prevPage" :disabled="currentPage <= 1" title="Sebelumnya">
            ◀
          </button>
          
          <div class="page-counter">
            <span>Hlm</span>
            <input
              type="number"
              v-model.number="inputPage"
              @keyup.enter="applyPageInput"
              min="1"
              :max="totalPages"
              class="page-input"
            />
            <span>dari {{ totalPages }}</span>
          </div>

          <button class="btn-ctrl" @click="nextPage" :disabled="currentPage >= totalPages" title="Selanjutnya">
            ▶
          </button>
          <button class="btn-ctrl" @click="goToPage(totalPages)" :disabled="currentPage >= totalPages" title="Halaman Terakhir">
            ⇥
          </button>
        </div>

        <!-- Slider Scrubber -->
        <div class="toolbar-slider-wrapper">
          <input
            type="range"
            min="1"
            :max="totalPages"
            :value="currentPage"
            @input="onSliderChange"
            class="page-slider"
          />
        </div>

        <div class="toolbar-section tools-right">
          <!-- Zoom Controls -->
          <button class="btn-ctrl" @click="zoomOut" :disabled="zoomLevel <= 0.7" title="Perkecil">
            ➖
          </button>
          <span class="zoom-text">{{ Math.round(zoomLevel * 100) }}%</span>
          <button class="btn-ctrl" @click="zoomIn" :disabled="zoomLevel >= 1.6" title="Perbesar">
            ➕
          </button>
          <button class="btn-ctrl" @click="resetZoom" title="Reset Zoom">
            ↺
          </button>

          <!-- Sound FX Toggle -->
          <button class="btn-ctrl" @click="toggleSound" :title="soundEnabled ? 'Matikan Suara Kertas' : 'Aktifkan Suara Kertas'">
            {{ soundEnabled ? '🔊' : '🔇' }}
          </button>

          <!-- Spread / Single Mode Toggle -->
          <button class="btn-ctrl btn-mode" @click="toggleSpreadMode" title="Ubah Mode Tampilan">
            {{ isSpreadMode ? '📄 Single' : '📖 Double' }}
          </button>
        </div>
      </div>

      <!-- Slide-in Drawer: Table of Contents -->
      <transition name="drawer">
        <div v-if="showTOC" class="drawer-overlay" @click.self="showTOC = false">
          <div class="drawer-panel">
            <div class="drawer-header">
              <h3>📑 Daftar Isi Buku</h3>
              <button class="btn-close" @click="showTOC = false">✕</button>
            </div>
            <div class="drawer-body">
              <ul class="toc-list">
                <li
                  v-for="(item, idx) in tocItems"
                  :key="idx"
                  :class="['toc-item', `toc-level-${item.level}`, { active: isItemActive(item.page) }]"
                  @click="jumpToTOC(item.page)"
                >
                  <span class="toc-title">{{ item.title }}</span>
                  <span class="toc-dots"></span>
                  <span class="toc-page">Hlm {{ item.page }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </transition>

      <!-- Slide-in Modal: Thumbnail Grid View -->
      <transition name="modal">
        <div v-if="showThumbnails" class="modal-overlay" @click.self="showThumbnails = false">
          <div class="modal-panel">
            <div class="modal-header">
              <h3>🖼️ Pratinjau Seluruh Halaman ({{ totalPages }} Halaman)</h3>
              <button class="btn-close" @click="showThumbnails = false">✕</button>
            </div>
            <div class="modal-body thumbnail-grid">
              <div
                v-for="p in totalPages"
                :key="p"
                class="thumb-card"
                :class="{ active: isPageInView(p) }"
                @click="jumpFromThumb(p)"
              >
                <div class="thumb-img-wrap">
                  <img :src="getPageUrl(p)" :alt="`Thumbnail Halaman ${p}`" loading="lazy" class="thumb-img" />
                </div>
                <div class="thumb-label">Hlm {{ p }}</div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </ClientOnly>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = withDefaults(
  defineProps<{
    title?: string
    subtitle?: string
    totalPages?: number
    basePath?: string
    pdfDownloadUrl?: string
    docDownloadUrl?: string
  }>(),
  {
    title: 'Pemrograman Berorientasi Objek menggunakan PHP 8+',
    subtitle: 'Buku Ajar Resmi Kurikulum OBE Program Studi Informatika UUI',
    totalPages: 86,
    basePath: '/Perkuliahan/flipbook/oop-php/page-',
    pdfDownloadUrl: '/Perkuliahan/books/Buku_Ajar_OOP_PHP8_Latest.pdf',
    docDownloadUrl: '/Perkuliahan/books/Buku_Ajar_OOP_PHP8_Latest.docx'
  }
)

const wrapperRef = ref<HTMLElement | null>(null)
const currentPage = ref(1)
const inputPage = ref(1)
const isSpreadMode = ref(true)
const isFullscreen = ref(false)
const zoomLevel = ref(1.0)
const soundEnabled = ref(true)
const showTOC = ref(false)
const showThumbnails = ref(false)

// Table of Contents Mapping
const tocItems = [
  { title: 'Halaman Sampul Depan (Cover)', page: 1, level: 1 },
  { title: 'Halaman Judul & Informasi Penulis', page: 2, level: 1 },
  { title: 'Informasi Penerbitan & Hak Cipta (KDT)', page: 3, level: 1 },
  { title: 'Kata Pengantar Penulis', page: 4, level: 1 },
  { title: 'Matriks Capaian Pembelajaran (CPL & CPMK)', page: 6, level: 1 },
  { title: 'Daftar Isi Lengkap', page: 8, level: 1 },
  { title: 'BAB 1: Pengantar Paradigma OOP & Ekosistem PHP 8+', page: 13, level: 1 },
  { title: 'BAB 2: Anatomi Class, Objek, dan Manajemen Memori', page: 18, level: 1 },
  { title: 'BAB 3: Method, Constructor Promotion, dan Siklus Hidup Objek', page: 22, level: 1 },
  { title: 'BAB 4: Enkapsulasi, Visibility Modifiers, Readonly & Hooks', page: 25, level: 1 },
  { title: 'BAB 5: Pewarisan (Inheritance), Final Keyword & Trait', page: 33, level: 1 },
  { title: 'BAB 6: Polimorfisme (Polymorphism) & Dynamic Dispatch', page: 39, level: 1 },
  { title: 'BAB 7: Abstraksi: Abstract Class, Interface & Backed Enum', page: 44, level: 1 },
  { title: 'BAB 8: Manajemen Namespace, Standar PSR-4 & Composer', page: 50, level: 1 },
  { title: 'BAB 9: Penanganan Kesalahan (Exception Handling) Tangguh', page: 55, level: 1 },
  { title: 'BAB 10: Koleksi Objek Terstruktur (First-Class Collections)', page: 60, level: 1 },
  { title: 'BAB 11: Manajemen Berkas & I/O Stream (Mitigasi Race Condition)', page: 64, level: 1 },
  { title: 'BAB 12: Prinsip Desain Perangkat Lunak SOLID pada PHP Modern', page: 68, level: 1 },
  { title: 'BAB 13: Arsitektur Aplikasi (Model-Service-Repository)', page: 72, level: 1 },
  { title: 'BAB 14: Studi Kasus Mini Project: Sistem POS Terpadu', page: 78, level: 1 },
  { title: 'Glosarium Istilah Rekayasa Perangkat Lunak', page: 82, level: 1 },
  { title: 'Daftar Pustaka Standar Internasional', page: 84, level: 1 },
  { title: 'Profil Tim Penulis & Dewan Pakar Informatika UUI', page: 86, level: 1 }
]

// Double-page spread computation
const leftPageNumber = computed(() => {
  if (!isSpreadMode.value) return currentPage.value
  if (currentPage.value === 1) return null
  return currentPage.value % 2 === 0 ? currentPage.value : currentPage.value - 1
})

const rightPageNumber = computed(() => {
  if (!isSpreadMode.value) return null
  if (currentPage.value === 1) return 1
  const rightNum = (currentPage.value % 2 === 0 ? currentPage.value : currentPage.value - 1) + 1
  return rightNum <= props.totalPages ? rightNum : null
})

function getPageUrl(pageNum: number): string {
  const pStr = String(pageNum).padStart(2, '0')
  return `${props.basePath}${pStr}.webp`
}

function formatPageNum(pageNum: number): string {
  if (pageNum === 1) return 'Sampul'
  if (pageNum >= 2 && pageNum <= 12) {
    const roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi']
    return roman[pageNum - 2] || String(pageNum)
  }
  return String(pageNum)
}

function isPageInView(p: number): boolean {
  if (!isSpreadMode.value) return currentPage.value === p
  return p === leftPageNumber.value || p === rightPageNumber.value
}

function isItemActive(p: number): boolean {
  return isPageInView(p)
}

// Synthesized Paper Flip Sound via Web Audio API
let audioCtx: AudioContext | null = null

function playFlipSound() {
  if (!soundEnabled.value) return
  try {
    const AudioContextClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext
    if (!audioCtx) audioCtx = new AudioContextClass()
    if (audioCtx.state === 'suspended') audioCtx.resume()

    const bufferSize = Math.floor(audioCtx.sampleRate * 0.1)
    const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate)
    const data = buffer.getChannelData(0)
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.3))
    }

    const noise = audioCtx.createBufferSource()
    noise.buffer = buffer

    const filter = audioCtx.createBiquadFilter()
    filter.type = 'lowpass'
    filter.frequency.setValueAtTime(1200, audioCtx.currentTime)
    filter.frequency.exponentialRampToValueAtTime(250, audioCtx.currentTime + 0.1)

    const gain = audioCtx.createGain()
    gain.gain.setValueAtTime(0.25, audioCtx.currentTime)
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1)

    noise.connect(filter)
    filter.connect(gain)
    gain.connect(audioCtx.destination)

    noise.start()
  } catch {
    // Ignore audio error
  }
}

// Navigation methods
function nextPage() {
  if (isSpreadMode.value) {
    if (currentPage.value === 1) {
      goToPage(2)
    } else {
      const next = currentPage.value + 2
      if (next <= props.totalPages) goToPage(next)
      else if (currentPage.value < props.totalPages) goToPage(props.totalPages)
    }
  } else {
    if (currentPage.value < props.totalPages) goToPage(currentPage.value + 1)
  }
}

function prevPage() {
  if (isSpreadMode.value) {
    if (currentPage.value <= 2) {
      goToPage(1)
    } else {
      goToPage(currentPage.value - 2)
    }
  } else {
    if (currentPage.value > 1) goToPage(currentPage.value - 1)
  }
}

function goToPage(pageNum: number) {
  const target = Math.max(1, Math.min(props.totalPages, pageNum))
  if (target !== currentPage.value) {
    currentPage.value = target
    inputPage.value = target
    playFlipSound()
  }
}

function applyPageInput() {
  goToPage(inputPage.value)
}

function onSliderChange(e: Event) {
  const val = Number((e.target as HTMLInputElement).value)
  goToPage(val)
}

function jumpToTOC(p: number) {
  goToPage(p)
  showTOC.value = false
}

function jumpFromThumb(p: number) {
  goToPage(p)
  showThumbnails.value = false
}

// Zoom & Modes
function zoomIn() {
  if (zoomLevel.value < 1.6) zoomLevel.value = Number((zoomLevel.value + 0.15).toFixed(2))
}

function zoomOut() {
  if (zoomLevel.value > 0.7) zoomLevel.value = Number((zoomLevel.value - 0.15).toFixed(2))
}

function resetZoom() {
  zoomLevel.value = 1.0
}

function toggleSpreadMode() {
  isSpreadMode.value = !isSpreadMode.value
}

function toggleSound() {
  soundEnabled.value = !soundEnabled.value
}

function toggleTOC() {
  showTOC.value = !showTOC.value
  showThumbnails.value = false
}

function toggleThumbnails() {
  showThumbnails.value = !showThumbnails.value
  showTOC.value = false
}

function toggleFullscreen() {
  if (!wrapperRef.value) return
  if (!document.fullscreenElement) {
    wrapperRef.value.requestFullscreen().then(() => {
      isFullscreen.value = true
    }).catch(() => {})
  } else {
    document.exitFullscreen().then(() => {
      isFullscreen.value = false
    }).catch(() => {})
  }
}

// Touch Swipes
let touchStartX = 0
function handleTouchStart(e: TouchEvent) {
  touchStartX = e.touches[0].clientX
}

function handleTouchEnd(e: TouchEvent) {
  const touchEndX = e.changedTouches[0].clientX
  const diff = touchEndX - touchStartX
  if (diff > 50) prevPage()
  else if (diff < -50) nextPage()
}

// Keybindings
function handleKeyDown(e: KeyboardEvent) {
  if (['input', 'textarea'].includes((e.target as HTMLElement)?.tagName?.toLowerCase())) return
  if (e.key === 'ArrowRight' || e.key === ' ') {
    e.preventDefault()
    nextPage()
  } else if (e.key === 'ArrowLeft') {
    e.preventDefault()
    prevPage()
  } else if (e.key === 'Home') {
    e.preventDefault()
    goToPage(1)
  } else if (e.key === 'End') {
    e.preventDefault()
    goToPage(props.totalPages)
  }
}

function handleResize() {
  if (typeof window !== 'undefined') {
    if (window.innerWidth < 768 && isSpreadMode.value) {
      isSpreadMode.value = false
    }
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeyDown)
  window.addEventListener('resize', handleResize)
  handleResize()
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyDown)
  window.removeEventListener('resize', handleResize)
})
</script>

<style scoped>
.flipbook-wrapper {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 1.5rem auto 3rem;
  background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
  border-radius: 16px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  color: #f8fafc;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  user-select: none;
}

.flipbook-wrapper.is-fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  max-width: 100vw;
  margin: 0;
  border-radius: 0;
  z-index: 9999;
}

/* Header */
.flipbook-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-wrap: wrap;
  gap: 1rem;
}

.book-info {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.book-badge {
  display: inline-block;
  align-self: flex-start;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  background: linear-gradient(90deg, #38bdf8 0%, #6366f1 100%);
  color: #ffffff;
}

.book-title {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  color: #f8fafc;
  line-height: 1.3;
}

.book-subtitle {
  font-size: 0.8rem;
  color: #94a3b8;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-tool {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0.45rem 0.85rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-tool:hover {
  background: rgba(255, 255, 255, 0.16);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.3);
}

.btn-tool.active {
  background: #3b82f6;
  color: #ffffff;
  border-color: #60a5fa;
}

.btn-download {
  background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
  color: #ffffff;
  border: none;
}

.btn-download:hover {
  filter: brightness(1.15);
}

/* Stage Area */
.flipbook-stage {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem 1rem;
  min-height: 580px;
  background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
  transform-origin: center center;
  transition: transform 0.25s ease-out;
  overflow: hidden;
}

.nav-edge {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 46px;
  height: 64px;
  background: rgba(15, 23, 42, 0.7);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  color: #ffffff;
  font-size: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.2s ease;
}

.nav-edge:hover:not(:disabled) {
  background: rgba(59, 130, 246, 0.85);
  border-color: #60a5fa;
  transform: translateY(-50%) scale(1.08);
}

.nav-edge:disabled {
  opacity: 0.25;
  cursor: not-allowed;
}

.nav-prev { left: 1rem; }
.nav-next { right: 1rem; }

/* Book 3D Container */
.book-container {
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.7), 0 0 40px rgba(0, 0, 0, 0.3);
  border-radius: 6px;
  background: #ffffff;
  perspective: 1500px;
  max-width: 90%;
  max-height: 72vh;
}

.page-sheet {
  position: relative;
  background: #ffffff;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.page-sheet:hover {
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.05);
}

.page-left {
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
}

.page-right {
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px;
}

.page-single {
  border-radius: 6px;
}

.page-img {
  width: auto;
  height: auto;
  max-height: 70vh;
  max-width: 100%;
  display: block;
  object-fit: contain;
}

.page-blank {
  background: #f8fafc;
  min-width: 320px;
  min-height: 450px;
}

.book-spine-crease {
  width: 10px;
  height: 100%;
  background: linear-gradient(90deg, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.25) 100%);
  box-shadow: inset 0 0 8px rgba(0,0,0,0.4);
  z-index: 5;
}

.spine-shadow {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 24px;
  pointer-events: none;
  z-index: 2;
}

.left-spine {
  right: 0;
  background: linear-gradient(to left, rgba(0, 0, 0, 0.18) 0%, transparent 100%);
}

.right-spine {
  left: 0;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.18) 0%, transparent 100%);
}

.page-number-pill {
  position: absolute;
  bottom: 0.5rem;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  z-index: 3;
}

.left-pill { left: 0.8rem; }
.right-pill { right: 0.8rem; }
.single-pill { bottom: 0.6rem; }

/* Bottom Toolbar */
.flipbook-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(12px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-wrap: wrap;
  gap: 0.75rem;
}

.toolbar-section {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.btn-ctrl {
  background: rgba(255, 255, 255, 0.08);
  color: #f8fafc;
  border: 1px solid rgba(255, 255, 255, 0.12);
  width: 34px;
  height: 34px;
  border-radius: 6px;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-ctrl:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

.btn-ctrl:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.btn-mode {
  width: auto;
  padding: 0 0.6rem;
  font-size: 0.8rem;
  font-weight: 600;
}

.page-counter {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  color: #cbd5e1;
  margin: 0 0.3rem;
}

.page-input {
  width: 48px;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff;
  text-align: center;
  border-radius: 4px;
  padding: 0.25rem 0.2rem;
  font-weight: 700;
  font-size: 0.85rem;
}

.page-input:focus {
  outline: none;
  border-color: #38bdf8;
  background: rgba(0, 0, 0, 0.6);
}

.toolbar-slider-wrapper {
  flex: 1;
  max-width: 280px;
  min-width: 140px;
  margin: 0 0.5rem;
  display: flex;
  align-items: center;
}

.page-slider {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 3px;
  outline: none;
  cursor: pointer;
  accent-color: #38bdf8;
}

.zoom-text {
  font-size: 0.8rem;
  color: #94a3b8;
  min-width: 42px;
  text-align: center;
}

/* Slide-in Drawers & Modals */
.drawer-overlay, .modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(6px);
  z-index: 100;
  display: flex;
}

.drawer-panel {
  width: 380px;
  max-width: 85vw;
  height: 100%;
  background: #0f172a;
  border-right: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  flex-direction: column;
  box-shadow: 10px 0 30px rgba(0, 0, 0, 0.5);
}

.drawer-header, .modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.drawer-header h3, .modal-header h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: #f8fafc;
}

.btn-close {
  background: transparent;
  border: none;
  color: #94a3b8;
  font-size: 1.3rem;
  cursor: pointer;
}

.btn-close:hover {
  color: #ffffff;
}

.drawer-body {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem 1rem;
}

.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-item {
  display: flex;
  align-items: baseline;
  padding: 0.65rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.88rem;
  color: #cbd5e1;
  transition: all 0.15s ease;
  margin-bottom: 0.25rem;
}

.toc-item:hover {
  background: rgba(59, 130, 246, 0.15);
  color: #38bdf8;
}

.toc-item.active {
  background: #2563eb;
  color: #ffffff;
  font-weight: 600;
}

.toc-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 70%;
}

.toc-dots {
  flex: 1;
  border-bottom: 1px dotted rgba(255, 255, 255, 0.2);
  margin: 0 0.4rem;
}

.toc-page {
  font-size: 0.8rem;
  font-weight: 600;
  color: #38bdf8;
}

.toc-item.active .toc-page {
  color: #ffffff;
}

/* Modal Thumbnail Grid */
.modal-overlay {
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.modal-panel {
  width: 900px;
  max-width: 90vw;
  max-height: 85vh;
  background: #0f172a;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
}

.thumbnail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
  gap: 1rem;
  padding: 1.5rem;
  overflow-y: auto;
}

.thumb-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid transparent;
  border-radius: 6px;
  padding: 0.4rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.thumb-card:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: #38bdf8;
  transform: translateY(-2px);
}

.thumb-card.active {
  border-color: #3b82f6;
  background: rgba(59, 130, 246, 0.2);
}

.thumb-img-wrap {
  width: 100%;
  aspect-ratio: 1 / 1.414;
  background: #ffffff;
  border-radius: 4px;
  overflow: hidden;
}

.thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thumb-label {
  font-size: 0.75rem;
  color: #94a3b8;
  margin-top: 0.3rem;
}

/* Animations */
.drawer-enter-active, .drawer-leave-active {
  transition: opacity 0.25s ease;
}
.drawer-enter-from, .drawer-leave-to {
  opacity: 0;
}
.drawer-enter-active .drawer-panel, .drawer-leave-active .drawer-panel {
  transition: transform 0.25s ease;
}
.drawer-enter-from .drawer-panel, .drawer-leave-to .drawer-panel {
  transform: translateX(-100%);
}

.modal-enter-active, .modal-leave-active {
  transition: opacity 0.2s ease;
}
.modal-enter-from, .modal-leave-to {
  opacity: 0;
}
.modal-enter-active .modal-panel, .modal-leave-active .modal-panel {
  transition: transform 0.2s ease;
}
.modal-enter-from .modal-panel, .modal-leave-to .modal-panel {
  transform: scale(0.95);
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .flipbook-header {
    flex-direction: column;
    align-items: flex-start;
  }
  .header-actions {
    width: 100%;
    justify-content: space-between;
  }
  .btn-label {
    display: none;
  }
  .flipbook-toolbar {
    justify-content: center;
  }
  .toolbar-slider-wrapper {
    order: 3;
    width: 100%;
    max-width: 100%;
    margin-top: 0.5rem;
  }
}
</style>
