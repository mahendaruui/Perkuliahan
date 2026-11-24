/* Isometric 2.5D canvas kit for the Big Data story canvases.
 * Design space is unbounded; drawScene() fits the scene to the canvas.
 * Palette semantics: raw data = gray/violet, process = blue,
 * output = gold, danger (shuffle/skew) = red-orange.
 */
export const ISO = { ux: 44, uy: 22, uz: 30 }

export const PALETTE = {
  ink: '#34302b',
  ink2: '#5c564e',
  cream: '#fbf7f1',
  paper: '#f4ebe0',
  raw: '#b7b1c2',
  rawDark: '#8f887e',
  process: '#7fb4e3',
  processDark: '#4c86ba',
  output: '#e6b94f',
  outputDark: '#b9872e',
  danger: '#e0804f',
  dangerDark: '#b85435',
  violet: '#cdbce6',
  green: '#b2d491',
  greenDark: '#6b9b58',
  blueSoft: '#c9dff2',
  goldSoft: '#f4dfa2',
  redSoft: '#f0bba5',
  teal: '#8dcfc5',
}

export type IsoNode = {
  id: string
  type: string
  x: number
  y: number
  z?: number
  label?: string
  sub?: string
  color?: string
  /** tag type only: pill fill */
  fill?: string
  status?: string
  scale?: number
}

export type IsoLink = {
  from: string
  to: string
  label?: string
  color?: string
  dashed?: boolean
  packets?: number
  reverse?: boolean
  /** vertical lift of the curve */
  lift?: number
}

export type IsoScene = {
  nodes: IsoNode[]
  links?: IsoLink[]
}

const NODE_HEIGHT: Record<string, number> = {
  server: 1.9,
  disk: 0.7,
  block: 0.8,
  file: 0.35,
  factory: 1.6,
  hive: 1.6,
  grid: 1.0,
  tower: 2.6,
  funnel: 1.7,
  truck: 1.2,
  chip: 0.8,
  prism: 2.0,
  dashboard: 1.3,
  folder: 0.5,
  book: 0.5,
  container: 1.5,
  filter: 1.5,
  gauge: 1.0,
  shield: 1.5,
  tube: 1.2,
  robot: 1.6,
  source: 0.9,
  bucket: 1.4,
  wall: 2.4,
  code: 1.4,
  symbol: 0.5,
  tag: 0,
}

export function isoPoint(x: number, y: number, z = 0) {
  return [ISO.ux * (x - y), ISO.uy * (x + y) - ISO.uz * z] as const
}

function clamp(v: number, a: number, b: number) {
  return Math.max(a, Math.min(b, v))
}

export function shade(hex: string, amount: number) {
  const h = hex.replace('#', '')
  const full = h.length === 3 ? h.split('').map((x) => x + x).join('') : h
  const r = clamp(parseInt(full.slice(0, 2), 16) + amount, 0, 255)
  const g = clamp(parseInt(full.slice(2, 4), 16) + amount, 0, 255)
  const b = clamp(parseInt(full.slice(4, 6), 16) + amount, 0, 255)
  return `rgb(${r},${g},${b})`
}

function rr(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  const rad = Math.min(r, w / 2, h / 2)
  c.beginPath()
  c.moveTo(x + rad, y)
  c.arcTo(x + w, y, x + w, y + h, rad)
  c.arcTo(x + w, y + h, x, y + h, rad)
  c.arcTo(x, y + h, x, y, rad)
  c.arcTo(x, y, x + w, y, rad)
  c.closePath()
}

export function pill(
  c: CanvasRenderingContext2D,
  text: string,
  sx: number,
  sy: number,
  fill = PALETTE.cream,
  color = PALETTE.ink,
  weight = 700,
  size = 11,
) {
  c.font = `${weight} ${size}px "JetBrains Mono", ui-monospace, monospace`
  const w = c.measureText(text).width + size * 1.5
  const h = size + 10
  rr(c, sx - w / 2 + 1.5, sy - h / 2 + 3, w, h, h / 2)
  c.fillStyle = 'rgba(52,48,43,.18)'
  c.fill()
  rr(c, sx - w / 2, sy - h / 2, w, h, h / 2)
  c.fillStyle = fill
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.2
  c.stroke()
  c.fillStyle = color
  c.textAlign = 'center'
  c.textBaseline = 'middle'
  c.fillText(text, sx, sy + 0.5)
  return w
}

/* ---------------- primiive shapes (local coordinates) ---------------- */

