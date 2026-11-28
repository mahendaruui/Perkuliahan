/* Pure 2D OOP UML & Dynamic Dispatch Canvas renderer sharing StoryCanvas2D controls. */

import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

function clamp(v: number, a: number, b: number) {
  return Math.max(a, Math.min(b, v))
}

function easeOut(t: number) {
  const x = clamp(t, 0, 1)
  return 1 - Math.pow(1 - x, 3)
}

function rr(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  c.beginPath()
  c.roundRect(x, y, w, h, r)
}

function txt(
  c: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  size = 11,
  weight = 600,
  color = PALETTE.ink,
  align: CanvasTextAlign = 'left',
  mono = false,
) {
  c.save()
  c.fillStyle = color
  c.font = `${weight} ${size}px ${mono ? '"JetBrains Mono", monospace' : '"Plus Jakarta Sans", sans-serif'}`
  c.textAlign = align
  c.textBaseline = 'middle'
  c.fillText(text, x, y)
  c.restore()
}

function cardFrame(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, title: string, badge?: string) {
  c.save()
  rr(c, x + 2, y + 3, w, h, 11)
  c.fillStyle = 'rgba(52,48,43,.07)'
  c.fill()

  rr(c, x, y, w, h, 11)
  c.fillStyle = PALETTE.cream
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.stroke()

  c.strokeStyle = 'rgba(52,48,43,.16)'
  c.lineWidth = 1
  c.beginPath()
  c.moveTo(x + 1, y + 29)
  c.lineTo(x + w - 1, y + 29)
  c.stroke()

  const dots = ['#e0804f', '#efc368', '#6b9b58']
  dots.forEach((col, i) => {
    c.beginPath()
    c.arc(x + 14 + i * 11, y + 15, 3.2, 0, Math.PI * 2)
    c.fillStyle = col
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 0.8
    c.stroke()
  })

  txt(c, title, x + 48, y + 15.5, 10.5, 700, PALETTE.ink, 'left', true)
  if (badge) {
    txt(c, badge, x + w - 12, y + 15.5, 9.5, 600, PALETTE.ink2, 'right', true)
  }
  c.restore()
}

function classCard(
  c: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  opts: {
    stereotype?: string
    title: string
    headerBg: string
    headerText?: string
    lines: string[]
    active?: boolean
    dashed?: boolean
  },
) {
  c.save()
  if (opts.active) {
    rr(c, x - 3, y - 3, w + 6, h + 6, 11)
    c.fillStyle = 'rgba(232,163,58,.18)'
    c.fill()
  }

  rr(c, x, y, w, h, 8)
  c.fillStyle = '#fffaf2'
  c.fill()
  c.strokeStyle = opts.active ? '#c97e1c' : PALETTE.ink
  c.lineWidth = opts.active ? 2 : 1.35
  if (opts.dashed) c.setLineDash([5, 3])
  c.stroke()
  c.setLineDash([])

  const headH = opts.stereotype ? 34 : 24
  c.save()
  rr(c, x, y, w, headH, [8, 8, 0, 0])
  c.fillStyle = opts.headerBg
  c.fill()
  c.restore()

  c.beginPath()
  c.moveTo(x, y + headH)
  c.lineTo(x + w, y + headH)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.1
  c.stroke()

  if (opts.stereotype) {
    txt(c, opts.stereotype, x + w / 2, y + 10, 8.2, 700, opts.headerText ?? PALETTE.ink2, 'center', true)
    txt(c, opts.title, x + w / 2, y + 23.5, 10.5, 800, opts.headerText ?? PALETTE.ink, 'center', true)
  } else {
    txt(c, opts.title, x + w / 2, y + 12.5, 10.2, 800, opts.headerText ?? PALETTE.ink, 'center', true)
  }

  const bodyTop = y + headH + 11
  const rowStep = Math.min(15, (h - headH - 12) / Math.max(1, opts.lines.length))
  opts.lines.forEach((ln, idx) => {
    txt(c, ln, x + 9, bodyTop + idx * rowStep, 9.2, 600, PALETTE.ink2, 'left', true)
  })
  c.restore()
}

