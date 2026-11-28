/* Pure 2D Time Series & Financial Visualization canvas renderer for StoryCanvas2D. */

import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'

function clamp(v: number, a: number, b: number) {
  return Math.max(a, Math.min(b, v))
}

function easeOut(x: number) {
  return 1 - Math.pow(1 - clamp(x, 0, 1), 3)
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
  weight: number | string = 600,
  color: string = PALETTE.ink,
  align: CanvasTextAlign = 'left',
  mono = false,
) {
  c.save()
  c.font = `${weight} ${size}px ${mono ? '"Fira Code", "JetBrains Mono", monospace' : '"Plus Jakarta Sans", sans-serif'}`
  c.fillStyle = color
  c.textAlign = align
  c.textBaseline = 'middle'
  c.fillText(text, x, y)
  c.restore()
}

function cardFrame(
  c: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  title: string,
  subtitle: string,
) {
  // Subtle drop shadow
  c.save()
  c.fillStyle = 'rgba(52,48,43,.12)'
  rr(c, x + 5, y + 6, w, h, 14)
  c.fill()
  c.restore()

  rr(c, x, y, w, h, 14)
  c.fillStyle = PALETTE.cream
  c.fill()

  // Header band
  c.save()
  rr(c, x, y, w, h, 14)
  c.clip()
  c.fillStyle = PALETTE.paper
  c.fillRect(x, y, w, 34)
  c.restore()

  c.beginPath()
  c.moveTo(x + 1, y + 34)
  c.lineTo(x + w - 1, y + 34)
  c.strokeStyle = 'rgba(52,48,43,.18)'
  c.lineWidth = 1.1
  c.stroke()

  // Window dots
  ;[PALETTE.green, PALETTE.output, PALETTE.danger].forEach((col, i) => {
    c.beginPath()
    c.arc(x + 16 + i * 11, y + 17, 3.3, 0, Math.PI * 2)
    c.fillStyle = col
    c.fill()
    c.strokeStyle = 'rgba(52,48,43,.65)'
    c.lineWidth = 0.8
    c.stroke()
  })

  txt(c, title, x + 52, y + 17.5, 11, 800, PALETTE.ink, 'left', true)
  if (subtitle) {
    txt(c, subtitle, x + w - 14, y + 17.5, 9.5, 600, PALETTE.ink2, 'right')
  }

  rr(c, x, y, w, h, 14)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.65
  c.stroke()
}

function gridH(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, rows = 4) {
  c.save()
  c.strokeStyle = 'rgba(143,136,126,.25)'
  c.lineWidth = 1
  c.setLineDash([3, 5])
  for (let i = 0; i < rows; i++) {
    const gy = y + (h / (rows - 1)) * i
    c.beginPath()
    c.moveTo(x, gy)
    c.lineTo(x + w, gy)
    c.stroke()
  }
  c.restore()
}

// Deterministic pseudo-random series for stable, crisp renders
function genSignal(n: number) {
  const obs: number[] = []
  const trend: number[] = []
  const seas: number[] = []
  const resid: number[] = []
  for (let i = 0; i < n; i++) {
    const tr = 20 + (i / (n - 1)) * 15
    const se = 4.6 * Math.sin((2 * Math.PI * i) / 9.2)
    const ns = 2.4 * Math.sin(i * 2.37) + 1.5 * Math.cos(i * 4.13)
    trend.push(tr)
    seas.push(se)
    resid.push(ns)
    obs.push(tr + se + ns)
  }
  return { obs, trend, seas, resid }
}

function drawPolyline(
  c: CanvasRenderingContext2D,
  pts: Array<[number, number]>,
  color: string,
  width = 2.2,
  dashed = false,
) {
  if (pts.length < 2) return
  c.save()
  c.beginPath()
  pts.forEach(([px, py], i) => (i === 0 ? c.moveTo(px, py) : c.lineTo(px, py)))
  c.strokeStyle = color
  c.lineWidth = width
  c.lineJoin = 'round'
  c.lineCap = 'round'
  if (dashed) c.setLineDash([5, 4])
  c.stroke()
  c.restore()
}

