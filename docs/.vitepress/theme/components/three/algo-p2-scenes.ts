import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 2 — Flowchart: Variabel, Tipe Data & Memori RAM             */
/* ------------------------------------------------------------------ */

export const algoP2Scenes: IsoScene[] = [
  // 1. RAM hanya menyimpan bit
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Program berjalan' },
      { id: 'io', type: 'io', x: 0, y: -1.1, label: 'RAM: 0100 1010 1100 ...' },
      { id: 'dec', type: 'decision', x: 0, y: -0.05, label: 'Ada tipe data?' },
      { id: 'raw', type: 'process', x: -1.6, y: 1.05, label: 'Semua bit mentah', status: 'failed' },
      { id: 'rawEnd', type: 'end', x: -1.6, y: 2.05, label: 'Salah baca', status: 'failed' },
      { id: 'typed', type: 'process', x: 1.6, y: 1.05, label: 'Variabel memberi makna', color: P.green },
      { id: 'typedEnd', type: 'end', x: 1.6, y: 2.05, label: 'Nilai terbaca', color: P.green },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'raw', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'raw', to: 'rawEnd', color: P.danger, packets: 1 },
      { from: 'dec', to: 'typed', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'typed', to: 'typedEnd', color: P.greenDark, packets: 1 },
    ],
  },

  // 2. Lima segmen memori
  {
    nodes: [
      { id: 'stack', type: 'process', x: 0, y: -1.5, label: 'Stack', sub: 'alamat tinggi · lokal', color: P.blueSoft },
      { id: 'heap', type: 'process', x: 0, y: -0.75, label: 'Heap', sub: 'alokasi dinamis', color: P.violet },
      { id: 'bss', type: 'process', x: 0, y: 0.0, label: 'BSS', sub: 'global = 0', color: P.raw },
      { id: 'data', type: 'process', x: 0, y: 0.75, label: 'Data', sub: 'global terisi', color: P.output },
      { id: 'text', type: 'process', x: 0, y: 1.5, label: 'Text', sub: 'alamat rendah · read-only', color: P.green },
    ],
    links: [],
  },

  // 3. Anatomi variabel & konstanta
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'int umur = 21' },
      { id: 'tipe', type: 'process', x: -1.7, y: -1.0, label: 'Tipe: int', sub: '4 byte', color: P.process },
      { id: 'nama', type: 'process', x: 1.7, y: -1.0, label: 'Nama: umur', sub: 'identifier', color: P.violet },
      { id: 'nilai', type: 'process', x: 0, y: 0.0, label: 'Nilai: 21', sub: 'isi memori', color: P.output },
      { id: 'alamat', type: 'process', x: 0, y: 0.9, label: 'Alamat: 0x7FF', sub: 'lokasi byte', color: P.raw },
      { id: 'dec', type: 'decision', x: 0, y: 1.75, label: 'const?' },
      { id: 'ro', type: 'end', x: -1.6, y: 1.75, label: 'read-only', color: P.green },
      { id: 'rw', type: 'end', x: 1.6, y: 1.75, label: 'bisa diubah', color: P.blueSoft },
    ],
    links: [
      { from: 'start', to: 'tipe', color: P.ink2, packets: 1 },
      { from: 'start', to: 'nama', color: P.ink2, packets: 1 },
      { from: 'tipe', to: 'nilai', color: P.process, packets: 1 },
      { from: 'nama', to: 'nilai', color: P.violet, packets: 1 },
      { from: 'nilai', to: 'alamat', color: P.ink2, packets: 1 },
      { from: 'alamat', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'ro', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'dec', to: 'rw', color: P.ink2, packets: 1, label: 'TIDAK' },
    ],
  },

  // 4. Tipe data primitif
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'Pilih tipe data' },
      { id: 'd1', type: 'decision', x: 0, y: -1.0, label: 'Butuh desimal?' },
      { id: 'f', type: 'end', x: 1.6, y: -1.0, label: 'float / double', sub: '4 / 8 byte', color: P.green },
      { id: 'd2', type: 'decision', x: 0, y: 0.0, label: 'Butuh teks?' },
      { id: 'c', type: 'end', x: -1.6, y: 0.0, label: 'char', sub: '1 byte', color: P.green },
      { id: 'i', type: 'end', x: 0, y: 1.1, label: 'int / bool', sub: '4 / 1 byte', color: P.green },
    ],
    links: [
      { from: 'start', to: 'd1', color: P.ink2, packets: 1 },
      { from: 'd1', to: 'f', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'd1', to: 'd2', color: P.ink2, packets: 1, label: 'TIDAK' },
      { from: 'd2', to: 'c', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'd2', to: 'i', color: P.greenDark, packets: 1, label: 'TIDAK' },
    ],
  },

  // 5. Two's Complement
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.8, label: '5 = 0000 0101' },
      { id: 'invert', type: 'process', x: 0, y: -0.9, label: 'Balik semua bit', sub: '1111 1010', color: P.violet },
      { id: 'add', type: 'process', x: 0, y: 0.0, label: 'Tambah 1', sub: '1111 1011', color: P.process },
      { id: 'read', type: 'process', x: 0, y: 0.9, label: 'Baca sebagai negatif', sub: '−5', color: P.output },
      { id: 'end', type: 'end', x: 0, y: 1.8, label: "Two's Complement", color: P.green },
    ],
    links: [
      { from: 'start', to: 'invert', color: P.ink2, packets: 1 },
      { from: 'invert', to: 'add', color: P.violet, packets: 1 },
      { from: 'add', to: 'read', color: P.process, packets: 1 },
      { from: 'read', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 6. Integer overflow
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'Mulai' },
      { id: 'val', type: 'process', x: 0, y: -1.15, label: 'int8 = 127', sub: '0111 1111', color: P.raw },
      { id: 'dec', type: 'decision', x: 0, y: -0.2, label: '127 + 1 masih muat?' },
      { id: 'yes', type: 'process', x: 1.6, y: -0.2, label: 'Overflow', sub: 'wrap / undefined', status: 'failed' },
      { id: 'no', type: 'process', x: -1.6, y: -0.2, label: 'Masih aman', color: P.green },
      { id: 'endY', type: 'end', x: 1.6, y: 0.9, label: '−128 atau UB', status: 'failed' },
      { id: 'endN', type: 'end', x: -1.6, y: 0.9, label: '128', color: P.green },
    ],
    links: [
      { from: 'start', to: 'val', color: P.ink2, packets: 1 },
      { from: 'val', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'yes', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'dec', to: 'no', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'yes', to: 'endY', color: P.danger, packets: 1 },
      { from: 'no', to: 'endN', color: P.greenDark, packets: 1 },
    ],
  },

  // 7. IEEE 754
  {
    nodes: [
      { id: 'io', type: 'io', x: 0, y: -1.6, label: 'Hitung 0.1 + 0.2' },
      { id: 'bin', type: 'process', x: 0, y: -0.8, label: 'Konversi ke biner', sub: 'pecahan berulang', color: P.process },
      { id: 'round', type: 'process', x: 0, y: 0.05, label: 'Bulatkan mantissa', sub: '23 bit', color: P.violet },
      { id: 'res', type: 'process', x: 0, y: 0.9, label: 'Hasil floating point', sub: '0.30000000000000004', color: P.raw },
      { id: 'dec', type: 'decision', x: 0, y: 1.75, label: 'Tepat 0.3?' },
      { id: 'eps', type: 'process', x: 1.6, y: 1.75, label: 'Pakai epsilon', sub: 'abs(a−b) < 1e-9', color: P.green },
      { id: 'end', type: 'end', x: 0, y: 2.55, label: 'Perbandingan aman', color: P.green },
    ],
    links: [
      { from: 'io', to: 'bin', color: P.ink2, packets: 1 },
      { from: 'bin', to: 'round', color: P.process, packets: 1 },
      { from: 'round', to: 'res', color: P.violet, packets: 1 },
      { from: 'res', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'eps', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'eps', to: 'end', color: P.greenDark, packets: 1 },
      { from: 'dec', to: 'end', color: P.greenDark, packets: 1, label: 'YA' },
    ],
  },

  // 8. Static vs dynamic typing
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'Deklarasi variabel' },
      { id: 'dec', type: 'decision', x: 0, y: -1.0, label: 'Kapan tipe dicek?' },
      { id: 'cpp', type: 'process', x: -1.7, y: 0.15, label: 'C++ · statis', sub: 'compile time', color: P.process },
      { id: 'py', type: 'process', x: 1.7, y: 0.15, label: 'Python · dinamis', sub: 'runtime', color: P.green },
      { id: 'join', type: 'connector', x: 0, y: 1.25, label: 'A' },
      { id: 'end', type: 'end', x: 0, y: 2.0, label: 'Program berjalan', color: P.green },
    ],
    links: [
      { from: 'start', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'cpp', color: P.process, packets: 1, label: 'COMPILE' },
      { from: 'dec', to: 'py', color: P.greenDark, packets: 1, label: 'RUNTIME' },
      { from: 'cpp', to: 'join', color: P.process, packets: 1 },
      { from: 'py', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'join', to: 'end', color: P.ink2, packets: 1 },
    ],
  },

  // 9. Type casting
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'int a = 5, b = 2' },
      { id: 'dec', type: 'decision', x: 0, y: -0.9, label: 'Butuh hasil desimal?' },
      { id: 'no', type: 'process', x: 1.6, y: -0.9, label: 'a / b = 2', sub: 'integer division', status: 'failed' },
      { id: 'yes', type: 'process', x: -1.6, y: -0.9, label: 'float(a) / b', sub: '= 2.5', color: P.green },
      { id: 'endNo', type: 'end', x: 1.6, y: 0.3, label: 'Data hilang', status: 'failed' },
      { id: 'endYes', type: 'end', x: -1.6, y: 0.3, label: 'Presisi aman', color: P.green },
    ],
    links: [
      { from: 'start', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'no', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'no', to: 'endNo', color: P.danger, packets: 1 },
      { from: 'yes', to: 'endYes', color: P.greenDark, packets: 1 },
    ],
  },

  // 10. Inspeksi ukuran di dua bahasa
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.1, label: 'Cek ukuran tipe' },
      { id: 'io1', type: 'io', x: 0, y: -1.3, label: 'C++: sizeof(int)' },
      { id: 'p1', type: 'process', x: 0, y: -0.45, label: '4 byte', sub: 'nilai langsung', color: P.process },
      { id: 'io2', type: 'io', x: 0, y: 0.4, label: 'Python: sys.getsizeof(int)' },
      { id: 'p2', type: 'process', x: 0, y: 1.25, label: '28 byte', sub: 'objek + header', color: P.violet },
      { id: 'end', type: 'end', x: 0, y: 2.1, label: 'Pahami overhead', color: P.green },
    ],
    links: [
      { from: 'start', to: 'io1', color: P.ink2, packets: 1 },
      { from: 'io1', to: 'p1', color: P.process, packets: 1 },
      { from: 'p1', to: 'io2', color: P.ink2, packets: 1 },
      { from: 'io2', to: 'p2', color: P.violet, packets: 1 },
      { from: 'p2', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },
]
