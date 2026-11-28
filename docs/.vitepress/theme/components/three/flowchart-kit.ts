/* Pure 2D ISO 5807 Flowchart canvas renderer sharing StoryCanvas2D controls. */

import type { IsoLink, IsoNode, IsoScene } from './iso-kit'
import { PALETTE, shade } from './iso-kit'

const FLOW = { ux: 155, uy: 102 }

function clamp(v: number, a: number, b: number) {
  return Math.max(a, Math.min(b, v))
}

function rr(c: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  c.beginPath()
  c.roundRect(x, y, w, h, r)
}

function pill(
  c: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  fill: string = PALETTE.cream,
  ink: string = PALETTE.ink,
  weight = 700,
  size = 11,
) {
  c.save()
  c.font = `${weight} ${size}px "Plus Jakarta Sans", sans-serif`
  const padX = 9
  const w = Math.ceil(c.measureText(text).width) + padX * 2
  const h = size + 10
  rr(c, x - w / 2, y - h / 2, w, h, h / 2)
  c.fillStyle = fill
  c.fill()
  c.strokeStyle = PALETTE.ink
  c.lineWidth = 1.25
  c.stroke()
  c.fillStyle = ink
  c.textAlign = 'center'
  c.textBaseline = 'middle'
  c.fillText(text, x, y + 0.5)
  c.restore()
}

function nodeBox(n: IsoNode): { w: number; h: number } {
  const s = n.scale ?? 1
  const textLen = Math.max((n.label ?? '').length, (n.sub ?? '').length)
  if (n.type === 'connector') return { w: 36 * s, h: 36 * s }
  if (n.type === 'decision') {
    const w = Math.max(158, textLen * 7.6 + 44) * s
    const h = Math.max(76, (n.sub ? 84 : 74)) * s
    return { w, h }
  }
  if (n.type === 'start' || n.type === 'end') {
    const w = Math.max(124, textLen * 7.4 + 34) * s
    return { w, h: 44 * s }
  }
  if (n.type === 'io') {
    const w = Math.max(152, textLen * 7.4 + 42) * s
    return { w, h: (n.sub ? 54 : 46) * s }
  }
  // process / codebox
  const w = Math.max(156, textLen * 7.4 + 30) * s
  const h = (n.sub ? 58 : 46) * s
  return { w, h }
}

function nodeCenter(n: IsoNode): [number, number] {
  return [n.x * FLOW.ux, n.y * FLOW.uy]
}

function drawNodeText(c: CanvasRenderingContext2D, n: IsoNode, maxW: number, ink = PALETTE.ink) {
  const label = n.label ?? ''
  const sub = n.sub ?? ''
  c.save()
  c.fillStyle = ink
  c.textAlign = 'center'
  c.textBaseline = 'middle'
  if (sub) {
    c.font = `700 11.5px "Plus Jakarta Sans", sans-serif`
    c.fillText(label, 0, -9, maxW)
    c.font = `600 10.5px "Fira Code", "JetBrains Mono", monospace`
    c.fillStyle = PALETTE.ink2
    c.fillText(sub, 0, 10, maxW)
  } else {
    c.font = `700 12px "Plus Jakarta Sans", sans-serif`
    c.fillText(label, 0, 0.5, maxW)
  }
  c.restore()
}

