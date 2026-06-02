# Lab 3: Clustering y Señales

!!! info "Sesión 5–6"
    **Fecha:** Jueves 11 / Martes 16 de Junio de 2026 | **Duración:** ~3 horas

## Objetivo de aprendizaje

Aplicar **PCA**, **K-Means** y **DBSCAN** a datos de sensores de monitoreo estructural (SHM): reducir dimensionalidad, agrupar patrones y comparar métodos de clustering frente a etiquetas de condición estructural.

## Contexto del problema

Dataset de sensores en edificio (Kaggle): lecturas de acelerómetros, inclinómetros, strain gauges, etc., con etiqueta de **condición estructural** (0 = sano, 1 = daño moderado, 2 = daño severo).

Explorarás correlaciones entre sensores, varianza explicada por PCA, clustering no supervisado y métricas de comparación (Silhouette, ARI).

## Abrir en GitHub Codespaces

1. Inicia sesión en GitHub.
2. **[Crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web)** y espera el build.
3. Abre el notebook:

   `labs/lab3/pca_monitoreo_estructural_alumno.ipynb`

   [Ver notebook en GitHub](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab3/pca_monitoreo_estructural_alumno.ipynb)

4. Ejecuta en orden; completa solo celdas `### TU TAREA AQUÍ ###`.

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

## Tareas prácticas

### Tarea 1: PCA y visualización (45 min)
- Interpreta varianza explicada y proyección 2D coloreada por daño.

### Tarea 2: K-Means y codo (45 min)
- Elige k con el método del codo; compara con etiquetas reales.

### Tarea 3: DBSCAN vs K-Means (45 min)
- Ajusta `eps` y `min_samples`; evalúa robustez ante ruido.

## Recursos en el repositorio

- **Notebook alumno:** `labs/lab3/pca_monitoreo_estructural_alumno.ipynb`
- **Dataset:** `labs/lab3/data/building_health_monitoring_dataset.csv`
- **Documentación:** `labs/lab3/data/DATOS.md`

## Lecturas adicionales

- [Kaggle — Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset)
- [Scikit-learn — Clustering](https://scikit-learn.org/stable/modules/clustering.html)

## Checklist

- [ ] Abrí el Codespace y el notebook alumno
- [ ] Completé PCA y visualizaciones
- [ ] Entrené K-Means y DBSCAN
- [ ] Comparé métricas con etiquetas reales
- [ ] Respondí las preguntas del notebook

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
