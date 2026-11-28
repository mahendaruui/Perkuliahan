/* 2D Flowchart & Data Architecture scenes for Big Data stories (rendered by flowchart-kit.ts). */

import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'
import type { StoryVariant } from './bigdata-story'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* 1. Foundation & Arsitektur (9 steps)                                */
/* ------------------------------------------------------------------ */

const foundation: IsoScene[] = [
  // 1. Batas satu server
  {
    nodes: [
      { id: 'src', type: 'io', x: -1.8, y: 0, label: 'Data Masuk', sub: 'app + log + IoT', color: P.raw },
      { id: 'srv', type: 'process', x: 0, y: 0, label: 'Server Tunggal', sub: 'disk · RAM · I/O', color: P.process },
      { id: 'err', type: 'end', x: 1.8, y: 0, label: 'Macet / Penuh', sub: 'single bottleneck', status: 'failed' },
    ],
    links: [
      { from: 'src', to: 'srv', color: P.processDark, packets: 2, label: 'volume ↑' },
      { from: 'srv', to: 'err', color: P.dangerDark, dashed: true, packets: 2, label: 'limit I/O' },
    ],
  },
  // 2. Scale-up vs Scale-out
  {
    nodes: [
      { id: 'q', type: 'decision', x: 0, y: -1.1, label: 'Pilih Skala?', color: P.goldSoft },
      { id: 'up', type: 'process', x: -1.4, y: 0.35, label: 'Scale-Up', sub: '1 mesin raksasa', color: P.raw },
      { id: 'out', type: 'process', x: 1.4, y: 0.35, label: 'Scale-Out', sub: 'cluster banyak node', color: P.green },
      { id: 'n1', type: 'end', x: 0.7, y: 1.4, label: 'Node 1–N Aktif', color: P.green },
      { id: 'spof', type: 'end', x: -1.4, y: 1.4, label: 'SPOF & Mahal', status: 'failed' },
    ],
    links: [
      { from: 'q', to: 'up', color: P.rawDark, dashed: true, packets: 1, label: 'vertikal' },
      { from: 'q', to: 'out', color: P.greenDark, packets: 2, label: 'horizontal' },
      { from: 'up', to: 'spof', color: P.dangerDark, dashed: true, packets: 1 },
      { from: 'out', to: 'n1', color: P.greenDark, packets: 2 },
    ],
  },
  // 3. Blok penyimpanan 128 MB
  {
    nodes: [
      { id: 'file', type: 'io', x: -1.7, y: 0, label: 'File Besar 1 TB', sub: 'log mentah', color: P.raw },
      { id: 'split', type: 'process', x: 0, y: 0, label: 'Pecah Blok', sub: '128 MB / blok', color: P.process },
      { id: 'b1', type: 'codebox', x: 1.65, y: -0.85, label: 'Blok S1 (128 MB)', color: P.output },
      { id: 'b2', type: 'codebox', x: 1.65, y: 0, label: 'Blok S2 (128 MB)', color: P.output },
      { id: 'b3', type: 'codebox', x: 1.65, y: 0.85, label: 'Blok S3 (128 MB)', color: P.output },
    ],
    links: [
      { from: 'file', to: 'split', color: P.processDark, packets: 2 },
      { from: 'split', to: 'b1', color: P.outputDark, packets: 1 },
      { from: 'split', to: 'b2', color: P.outputDark, packets: 1 },
      { from: 'split', to: 'b3', color: P.outputDark, packets: 1 },
    ],
  },
  // 4. Distribusi & Metadata
  {
    nodes: [
      { id: 'meta', type: 'codebox', x: 0, y: -1.05, label: 'Metadata Service', sub: 'peta lokasi blok', color: P.violet },
      { id: 'na', type: 'process', x: -1.55, y: 0.45, label: 'Node A', sub: 'simpan [Blok 1]', color: P.process },
      { id: 'nb', type: 'process', x: 0, y: 0.45, label: 'Node B', sub: 'simpan [Blok 2]', color: P.process },
      { id: 'nc', type: 'process', x: 1.55, y: 0.45, label: 'Node C', sub: 'simpan [Blok 3]', color: P.process },
    ],
    links: [
      { from: 'meta', to: 'na', color: P.processDark, dashed: true, packets: 1, label: 'lacak' },
      { from: 'meta', to: 'nb', color: P.processDark, dashed: true, packets: 1 },
      { from: 'meta', to: 'nc', color: P.processDark, dashed: true, packets: 1 },
    ],
  },
  // 5. Replikasi factor 3
  {
    nodes: [
      { id: 'src', type: 'io', x: -1.8, y: 0, label: 'Blok Primer S1', sub: 'replication = 3', color: P.violet },
      { id: 'na', type: 'process', x: 0, y: -0.9, label: 'Node A (Aktif)', sub: 'salinan #1', color: P.green },
      { id: 'nb', type: 'end', x: 0, y: 0, label: 'Node B (Mati)', sub: 'gagal hardware', status: 'failed' },
      { id: 'nc', type: 'process', x: 0, y: 0.9, label: 'Node C (Aktif)', sub: 'salinan #3', color: P.green },
      { id: 'ok', type: 'end', x: 1.85, y: 0, label: 'Data Tetap Aman', color: P.green },
    ],
    links: [
      { from: 'src', to: 'na', color: P.greenDark, packets: 1 },
      { from: 'src', to: 'nb', color: P.dangerDark, dashed: true, packets: 1 },
      { from: 'src', to: 'nc', color: P.greenDark, packets: 1 },
      { from: 'na', to: 'ok', color: P.greenDark, packets: 2 },
      { from: 'nc', to: 'ok', color: P.greenDark, packets: 2 },
    ],
  },
  // 6. HDFS NameNode & DataNode
  {
    nodes: [
      { id: 'cli', type: 'start', x: -1.65, y: -0.7, label: 'Client App', color: P.goldSoft },
      { id: 'nn', type: 'codebox', x: 0.35, y: -0.7, label: 'NameNode', sub: 'metadata · peta blok', color: P.violet },
      { id: 'dn1', type: 'process', x: -1.4, y: 0.7, label: 'DataNode 1', sub: 'blok fisik A', color: P.process },
      { id: 'dn2', type: 'process', x: 0.35, y: 0.7, label: 'DataNode 2', sub: 'blok fisik B', color: P.process },
      { id: 'dn3', type: 'process', x: 2.0, y: 0.7, label: 'DataNode 3', sub: 'blok fisik C', color: P.process },
    ],
    links: [
      { from: 'cli', to: 'nn', color: P.processDark, dashed: true, packets: 1, label: '1. tanya lokasi' },
      { from: 'cli', to: 'dn1', color: P.greenDark, packets: 2, label: '2. baca blok' },
      { from: 'nn', to: 'dn2', color: P.rawDark, dashed: true, packets: 1, label: 'heartbeat' },
      { from: 'nn', to: 'dn3', color: P.rawDark, dashed: true, packets: 1 },
    ],
  },
  // 7. CAP Theorem trade-off
  {
    nodes: [
      { id: 'part', type: 'decision', x: 0, y: -1.0, label: 'Network Partition?', sub: 'jaringan terbelah', color: P.redSoft, status: 'failed' },
      { id: 'cp', type: 'process', x: -1.35, y: 0.45, label: 'Pilih CP (Consistent)', sub: 'tolak tulis sementara', color: P.process },
      { id: 'ap', type: 'process', x: 1.35, y: 0.45, label: 'Pilih AP (Available)', sub: 'layani baca terbaru', color: P.output },
    ],
    links: [
      { from: 'part', to: 'cp', color: P.processDark, packets: 1, label: 'jaga data sama' },
      { from: 'part', to: 'ap', color: P.outputDark, packets: 1, label: 'tetap merespons' },
    ],
  },
  // 8. Object storage & data lake
  {
    nodes: [
      { id: 'obj1', type: 'io', x: -1.65, y: -0.55, label: 'File JSON / Log', color: P.raw },
      { id: 'obj2', type: 'io', x: -1.65, y: 0.55, label: 'Tabel Parquet', color: P.raw },
      { id: 'bkt', type: 'process', x: 0, y: 0, label: 'Object Bucket', sub: 'elastis + tahan lama', color: P.output },
      { id: 'lake', type: 'end', x: 1.75, y: 0, label: 'Data Lake Cloud', sub: 'hemat biaya arsip', color: P.blueSoft },
    ],
    links: [
      { from: 'obj1', to: 'bkt', color: P.outputDark, packets: 1 },
      { from: 'obj2', to: 'bkt', color: P.outputDark, packets: 1 },
      { from: 'bkt', to: 'lake', color: P.processDark, packets: 2, label: 'put / get API' },
    ],
  },
  // 9. Rekap arsitektur data end-to-end
  {
    nodes: [
      { id: 's', type: 'start', x: -2.0, y: -0.55, label: '1. Sumber', sub: 'DB · IoT · App', color: P.raw },
      { id: 'i', type: 'io', x: -0.35, y: -0.55, label: '2. Ingestion', sub: 'batch / stream', color: P.blueSoft },
      { id: 'st', type: 'process', x: 1.35, y: -0.55, label: '3. Storage', sub: 'HDFS / Lake', color: P.process },
      { id: 'c', type: 'process', x: -0.35, y: 0.7, label: '4. Compute', sub: 'Spark / Engine', color: P.violet },
      { id: 'sv', type: 'end', x: 1.35, y: 0.7, label: '5. Serving', sub: 'BI · ML · API', color: P.green },
    ],
    links: [
      { from: 's', to: 'i', color: P.rawDark, packets: 2 },
      { from: 'i', to: 'st', color: P.processDark, packets: 2 },
      { from: 'st', to: 'c', color: P.processDark, packets: 2 },
      { from: 'c', to: 'sv', color: P.greenDark, packets: 2, label: 'insight' },
    ],
  },
]