function drawFlowNode(c: CanvasRenderingContext2D, n: IsoNode) {
  const [cx, cy] = nodeCenter(n)
  const { w, h } = nodeBox(n)
  const failed = n.status === 'failed'
  const fill =
    n.color ??
    (n.type === 'start'
      ? PALETTE.green
      : n.type === 'end'
        ? failed
          ? PALETTE.redSoft
          : PALETTE.blueSoft
        : n.type === 'decision'
          ? PALETTE.goldSoft
          : n.type === 'io'
            ? PALETTE.blueSoft
            : n.type === 'connector'
              ? PALETTE.cream
              : PALETTE.cream)

  c.save()
  c.translate(cx, cy)

  // Soft 2D drop shadow
  c.save()
  c.translate(0, 3)
  c.fillStyle = 'rgba(52,48,43,.10)'
  if (n.type === 'start' || n.type === 'end') {
    rr(c, -w / 2, -h / 2, w, h, h / 2)
    c.fill()
  } else if (n.type === 'connector') {
    c.beginPath()
    c.arc(0, 0, w / 2, 0, Math.PI * 2)
    c.fill()
  } else if (n.type === 'decision') {
    c.beginPath()
    c.moveTo(0, -h / 2)
    c.lineTo(w / 2, 0)
    c.lineTo(0, h / 2)
    c.lineTo(-w / 2, 0)
    c.closePath()
    c.fill()
  } else if (n.type === 'io') {
    const skew = 13
    c.beginPath()
    c.moveTo(-w / 2 + skew, -h / 2)
    c.lineTo(w / 2 + skew, -h / 2)
    c.lineTo(w / 2 - skew, h / 2)
    c.lineTo(-w / 2 - skew, h / 2)
    c.closePath()
    c.fill()
  } else {
    rr(c, -w / 2, -h / 2, w, h, 8)
    c.fill()
  }
  c.restore()

  c.strokeStyle = failed ? PALETTE.dangerDark : PALETTE.ink
  c.lineWidth = failed ? 1.8 : 1.5

  if (n.type === 'start' || n.type === 'end') {
    rr(c, -w / 2, -h / 2, w, h, h / 2)
    c.fillStyle = fill
    c.fill()
    c.stroke()
    drawNodeText(c, n, w - 20)
  } else if (n.type === 'connector') {
    c.beginPath()
    c.arc(0, 0, w / 2, 0, Math.PI * 2)
    c.fillStyle = fill
    c.fill()
    c.stroke()
    if (n.label) {
      c.fillStyle = PALETTE.ink
      c.font = `700 10.5px "Plus Jakarta Sans", sans-serif`
      c.textAlign = 'center'
      c.textBaseline = 'middle'
      c.fillText(n.label, 0, 0.5, w - 6)
    }
  } else if (n.type === 'decision') {
    c.beginPath()
    c.moveTo(0, -h / 2)
    c.lineTo(w / 2, 0)
    c.lineTo(0, h / 2)
    c.lineTo(-w / 2, 0)
    c.closePath()
    c.fillStyle = fill
    c.fill()
    c.stroke()
    drawNodeText(c, n, w * 0.66)
  } else if (n.type === 'io') {
    const skew = 13
    c.beginPath()
    c.moveTo(-w / 2 + skew, -h / 2)
    c.lineTo(w / 2 + skew, -h / 2)
    c.lineTo(w / 2 - skew, h / 2)
    c.lineTo(-w / 2 - skew, h / 2)
    c.closePath()
    c.fillStyle = fill
    c.fill()
    c.stroke()
    drawNodeText(c, n, w - 30)
  } else {
    // Process / Code block (ISO rectangle with crisp header accent if color set)
    rr(c, -w / 2, -h / 2, w, h, 8)
    c.fillStyle = n.type === 'codebox' ? '#fdfaf4' : PALETTE.cream
    c.fill()
    c.stroke()

    if (n.color) {
      c.save()
      c.beginPath()
      c.roundRect(-w / 2 + 1, -h / 2 + 1, w - 2, 7, [7, 7, 0, 0])
      c.fillStyle = failed ? PALETTE.danger : shade(n.color, 4)
      c.fill()
      c.restore()
    }
    c.save()
    if (n.color) c.translate(0, 3)
    drawNodeText(c, n, w - 18)
    c.restore()
  }

  c.restore()
}

function portPoint(n: IsoNode, side: 'top' | 'bottom' | 'left' | 'right'): [number, number] {
  const [cx, cy] = nodeCenter(n)
  const { w, h } = nodeBox(n)
  if (side === 'top') return [cx, cy - h / 2]
  if (side === 'bottom') return [cx, cy + h / 2]
  if (side === 'left') return [cx - w / 2, cy]
  return [cx + w / 2, cy]
}

