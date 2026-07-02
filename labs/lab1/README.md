# Lab 1 — PCA, Kernel PCA, Clustering y Monitoreo Estructural (SHM)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?ref=main)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ia-estructuras-diplomado/curso-ia-web/main?labpath=labs/lab1/pca_monitoreo_estructural_alumno.ipynb)

**Sesión 2** · PCA lineal, **Kernel PCA**, KMeans (codo), DBSCAN, loadings y clasificación con sensores Kaggle.

## ¿Qué notebook abrir?

| Si… | Abre |
|-----|------|
| Sabes editar variables Python | [`pca_monitoreo_estructural_alumno.ipynb`](pca_monitoreo_estructural_alumno.ipynb) |
| Prefieres Copilot / Gemini / Cursor | [`pca_monitoreo_estructural_alumno_ia.ipynb`](pca_monitoreo_estructural_alumno_ia.ipynb) + [`prompts_entregados.md`](prompts_entregados.md) |

**Abrir en la nube (sin instalar nada local):**

| Plataforma | Notebook alumno |
|------------|-----------------|
| [GitHub Codespaces](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?ref=main) | `labs/lab1/pca_monitoreo_estructural_alumno.ipynb` |
| [Binder](https://mybinder.org/v2/gh/ia-estructuras-diplomado/curso-ia-web/main?labpath=labs/lab1/pca_monitoreo_estructural_alumno.ipynb) | mismo notebook |

## Archivos

| Archivo | Uso |
|---------|-----|
| `pca_monitoreo_estructural_alumno.ipynb` | Vía manual (13 preguntas + Kernel PCA 9.c/9.d) |
| `pca_monitoreo_estructural_alumno_ia.ipynb` | Vía IA — prompts y pegar código |
| `pca_monitoreo_estructural_solucion.ipynb` | Referencia docente (manual) |
| `pca_monitoreo_estructural_solucion_ia.ipynb` | Referencia docente (prompts canónicos) |
| `prompts_entregados.md` | Bitácora de prompts (entrega vía IA) |
| `_verificar.py` | Autoevaluación ✅ / ❌ (ambas vías) |
| `data/building_health_monitoring_dataset.csv` | Dataset Kaggle (1 000 × 7) |
| `data/DATOS.md` | Documentación de sensores |

## Flujo del lab (Pregunta 9 en adelante)

1. **PCA lineal** — proyección PC1 vs PC2 y scree plot.
2. **Kernel PCA (9.c)** — proyección no lineal; `X_cluster_input` para clustering.
3. **Comparación de kernels (9.d)** — `linear`, `poly`, `rbf`, `cosine`, `sigmoid`.
4. **KMeans y DBSCAN** — sobre el espacio Kernel PCA (no sobre sensores crudos).

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab1
jupyter notebook pca_monitoreo_estructural_alumno.ipynb
```

## GitHub Codespaces

1. Pulsa el badge **Open in GitHub Codespaces** (arriba) o [crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?ref=main).
2. Abre `labs/lab1/pca_monitoreo_estructural_alumno.ipynb`.
3. Kernel: **Python (curso-ia labs)** / `labs/.venv/bin/python`.

Guía del curso: [Lab 1 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab1/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
