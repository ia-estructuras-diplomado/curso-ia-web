# Lab 1: Fundamentos de Machine Learning

--8<-- "lab1-actions.md"

!!! info "Sesión 3"
    **Fecha:** Jueves, 4 de Junio de 2026 | **Duración:** ~2 horas

## Objetivo

Aprender el flujo completo de un problema de **regresión supervisada**: exploración de datos, partición train/test, entrenamiento de Random Forest e interpretación de resultados, usando el dataset UCI de **resistencia a compresión del hormigón**.

## Contexto del problema

El dataset incluye variables de mezcla (cemento, agua, aditivos, edad de curado, etc.) y la variable objetivo **Resistencia** (MPa). Tu meta es predecir la resistencia a partir de la composición y comparar la importancia de cada feature.

## Pasos en Codespaces

1. Pulsa **Crear Codespace — Lab 1** (arriba) e inicia sesión en GitHub si te lo pide.
2. Espera el build del contenedor (instala dependencias con `labs/setup.sh`).
3. Abre **`labs/lab1/resistencia_compresion_alumno.ipynb`** (botón *Abrir notebook* o explorador de archivos).
4. Ejecuta las celdas en orden; modifica solo bloques `### TU TAREA AQUÍ ###`.

## Contenido del notebook

1. Contexto ML (regresión vs clasificación)
2. Carga del dataset UCI (`data/concrete.csv`)
3. Calidad de datos y estadísticas descriptivas
4. Distribución del target y correlaciones
5. Partición train/test
6. Random Forest — hiperparámetros y selección de features
7. Feature importance y gráfico predicción vs realidad

## Tareas prácticas

### Tarea 1: Exploración (30 min)
- Revisa estadísticas descriptivas y correlaciones.
- Identifica variables más relacionadas con la resistencia.

### Tarea 2: Entrenamiento (45 min)
- Experimenta con `n_estimators`, `max_depth` y columnas de entrada.
- Compara métricas en train vs test (¿overfitting?).

### Tarea 3: Interpretación (30 min)
- Analiza feature importance.
- Propón mejoras para un caso real de control de calidad en obra.

## Recursos en el repositorio

- **Notebook alumno:** `labs/lab1/resistencia_compresion_alumno.ipynb`
- **Dataset:** `labs/lab1/data/concrete.csv`
- **Documentación de datos:** `labs/lab1/data/DATOS.md`

## Lecturas adicionales

- [Scikit-learn — Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forest)
- [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)

## Checklist

- [ ] Abrí el Codespace y el notebook alumno
- [ ] Completé la exploración de datos
- [ ] Entrené Random Forest con distintos hiperparámetros
- [ ] Interpreté feature importance y predicción vs realidad
- [ ] Respondí las preguntas del notebook

## Próximos pasos

- Lab 2 (detección de anomalías SHM) en Sesión 5
- Aplicar estos conceptos en el Trabajo Grupal 1

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