// 1. Raw noisy signal
function drawRawSignal(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'suhu_sensor_iot.csv', '365 hari · interval harian (D)')
  const px = x + 36
  const py = y + 66
  const pw = w - 60
  const ph = h - 104
  txt(c, 'DATA MENTAH HARIAN (SIGNAL + NOISE)', x + 22, y + 49, 9.5, 800, PALETTE.ink2)
  gridH(c, px, py, pw, ph, 4)

  const { obs } = genSignal(48)
  const p = easeOut(intro)
  const minV = 12
  const maxV = 42
  const xAt = (i: number) => px + (i / (obs.length - 1)) * pw
  const yAt = (v: number) => py + ph - ((v - minV) / (maxV - minV)) * ph
  const pts: Array<[number, number]> = obs.map((v, i) => [xAt(i), yAt(v)])

  c.save()
  c.beginPath()
  c.rect(px - 4, py - 8, (pw + 8) * p, ph + 16)
  c.clip()
  drawPolyline(c, pts, PALETTE.processDark, 2.1)
  pts.forEach(([ax, ay], i) => {
    if (i % 2 !== 0) return
    c.beginPath()
    c.arc(ax, ay, 2.7, 0, Math.PI * 2)
    c.fillStyle = PALETTE.cream
    c.fill()
    c.strokeStyle = PALETTE.processDark
    c.lineWidth = 1.2
    c.stroke()
  })
  c.restore()

  // Animated scanner cursor showing noisy reading
  const scanIdx = Math.floor(((t * 6) % obs.length))
  const sx = xAt(scanIdx)
  const sy = yAt(obs[scanIdx])
  c.save()
  c.strokeStyle = PALETTE.danger
  c.lineWidth = 1.2
  c.setLineDash([3, 3])
  c.beginPath()
  c.moveTo(sx, py)
  c.lineTo(sx, py + ph)
  c.stroke()
  c.setLineDash([])
  c.beginPath()
  c.arc(sx, sy, 5, 0, Math.PI * 2)
  c.fillStyle = PALETTE.danger
  c.fill()
  c.strokeStyle = PALETTE.cream
  c.lineWidth = 1.4
  c.stroke()
  c.restore()

  txt(c, '40°C', px - 8, py + 2, 8.5, 600, PALETTE.rawDark, 'right')
  txt(c, '25°C', px - 8, py + ph / 2, 8.5, 600, PALETTE.rawDark, 'right')
  txt(c, '15°C', px - 8, py + ph, 8.5, 600, PALETTE.rawDark, 'right')
  ;['Jan', 'Apr', 'Jul', 'Okt', 'Des'].forEach((m, i) => {
    txt(c, m, px + (i / 4) * pw, py + ph + 16, 9, 600, PALETTE.ink2, 'center')
  })
}

// 2. Four fundamental components in 2x2 grid
function drawComponentsGrid(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  const gap = 14
  const cw = (w - gap) / 2
  const ch = (h - gap) / 2
  const p = easeOut(intro)

  const panels = [
    {
      title: '1. Tren T(t)',
      sub: 'jangka panjang',
      color: PALETTE.processDark,
      fn: (i: number) => 0.15 + i * 0.72,
      kind: 'line',
    },
    {
      title: '2. Musiman S(t)',
      sub: 'periodik tetap',
      color: PALETTE.greenDark,
      fn: (i: number) => 0.5 + 0.36 * Math.sin(i * Math.PI * 6),
      kind: 'line',
    },
    {
      title: '3. Siklus C(t)',
      sub: 'tak periodik',
      color: PALETTE.outputDark,
      fn: (i: number) => 0.5 + 0.34 * Math.sin(i * Math.PI * 2.2 + 0.4) * (0.75 + 0.25 * Math.cos(i * 3)),
      kind: 'line',
    },
    {
      title: '4. Residu I(t)',
      sub: 'noise acak',
      color: PALETTE.dangerDark,
      fn: (i: number) => 0.5 + 0.34 * Math.sin(i * 37.3) * Math.cos(i * 19.7),
      kind: 'scatter',
    },
  ]

  panels.forEach((pan, idx) => {
    const col = idx % 2
    const row = Math.floor(idx / 2)
    const bx = x + col * (cw + gap)
    const by = y + row * (ch + gap)
    cardFrame(c, bx, by, cw, ch, pan.title, pan.sub)
    const px = bx + 18
    const py = by + 48
    const pw = cw - 36
    const ph = ch - 64
    gridH(c, px, py, pw, ph, 3)

    const n = 34
    const pts: Array<[number, number]> = []
    for (let i = 0; i < n; i++) {
      const u = i / (n - 1)
      const val = clamp(pan.fn(u), 0.08, 0.92)
      pts.push([px + u * pw, py + ph - val * ph])
    }

    c.save()
    c.beginPath()
    c.rect(px - 4, py - 6, (pw + 8) * p, ph + 12)
    c.clip()
    if (pan.kind === 'scatter') {
      // Zero reference line
      drawPolyline(c, [[px, py + ph / 2], [px + pw, py + ph / 2]], PALETTE.rawDark, 1.1, true)
      pts.forEach(([sx, sy]) => {
        c.beginPath()
        c.arc(sx, sy, 2.8, 0, Math.PI * 2)
        c.fillStyle = pan.color
        c.fill()
      })
    } else {
      drawPolyline(c, pts, pan.color, 2.3)
    }
    c.restore()
  })
}

