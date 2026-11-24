import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 3 — Flowchart: Operator, Aljabar Boolean & Bitwise          */
/* ------------------------------------------------------------------ */

export const algoP3Scenes: IsoScene[] = [
  // 1. Ekspresi ambigu tanpa aturan urutan
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Ekspresi: 2 + 3 * 4' },
      { id: 'dec', type: 'decision', x: 0, y: -0.9, label: 'Hitung kiri ke kanan?' },
      { id: 'left', type: 'process', x: -1.6, y: -0.9, label: '(2+3)*4 = 20', status: 'failed' },
      { id: 'right', type: 'process', x: 1.6, y: -0.9, label: '2+(3*4) = 14', color: P.green },
      { id: 'endL', type: 'end', x: -1.6, y: 0.3, label: 'Salah', status: 'failed' },
      { id: 'endR', type: 'end', x: 1.6, y: 0.3, label: 'Benar', color: P.green },
    ],
    links: [
      { from: 'start', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'left', color: P.danger, dashed: true, packets: 1, label: 'YA' },
      { from: 'dec', to: 'right', color: P.greenDark, packets: 2, label: 'TIDAK' },
      { from: 'left', to: 'endL', color: P.danger, packets: 1 },
      { from: 'right', to: 'endR', color: P.greenDark, packets: 1 },
    ],
  },

  // 2. Lima keluarga operator
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'Ekspresi' },
      { id: 'p1', type: 'process', x: -2.4, y: -0.6, label: 'Aritmatika', sub: '+ − * / %', color: P.blueSoft },
      { id: 'p2', type: 'process', x: -1.2, y: -0.6, label: 'Relasional', sub: '== != > <', color: P.green },
      { id: 'p3', type: 'process', x: 0, y: -0.6, label: 'Logika', sub: '&& || !', color: P.violet },
      { id: 'p4', type: 'process', x: 1.2, y: -0.6, label: 'Bitwise', sub: '& | ^ ~', color: P.output },
      { id: 'p5', type: 'process', x: 2.4, y: -0.6, label: 'Assignment', sub: '= += −=', color: P.raw },
      { id: 'end', type: 'end', x: 0, y: 0.8, label: 'Satu ekspresi', color: P.green },
    ],
    links: [
      { from: 'start', to: 'p1', color: P.ink2, packets: 1 },
      { from: 'p1', to: 'p2', color: P.ink2, packets: 1 },
      { from: 'p2', to: 'p3', color: P.ink2, packets: 1 },
      { from: 'p3', to: 'p4', color: P.ink2, packets: 1 },
      { from: 'p4', to: 'p5', color: P.ink2, packets: 1 },
      { from: 'p5', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 3. Aljabar Boolean
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'A = TRUE · B = FALSE' },
      { id: 'p1', type: 'process', x: -2.4, y: -0.5, label: 'AND (A && B)', sub: 'FALSE', color: P.blueSoft },
      { id: 'p2', type: 'process', x: -0.8, y: -0.5, label: 'OR (A || B)', sub: 'TRUE', color: P.green },
      { id: 'p3', type: 'process', x: 0.8, y: -0.5, label: 'XOR (A ^ B)', sub: 'TRUE', color: P.violet },
      { id: 'p4', type: 'process', x: 2.4, y: -0.5, label: 'NOT (!A)', sub: 'FALSE', color: P.output },
      { id: 'end', type: 'end', x: 0, y: 0.9, label: 'Nilai boolean', color: P.green },
    ],
    links: [
      { from: 'start', to: 'p1', color: P.ink2, packets: 1 },
      { from: 'p1', to: 'p2', color: P.ink2, packets: 1 },
      { from: 'p2', to: 'p3', color: P.ink2, packets: 1 },
      { from: 'p3', to: 'p4', color: P.ink2, packets: 1 },
      { from: 'p4', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 4. Hukum De Morgan
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: '!(A && B)' },
      { id: 'dec', type: 'decision', x: 0, y: -1.0, label: 'Bentuk mana yang setara?' },
      { id: 'ok', type: 'process', x: -1.6, y: 0.2, label: '!A || !B', sub: 'setara', color: P.green },
      { id: 'bad', type: 'process', x: 1.6, y: 0.2, label: '!A && !B', sub: 'tidak setara', status: 'failed' },
      { id: 'endOk', type: 'end', x: -1.6, y: 1.4, label: 'Benar', color: P.green },
      { id: 'endBad', type: 'end', x: 1.6, y: 1.4, label: 'Salah', status: 'failed' },
    ],
    links: [
      { from: 'start', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'ok', color: P.greenDark, packets: 2, label: 'BENAR' },
      { from: 'dec', to: 'bad', color: P.danger, dashed: true, packets: 1, label: 'SALAH' },
      { from: 'ok', to: 'endOk', color: P.greenDark, packets: 1 },
      { from: 'bad', to: 'endBad', color: P.danger, packets: 1 },
    ],
  },

  // 5. Short-circuit evaluation
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'if (b != 0 && a / b > 2)' },
      { id: 'dec', type: 'decision', x: 0, y: -1.0, label: 'b != 0?' },
      { id: 'skip', type: 'process', x: -1.7, y: 0.15, label: 'Short-circuit', sub: 'a / b dilewati', color: P.green },
      { id: 'eval', type: 'process', x: 1.7, y: 0.15, label: 'Evaluasi a / b', color: P.process },
      { id: 'join', type: 'connector', x: 0, y: 1.25, label: 'A' },
      { id: 'end', type: 'end', x: 0, y: 2.0, label: 'Tidak crash', color: P.green },
    ],
    links: [
      { from: 'start', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'skip', color: P.greenDark, packets: 1, label: 'TIDAK' },
      { from: 'dec', to: 'eval', color: P.process, packets: 1, label: 'YA' },
      { from: 'skip', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'eval', to: 'join', color: P.process, packets: 1 },
      { from: 'join', to: 'end', color: P.ink2, packets: 1 },
    ],
  },

  // 6. Presedensi operator
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.1, label: 'Ekspresi 2 + 3 * 4' },
      { id: 'l1', type: 'process', x: 0, y: -1.35, label: '1 · Kurung ( )' },
      { id: 'l2', type: 'process', x: 0, y: -0.6, label: '2 · Unary ! ~ ++' },
      { id: 'l3', type: 'process', x: 0, y: 0.15, label: '3 · * / %', sub: 'aritmatika', color: P.process },
      { id: 'l4', type: 'process', x: 0, y: 0.9, label: '4 · < > && ||', sub: 'relasional & logika', color: P.violet },
      { id: 'l5', type: 'process', x: 0, y: 1.65, label: '5 · Assignment =', color: P.raw },
      { id: 'end', type: 'end', x: 0, y: 2.4, label: 'Hasil 14', color: P.green },
    ],
    links: [
      { from: 'start', to: 'l1', color: P.ink2, packets: 1 },
      { from: 'l1', to: 'l2', color: P.ink2, packets: 1 },
      { from: 'l2', to: 'l3', color: P.process, packets: 1 },
      { from: 'l3', to: 'l4', color: P.violet, packets: 1 },
      { from: 'l4', to: 'l5', color: P.ink2, packets: 1 },
      { from: 'l5', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 7. Operator bitwise
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: '12 & 10', sub: '0000 1100 · 0000 1010' },
      { id: 'p1', type: 'process', x: -2.4, y: -0.5, label: 'AND (&)', sub: '0000 1000 = 8', color: P.blueSoft },
      { id: 'p2', type: 'process', x: -0.8, y: -0.5, label: 'OR (|)', sub: '0000 1110 = 14', color: P.green },
      { id: 'p3', type: 'process', x: 0.8, y: -0.5, label: 'XOR (^)', sub: '0000 0110 = 6', color: P.violet },
      { id: 'p4', type: 'process', x: 2.4, y: -0.5, label: 'NOT (~)', sub: '1111 0011', color: P.output },
    ],
    links: [
      { from: 'start', to: 'p1', color: P.process, packets: 1 },
      { from: 'start', to: 'p2', color: P.process, packets: 1 },
      { from: 'start', to: 'p3', color: P.process, packets: 1 },
      { from: 'start', to: 'p4', color: P.process, packets: 1 },
    ],
  },

  // 8. Bit shift
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.9, label: 'x = 5', sub: '0000 0101' },
      { id: 'p1', type: 'process', x: 0, y: -0.95, label: 'x << 1', sub: '0000 1010 = 10', color: P.blueSoft },
      { id: 'p2', type: 'process', x: 0, y: 0.0, label: 'x << 2', sub: '0001 0100 = 20', color: P.violet },
      { id: 'p3', type: 'process', x: 0, y: 0.95, label: 'x >> 1', sub: '0000 0010 = 2', color: P.output },
      { id: 'end', type: 'end', x: 0, y: 1.9, label: '×2 / ÷2 per geser', color: P.green },
    ],
    links: [
      { from: 'start', to: 'p1', color: P.ink2, packets: 1 },
      { from: 'p1', to: 'p2', color: P.process, packets: 1 },
      { from: 'p2', to: 'p3', color: P.violet, packets: 1 },
      { from: 'p3', to: 'end', color: P.greenDark, packets: 1 },
    ],
  },

  // 9. Bitmasking izin akses
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.1, label: 'Flags izin = 0000' },
      { id: 'set', type: 'process', x: 0, y: -1.2, label: 'SET WRITE', sub: 'flags |= 0100', color: P.process },
      { id: 'dec', type: 'decision', x: 0, y: -0.2, label: 'READ aktif?', sub: 'flags & 0001' },
      { id: 'yes', type: 'process', x: -1.6, y: 0.9, label: 'Akses diberi', color: P.green },
      { id: 'no', type: 'process', x: 1.6, y: 0.9, label: 'Akses ditolak', status: 'failed' },
      { id: 'end', type: 'end', x: 0, y: 2.0, label: 'Dekode izin', color: P.green },
    ],
    links: [
      { from: 'start', to: 'set', color: P.ink2, packets: 1 },
      { from: 'set', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 2, label: 'ADA' },
      { from: 'dec', to: 'no', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'yes', to: 'end', color: P.greenDark, packets: 1 },
      { from: 'no', to: 'end', color: P.danger, packets: 1 },
    ],
  },

  // 10. Implementasi dual-stack
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -2.0, label: 'Uji perilaku' },
      { id: 'cpp', type: 'process', x: -1.5, y: -0.9, label: 'C++', sub: 'short-circuit & mask', color: P.process },
      { id: 'py', type: 'process', x: 1.5, y: -0.9, label: 'Python', sub: 'short-circuit & int', color: P.green },
      { id: 'join', type: 'connector', x: 0, y: 0.2, label: 'A' },
      { id: 'dec', type: 'decision', x: 0, y: 1.0, label: 'Output sama?' },
      { id: 'end', type: 'end', x: 0, y: 1.9, label: 'Lulus', color: P.green },
      { id: 'fail', type: 'end', x: 0, y: 2.8, label: 'Perbaiki', status: 'failed' },
    ],
    links: [
      { from: 'start', to: 'cpp', color: P.process, packets: 1, label: 'compile' },
      { from: 'start', to: 'py', color: P.greenDark, packets: 1, label: 'interpret' },
      { from: 'cpp', to: 'join', color: P.process, packets: 1 },
      { from: 'py', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'join', to: 'dec', color: P.ink2, packets: 1 },
      { from: 'dec', to: 'end', color: P.greenDark, packets: 2, label: 'YA' },
      { from: 'dec', to: 'fail', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
    ],
  },
]