function shadow(c: CanvasRenderingContext2D, w: number, d: number) {
  c.save()
  c.globalAlpha = 0.13
  c.fillStyle = PALETTE.ink
  c.beginPath()
  c.ellipse(0, d * 0.34, w * 0.56, d * 0.5, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()
}

function cuboid(
  c: CanvasRenderingContext2D,
  w: number,
  d: number,
  h: number,
  top: string,
  left: string,
  right: string,
  baseY = 0,
  line = 1.4,
) {
  const dx = w / 2
  const dy = d / 4
  const b = [
    [0, baseY - dy],
    [dx, baseY],
    [0, baseY + dy],
    [-dx, baseY],
  ]
  const t = b.map(([x, y]) => [x, y - h])
  c.lineJoin = 'round'
  // left face
  c.beginPath()
  c.moveTo(b[3][0], b[3][1])
  c.lineTo(b[2][0], b[2][1])
  c.lineTo(t[2][0], t[2][1])
  c.lineTo(t[3][0], t[3][1])
  c.closePath()
  c.fillStyle = left
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = line
  c.stroke()
  // right face
  c.beginPath()
  c.moveTo(b[1][0], b[1][1])
  c.lineTo(b[2][0], b[2][1])
  c.lineTo(t[2][0], t[2][1])
  c.lineTo(t[1][0], t[1][1])
  c.closePath()
  c.fillStyle = right
  c.fill()
  c.stroke()
  // top face
  c.beginPath()
  c.moveTo(t[0][0], t[0][1])
  c.lineTo(t[1][0], t[1][1])
  c.lineTo(t[2][0], t[2][1])
  c.lineTo(t[3][0], t[3][1])
  c.closePath()
  c.fillStyle = top
  c.fill()
  c.stroke()
  return t
}

function cylinder(c: CanvasRenderingContext2D, rx: number, h: number, body: string, top = body, baseY = 0) {
  const ry = rx * 0.46
  c.beginPath()
  c.ellipse(0, baseY, rx, ry, 0, 0, Math.PI)
  c.lineTo(rx, baseY - h)
  c.ellipse(0, baseY - h, rx, ry, 0, 0, Math.PI, true)
  c.closePath()
  c.fillStyle = body
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.3
  c.stroke()
  c.beginPath()
  c.ellipse(0, baseY - h, rx, ry, 0, 0, Math.PI * 2)
  c.fillStyle = top
  c.fill()
  c.stroke()
}

function sideGlow(c: CanvasRenderingContext2D, w: number, h: number, color: string) {
  c.save()
  c.globalAlpha = 0.18
  c.fillStyle = color
  c.beginPath()
  c.ellipse(0, -h * 0.4, w * 0.7, h * 0.5, 0, 0, Math.PI * 2)
  c.fill()
  c.restore()
}

/* ---------------- icon renderers ---------------- */

function drawServer(c: CanvasRenderingContext2D, n: IsoNode, t: number) {
  const col = n.color ?? PALETTE.process
  const failed = n.status === 'failed' || n.status === 'smoke'
  const w = 60
  const d = 34
  const h = 88
  shadow(c, w, d)
  cuboid(c, w, d, h, failed ? PALETTE.redSoft : PALETTE.cream, failed ? PALETTE.danger : PALETTE.ink2, failed ? PALETTE.dangerDark : PALETTE.ink, 0, 1.5)
  // front face sits on the right-front plane
  const fy = -h + 7
  c.fillStyle = failed ? PALETTE.danger : col
  c.fillRect(-w * 0.3, fy, w * 0.56, 4)
  for (let i = 0; i < 4; i++) {
    const y = fy + 14 + i * 14
    c.fillStyle = 'rgba(52,48,43,.78)'
    c.fillRect(-w * 0.3, y, w * 0.36, 3.4)
    c.fillStyle = failed && i === 1 ? PALETTE.dangerDark : n.status === 'active' ? PALETTE.greenDark : col
    c.fillRect(-w * 0.3 + w * 0.42, y - 1, 4.4, 4.4)
  }
  if (n.status === 'smoke') {
    for (let i = 0; i < 3; i++) {
      c.save()
      c.globalAlpha = 0.24
      c.fillStyle = PALETTE.rawDark
      c.beginPath()
      c.arc(6 + i * 9, -h - 8 - i * 11 - Math.sin(t + i) * 2, 7 + i * 3, 0, Math.PI * 2)
      c.fill()
      c.restore()
    }
  }
  if (failed) {
    c.beginPath()
    c.arc(w * 0.42, -h - 6, 11, 0, Math.PI * 2)
    c.fillStyle = PALETTE.danger
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1.3
    c.stroke()
    c.fillStyle = PALETTE.cream
    c.font = '800 15px "JetBrains Mono", monospace'
    c.textAlign = 'center'
    c.textBaseline = 'middle'
    c.fillText('!', w * 0.42, -h - 5)
  }
}

function drawDisk(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 64, 36)
  cuboid(c, 64, 36, 12, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -14), 0, 1.2)
  c.beginPath()
  c.ellipse(0, -24, 24, 10.5, 0, 0, Math.PI * 2)
  c.fillStyle = col
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.stroke()
  c.beginPath()
  c.ellipse(0, -24, 8, 3.4, 0, 0, Math.PI * 2)
  c.fillStyle = PALETTE.cream
  c.fill()
  c.stroke()
  c.beginPath()
  c.moveTo(4, -26)
  c.lineTo(20, -31)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 2
  c.stroke()
}

