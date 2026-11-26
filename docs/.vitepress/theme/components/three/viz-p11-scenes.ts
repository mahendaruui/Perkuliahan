import type { IsoScene } from './iso-kit'

/* ------------------------------------------------------------------ */
/* Visualisasi Data — Minggu 11: Time Series & Finansial              */
/* ------------------------------------------------------------------ */

export const vizP11Scenes: IsoScene[] = [
  // 1. Sinyal vs Noise
  { nodes: [{ id: 'chart', type: 'ts_signal', x: 0, y: 0 }] },
  // 2. Empat Komponen Time Series
  { nodes: [{ id: 'chart', type: 'ts_components', x: 0, y: 0 }] },
  // 3. Model Aditif vs Multiplikatif
  { nodes: [{ id: 'chart', type: 'ts_models', x: 0, y: 0 }] },
  // 4. Resampling Temporal D -> W
  { nodes: [{ id: 'chart', type: 'ts_resampling', x: 0, y: 0 }] },
  // 5. Moving Average SMA 7, SMA 30 & +-1 sigma
  { nodes: [{ id: 'chart', type: 'ts_moving_avg', x: 0, y: 0 }] },
  // 6. Dekomposisi 4 Panel Statsmodels
  { nodes: [{ id: 'chart', type: 'ts_decompose', x: 0, y: 0 }] },
  // 7. Anatomi Candlestick OHLC
  { nodes: [{ id: 'chart', type: 'ts_ohlc', x: 0, y: 0 }] },
  // 8. Dashboard Candlestick + MA20 + Bollinger + Volume
  { nodes: [{ id: 'chart', type: 'ts_candlestick_vol', x: 0, y: 0 }] },
]