/* ------------------------------------------------------------------ */
/* 2. Hadoop, MapReduce, YARN & Hive (12 steps)                        */
/* ------------------------------------------------------------------ */

const hadoop: IsoScene[] = [
  // 1. Masalah file 1 TB di satu server
  {
    nodes: [
      { id: 'f', type: 'io', x: -1.7, y: 0, label: '1 TB Event Log', sub: '1 file raksasa', color: P.raw },
      { id: 'srv', type: 'process', x: 0, y: 0, label: 'Server Tunggal', sub: 'disk penuh + crash', color: P.redSoft, status: 'failed' },
      { id: 'fail', type: 'end', x: 1.75, y: 0, label: 'Job Berhenti Total', status: 'failed' },
    ],
    links: [
      { from: 'f', to: 'srv', color: P.dangerDark, packets: 2, label: 'I/O jenuh' },
      { from: 'srv', to: 'fail', color: P.dangerDark, dashed: true, packets: 2 },
    ],
  },
  // 2. Ekosistem Hadoop (5 komponen)
  {
    nodes: [
      { id: 'hdfs', type: 'process', x: -1.5, y: 0.65, label: 'HDFS', sub: 'simpan terdistribusi', color: P.process },
      { id: 'yarn', type: 'process', x: 0, y: 0.65, label: 'YARN', sub: 'bagi CPU & RAM', color: P.violet },
      { id: 'mr', type: 'process', x: 1.5, y: 0.65, label: 'MapReduce', sub: 'komputasi paralel', color: P.green },
      { id: 'hive', type: 'codebox', x: -0.85, y: -0.65, label: 'Hive (SQL Engine)', sub: 'query deklaratif', color: P.output },
      { id: 'hb', type: 'codebox', x: 0.95, y: -0.65, label: 'HBase (NoSQL)', sub: 'akses acak real-time', color: P.blueSoft },
    ],
    links: [
      { from: 'hive', to: 'mr', color: P.outputDark, dashed: true, packets: 1 },
      { from: 'hive', to: 'yarn', color: P.ink2, dashed: true, packets: 1 },
      { from: 'hb', to: 'hdfs', color: P.processDark, dashed: true, packets: 1 },
      { from: 'yarn', to: 'mr', color: P.processDark, packets: 1 },
    ],
  },
  // 3. Move compute to data
  {
    nodes: [
      { id: 'job', type: 'codebox', x: -1.55, y: -0.45, label: 'Kode Program', sub: 'hanya beberapa KB', color: P.green },
      { id: 'node', type: 'process', x: 0.95, y: -0.45, label: 'Node A (Data Lokal)', sub: 'menyimpan 1 TB blok', color: P.process },
      { id: 'bad', type: 'end', x: 0.95, y: 0.75, label: 'Hindari Tarik 1 TB lewat Jaringan', status: 'failed' },
    ],
    links: [
      { from: 'job', to: 'node', color: P.greenDark, packets: 2, label: 'kirim kode kecil' },
      { from: 'node', to: 'bad', color: P.dangerDark, dashed: true, packets: 1, label: 'mahal!' },
    ],
  },
  // 4. Input Split
  {
    nodes: [
      { id: 'f', type: 'io', x: -1.7, y: 0, label: 'File 1 TB (HDFS)', color: P.raw },
      { id: 'sp', type: 'process', x: -0.1, y: 0, label: 'InputSplit', sub: '128 MB / unit', color: P.output },
      { id: 's1', type: 'codebox', x: 1.65, y: -0.8, label: 'Split 1 → Map 1', color: P.process },
      { id: 's2', type: 'codebox', x: 1.65, y: 0, label: 'Split 2 → Map 2', color: P.process },
      { id: 's3', type: 'codebox', x: 1.65, y: 0.8, label: 'Split 3 → Map 3', color: P.process },
    ],
    links: [
      { from: 'f', to: 'sp', color: P.ink2, packets: 2 },
      { from: 'sp', to: 's1', color: P.processDark, packets: 1 },
      { from: 'sp', to: 's2', color: P.processDark, packets: 1 },
      { from: 'sp', to: 's3', color: P.processDark, packets: 1 },
    ],
  },
  // 5. Fase Map
  {
    nodes: [
      { id: 's1', type: 'io', x: -1.6, y: -0.65, label: 'Split 1: "Aceh Bandung"', color: P.raw },
      { id: 's2', type: 'io', x: -1.6, y: 0.65, label: 'Split 2: "Aceh Medan"', color: P.raw },
      { id: 'm1', type: 'process', x: 0.1, y: -0.65, label: 'Mapper 1', sub: 'independen', color: P.process },
      { id: 'm2', type: 'process', x: 0.1, y: 0.65, label: 'Mapper 2', sub: 'independen', color: P.process },
      { id: 'o1', type: 'codebox', x: 1.7, y: -0.65, label: '(Aceh,1), (Bandung,1)', color: P.output },
      { id: 'o2', type: 'codebox', x: 1.7, y: 0.65, label: '(Aceh,1), (Medan,1)', color: P.output },
    ],
    links: [
      { from: 's1', to: 'm1', color: P.processDark, packets: 2 },
      { from: 's2', to: 'm2', color: P.processDark, packets: 2 },
      { from: 'm1', to: 'o1', color: P.outputDark, packets: 1 },
      { from: 'm2', to: 'o2', color: P.outputDark, packets: 1 },
    ],
  },
  // 6. Combiner (mini-reduce lokal)
  {
    nodes: [
      { id: 'raw', type: 'io', x: -1.75, y: 0, label: '1.000.000x', sub: '(kota, 1)', color: P.raw },
      { id: 'dec', type: 'decision', x: -0.15, y: 0, label: 'Asosiatif?', color: P.goldSoft },
      { id: 'cmb', type: 'process', x: 1.4, y: -0.55, label: 'Combiner Lokal', sub: 'padat di sisi map', color: P.violet },
      { id: 'out', type: 'end', x: 1.4, y: 0.65, label: '1.000x (kota, 1000)', sub: 'hemat jaringan!', color: P.green },
    ],
    links: [
      { from: 'raw', to: 'dec', color: P.ink2, packets: 2 },
      { from: 'dec', to: 'cmb', color: P.processDark, packets: 2, label: 'Ya' },
      { from: 'cmb', to: 'out', color: P.greenDark, packets: 2, label: 'mini-reduce' },
    ],
  },
  // 7. Shuffle & Sort
  {
    nodes: [
      { id: 'm1', type: 'process', x: -1.65, y: -0.65, label: 'Mapper 1', color: P.process },
      { id: 'm2', type: 'process', x: -1.65, y: 0.65, label: 'Mapper 2', color: P.process },
      { id: 'pt', type: 'codebox', x: 0, y: 0, label: 'Shuffle & Sort', sub: 'hash(key) lintas node', color: P.redSoft, status: 'failed' },
      { id: 'r1', type: 'process', x: 1.65, y: -0.65, label: 'Reducer 1', color: P.output },
      { id: 'r2', type: 'process', x: 1.65, y: 0.65, label: 'Reducer 2', color: P.output },
    ],
    links: [
      { from: 'm1', to: 'pt', color: P.dangerDark, dashed: true, packets: 2 },
      { from: 'm2', to: 'pt', color: P.dangerDark, dashed: true, packets: 2 },
      { from: 'pt', to: 'r1', color: P.dangerDark, dashed: true, packets: 2, label: 'bottleneck I/O' },
      { from: 'pt', to: 'r2', color: P.dangerDark, dashed: true, packets: 2 },
    ],
  },
  // 8. Reduce & Output HDFS
  {
    nodes: [
      { id: 'grp', type: 'io', x: -1.7, y: 0, label: 'Group By Key', sub: 'Aceh: [1, 1, 1]', color: P.violet },
      { id: 'red', type: 'process', x: -0.05, y: 0, label: 'Reducer', sub: 'jumlah & agregasi', color: P.output },
      { id: 'hdfs', type: 'end', x: 1.7, y: 0, label: 'Output HDFS (3x)', sub: 'part-r-00000', color: P.green },
    ],
    links: [
      { from: 'grp', to: 'red', color: P.outputDark, packets: 2 },
      { from: 'red', to: 'hdfs', color: P.greenDark, packets: 2, label: 'replikasi 3' },
    ],
  },
  // 9. Data Skew & Salting
  {
    nodes: [
      { id: 'sk', type: 'decision', x: -1.55, y: 0, label: '80% "Jakarta"?', status: 'failed', color: P.redSoft },
      { id: 'bad', type: 'end', x: 0.3, y: -0.7, label: 'Macet di 99%', sub: '1 reducer overload', status: 'failed' },
      { id: 'slt', type: 'process', x: 0.3, y: 0.7, label: 'Terapkan Salting', sub: 'Jakarta-0 … Jakarta-9', color: P.green },
      { id: 'ok', type: 'end', x: 1.9, y: 0.7, label: 'Beban Merata', color: P.green },
    ],
    links: [
      { from: 'sk', to: 'bad', color: P.dangerDark, dashed: true, packets: 2, label: 'tanpa salt' },
      { from: 'sk', to: 'slt', color: P.greenDark, packets: 2, label: 'solusi' },
      { from: 'slt', to: 'ok', color: P.greenDark, packets: 2 },
    ],
  },
  // 10. Arsitektur YARN
  {
    nodes: [
      { id: 'rm', type: 'codebox', x: 0, y: -1.0, label: 'ResourceManager', sub: 'scheduler global CPU/RAM', color: P.process },
      { id: 'nm1', type: 'process', x: -1.35, y: 0.4, label: 'NodeManager 1', sub: 'Container + AppMaster', color: P.output },
      { id: 'nm2', type: 'process', x: 1.35, y: 0.4, label: 'NodeManager 2', sub: 'Container Task A & B', color: P.blueSoft },
    ],
    links: [
      { from: 'rm', to: 'nm1', color: P.processDark, packets: 2, label: 'alokasi container' },
      { from: 'rm', to: 'nm2', color: P.processDark, packets: 2, label: 'pantau resource' },
      { from: 'nm1', to: 'nm2', color: P.ink2, dashed: true, packets: 1, label: 'koordinasi AM' },
    ],
  },
  // 11. Hive Metastore & Partisi
  {
    nodes: [
      { id: 'sql', type: 'io', x: -1.75, y: -0.45, label: 'SQL SELECT', sub: "WHERE dt='09-02'", color: P.output },
      { id: 'ms', type: 'codebox', x: 0, y: -0.45, label: 'Hive Metastore', sub: 'katalog skema + partisi', color: P.violet },
      { id: 'd1', type: 'end', x: -0.8, y: 0.75, label: 'dt=09-01 (Lewati)', color: P.raw },
      { id: 'd2', type: 'end', x: 1.25, y: 0.75, label: 'dt=09-02 (Baca!)', color: P.green },
    ],
    links: [
      { from: 'sql', to: 'ms', color: P.processDark, packets: 2 },
      { from: 'ms', to: 'd1', color: P.rawDark, dashed: true, packets: 1, label: 'prune' },
      { from: 'ms', to: 'd2', color: P.greenDark, packets: 2, label: 'partition pruning' },
    ],
  },
  // 12. Format Kolumnar & Hasil Analitik
  {
    nodes: [
      { id: 'col', type: 'io', x: -1.7, y: 0, label: 'Parquet / ORC', sub: 'format kolumnar', color: P.output },
      { id: 'cbo', type: 'process', x: 0, y: 0, label: 'Column Pruning + CBO', sub: 'hindari SELECT *', color: P.process },
      { id: 'bi', type: 'end', x: 1.75, y: 0, label: 'Query Cepat → BI', color: P.green },
    ],
    links: [
      { from: 'col', to: 'cbo', color: P.outputDark, packets: 2 },
      { from: 'cbo', to: 'bi', color: P.greenDark, packets: 2, label: 'baca kolom perlu' },
    ],
  },
]

