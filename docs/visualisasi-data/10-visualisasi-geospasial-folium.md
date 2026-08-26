# 📘 Modul 10: Visualisasi Data Geospasial & Pemetaan Wilayah

## 🎯 Capaian Pembelajaran (Sub-CPMK 3)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memahami konsep dasar data geospasial: Sistem Koordinat Geografis (WGS84 / EPSG:4326), Lintang & Bujur, Poligon, serta format GeoJSON / Shapefile.
2. Membangun peta interaktif menggunakan pustaka **Folium** (berbasis Leaflet.js).
3. Membuat **Peta Choropleth** untuk memvisualisasikan data statistik per wilayah administratif (Provinsi / Kabupaten di Indonesia).
4. Menerapkan Marker Clustering dan Heatmap Kepadatan Titik Lokasi.

---

## 1. Pembuatan Peta Interaktif dengan Folium

```python
import folium
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd

# Koordinat Pusat: Kota Banda Aceh
peta_aceh = folium.Map(location=[5.5483, 95.3238], zoom_start=13, tiles='CartoDB positron')

# Data Titik Fasilitas Kesehatan (Simulasi)
faskes_data = [
    {"nama": "RSUD Dr. Zainoel Abidin", "lat": 5.5686, "lon": 95.3402, "tipe": "RSUD Rujukan"},
    {"nama": "RS Ibu dan Anak Aceh", "lat": 5.5612, "lon": 95.3345, "tipe": "RS Khusus"},
    {"nama": "Klinik Pratama UUI", "lat": 5.5501, "lon": 95.3190, "tipe": "Klinik Kampus"}
]

marker_cluster = MarkerCluster().add_to(peta_aceh)

for faskes in faskes_data:
    folium.Marker(
        location=[faskes["lat"], faskes["lon"]],
        popup=f"<b>{faskes['nama']}</b><br>Tipe: {faskes['tipe']}",
        tooltip=faskes["nama"],
        icon=folium.Icon(color="blue", icon="plus-sign")
    ).add_to(marker_cluster)

peta_aceh.save("peta_faskes_aceh.html")
```

---

## 2. Pembuatan Peta Choropleth dengan GeoPandas & Folium

```python
import geopandas as gpd

# Memuat file batas wilayah GeoJSON Provinsi di Indonesia
# gdf_indonesia = gpd.read_file('indonesia_provinces.geojson')

# folium.Choropleth(
#     geo_data=gdf_indonesia,
#     name='choropleth',
#     data=df_ipm,
#     columns=['kode_provinsi', 'indeks_pembangunan_manusia'],
#     key_on='feature.properties.id',
#     fill_color='YlGnBu',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name='Indeks Pembangunan Manusia (IPM)'
# ).add_to(peta_indonesia)
```