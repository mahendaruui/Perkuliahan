# 📘 Modul 12: Visualisasi Model AI, Machine Learning & Reduksi Dimensi

## 🎯 Capaian Pembelajaran (Sub-CPMK 4)
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:
1. Memvisualisasikan dataset berdimensi tinggi ke dalam ruang 2D/3D menggunakan **Principal Component Analysis (PCA)** dan **t-SNE / UMAP**.
2. Mengevaluasi performa model klasifikasi Machine Learning melalui visualisasi: **Confusion Matrix**, **Kurva ROC-AUC**, dan **Precision-Recall Curve**.
3. Memvisualisasikan bobot fitur (*Feature Importance*) dan interpretasi model (*Explainable AI - SHAP Values*).
4. Memvisualisasikan struktur pohon keputusan (*Decision Tree Visualizer*).

---

## 1. Reduksi Dimensi & Visualisasi Klaster dengan PCA

```python
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
import pandas as pd

# Load dataset Wine (13 fitur kimiawi)
wine = load_wine()
X = wine.data
y = wine.target
target_names = wine.target_names

# Reduksi 13 Dimensi menjadi 2 Komponen Utama (PC1 & PC2)
pca = PCA(n_components=2)
components = pca.fit_transform(X)

df_pca = pd.DataFrame(data=components, columns=['PC 1', 'PC 2'])
df_pca['Class'] = [target_names[i] for i in y]

# Plot Hasil Reduksi Dimensi
fig = px.scatter(
    df_pca, x='PC 1', y='PC 2', color='Class',
    title=f'Visualisasi PCA Dataset Wine (Variansi Total: {sum(pca.explained_variance_ratio_)*100:.1f}%)',
    template='plotly_white'
)
fig.show()
```

---

## 2. Visualisasi Evaluasi Model: Confusion Matrix Heatmap

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# y_true, y_pred = ...
# cm = confusion_matrix(y_true, y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Kelas A', 'Kelas B'])
# disp.plot(cmap='Blues', values_format='d')
# plt.title("Confusion Matrix Model Klasifikasi", fontweight='bold')
# plt.show()
```