function drawBlock(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 28, 16)
  cuboid(c, 28, 16, 24, shade(col, 22), shade(col, -18), col, 0, 1.2)
}

function drawFile(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.raw
  shadow(c, 52, 26)
  cuboid(c, 52, 26, 8, shade(col, 18), shade(col, -16), col, 0, 1.2)
  // folded page corner
  c.beginPath()
  c.moveTo(26, -8)
  c.lineTo(14, -8)
  c.lineTo(26, -18)
  c.closePath()
  c.fillStyle = PALETTE.cream
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.stroke()
  c.strokeStyle = 'rgba(52,48,43,.38)'
  c.lineWidth = 1
  for (let i = 0; i < 3; i++) {
    c.beginPath()
    c.moveTo(-16, -3 + i * 4)
    c.lineTo(6, -3 + i * 4)
    c.stroke()
  }
}

function drawFactory(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 72, 40)
  cuboid(c, 72, 40, 44, PALETTE.blueSoft, shade(col, -16), col, 0, 1.4)
  // roof chimney block
  c.save()
  c.translate(-14, -44)
  cuboid(c, 18, 12, 24, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1)
  c.restore()
  c.save()
  c.translate(14, -48)
  cuboid(c, 15, 11, 32, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1)
  c.restore()
  // gear
  c.beginPath()
  c.arc(0, -26, 8, 0, Math.PI * 2)
  c.fillStyle = PALETTE.output
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.2
  c.stroke()
  c.beginPath()
  c.arc(0, -26, 3, 0, Math.PI * 2)
  c.fillStyle = PALETTE.cream
  c.fill()
}

function drawHive(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.output
  shadow(c, 62, 32)
  const cells = [
    [0, -26], [-20, -14], [20, -14], [-20, -46], [20, -46], [0, -58],
  ]
  cells.forEach(([dx, dy], i) => {
    const r = 13
    c.save()
    c.translate(dx, dy)
    c.beginPath()
    for (let k = 0; k < 6; k++) {
      const a = (Math.PI / 3) * k - Math.PI / 6
      const x = Math.cos(a) * r
      const y = Math.sin(a) * r * 0.9
      k === 0 ? c.moveTo(x, y) : c.lineTo(x, y)
    }
    c.closePath()
    c.fillStyle = i % 2 ? shade(col, -10) : col
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1.2
    c.stroke()
    c.restore()
  })
}

function drawGrid(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.violet
  shadow(c, 68, 36)
  cuboid(c, 68, 36, 8, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.1)
  for (let r = 0; r < 3; r++) {
    for (let k = 0; k < 3; k++) {
      c.save()
      c.translate(-20 + k * 20, -8 + r * 9 + 2)
      cuboid(c, 15, 8, 9, shade(col, 18), shade(col, -18), col, 0, 0.9)
      c.restore()
    }
  }
}

function drawTower(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 46, 26)
  cuboid(c, 46, 26, 108, shade(col, 16), shade(col, -18), col, 0, 1.4)
  cuboid(c, 30, 17, 12, PALETTE.output, PALETTE.outputDark, PALETTE.outputDark, -108, 1)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.beginPath()
  c.moveTo(0, -122)
  c.lineTo(0, -142)
  c.stroke()
  c.beginPath()
  c.arc(0, -145, 4, 0, Math.PI * 2)
  c.fillStyle = PALETTE.danger
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.stroke()
}

function drawFunnel(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 60, 32)
  c.beginPath()
  c.moveTo(-30, -76)
  c.lineTo(30, -76)
  c.lineTo(11, -14)
  c.lineTo(-11, -14)
  c.closePath()
  c.fillStyle = col
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.stroke()
  c.beginPath()
  c.ellipse(0, -76, 30, 12, 0, 0, Math.PI * 2)
  c.fillStyle = PALETTE.goldSoft
  c.fill()
  c.stroke()
  cuboid(c, 22, 10, 16, shade(col, 12), shade(col, -16), col, -14, 1)
}

function drawTruck(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.output
  shadow(c, 66, 34)
  c.save()
  c.translate(7, -18)
  cuboid(c, 50, 26, 26, shade(col, 18), shade(col, -16), col, 0, 1.2)
  c.restore()
  c.save()
  c.translate(-25, -16)
  cuboid(c, 22, 22, 30, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.1)
  c.restore()
  ;[-18, 22].forEach((x) => {
    c.beginPath()
    c.arc(x, 0, 6.4, 0, Math.PI * 2)
    c.fillStyle = PALETTE.ink
    c.fill()
  })
  if (n.status === 'overloaded') {
    const cols = [PALETTE.raw, PALETTE.process, PALETTE.output, PALETTE.violet]
    for (let i = 0; i < 4; i++) {
      c.save()
      c.translate(-2 + i * 12, -48 - (i % 2) * 7)
      cuboid(c, 16, 9, 10, shade(cols[i], 16), shade(cols[i], -18), cols[i], 0, 0.9)
      c.restore()
    }
    c.save()
    c.globalAlpha = 0.7
    c.strokeStyle = PALETTE.danger
    c.lineWidth = 2
    c.beginPath()
    c.moveTo(-28, -70)
    c.lineTo(-20, -62)
    c.moveTo(30, -70)
    c.lineTo(38, -62)
    c.stroke()
    c.restore()
  }
}

