# Dataset — Resistencia a la compresión del hormigón (UCI)

## Origen y licencia

- **Repositorio:** [UCI Machine Learning — Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength)
- **Autor original:** Prof. I-Cheng Yeh (Chung-Hua University, Taiwán)
- **Archivo fuente en este repo:** `Concrete_Data.xls` → convertido a `concrete.csv`
- **Observaciones:** 1 030 mezclas de laboratorio · **sin valores faltantes**

> Reutilización permitida citando el paper original de Yeh (1998), *Cement and Concrete Research*.

## ¿Qué representa cada fila?

Cada registro es una **mezcla de hormigón** probada en laboratorio. Se midieron los kg/m³ de cada componente, la **edad del ensayo** (días de curado) y la **resistencia a compresión** obtenida (MPa).

En obra, esta variable es la que usamos para verificar cumplimiento estructural; aquí la predecimos a partir de la dosificación.

## Variables (`concrete.csv`)

| Columna | Unidad | Rol | Descripción breve |
|---------|--------|-----|-------------------|
| `Cemento` | kg/m³ | Feature | Ligante principal |
| `Escoria` | kg/m³ | Feature | Escoria de alto horno (cemento suplementario) |
| `CenizaVolante` | kg/m³ | Feature | Ceniza volante (puzolana) |
| `Agua` | kg/m³ | Feature | Agua de amasado — influye en relación a/c |
| `Superplastificante` | kg/m³ | Feature | Aditivo reductor de agua |
| `AgregadoGrueso` | kg/m³ | Feature | Grava / áridos gruesos |
| `AgregadoFino` | kg/m³ | Feature | Arena / áridos finos |
| `Edad` | días | Feature | Días desde el vaciado hasta el ensayo (1–365) |
| `Resistencia` | MPa | **Target (y)** | Resistencia a compresión medida |

## Rangos típicos (resumen estadístico)

| Variable | Mín | Media | Máx |
|----------|-----|-------|-----|
| Cemento | 102 | 281 | 540 |
| Agua | 122 | 182 | 247 |
| Edad | 1 | 46 | 365 |
| Resistencia | 2,3 | 35,8 | 82,6 |

La resistencia varía mucho porque incluye probetas jóvenes (pocos días) y mezclas con distinta dosificación.

## Tipo de problema de Machine Learning

- **Regresión supervisada:** predecir `Resistencia` en MPa (valor continuo).
- **Clasificación supervisada (Lab 2, sección 10):** etiqueta binaria *fuerte* (≥ 40 MPa) vs *débil* (< 40 MPa), útil para verificar cumplimiento rápido en planta.
- **Features (X):** las 8 columnas de ingredientes y edad.
- **Targets (y):** `Resistencia` (regresión) o binario derivado del umbral (clasificación).

Modelos usados en el lab: `LinearRegression`, `RandomForest`, `XGBoost` (regresión) y `RandomForestClassifier` (clasificación).

## Interpretación física (enfoque profesional)

1. **Edad:** a igual dosificación, probetas más viejas suelen tener mayor resistencia (hidrataración).
2. **Agua:** más agua → mayor relación agua/cemento → suele **reducir** resistencia (correlación negativa en este dataset).
3. **Cemento y aditivos:** más cemento o superplastificante bien dosificado puede **aumentar** resistencia sin subir agua.
4. **Uso en planta:** un modelo no sustituye ensayos normativos, pero ayuda a **explorar dosificaciones** y reducir ensayos destructivos de prueba.

## Advertencia

Estos datos provienen de **laboratorio controlado**. Antes de aplicar un modelo en obra real debes validar con ensayos locales, normativa vigente y condiciones de planta (temperatura, curado, calidad de áridos).
