import type { IsoScene } from './iso-kit'
import { PALETTE } from './iso-kit'
import type { StoryVariant } from './bigdata-story'

const P = PALETTE

/* ------------------------------------------------------------------ */
/* Foundation & Arsitektur                                             */
/* ------------------------------------------------------------------ */

const foundation: IsoScene[] = [
  {
    nodes: [
      { id: 'src', type: 'source', x: -2.8, y: 1.4, label: 'DATA MASUK', color: P.raw },
      { id: 'srv', type: 'server', x: 0.2, y: -0.2, label: 'SERVER 01', status: 'smoke', scale: 1.05 },
      { id: 'b1', type: 'block', x: 1.4, y: 0.6, color: P.raw, scale: 0.8 },
      { id: 'b2', type: 'block', x: 1.9, y: 0.2, color: P.violet, scale: 0.7 },
      { id: 'b3', type: 'block', x: 0.9, y: 1.1, color: P.process, scale: 0.7 },
      { id: 'b4', type: 'block', x: 2.2, y: 0.8, color: P.output, scale: 0.66 },
      { id: 'b5', type: 'block', x: 2.6, y: 1.1, color: P.raw, scale: 0.6 },
      { id: 'b6', type: 'block', x: 2.9, y: 0.6, color: P.process, scale: 0.56 },
      { id: 'b7', type: 'block', x: 2.4, y: 1.5, color: P.violet, scale: 0.5 },
      { id: 'b8', type: 'block', x: 3.1, y: 1.0, color: P.raw, scale: 0.46 },
    ],
    links: [
      { from: 'src', to: 'srv', label: '1 TB', color: P.danger, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'up', type: 'tower', x: -2.4, y: 1.0, label: 'Scale-up', color: P.process },
      { id: 'n1', type: 'server', x: 0.6, y: -0.2, label: 'Node 1', color: P.greenDark, status: 'active' },
      { id: 'n2', type: 'server', x: 1.6, y: -0.8, label: 'Node 2', color: P.greenDark },
      { id: 'n3', type: 'server', x: 2.6, y: -1.4, label: 'Node 3', color: P.greenDark },
    ],
    links: [
      { from: 'n1', to: 'n2', color: P.greenDark, packets: 1, dashed: true },
      { from: 'n2', to: 'n3', color: P.greenDark, packets: 1, dashed: true },
    ],
  },
  {
    nodes: [
      { id: 'file', type: 'file', x: -2.8, y: 1.2, label: 'FILE 1 TB', color: P.raw, scale: 1.1 },
      { id: 'wall', type: 'wall', x: -1.4, y: 0.6, label: 'laser split' },
      { id: 's1', type: 'block', x: 0.2, y: 0.4, color: P.raw, label: 'S1' },
      { id: 's2', type: 'block', x: 1.0, y: 0.0, color: P.raw, label: 'S2' },
      { id: 's3', type: 'block', x: 1.8, y: -0.4, color: P.raw, label: 'S3' },
      { id: 's4', type: 'block', x: 2.6, y: -0.8, color: P.raw, label: 'S4' },
    ],
    links: [
      { from: 'file', to: 's1', color: P.ink2, dashed: true, packets: 1, label: '128 MB' },
      { from: 'file', to: 's2', color: P.ink2, dashed: true, packets: 1 },
      { from: 'file', to: 's3', color: P.ink2, dashed: true, packets: 1 },
      { from: 'file', to: 's4', color: P.ink2, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'meta', type: 'book', x: -2.6, y: 1.2, label: 'Metadata' },
      { id: 'na', type: 'server', x: 0.2, y: 0.2, label: 'Node A', color: P.process },
      { id: 'nb', type: 'server', x: 1.4, y: -0.4, label: 'Node B', color: P.process },
      { id: 'nc', type: 'server', x: 2.6, y: -1.0, label: 'Node C', color: P.process },
      { id: 'ba', type: 'block', x: 0.2, y: 0.9, color: P.raw, label: 'blok' },
      { id: 'bb', type: 'block', x: 1.4, y: 0.3, color: P.raw, label: 'blok' },
      { id: 'bc', type: 'block', x: 2.6, y: -0.3, color: P.raw, label: 'blok' },
    ],
    links: [
      { from: 'meta', to: 'na', color: P.process, dashed: true, packets: 1 },
      { from: 'meta', to: 'nb', color: P.process, dashed: true, packets: 1 },
      { from: 'meta', to: 'nc', color: P.process, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'na', type: 'server', x: -0.4, y: 0.8, label: 'Node A', color: P.process },
      { id: 'nb', type: 'server', x: 1.0, y: 0.0, label: 'Node B', color: P.process },
      { id: 'nc', type: 'server', x: 2.4, y: -0.8, label: 'Node C', color: P.process },
      { id: 'ba', type: 'block', x: -0.4, y: 1.7, color: P.violet },
      { id: 'bb', type: 'block', x: 1.0, y: 0.9, color: P.violet },
      { id: 'bc', type: 'block', x: 2.4, y: 0.1, color: P.violet },
    ],
    links: [
      { from: 'na', to: 'nb', color: P.greenDark, dashed: true, packets: 1, label: 'replica', lift: 54 },
      { from: 'nb', to: 'nc', color: P.greenDark, dashed: true, packets: 1 },
      { from: 'ba', to: 'bb', color: P.output, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'nn', type: 'book', x: -2.6, y: 1.2, label: 'NameNode' },
      { id: 'd1', type: 'server', x: 0.2, y: 0.2, label: 'DataNode 1', color: P.process },
      { id: 'd2', type: 'server', x: 1.4, y: -0.4, label: 'DataNode 2', color: P.process },
      { id: 'd3', type: 'server', x: 2.6, y: -1.0, label: 'DataNode 3', color: P.process },
      { id: 'b1', type: 'block', x: 0.2, y: 0.9, color: P.raw },
      { id: 'b2', type: 'block', x: 1.4, y: 0.3, color: P.raw },
      { id: 'b3', type: 'block', x: 2.6, y: -0.3, color: P.raw },
    ],
    links: [
      { from: 'nn', to: 'd1', color: P.process, dashed: true, packets: 1, label: 'peta blok' },
      { from: 'nn', to: 'd2', color: P.process, dashed: true, packets: 1 },
      { from: 'nn', to: 'd3', color: P.process, dashed: true, packets: 1 },
      { from: 'd1', to: 'b1', color: P.ink2, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'c', type: 'server', x: -2.2, y: 0.9, label: 'Consistency', color: P.process },
      { id: 'a', type: 'server', x: 2.2, y: -0.9, label: 'Availability', color: P.output },
      { id: 'wall', type: 'wall', x: 0, y: 0, label: 'network partition' },
      { id: 'bc', type: 'block', x: -2.2, y: 1.8, color: P.raw, label: 'C' },
      { id: 'ba', type: 'block', x: 2.2, y: 0, color: P.raw, label: 'A' },
    ],
    links: [
      { from: 'c', to: 'a', color: P.danger, dashed: true, packets: 1, label: 'salinan tertunda', lift: 80 },
      { from: 'bc', to: 'ba', color: P.rawDark, dashed: true, packets: 1, lift: 110 },
    ],
  },
  {
    nodes: [
      { id: 'bucket', type: 'bucket', x: -1.6, y: 0.8, label: 'Bucket', color: P.output },
      { id: 'f1', type: 'folder', x: -2.9, y: 1.7, label: 'objek' },
      { id: 'f2', type: 'folder', x: -2.1, y: 2.3, label: 'objek' },
      { id: 'lake', type: 'dashboard', x: 2.0, y: -0.8, label: 'Data lake' },
    ],
    links: [
      { from: 'f1', to: 'bucket', color: P.output, packets: 1 },
      { from: 'f2', to: 'bucket', color: P.output, packets: 1 },
      { from: 'bucket', to: 'lake', color: P.output, packets: 2, label: 'data lake' },
    ],
  },
  {
    nodes: [
      { id: 'src', type: 'source', x: -2.8, y: 1.4, label: 'Sumber', color: P.raw },
      { id: 'ing', type: 'funnel', x: -1.5, y: 0.7, label: 'Ingestion', color: P.process },
      { id: 'sto', type: 'disk', x: -0.2, y: 0.0, label: 'Storage', color: P.process },
      { id: 'com', type: 'factory', x: 1.1, y: -0.7, label: 'Compute', color: P.process, scale: 0.9 },
      { id: 'srv', type: 'dashboard', x: 3.1, y: -2.0, label: 'Serving' },
    ],
    links: [
      { from: 'src', to: 'ing', color: P.rawDark, packets: 2 },
      { from: 'ing', to: 'sto', color: P.process, packets: 2 },
      { from: 'sto', to: 'com', color: P.process, packets: 2 },
      { from: 'com', to: 'srv', color: P.output, packets: 2, label: 'insight' },
    ],
  },
]