function arrow(
  c: CanvasRenderingContext2D,
  x1: number,
  y1: number,
  x2: number,
  y2: number,
  opts: { color?: string; dashed?: boolean; active?: boolean; pulse?: number; label?: string } = {},
) {
  c.save()
  const col = opts.active ? '#c97e1c' : opts.color ?? PALETTE.ink2
  c.strokeStyle = col
  c.lineWidth = opts.active ? 2.2 : 1.35
  if (opts.dashed) c.setLineDash([5, 4])
  c.beginPath()
  c.moveTo(x1, y1)
  c.lineTo(x2, y2)
  c.stroke()
  c.setLineDash([])

  const ang = Math.atan2(y2 - y1, x2 - x1)
  const hs = 6.5
  c.beginPath()
  c.moveTo(x2, y2)
  c.lineTo(x2 - hs * Math.cos(ang - 0.45), y2 - hs * Math.sin(ang - 0.45))
  c.lineTo(x2 - hs * Math.cos(ang + 0.45), y2 - hs * Math.sin(ang + 0.45))
  c.closePath()
  c.fillStyle = col
  c.fill()

  if (typeof opts.pulse === 'number') {
    const px = x1 + (x2 - x1) * opts.pulse
    const py = y1 + (y2 - y1) * opts.pulse
    c.beginPath()
    c.arc(px, py, 4.2, 0, Math.PI * 2)
    c.fillStyle = '#efc368'
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1.2
    c.stroke()
  }

  if (opts.label) {
    txt(c, opts.label, (x1 + x2) / 2, (y1 + y2) / 2 - 8, 8.6, 700, col, 'center', true)
  }
  c.restore()
}

// 1. Filosofi: Satu Antarmuka, Banyak Perilaku
function drawFilosofi(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Satu Antarmuka, Banyak Perilaku', 'What vs How')
  const p = easeOut(intro)
  const activeIdx = Math.floor((t * 0.7) % 3)
  const pulse = (t * 0.7) % 1

  c.save()
  c.globalAlpha = p
  const cx = x + w / 2
  const availH = h - 44
  const h1 = 42
  const h2 = 52
  const h3 = clamp(Math.floor(availH * 0.30), 48, 66)
  const free = Math.max(28, availH - h1 - h2 - h3)
  const g1 = Math.floor(free * 0.42)
  const g2 = free - g1
  const y1 = y + 36
  const y2 = y1 + h1 + g1
  const y3 = y2 + h2 + g2

  const clientW = Math.min(280, w - 40)
  classCard(c, cx - clientW / 2, y1, clientW, h1, {
    title: 'Client: $saluran->bayar()',
    headerBg: '#f6e6c9',
    lines: ['Kontrak umum (What to do)'],
  })

  const parentW = Math.min(310, w - 36)
  classCard(c, cx - parentW / 2, y2, parentW, h2, {
    stereotype: '«abstract»',
    title: 'SaluranPembayaran',
    headerBg: '#dbeafe',
    lines: ['+ bayar() · + hitungBiayaAdmin()'],
  })

  arrow(c, cx, y1 + h1, cx, y2, { active: true, pulse })

  const gap = 12
  const childW = Math.min(168, (w - 40 - gap * 2) / 3)
  const totalW = childW * 3 + gap * 2
  const startX = cx - totalW / 2
  const children = [
    { name: 'TransferBank', bg: '#dff0de', lines: ['Admin: Rp 4.000'] },
    { name: 'QrisInstant', bg: '#e7ddf5', lines: ['MDR: 0.7%'] },
    { name: 'EWalletGoPay', bg: '#fcdcbd', lines: ['Fee: Rp 1.000'] },
  ]

  children.forEach((ch, i) => {
    const bx = startX + i * (childW + gap)
    const isAct = i === activeIdx
    arrow(c, cx + (i - 1) * (parentW * 0.28), y2 + h2, bx + childW / 2, y3, {
      dashed: true,
      active: isAct,
      pulse: isAct ? pulse : undefined,
    })
    classCard(c, bx, y3, childW, h3, {
      title: ch.name,
      headerBg: ch.bg,
      lines: ch.lines,
      active: isAct,
    })
  })
  c.restore()
}

