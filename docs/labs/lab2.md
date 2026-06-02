# Lab 2: Predicción de Resistencia a la Compresión

--8<-- "lab2-actions.md"

!!! info "Sesión 3"
    **Duración:** ~2 horas

## Objetivo

**Regresión supervisada** con el dataset UCI de resistencia a compresión del hormigón: EDA, train/test, Random Forest e interpretación.

## Contexto

Variables de mezcla (cemento, agua, aditivos, edad de curado) y target **Resistencia** (MPa). Predecir resistencia a partir de la dosificación.

## Pasos en Codespaces

1. Pulsa **Crear Codespace — Lab 2** (arriba).
2. Abre **`labs/lab2/resistencia_compresion_alumno.ipynb`**.
3. Ejecuta en orden; modifica solo bloques `### TU TAREA AQUÍ ###`.

## Contenido del notebook

1. Contexto ML (regresión vs clasificación)
2. Carga del dataset UCI (`data/concrete.csv`)
3. Calidad de datos y estadísticas descriptivas
4. Distribución del target y correlaciones
5. Partición train/test
6. Random Forest — hiperparámetros y features
7. Feature importance y predicción vs realidad

## Recursos en el repositorio

- **Notebook:** `labs/lab2/resistencia_compresion_alumno.ipynb`
- **Dataset:** `labs/lab2/data/concrete.csv`
- **Documentación:** `labs/lab2/data/DATOS.md`

## Lecturas

- [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- [Scikit-learn — Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forest)

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
