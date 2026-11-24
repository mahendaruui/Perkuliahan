import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 4 — Flowchart ISO 5807: Percabangan & Defensive Programming */
/* ------------------------------------------------------------------ */

export const algoP4Scenes: IsoScene[] = [
  // 1. Teorema Böhm-Jacopini (Flowchart 3 Struktur Kendali)
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.6, label: 'Mulai Program' },
      { id: 'seq', type: 'process', x: 0, y: -0.6, label: '1. Sequence', sub: 'instruksi berurutan', color: P.process },
      { id: 'sel', type: 'decision', x: 0, y: 0.55, label: '2. Selection?', sub: 'kondisi boolean' },
      { id: 'itr', type: 'process', x: 1.6, y: 0.55, label: '3. Iteration', sub: 'ulang selama TRUE', color: P.violet },
      { id: 'end', type: 'end', x: 0, y: 1.75, label: 'Selesai', color: P.blueSoft },
    ],
    links: [
      { from: 'start', to: 'seq', color: P.ink2, packets: 1 },
      { from: 'seq', to: 'sel', color: P.process, packets: 1 },
      { from: 'sel', to: 'itr', color: P.violet, packets: 1, label: 'TRUE' },
      { from: 'itr', to: 'end', color: P.ink2, packets: 1 },
      { from: 'sel', to: 'end', color: P.greenDark, packets: 1, label: 'FALSE' },
    ],
  },

  // 2. Percabangan Tunggal & Ganda (If / If-Else)
  {
    nodes: [
      { id: 'start', type: 'start', x: 0, y: -1.8, label: 'Mulai' },
      { id: 'io', type: 'io', x: 0, y: -0.9, label: 'Input: nilai' },
      { id: 'dec', type: 'decision', x: 0, y: 0.1, label: 'nilai >= 60 ?' },
      { id: 'yes', type: 'process', x: -1.35, y: 1.1, label: 'Cetak: LULUS', color: P.green },
      { id: 'no', type: 'process', x: 1.35, y: 1.1, label: 'Cetak: ULANG', status: 'failed', color: P.danger },
      { id: 'join', type: 'connector', x: 0, y: 1.85, label: '○' },
      { id: 'end', type: 'end', x: 0, y: 2.65, label: 'Selesai', color: P.blueSoft },
    ],
    links: [
      { from: 'start', to: 'io', color: P.ink2, packets: 1 },
      { from: 'io', to: 'dec', color: P.process, packets: 1 },
      { from: 'dec', to: 'yes', color: P.greenDark, packets: 2, label: 'TRUE' },
      { from: 'dec', to: 'no', color: P.danger, dashed: true, packets: 1, label: 'FALSE' },
      { from: 'yes', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'no', to: 'join', color: P.ink2, dashed: true, packets: 1 },
      { from: 'join', to: 'end', color: P.ink2, packets: 1 },
    ],
  },

  // 3. Majemuk (if-else-if) & Nested-If
  {
    nodes: [
      { id: 'io', type: 'io', x: -1.3, y: -1.5, label: 'Input: skor, tugas' },
      { id: 'c1', type: 'decision', x: -1.3, y: -0.4, label: 'skor >= 80 ?' },
      { id: 'gA', type: 'process', x: 0.9, y: -0.4, label: 'Grade = A', color: P.green },
      { id: 'c2', type: 'decision', x: -1.3, y: 0.8, label: 'skor >= 60 ?' },
      { id: 'nest', type: 'decision', x: 0.9, y: 0.8, label: 'tugasLengkap?', sub: 'nested-if' },
      { id: 'gB', type: 'process', x: 2.6, y: 0.8, label: 'Grade = B / C', color: P.process },
      { id: 'gE', type: 'process', x: -1.3, y: 1.9, label: 'else: Grade D / E', status: 'failed', color: P.danger },
    ],
    links: [
      { from: 'io', to: 'c1', color: P.ink2, packets: 1 },
      { from: 'c1', to: 'gA', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'c1', to: 'c2', color: P.ink2, packets: 1, label: 'TIDAK' },
      { from: 'c2', to: 'nest', color: P.process, packets: 1, label: 'YA (nested)' },
      { from: 'nest', to: 'gB', color: P.process, packets: 1 },
      { from: 'c2', to: 'gE', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
    ],
  },

  // 4. The Dangling Else Problem
  {
    nodes: [
      { id: 'outer', type: 'decision', x: 0, y: -1.5, label: 'if (x > 0) Luar' },
      { id: 'inner', type: 'decision', x: -0.9, y: -0.3, label: 'if (y > 0) Terdekat' },
      { id: 'ok', type: 'process', x: -1.8, y: 0.9, label: 'X & Y Positif', color: P.green },
      { id: 'dang', type: 'process', x: 0.4, y: 0.9, label: 'else Terikat ke if(y>0)!', sub: 'abaikan indentasi', status: 'failed', color: P.danger },
      { id: 'fix', type: 'end', x: 1.6, y: -0.3, label: 'Solusi: Pakai { }', color: P.green },
    ],
    links: [
      { from: 'outer', to: 'inner', color: P.process, packets: 1, label: 'TRUE (tanpa {})' },
      { from: 'inner', to: 'ok', color: P.greenDark, packets: 1, label: 'TRUE' },
      { from: 'inner', to: 'dang', color: P.danger, packets: 2, label: 'FALSE (terikat!)' },
      { from: 'outer', to: 'fix', color: P.greenDark, dashed: true, packets: 1, label: 'aman dengan {}' },
    ],
  },

  // 5. Operator Ternary
  {
    nodes: [
      { id: 'in', type: 'io', x: 0, y: -1.6, label: 'nilaiAkhir = 82.5' },
      { id: 'cond', type: 'decision', x: 0, y: -0.5, label: 'nilaiAkhir >= 60 ?' },
      { id: 't', type: 'process', x: -1.25, y: 0.65, label: '"LULUS"', color: P.green },
      { id: 'f', type: 'process', x: 1.25, y: 0.65, label: '"TIDAK LULUS"', status: 'failed', color: P.danger },
      { id: 'assign', type: 'codebox', x: 0, y: 1.75, label: 'status = hasil', sub: '1 baris ekspresi', color: P.output },
    ],
    links: [
      { from: 'in', to: 'cond', color: P.ink2, packets: 1 },
      { from: 'cond', to: 't', color: P.greenDark, packets: 2, label: '? TRUE' },
      { from: 'cond', to: 'f', color: P.danger, dashed: true, packets: 1, label: ': FALSE' },
      { from: 't', to: 'assign', color: P.greenDark, packets: 1 },
      { from: 'f', to: 'assign', color: P.ink2, dashed: true, packets: 1 },
    ],
  },

  // 6. Arrow Anti-Pattern (Deeply Nested Flowchart)
  {
    nodes: [
      { id: 'd1', type: 'decision', x: -1.7, y: -1.4, label: 'if (inputValid)' },
      { id: 'd2', type: 'decision', x: -0.8, y: -0.5, label: 'if (userAktif)' },
      { id: 'd3', type: 'decision', x: 0.1, y: 0.4, label: 'if (saldoCukup)' },
      { id: 'd4', type: 'decision', x: 1.0, y: 1.3, label: 'if (kuotaAda)' },
      { id: 'core', type: 'process', x: 2.3, y: 1.3, label: 'prosesTransaksi()', sub: 'menjorok 4 lapis', status: 'failed', color: P.danger },
    ],
    links: [
      { from: 'd1', to: 'd2', color: P.process, packets: 1, label: 'TRUE' },
      { from: 'd2', to: 'd3', color: P.violet, packets: 1, label: 'TRUE' },
      { from: 'd3', to: 'd4', color: P.danger, packets: 1, label: 'TRUE' },
      { from: 'd4', to: 'core', color: P.danger, packets: 2, label: 'TRUE' },
    ],
  },

  // 7. Guard Clauses (Early Return Flowchart)
  {
    nodes: [
      { id: 'g1', type: 'decision', x: -0.8, y: -1.6, label: '!inputValid ?' },
      { id: 'r1', type: 'end', x: 1.3, y: -1.6, label: 'return ERROR_INVALID', status: 'failed' },
      { id: 'g2', type: 'decision', x: -0.8, y: -0.5, label: '!userAktif ?' },
      { id: 'r2', type: 'end', x: 1.3, y: -0.5, label: 'return ERROR_USER', status: 'failed' },
      { id: 'g3', type: 'decision', x: -0.8, y: 0.6, label: '!saldoCukup ?' },
      { id: 'r3', type: 'end', x: 1.3, y: 0.6, label: 'return ERROR_SALDO', status: 'failed' },
      { id: 'ok', type: 'process', x: -0.8, y: 1.75, label: 'prosesTransaksi()', sub: 'alur utama bersih', color: P.green },
    ],
    links: [
      { from: 'g1', to: 'r1', color: P.danger, packets: 1, label: 'YA' },
      { from: 'g1', to: 'g2', color: P.greenDark, packets: 1, label: 'TIDAK' },
      { from: 'g2', to: 'r2', color: P.danger, packets: 1, label: 'YA' },
      { from: 'g2', to: 'g3', color: P.greenDark, packets: 1, label: 'TIDAK' },
      { from: 'g3', to: 'r3', color: P.danger, packets: 1, label: 'YA' },
      { from: 'g3', to: 'ok', color: P.greenDark, packets: 2, label: 'TIDAK' },
    ],
  },

  // 8. Studi Kasus Kelayakan Kredit Bank (Flowchart Lengkap)
  {
    nodes: [
      { id: 'in', type: 'io', x: -1.0, y: -1.9, label: 'Input: Profil Kredit' },
      { id: 'g1', type: 'decision', x: -1.0, y: -0.95, label: 'Usia 21–60?' },
      { id: 'g2', type: 'decision', x: -1.0, y: 0.0, label: 'Gaji >= 4 Jt?' },
      { id: 'g3', type: 'decision', x: -1.0, y: 0.95, label: 'BI >= 650 & DTI <= 40%?' },
      { id: 'rej', type: 'end', x: 1.5, y: 0.0, label: 'return DITOLAK', status: 'failed' },
      { id: 'tier', type: 'decision', x: -1.0, y: 1.95, label: 'BI >= 750 & DTI <= 25%?' },
      { id: 'plat', type: 'end', x: 1.5, y: 1.5, label: 'TIER PLATINUM', color: P.output },
      { id: 'reg', type: 'end', x: 1.5, y: 2.4, label: 'TIER REGULER', color: P.blueSoft },
    ],
    links: [
      { from: 'in', to: 'g1', color: P.ink2, packets: 1 },
      { from: 'g1', to: 'rej', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'g1', to: 'g2', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'g2', to: 'rej', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'g2', to: 'g3', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'g3', to: 'rej', color: P.danger, dashed: true, packets: 1, label: 'TIDAK' },
      { from: 'g3', to: 'tier', color: P.greenDark, packets: 1, label: 'YA' },
      { from: 'tier', to: 'plat', color: P.output, packets: 2, label: 'YA' },
      { from: 'tier', to: 'reg', color: P.process, packets: 1, label: 'TIDAK' },
    ],
  },
]