function quadratic(x0: number, y0: number, cx: number, cy: number, x1: number, y1: number, t: number) {
  const mt = 1 - t
  return [mt * mt * x0 + 2 * mt * t * cx + t * t * x1, mt * mt * y0 + 2 * mt * t * cy + t * t * y1] as const
}

function drawFlowLink(c: CanvasRenderingContext2D, link: IsoLink, from: IsoNode, to: IsoNode, t: number) {
  const [fx, fy] = nodeCenter(from)
  const [tx, ty] = nodeCenter(to)
  const dx = tx - fx
  const dy = ty - fy

  let startSide: 'top' | 'bottom' | 'left' | 'right'
  let endSide: 'top' | 'bottom' | 'left' | 'right'

  if (Math.abs(dy) >= Math.abs(dx) * 0.65) {
    startSide = dy >= 0 ? 'bottom' : 'top'
    endSide = dy >= 0 ? 'top' : 'bottom'
  } else {
    startSide = dx >= 0 ? 'right' : 'left'
    endSide = dx >= 0 ? 'left' : 'right'
  }

  // Decision side branches exit from left/right if target is horizontally displaced
  if (from.type === 'decision' && Math.abs(dx) > 90 && Math.abs(dy) < 160) {
    startSide = dx >= 0 ? 'right' : 'left'
    endSide = dy > 25 ? 'top' : dx >= 0 ? 'left' : 'right'
  }

  const [sx, sy] = portPoint(from, startSide)
  const [ex, ey] = portPoint(to, endSide)

  // Control point for clean curve or straight/elbowed flowline
  const mxBase = (sx + ex) / 2
  const myBase = (sy + ey) / 2
  let cx = mxBase
  let cy = myBase
  if (link.lift) {
    const len = Math.hypot(ex - sx, ey - sy) || 1
    const nx = -(ey - sy) / len
    const ny = (ex - sx) / len
    cx = mxBase + nx * link.lift
    cy = myBase + ny * link.lift
  } else if (startSide !== endSide && (startSide === 'right' || startSide === 'left') && endSide === 'top') {
    cx = ex
    cy = sy
  } else if (startSide === 'bottom' && (endSide === 'left' || endSide === 'right')) {
    cx = sx
    cy = ey
  }

  const col = link.color ?? PALETTE.ink2
  c.save()
  c.strokeStyle = col
  c.lineWidth = 1.85
  c.lineCap = 'round'
  if (link.dashed) {
    c.setLineDash([6, 5])
    c.lineDashOffset = -(t * 16) % 11
  }
  c.beginPath()
  c.moveTo(sx, sy)
  c.quadraticCurveTo(cx, cy, ex, ey)
  c.stroke()
  c.setLineDash([])

  // Arrowhead at end
  const tangentX = ex - cx
  const tangentY = ey - cy
  const angle = Math.atan2(tangentY || ey - sy, tangentX || ex - sx)
  const ah = 7
  c.beginPath()
  c.moveTo(ex, ey)
  c.lineTo(ex - Math.cos(angle - 0.42) * ah, ey - Math.sin(angle - 0.42) * ah)
  c.lineTo(ex - Math.cos(angle + 0.42) * ah, ey - Math.sin(angle + 0.42) * ah)
  c.closePath()
  c.fillStyle = col
  c.fill()

  // Moving execution pulses
  const count = link.packets ?? 1
  for (let i = 0; i < count; i++) {
    const p = (t * 0.28 + i / count + (link.reverse ? 0.5 : 0)) % 1
    const [qx, qy] = quadratic(sx, sy, cx, cy, ex, ey, p)
    c.beginPath()
    c.arc(qx, qy, 3.8, 0, Math.PI * 2)
    c.fillStyle = link.color ?? PALETTE.output
    c.fill()
    c.strokeStyle = PALETTE.ink
    c.lineWidth = 1
    c.stroke()
  }

  if (link.label) {
    const [lx, ly] = quadratic(sx, sy, cx, cy, ex, ey, 0.46)
    c.restore()
    return [lx, ly] as const
  }
  c.restore()
  return null
}

