# Lab 4 Parte 2 — LSTM en sensores SHM

**Sesión 8** · Redes recurrentes aplicadas a monitoreo estructural con series temporales.

## Objetivo

Entrenar una **LSTM** (PyTorch) sobre el dataset [Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset) — el mismo CSV que los Labs 1 y 3, pero esta vez explotando el **orden temporal** de las lecturas en lugar de tratarlas como filas independientes.

## Contexto de ingeniería

Un modelo tabular (como el XGBoost del Lab 3) trata cada lectura de forma aislada. Una LSTM, en cambio, tiene memoria: puede aprender cómo evoluciona `Strain` en los segundos previos a un cambio de estado. Esa memoria temporal es la base de dos capacidades con valor real en obra: **detectar** el estado actual de la estructura a partir de una ventana reciente de sensores, y **pronosticar** hacia dónde va la señal — con sus límites, que este lab hace explícitos (ver sección 9).

## Datos

CSV de sensores SHM (mismo dataset que Lab 1/Lab 3) — ver [`data/DATOS.md`](data/DATOS.md).

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4/part_2
jupyter notebook rnn_sensores_estructuras.ipynb
```

Ver también [Parte 1 — CNN](../part_1/README.md).

## Notebook de referencia

`rnn_sensores_estructuras.ipynb` es un notebook completo y ejecutable de punta a punta. Ábrelo, ejecútalo (Run All) para ver el resultado esperado, y luego construye tu propio notebook guiándote por las secciones siguientes y por tu asistente de IA.

## Secciones y prompts sugeridos

### 1 — Panorama RNN/LSTM
**Objetivo:** listar los componentes clave de una RNN/LSTM aplicada a sensores SHM.
**Qué debería producir tu celda:** una lista con al menos 4 componentes (ventana temporal, LSTM, hidden size, dropout…) impresa uno por línea.
**Prompt sugerido:**
> Lab 4 Parte 2 — LSTM en sensores SHM. Genera código que: 1) defina una lista de componentes clave de una LSTM aplicada a series de sensores (ventana temporal, LSTM, hidden size, dropout, fully connected); 2) imprima cada componente. No uses imports nuevos.

### 2 — Carga y orden temporal
**Objetivo:** definir las columnas de sensores a usar y mostrar las primeras filas del CSV ya ordenado por tiempo.
**Qué debería producir tu celda:** una lista `FEATURES` con los 5 sensores (sin `Timestamp` ni `Condition Label`), y una vista de las primeras filas.
**Prompt sugerido:**
> En Jupyter ya tengo `df` cargado y ordenado por Timestamp (1000 filas). Genera código que: 1) defina la lista de columnas de sensores a usar como features (excluyendo Timestamp y Condition Label); 2) defina cuántas filas mostrar; 3) imprima las features y muestre esas primeras filas.

### 3 — Calidad y balance
**Objetivo:** revisar un sensor crítico y confirmar que la limpieza (quitar nulos) no distorsiona el dataset.
**Qué debería producir tu celda:** estadísticas descriptivas (`describe()`) de un sensor elegido, calculadas sobre los datos crudos.
**Prompt sugerido:**
> Tengo `df` (crudo) y `df_limpio` (sin nulos en las features). Genera código que elija un sensor relevante para daño estructural, calcule `describe()` sobre el `df` crudo para esa columna, y lo muestre.

### 4 — Serie temporal global (EDA)
**Objetivo:** graficar un sensor contra el tiempo antes de entrenar cualquier modelo.
**Qué debería producir tu celda:** una gráfica de línea de un tramo del sensor elegido, con título y ejes etiquetados.
**Prompt sugerido:**
> Tengo `df_limpio` con una columna de sensor. Genera matplotlib que tome los primeros N puntos de esa columna y grafique una línea temporal con título y `plt.show()`.

### 5 — Series por condición estructural
**Objetivo:** comparar cómo se ven 2-3 sensores según `Condition Label` (0/1/2).
**Qué debería producir tu celda:** subplots, uno por sensor, cada uno con una línea por clase y leyenda.
**Prompt sugerido:**
> Tengo `df_limpio` con las features y `Condition Label`. Genera código que, para 2-3 sensores, grafique en subplots los primeros ~100 puntos de cada clase (0, 1, 2) con leyenda y títulos.

### 6 — Ventanas deslizantes y split temporal
**Objetivo:** construir los `DataLoader` de entrenamiento/validación a partir de ventanas deslizantes, sin fuga de información futura.
**Qué debería producir tu celda:** un tamaño de ventana y de batch, y los loaders resultantes junto con sus tamaños.
**Prompt sugerido:**
> Tengo una función `make_sequence_loaders(df, features, window_size, batch_size)` ya definida. Genera código que elija un tamaño de ventana y de batch razonables, cree los loaders de train/val, e imprima cuántas ventanas hay en cada uno y la forma del primer batch.

### 7 — Arquitectura LSTM
**Objetivo:** construir un clasificador LSTM multiclase sobre las ventanas.
**Qué debería producir tu celda:** una clase `LSTMClassifier` (LSTM + capa lineal a 3 clases) instanciada y movida al dispositivo (`device`).
**Prompt sugerido:**
> Tengo `WINDOW_SIZE`, `device`, 5 features de entrada y 3 clases de salida. Genera una clase `LSTMClassifier(nn.Module)` con una LSTM (`batch_first=True`) seguida de una capa lineal a 3 clases, usando el último estado oculto para clasificar. Instáncialo y muévelo a `device`.

### 8 — Entrenamiento y métricas
**Objetivo:** entrenar el clasificador y registrar la evolución de pérdida/accuracy.
**Qué debería producir tu celda:** un número de épocas y tasa de aprendizaje, un bucle de entrenamiento usando funciones de entrenamiento/evaluación ya definidas, y la accuracy final de validación.
**Prompt sugerido:**
> Tengo `modelo`, `train_loader`, `val_loader`, y funciones `train_one_epoch`/`eval_epoch` ya definidas. Genera un número de épocas, una tasa de aprendizaje, la función de pérdida y el optimizador, un bucle que entrene y evalúe por época guardando el historial, y al final calcula la accuracy de validación de la última época.

### 9 — Pronóstico: interpolación, extrapolación y umbral de alerta
**Objetivo:** medir qué tan bien un segundo modelo (LSTM regresora sobre `Strain`) reconstruye un tramo enmascarado (interpolación) frente a pronosticar pasos futuros nunca vistos (extrapolación), y reconocer que ambas tareas tienen niveles de confianza muy distintos.
**Qué debería producir tu celda:** para interpolación, un error medio (MAE) y una gráfica real-vs-predicho en el hueco enmascarado; para extrapolación, lo mismo pero sobre un horizonte futuro, además de una comprobación explícita de si el pronóstico cruza un umbral de alerta.
**Prompt sugerido:**
> Tengo un modelo regresor LSTM entrenado sobre `Strain` normalizado, y funciones `evaluar_interpolacion(...)` y `evaluar_extrapolacion(...)` ya definidas. Genera código que: 1) llame a la de interpolación con un hueco pequeño y grafique real vs. predicho; 2) llame a la de extrapolación con un horizonte de pasos futuros, grafique histórico + real + predicho, dibuje una línea horizontal de umbral ilustrativo, e imprima una advertencia si el pronóstico la cruza.

El umbral usado en el notebook de referencia es **ilustrativo**, no normativo — en el **Lab 5** recuperarás con RAG el valor exacto desde las normas peruanas (E.020/E.030/E.050) en PDF y podrás reemplazarlo por uno verificado, citando la página exacta.

## Validación

No hay autoevaluación automática (✅/❌). Compara tus gráficos y métricas (accuracy de validación, MAE de interpolación/extrapolación) con los del notebook de referencia, y valida con tu criterio de ingeniero — especialmente si el MAE de extrapolación te parece aceptable para tomar una decisión real.

## Entrega

- Tu notebook ejecutado de punta a punta
- `prompts_entregados.md` completado