// 2. Taksonomi Cardelli & Wegner (1985)
function drawTaksonomi(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Taksonomi Cardelli & Wegner (1985)', '4 Jenis Polimorfisme')
  const p = easeOut(intro)
  const gap = 12
  const cw = (w - 36 - gap) / 2
  const ch = (h - 54 - gap) / 2
  const sx = x + 18
  const sy = y + 40
  const pulse = 0.5 + 0.5 * Math.sin(t * 2.5)

  const cells = [
    { title: '1. Subtyping (OOP)', sub: 'Fokus Utama PHP 8+', bg: '#dff0de', lines: ['Variabel tipe induk', 'menampung objek anak'], active: true },
    { title: '2. Parametric', sub: 'Generics / Template', bg: '#dbeafe', lines: ['Logika generik lintas', 'tipe data (List<T>)'], active: false },
    { title: '3. Ad-hoc', sub: 'Overloading', bg: '#f6e6c9', lines: ['Nama fungsi sama,', 'parameter berbeda'], active: false },
    { title: '4. Coercion', sub: 'Implicit Casting', bg: '#e7ddf5', lines: ['Konversi tipe otomatis', 'misal int → float'], active: false },
  ]

  c.save()
  c.globalAlpha = p
  cells.forEach((item, idx) => {
    const col = idx % 2
    const row = Math.floor(idx / 2)
    const bx = sx + col * (cw + gap)
    const by = sy + row * (ch + gap)
    classCard(c, bx, by, cw, ch, {
      stereotype: item.sub,
      title: item.title,
      headerBg: item.bg,
      lines: item.lines,
      active: item.active && pulse > 0.25,
    })
  })
  c.restore()
}

// 3. Zend Engine Dynamic Method Dispatch
function drawDispatch(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Zend Engine: Dynamic Method Dispatch', 'Resolusi Runtime')
  const p = easeOut(intro)
  const stage = Math.floor((t * 0.75) % 3)
  const pulse = (t * 0.75) % 1

  c.save()
  c.globalAlpha = p
  const bw = Math.min(210, (w - 64) / 3)
  const gap = (w - 36 - bw * 3) / 2
  const sx = x + 18
  const by = y + 66
  const bh = Math.min(130, h - 110)

  classCard(c, sx, by, bw, bh, {
    stereotype: '1. Panggilan',
    title: '$obj->bayar()',
    headerBg: '#f6e6c9',
    lines: ['Tipe hint:', 'SaluranPembayaran', 'Objek riil: Qris'],
    active: stage === 0,
  })

  classCard(c, sx + bw + gap, by, bw, bh, {
    stereotype: '2. Zend Class Entry',
    title: 'Cek Class Riil',
    headerBg: '#dbeafe',
    lines: ['Baca vtable milik', 'QrisInstant::class', 'Cari method bayar()'],
    active: stage === 1,
  })

  classCard(c, sx + (bw + gap) * 2, by, bw, bh, {
    stereotype: '3. Eksekusi',
    title: 'QrisInstant::bayar',
    headerBg: '#dff0de',
    lines: ['Ditemukan di child!', 'Jalankan override.', '(Fallback → parent)'],
    active: stage === 2,
  })

  arrow(c, sx + bw, by + bh / 2, sx + bw + gap, by + bh / 2, {
    active: stage === 0,
    pulse: stage === 0 ? pulse : undefined,
  })
  arrow(c, sx + bw * 2 + gap, by + bh / 2, sx + (bw + gap) * 2, by + bh / 2, {
    active: stage === 1,
    pulse: stage === 1 ? pulse : undefined,
  })

  txt(c, 'Resolusi terjadi saat runtime, bukan saat kompilasi.', x + w / 2, y + h - 20, 10, 600, PALETTE.ink2, 'center', true)
  c.restore()
}