function drawChip(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 70, 36)
  cuboid(c, 78, 40, 8, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.2)
  cuboid(c, 58, 28, 9, PALETTE.process, PALETTE.processDark, PALETTE.process, -8, 1.1)
  for (let i = 0; i < 6; i++) {
    c.fillStyle = PALETTE.output
    c.fillRect(-25 + i * 10, -4, 4, 4)
    c.fillRect(-25 + i * 10, -22, 4, 4)
  }
  c.beginPath()
  c.moveTo(-5, -40)
  c.lineTo(3, -26)
  c.lineTo(-5, -23)
  c.lineTo(1, -11)
  c.lineTo(11, -26)
  c.lineTo(3, -28)
  c.closePath()
  c.fillStyle = PALETTE.output
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.stroke()
}

function drawPrism(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 64, 34)
  c.beginPath()
  c.moveTo(0, -96)
  c.lineTo(36, -40)
  c.lineTo(0, 0)
  c.lineTo(-36, -40)
  c.closePath()
  c.fillStyle = 'rgba(205,188,230,.82)'
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.5
  c.stroke()
  c.beginPath()
  c.moveTo(0, -96)
  c.lineTo(0, 0)
  c.lineTo(-36, -40)
  c.closePath()
  c.fillStyle = 'rgba(255,255,255,.4)'
  c.fill()
  c.beginPath()
  c.moveTo(0, -96)
  c.lineTo(0, 0)
  c.strokeStyle = 'rgba(52,48,43,.35)'
  c.lineWidth = 1
  c.stroke()
}

function drawDashboard(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 96, 40)
  c.save()
  c.translate(0, -58)
  rr(c, -50, -34, 100, 68, 7)
  c.fillStyle = PALETTE.ink
  c.fill()
  rr(c, -45, -39, 90, 68, 6)
  c.fillStyle = PALETTE.cream
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.3
  c.stroke()
  ;[0.4, 0.65, 0.95].forEach((v, i) => {
    c.fillStyle = i === 2 ? PALETTE.output : PALETTE.process
    c.fillRect(-32 + i * 22, 20 - v * 46, 13, v * 46)
  })
  c.strokeStyle = PALETTE.danger
  c.lineWidth = 2
  c.beginPath()
  c.moveTo(-34, 8)
  c.lineTo(-14, -4)
  c.lineTo(6, 2)
  c.lineTo(30, -18)
  c.stroke()
  c.restore()
}

function drawFolder(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.output
  shadow(c, 54, 26)
  cuboid(c, 56, 26, 6, shade(col, 18), shade(col, -16), col, 0, 1.1)
  c.save()
  c.translate(-13, -9)
  cuboid(c, 20, 8, 11, col, shade(col, -18), col, 0, 0.9)
  c.restore()
}

function drawBook(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 52, 26)
  cuboid(c, 58, 26, 8, PALETTE.output, PALETTE.outputDark, PALETTE.output, 0, 1.1)
  cuboid(c, 52, 23, 7, PALETTE.cream, PALETTE.paper, PALETTE.paper, -8, 0.9)
  c.strokeStyle = 'rgba(52,48,43,.35)'
  c.lineWidth = 1
  c.beginPath()
  c.moveTo(-14, -12)
  c.lineTo(12, -12)
  c.stroke()
}

function drawContainer(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.output
  shadow(c, 56, 30)
  for (let i = 0; i < 3; i++) {
    c.save()
    c.translate(i % 2 ? 4 : -4, -i * 20)
    cuboid(c, 52, 26, 17, i === 2 ? shade(col, 16) : PALETTE.blueSoft, shade(PALETTE.blueSoft, -16), i === 2 ? col : PALETTE.blueSoft, 0, 1.1)
    c.restore()
  }
}

function drawFilter(c: CanvasRenderingContext2D, n: IsoNode) {
  for (let i = 0; i < 4; i++) {
    c.save()
    c.translate(0, -i * 17)
    cuboid(c, 66, 30, 6, i === 3 ? PALETTE.green : PALETTE.blueSoft, PALETTE.process, PALETTE.process, 0, 1.1)
    c.restore()
  }
}

function drawGauge(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 58, 28)
  cuboid(c, 62, 30, 11, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.1)
  c.beginPath()
  c.arc(0, -30, 25, 0, Math.PI * 2)
  c.fillStyle = PALETTE.cream
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.stroke()
  c.beginPath()
  c.arc(0, -30, 18, Math.PI * 0.85, Math.PI * 1.95)
  c.strokeStyle = PALETTE.process
  c.lineWidth = 3
  c.stroke()
  c.beginPath()
  c.moveTo(0, -30)
  c.lineTo(14, -41)
  c.strokeStyle = PALETTE.danger
  c.lineWidth = 2.2
  c.lineCap = 'round'
  c.stroke()
  c.beginPath()
  c.arc(0, -30, 3.4, 0, Math.PI * 2)
  c.fillStyle = PALETTE.ink
  c.fill()
}

