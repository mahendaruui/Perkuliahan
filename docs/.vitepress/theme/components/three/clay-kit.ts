/* Low-poly clay icon kit for the Big Data story canvases. */
export const CLAY = {
  ink: 0x34302b,
  inkSoft: 0x5c564e,
  cream: 0xfbf7f1,
  paper: 0xe8ddd0,
  raw: 0xb7b1c2,
  rawDark: 0x8f887e,
  process: 0x7fb4e3,
  processDark: 0x4c86ba,
  output: 0xe6b94f,
  outputDark: 0xb9872e,
  danger: 0xe0804f,
  dangerDark: 0xb85435,
  violet: 0xcdbce6,
  green: 0xb2d491,
  greenDark: 0x6b9b58,
  blueSoft: 0xc9dff2,
  goldSoft: 0xf4dfa2,
  redSoft: 0xf0bba5,
  teal: 0x8dcfc5,
}

type KitContext = {
  THREE: any
  stageGroup: any
  nodes: any[]
  label: (text: string, fill?: number, textColor?: number) => any
  beam: (start: any, end: any, options?: any) => any
}

export function createClayKit(ctx: KitContext) {
  const { THREE, stageGroup, nodes, label, beam } = ctx

  const mat = (color: number, opts: any = {}) =>
    new THREE.MeshStandardMaterial({
      color,
      roughness: 0.86,
      metalness: 0.02,
      flatShading: true,
      ...opts,
    })

  const box = (w: number, h: number, d: number, color: number, x = 0, y = 0, z = 0) => {
    const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat(color))
    mesh.position.set(x, y, z)
    mesh.castShadow = true
    mesh.receiveShadow = true
    return mesh
  }

  const cyl = (rt: number, rb: number, h: number, color: number, seg = 8, x = 0, y = 0, z = 0, open = false) => {
    const mesh = new THREE.Mesh(
      new THREE.CylinderGeometry(rt, rb, h, seg, 1, open),
      mat(color, open ? { side: THREE.DoubleSide, transparent: true, opacity: 0.9 } : {}),
    )
    mesh.position.set(x, y, z)
    mesh.castShadow = true
    mesh.receiveShadow = true
    return mesh
  }

  const edges = (group: any, w: number, h: number, d: number, x = 0, y = 0, z = 0, opacity = 0.22) => {
    const line = new THREE.LineSegments(
      new THREE.EdgesGeometry(new THREE.BoxGeometry(w, h, d)),
      new THREE.LineBasicMaterial({ color: CLAY.ink, transparent: true, opacity }),
    )
    line.position.set(x, y, z)
    group.add(line)
  }

  const addLabel = (group: any, text: string, y: number, fill = CLAY.cream, textColor = CLAY.ink, sx = 1.6) => {
    const sprite = label(text, fill, textColor)
    if (sprite) {
      sprite.position.set(0, y, 0)
      sprite.scale.set(sx, 0.38, 1)
      group.add(sprite)
    }
  }

  const finish = (group: any) => {
    stageGroup.add(group)
    return group
  }

  const server = (o: {
    x: number
    y?: number
    z?: number
    title: string
    height?: number
    slots?: number
    color?: number
    status?: 'ok' | 'failed' | 'smoke' | 'tired'
    active?: boolean
    label?: boolean
    labelScale?: number
  }) => {
    const g = new THREE.Group()
    const baseY = o.y ?? -2.85
    const h = o.height ?? 1.55
    const w = 0.95
    const d = 0.72
    g.position.set(o.x, baseY, o.z ?? 0)
    g.userData.noBob = true
    const failed = o.status === 'failed' || o.status === 'smoke'
    const body = box(w, h, d, failed ? 0x70423a : o.color ?? CLAY.ink, 0, h / 2, 0)
    g.add(body)
    edges(g, w, h, d, 0, h / 2, 0, 0.55)
    g.add(box(w * 0.82, h * 0.78, 0.035, failed ? CLAY.redSoft : CLAY.cream, 0, h / 2, d / 2 + 0.02))
    const slots = o.slots ?? 4
    const led = failed ? CLAY.danger : o.active ? CLAY.green : CLAY.process
    for (let i = 0; i < slots; i++) {
      const sy = h * 0.28 + (h * 0.56 / slots) * i
      g.add(box(w * 0.58, 0.055, 0.015, CLAY.ink, -w * 0.06, sy, d / 2 + 0.045))
      g.add(box(0.055, 0.055, 0.015, failed && i === 1 ? CLAY.danger : led, w * 0.33, sy, d / 2 + 0.055))
    }
    g.add(box(w * 0.9, 0.055, d * 0.9, failed ? CLAY.danger : o.color ?? CLAY.process, 0, h + 0.02, 0))
    if (o.status === 'smoke') {
      for (let i = 0; i < 3; i++) {
        const puff = new THREE.Mesh(
          new THREE.IcosahedronGeometry(0.18 + i * 0.07, 0),
          new THREE.MeshBasicMaterial({ color: CLAY.rawDark, transparent: true, opacity: 0.28 }),
        )
        puff.position.set(0.15 + i * 0.12, h + 0.25 + i * 0.22, 0)
        g.add(puff)
      }
    }
    if (o.status === 'tired') {
      g.rotation.z = -0.08
    }
    if (o.label !== false) addLabel(g, o.title, h + 0.42, failed ? CLAY.redSoft : CLAY.cream, CLAY.ink, o.labelScale ?? 1.55)
    if (o.status === 'failed' || o.status === 'smoke') addLabel(g, '!', h + 0.95, CLAY.danger, CLAY.cream, 0.75)
    return finish(g)
  }

  const disk = (o: { x: number; y?: number; z?: number; title?: string; color?: number; scale?: number; tired?: boolean }) => {
    const g = new THREE.Group()
    const baseY = o.y ?? -2.85
    g.position.set(o.x, baseY, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.02, 0.2, 0.9, CLAY.ink, 0, 0.1, 0))
    edges(g, 1.02, 0.2, 0.9, 0, 0.1, 0, 0.4)
    const platter = cyl(0.36, 0.36, 0.075, o.color ?? 0xc6bbac, 24, 0, 0.27, 0)
    platter.material = mat(o.color ?? 0xc6bbac, { metalness: 0.35, roughness: 0.38 })
    g.add(platter)
    g.add(cyl(0.065, 0.065, 0.1, CLAY.ink, 12, 0, 0.33, 0))
    g.add(box(0.46, 0.03, 0.055, CLAY.ink, 0.14, 0.35, 0))
    if (o.tired) g.rotation.z = 0.07
    if (o.title) addLabel(g, o.title, 0.8, CLAY.cream, CLAY.ink, 1.35)
    if (o.scale) g.scale.setScalar(o.scale)
    return finish(g)
  }

  const block = (o: { x: number; y: number; z?: number; size?: number; color: number; label?: string; bob?: boolean }) => {
    const size = o.size ?? 0.32
    const g = new THREE.Group()
    g.position.set(o.x, o.y, o.z ?? 0)
    g.userData.baseY = o.y
    g.userData.phase = Math.random() * Math.PI * 2
    g.add(box(size, size, size, o.color, 0, 0, 0))
    edges(g, size, size, size, 0, 0, 0, 0.45)
    if (o.label) addLabel(g, o.label, size * 0.85, CLAY.cream, CLAY.ink, 1.2)
    stageGroup.add(g)
    if (o.bob !== false) nodes.push(g)
    return g
  }

  const file = (o: { x: number; y: number; z?: number; title: string; color?: number; size?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y, o.z ?? 0)
    const s = o.size ?? 1
    g.add(box(1.0 * s, 0.08 * s, 0.76 * s, o.color ?? CLAY.raw, 0, 0, 0))
    for (let i = 0; i < 3; i++) {
      g.add(box(0.62 * s, 0.012, 0.022 * s, CLAY.inkSoft, -0.08 * s, 0.052 * s, -0.16 * s + i * 0.13 * s))
    }
    addLabel(g, o.title, 0.4 * s, CLAY.cream, CLAY.ink, 1.65)
    return finish(g)
  }

  const factory = (o: { x: number; y?: number; z?: number; title?: string; color?: number; scale?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const base = box(1.6, 0.9, 1.1, o.color ?? CLAY.process, 0, 0.45, 0)
    g.add(base)
    edges(g, 1.6, 0.9, 1.1, 0, 0.45, 0, 0.3)
    const roof = box(1.7, 0.12, 1.2, CLAY.inkSoft, 0, 0.96, 0)
    roof.rotation.z = 0.0
    g.add(roof)
    g.add(cyl(0.13, 0.16, 0.55, CLAY.inkSoft, 8, -0.45, 1.25, 0.2))
    g.add(cyl(0.13, 0.16, 0.75, CLAY.inkSoft, 8, 0.4, 1.35, 0.2))
    const gear = cyl(0.2, 0.2, 0.07, CLAY.output, 8, 0.35, 0.48, 0.58)
    gear.rotation.x = Math.PI / 2
    g.add(gear)
    if (o.scale) g.scale.setScalar(o.scale)
    if (o.title) addLabel(g, o.title, 1.55, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const hive = (o: { x: number; y?: number; z?: number; title?: string; color?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const cells = [
      [0, 0.9, 0], [-0.4, 0.55, 0], [0.4, 0.55, 0], [-0.4, 1.25, 0], [0.4, 1.25, 0], [0, 0.55, 0.45], [0, 1.25, 0.45],
    ]
    cells.forEach(([x, y, z]) => {
      const c = cyl(0.24, 0.24, 0.62, o.color ?? CLAY.output, 6, x, y, z)
      c.rotation.x = Math.PI / 2
      g.add(c)
    })
    addLabel(g, o.title ?? 'Hive', 1.85, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const grid = (o: { x: number; y?: number; z?: number; title?: string; color?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.8, 0.12, 1.2, CLAY.ink, 0, 0.06, 0))
    for (let row = 0; row < 3; row++) {
      for (let col = 0; col < 3; col++) {
        g.add(box(0.42, 0.16, 0.3, o.color ?? CLAY.violet, -0.55 + col * 0.55, 0.2 + row * 0.2, 0))
      }
    }
    addLabel(g, o.title ?? 'HBase', 1.2, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const tower = (o: { x: number; y?: number; z?: number; title?: string; color?: number; height?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const h = o.height ?? 2.2
    g.add(box(0.8, h, 0.8, o.color ?? CLAY.process, 0, h / 2, 0))
    edges(g, 0.8, h, 0.8, 0, h / 2, 0, 0.35)
    g.add(box(1.15, 0.25, 1.15, CLAY.inkSoft, 0, h + 0.12, 0))
    g.add(box(0.5, 0.2, 0.5, CLAY.output, 0, h + 0.35, 0))
    g.add(cyl(0.035, 0.035, 0.8, CLAY.ink, 6, 0, h + 0.8, 0))
    g.add(cyl(0.07, 0.07, 0.12, CLAY.danger, 6, 0, h + 1.2, 0))
    addLabel(g, o.title ?? 'YARN', h + 1.55, CLAY.cream, CLAY.ink, 1.5)
    return finish(g)
  }

  const funnel = (o: { x: number; y?: number; z?: number; title?: string; color?: number; scale?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const body = cyl(0.75, 0.26, 1.15, o.color ?? CLAY.process, 16, 0, 1.0, 0, true)
    g.add(body)
    g.add(cyl(0.28, 0.28, 0.6, o.color ?? CLAY.process, 12, 0, 0.3, 0))
    g.add(new THREE.Mesh(new THREE.TorusGeometry(0.75, 0.035, 6, 24), mat(CLAY.ink)))
    const rim = g.children[g.children.length - 1]
    rim.rotation.x = Math.PI / 2
    rim.position.y = 1.58
    if (o.scale) g.scale.setScalar(o.scale)
    if (o.title) addLabel(g, o.title, 1.95, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const truck = (o: { x: number; y?: number; z?: number; title?: string; color?: number; scale?: number; overloaded?: boolean }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const s = o.scale ?? 1
    g.add(box(1.6 * s, 0.72 * s, 0.9 * s, o.color ?? CLAY.output, 0.2 * s, 0.62 * s, 0))
    edges(g, 1.6 * s, 0.72 * s, 0.9 * s, 0.2 * s, 0.62 * s, 0, 0.3)
    g.add(box(0.62 * s, 0.66 * s, 0.86 * s, CLAY.inkSoft, -0.72 * s, 0.58 * s, 0))
    g.add(box(0.34 * s, 0.25 * s, 0.02 * s, CLAY.blueSoft, -0.72 * s, 0.68 * s, 0.44 * s))
    ;[-0.52, 0.14, 0.7].forEach((wx) => {
      const wheel = cyl(0.18 * s, 0.18 * s, 0.15 * s, CLAY.ink, 12, wx * s, 0.2 * s, 0.43 * s)
      wheel.rotation.z = Math.PI / 2
      g.add(wheel)
    })
    if (o.overloaded) {
      for (let i = 0; i < 4; i++) {
        g.add(box(0.3 * s, 0.25 * s, 0.3 * s, [CLAY.raw, CLAY.process, CLAY.output, CLAY.violet][i], -0.1 * s + i * 0.3 * s, 1.1 * s, 0))
      }
    }
    if (o.title) addLabel(g, o.title, 1.6 * s, CLAY.cream, CLAY.ink, 1.5)
    return finish(g)
  }

  const chip = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.75, 0.18, 1.3, CLAY.ink, 0, 0.1, 0))
    g.add(box(1.35, 0.16, 0.95, CLAY.process, 0, 0.25, 0))
    for (let i = 0; i < 8; i++) {
      g.add(box(0.08, 0.06, 0.22, CLAY.output, -0.65 + i * 0.19, 0.36, 0.61))
      g.add(box(0.08, 0.06, 0.22, CLAY.output, -0.65 + i * 0.19, 0.36, -0.61))
    }
    const glow = new THREE.Mesh(
      new THREE.PlaneGeometry(1.2, 0.8),
      new THREE.MeshBasicMaterial({ color: CLAY.output, transparent: true, opacity: 0.16, side: THREE.DoubleSide }),
    )
    glow.rotation.x = -Math.PI / 2
    glow.position.y = 0.4
    g.add(glow)
    const boltA = box(0.07, 0.3, 0.05, CLAY.output, -0.04, 0.82, 0.15)
    boltA.rotation.z = 0.55
    g.add(boltA)
    const boltB = box(0.07, 0.3, 0.05, CLAY.output, 0.1, 0.62, 0.15)
    boltB.rotation.z = -0.55
    g.add(boltB)
    if (o.title) addLabel(g, o.title, 1.35, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const prism = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const m = new THREE.Mesh(
      new THREE.OctahedronGeometry(0.85, 0),
      mat(CLAY.violet, { transparent: true, opacity: 0.72, roughness: 0.2, metalness: 0.2 }),
    )
    m.position.y = 1.1
    m.castShadow = true
    g.add(m)
    g.add(box(1.25, 0.12, 1.05, CLAY.ink, 0, 0.08, 0))
    addLabel(g, o.title ?? 'Catalyst', 2.15, CLAY.cream, CLAY.ink, 1.5)
    return finish(g)
  }

  const dashboard = (o: { x: number; y: number; z?: number; title?: string; gold?: boolean }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y, o.z ?? 0)
    g.add(box(1.9, 1.2, 0.12, CLAY.ink, 0, 0, 0))
    g.add(box(1.72, 1.03, 0.04, CLAY.cream, 0, 0, 0.08))
    ;[0.35, 0.62, 0.9].forEach((v, i) => {
      g.add(box(0.28, v * 0.72, 0.05, i === 2 ? CLAY.output : CLAY.process, -0.5 + i * 0.42, -0.45 + v * 0.36, 0.13))
    })
    if (o.title) addLabel(g, o.title, 0.85, CLAY.cream, CLAY.ink, 1.35)
    return finish(g)
  }

  const folder = (o: { x: number; y?: number; z?: number; title: string; color?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.0, 0.12, 0.68, o.color ?? CLAY.output, 0, 0.06, 0))
    g.add(box(0.42, 0.1, 0.24, o.color ?? CLAY.output, -0.26, 0.16, -0.2))
    addLabel(g, o.title, 0.62, CLAY.cream, CLAY.ink, 1.2)
    return finish(g)
  }

  const book = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.1, 0.12, 0.75, CLAY.output, 0, 0.06, 0))
    g.add(box(1.0, 0.08, 0.68, CLAY.blueSoft, 0.05, 0.16, 0))
    g.add(box(0.95, 0.07, 0.62, CLAY.cream, -0.04, 0.24, 0))
    addLabel(g, o.title ?? 'Metastore', 0.75, CLAY.cream, CLAY.ink, 1.55)
    return finish(g)
  }

  const container = (o: { x: number; y?: number; z?: number; title?: string; color?: number; count?: number }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    const n = o.count ?? 4
    for (let i = 0; i < n; i++) {
      const b = box(0.9, 0.35, 0.7, i % 2 ? o.color ?? CLAY.output : CLAY.blueSoft, (i % 2) * 0.15, 0.28 + Math.floor(i / 2) * 0.4, 0)
      g.add(b)
      edges(g, 0.9, 0.35, 0.7, (i % 2) * 0.15, 0.28 + Math.floor(i / 2) * 0.4, 0, 0.25)
    }
    if (o.title) addLabel(g, o.title, 1.35, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const filter = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    for (let i = 0; i < 4; i++) {
      g.add(box(1.5, 0.08, 0.95, i % 2 ? CLAY.blueSoft : CLAY.process, 0, 0.25 + i * 0.35, 0))
    }
    addLabel(g, o.title ?? 'Quality filter', 1.8, CLAY.cream, CLAY.ink, 1.55)
    return finish(g)
  }

  const gauge = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.3, 0.18, 0.85, CLAY.ink, 0, 0.1, 0))
    const dial = cyl(0.5, 0.5, 0.08, CLAY.cream, 20, 0, 0.3, 0.1)
    dial.rotation.x = Math.PI / 2
    g.add(dial)
    const needle = box(0.42, 0.03, 0.03, CLAY.danger, 0.18, 0.35, 0.45)
    needle.rotation.z = 0.5
    g.add(needle)
    if (o.title) addLabel(g, o.title, 0.85, CLAY.cream, CLAY.ink, 1.35)
    return finish(g)
  }

  const shield = (o: { x: number; y: number; z?: number; title?: string }) => {
    const shape = new THREE.Shape()
    shape.moveTo(0, 0.7)
    shape.lineTo(0.55, 0.45)
    shape.lineTo(0.42, -0.25)
    shape.lineTo(0, -0.7)
    shape.lineTo(-0.42, -0.25)
    shape.lineTo(-0.55, 0.45)
    shape.closePath()
    const geo = new THREE.ExtrudeGeometry(shape, { depth: 0.12, bevelEnabled: true, bevelSize: 0.04, bevelThickness: 0.04, bevelSegments: 1 })
    const mesh = new THREE.Mesh(geo, mat(CLAY.green))
    mesh.castShadow = true
    const g = new THREE.Group()
    g.position.set(o.x, o.y, o.z ?? 0)
    g.add(mesh)
    addLabel(g, o.title ?? 'Release ready', 0.95, CLAY.cream, CLAY.ink, 1.6)
    return finish(g)
  }

  const testTube = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(cyl(0.25, 0.25, 1.0, CLAY.blueSoft, 16, 0, 0.6, 0, true))
    g.add(cyl(0.18, 0.18, 0.6, CLAY.green, 16, 0, 0.42, 0))
    g.add(cyl(0.28, 0.28, 0.08, CLAY.ink, 16, 0, 0.05, 0))
    addLabel(g, o.title ?? 'pytest ✓', 1.25, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  const robot = (o: { x: number; y?: number; z?: number; title?: string }) => {
    const g = new THREE.Group()
    g.position.set(o.x, o.y ?? -2.85, o.z ?? 0)
    g.userData.noBob = true
    g.add(box(1.0, 0.55, 0.9, CLAY.inkSoft, 0, 0.28, 0))
    g.add(cyl(0.12, 0.12, 0.8, CLAY.output, 8, 0.1, 0.95, 0))
    const arm = box(0.75, 0.12, 0.12, CLAY.output, 0.42, 1.28, 0)
    arm.rotation.z = -0.35
    g.add(arm)
    g.add(box(0.18, 0.18, 0.18, CLAY.process, 0.75, 1.1, 0))
    addLabel(g, o.title ?? 'Robot map', 1.8, CLAY.cream, CLAY.ink, 1.4)
    return finish(g)
  }

  return {
    server,
    disk,
    block,
    file,
    factory,
    hive,
    grid,
    tower,
    funnel,
    truck,
    chip,
    prism,
    dashboard,
    folder,
    book,
    container,
    filter,
    gauge,
    shield,
    testTube,
    robot,
    beam,
    label,
  }
}
