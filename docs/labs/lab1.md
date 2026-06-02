# Lab 1: PCA, Clustering y Monitoreo Estructural (SHM)

--8<-- "lab1-actions.md"

!!! info "Sesiones 4–5"
    **Duración:** ~3 horas

## Objetivo

Aplicar **PCA**, **K-Means** (codo), **DBSCAN**, loadings y clasificación con sensores Kaggle (monitoreo estructural).

## Contexto

Dataset con lecturas de acelerómetros, inclinómetros, strain gauges, etc., y etiqueta de **condición estructural** (0 = sano, 1 = daño moderado, 2 = daño severo).

## Pasos en Codespaces

1. Pulsa **Crear Codespace — Lab 1** (arriba).
2. Abre **`labs/lab1/pca_monitoreo_estructural_alumno.ipynb`**.
3. Ejecuta en orden; completa solo celdas `### TU TAREA AQUÍ ###`.

## Contenido del notebook

1. Contexto PCA en monitoreo estructural
2. Carga y limpieza del dataset Kaggle
3. Estadísticas descriptivas y correlaciones
4. Estandarización (`StandardScaler`)
5. PCA — scree plot y varianza explicada
6. Proyección 2D PC1 vs PC2
7. K-Means — gráfico del codo
8. DBSCAN — densidad y ruido
9. Comparativa KMeans vs DBSCAN (Silhouette, ARI)
10. Loadings, biplot y clasificación

## Recursos en el repositorio

- **Notebook:** `labs/lab1/pca_monitoreo_estructural_alumno.ipynb`
- **Dataset:** `labs/lab1/data/building_health_monitoring_dataset.csv`
- **Documentación:** `labs/lab1/data/DATOS.md`

## Lecturas

- [Kaggle — Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset)
- [Scikit-learn — Clustering](https://scikit-learn.org/stable/modules/clustering.html)

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
