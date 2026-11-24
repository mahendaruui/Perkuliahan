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
      { id: 'bits', type: 'bitreg', x: -3.4, y: 0.4, sub: '01000001', label: '8-bit RAM (01000001)', color: P.process },
      { id: 'cpu', type: 'chip', x: -0.6, y: 0.0, label: 'Decoder Tipe' },
      { id: 'asInt', type: 'valuebox', x: 2.6, y: -2.2, sub: '65', label: 'Hasil int', color: P.process },
      { id: 'asChar', type: 'valuebox', x: 3.2, y: 1.4, sub: "'A'", label: 'Hasil char', color: P.output },
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
      { id: 'stack', type: 'container', x: -4.2, y: 2.1, label: 'Stack ↓ (Lokal)', color: P.process },
      { id: 'heap', type: 'ram', x: -2.1, y: 1.05, sub: 'Dinamis', label: 'Heap ↑', color: P.violet },
      { id: 'bss', type: 'ram', x: 0.0, y: 0.0, sub: '= 0', label: 'BSS (Belum Init)', color: P.raw },
      { id: 'data', type: 'ram', x: 2.1, y: -1.05, sub: 'Global', label: 'Data (Terisi)', color: P.output },
      { id: 'text', type: 'shield', x: 4.2, y: -2.1, label: 'Text (Read-Only)', color: P.greenDark },
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
      { id: 'name', type: 'valuebox', x: -3.6, y: 0.8, sub: 'umur', label: '1. Identifier', color: P.raw },
      { id: 'type', type: 'gate', x: -1.2, y: 0.2, sub: 'int 4B', label: '2. Data Type', color: P.process },
      { id: 'addr', type: 'ram', x: 1.2, y: -0.4, sub: '0x7ffe', label: '3. Alamat RAM', color: P.violet },
      { id: 'val', type: 'valuebox', x: 3.6, y: -1.2, sub: '21', label: '4. Nilai Data', color: P.output },
      { id: 'constLock', type: 'shield', x: 4.2, y: 2.4, label: 'Kunci const / Final', color: P.greenDark },
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
      { id: 'bool', type: 'block', x: -4.8, y: 2.4, label: 'bool · 1B', color: P.raw, scale: 0.9 },
      { id: 'char', type: 'block', x: -3.0, y: 1.5, label: 'char · 1B', color: P.raw, scale: 0.9 },
      { id: 'int', type: 'ram', x: -1.0, y: 0.5, sub: '4B', label: 'int · 32-bit', color: P.process },
      { id: 'float', type: 'ram', x: 1.0, y: -0.5, sub: '4B', label: 'float · IEEE', color: P.violet },
      { id: 'll', type: 'ram', x: 3.2, y: -1.6, sub: '8B', label: 'long long · 64-bit', color: P.output },
      { id: 'dbl', type: 'ram', x: 5.4, y: -2.7, sub: '8B', label: 'double · 15-17d', color: P.green },
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
      { id: 'pos', type: 'bitreg', x: -3.6, y: 1.2, sub: '00101101', label: '+45 (Asli)', color: P.process },
      { id: 'inv', type: 'gate', x: -1.0, y: 0.3, sub: '~', label: '1. Invert Bit', color: P.violet },
      { id: 'plus1', type: 'gate', x: 1.4, y: -0.5, sub: '+ 1', label: '2. Tambah 1', color: P.output },
      { id: 'neg', type: 'bitreg', x: 3.8, y: -1.4, sub: '11010011', label: '−45 (MSB=1)', color: P.output },
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
      { id: 'max', type: 'valuebox', x: -3.6, y: 1.2, sub: '2147483647', label: 'INT_MAX (32-bit)', color: P.process },
      { id: 'add', type: 'gate', x: -1.0, y: 0.3, sub: '+ 1', label: 'Tambah 1', color: P.output },
      { id: 'boom', type: 'gauge', x: 1.4, y: -0.5, label: 'Batas Bit Jebol!' },
      { id: 'min', type: 'valuebox', x: 3.8, y: -1.4, sub: '-2147483648', label: 'Wrap ke INT_MIN', status: 'failed', color: P.danger },
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
      { id: 'dec', type: 'valuebox', x: -3.5, y: 0.6, sub: '0.1 + 0.2', label: 'Desimal Basis-10', color: P.raw },
      { id: 'ieee', type: 'chip', x: -0.4, y: 0.0, label: 'Konversi IEEE 754' },
      { id: 'exactErr', type: 'valuebox', x: 2.6, y: -2.2, sub: '== 0.3 ?', label: 'FALSE (0.30000004)', status: 'failed', color: P.danger },
      { id: 'eps', type: 'shield', x: 3.0, y: 1.4, label: 'Aman: |a−b| < 1e-9', color: P.greenDark },
    ],
    links: [
      { from: 'dec', to: 'ieee', color: P.process, packets: 1 },
      { from: 'ieee', to: 'exactErr', color: P.danger, dashed: true, packets: 1, label: 'pembulatan biner' },
      { from: 'ieee', to: 'eps', color: P.greenDark, packets: 2, label: 'pakai epsilon', lift: 44 },
    ],
  },

  // 8. Static vs Dynamic Typing
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -3.6, y: -1.4, label: 'C++ (Compile-Time)', color: P.process },
      { id: 'stack', type: 'ram', x: -0.2, y: -2.2, sub: '4 Byte', label: 'Ukuran Tetap (Stack)', color: P.process },
      { id: 'py', type: 'code', x: -0.8, y: 2.2, label: 'Python (Runtime)', color: P.green },
      { id: 'heapObj', type: 'container', x: 2.2, y: 1.6, label: 'Objek Dinamis (Heap)', color: P.output },
      { id: 'bignum', type: 'valuebox', x: 4.8, y: 0.4, sub: '2^63 + 1', label: 'Bignum Bebas Overflow', color: P.green },
    ],
    links: [
      { from: 'cpp', to: 'stack', color: P.process, packets: 1, label: 'terkunci' },
      { from: 'py', to: 'heapObj', color: P.greenDark, packets: 1, label: 'dinamis' },
      { from: 'heapObj', to: 'bignum', color: P.output, dashed: true, packets: 2, label: 'otomatis membesar' },
    ],
  },

  // 9. Type Casting
  {
    nodes: [
      { id: 'div', type: 'valuebox', x: -3.6, y: 0.4, sub: '275 / 3', label: 'Dua Integer', color: P.raw },
      { id: 'trunc', type: 'funnel', x: -0.2, y: -1.8, label: 'Potong Desimal', color: P.danger },
      { id: 'resBad', type: 'valuebox', x: 2.8, y: -2.1, sub: '91', label: 'Hilang .6667', status: 'failed', color: P.danger },
      { id: 'cast', type: 'gate', x: -0.2, y: 1.8, sub: 'static_cast', label: 'Explicit Cast', color: P.process },
      { id: 'resOk', type: 'valuebox', x: 2.8, y: 1.9, sub: '91.6667', label: 'Presisi Terjaga', color: P.output },
    ],
    links: [
      { from: 'div', to: 'trunc', color: P.danger, dashed: true, packets: 1, label: 'implisit int' },
      { from: 'trunc', to: 'resBad', color: P.danger, packets: 1 },
      { from: 'div', to: 'cast', color: P.process, packets: 2, label: 'eksplisit' },
      { from: 'cast', to: 'resOk', color: P.output, packets: 2 },
    ],
  },

  // 10. Inspeksi Memori Dual-Stack
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -3.6, y: -1.2, label: 'C++: sizeof() & &var', color: P.process },
      { id: 'py', type: 'code', x: -0.8, y: 2.4, label: 'Python: getsizeof() & id()', color: P.green },
      { id: 'ram', type: 'ram', x: 1.2, y: -0.2, sub: '0x1000', label: 'Alamat & Byte RAM', color: P.violet },
      { id: 'out', type: 'valuebox', x: 4.0, y: -0.8, sub: '4B / 28B', label: 'Terukur Eksak', color: P.output },
    ],
    links: [
      { from: 'cpp', to: 'ram', color: P.process, packets: 1 },
      { from: 'py', to: 'ram', color: P.greenDark, packets: 1 },
      { from: 'ram', to: 'out', color: P.output, packets: 2, label: 'byte & hex' },
    ],
  },
]
