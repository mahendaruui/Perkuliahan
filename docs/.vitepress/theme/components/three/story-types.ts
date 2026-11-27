/* Story model shared by every 2.5D lesson canvas. */

export type StoryTone = 'sand' | 'blue' | 'green' | 'amber' | 'violet' | 'red'

export interface StoryStep {
  id: string
  short: string
  title: string
  phase: string
  tone: StoryTone
  body: string
  idea: string
  panelTitle: string
  panelMetric: string
  nodeCount: string
  dataCount: string
  linkCount: string
  focus: string
}

export interface StoryGoal {
  text: string
  at: number
}

export interface StoryModule {
  id: string
  title: string
  color: string
  items: number[]
}

export interface StoryLegendItem {
  label: string
  color: string
}

export interface StoryMeta {
  brand: string
  /** Course label shown before the breadcrumb slash. */
  course: string
  brandSub: string
  /** Canvas URL, used by the brand link and the first step. */
  href: string
  /** Course index URL behind the "Modul" nav item. */
  moduleHref: string
  /** Optional slide URL behind the "Slide" nav item. */
  slideHref?: string
  /** Optional renderer mode: 'iso' (default 2.5D), 'flowchart' (2D ISO 5807), 'timeseries' (2D charts), or 'oop' (2D OOP UML & dispatch). */
  renderMode?: 'iso' | 'flowchart' | 'timeseries' | 'oop'
  crumb: string
  title: string
  subtitle: string
  duration: string
  level: string
  longTitle: boolean
  footnote: string
  searchHint: string
  /** Optional overrides for the four HUD chips. */
  chipLabels?: [string, string, string, string]
  /** Optional legend; defaults to the raw/process/output/danger palette. */
  legend?: StoryLegendItem[]
}

export interface Story {
  meta: StoryMeta
  steps: StoryStep[]
  goals: StoryGoal[]
  modules: StoryModule[]
}