// 3. Additive vs Multiplicative comparison
function drawAdditiveVsMult(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  const gap = 16
  const cw = (w - gap) / 2
  const p = easeOut(intro)
  const n = 36

  const specs = [
    {
      title: 'Model Aditif',
      sub: 'Y = T + S + C + I',
      note: 'Amplitudo musiman konstan',
      color: PALETTE.processDark,
      envColor: PALETTE.process,
      mult: false,
    },
    {
      title: 'Model Multiplikatif',
      sub: 'Y = T × S × C × I',
      note: 'Amplitudo membesar ikut tren',
      color: PALETTE.dangerDark,
      envColor: PALETTE.danger,
      mult: true,
    },
  ]

  specs.forEach((sp, idx) => {
    const bx = x + idx * (cw + gap)
    cardFrame(c, bx, y, cw, h, sp.title, sp.sub)
    txt(c, sp.note, bx + 18, y + 48, 9.5, 700, sp.color)

    const px = bx + 20
    const py = y + 66
    const pw = cw - 40
    const ph = h - 92
    gridH(c, px, py, pw, ph, 4)

    const pts: Array<[number, number]> = []
    const topEnv: Array<[number, number]> = []
    const botEnv: Array<[number, number]> = []
    const trPts: Array<[number, number]> = []

    for (let i = 0; i < n; i++) {
      const u = i / (n - 1)
      const tr = 0.24 + u * 0.52
      const amp = sp.mult ? 0.06 + u * 0.22 : 0.14
      const val = tr + amp * Math.sin(u * Math.PI * 8)
      const gx = px + u * pw
      pts.push([gx, py + ph - val * ph])
      trPts.push([gx, py + ph - tr * ph])
      topEnv.push([gx, py + ph - (tr + amp) * ph])
      botEnv.push([gx, py + ph - (tr - amp) * ph])
    }

    c.save()
    c.beginPath()
    c.rect(px - 4, py - 8, (pw + 8) * p, ph + 16)
    c.clip()

    // Shaded envelope
    c.beginPath()
    topEnv.forEach(([ex, ey], i) => (i === 0 ? c.moveTo(ex, ey) : c.lineTo(ex, ey)))
    for (let i = botEnv.length - 1; i >= 0; i--) c.lineTo(botEnv[i][0], botEnv[i][1])
    c.closePath()
    c.fillStyle = sp.mult ? 'rgba(224,128,79,.16)' : 'rgba(127,180,227,.18)'
    c.fill()

    drawPolyline(c, topEnv, sp.envColor, 1.3, true)
    drawPolyline(c, botEnv, sp.envColor, 1.3, true)
    drawPolyline(c, trPts, PALETTE.ink2, 1.4, true)
    drawPolyline(c, pts, sp.color, 2.3)
    c.restore()
  })
}