function drawShield(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 50, 26)
  c.save()
  c.translate(0, -36)
  c.beginPath()
  c.moveTo(0, -34)
  c.lineTo(30, -22)
  c.lineTo(23, 12)
  c.lineTo(0, 36)
  c.lineTo(-23, 12)
  c.lineTo(-30, -22)
  c.closePath()
  c.fillStyle = PALETTE.green
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.5
  c.stroke()
  c.beginPath()
  c.moveTo(-11, 0)
  c.lineTo(-2, 10)
  c.lineTo(15, -12)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 2.6
  c.lineCap = 'round'
  c.stroke()
  c.restore()
}

function drawTube(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 36, 20)
  // glass body
  c.beginPath()
  c.moveTo(-12, -52)
  c.lineTo(-12, -9)
  c.quadraticCurveTo(-12, 0, 0, 0)
  c.quadraticCurveTo(12, 0, 12, -9)
  c.lineTo(12, -52)
  c.closePath()
  c.fillStyle = 'rgba(233,242,250,.86)'
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.3
  c.stroke()
  // green liquid
  c.save()
  c.clip()
  c.fillStyle = PALETTE.green
  c.fillRect(-13, -26, 26, 27)
  c.beginPath()
  c.ellipse(0, -26, 12, 4.6, 0, 0, Math.PI * 2)
  c.fillStyle = shade(PALETTE.green, 18)
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.stroke()
  c.restore()
  // rim
  c.beginPath()
  c.ellipse(0, -52, 12, 4.8, 0, 0, Math.PI * 2)
  c.fillStyle = PALETTE.cream
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.3
  c.stroke()
}

function drawRobot(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 50, 26)
  // body
  cuboid(c, 46, 24, 22, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.2)
  c.fillStyle = PALETTE.process
  c.fillRect(-9, -17, 14, 8)
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.strokeRect(-9, -17, 14, 8)
  // head
  c.save()
  c.translate(0, -22)
  cuboid(c, 30, 16, 18, PALETTE.cream, PALETTE.paper, shade(PALETTE.paper, -8), 0, 1.1)
  c.fillStyle = PALETTE.ink
  c.fillRect(-9, -13, 4.4, 4.4)
  c.fillRect(4.2, -13, 4.4, 4.4)
  c.fillStyle = PALETTE.output
  c.fillRect(-4, -6.5, 9, 2.6)
  c.restore()
  // antenna
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.5
  c.beginPath()
  c.moveTo(0, -40)
  c.lineTo(0, -47)
  c.stroke()
  c.beginPath()
  c.arc(0, -49.5, 3, 0, Math.PI * 2)
  c.fillStyle = PALETTE.danger
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1
  c.stroke()
  // arm with a small block
  c.strokeStyle = PALETTE.output
  c.lineWidth = 3.4
  c.lineCap = 'round'
  c.beginPath()
  c.moveTo(20, -24)
  c.lineTo(30, -34)
  c.stroke()
  c.save()
  c.translate(33, -40)
  cuboid(c, 12, 7, 10, PALETTE.blueSoft, PALETTE.processDark, PALETTE.process, 0, 0.9)
  c.restore()
}

function drawSource(c: CanvasRenderingContext2D, n: IsoNode) {
  shadow(c, 56, 28)
  cuboid(c, 58, 28, 8, PALETTE.ink2, PALETTE.ink2, shade(PALETTE.ink2, -12), 0, 1.1)
  ;[PALETTE.raw, PALETTE.process, PALETTE.output].forEach((col, i) => {
    c.save()
    c.translate(-16 + i * 16, -12)
    cuboid(c, 14, 8, 12, shade(col, 16), shade(col, -18), col, 0, 0.9)
    c.restore()
  })
}

function drawBucket(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.output
  shadow(c, 58, 30)
  c.beginPath()
  c.moveTo(-26, -50)
  c.lineTo(26, -50)
  c.lineTo(19, 0)
  c.lineTo(-19, 0)
  c.closePath()
  c.fillStyle = shade(col, 8)
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  c.stroke()
  c.beginPath()
  c.ellipse(0, -50, 26, 10, 0, 0, Math.PI * 2)
  c.fillStyle = PALETTE.goldSoft
  c.fill()
  c.stroke()
  c.beginPath()
  c.ellipse(0, 0, 19, 7.4, 0, 0, Math.PI)
  c.fillStyle = shade(col, -14)
  c.fill()
  c.stroke()
  // objects peeking out
  ;[-10, 4].forEach((x, i) => {
    c.save()
    c.translate(x, -54 - i * 3)
    cuboid(c, 14, 8, 10, i ? PALETTE.process : PALETTE.raw, shade(i ? PALETTE.process : PALETTE.raw, -16), i ? PALETTE.process : PALETTE.raw, 0, 0.9)
    c.restore()
  })
}