// 4. Polymorphic Type Hinting
function drawTypeHint(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Polymorphic Type Hinting: prosesTransaksiKasir()', 'Parameter Tipe Induk')
  const p = easeOut(intro)
  const activeIdx = Math.floor((t * 0.7) % 3)
  const pulse = (t * 0.7) % 1

  c.save()
  c.globalAlpha = p
  const leftW = Math.min(200, w * 0.4)
  const rightW = Math.min(230, w * 0.45)
  const lx = x + 22
  const rx = x + w - rightW - 22

  const inputs = [
    { name: 'new TransferBank()', bg: '#dff0de', lines: ['Admin: Rp 4.000'] },
    { name: 'new QrisInstant()', bg: '#e7ddf5', lines: ['Admin: MDR 0.7%'] },
    { name: 'new EWalletGoPay()', bg: '#fcdcbd', lines: ['Admin: Rp 1.000'] },
  ]

  const boxH = Math.min(54, (h - 76) / 3)
  inputs.forEach((inp, i) => {
    const iy = y + 44 + i * (boxH + 10)
    const isAct = i === activeIdx
    classCard(c, lx, iy, leftW, boxH, {
      title: inp.name,
      headerBg: inp.bg,
      lines: inp.lines,
      active: isAct,
    })
    arrow(c, lx + leftW, iy + boxH / 2, rx, y + h / 2, {
      active: isAct,
      pulse: isAct ? pulse : undefined,
    })
  })

  classCard(c, rx, y + h / 2 - 58, rightW, 116, {
    stereotype: 'function',
    title: 'prosesTransaksiKasir',
    headerBg: '#dbeafe',
    lines: [
      '(SaluranPembayaran $s)',
      '$s->bayar();',
      '$s->hitungBiayaAdmin();',
      '// Tidak perlu diubah!',
    ],
    active: true,
  })
  c.restore()
}

// 5. Koleksi Polimorfik
function drawCollection(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Koleksi Polimorfik: SaluranPembayaran[]', 'Iterasi Tunggal foreach')
  const p = easeOut(intro)
  const activeIdx = Math.floor((t * 0.85) % 4)

  c.save()
  c.globalAlpha = p
  const items = [
    { idx: '[0]', name: 'TransferBank', val: 'Rp 504.000', bg: '#dff0de' },
    { idx: '[1]', name: 'QrisInstant', val: 'Rp 25.175', bg: '#e7ddf5' },
    { idx: '[2]', name: 'EWalletGoPay', val: 'Rp 76.000', bg: '#fcdcbd' },
    { idx: '[3]', name: 'QrisInstant', val: 'Rp 151.050', bg: '#e7ddf5' },
  ]

  const gap = 8
  const cw = (w - 40 - gap * 3) / 4
  const sx = x + 20
  const iy = y + 46
  const ch = 82

  items.forEach((it, i) => {
    const bx = sx + i * (cw + gap)
    const isAct = i === activeIdx
    classCard(c, bx, iy, cw, ch, {
      stereotype: it.idx,
      title: it.name,
      headerBg: it.bg,
      lines: [it.val],
      active: isAct,
    })
    arrow(c, bx + cw / 2, iy + ch, x + w / 2, y + h - 88, {
      active: isAct,
      pulse: isAct ? ((t * 0.85) % 1) : undefined,
    })
  })

  const loopW = Math.min(350, w - 40)
  classCard(c, x + (w - loopW) / 2, y + h - 88, loopW, 66, {
    stereotype: 'foreach ($antreanPembayaran as $tx)',
    title: 'prosesTransaksiKasir($tx)',
    headerBg: '#f6e6c9',
    lines: [`Menjalankan item [${activeIdx}] -> ${items[activeIdx].name}`],
    active: true,
  })
  c.restore()
}