// 4. Resampling D -> W -> M
function drawResampling(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'df.resample("W").mean()', 'Harian (D) → Mingguan (W)')
  const px = x + 36
  const py = y + 68
  const pw = w - 60
  const ph = h - 106
  txt(c, 'TITIK HARIAN (ABU) VS RATA-RATA MINGGUAN (EMAS)', x + 22, y + 50, 9.5, 800, PALETTE.ink2)
  gridH(c, px, py, pw, ph, 4)

  const { obs } = genSignal(49)
  const p = easeOut(intro)
  const minV = 12
  const maxV = 42
  const xAt = (i: number) => px + (i / (obs.length - 1)) * pw
  const yAt = (v: number) => py + ph - ((v - minV) / (maxV - minV)) * ph

  // Daily noisy dots + faint line
  const dPts: Array<[number, number]> = obs.map((v, i) => [xAt(i), yAt(v)])
  c.save()
  c.globalAlpha = 0.55
  drawPolyline(c, dPts, PALETTE.rawDark, 1.2)
  dPts.forEach(([dx, dy]) => {
    c.beginPath()
    c.arc(dx, dy, 2.3, 0, Math.PI * 2)
    c.fillStyle = PALETTE.raw
    c.fill()
  })
  c.restore()

  // Weekly resampled averages (every 7 points)
  const wPts: Array<[number, number]> = []
  for (let g = 0; g < 7; g++) {
    const slice = obs.slice(g * 7, g * 7 + 7)
    const mean = slice.reduce((a, b) => a + b, 0) / slice.length
    const centerIdx = g * 7 + 3
    wPts.push([xAt(centerIdx), yAt(mean)])
  }

  c.save()
  c.beginPath()
  c.rect(px - 6, py - 10, (pw + 12) * p, ph + 20)
  c.clip()
  drawPolyline(c, wPts, PALETTE.outputDark, 2.8)
  wPts.forEach(([wx, wy], idx) => {
    // Subtle vertical bin divider
    c.beginPath()
    c.arc(wx, wy, 5.2, 0, Math.PI * 2)
    c.fillStyle = PALETTE.output
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1.4
    c.stroke()
    txt(c, `M${idx + 1}`, wx, py + ph + 16, 9, 700, PALETTE.ink2, 'center')
  })
  c.restore()
}

// 5. Moving Average SMA 7, SMA 30 & +-1 sigma volatility band
function drawMovingAvg(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'rolling(window=7 / 30)', 'Praktikum 1 · SMA & Pita ±1σ')
  const px = x + 36
  const py = y + 68
  const pw = w - 60
  const ph = h - 106
  txt(c, 'DATA MENTAH · SMA 7 · SMA 30 + PITA VOLATILITAS (±1σ)', x + 22, y + 50, 9.2, 800, PALETTE.ink2)
  gridH(c, px, py, pw, ph, 4)

  const n = 56
  const { obs, trend } = genSignal(n)
  const sma7: Array<[number, number]> = []
  const sma30: Array<[number, number]> = []
  const bandTop: Array<[number, number]> = []
  const bandBot: Array<[number, number]> = []
  const rawPts: Array<[number, number]> = []
  const minV = 12
  const maxV = 42
  const xAt = (i: number) => px + (i / (n - 1)) * pw
  const yAt = (v: number) => py + ph - ((v - minV) / (maxV - minV)) * ph

  for (let i = 0; i < n; i++) {
    rawPts.push([xAt(i), yAt(obs[i])])
    const w7 = obs.slice(Math.max(0, i - 3), Math.min(n, i + 4))
    const m7 = w7.reduce((a, b) => a + b, 0) / w7.length
    sma7.push([xAt(i), yAt(m7)])
    const m30 = trend[i] + 0.8 * Math.sin(i / 6)
    sma30.push([xAt(i), yAt(m30)])
    bandTop.push([xAt(i), yAt(m30 + 3.4)])
    bandBot.push([xAt(i), yAt(m30 - 3.4)])
  }

  const p = easeOut(intro)
  c.save()
  c.beginPath()
  c.rect(px - 4, py - 8, (pw + 8) * p, ph + 16)
  c.clip()

  // Shaded +-1 sigma band
  c.beginPath()
  bandTop.forEach(([bx, by], i) => (i === 0 ? c.moveTo(bx, by) : c.lineTo(bx, by)))
  for (let i = bandBot.length - 1; i >= 0; i--) c.lineTo(bandBot[i][0], bandBot[i][1])
  c.closePath()
  c.fillStyle = 'rgba(127,180,227,.24)'
  c.fill()

  drawPolyline(c, rawPts, PALETTE.raw, 1.3)
  drawPolyline(c, sma7, PALETTE.process, 2.0)
  drawPolyline(c, sma30, PALETTE.processDark, 2.9)
  c.restore()

  // Inline compact legend pills
  const lx = px + pw - 220
  const ly = py + 12
  rr(c, lx, ly - 10, 214, 22, 8)
  c.fillStyle = 'rgba(251,247,241,.9)'
  c.fill()
  c.strokeStyle = 'rgba(52,48,43,.2)'
  c.lineWidth = 1
  c.stroke()
  txt(c, '— Mentah', lx + 10, ly + 1, 8.8, 700, PALETTE.rawDark)
  txt(c, '— SMA 7', lx + 74, ly + 1, 8.8, 700, PALETTE.process)
  txt(c, '— SMA 30 ±1σ', lx + 132, ly + 1, 8.8, 800, PALETTE.processDark)

  ;['Jan', 'Mar', 'Mei', 'Jul', 'Sep', 'Des'].forEach((m, i) => {
    txt(c, m, px + (i / 5) * pw, py + ph + 16, 9, 600, PALETTE.ink2, 'center')
  })
}

