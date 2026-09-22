# Lab 2 — Resistencia a la compresión del hormigón

**Sesión 3** · Regresión supervisada con el dataset UCI de **resistencia a compresión del hormigón**.

## Objetivo de aprendizaje

Entrenar un modelo de regresión (Random Forest) que prediga la resistencia a compresión de una mezcla de hormigón a partir de su dosificación, y usar la importancia de variables para razonar sobre qué ingredientes dominan el resultado.

## Contexto de ingeniería

En planta, decidir una dosificación implica ensayos destructivos costosos y lentos. Un modelo entrenado sobre datos históricos permite **explorar** combinaciones de ingredientes antes de invertir en esos ensayos — no los reemplaza, pero orienta qué probar primero.

## Datos

Dataset UCI — 1030 mezclas de hormigón de laboratorio, sin valores faltantes. Detalle completo: [`data/DATOS.md`](data/DATOS.md).

## Entorno

```bash
bash labs/setup.sh   # una sola vez, para todo el curso
source labs/.venv/bin/activate
```

## Notebook de referencia

[`resistencia_compresion.ipynb`](resistencia_compresion.ipynb) es un notebook completo y ejecutable de punta a punta. Ábrelo, ejecútalo (Run All) para ver el resultado esperado, y luego construye tu propio notebook guiándote por las secciones siguientes y por tu asistente de IA.

## Secciones y prompts sugeridos

### 1 — Contexto del hormigón y Machine Learning
**Objetivo:** identificar que predecir MPa es un problema de regresión.
**Qué debería producir tu celda:** una variable con el tipo de problema elegido, impresa en pantalla.
**Prompt sugerido:**
> Estoy en un Jupyter Lab de ingeniería civil (predicción de resistencia del hormigón). Necesito asignar una variable con el tipo de problema ("regresion" o "clasificacion") según si el target es MPa continuo, y un print del valor. El target es Resistencia en MPa (1030 mezclas UCI).

### 2 — Carga del dataset
**Objetivo:** cargar `data/concrete.csv` y mostrar las primeras filas.
**Qué debería producir tu celda:** un `DataFrame` cargado y una vista de sus primeras N filas.
**Prompt sugerido:**
> Ya existe un DataFrame `df` cargado desde `data/concrete.csv` (1030 filas, 9 columnas en español). Necesito mostrar sus primeras N filas (N entre 1 y 20) con `display`.

### 3 — Calidad de datos
**Objetivo:** revisar estadísticas de una columna de dosificación clave.
**Qué debería producir tu celda:** el resumen estadístico (`describe()`) de una columna elegida.
**Prompt sugerido:**
> El DataFrame `df` tiene columnas Cemento, Escoria, CenizaVolante, Agua, Superplastificante, AgregadoGrueso, AgregadoFino, Edad, Resistencia. Necesito el resumen estadístico (`describe()`) de una de ellas (por ejemplo Agua), mostrado con `display`.

### 4 — Estadísticas descriptivas
**Objetivo:** comparar dispersión entre varias columnas a la vez.
**Qué debería producir tu celda:** el resumen estadístico conjunto de al menos Agua, Edad y Resistencia.
**Prompt sugerido:**
> Usando el DataFrame `df` existente, necesito el resumen estadístico conjunto de las columnas Agua, Edad y Resistencia, mostrado con `display`.

### 5 — Distribución del target (Resistencia)
**Objetivo:** contar mezclas fuertes/débiles según un umbral de resistencia.
**Qué debería producir tu celda:** dos conteos (mezclas por encima y por debajo de un umbral en MPa) impresos con un f-string.
**Prompt sugerido:**
> El DataFrame `df` tiene columna Resistencia (MPa). Necesito definir un umbral en MPa (por ejemplo 40) y contar cuántas filas están por encima y por debajo, imprimiendo ambos conteos.

### 6 — Correlación entre variables
**Objetivo:** identificar qué ingredientes correlacionan más con la resistencia.
**Qué debería producir tu celda:** una lista de las N variables con mayor correlación absoluta respecto a Resistencia, impresas con su valor de r.
**Prompt sugerido:**
> Ya existe `corr = df.corr(numeric_only=True)`. Necesito ordenar las variables por correlación absoluta con Resistencia (excluyendo Resistencia misma) y mostrar las top-N con su valor de r.

### 7 — Relación física Agua vs Resistencia
**Objetivo:** graficar Agua vs Resistencia filtrando por edad mínima de curado.
**Qué debería producir tu celda:** un scatter (usando la función de graficado ya definida en el notebook) sobre un subconjunto filtrado por edad, y el conteo de filas filtradas.
**Prompt sugerido:**
> Ya existe una función `graficar_agua_resistencia(datos, titulo_extra)`. Necesito filtrar `df` por una edad mínima de curado (7, 14, 28 o 56 días) y llamar a esa función sobre el subconjunto filtrado, indicando cuántas filas quedaron.

### 8 — Partición train / test
**Objetivo:** separar los datos en entrenamiento y prueba.
**Qué debería producir tu celda:** `X_train`, `X_test`, `y_train`, `y_test`, con sus tamaños impresos.
**Prompt sugerido:**
> Ya existen `X` (features) e `y` (target Resistencia). Necesito partirlos con `train_test_split` (test_size=0.2, random_state=42) y mostrar el tamaño de cada conjunto.

### 9 — Random Forest (hiperparámetros)
**Objetivo:** entrenar un Random Forest y calcular su R² sobre test.
**Qué debería producir tu celda:** un modelo entrenado, sus predicciones sobre test, el R² correspondiente, y un diccionario de importancia de variables.
**Prompt sugerido:**
> Usando X_train, X_test, y_train, y_test ya definidos, necesito entrenar un RandomForestRegressor (n_estimators=100, max_depth=10), calcular sus predicciones y el R² sobre test, y un diccionario de importancia de variables por nombre de columna.

### 10 — Feature importance y validación visual
**Objetivo:** visualizar la importancia de variables junto a la calidad de las predicciones.
**Qué debería producir tu celda:** una figura con dos paneles — un barplot horizontal con las top-N variables más importantes, y un scatter de valores reales vs predichos con línea de predicción perfecta.
**Prompt sugerido:**
> Tengo un diccionario `importancias`, y los arrays `y_test`/`y_pred` de un modelo ya entrenado (R² en `r2_test`). Necesito una figura de 2 paneles: un barh con las top-N importancias, y un scatter real-vs-predicho con una línea diagonal de referencia.

## Validación

No hay autoevaluación automática (✅/❌). Compara tus gráficos y tu R² con los del notebook de referencia, y valida con tu criterio de ingeniero — la IA propone, el ingeniero valida visualmente.

## Entrega

- Tu propio notebook, ejecutado de punta a punta.
- `prompts_entregados.md` completado.