// 6. Extends vs Interface
function drawExtendsVsImpl(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Class Inheritance (extends) vs Interface (implements)', 'Is-A vs Can-Do')
  const p = easeOut(intro)
  const gap = 14
  const cw = (w - 40 - gap) / 2
  const ch = h - 56
  const sx = x + 20
  const sy = y + 42
  const leftActive = Math.floor((t * 0.5) % 2) === 0

  c.save()
  c.globalAlpha = p
  classCard(c, sx, sy, cw, ch, {
    stereotype: 'extends (Is-A)',
    title: 'Pewarisan Class',
    headerBg: '#dbeafe',
    lines: [
      '• Mewarisi state & method',
      '• Single inheritance (1)',
      '• Cocok: hierarki entitas',
      '  dengan data bersama',
      '• Contoh: SaluranPembayaran',
    ],
    active: leftActive,
  })

  classCard(c, sx + cw + gap, sy, cw, ch, {
    stereotype: 'implements (Can-Do)',
    title: 'Kontrak Interface',
    headerBg: '#dff0de',
    lines: [
      '• Murni kontrak method',
      '• Multiple implementation',
      '• Lintas rumpun class',
      '• Standar Dependency Inj.',
      '• Contoh: NotifikasiInterface',
    ],
    active: !leftActive,
    dashed: true,
  })
  c.restore()
}

// 7. Type Narrowing instanceof vs Anti-Pattern
function drawInstanceOf(c: CanvasRenderingContext2D, _t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Type Narrowing (instanceof) vs Code Smell', 'Audit vs Logika Bisnis')
  const p = easeOut(intro)
  const gap = 14
  const cw = (w - 40 - gap) / 2
  const ch = h - 56
  const sx = x + 20
  const sy = y + 42

  c.save()
  c.globalAlpha = p
  classCard(c, sx, sy, cw, ch, {
    stereotype: 'ANTI-PATTERN (HINDARI)',
    title: 'if-elseif instanceof',
    headerBg: '#fee2e2',
    lines: [
      'if ($s instanceof Bank) ...',
      'elseif ($s instanceof QRIS)',
      'elseif ($s instanceof EWal)',
      '• Melanggar OCP!',
      '• Pindah ke method child',
    ],
  })

  classCard(c, sx + cw + gap, sy, cw, ch, {
    stereotype: 'TEPAT GUNA',
    title: 'LaporanAuditor::audit',
    headerBg: '#dff0de',
    lines: [
      '$s->bayar(); // Polimorfik',
      'if ($s instanceof Qris) {',
      '  // Cek signature BI',
      '}',
      '• Hanya untuk kasus khusus',
    ],
    active: true,
  })
  c.restore()
}

