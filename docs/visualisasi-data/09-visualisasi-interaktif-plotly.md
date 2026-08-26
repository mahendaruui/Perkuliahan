# 📘 Modul 09: Visualisasi Interaktif & Web-Ready dengan Plotly

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memahami arsitektur pustaka **Plotly Express** dan **Plotly Graph Objects** berbasis D3.js dan WebGL.
2. Membangun visualisasi interaktif dengan fitur: hover tooltip dinamis, zooming, panning, dan seleksi data.
3. Menambahkan kontrol interaktif: dropdown selector, range slider, dan animasi pergeseran waktu (*temporal animation*).
4. Mengekspor grafik ke format HTML interaktif siap web (*standalone HTML*).

---

## 1. Keunggulan Visualisasi Interaktif

Visualisasi statis sering kali mengalami masalah *overplotting* saat menampilkan ribuan titik data. Plotly memecahkan masalah ini dengan memberikan pengguna kendali untuk mengeksplorasi data secara mandiri (*self-service analytics*).

---

## 2. Implementasi Plotly Express dengan Animasi Dinamis

```python
import plotly.express as px

# Memuat dataset global Gapminder
df = px.data.gapminder()

# Scatter Plot Animasi Dinamis (Hans Rosling Style)
fig = px.scatter(
    df, 
    x="gdpPercap", 
    y="lifeExp", 
    animation_frame="year", 
    animation_group="country",
    size="pop", 
    color="continent", 
    hover_name="country",
    log_x=True, 
    size_max=55, 
    range_x=[100, 100000], 
    range_y=[25, 90],
    labels={
        "gdpPercap": "PDB Per Kapita (USD - Skala Log)",
        "lifeExp": "Angka Harapan Hidup (Tahun)",
        "pop": "Populasi",
        "continent": "Benua"
    },
    title="Evolusi PDB vs Harapan Hidup Global (1952–2007)"
)

# Kustomisasi Layout & Template Dark/Light
fig.update_layout(
    template="plotly_white",
    font=dict(family="Arial, sans-serif", size=12),
    title_font=dict(size=16, color="#1e293b")
)

# Menyimpan ke File HTML Mandiri
fig.write_html("gapminder_interaktif.html")
fig.show()
```