// 6. 4-Panel Statsmodels seasonal_decompose
function drawDecompose4Panel(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'seasonal_decompose(model="additive")', 'Praktikum 2 · 4 Subplot')
  const px = x + 82
  const pw = w - 104
  const topY = y + 46
  const totalH = h - 68
  const gap = 8
  const rowH = (totalH - gap * 3) / 4
  const p = easeOut(intro)

  const { obs, trend, seas, resid } = genSignal(44)
  const panels = [
    { name: 'Observed', data: obs, min: 14, max: 42, col: PALETTE.ink, kind: 'line' },
    { name: 'Trend', data: trend, min: 14, max: 42, col: PALETTE.processDark, kind: 'line' },
    { name: 'Seasonal', data: seas, min: -6, max: 6, col: PALETTE.greenDark, kind: 'line' },
    { name: 'Residual', data: resid, min: -5, max: 5, col: PALETTE.dangerDark, kind: 'scatter' },
  ]

  panels.forEach((pan, rIdx) => {
    const ry = topY + rIdx * (rowH + gap)
    rr(c, px, ry, pw, rowH, 6)
    c.fillStyle = 'rgba(244,235,224,.45)'
    c.fill()
    c.strokeStyle = 'rgba(52,48,43,.18)'
    c.lineWidth = 1
    c.stroke()

    txt(c, pan.name, px - 10, ry + rowH / 2, 10, 700, pan.col, 'right')

    const pts: Array<[number, number]> = pan.data.map((v, i) => [
      px + 8 + (i / (pan.data.length - 1)) * (pw - 16),
      ry + rowH - 6 - ((v - pan.min) / (pan.max - pan.min)) * (rowH - 12),
    ])

    c.save()
    c.beginPath()
    c.rect(px + 2, ry + 1, (pw - 4) * p, rowH - 2)
    c.clip()
    if (pan.kind === 'scatter') {
      drawPolyline(c, [[px + 6, ry + rowH / 2], [px + pw - 6, ry + rowH / 2]], PALETTE.rawDark, 1, true)
      pts.forEach(([sx, sy]) => {
        c.beginPath()
        c.arc(sx, sy, 2.3, 0, Math.PI * 2)
        c.fillStyle = pan.col
        c.fill()
      })
    } else {
      drawPolyline(c, pts, pan.col, 2.0)
    }
    c.restore()
  })
}

