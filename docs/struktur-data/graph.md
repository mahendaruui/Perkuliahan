# Minggu 12: Struktur Data Graf (Graph Network) & Pemodelan Relasi

::: tip CAPAIAN PEMBELAJARAN (SUB-CPMK 6)
- **CPMK Terkait:** CPMK0101 (Struktur Data Non-Linear), CPMK0106 (Analisis Kompleksitas)
- **CPL Terkait:** CPL01 (Pengetahuan Dasar), CPL04 (Solusi Rekayasa Komputasi)
- **Indikator:** Mahasiswa mampu menguraikan definisi formal Graf `G = (V, E)`, membedakan graf berarah (*Directed*) vs tidak berarah (*Undirected*), berbobot (*Weighted*), serta mengimplementasikan representasi *Adjacency List* menggunakan Golang `map[T][]Edge[T]`.
:::

---

## 1. Definisi & Jenis-Jenis Graf

**Graf ($G$)** adalah struktur data non-linear matematika yang didefinisikan sebagai pasangan himpunan:
$`G = (V, E)`$
- **$V$ (*Vertices / Nodes*):** Himpunan simpul objek data.
- **$E$ (*Edges / Links*):** Himpunan pasangan simpul yang menyatakan relasi/koneksi antar objek.

```mermaid
graph LR
    subgraph Graf Tidak Berarah (Undirected)
        A((A)) --- B((B))
        B --- C((C))
        A --- C
    end
    subgraph Graf Berarah & Berbobot (Directed Weighted)
        X((Banda Aceh)) -- "100 km (Biaya: 50)" --> Y((Sigli))
        Y -- "120 km (Biaya: 60)" --> Z((Bireuen))
    end
    style A fill:#e0f2fe,stroke:#0284c7;
    style B fill:#e0f2fe,stroke:#0284c7;
    style C fill:#e0f2fe,stroke:#0284c7;
    style X fill:#dcfce7,stroke:#16a34a;
    style Y fill:#dcfce7,stroke:#16a34a;
    style Z fill:#dcfce7,stroke:#16a34a;
```

---

## 2. Komparasi Representasi Memori: Adjacency Matrix vs Adjacency List

| Parameter | Adjacency Matrix (Matriks $V × V$) | Adjacency List (Daftar Tetangga) |
| :--- | :--- | :--- |
| **Konsumsi Memori** | `O(V²)` (Boros jika graf renggang / *sparse*). | **`O(V + E)` (Sangat Hemat & Optimal)**. |
| **Cek Ketetanggaan ($u \to v$)** | **`O(1)`** (Langsung akses matriks `[u][v]`). | $O(degree(u))$. |
| **Cari Seluruh Tetangga Simpul**| $O(V)$ (Harus pindai seluruh baris). | **$O(degree(u))$ (Cepat)**. |
| **Rekomendasi Industri** | Graf padat (*dense graph*). | **Graf umum, jejaring sosial, peta jalan**. |

---

## 3. Implementasi Generic Weighted Graph di Golang

::: code-group
```go [graph.go]
package main

import "fmt"

type Edge[T comparable] struct {
    To     T
    Weight int
}

type Graph[T comparable] struct {
    adjList map[T][]Edge[T]
}

func NewGraph[T comparable]() *Graph[T] {
    return &Graph[T]{
        adjList: make(map[T][]Edge[T]),
    }
}

// Menambahkan Sisi Graf (Undirected)
func (g *Graph[T]) AddEdge(from, to T, weight int) {
    g.adjList[from] = append(g.adjList[from], Edge[T]{To: to, Weight: weight})
    g.adjList[to] = append(g.adjList[to], Edge[T]{To: from, Weight: weight})
}

// Menampilkan Struktur Graf
func (g *Graph[T]) PrintGraph() {
    for vertex, edges := range g.adjList {
        fmt.Printf("Simpul [%v] terhubung ke:\n", vertex)
        for _, edge := range edges {
            fmt.Printf("  -> %v (Bobot/Jarak: %d)\n", edge.To, edge.Weight)
        }
    }
}

func main() {
    petaAceh := NewGraph[string]()

    petaAceh.AddEdge("Banda Aceh", "Jantho", 55)
    petaAceh.AddEdge("Banda Aceh", "Sigli", 110)
    petaAceh.AddEdge("Sigli", "Bireuen", 105)
    petaAceh.AddEdge("Bireuen", "Lhokseumawe", 45)

    petaAceh.PrintGraph()
}
```
:::

---

## 📝 Evaluasi & Latihan Mandiri (Sub-CPMK 6)

1. Hitunglah konsumsi memori yang dihemat oleh *Adjacency List* dibandingkan *Adjacency Matrix* untuk graf dengan $10.000$ simpul dan $30.000$ sisi!
2. Rancanglah fungsi untuk menghitung nilai **Derajat (*Degree*)** dari suatu simpul pada graf tidak berarah!
