import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 2 — Variabel, Tipe Data & Dekonstruksi Memori Komputer       */
/* ------------------------------------------------------------------ */

export const algoP2Scenes: IsoScene[] = [
  // 1. RAM hanya menyimpan bit 0 dan 1
  {
    nodes: [
      { id: 'bits', type: 'block', x: -2.6, y: 1.1, label: '01000001', color: P.raw, scale: 1.3 },
      { id: 'cpu', type: 'chip', x: -0.2, y: 0.2, label: 'Decoder Tipe' },
      { id: 'asInt', type: 'dashboard', x: 2.0, y: -1.4, label: 'int → 65', color: P.process },
      { id: 'asChar', type: 'file', x: 2.0, y: 1.6, label: "char → 'A'", color: P.output },
    ],
    links: [
      { from: 'bits', to: 'cpu', color: P.ink2, packets: 2, label: '1 byte' },
      { from: 'cpu', to: 'asInt', color: P.process, packets: 1, label: 'angka' },
      { from: 'cpu', to: 'asChar', color: P.output, packets: 1, label: 'ASCII' },
    ],
  },

  // 2. Lima segmen memori program
  {
    nodes: [
      { id: 'stack', type: 'server', x: -3.0, y: 1.4, label: 'Stack ↓', color: P.process, status: 'active' },
      { id: 'heap', type: 'container', x: -1.5, y: 0.7, label: 'Heap ↑', color: P.violet },
      { id: 'bss', type: 'folder', x: 0.0, y: 0.0, label: 'BSS (0)' },
      { id: 'data', type: 'disk', x: 1.5, y: -0.7, label: 'Data', color: P.output },
      { id: 'text', type: 'shield', x: 3.0, y: -1.4, label: 'Text (RO)', color: P.rawDark },
    ],
    links: [
      { from: 'stack', to: 'heap', color: P.process, dashed: true, packets: 1, label: 'dinamis' },
      { from: 'heap', to: 'bss', color: P.ink2, dashed: true, packets: 1 },
      { from: 'bss', to: 'data', color: P.output, dashed: true, packets: 1 },
      { from: 'data', to: 'text', color: P.ink2, dashed: true, packets: 1 },
    ],
  },

  // 3. Empat atribut variabel & konstanta
  {
    nodes: [
      { id: 'name', type: 'tag', x: -2.8, y: 1.2, label: 'umurMahasiswa', fill: P.goldSoft },
      { id: 'type', type: 'prism', x: -0.9, y: 0.4, label: 'int (4B)' },
      { id: 'addr', type: 'grid', x: 1.0, y: -0.4, label: '0x7ffee4b6', color: P.process },
      { id: 'val', type: 'block', x: 2.8, y: -1.2, label: '21', color: P.output, scale: 1.3 },
      { id: 'constLock', type: 'shield', x: 0.9, y: 1.9, label: 'const / Final', color: P.greenDark },
    ],
    links: [
      { from: 'name', to: 'type', color: P.ink2, packets: 1 },
      { from: 'type', to: 'addr', color: P.process, packets: 1 },
      { from: 'addr', to: 'val', color: P.output, packets: 2 },
      { from: 'constLock', to: 'val', color: P.greenDark, dashed: true, packets: 1, label: 'immutable' },
    ],
  },

  // 4. Tipe primitif & ukuran byte
  {
    nodes: [
      { id: 'bool', type: 'block', x: -3.2, y: 1.5, label: 'bool · 1B', color: P.raw, scale: 0.85 },
      { id: 'char', type: 'block', x: -2.0, y: 0.9, label: 'char · 1B', color: P.raw, scale: 0.85 },
      { id: 'int', type: 'block', x: -0.7, y: 0.3, label: 'int · 4B', color: P.process, scale: 1.15 },
      { id: 'float', type: 'block', x: 0.6, y: -0.3, label: 'float · 4B', color: P.violet, scale: 1.15 },
      { id: 'll', type: 'block', x: 1.9, y: -0.9, label: 'long long · 8B', color: P.output, scale: 1.45 },
      { id: 'dbl', type: 'block', x: 3.3, y: -1.5, label: 'double · 8B', color: P.green, scale: 1.45 },
    ],
    links: [
      { from: 'bool', to: 'char', color: P.ink2, dashed: true, packets: 1 },
      { from: 'char', to: 'int', color: P.process, packets: 1 },
      { from: 'int', to: 'float', color: P.ink2, dashed: true, packets: 1 },
      { from: 'float', to: 'll', color: P.output, packets: 1 },
      { from: 'll', to: 'dbl', color: P.greenDark, dashed: true, packets: 1 },
    ],
  },

  // 5. Two's Complement
  {
    nodes: [
      { id: 'pos', type: 'block', x: -2.6, y: 1.2, label: '+45 (00101101)', color: P.process, scale: 1.2 },
      { id: 'inv', type: 'factory', x: -0.3, y: 0.2, label: 'Invert Bit (~)', color: P.violet },
      { id: 'plus1', type: 'prism', x: 1.6, y: -0.6, label: '+ 1' },
      { id: 'neg', type: 'block', x: 3.2, y: -1.4, label: '−45 (11010011)', color: P.output, scale: 1.2 },
    ],
    links: [
      { from: 'pos', to: 'inv', color: P.process, packets: 1 },
      { from: 'inv', to: 'plus1', color: P.violet, packets: 1 },
      { from: 'plus1', to: 'neg', color: P.output, packets: 2, label: 'MSB = 1' },
    ],
  },

  // 6. Integer Overflow
  {
    nodes: [
      { id: 'max', type: 'gauge', x: -2.6, y: 1.2, label: 'INT_MAX' },
      { id: 'add', type: 'block', x: -0.4, y: 0.2, label: '+ 1', color: P.process, scale: 1.1 },
      { id: 'boom', type: 'server', x: 1.6, y: -0.7, label: 'Overflow!', status: 'smoke', color: P.danger },
      { id: 'min', type: 'block', x: 3.3, y: -1.5, label: '-2.147.483.648', color: P.danger, scale: 1.3 },
    ],
    links: [
      { from: 'max', to: 'add', color: P.process, packets: 1 },
      { from: 'add', to: 'boom', color: P.danger, packets: 2, label: 'bit tanda terbalik' },
      { from: 'boom', to: 'min', color: P.dangerDark, dashed: true, packets: 2 },
    ],
  },

  // 7. IEEE 754 Floating-Point Imprecision
  {
    nodes: [
      { id: 'dec', type: 'source', x: -2.8, y: 1.2, label: '0.1 + 0.2', color: P.raw },
      { id: 'ieee', type: 'chip', x: -0.6, y: 0.2, label: 'IEEE 754' },
      { id: 'exactErr', type: 'wall', x: 1.3, y: -0.6, label: '== 0.3 FALSE' },
      { id: 'eps', type: 'shield', x: 3.0, y: -1.4, label: 'Epsilon < 1e-9', color: P.greenDark },
    ],
    links: [
      { from: 'dec', to: 'ieee', color: P.process, packets: 1 },
      { from: 'ieee', to: 'exactErr', color: P.danger, dashed: true, packets: 1, label: '0.30000000000000004' },
      { from: 'ieee', to: 'eps', color: P.greenDark, packets: 2, label: 'aman', lift: 75 },
    ],
  },

  // 8. Static vs Dynamic Typing
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -2.9, y: 1.2, label: 'C++ Static', color: P.process },
      { id: 'stack', type: 'block', x: -0.8, y: 2.0, label: '4B Tetap', color: P.process, scale: 1.15 },
      { id: 'py', type: 'code', x: -1.0, y: -1.2, label: 'Python Dynamic', color: P.green },
      { id: 'heapObj', type: 'container', x: 1.4, y: -0.5, label: 'Objek Heap', color: P.output },
      { id: 'bignum', type: 'tower', x: 3.1, y: -1.4, label: 'Bignum', color: P.greenDark },
    ],
    links: [
      { from: 'cpp', to: 'stack', color: P.process, packets: 1, label: 'compile-time' },
      { from: 'py', to: 'heapObj', color: P.greenDark, packets: 1, label: 'runtime' },
      { from: 'heapObj', to: 'bignum', color: P.output, dashed: true, packets: 2, label: 'bebas overflow' },
    ],
  },

  // 9. Type Casting
  {
    nodes: [
      { id: 'div', type: 'source', x: -2.9, y: 1.2, label: '275 / 3', color: P.raw },
      { id: 'trunc', type: 'funnel', x: -0.7, y: 2.0, label: 'Int Division', color: P.danger },
      { id: 'resBad', type: 'block', x: 1.6, y: 2.2, label: '91 (hilang)', color: P.danger, scale: 1.1 },
      { id: 'cast', type: 'prism', x: -0.5, y: -0.9, label: 'static_cast<double>' },
      { id: 'resOk', type: 'dashboard', x: 2.2, y: -1.3, label: '91.6667', color: P.output },
    ],
    links: [
      { from: 'div', to: 'trunc', color: P.danger, dashed: true, packets: 1 },
      { from: 'trunc', to: 'resBad', color: P.danger, packets: 1 },
      { from: 'div', to: 'cast', color: P.process, packets: 2, label: 'eksplisit' },
      { from: 'cast', to: 'resOk', color: P.output, packets: 2 },
    ],
  },

  // 10. Inspeksi Memori Dual-Stack
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -2.7, y: 1.2, label: 'sizeof() & &var', color: P.process },
      { id: 'py', type: 'code', x: -0.6, y: -1.1, label: 'getsizeof() & id()', color: P.green },
      { id: 'ram', type: 'grid', x: 1.6, y: 0.2, label: 'Peta RAM', color: P.violet, scale: 1.2 },
      { id: 'out', type: 'dashboard', x: 3.4, y: -0.8, label: 'Terverifikasi', color: P.output },
    ],
    links: [
      { from: 'cpp', to: 'ram', color: P.process, packets: 1 },
      { from: 'py', to: 'ram', color: P.greenDark, packets: 1 },
      { from: 'ram', to: 'out', color: P.output, packets: 2, label: 'byte & hex' },
    ],
  },
]
