import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 1 — Pengenalan Algoritma & Pemrograman                       */
/* ------------------------------------------------------------------ */

export const algoP1Scenes: IsoScene[] = [
  // 1. Instruksi ambigu
  {
    nodes: [
      { id: 'instr', type: 'file', x: -2.8, y: 1.3, label: 'instruksi', color: P.raw, scale: 1.05 },
      { id: 'a', type: 'server', x: -0.9, y: 0.6, label: 'Mesin A', color: P.process, status: 'active' },
      { id: 'b', type: 'server', x: 0.9, y: -0.2, label: 'Mesin B', color: P.violet },
      { id: 'ra', type: 'block', x: -1.0, y: 2.0, color: P.output, label: '2 sdm' },
      { id: 'rb', type: 'block', x: 1.8, y: 1.4, color: P.danger, label: '1 cangkir' },
    ],
    links: [
      { from: 'instr', to: 'a', color: P.process, packets: 1, label: 'baca' },
      { from: 'instr', to: 'b', color: P.violet, packets: 1 },
      { from: 'a', to: 'ra', color: P.output, packets: 1 },
      { from: 'b', to: 'rb', color: P.danger, packets: 1 },
    ],
  },

  // 2. Sejarah
  {
    nodes: [
      { id: 'khwarizmi', type: 'book', x: -2.6, y: 1.2, label: 'Al-Khwarizmi' },
      { id: 'ada', type: 'code', x: -0.4, y: 0.2, label: 'Ada Lovelace', color: P.process },
      { id: 'turing', type: 'chip', x: 2.0, y: -0.8, label: 'Alan Turing' },
    ],
    links: [
      { from: 'khwarizmi', to: 'ada', color: P.ink2, dashed: true, packets: 1, label: 'aljabar' },
      { from: 'ada', to: 'turing', color: P.ink2, dashed: true, packets: 1, label: 'mesin' },
    ],
  },

  // 3. Definisi input → proses → output
  {
    nodes: [
      { id: 'in', type: 'source', x: -2.6, y: 1.2, label: 'Input', color: P.raw },
      { id: 'proc', type: 'factory', x: -0.2, y: 0.2, label: 'Proses', color: P.process },
      { id: 'out', type: 'dashboard', x: 2.2, y: -0.8, label: 'Output' },
    ],
    links: [
      { from: 'in', to: 'proc', color: P.process, packets: 2, label: 'nilai sah' },
      { from: 'proc', to: 'out', color: P.output, packets: 2, label: 'hasil' },
    ],
  },

  // 4. Lima syarat Knuth
  {
    nodes: [
      { id: 'k1', type: 'gauge', x: -2.9, y: 1.4, label: 'Finiteness' },
      { id: 'k2', type: 'prism', x: -1.45, y: 0.7, label: 'Definiteness' },
      { id: 'k3', type: 'source', x: 0, y: 0, label: 'Input', color: P.raw },
      { id: 'k4', type: 'dashboard', x: 1.45, y: -0.7, label: 'Output' },
      { id: 'k5', type: 'chip', x: 2.9, y: -1.4, label: 'Effectiveness' },
    ],
    links: [
      { from: 'k1', to: 'k2', color: P.ink2, dashed: true, packets: 1 },
      { from: 'k2', to: 'k3', color: P.ink2, dashed: true, packets: 1 },
      { from: 'k3', to: 'k4', color: P.ink2, dashed: true, packets: 1 },
      { from: 'k4', to: 'k5', color: P.ink2, dashed: true, packets: 1 },
    ],
  },

  // 5. Wirth
  {
    nodes: [
      { id: 'algo', type: 'prism', x: -2.4, y: 1.0, label: 'Algoritma' },
      { id: 'data', type: 'grid', x: 0, y: 0, label: 'Struktur Data', color: P.violet, scale: 1.25 },
      { id: 'program', type: 'code', x: 2.2, y: -0.9, label: 'Program', color: P.output },
    ],
    links: [
      { from: 'algo', to: 'data', color: P.process, packets: 1, label: '+' },
      { from: 'data', to: 'program', color: P.output, packets: 1, label: '=' },
    ],
  },

  // 6. Siklus pemecahan masalah
  {
    nodes: [
      { id: 's1', type: 'source', x: -3.0, y: 1.5, label: 'Masalah', color: P.raw },
      { id: 's2', type: 'book', x: -1.7, y: 0.85, label: 'Analisis' },
      { id: 's3', type: 'prism', x: -0.4, y: 0.2, label: 'Desain' },
      { id: 's4', type: 'code', x: 0.9, y: -0.45, label: 'Coding', color: P.process },
      { id: 's5', type: 'factory', x: 2.2, y: -1.1, label: 'Compile', color: P.process, scale: 0.78 },
      { id: 's6', type: 'shield', x: 3.5, y: -1.75, label: 'Uji' },
    ],
    links: [
      { from: 's1', to: 's2', color: P.ink2, dashed: true, packets: 1 },
      { from: 's2', to: 's3', color: P.ink2, dashed: true, packets: 1 },
      { from: 's3', to: 's4', color: P.process, packets: 1 },
      { from: 's4', to: 's5', color: P.process, packets: 1 },
      { from: 's5', to: 's6', color: P.greenDark, packets: 1 },
    ],
  },

  // 7. Simbol flowchart ISO 5807
  {
    nodes: [
      { id: 'start', type: 'symbol', x: -3.0, y: 0.6, label: 'Terminator', status: 'start' },
      { id: 'io', type: 'symbol', x: -1.4, y: -1.0, label: 'Input / Output', status: 'io' },
      { id: 'process', type: 'symbol', x: 0.2, y: -2.6, label: 'Process', status: 'process' },
      { id: 'decision', type: 'symbol', x: -0.6, y: 3.0, label: 'Decision', status: 'decision' },
      { id: 'prep', type: 'symbol', x: 1.0, y: 1.4, label: 'Preparation', status: 'prep' },
      { id: 'connector', type: 'symbol', x: 2.6, y: -0.2, label: 'Connector', status: 'connector' },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1, label: 'flowline' },
    ],
  },

  // 8. Flowchart tarif parkir
  {
    nodes: [
      { id: 'start', type: 'symbol', x: -3.0, y: 1.2, label: 'Mulai', status: 'start' },
      { id: 'io', type: 'symbol', x: -1.8, y: 0.6, label: 'Jam masuk/keluar', status: 'io' },
      { id: 'proc', type: 'symbol', x: -0.6, y: 0.0, label: 'Durasi', status: 'process' },
      { id: 'dec', type: 'symbol', x: 0.6, y: -0.6, label: '≤ 2 jam?', status: 'decision' },
      { id: 'yes', type: 'block', x: 1.9, y: -1.3, color: P.output, label: 'Ya · 5.000', scale: 1.25 },
      { id: 'no', type: 'block', x: 2.2, y: 1.8, color: P.violet, label: 'Tidak · +3.000/jam', scale: 1.25 },
      { id: 'out', type: 'symbol', x: 3.4, y: -1.2, label: 'Selesai', status: 'start', color: P.redSoft },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'proc', color: P.ink2, packets: 1 },
      { from: 'proc', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 1 },
      { from: 'dec', to: 'no', color: P.danger, packets: 1 },
      { from: 'yes', to: 'out', color: P.output, packets: 1 },
      { from: 'no', to: 'out', color: P.violet, packets: 1 },
    ],
  },

  // 9. Pseudocode
  {
    nodes: [
      { id: 'pseudo', type: 'code', x: -2.6, y: 1.2, label: 'Pseudocode', color: P.process },
      { id: 'program', type: 'block', x: -0.6, y: 0.2, color: P.violet, label: 'PROGRAM', scale: 1.5 },
      { id: 'deklarasi', type: 'block', x: 0.6, y: -0.4, color: P.raw, label: 'DEKLARASI', scale: 1.5 },
      { id: 'algoritma', type: 'block', x: 1.8, y: -1.0, color: P.output, label: 'ALGORITMA', scale: 1.5 },
    ],
    links: [
      { from: 'pseudo', to: 'program', color: P.ink2, dashed: true, packets: 1 },
      { from: 'pseudo', to: 'deklarasi', color: P.ink2, dashed: true, packets: 1 },
      { from: 'pseudo', to: 'algoritma', color: P.ink2, dashed: true, packets: 1 },
    ],
  },

  // 10. Kompilasi vs interpretasi
  {
    nodes: [
      { id: 'cpp', type: 'file', x: -3.4, y: 0.7, label: 'source.cpp', color: P.raw },
      { id: 'compiler', type: 'factory', x: -2.6, y: -1.5, label: 'Compiler', color: P.process, scale: 0.85 },
      { id: 'binary', type: 'block', x: -0.5, y: -2.2, color: P.output, label: 'biner', scale: 1.2 },
      { id: 'py', type: 'file', x: -1.1, y: 3.0, label: 'script.py', color: P.raw },
      { id: 'interp', type: 'robot', x: 1.0, y: 2.2, label: 'Interpreter', scale: 1.2 },
      { id: 'bytecode', type: 'block', x: 1.8, y: 0.0, color: P.violet, label: 'bytecode', scale: 1.2 },
    ],
    links: [
      { from: 'cpp', to: 'compiler', color: P.process, packets: 1 },
      { from: 'compiler', to: 'binary', color: P.output, packets: 1, label: 'sekali' },
      { from: 'py', to: 'interp', color: P.process, packets: 1 },
      { from: 'interp', to: 'bytecode', color: P.violet, packets: 1, label: 'per baris' },
    ],
  },

  // 11. Implementasi C++ & Python
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -2.95, y: 1.14, label: 'C++', color: P.process },
      { id: 'py', type: 'code', x: -0.68, y: -1.14, label: 'Python', color: P.green },
      { id: 'valid', type: 'funnel', x: 3.18, y: 1.36, label: 'Validasi', color: P.process },
      { id: 'out', type: 'dashboard', x: 5.0, y: 0.0, label: 'Hasil' },
    ],
    links: [
      { from: 'cpp', to: 'valid', color: P.process, packets: 1 },
      { from: 'py', to: 'valid', color: P.greenDark, packets: 1 },
      { from: 'valid', to: 'out', color: P.output, packets: 2, label: 'suhu' },
    ],
  },
]
