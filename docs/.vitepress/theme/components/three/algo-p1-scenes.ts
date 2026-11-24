import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 1 — Flowchart: Pengenalan Algoritma & Notasi Standar         */
/* ------------------------------------------------------------------ */

export const algoP1Scenes: IsoScene[] = [
  // 1. Instruksi ambigu → hasil berbeda
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Mulai' },
      { id: 'io', type: 'io', x: 0, y: -1.1, label: 'Instruksi: "tambah sedikit gula"' },
      { id: 'dec', type: 'decision', x: 0, y: -0.05, label: 'Definisi jelas?' },
      { id: 'no', type: 'process', x: -1.6, y: 1.05, label: 'Mesin menebak', sub: '2 sendok vs 1 cangkir', status: 'failed', color: P.danger },
      { id: 'noEnd', type: 'end', x: -1.6, y: 2.05, label: 'Hasil berbeda', status: 'failed', color: P.redSoft },
      { id: 'yes', type: 'process', x: 1.6, y: 1.05, label: 'Langkah pasti', color: P.green },
      { id: 'yesEnd', type: 'end', x: 1.6, y: 2.05, label: 'Hasil konsisten', color: P.green },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'no', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'no', to: 'noEnd', color: P.danger, packets: 1 },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'yes', to: 'yesEnd', color: P.greenDark, packets: 1 },
    ],
  },

  // 2. Sejarah tiga tokoh
  {
    nodes: [
      { id: 'start', type: 'start', x: -2.4, y: -1.6, label: 'Sumber' },
      { id: 'khwarizmi', type: 'process', x: -2.4, y: -0.65, label: 'Al-Khwarizmi', sub: '780–850 · aljabar', color: P.raw },
      { id: 'ada', type: 'process', x: -0.6, y: -0.65, label: 'Ada Lovelace', sub: '1843 · program pertama', color: P.process },
      { id: 'turing', type: 'process', x: 1.4, y: -0.65, label: 'Alan Turing', sub: '1936 · mesin Turing', color: P.violet },
      { id: 'end', type: 'end', x: 1.4, y: 0.65, label: 'Algoritma modern', color: P.green },
    ],
    links: [
      { from: 'start', to: 'khwarizmi', color: P.ink2, packets: 1 },
      { from: 'khwarizmi', to: 'ada', color: P.ink2, packets: 1, label: 'abad ke-9' },
      { from: 'ada', to: 'turing', color: P.process, packets: 1, label: '1843' },
      { from: 'turing', to: 'end', color: P.greenDark, packets: 1, label: '1936' },
    ],
  },

  // 3. Definisi formal & syarat berhingga
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Mulai' },
      { id: 'io', type: 'io', x: 0, y: -1.15, label: 'Input: data sah' },
      { id: 'dec1', type: 'decision', x: 0, y: -0.25, label: 'Langkah berhingga?' },
      { id: 'fail1', type: 'end', x: -1.7, y: -0.25, label: 'Bukan algoritma', status: 'failed' },
      { id: 'proc', type: 'process', x: 0, y: 0.7, label: 'Proses deterministik', sub: 'tidak ambigu', color: P.process },
      { id: 'dec2', type: 'decision', x: 0, y: 1.6, label: 'Output benar?' },
      { id: 'fail2', type: 'end', x: 1.7, y: 1.6, label: 'Perbaiki', status: 'failed' },
      { id: 'end', type: 'end', x: 0, y: 2.4, label: 'Selesai', color: P.green },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'dec1', color: P.process, packets: 1 },
      { from: 'dec1', to: 'fail1', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'dec1', to: 'proc', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'proc', to: 'dec2', color: P.process, packets: 1 },
      { from: 'dec2', to: 'end', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'dec2', to: 'fail2', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
    ],
  },

  // 4. Lima syarat Knuth
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Mulai' },
      { id: 'c1', type: 'process', x: -2.3, y: -0.6, label: '1 · Finiteness', sub: 'berhenti', color: P.blueSoft },
      { id: 'c2', type: 'process', x: -1.15, y: -0.6, label: '2 · Definiteness', sub: 'tidak ambigu', color: P.violet },
      { id: 'c3', type: 'process', x: 0, y: -0.6, label: '3 · Input', sub: 'berdefinisi', color: P.raw },
      { id: 'c4', type: 'process', x: 1.15, y: -0.6, label: '4 · Output', sub: 'tepat', color: P.output },
      { id: 'c5', type: 'process', x: 2.3, y: -0.6, label: '5 · Effectiveness', sub: 'dapat dikerjakan', color: P.green },
      { id: 'end', type: 'end', x: 0, y: 0.8, label: 'Lolos 5 syarat', color: P.green },
    ],
    links: [
      { from: 'start', to: 'c1', color: P.ink2, packets: 1 },
      { from: 'c1', to: 'c2', color: P.ink2, packets: 1 },
      { from: 'c2', to: 'c3', color: P.ink2, packets: 1 },
      { from: 'c3', to: 'c4', color: P.ink2, packets: 1 },
      { from: 'c4', to: 'c5', color: P.ink2, packets: 1 },
      { from: 'c5', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 5. Aksioma Wirth
  {
    nodes: [
      { id: 'start', type: 'start', x: -2.0, y: -1.6, label: 'Masalah' },
      { id: 'algo', type: 'process', x: -2.0, y: -0.6, label: 'Algoritma', sub: 'logika langkah', color: P.process },
      { id: 'data', type: 'process', x: -0.4, y: -0.6, label: 'Struktur Data', sub: 'wadah data', color: P.violet },
      { id: 'program', type: 'process', x: 1.3, y: -0.6, label: 'Program', sub: 'sintaks bahasa', color: P.output },
      { id: 'run', type: 'process', x: 1.3, y: 0.45, label: 'Compiler / Interpreter', color: P.blueSoft },
      { id: 'end', type: 'end', x: 1.3, y: 1.5, label: 'Dijalankan CPU', color: P.green },
    ],
    links: [
      { from: 'start', to: 'algo', color: P.ink2, packets: 1 },
      { from: 'algo', to: 'data', color: P.process, packets: 1, label: '+' },
      { from: 'data', to: 'program', color: P.output, packets: 1, label: '=' },
      { from: 'program', to: 'run', color: P.process, packets: 1 },
      { from: 'run', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 6. Siklus pemecahan masalah
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.2, label: 'Masalah nyata' },
      { id: 'analisis', type: 'process', x: 0, y: -1.4, label: 'Analisis kebutuhan', color: P.blueSoft },
      { id: 'desain', type: 'process', x: 0, y: -0.6, label: 'Desain flowchart', sub: 'pseudocode', color: P.violet },
      { id: 'coding', type: 'codebox', x: 0, y: 0.3, label: 'Coding C++ / Python', color: P.process },
      { id: 'compile', type: 'process', x: 0, y: 1.2, label: 'Compile & debug', color: P.output },
      { id: 'uji', type: 'decision', x: 0, y: 2.1, label: 'Lulus uji?' },
      { id: 'end', type: 'end', x: 1.6, y: 2.1, label: 'Rilis', color: P.green },
    ],
    links: [
      { from: 'start', to: 'analisis', color: P.ink2, packets: 1 },
      { from: 'analisis', to: 'desain', color: P.process, packets: 1 },
      { from: 'desain', to: 'coding', color: P.violet, packets: 1 },
      { from: 'coding', to: 'compile', color: P.process, packets: 1 },
      { from: 'compile', to: 'uji', color: P.ink2, packets: 1 },
      { from: 'uji', to: 'end', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'uji', to: 'coding', color: P.danger, dashed: true, packets: 1, label: 'TIDAK', lift: 430 },
    ],
  },

  // 7. Simbol flowchart ISO 5807
  {
    nodes: [
      { id: 'start', type: 'start', x: -2.1, y: -1.0, label: 'Terminator' },
      { id: 'io', type: 'io', x: 0, y: -1.0, label: 'Data / I/O' },
      { id: 'dec', type: 'decision', x: 2.1, y: -1.0, label: 'Decision' },
      { id: 'proc', type: 'process', x: -2.1, y: 0.35, label: 'Process', sub: 'pemrosesan', color: P.blueSoft },
      { id: 'prep', type: 'process', x: 0, y: 0.35, label: 'Preparation', sub: 'loop setup', color: P.violet },
      { id: 'conn', type: 'connector', x: 2.1, y: 0.35, label: 'A' },
    ],
    links: [{ from: 'start', to: 'io', color: P.ink2, packets: 1, label: 'flowline' }],
  },

  // 8. Studi kasus tarif parkir
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Mulai' },
      { id: 'io', type: 'io', x: 0, y: -1.15, label: 'Input: jam masuk, jam keluar' },
      { id: 'proc', type: 'process', x: 0, y: -0.3, label: 'Durasi = keluar − masuk', color: P.blueSoft },
      { id: 'dec', type: 'decision', x: 0, y: 0.55, label: 'Durasi ≤ 2 jam?' },
      { id: 'yes', type: 'process', x: -1.6, y: 1.55, label: 'Biaya = 5.000', color: P.green },
      { id: 'no', type: 'process', x: 1.6, y: 1.55, label: 'Biaya = 5.000 + (d−2) × 3.000', color: P.violet },
      { id: 'join', type: 'connector', x: 0, y: 2.5, label: 'A' },
      { id: 'end', type: 'end', x: 0, y: 3.2, label: 'Selesai', color: P.green },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'proc', color: P.process, packets: 1 },
      { from: 'proc', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'dec', to: 'no', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'yes', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'no', to: 'join', color: P.violet, packets: 1 },
      { from: 'join', to: 'end', color: P.ink2, packets: 1 },
    ],
  },

  // 9. Pseudocode terstruktur
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.1, label: 'Mulai' },
      { id: 'program', type: 'codebox', x: 0, y: -1.25, label: 'PROGRAM HitungTarif', sub: 'identitas program', color: P.output },
      { id: 'deklarasi', type: 'process', x: -1.6, y: -0.05, label: 'DEKLARASI', sub: 'variabel & tipe', color: P.raw },
      { id: 'algoritma', type: 'process', x: 1.6, y: -0.05, label: 'ALGORITMA', sub: 'read · if · write', color: P.violet },
      { id: 'write', type: 'codebox', x: 0, y: 1.15, label: 'write(biaya)', sub: 'output', color: P.process },
      { id: 'end', type: 'end', x: 0, y: 2.05, label: 'Selesai', color: P.green },
    ],
    links: [
      { from: 'start', to: 'program', color: P.ink2, packets: 1 },
      { from: 'program', to: 'deklarasi', color: P.process, packets: 1 },
      { from: 'program', to: 'algoritma', color: P.violet, packets: 1 },
      { from: 'deklarasi', to: 'write', color: P.ink2, packets: 1 },
      { from: 'algoritma', to: 'write', color: P.ink2, packets: 1 },
      { from: 'write', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 10. Kompilasi vs interpretasi
  {
    nodes: [
      { id: 'cpp', type: 'io', x: -2.2, y: -1.7, label: 'source.cpp' },
      { id: 'compiler', type: 'process', x: -2.2, y: -0.8, label: 'Compiler', sub: 'g++ / clang++', color: P.process },
      { id: 'binary', type: 'process', x: -2.2, y: 0.1, label: 'Biner mesin', sub: '.exe / a.out', color: P.raw },
      { id: 'cpuA', type: 'process', x: -2.2, y: 1.0, label: 'CPU', sub: 'eksekusi langsung', color: P.green },
      { id: 'py', type: 'io', x: 1.5, y: -1.7, label: 'script.py' },
      { id: 'bytecode', type: 'process', x: 1.5, y: -0.8, label: 'Bytecode', sub: '.pyc', color: P.violet },
      { id: 'pvm', type: 'process', x: 1.5, y: 0.1, label: 'PVM', sub: 'interpreter', color: P.process },
      { id: 'cpuB', type: 'process', x: 1.5, y: 1.0, label: 'CPU', sub: 'per baris', color: P.green },
    ],
    links: [
      { from: 'cpp', to: 'compiler', color: P.process, packets: 1 },
      { from: 'compiler', to: 'binary', color: P.output, packets: 1, label: 'sekali' },
      { from: 'binary', to: 'cpuA', color: P.greenDark, packets: 1, label: 'cepat' },
      { from: 'py', to: 'bytecode', color: P.process, packets: 1 },
      { from: 'bytecode', to: 'pvm', color: P.violet, packets: 1, label: 'per baris' },
      { from: 'pvm', to: 'cpuB', color: P.greenDark, packets: 1, label: 'fleksibel' },
    ],
  },

  // 11. Implementasi dua bahasa
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'Mulai' },
      { id: 'io', type: 'io', x: 0, y: -1.2, label: 'Input: suhu Celcius' },
      { id: 'cpp', type: 'process', x: -1.6, y: -0.2, label: 'C++', sub: 'compiled', color: P.process },
      { id: 'py', type: 'process', x: 1.6, y: -0.2, label: 'Python', sub: 'interpreted', color: P.green },
      { id: 'valid', type: 'process', x: 0, y: 0.85, label: 'Validasi hasil', sub: 'kasus batas 0 K', color: P.output },
      { id: 'dec', type: 'decision', x: 0, y: 1.75, label: 'Output sama?' },
      { id: 'end', type: 'end', x: -1.6, y: 2.5, label: 'Rilis', color: P.green },
      { id: 'fail', type: 'end', x: 1.6, y: 2.5, label: 'Debug', status: 'failed' },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'cpp', color: P.process, packets: 1 },
      { from: 'io', to: 'py', color: P.greenDark, packets: 1 },
      { from: 'cpp', to: 'valid', color: P.process, packets: 1 },
      { from: 'py', to: 'valid', color: P.greenDark, packets: 1 },
      { from: 'valid', to: 'dec', color: P.output, packets: 1 },
      { from: 'dec', to: 'end', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'dec', to: 'fail', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
    ],
  },
]