// 7. Anatomy of Bullish vs Bearish Candlestick (OHLC)
function drawOHLCAnatomy(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'Anatomi Candlestick (OHLC)', 'Open · High · Low · Close')
  const p = easeOut(intro)
  const midX = x + w / 2

  c.save()
  c.strokeStyle = 'rgba(52,48,43,.14)'
  c.setLineDash([4, 4])
  c.beginPath()
  c.moveTo(midX, y + 48)
  c.lineTo(midX, y + h - 18)
  c.stroke()
  c.restore()

  const candles = [
    {
      cx: x + w * 0.25,
      title: 'Bullish (Naik)',
      sub: 'Close > Open',
      col: PALETTE.greenDark,
      fill: PALETTE.green,
      topLbl: 'Close',
      botLbl: 'Open',
    },
    {
      cx: x + w * 0.75,
      title: 'Bearish (Turun)',
      sub: 'Close < Open',
      col: PALETTE.dangerDark,
      fill: PALETTE.danger,
      topLbl: 'Open',
      botLbl: 'Close',
    },
  ]

  const topY = y + 92
  const botY = y + h - 42
  const bodyTop = topY + (botY - topY) * 0.26
  const bodyBot = topY + (botY - topY) * 0.74
  const bodyW = 40

  candles.forEach((cd, idx) => {
    txt(c, cd.title, cd.cx, y + 52, 11.5, 800, cd.col, 'center')
    txt(c, cd.sub, cd.cx, y + 67, 9.5, 600, PALETTE.ink2, 'center', true)

    c.save()
    c.globalAlpha = p
    // Wick (High to Low)
    c.strokeStyle = cd.col
    c.lineWidth = 2.8
    c.beginPath()
    c.moveTo(cd.cx, topY)
    c.lineTo(cd.cx, botY)
    c.stroke()

    // Real body
    rr(c, cd.cx - bodyW / 2, bodyTop, bodyW, bodyBot - bodyTop, 4)
    c.fillStyle = cd.fill
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1.6
    c.stroke()

    // Callout annotations on left/right of candle
    const dir = idx === 0 ? 1 : -1
    const align: CanvasTextAlign = idx === 0 ? 'left' : 'right'
    const tx = cd.cx + dir * 38
    const pts: Array<[number, string, string]> = [
      [topY + 2, 'High', PALETTE.ink],
      [(topY + bodyTop) / 2, 'Upper Shadow', PALETTE.ink2],
      [bodyTop + 4, cd.topLbl, cd.col],
      [(bodyTop + bodyBot) / 2, 'Real Body', PALETTE.ink],
      [bodyBot - 4, cd.botLbl, cd.col],
      [(bodyBot + botY) / 2, 'Lower Shadow', PALETTE.ink2],
      [botY - 2, 'Low', PALETTE.ink],
    ]
    pts.forEach(([py, label, col]) => {
      c.strokeStyle = 'rgba(52,48,43,.35)'
      c.lineWidth = 1
      c.beginPath()
      c.moveTo(cd.cx + dir * (Math.abs(py - (bodyTop + bodyBot) / 2) < (bodyBot - bodyTop) / 2 ? bodyW / 2 + 2 : 4), py)
      c.lineTo(tx - dir * 4, py)
      c.stroke()
      txt(c, label, tx, py, 9.3, 700, col, align)
    })
    c.restore()
  })
}

// 8. Financial Candlestick + MA20 + Bollinger + Volume subplot
function drawCandlestickDashboard(c: CanvasRenderingContext2D, t: number, x: number, y: number, w: number, h: number, intro: number) {
  cardFrame(c, x, y, w, h, 'go.Candlestick() + MA20 + Volume', 'Praktikum 3 & Bollinger Bands')
  const px = x + 36
  const pw = w - 58
  const topY = y + 48
  const priceH = (h - 80) * 0.68
  const volY = topY + priceH + 16
  const volH = (h - 80) * 0.28
  const p = easeOut(intro)

  gridH(c, px, topY, pw, priceH, 4)
  gridH(c, px, volY, pw, volH, 2)
  txt(c, 'OHLC + MA20 + ±2σ', px + 4, topY + 8, 8.8, 800, PALETTE.ink2)
  txt(c, 'Volume', px + 4, volY + 8, 8.8, 800, PALETTE.ink2)

  // Generate 22 OHLC bars
  const n = 22
  const bars: Array<{ o: number; h: number; l: number; c: number; ma: number; vol: number }> = []
  let prev = 50
  for (let i = 0; i < n; i++) {
    const delta = 4.2 * Math.sin(i * 0.65) + 2.4 * Math.cos(i * 1.45) + (i > 12 ? 1.4 : -0.3)
    const o = prev
    const cl = clamp(o + delta, 18, 88)
    const hi = Math.min(95, Math.max(o, cl) + 4 + (i % 3) * 2.2)
    const lo = Math.max(10, Math.min(o, cl) - 4 - ((i + 1) % 3) * 2.0)
    const ma = 46 + i * 1.15 + 3.2 * Math.sin(i * 0.35)
    const vol = 0.3 + 0.55 * Math.abs(Math.sin(i * 1.2 + 0.5))
    bars.push({ o, h: hi, l: lo, c: cl, ma, vol })
    prev = cl - 0.8
  }

  const slot = pw / n
  const xAt = (i: number) => px + (i + 0.5) * slot
  const yAt = (v: number) => topY + priceH - ((v - 8) / 92) * priceH

  const maPts: Array<[number, number]> = bars.map((b, i) => [xAt(i), yAt(b.ma)])
  const bbTop: Array<[number, number]> = bars.map((b, i) => [xAt(i), yAt(b.ma + 11)])
  const bbBot: Array<[number, number]> = bars.map((b, i) => [xAt(i), yAt(b.ma - 11)])

  c.save()
  c.beginPath()
  c.rect(px - 2, topY - 4, (pw + 4) * p, priceH + volH + 26)
  c.clip()

  // Bollinger band ±2 sigma shaded envelope
  c.beginPath()
  bbTop.forEach(([bx, by], i) => (i === 0 ? c.moveTo(bx, by) : c.lineTo(bx, by)))
  for (let i = bbBot.length - 1; i >= 0; i--) c.lineTo(bbBot[i][0], bbBot[i][1])
  c.closePath()
  c.fillStyle = 'rgba(230,185,79,.16)'
  c.fill()
  drawPolyline(c, bbTop, PALETTE.output, 1.1, true)
  drawPolyline(c, bbBot, PALETTE.output, 1.1, true)

  // Candlesticks + Volume bars
  const cw = Math.max(6, slot * 0.56)
  bars.forEach((b, i) => {
    const cx = xAt(i)
    const bull = b.c >= b.o
    const col = bull ? PALETTE.greenDark : PALETTE.dangerDark
    const fill = bull ? PALETTE.green : PALETTE.danger

    // Wick
    c.strokeStyle = col
    c.lineWidth = 1.6
    c.beginPath()
    c.moveTo(cx, yAt(b.h))
    c.lineTo(cx, yAt(b.l))
    c.stroke()

    // Candle body
    const yTop = yAt(Math.max(b.o, b.c))
    const yBot = yAt(Math.min(b.o, b.c))
    const bh = Math.max(3, yBot - yTop)
    c.fillStyle = fill
    c.fillRect(cx - cw / 2, yTop, cw, bh)
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1
    c.strokeRect(cx - cw / 2, yTop, cw, bh)

    // Volume bar
    const vh = b.vol * (volH - 10)
    c.fillStyle = bull ? 'rgba(107,155,88,.72)' : 'rgba(184,84,53,.72)'
    c.fillRect(cx - cw / 2, volY + volH - vh, cw, vh)
  })

  // MA20 smooth overlay
  drawPolyline(c, maPts, PALETTE.outputDark, 2.3)
  c.restore()
}