/* ------------------------------------------------------------------ */
/* 3. Apache Spark & Optimasi ETL (11 steps)                           */
/* ------------------------------------------------------------------ */

const spark: IsoScene[] = [
  // 1. Masalah I/O MapReduce
  {
    nodes: [
      { id: 'f1', type: 'process', x: -1.65, y: 0, label: 'MapReduce Fase 1', color: P.process },
      { id: 'hdfs', type: 'codebox', x: 0, y: 0, label: 'Tulis & Baca HDFS', sub: 'disk I/O mahal', status: 'failed', color: P.redSoft },
      { id: 'f2', type: 'process', x: 1.65, y: 0, label: 'MapReduce Fase 2', color: P.process },
    ],
    links: [
      { from: 'f1', to: 'hdfs', color: P.dangerDark, dashed: true, packets: 2, label: 'tulis disk' },
      { from: 'hdfs', to: 'f2', color: P.dangerDark, dashed: true, packets: 2, label: 'baca lagi' },
    ],
  },
  // 2. Spark In-Memory & DAG
  {
    nodes: [
      { id: 'in', type: 'io', x: -1.75, y: 0, label: 'Data Masuk', color: P.raw },
      { id: 'ram', type: 'process', x: 0, y: 0, label: 'Spark In-Memory RAM', sub: 'rantai DAG tanpa spill', color: P.green },
      { id: 'out', type: 'end', x: 1.75, y: 0, label: 'Iterasi Cepat', color: P.green },
    ],
    links: [
      { from: 'in', to: 'ram', color: P.greenDark, packets: 2 },
      { from: 'ram', to: 'out', color: P.greenDark, packets: 2, label: 'cache memori' },
    ],
  },
  // 3. Arsitektur Cluster Spark
  {
    nodes: [
      { id: 'drv', type: 'codebox', x: -1.65, y: 0, label: 'Spark Driver', sub: 'SparkSession + DAG', color: P.process },
      { id: 'cm', type: 'decision', x: -0.05, y: 0, label: 'Cluster Mgr', sub: 'YARN / K8s', color: P.goldSoft },
      { id: 'e1', type: 'process', x: 1.65, y: -0.75, label: 'Executor 1 (Cache)', color: P.green },
      { id: 'e2', type: 'process', x: 1.65, y: 0, label: 'Executor 2 (Cache)', color: P.green },
      { id: 'e3', type: 'process', x: 1.65, y: 0.75, label: 'Executor 3 (Cache)', color: P.green },
    ],
    links: [
      { from: 'drv', to: 'cm', color: P.processDark, packets: 2, label: 'minta slot' },
      { from: 'cm', to: 'e1', color: P.greenDark, packets: 1 },
      { from: 'cm', to: 'e2', color: P.greenDark, packets: 1 },
      { from: 'cm', to: 'e3', color: P.greenDark, packets: 1 },
    ],
  },
  // 4. Lazy Evaluation & DAG
  {
    nodes: [
      { id: 'r', type: 'io', x: -1.85, y: 0, label: 'read()', sub: 'lazy', color: P.raw },
      { id: 'f', type: 'process', x: -0.65, y: 0, label: 'filter()', sub: 'lazy plan', color: P.blueSoft },
      { id: 'g', type: 'process', x: 0.6, y: 0, label: 'groupBy()', sub: 'lazy plan', color: P.violet },
      { id: 'act', type: 'end', x: 1.85, y: 0, label: 'show() / write()', sub: 'ACTION → eksekusi!', color: P.green },
    ],
    links: [
      { from: 'r', to: 'f', color: P.ink2, dashed: true, packets: 1 },
      { from: 'f', to: 'g', color: P.ink2, dashed: true, packets: 1 },
      { from: 'g', to: 'act', color: P.greenDark, packets: 2, label: 'nyalakan DAG' },
    ],
  },
  // 5. Catalyst Optimizer & Tungsten
  {
    nodes: [
      { id: 'an', type: 'process', x: -1.8, y: 0, label: '1. Analysis', sub: 'cek skema', color: P.raw },
      { id: 'lg', type: 'process', x: -0.6, y: 0, label: '2. Logical Plan', sub: 'pushdown + prune', color: P.blueSoft },
      { id: 'ph', type: 'process', x: 0.65, y: 0, label: '3. Physical Plan', sub: 'pilih join terbaik', color: P.violet },
      { id: 'cg', type: 'end', x: 1.85, y: 0, label: '4. Tungsten Codegen', color: P.output },
    ],
    links: [
      { from: 'an', to: 'lg', color: P.processDark, packets: 2 },
      { from: 'lg', to: 'ph', color: P.processDark, packets: 2 },
      { from: 'ph', to: 'cg', color: P.outputDark, packets: 2 },
    ],
  },
  // 6. Narrow vs Wide Transformation (Shuffle Boundary)
  {
    nodes: [
      { id: 's1', type: 'process', x: -1.55, y: -0.65, label: 'filter() / map()', sub: '1 partisi → 1 partisi', color: P.green },
      { id: 's2', type: 'end', x: 1.55, y: -0.65, label: 'Narrow (Tanpa Shuffle)', color: P.green },
      { id: 'w1', type: 'process', x: -1.55, y: 0.65, label: 'groupBy() / join()', sub: 'lintas banyak partisi', color: P.redSoft, status: 'failed' },
      { id: 'w2', type: 'end', x: 1.55, y: 0.65, label: 'Wide (Batas Stage + Shuffle)', status: 'failed' },
    ],
    links: [
      { from: 's1', to: 's2', color: P.greenDark, packets: 2, label: 'cepat (lokal)' },
      { from: 'w1', to: 'w2', color: P.dangerDark, dashed: true, packets: 2, label: 'shuffle jaringan!' },
    ],
  },
  // 7. Medallion Bronze -> Silver
  {
    nodes: [
      { id: 'br', type: 'io', x: -1.7, y: 0, label: 'Bronze Layer', sub: 'JSON mentah', color: P.raw },
      { id: 'qc', type: 'decision', x: -0.05, y: 0, label: 'Quality Check', sub: 'null · tipe · duplikat', color: P.goldSoft },
      { id: 'sv', type: 'end', x: 1.7, y: 0, label: 'Silver Parquet', sub: 'partisi dt=...', color: P.process },
    ],
    links: [
      { from: 'br', to: 'qc', color: P.ink2, packets: 2 },
      { from: 'qc', to: 'sv', color: P.processDark, packets: 2, label: 'bersih & tervalidasi' },
    ],
  },
  // 8. Silver -> Gold & Broadcast Join
  {
    nodes: [
      { id: 'dim', type: 'io', x: -1.55, y: -0.65, label: 'Tabel Produk Kecil', color: P.output },
      { id: 'bc', type: 'codebox', x: 0.1, y: -0.65, label: 'Broadcast Join', sub: 'salin ke semua executor', color: P.green },
      { id: 'sv', type: 'process', x: -1.55, y: 0.65, label: 'Data Silver Besar', color: P.process },
      { id: 'gd', type: 'end', x: 1.65, y: 0, label: 'Gold Table', sub: 'revenue · KPI bisnis', color: P.output },
    ],
    links: [
      { from: 'dim', to: 'bc', color: P.outputDark, packets: 2 },
      { from: 'bc', to: 'gd', color: P.greenDark, packets: 2, label: 'tanpa shuffle!' },
      { from: 'sv', to: 'gd', color: P.processDark, packets: 2, label: 'agregasi' },
    ],
  },
  // 9. Tuning Partisi
  {
    nodes: [
      { id: 'raw', type: 'io', x: -1.7, y: 0, label: '200 Partisi Kecil', sub: 'task overhead tinggi', color: P.redSoft, status: 'failed' },
      { id: 'aqe', type: 'process', x: -0.05, y: 0, label: 'coalesce() / AQE', sub: 'gabung otomatis', color: P.process },
      { id: 'opt', type: 'end', x: 1.7, y: 0, label: '8 Partisi Optimal', sub: '~128 MB per partisi', color: P.green },
    ],
    links: [
      { from: 'raw', to: 'aqe', color: P.dangerDark, dashed: true, packets: 2 },
      { from: 'aqe', to: 'opt', color: P.greenDark, packets: 2, label: 'tuning ukuran' },
    ],
  },
  // 10. Skew & Compaction Small Files
  {
    nodes: [
      { id: 'sk', type: 'process', x: -1.55, y: -0.65, label: 'Partisi Skew Raksasa', status: 'failed', color: P.redSoft },
      { id: 'aq', type: 'end', x: 1.55, y: -0.65, label: 'AQE Skew Join / Salting', color: P.green },
      { id: 'sf', type: 'process', x: -1.55, y: 0.65, label: 'Jutaan File Kecil', status: 'failed', color: P.redSoft },
      { id: 'cp', type: 'end', x: 1.55, y: 0.65, label: 'Compaction 128 MB–1 GB', color: P.output },
    ],
    links: [
      { from: 'sk', to: 'aq', color: P.greenDark, packets: 2, label: 'pecah key panas' },
      { from: 'sf', to: 'cp', color: P.outputDark, packets: 2, label: 'pres file output' },
    ],
  },
  // 11. Uji, Ukur, Rilis
  {
    nodes: [
      { id: 'py', type: 'codebox', x: -1.7, y: 0, label: 'pytest Unit Test', sub: 'fungsi transformasi murni', color: P.process },
      { id: 'ci', type: 'decision', x: -0.05, y: 0, label: 'CI + Metrik Lolos?', color: P.goldSoft },
      { id: 'rel', type: 'end', x: 1.7, y: 0, label: 'Rilis Gold Produksi', sub: 'siap pantau SLA', color: P.green },
    ],
    links: [
      { from: 'py', to: 'ci', color: P.processDark, packets: 2 },
      { from: 'ci', to: 'rel', color: P.greenDark, packets: 2, label: 'terverifikasi' },
    ],
  },
]

export const storyScenes: Record<StoryVariant, IsoScene[]> = { foundation, hadoop, spark }

export function sceneFor(variant: StoryVariant, index: number): IsoScene {
  const list = storyScenes[variant]
  return list[Math.min(index, list.length - 1)] ?? { nodes: [] }
}
