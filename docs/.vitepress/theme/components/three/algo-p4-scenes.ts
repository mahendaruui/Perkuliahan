import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 4 — Struktur Kontrol Percabangan & Defensive Programming     */
/* ------------------------------------------------------------------ */

export const algoP4Scenes: IsoScene[] = [
  // 1. Teorema Böhm-Jacopini
  {
    nodes: [
      { id: 'seq', type: 'gate', x: -3.6, y: 1.8, sub: '1. Sequence', label: 'Urutan Lurus', color: P.raw },
      { id: 'sel', type: 'symbol', x: -1.0, y: 0.5, status: 'decision', label: '2. Selection (Cabang)', color: P.process },
      { id: 'itr', type: 'gate', x: 1.6, y: -0.8, sub: '3. Iteration', label: 'Perulangan', color: P.violet },
      { id: 'prog', type: 'code', x: 4.2, y: -2.1, label: 'Program Universal', color: P.output },
    ],
    links: [
      { from: 'seq', to: 'sel', color: P.process, packets: 1 },
      { from: 'sel', to: 'itr', color: P.violet, packets: 1 },
      { from: 'itr', to: 'prog', color: P.output, packets: 2, label: 'komplit' },
    ],
  },

  // 2. Percabangan Tunggal & Ganda
  {
    nodes: [
      { id: 'in', type: 'valuebox', x: -3.8, y: 0.4, sub: 'nilai = 75', label: 'Aliran Masuk', color: P.raw },
      { id: 'cond', type: 'symbol', x: -0.8, y: 0.0, status: 'decision', label: 'nilai >= 60 ?', color: P.output },
      { id: 't', type: 'valuebox', x: 2.0, y: -2.4, sub: 'LULUS', label: 'Cabang TRUE', color: P.green },
      { id: 'f', type: 'valuebox', x: 2.8, y: 1.6, sub: 'ULANG', label: 'Cabang FALSE', status: 'failed', color: P.danger },
      { id: 'join', type: 'symbol', x: 4.6, y: -0.6, status: 'connector', label: 'Titik Konvergensi', color: P.process },
    ],
    links: [
      { from: 'in', to: 'cond', color: P.ink2, packets: 1 },
      { from: 'cond', to: 't', color: P.greenDark, packets: 2, label: 'TRUE' },
      { from: 'cond', to: 'f', color: P.danger, dashed: true, packets: 1, label: 'FALSE' },
      { from: 't', to: 'join', color: P.greenDark, packets: 1 },
      { from: 'f', to: 'join', color: P.ink2, dashed: true, packets: 1 },
    ],
  },

  // 3. Majemuk (if-else-if) & Nested-If
  {
    nodes: [
      { id: 'c1', type: 'symbol', x: -4.2, y: 2.1, status: 'decision', label: 'if (A >= 80)', color: P.green },
      { id: 'c2', type: 'symbol', x: -2.0, y: 1.0, status: 'decision', label: 'else if (B >= 60)', color: P.process },
      { id: 'c3', type: 'symbol', x: 0.2, y: -0.1, status: 'decision', label: 'else if (C >= 40)', color: P.violet },
      { id: 'nest', type: 'gate', x: 2.4, y: -1.2, sub: 'Nested { }', label: 'Cek Lanjutan', color: P.output },
      { id: 'def', type: 'valuebox', x: 4.8, y: -2.4, sub: 'else', label: 'Alternatif Akhir', color: P.rawDark },
    ],
    links: [
      { from: 'c1', to: 'c2', color: P.ink2, dashed: true, packets: 1, label: 'false' },
      { from: 'c2', to: 'c3', color: P.ink2, dashed: true, packets: 1, label: 'false' },
      { from: 'c3', to: 'nest', color: P.process, packets: 1, label: 'nested' },
      { from: 'nest', to: 'def', color: P.output, dashed: true, packets: 1 },
    ],
  },

  // 4. The Dangling Else Problem
  {
    nodes: [
      { id: 'outer', type: 'symbol', x: -3.8, y: 1.4, status: 'decision', label: 'if (x > 0) Luar', color: P.raw },
      { id: 'inner', type: 'symbol', x: -1.2, y: 0.2, status: 'decision', label: 'if (y > 0) Terdekat', color: P.process },
      { id: 'dangling', type: 'gate', x: 1.6, y: -1.0, sub: 'else ?', label: 'Terikat ke if Terdekat', status: 'failed', color: P.danger },
      { id: 'fix', type: 'shield', x: 4.2, y: -2.2, label: 'Wajib Pakai { }', color: P.greenDark },
    ],
    links: [
      { from: 'outer', to: 'inner', color: P.process, packets: 1, label: 'tanpa {}' },
      { from: 'inner', to: 'dangling', color: P.danger, packets: 2, label: 'terikat!' },
      { from: 'dangling', to: 'fix', color: P.greenDark, dashed: true, packets: 2, label: 'solusi' },
    ],
  },

  // 5. Operator Ternary
  {
    nodes: [
      { id: 'cond', type: 'symbol', x: -3.6, y: 1.2, status: 'decision', label: 'nilai >= 60', color: P.process },
      { id: 'op', type: 'gate', x: -0.9, y: 0.2, sub: '?  :', label: 'Ternary (3 Operan)', color: P.violet },
      { id: 'res', type: 'valuebox', x: 2.0, y: -1.0, sub: '"LULUS"', label: 'Nilai Kembalian', color: P.output },
      { id: 'py', type: 'code', x: 4.4, y: -2.2, label: 'C++ ?: & Python if-else', color: P.green },
    ],
    links: [
      { from: 'cond', to: 'op', color: P.process, packets: 1 },
      { from: 'op', to: 'res', color: P.output, packets: 2, label: '1 baris' },
      { from: 'res', to: 'py', color: P.greenDark, dashed: true, packets: 1 },
    ],
  },

  // 6. Arrow Anti-Pattern
  {
    nodes: [
      { id: 'l1', type: 'gate', x: -4.4, y: 2.2, sub: 'if (valid)', label: 'Lapis 1', color: P.raw },
      { id: 'l2', type: 'gate', x: -2.2, y: 1.1, sub: '  if (aktif)', label: 'Lapis 2', color: P.process },
      { id: 'l3', type: 'gate', x: 0.0, y: 0.0, sub: '    if (saldo)', label: 'Lapis 3', color: P.violet },
      { id: 'l4', type: 'gate', x: 2.2, y: -1.1, sub: '      if (kuota)', label: 'Lapis 4 (Dalam)', status: 'failed', color: P.danger },
      { id: 'core', type: 'valuebox', x: 4.6, y: -2.3, sub: 'Arrow!', label: 'Sulit Dibaca', status: 'failed', color: P.danger },
    ],
    links: [
      { from: 'l1', to: 'l2', color: P.process, packets: 1 },
      { from: 'l2', to: 'l3', color: P.violet, packets: 1 },
      { from: 'l3', to: 'l4', color: P.danger, packets: 1 },
      { from: 'l4', to: 'core', color: P.dangerDark, packets: 2, label: 'menjorok' },
    ],
  },

  // 7. Guard Clauses (Early Return)
  {
    nodes: [
      { id: 'g1', type: 'shield', x: -4.2, y: 2.1, label: '!inputValid → return', color: P.danger },
      { id: 'g2', type: 'shield', x: -2.0, y: 1.0, label: '!userAktif → return', color: P.danger },
      { id: 'g3', type: 'shield', x: 0.2, y: -0.1, label: '!saldoCukup → return', color: P.danger },
      { id: 'wall', type: 'wall', x: 2.2, y: -1.1, label: 'Filter Awal' },
      { id: 'ok', type: 'valuebox', x: 4.4, y: -2.2, sub: 'PROSES()', label: 'Alur Utama Linier', color: P.green },
    ],
    links: [
      { from: 'g1', to: 'g2', color: P.process, packets: 1, label: 'lolos' },
      { from: 'g2', to: 'g3', color: P.process, packets: 1, label: 'lolos' },
      { from: 'g3', to: 'wall', color: P.greenDark, packets: 1 },
      { from: 'wall', to: 'ok', color: P.greenDark, packets: 2, label: 'bersih' },
    ],
  },

  // 8. Studi Kasus Kelayakan Kredit Bank
  {
    nodes: [
      { id: 'g1', type: 'gate', x: -3.6, y: -1.6, sub: 'Usia 21-60', label: 'Guard 1: Usia', color: P.process },
      { id: 'g2', type: 'gate', x: -1.4, y: -0.6, sub: 'Gaji >= 4Jt', label: 'Guard 2: Gaji', color: P.process },
      { id: 'g3', type: 'gate', x: 0.8, y: 0.4, sub: 'BI >= 650', label: 'Guard 3: Kredit', color: P.violet },
      { id: 'g4', type: 'gate', x: 3.0, y: 1.4, sub: 'DTI <= 40%', label: 'Guard 4: Rasio', color: P.violet },
      { id: 'tier', type: 'valuebox', x: 4.2, y: -1.6, sub: 'PLATINUM', label: 'Lolos Semua Guard', color: P.output },
    ],
    links: [
      { from: 'g1', to: 'g2', color: P.process, packets: 1 },
      { from: 'g2', to: 'g3', color: P.violet, packets: 1 },
      { from: 'g3', to: 'g4', color: P.violet, packets: 1 },
      { from: 'g4', to: 'tier', color: P.output, packets: 2, label: 'disetujui' },
    ],
  },
]
