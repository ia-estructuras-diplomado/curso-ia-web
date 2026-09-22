# Lab 2: Predicción de Resistencia a la Compresión

--8<-- "lab2-actions.md"

!!! info "Sesión 3"
    **Duración:** ~2 horas

## Objetivo

Entrenar un modelo de **regresión** (Random Forest) que prediga la
resistencia a compresión (MPa) de una mezcla de hormigón a partir de su
dosificación, y usar la importancia de variables para razonar sobre qué
ingredientes dominan el resultado.

## Pasos

1. Abre **`labs/lab2/resistencia_compresion.ipynb`** y ejecútalo (Run All).
2. Construye tu propio notebook guiándote por el
   [README del lab](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab2/README.md).

## Contenido del notebook

1. Contexto del problema y carga del dataset UCI (`data/concrete.csv`)
2. Calidad de datos y estadísticas descriptivas
3. Distribución del target y correlaciones
4. Relación física Agua vs Resistencia
5. Partición train/test y Random Forest
6. Feature importance y validación visual (real vs. predicho)

## Recursos

- [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- [Scikit-learn — Ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html)

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)
