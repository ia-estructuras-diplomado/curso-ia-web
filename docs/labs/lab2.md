# Lab 2: Predicción de Resistencia a la Compresión

--8<-- "lab2-actions.md"

!!! info "Sesión 3"
    **Duración:** ~2 horas

## Objetivo

**Regresión y clasificación supervisada** con el dataset UCI de resistencia a compresión del hormigón: EDA, comparar modelos de regresión (LinearRegression, Random Forest, XGBoost) y un modelo de clasificación binaria (fuerte/débil ≥ 40 MPa).

## Contexto

Variables de mezcla (cemento, agua, aditivos, edad de curado) y target **Resistencia** (MPa). El lab explora el dataset al máximo: predecir MPa (regresión) y si la mezcla supera un umbral de obra (clasificación).

## Pasos en Codespaces

1. Pulsa **Crear Codespace — Lab 2** (arriba).
2. Abre **`labs/lab2/resistencia_compresion_alumno.ipynb`**.
3. Ejecuta en orden; modifica solo bloques `### TU TAREA AQUÍ ###`.

## Contenido del notebook

1. Contexto ML (regresión vs clasificación)
2. Carga del dataset UCI (`data/concrete.csv`)
3. Calidad de datos y estadísticas descriptivas
4. Distribución del target, umbral 40 MPa y correlaciones
5. Partición train/test
6. **Comparar regresión:** LinearRegression, Random Forest, XGBoost
7. **Clasificación:** fuerte/débil con Random Forest + matriz de confusión

## Recursos en el repositorio

- **Notebook:** `labs/lab2/resistencia_compresion_alumno.ipynb`
- **Dataset:** `labs/lab2/data/concrete.csv`
- **Documentación:** `labs/lab2/data/DATOS.md`

## Lecturas

- [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- [Scikit-learn — Ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [XGBoost — Python API](https://xgboost.readthedocs.io/en/stable/python/python_api.html)

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
