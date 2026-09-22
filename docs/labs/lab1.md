# Lab 1: PCA, Clustering y Monitoreo Estructural (SHM)

--8<-- "lab1-actions.md"

!!! info "Sesiones 4–5"
    **Duración:** ~3 horas

## Objetivo

Reducir la dimensionalidad de 5 señales de sensor (aceleración en 3 ejes,
deformación, temperatura) con **PCA**, y explorar si los estados de daño
(`Condition Label`) emergen como agrupaciones naturales con **KMeans** y
**DBSCAN** — sin usar la etiqueta para calcularlas, solo para evaluar al final.

## Pasos

1. Abre **`labs/lab1/pca_monitoreo_estructural.ipynb`** y ejecútalo (Run All).
2. Construye tu propio notebook guiándote por el
   [README del lab](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/README.md).

## Contenido del notebook

1. Carga y limpieza del dataset de sensores
2. Estadísticas descriptivas, distribución de clases, correlación
3. Estandarización y PCA (varianza explicada, proyección 2D)
4. KMeans (método del codo) y DBSCAN (densidad)
5. Comparación contra la etiqueta real (Silhouette, ARI)
6. Loadings y clasificación (features originales vs. PCA)

## Recursos

- **Dataset:** `labs/lab1/data/building_health_monitoring_dataset.csv` ([DATOS.md](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/data/DATOS.md))
- [Kaggle — Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset)
- [Scikit-learn — Clustering](https://scikit-learn.org/stable/modules/clustering.html)

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)