/* ------------------------------------------------------------------ */
/* Hadoop, MapReduce, YARN & Hive                                      */
/* ------------------------------------------------------------------ */

const hadoop: IsoScene[] = [
  {
    nodes: [
      { id: 'file', type: 'file', x: -2.6, y: 1.2, label: '1 TB event', color: P.raw, scale: 1.2 },
      { id: 'srv', type: 'server', x: 0.2, y: -0.2, label: 'SERVER 01', status: 'smoke', scale: 1.05 },
      { id: 'b1', type: 'block', x: 1.3, y: 0.6, color: P.raw, scale: 0.8 },
      { id: 'b2', type: 'block', x: 1.8, y: 0.2, color: P.process, scale: 0.72 },
      { id: 'b3', type: 'block', x: 0.9, y: 1.1, color: P.violet, scale: 0.72 },
      { id: 'b4', type: 'block', x: 2.1, y: 0.8, color: P.output, scale: 0.68 },
      { id: 'b5', type: 'block', x: 2.5, y: 1.1, color: P.raw, scale: 0.62 },
      { id: 'b6', type: 'block', x: 2.9, y: 0.6, color: P.process, scale: 0.56 },
      { id: 'b7', type: 'block', x: 2.6, y: 1.5, color: P.violet, scale: 0.5 },
    ],
    links: [
      { from: 'file', to: 'srv', label: '1 TB', color: P.danger, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'hdfs', type: 'disk', x: -2.6, y: 1.2, label: 'HDFS', color: P.process },
      { id: 'yarn', type: 'tower', x: -1.3, y: 0.6, label: 'YARN', color: P.process },
      { id: 'mr', type: 'factory', x: 0, y: 0, label: 'MapReduce', color: P.process },
      { id: 'hive', type: 'hive', x: 1.3, y: -0.6, label: 'Hive', color: P.output },
      { id: 'hbase', type: 'grid', x: 2.6, y: -1.2, label: 'HBase', color: P.violet },
    ],
  },
  {
    nodes: [
      { id: 'job', type: 'file', x: -2.6, y: 1.2, label: 'JOB (kode)', color: P.process, scale: 0.95 },
      { id: 'na', type: 'server', x: 0.4, y: 0.0, label: 'NODE A', color: P.process, status: 'active' },
      { id: 'nb', type: 'server', x: 1.8, y: -0.8, label: 'NODE B', color: P.process },
      { id: 'd1', type: 'block', x: 0.4, y: 0.9, color: P.raw, label: 'blok' },
      { id: 'd2', type: 'block', x: 1.8, y: 0.1, color: P.raw },
    ],
    links: [
      { from: 'job', to: 'na', color: P.process, packets: 2, label: 'kode kecil' },
    ],
  },
  {
    nodes: [
      { id: 'file', type: 'file', x: -2.8, y: 1.2, label: 'FILE 1 TB', color: P.raw, scale: 1.15 },
      { id: 'wall', type: 'wall', x: -1.4, y: 0.6, label: 'laser split' },
      { id: 's1', type: 'block', x: 0.2, y: 0.4, color: P.raw, label: 'S1' },
      { id: 's2', type: 'block', x: 1.0, y: 0.0, color: P.raw, label: 'S2' },
      { id: 's3', type: 'block', x: 1.8, y: -0.4, color: P.raw, label: 'S3' },
      { id: 's4', type: 'block', x: 2.6, y: -0.8, color: P.raw, label: 'S4' },
    ],
    links: [
      { from: 'file', to: 's1', color: P.ink2, dashed: true, packets: 1, label: '128 MB' },
      { from: 'file', to: 's2', color: P.ink2, dashed: true, packets: 1 },
      { from: 'file', to: 's3', color: P.ink2, dashed: true, packets: 1 },
      { from: 'file', to: 's4', color: P.ink2, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'split', type: 'file', x: -2.6, y: 1.2, label: 'Split', color: P.raw, scale: 0.9 },
      { id: 'm1', type: 'factory', x: -0.6, y: 1.0, label: 'Map 1', color: P.process, scale: 0.85 },
      { id: 'm2', type: 'factory', x: 0.7, y: 0.4, label: 'Map 2', color: P.process, scale: 0.85 },
      { id: 'm3', type: 'factory', x: 2.0, y: -0.2, label: 'Map 3', color: P.process, scale: 0.85 },
      { id: 'k1', type: 'block', x: -0.6, y: 1.75, color: P.output, label: '(kota,1)' },
      { id: 'k2', type: 'block', x: 0.7, y: 1.15, color: P.blueSoft, label: '(kota,1)' },
      { id: 'k3', type: 'block', x: 2.0, y: 0.55, color: P.output, label: '(kota,1)' },
    ],
    links: [
      { from: 'split', to: 'm1', color: P.ink2, dashed: true, packets: 2 },
      { from: 'split', to: 'm2', color: P.ink2, dashed: true, packets: 2 },
      { from: 'split', to: 'm3', color: P.ink2, dashed: true, packets: 2 },
      { from: 'm1', to: 'k1', color: P.ink2, packets: 1 },
      { from: 'm2', to: 'k2', color: P.ink2, packets: 1 },
      { from: 'm3', to: 'k3', color: P.ink2, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'c1', type: 'block', x: -2.9, y: 1.0, color: P.raw, scale: 0.62 },
      { id: 'c2', type: 'block', x: -2.5, y: 1.4, color: P.process, scale: 0.62 },
      { id: 'c3', type: 'block', x: -2.1, y: 1.8, color: P.violet, scale: 0.62 },
      { id: 'c4', type: 'block', x: -2.5, y: 0.9, color: P.raw, scale: 0.58 },
      { id: 'c5', type: 'block', x: -2.1, y: 1.3, color: P.process, scale: 0.58 },
      { id: 'c6', type: 'block', x: -1.7, y: 1.7, color: P.violet, scale: 0.58 },
      { id: 'fun', type: 'funnel', x: 0, y: 0.4, label: 'Combiner', color: P.process },
      { id: 'out', type: 'block', x: 2.2, y: -0.4, color: P.output, label: '1000', scale: 1.7 },
    ],
    links: [
      { from: 'c1', to: 'fun', color: P.ink2, dashed: true, packets: 1 },
      { from: 'c3', to: 'fun', color: P.ink2, dashed: true, packets: 1 },
      { from: 'c5', to: 'fun', color: P.ink2, dashed: true, packets: 1 },
      { from: 'c6', to: 'fun', color: P.ink2, dashed: true, packets: 1 },
      { from: 'fun', to: 'out', color: P.output, packets: 2, label: 'mini reduce' },
    ],
  },
  {
    nodes: [
      { id: 'm1', type: 'factory', x: -2.8, y: 1.3, label: 'Map 1', color: P.process, scale: 0.78 },
      { id: 'm2', type: 'factory', x: -2.0, y: 0.9, label: 'Map 2', color: P.process, scale: 0.78 },
      { id: 'm3', type: 'factory', x: -1.2, y: 0.5, label: 'Map 3', color: P.process, scale: 0.78 },
      { id: 'r1', type: 'factory', x: 1.4, y: -0.2, label: 'Reduce 1', color: P.output, scale: 0.88 },
      { id: 'r2', type: 'factory', x: 2.6, y: -0.8, label: 'Reduce 2', color: P.output, scale: 0.88 },
    ],
    links: [
      { from: 'm1', to: 'r1', color: P.danger, dashed: true, packets: 2, lift: 54 },
      { from: 'm2', to: 'r2', color: P.danger, dashed: true, packets: 2, lift: 14 },
      { from: 'm3', to: 'r1', color: P.danger, dashed: true, packets: 2, lift: 74 },
      { from: 'm1', to: 'r2', color: P.danger, dashed: true, packets: 1, lift: 96 },
    ],
  },
  {
    nodes: [
      { id: 'red', type: 'factory', x: -1.6, y: 0.8, label: 'Reducer', color: P.output, scale: 1.05 },
      { id: 'r1', type: 'disk', x: 0.6, y: -0.2, label: 'Replica 1', color: P.output },
      { id: 'r2', type: 'disk', x: 1.6, y: -0.8, label: 'Replica 2', color: P.output },
      { id: 'r3', type: 'disk', x: 2.6, y: -1.4, label: 'Replica 3', color: P.output },
    ],
    links: [
      { from: 'red', to: 'r1', color: P.output, packets: 2 },
      { from: 'red', to: 'r2', color: P.output, packets: 2 },
      { from: 'red', to: 'r3', color: P.output, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'jak', type: 'truck', x: -2.8, y: 1.2, label: 'Jakarta 80%', color: P.danger, status: 'overloaded' },
      { id: 'j1', type: 'truck', x: -0.2, y: 0.2, label: 'J1', color: P.output, scale: 0.8 },
      { id: 'j2', type: 'truck', x: 0.6, y: -0.2, label: 'J2', color: P.output, scale: 0.8 },
      { id: 'j3', type: 'truck', x: 1.4, y: -0.6, label: 'J3', color: P.output, scale: 0.8 },
      { id: 'j4', type: 'truck', x: 2.2, y: -1.0, label: 'J4', color: P.output, scale: 0.8 },
    ],
    links: [
      { from: 'jak', to: 'j1', color: P.danger, dashed: true, packets: 1 },
      { from: 'jak', to: 'j2', color: P.danger, dashed: true, packets: 1 },
      { from: 'jak', to: 'j3', color: P.danger, dashed: true, packets: 1 },
      { from: 'jak', to: 'j4', color: P.danger, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'rm', type: 'tower', x: -2.6, y: 1.2, label: 'ResourceManager', color: P.process },
      { id: 'am', type: 'container', x: -0.2, y: 0.2, label: 'AM · container', color: P.output },
      { id: 'nm1', type: 'container', x: 1.0, y: -0.4, label: 'NodeManager 1', color: P.blueSoft },
      { id: 'nm2', type: 'container', x: 2.2, y: -1.0, label: 'NodeManager 2', color: P.blueSoft },
    ],
    links: [
      { from: 'rm', to: 'am', color: P.ink2, dashed: true, packets: 2 },
      { from: 'rm', to: 'nm1', color: P.ink2, dashed: true, packets: 1 },
      { from: 'rm', to: 'nm2', color: P.ink2, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'hive', type: 'hive', x: -2.6, y: 1.2, label: 'Hive', color: P.output },
      { id: 'meta', type: 'book', x: -0.8, y: 0.2, label: 'Metastore' },
      { id: 'd1', type: 'folder', x: 0.6, y: -0.4, label: 'dt=09-01' },
      { id: 'd2', type: 'folder', x: 1.6, y: -0.9, label: 'dt=09-02' },
      { id: 'd3', type: 'folder', x: 2.6, y: -1.4, label: 'dt=09-03' },
    ],
    links: [
      { from: 'hive', to: 'meta', color: P.process, packets: 2, label: 'SQL' },
      { from: 'meta', to: 'd1', color: P.output, dashed: true, packets: 1 },
      { from: 'meta', to: 'd2', color: P.output, dashed: true, packets: 1 },
      { from: 'meta', to: 'd3', color: P.output, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'file', type: 'file', x: -2.6, y: 1.2, label: 'Parquet / ORC', color: P.output, scale: 1.1 },
      { id: 'q', type: 'funnel', x: -0.6, y: 0.2, label: 'Query', color: P.process },
      { id: 'dash', type: 'dashboard', x: 1.8, y: -0.8, label: 'Revenue' },
    ],
    links: [
      { from: 'file', to: 'q', color: P.output, packets: 2, label: 'baca kolom' },
      { from: 'q', to: 'dash', color: P.output, packets: 2, label: 'BI' },
    ],
  },
]