function drawWall(c: CanvasRenderingContext2D, n: IsoNode) {
  c.save()
  c.globalAlpha = 0.16
  c.fillStyle = PALETTE.danger
  c.fillRect(-2, -104, 4, 108)
  c.restore()
  c.strokeStyle = PALETTE.danger
  c.setLineDash([5, 5])
  c.lineWidth = 1.6
  c.beginPath()
  c.moveTo(0, 4)
  c.lineTo(0, -104)
  c.stroke()
  c.setLineDash([])
  c.beginPath()
  c.arc(0, -104, 3.5, 0, Math.PI * 2)
  c.fillStyle = PALETTE.danger
  c.fill()
}

function drawTag(c: CanvasRenderingContext2D, n: IsoNode) {
  pill(c, n.label ?? '', 0, 0, n.fill ?? PALETTE.cream, n.color ?? PALETTE.ink, 700, 11)
}

function drawCode(c: CanvasRenderingContext2D, n: IsoNode) {
  const col = n.color ?? PALETTE.process
  shadow(c, 96, 40)
  c.save()
  c.translate(0, -54)
  rr(c, -48, -36, 96, 70, 8)
  c.fillStyle = PALETTE.ink
  c.fill()
  rr(c, -43, -31, 86, 60, 5)
  c.fillStyle = '#2f2b27'
  c.fill()
  ;['#e0804f', '#e6b94f', '#b2d491'].forEach((dot, i) => {
    c.beginPath()
    c.arc(-35 + i * 8, -25, 2.4, 0, Math.PI * 2)
    c.fillStyle = dot
    c.fill()
  })
  const lines: Array<[string, number, number]> = [
    [col, -15, 28],
    [PALETTE.raw, -9, 18],
    [PALETTE.output, -3, 34],
    [PALETTE.green, 3, 22],
    [PALETTE.violet, 9, 16],
  ]
  lines.forEach(([color, y, w]) => {
    rr(c, -34, y - 1.7, w, 3.4, 1.7)
    c.fillStyle = color
    c.fill()
  })
  c.fillStyle = PALETTE.ink2
  c.fillRect(-7, 34, 14, 6)
  c.fillRect(-17, 40, 34, 4)
  c.restore()
}

function drawSymbol(c: CanvasRenderingContext2D, n: IsoNode) {
  const status = n.status ?? 'process'
  const col =
    n.color ??
    (status === 'start'
      ? PALETTE.green
      : status === 'decision'
        ? PALETTE.output
        : status === 'io'
          ? PALETTE.process
          : status === 'prep'
            ? PALETTE.violet
            : PALETTE.teal)
  shadow(c, 66, 34)
  cuboid(c, 66, 34, 10, PALETTE.cream, PALETTE.paper, '#e8ddd0', 0, 1.2)
  c.save()
  c.transform(0.7, 0.35, -0.7, 0.35, 0, -10.4)
  c.fillStyle = col
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.4
  const w = 24
  const h = 11
  if (status === 'start') {
    rr(c, -w, -h, w * 2, h * 2, h * 2)
    c.fill()
    c.stroke()
  } else if (status === 'io') {
    c.beginPath()
    c.moveTo(-w + 7, -h)
    c.lineTo(w + 7, -h)
    c.lineTo(w - 7, h)
    c.lineTo(-w - 7, h)
    c.closePath()
    c.fill()
    c.stroke()
  } else if (status === 'decision') {
    c.beginPath()
    c.moveTo(0, -h - 4)
    c.lineTo(w + 5, 0)
    c.lineTo(0, h + 4)
    c.lineTo(-w - 5, 0)
    c.closePath()
    c.fill()
    c.stroke()
  } else if (status === 'prep') {
    c.beginPath()
    for (let i = 0; i < 6; i++) {
      const a = (Math.PI / 3) * i - Math.PI / 6
      const x = Math.cos(a) * (w + 2)
      const y = Math.sin(a) * (h + 3)
      i === 0 ? c.moveTo(x, y) : c.lineTo(x, y)
    }
    c.closePath()
    c.fill()
    c.stroke()
  } else if (status === 'connector') {
    c.beginPath()
    c.arc(0, 0, 12, 0, Math.PI * 2)
    c.fill()
    c.stroke()
  } else {
    c.beginPath()
    c.rect(-w, -h, w * 2, h * 2)
    c.fill()
    c.stroke()
  }
  c.restore()
}

const RENDERERS: Record<string, (c: CanvasRenderingContext2D, n: IsoNode, t: number) => void> = {
  server: drawServer,
  disk: drawDisk,
  block: drawBlock,
  file: drawFile,
  factory: drawFactory,
  hive: drawHive,
  grid: drawGrid,
  tower: drawTower,
  funnel: drawFunnel,
  truck: drawTruck,
  chip: drawChip,
  prism: drawPrism,
  dashboard: drawDashboard,
  folder: drawFolder,
  book: drawBook,
  container: drawContainer,
  filter: drawFilter,
  gauge: drawGauge,
  shield: drawShield,
  tube: drawTube,
  robot: drawRobot,
  source: drawSource,
  bucket: drawBucket,
  wall: drawWall,
  code: drawCode,
  symbol: drawSymbol,
  tag: drawTag,
}