function measureFlow(scene: IsoScene) {
  let minX = Infinity
  let maxX = -Infinity
  let minY = Infinity
  let maxY = -Infinity
  scene.nodes.forEach((n) => {
    const [cx, cy] = nodeCenter(n)
    const { w, h } = nodeBox(n)
    minX = Math.min(minX, cx - w / 2 - 22)
    maxX = Math.max(maxX, cx + w / 2 + 22)
    minY = Math.min(minY, cy - h / 2 - 20)
    maxY = Math.max(maxY, cy + h / 2 + 20)
  })
  if (!Number.isFinite(minX)) {
    return { minX: -120, maxX: 120, minY: -90, maxY: 90 }
  }
  return { minX, maxX, minY, maxY }
}

export function drawFlowchartScene(
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

  const { minX, maxX, minY, maxY } = measureFlow(scene)
  const bw = Math.max(180, maxX - minX)
  const bh = Math.max(140, maxY - minY)
  // Leave breathing room below single-row HUD chips and above bottom caption pill
  const padTop = h > 260 ? 12 : 8
  const padBottom = h > 280 ? 52 : 26
  const s = clamp(Math.min((w - 56) / bw, (h - padTop - padBottom) / bh), 0.44, 1.24)
  const cx = (minX + maxX) / 2
  const cy = (minY + maxY) / 2
  const ox = w / 2
  const oy = padTop + (h - padTop - padBottom) / 2
  const labelSize = w < 560 ? 9.5 : 10.5
  const tx = (x: number) => ox + s * (x - cx)
  const ty = (y: number) => oy + s * (y - cy)

  c.save()
  c.translate(ox, oy)
  c.scale(s, s)
  c.translate(-cx, -cy)

  // Subtle 2D orthogonal dot grid (no 3D isometric grid)
  c.save()
  c.fillStyle = 'rgba(120,96,66,.18)'
  const step = 36
  const gx0 = Math.floor((minX - 180) / step) * step
  const gx1 = Math.ceil((maxX + 180) / step) * step
  const gy0 = Math.floor((minY - 120) / step) * step
  const gy1 = Math.ceil((maxY + 120) / step) * step
  for (let gx = gx0; gx <= gx1; gx += step) {
    for (let gy = gy0; gy <= gy1; gy += step) {
      c.beginPath()
      c.arc(gx, gy, 1.15, 0, Math.PI * 2)
      c.fill()
    }
  }
  c.restore()

  const byId = new Map(scene.nodes.map((n) => [n.id, n]))
  const linkLabels: Array<{ text: string; x: number; y: number; color?: string }> = []
  ;(scene.links ?? []).forEach((link) => {
    const from = byId.get(link.from)
    const to = byId.get(link.to)
    if (!from || !to) return
    const anchor = drawFlowLink(c, link, from, to, t)
    if (anchor && link.label) linkLabels.push({ text: link.label, x: anchor[0], y: anchor[1], color: link.color })
  })

  const intro = opts.intro ?? 1
  scene.nodes.forEach((node, i) => {
    const local = clamp(intro * 1.5 - i * 0.05, 0, 1)
    if (local <= 0) return
    c.save()
    c.globalAlpha = local
    c.translate(0, (1 - local) * 10)
    drawFlowNode(c, node)
    c.restore()
  })

  c.restore()

  // Screen-space crisp branch labels
  linkLabels.forEach((label) => {
    pill(
      c,
      label.text,
      clamp(tx(label.x), 48, w - 48),
      clamp(ty(label.y), 16, h - 14),
      PALETTE.cream,
      label.color === PALETTE.danger ? PALETTE.dangerDark : PALETTE.ink,
      700,
      labelSize,
    )
  })
}