// 8. Praktikum NotifikasiManager & Open/Closed Principle (OCP)
function drawOcpNotif(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'NotifikasiManager & Open/Closed Principle (OCP)', 'Plug-and-Play')
  const p = easeOut(intro)
  const activeIdx = Math.floor((t * 0.75) % 4)
  const pulse = (t * 0.75) % 1
  const cx = x + w / 2

  c.save()
  c.globalAlpha = p
  const availH = h - 44
  const h1 = 44
  const h2 = 52
  const h3 = clamp(Math.floor(availH * 0.27), 46, 62)
  const free = Math.max(28, availH - h1 - h2 - h3)
  const g1 = Math.floor(free * 0.4)
  const g2 = free - g1
  const y1 = y + 36
  const y2 = y1 + h1 + g1
  const y3 = y2 + h2 + g2

  const topW = Math.min(310, w - 40)
  classCard(c, cx - topW / 2, y1, topW, h1, {
    title: 'NotifikasiManager',
    headerBg: '#f6e6c9',
    lines: ['broadcastPesan() · tertutup modifikasi'],
  })

  const intW = Math.min(270, w - 40)
  classCard(c, cx - intW / 2, y2, intW, h2, {
    stereotype: '«interface»',
    title: 'NotifikasiInterface',
    headerBg: '#dbeafe',
    lines: ['+ kirim(string $p, string $m): bool'],
    dashed: true,
  })

  arrow(c, cx, y1 + h1, cx, y2, { active: true, pulse })

  const gap = 8
  const cw = (w - 40 - gap * 3) / 4
  const sx = x + 20
  const channels = [
    { name: 'EmailNotif', bg: '#dff0de', desc: 'SMTP / Mail', plug: false },
    { name: 'WhatsApp', bg: '#e7ddf5', desc: 'Cloud API', plug: false },
    { name: 'PushFCM', bg: '#fcdcbd', desc: 'Device Token', plug: false },
    { name: '+ Telegram', bg: '#fef3c7', desc: 'Ekstensi Baru', plug: true },
  ]

  channels.forEach((ch, i) => {
    const bx = sx + i * (cw + gap)
    const isAct = i === activeIdx
    arrow(c, cx + (i - 1.5) * (intW * 0.22), y2 + h2, bx + cw / 2, y3, {
      dashed: true,
      active: isAct,
      pulse: isAct ? pulse : undefined,
    })
    classCard(c, bx, y3, cw, h3, {
      title: ch.name,
      headerBg: ch.bg,
      lines: [ch.desc],
      active: isAct,
      dashed: ch.plug,
    })
  })
  c.restore()
}

export function drawOopScene(
  c: CanvasRenderingContext2D,
  scene: IsoScene,
  t: number,
  w: number,
  h: number,
  opts: { intro?: number } = {},
) {
  c.clearRect(0, 0, w, h)
  const bg = c.createRadialGradient(w * 0.5, h * 0.45, 20, w * 0.5, h * 0.45, Math.max(w, h) * 0.72)
  bg.addColorStop(0, 'rgba(255,255,255,.72)')
  bg.addColorStop(0.55, 'rgba(252,251,249,.35)')
  bg.addColorStop(1, 'rgba(252,251,249,0)')
  c.fillStyle = bg
  c.fillRect(0, 0, w, h)

  const padX = w < 560 ? 14 : 24
  const padTop = h > 260 ? 12 : 8
  const padBottom = h > 280 ? 52 : 26
  const x = padX
  const y = padTop
  const cw = Math.max(240, w - padX * 2)
  const ch = Math.max(180, h - padTop - padBottom)
  const intro = opts.intro ?? 1

  const kind = scene.nodes[0]?.type ?? 'oop_filosofi'
  switch (kind) {
    case 'oop_filosofi':
      drawFilosofi(c, t, x, y, cw, ch, intro)
      break
    case 'oop_taksonomi':
      drawTaksonomi(c, t, x, y, cw, ch, intro)
      break
    case 'oop_dispatch':
      drawDispatch(c, t, x, y, cw, ch, intro)
      break
    case 'oop_typehint':
      drawTypeHint(c, t, x, y, cw, ch, intro)
      break
    case 'oop_collection':
      drawCollection(c, t, x, y, cw, ch, intro)
      break
    case 'oop_extends_impl':
      drawExtendsVsImpl(c, t, x, y, cw, ch, intro)
      break
    case 'oop_instanceof':
      drawInstanceOf(c, t, x, y, cw, ch, intro)
      break
    case 'oop_ocp_notif':
      drawOcpNotif(c, t, x, y, cw, ch, intro)
      break
    default:
      drawFilosofi(c, t, x, y, cw, ch, intro)
      break
  }
}