/** Visual footprint used for fitting and link anchors (design px, above anchor). */
const NODE_EXTENT: Record<string, { w: number; up: number }> = {
  server: { w: 62, up: 108 },
  disk: { w: 66, up: 56 },
  block: { w: 30, up: 36 },
  file: { w: 54, up: 34 },
  factory: { w: 74, up: 96 },
  hive: { w: 66, up: 86 },
  grid: { w: 70, up: 52 },
  tower: { w: 48, up: 156 },
  funnel: { w: 62, up: 100 },
  truck: { w: 70, up: 82 },
  chip: { w: 80, up: 66 },
  prism: { w: 66, up: 116 },
  dashboard: { w: 100, up: 112 },
  folder: { w: 56, up: 40 },
  book: { w: 60, up: 40 },
  container: { w: 56, up: 78 },
  filter: { w: 68, up: 76 },
  gauge: { w: 62, up: 74 },
  shield: { w: 52, up: 88 },
  tube: { w: 42, up: 66 },
  robot: { w: 56, up: 74 },
  source: { w: 58, up: 44 },
  bucket: { w: 58, up: 78 },
  wall: { w: 10, up: 112 },
  code: { w: 100, up: 116 },
  symbol: { w: 68, up: 32 },
  tag: { w: 90, up: 18 },
}

export function nodeLabelAnchor(node: IsoNode) {
  const [px, py] = isoPoint(node.x, node.y, node.z ?? 0)
  const up = (NODE_EXTENT[node.type]?.up ?? 40) + 14
  return [px, py - up * (node.scale ?? 1), px, py] as const
}

export function drawNode(c: CanvasRenderingContext2D, node: IsoNode, t: number) {
  const [px, py] = isoPoint(node.x, node.y, node.z ?? 0)
  const render = RENDERERS[node.type] ?? RENDERERS.block
  const scale = node.scale ?? 1
  c.save()
  c.translate(px, py)
  if (scale !== 1) c.scale(scale, scale)
  const bob = node.type === 'block' || node.type === 'file' ? Math.sin(t * 1.4 + node.x * 1.3 + node.y) * 1.8 : 0
  if (bob) c.translate(0, bob)
  render(c, node, t)
  c.restore()
}

export function drawLink(
  c: CanvasRenderingContext2D,
  link: IsoLink,
  from: IsoNode,
  to: IsoNode,
  t: number,
) {
  const [ax, ay] = isoPoint(from.x, from.y, from.z ?? 0)
  const [bx, by] = isoPoint(to.x, to.y, to.z ?? 0)
  const aUp = (NODE_EXTENT[from.type]?.up ?? 40) * 0.28
  const bUp = (NODE_EXTENT[to.type]?.up ?? 40) * 0.3
  const sx = ax
  const sy = ay - aUp
  const ex = bx
  const ey = by - bUp
  const mx = (sx + ex) / 2
  const my = Math.min(sy, ey) - (link.lift ?? 34)
  c.save()
  c.strokeStyle = link.color ?? PALETTE.ink2
  c.lineWidth = 1.7
  c.lineCap = 'round'
  if (link.dashed) {
    c.setLineDash([6, 5])
    c.lineDashOffset = -(t * 16) % 11
  }
  c.beginPath()
  c.moveTo(sx, sy)
  c.quadraticCurveTo(mx, my, ex, ey)
  c.stroke()
  c.setLineDash([])
  const angle = Math.atan2(ey - my, ex - mx)
  const ah = 6
  c.beginPath()
  c.moveTo(ex, ey)
  c.lineTo(ex - Math.cos(angle - 0.45) * ah, ey - Math.sin(angle - 0.45) * ah)
  c.lineTo(ex - Math.cos(angle + 0.45) * ah, ey - Math.sin(angle + 0.45) * ah)
  c.closePath()
  c.fillStyle = link.color ?? PALETTE.ink2
  c.fill()
  const count = link.packets ?? 2
  for (let i = 0; i < count; i++) {
    const p = (t * 0.22 + i / count + (link.reverse ? 0.5 : 0)) % 1
    const q = quadratic(sx, sy, mx, my, ex, ey, p)
    c.beginPath()
    c.arc(q[0], q[1], 4, 0, Math.PI * 2)
    c.fillStyle = link.color ?? PALETTE.output
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1
    c.stroke()
  }
  if (link.label) {
    const [lx, ly] = quadratic(sx, sy, mx, my, ex, ey, 0.5)
    c.restore()
    return [lx, ly - 14] as const
  }
  c.restore()
  return null
}

function quadratic(x0: number, y0: number, cx: number, cy: number, x1: number, y1: number, t: number) {
  const mt = 1 - t
  return [mt * mt * x0 + 2 * mt * t * cx + t * t * x1, mt * mt * y0 + 2 * mt * t * cy + t * t * y1]
}