export function drawTimeSeriesScene(
  c: CanvasRenderingContext2D,
  scene: IsoScene,
  t: number,
  w: number,
  h: number,
  opts: { intro?: number } = {},
) {
  c.clearRect(0, 0, w, h)
  // Swiss gallery spotlight fading into drafting grid
  const bg = c.createRadialGradient(w * 0.5, h * 0.45, 20, w * 0.5, h * 0.45, Math.max(w, h) * 0.72)
  bg.addColorStop(0, 'rgba(255,255,255,.72)')
  bg.addColorStop(0.55, 'rgba(252,251,249,.35)')
  bg.addColorStop(1, 'rgba(252,251,249,0)')
  c.fillStyle = bg
  c.fillRect(0, 0, w, h)

  // Clean clear area below single-row HUD chips and above bottom caption card
  const padX = w < 560 ? 18 : 28
  const padTop = h > 260 ? 12 : 8
  const padBottom = h > 280 ? 52 : 26
  const x = padX
  const y = padTop
  const cw = Math.max(240, w - padX * 2)
  const ch = Math.max(180, h - padTop - padBottom)
  const intro = opts.intro ?? 1

  const kind = scene.nodes[0]?.type ?? 'ts_signal'
  switch (kind) {
    case 'ts_signal':
      drawRawSignal(c, t, x, y, cw, ch, intro)
      break
    case 'ts_components':
      drawComponentsGrid(c, t, x, y, cw, ch, intro)
      break
    case 'ts_models':
      drawAdditiveVsMult(c, t, x, y, cw, ch, intro)
      break
    case 'ts_resampling':
      drawResampling(c, t, x, y, cw, ch, intro)
      break
    case 'ts_moving_avg':
      drawMovingAvg(c, t, x, y, cw, ch, intro)
      break
    case 'ts_decompose':
      drawDecompose4Panel(c, t, x, y, cw, ch, intro)
      break
    case 'ts_ohlc':
      drawOHLCAnatomy(c, t, x, y, cw, ch, intro)
      break
    case 'ts_candlestick_vol':
      drawCandlestickDashboard(c, t, x, y, cw, ch, intro)
      break
    default:
      drawRawSignal(c, t, x, y, cw, ch, intro)
      break
  }
}
