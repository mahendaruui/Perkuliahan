import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Minggu 3 — Operator, Aljabar Boolean & Manipulasi Bitwise           */
/* ------------------------------------------------------------------ */

export const algoP3Scenes: IsoScene[] = [
  // 1. Ambiguitas tanpa aturan presedensi
  {
    nodes: [
      { id: 'expr', type: 'valuebox', x: -3.8, y: 0.4, sub: '2 + 3 * 4', label: 'Ekspresi Input', color: P.raw },
      { id: 'alu', type: 'chip', x: -0.8, y: 0.0, label: 'Evaluasi ALU' },
      { id: 'bad', type: 'valuebox', x: 3.6, y: 1.6, sub: '20', label: 'Salah (Kiri→Kanan)', status: 'failed', color: P.danger },
      { id: 'good', type: 'valuebox', x: 2.4, y: -2.6, sub: '14', label: 'Benar (Presedensi *)', color: P.output },
    ],
    links: [
      { from: 'expr', to: 'alu', color: P.process, packets: 2 },
      { from: 'alu', to: 'bad', color: P.danger, dashed: true, packets: 1, label: 'tanpa aturan' },
      { from: 'alu', to: 'good', color: P.output, packets: 2, label: '* dulu baru +' },
    ],
  },

  // 2. Lima keluarga operator
  {
    nodes: [
      { id: 'arit', type: 'gate', x: -4.4, y: 2.2, sub: '+ - * / %', label: '1. Aritmatika', color: P.process },
      { id: 'rel', type: 'gate', x: -2.2, y: 1.1, sub: '== != > <', label: '2. Relasional', color: P.violet },
      { id: 'log', type: 'gate', x: 0.0, y: 0.0, sub: '&& || !', label: '3. Logika Boolean', color: P.green },
      { id: 'bit', type: 'bitreg', x: 2.2, y: -1.1, sub: '01011010', label: '4. Bitwise (& | ^ <<)', color: P.output },
      { id: 'ass', type: 'ram', x: 4.5, y: -2.25, sub: '= += -=', label: '5. Assignment', color: P.rawDark },
    ],
    links: [
      { from: 'arit', to: 'rel', color: P.process, dashed: true, packets: 1 },
      { from: 'rel', to: 'log', color: P.greenDark, dashed: true, packets: 1 },
      { from: 'log', to: 'bit', color: P.ink2, dashed: true, packets: 1 },
      { from: 'bit', to: 'ass', color: P.output, dashed: true, packets: 1 },
    ],
  },

  // 3. Aljabar Boolean
  {
    nodes: [
      { id: 'a', type: 'valuebox', x: -3.8, y: -1.8, sub: 'A: TRUE', label: 'Input A', color: P.raw },
      { id: 'b', type: 'valuebox', x: -2.4, y: 2.2, sub: 'B: FALSE', label: 'Input B', color: P.raw },
      { id: 'andG', type: 'gate', x: -0.2, y: -2.5, sub: 'AND (&&)', label: 'Semua Benar', color: P.process },
      { id: 'orG', type: 'gate', x: 0.3, y: 0.3, sub: 'OR (||)', label: 'Salah Satu Benar', color: P.violet },
      { id: 'xorG', type: 'gate', x: 1.4, y: 3.0, sub: 'XOR (^)', label: 'Harus Berbeda', color: P.teal },
      { id: 'res', type: 'valuebox', x: 4.0, y: 0.0, sub: 'T / F', label: 'Hasil Boolean', color: P.output },
    ],
    links: [
      { from: 'a', to: 'andG', color: P.process, packets: 1 },
      { from: 'b', to: 'orG', color: P.violet, packets: 1 },
      { from: 'b', to: 'xorG', color: P.teal, packets: 1 },
      { from: 'andG', to: 'res', color: P.process, packets: 1 },
      { from: 'orG', to: 'res', color: P.violet, packets: 1 },
      { from: 'xorG', to: 'res', color: P.teal, packets: 1 },
    ],
  },

  // 4. Hukum De Morgan
  {
    nodes: [
      { id: 'in', type: 'valuebox', x: -3.8, y: 1.4, sub: '!(A && B)', label: 'Bentuk Awal', status: 'failed', color: P.danger },
      { id: 'law', type: 'gate', x: -1.2, y: 0.4, sub: 'De Morgan', label: 'Sebar Negasi !', color: P.process },
      { id: 'flip', type: 'symbol', x: 1.3, y: -0.5, status: 'decision', label: 'Balik && ↔ ||', color: P.violet },
      { id: 'out', type: 'valuebox', x: 3.8, y: -1.5, sub: '!A || !B', label: 'Bentuk Setara', color: P.output },
    ],
    links: [
      { from: 'in', to: 'law', color: P.danger, packets: 1, label: 'negasi masuk' },
      { from: 'law', to: 'flip', color: P.process, packets: 1 },
      { from: 'flip', to: 'out', color: P.output, packets: 2, label: 'ekuivalen' },
    ],
  },

  // 5. Short-Circuit Evaluation
  {
    nodes: [
      { id: 'left', type: 'shield', x: -3.6, y: 0.4, label: 'pembagi != 0 (FALSE)', color: P.process },
      { id: 'gate', type: 'wall', x: -0.4, y: 0.0, label: 'Short-Circuit Stop' },
      { id: 'right', type: 'gate', x: 3.2, y: 1.4, sub: 'total / 0', label: 'Dilewati CPU', status: 'failed', color: P.danger },
      { id: 'safe', type: 'valuebox', x: 2.2, y: -2.2, sub: 'AMAN', label: 'Bebas Zero Division', color: P.green },
    ],
    links: [
      { from: 'left', to: 'gate', color: P.process, packets: 2, label: 'false' },
      { from: 'gate', to: 'right', color: P.danger, dashed: true, packets: 0, label: 'dilewati' },
      { from: 'gate', to: 'safe', color: P.greenDark, packets: 2, label: 'short-circuit' },
    ],
  },

  // 6. Hierarki Presedensi
  {
    nodes: [
      { id: 'p1', type: 'gate', x: -4.4, y: 2.2, sub: '1. () ! ++', label: 'Tertinggi', color: P.output },
      { id: 'p2', type: 'gate', x: -2.2, y: 1.1, sub: '2. * / %', label: 'Multiplikasi', color: P.process },
      { id: 'p3', type: 'gate', x: 0.0, y: 0.0, sub: '3. + − > ==', label: 'Adisi & Relasi', color: P.violet },
      { id: 'p4', type: 'gate', x: 2.2, y: -1.1, sub: '4. && || ?:', label: 'Logika & Ternary', color: P.green },
      { id: 'p5', type: 'gate', x: 4.5, y: -2.25, sub: '5. = +=', label: 'Terendah (Assign)', color: P.rawDark },
    ],
    links: [
      { from: 'p1', to: 'p2', color: P.output, packets: 1 },
      { from: 'p2', to: 'p3', color: P.process, packets: 1 },
      { from: 'p3', to: 'p4', color: P.violet, packets: 1 },
      { from: 'p4', to: 'p5', color: P.greenDark, packets: 1 },
    ],
  },

  // 7. Operasi Bitwise
  {
    nodes: [
      { id: 'x', type: 'bitreg', x: -3.6, y: -1.5, sub: '00101010', label: '42 (00101010)', color: P.process },
      { id: 'y', type: 'bitreg', x: -2.2, y: 2.1, sub: '00011011', label: '27 (00011011)', color: P.violet },
      { id: 'alu', type: 'gate', x: 0.4, y: 0.2, sub: 'BIT &', label: 'AND Per Bit', color: P.process },
      { id: 'z', type: 'bitreg', x: 3.4, y: -0.3, sub: '00001010', label: 'Hasil: 10 (00001010)', color: P.output },
    ],
    links: [
      { from: 'x', to: 'alu', color: P.process, packets: 2 },
      { from: 'y', to: 'alu', color: P.violet, packets: 2 },
      { from: 'alu', to: 'z', color: P.output, packets: 2, label: 'per bit' },
    ],
  },

  // 8. Bit Shift
  {
    nodes: [
      { id: 'v', type: 'bitreg', x: -3.5, y: 0.4, sub: '00000111', label: 'Nilai 7 (00000111)', color: P.raw },
      { id: 'shl', type: 'gate', x: -0.4, y: -1.9, sub: '<< 2 (×4)', label: 'Geser Kiri', color: P.process },
      { id: 'shr', type: 'gate', x: 0.2, y: 2.1, sub: '>> 3 (÷8)', label: 'Geser Kanan (32)', color: P.violet },
      { id: 'out', type: 'valuebox', x: 3.4, y: -0.1, sub: '28  |  4', label: 'Hasil Shift Kilat', color: P.output },
    ],
    links: [
      { from: 'v', to: 'shl', color: P.process, packets: 2, label: 'geser kiri' },
      { from: 'shl', to: 'out', color: P.output, packets: 2 },
      { from: 'shr', to: 'out', color: P.violet, packets: 2, label: 'geser kanan' },
    ],
  },

  // 9. Bitmasking Izin Akses
  {
    nodes: [
      { id: 'byte', type: 'bitreg', x: -3.6, y: 0.4, sub: '00000011', label: 'userPerm (1 Byte)', color: P.process },
      { id: 'set', type: 'gate', x: -0.4, y: -2.0, sub: '| (Set)', label: 'Nyalakan Bit', color: P.green },
      { id: 'clr', type: 'gate', x: 1.8, y: -1.0, sub: '&~ (Clear)', label: 'Cabut Bit', color: P.danger },
      { id: 'tgl', type: 'gate', x: -0.2, y: 2.2, sub: '^ (Toggle)', label: 'Balik Bit', color: P.violet },
      { id: 'chk', type: 'shield', x: 3.6, y: 2.6, label: 'Cek Izin (&)', color: P.output },
    ],
    links: [
      { from: 'byte', to: 'set', color: P.greenDark, packets: 1 },
      { from: 'set', to: 'clr', color: P.danger, packets: 1 },
      { from: 'byte', to: 'tgl', color: P.violet, dashed: true, packets: 1 },
      { from: 'clr', to: 'chk', color: P.output, packets: 2 },
    ],
  },

  // 10. Implementasi Dual-Stack
  {
    nodes: [
      { id: 'cpp', type: 'code', x: -3.6, y: -1.2, label: 'C++: bitset<8>', color: P.process },
      { id: 'py', type: 'code', x: -0.8, y: 2.4, label: 'Python: f"{p:08b}"', color: P.green },
      { id: 'mask', type: 'bitreg', x: 1.2, y: -0.2, sub: '00000101', label: 'R + X Aktif (5)', color: P.output },
      { id: 'out', type: 'valuebox', x: 4.0, y: -0.8, sub: '00000101', label: 'Output Identik', color: P.output },
    ],
    links: [
      { from: 'cpp', to: 'mask', color: P.process, packets: 1 },
      { from: 'py', to: 'mask', color: P.greenDark, packets: 1 },
      { from: 'mask', to: 'out', color: P.output, packets: 2, label: 'R + X aktif' },
    ],
  },
]