function measure(scene: IsoScene) {
  let minX = Infinity
  let maxX = -Infinity
  let minY = Infinity
  let maxY = -Infinity
  scene.nodes.forEach((n) => {
    const [px, py] = isoPoint(n.x, n.y, n.z ?? 0)
    const e = NODE_EXTENT[n.type] ?? { w: 50, up: 50 }
    const s = n.scale ?? 1
    const w = (e.w / 2) * s
    minX = Math.min(minX, px - w - 26)
    maxX = Math.max(maxX, px + w + 26)
    minY = Math.min(minY, py - e.up * s - (n.label ? 30 : 8))
    maxY = Math.max(maxY, py + 26)
  })
  if (!Number.isFinite(minX)) {
    minX = -100
    maxX = 100
    minY = -80
    maxY = 40
  }
  return { minX, maxX, minY, maxY }
}

export function drawScene(
  c: CanvasRenderingContext2D,
  scene: IsoScene,
  t: number,
  w: number,
  h: number,
  opts: { intro?: number } = {},
) {
  c.clearRect(0, 0, w, h)
  // warm paper backdrop
  const bg = c.createRadialGradient(w * 0.5, h * 0.42, 20, w * 0.5, h * 0.42, Math.max(w, h) * 0.72)
  bg.addColorStop(0, 'rgba(255,250,242,.9)')
  bg.addColorStop(0.55, 'rgba(250,240,227,.55)')
  bg.addColorStop(1, 'rgba(240,226,209,0)')
  c.fillStyle = bg
  c.fillRect(0, 0, w, h)

  const { minX, maxX, minY, maxY } = measure(scene)
  const bw = Math.max(120, maxX - minX)
  const bh = Math.max(90, maxY - minY)
  const s = clamp(Math.min((w - 44) / bw, (h - 30) / bh), 0.52, 1.55)
  const cx = (minX + maxX) / 2
  const cy = (minY + maxY) / 2
  const ox = w / 2
  const oy = h / 2 + 4
  const labelSize = w < 560 ? 9.5 : w < 760 ? 10.5 : 11
  const tx = (x: number) => ox + s * (x - cx)
  const ty = (y: number) => oy + s * (y - cy)

  c.save()
  c.translate(ox, oy)
  c.scale(s, s)
  c.translate(-cx, -cy)

  // isometric floor grid
  c.save()
  c.strokeStyle = 'rgba(120,96,66,.10)'
  c.lineWidth = 1
  for (let i = -13; i <= 13; i++) {
    const a = isoPoint(i, -13, 0)
    const b = isoPoint(i, 13, 0)
    c.beginPath()
    c.moveTo(a[0], a[1])
    c.lineTo(b[0], b[1])
    c.stroke()
    const d = isoPoint(-13, i, 0)
    const e = isoPoint(13, i, 0)
    c.beginPath()
    c.moveTo(d[0], d[1])
    c.lineTo(e[0], e[1])
    c.stroke()
  }
  c.restore()

  const byId = new Map(scene.nodes.map((n) => [n.id, n]))
  const linkLabels: Array<{ text: string; x: number; y: number }> = []
  ;(scene.links ?? []).forEach((link) => {
    const from = byId.get(link.from)
    const to = byId.get(link.to)
    if (!from || !to) return
    const anchor = drawLink(c, link, from, to, t)
    if (anchor && link.label) linkLabels.push({ text: link.label, x: anchor[0], y: anchor[1] })
  })

  const sorted = [...scene.nodes].sort((a, b) => a.x + a.y - (b.x + b.y) || (a.z ?? 0) - (b.z ?? 0))
  const intro = opts.intro ?? 1
  const shown: Array<{ node: IsoNode; local: number }> = []
  sorted.forEach((node, i) => {
    const local = clamp(intro * 1.5 - i * 0.045, 0, 1)
    if (local <= 0) return
    shown.push({ node, local })
    c.save()
    c.globalAlpha = local
    c.translate(0, (1 - local) * 16)
    drawNode(c, node, t)
    c.restore()
  })
  c.restore()

  // Labels are drawn in screen space so they stay crisp and readable.
  linkLabels.forEach((label) => {
    pill(c, label.text, clamp(tx(label.x), 70, w - 70), clamp(ty(label.y), 16, h - 12), PALETTE.cream, PALETTE.ink, 700, labelSize)
  })
  shown.forEach(({ node, local }) => {
    if (!node.label) return
    c.save()
    c.globalAlpha = local
    const [lx, ly] = nodeLabelAnchor(node)
    if (node.type === 'tag') {
      pill(c, node.label, clamp(tx(lx), 76, w - 76), clamp(ty(ly), 16, h - 12), node.fill ?? PALETTE.cream, PALETTE.ink, 700, labelSize)
    } else {
      pill(c, node.label, clamp(tx(lx), 58, w - 58), clamp(ty(ly), 14, h - 10), PALETTE.cream, PALETTE.ink, 700, labelSize)
    }
    c.restore()
  })
}