/* ------------------------------------------------------------------ */
/* Apache Spark & Optimasi ETL                                         */
/* ------------------------------------------------------------------ */

const spark: IsoScene[] = [
  {
    nodes: [
      { id: 'd1', type: 'disk', x: -1.6, y: 0.8, label: 'Fase 1', color: P.raw, status: 'tired' },
      { id: 'd2', type: 'disk', x: 1.6, y: -0.8, label: 'Fase 2', color: P.raw, status: 'tired' },
    ],
    links: [
      { from: 'd1', to: 'd2', color: P.danger, dashed: true, packets: 2, label: 'tulis HDFS', lift: 34 },
      { from: 'd2', to: 'd1', color: P.danger, dashed: true, packets: 2, label: 'baca', lift: 132, reverse: true },
    ],
  },
  {
    nodes: [
      { id: 'chip', type: 'chip', x: 0, y: 0, label: 'SPARK · in-memory' },
      { id: 'b1', type: 'block', x: -2.2, y: 1.2, color: P.raw },
      { id: 'b2', type: 'block', x: -1.2, y: 1.8, color: P.process },
      { id: 'b3', type: 'block', x: 1.2, y: -0.6, color: P.output },
      { id: 'b4', type: 'block', x: 2.1, y: 0.1, color: P.violet },
    ],
  },
  {
    nodes: [
      { id: 'drv', type: 'tower', x: -2.6, y: 1.2, label: 'Driver', color: P.process },
      { id: 'e1', type: 'server', x: 0.0, y: 0.2, label: 'Executor 1', color: P.greenDark, status: 'active' },
      { id: 'e2', type: 'server', x: 1.2, y: -0.4, label: 'Executor 2', color: P.greenDark },
      { id: 'e3', type: 'server', x: 2.4, y: -1.0, label: 'Executor 3', color: P.greenDark },
    ],
    links: [
      { from: 'drv', to: 'e1', color: P.process, dashed: true, packets: 2, label: 'task' },
      { from: 'drv', to: 'e2', color: P.process, dashed: true, packets: 2 },
      { from: 'drv', to: 'e3', color: P.process, dashed: true, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'read', type: 'block', x: -2.8, y: 1.3, color: P.raw, label: 'read', scale: 1.3 },
      { id: 'filter', type: 'block', x: -1.6, y: 0.7, color: P.process, label: 'filter', scale: 1.3 },
      { id: 'group', type: 'block', x: -0.4, y: 0.1, color: P.violet, label: 'groupBy', scale: 1.3 },
      { id: 'show', type: 'block', x: 0.8, y: -0.5, color: P.green, label: 'show()', scale: 1.3 },
    ],
    links: [
      { from: 'read', to: 'filter', color: P.ink2, dashed: true, packets: 1 },
      { from: 'filter', to: 'group', color: P.ink2, dashed: true, packets: 1 },
      { from: 'group', to: 'show', color: P.greenDark, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 'prism', type: 'prism', x: -2.2, y: 0.9, label: 'Catalyst' },
      { id: 'a', type: 'block', x: 0.0, y: 0.3, color: P.raw, label: 'Analysis', scale: 1.5 },
      { id: 'l', type: 'block', x: 0.9, y: -0.15, color: P.process, label: 'Logical', scale: 1.5 },
      { id: 'p', type: 'block', x: 1.8, y: -0.6, color: P.violet, label: 'Physical', scale: 1.5 },
      { id: 'c', type: 'block', x: 2.7, y: -1.05, color: P.output, label: 'Codegen', scale: 1.5 },
    ],
    links: [
      { from: 'prism', to: 'a', color: P.violet, dashed: true, packets: 1 },
      { from: 'prism', to: 'l', color: P.violet, dashed: true, packets: 1 },
      { from: 'prism', to: 'p', color: P.violet, dashed: true, packets: 1 },
      { from: 'prism', to: 'c', color: P.violet, dashed: true, packets: 1 },
    ],
  },
  {
    nodes: [
      { id: 's1', type: 'block', x: -2.8, y: 1.3, color: P.process, label: 'Stage 1', scale: 1.5 },
      { id: 's2', type: 'block', x: 2.8, y: -1.3, color: P.output, label: 'Stage 2', scale: 1.5 },
      { id: 'wall', type: 'wall', x: 0, y: 0, label: 'stage boundary' },
    ],
    links: [
      { from: 's1', to: 's2', color: P.process, packets: 2, label: 'narrow · tanpa shuffle', lift: 118 },
      { from: 's1', to: 's2', color: P.danger, dashed: true, packets: 2, label: 'wide · shuffle', lift: 24 },
    ],
  },
  {
    nodes: [
      { id: 'bronze', type: 'block', x: -2.8, y: 1.3, color: P.raw, label: 'Bronze', scale: 1.6 },
      { id: 'q', type: 'filter', x: 0, y: 0.2, label: 'null · tipe · negatif · duplikat' },
      { id: 'silver', type: 'block', x: 2.2, y: -0.8, color: P.process, label: 'Silver', scale: 1.5 },
    ],
    links: [
      { from: 'bronze', to: 'q', color: P.rawDark, packets: 2 },
      { from: 'q', to: 'silver', color: P.process, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'silver', type: 'block', x: -2.8, y: 1.3, color: P.process, label: 'Silver', scale: 1.4 },
      { id: 'bc', type: 'tower', x: -1.0, y: 0.4, label: 'Broadcast', color: P.output },
      { id: 'e1', type: 'server', x: 0.6, y: -0.2, label: 'Exec 1', color: P.greenDark, scale: 0.85 },
      { id: 'e2', type: 'server', x: 1.6, y: -0.8, label: 'Exec 2', color: P.greenDark, scale: 0.85 },
      { id: 'gold', type: 'block', x: 2.9, y: -1.5, color: P.output, label: 'Gold', scale: 1.4 },
    ],
    links: [
      { from: 'silver', to: 'bc', color: P.process, dashed: true, packets: 2 },
      { from: 'bc', to: 'e1', color: P.output, dashed: true, packets: 2, label: 'broadcast' },
      { from: 'bc', to: 'e2', color: P.output, dashed: true, packets: 2 },
      { from: 'e2', to: 'gold', color: P.greenDark, packets: 2, label: 'revenue' },
    ],
  },
  {
    nodes: [
      { id: 'g', type: 'gauge', x: -0.6, y: 0.2, label: 'shuffle partitions' },
      { id: 'e1', type: 'block', x: -2.9, y: 1.0, color: P.rawDark, scale: 0.7 },
      { id: 'e2', type: 'block', x: -2.4, y: 0.5, color: P.raw, scale: 0.7 },
      { id: 'e3', type: 'block', x: -1.9, y: 0.0, color: P.rawDark, scale: 0.7 },
      { id: 'e4', type: 'block', x: -2.4, y: 1.5, color: P.raw, scale: 0.66 },
      { id: 'e5', type: 'block', x: -1.9, y: 1.0, color: P.rawDark, scale: 0.66 },
      { id: 'e6', type: 'block', x: -1.4, y: 0.5, color: P.raw, scale: 0.66 },
      { id: 'f1', type: 'block', x: 1.2, y: -0.2, color: P.process, scale: 0.8 },
      { id: 'f2', type: 'block', x: 1.7, y: -0.7, color: P.output, scale: 0.8 },
      { id: 'f3', type: 'block', x: 2.2, y: -1.2, color: P.process, scale: 0.8 },
      { id: 'f4', type: 'block', x: 2.7, y: -1.7, color: P.output, scale: 0.8 },
      { id: 'f5', type: 'block', x: 1.7, y: 0.3, color: P.output, scale: 0.76 },
      { id: 'f6', type: 'block', x: 2.2, y: -0.2, color: P.process, scale: 0.76 },
      { id: 'f7', type: 'block', x: 2.7, y: -0.7, color: P.output, scale: 0.76 },
      { id: 'f8', type: 'block', x: 3.2, y: -1.2, color: P.process, scale: 0.76 },
    ],
    links: [
      { from: 'e3', to: 'g', color: P.rawDark, dashed: true, packets: 1 },
      { from: 'g', to: 'f1', color: P.output, packets: 2, label: '→ 8 partisi' },
    ],
  },
  {
    nodes: [
      { id: 'skew', type: 'block', x: -2.8, y: 1.3, color: P.danger, label: 'Skew 80%', scale: 2.0 },
      { id: 'a1', type: 'block', x: -0.6, y: 0.6, color: P.process, label: 'AQE 1', scale: 1.1 },
      { id: 'a2', type: 'block', x: 0.3, y: 0.2, color: P.process, label: 'AQE 2', scale: 1.1 },
      { id: 'a3', type: 'block', x: 1.2, y: -0.2, color: P.process, label: 'AQE 3', scale: 1.1 },
      { id: 'f1', type: 'folder', x: 2.1, y: -0.7, label: '128 MB' },
      { id: 'f2', type: 'folder', x: 3.3, y: -2.0, label: '512 MB' },
    ],
    links: [
      { from: 'skew', to: 'a1', color: P.danger, dashed: true, packets: 2 },
      { from: 'skew', to: 'a2', color: P.danger, dashed: true, packets: 2 },
      { from: 'skew', to: 'a3', color: P.danger, dashed: true, packets: 2 },
      { from: 'a3', to: 'f1', color: P.output, packets: 2 },
      { from: 'a3', to: 'f2', color: P.output, packets: 2 },
    ],
  },
  {
    nodes: [
      { id: 'tube', type: 'tube', x: -2.4, y: 1.2, label: 'pytest ✓' },
      { id: 'shield', type: 'shield', x: -0.4, y: 0.4, label: 'CI · release' },
      { id: 'gold', type: 'block', x: 2.0, y: -0.8, color: P.output, label: 'Gold', scale: 1.5 },
    ],
    links: [
      { from: 'tube', to: 'shield', color: P.greenDark, packets: 2 },
      { from: 'shield', to: 'gold', color: P.output, packets: 2, label: 'rilis' },
    ],
  },
]

const allScenes: Record<StoryVariant, IsoScene[]> = { foundation, hadoop, spark }

export function sceneFor(variant: StoryVariant, index: number): IsoScene {
  const list = allScenes[variant]
  return list[Math.min(index, list.length - 1)] ?? { nodes: [] }
}
