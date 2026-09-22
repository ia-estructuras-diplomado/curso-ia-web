# Lab 1 — PCA, Clustering y Monitoreo Estructural (SHM)

**Sesión 4–5** · PCA, KMeans (método del codo), DBSCAN, loadings y una comparación de clasificación, sobre
lecturas de sensores de monitoreo estructural (SHM).

## Objetivo

Reducir la dimensionalidad de 5 señales de sensor (aceleración en 3 ejes, deformación, temperatura) con PCA, y
explorar si los estados de daño de una estructura (`Condition Label`) emergen como agrupaciones naturales al
aplicar KMeans y DBSCAN — sin usar esa etiqueta para calcular ni los componentes ni los clústeres, solo para
evaluar al final qué tan bien se alinean con la realidad conocida.

## Contexto de ingeniería

En monitoreo estructural real, decenas de sensores generan lecturas redundantes y ruidosas. PCA condensa esa
información en pocas componentes interpretables antes de visualizar o alimentar un clasificador; el clustering no
supervisado explora si el propio patrón de los datos ya sugiere distintos estados estructurales, útil como
primera señal de alerta antes de confirmar con inspección normativa.

## Datos

`data/building_health_monitoring_dataset.csv` (1000 filas × 7 columnas, dataset Kaggle) — ver
[`data/DATOS.md`](data/DATOS.md) para el detalle de cada sensor.

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab1
jupyter notebook pca_monitoreo_estructural.ipynb
```

En Windows, usa `labs\setup.ps1` y abre el notebook como se indica en [`../INSTALACION_WINDOWS.md`](../INSTALACION_WINDOWS.md).

## Notebook de referencia

`pca_monitoreo_estructural.ipynb` es un notebook completo y ejecutable de punta a punta: carga y limpia los datos,
explora estadísticas y correlaciones, aplica PCA, corre KMeans y DBSCAN, y cierra comparando ambos métodos contra
la etiqueta real. Ábrelo, ejecútalo (Run All) para ver el resultado esperado, y luego construye tu propio notebook
guiándote por las secciones siguientes y tu asistente de IA.

## Secciones y prompts sugeridos

### 1 — Contexto PCA
**Objetivo:** confirmar que el método de reducción de dimensionalidad es PCA.
**Qué debería producir tu celda:** una variable que identifique el método elegido, impresa en pantalla.
**Prompt sugerido:**
> Lab SHM (sensores estructura). Celda de solución:
> METODO_REDUCCION = "pca"
> print(f"Método elegido: {METODO_REDUCCION}")

### 2 — Carga
**Objetivo:** definir las 5 features de sensor y mostrar las primeras filas del CSV.
**Qué debería producir tu celda:** una lista con los 5 nombres exactos de columnas de sensor y una vista previa
del dataframe.
**Prompt sugerido:**
> df ya cargado desde data/building_health_monitoring_dataset.csv (1000×7).
> Columnas sensor exactas: "Accel_X (m/s^2)", "Accel_Y (m/s^2)", "Accel_Z (m/s^2)", "Strain (με)", "Temp (°C)"
> Celda de solución: lista FEATURES (5), N_FILAS_HEAD=5, print y display(df.head)

### 3 — Calidad
**Objetivo:** revisar estadísticas descriptivas de un sensor en los datos crudos.
**Qué debería producir tu celda:** un `describe()` del sensor elegido, mostrado con `display`.
**Prompt sugerido:**
> df y df_limpio ya creados arriba. Celda de solución:
> COLUMNA_REVISAR = "Strain (με)"
> stats_col = df[COLUMNA_REVISAR].describe()
> print y display

### 4 — Describe
**Objetivo:** resumen y dispersión relativa (std vs |media|) de varios sensores en `df_limpio`.
**Qué debería producir tu celda:** una tabla `describe()` y una serie de dispersión relativa ordenada.
**Prompt sugerido:**
> Usar df_limpio. Celda de solución:
> COLUMNAS_RESUMEN = ["Strain (με)", "Temp (°C)", "Accel_Z (m/s^2)"]
> resumen = df_limpio[COLUMNAS_RESUMEN].describe(); display(resumen)
> medias_abs y dispersion = std/medias_abs; display(dispersion)

### 5 — Etiquetas
**Objetivo:** mostrar el conteo de `Condition Label`.
**Qué debería producir tu celda:** una serie con el conteo por clase.
**Prompt sugerido:**
> conteo ya existe (df_limpio Condition Label). Celda de solución:
> N_CLASES_MOSTRAR = 3
> serie_clases = pd.Series(conteo).sort_index().head(N_CLASES_MOSTRAR)
> print y display

### 6 — Correlación
**Objetivo:** identificar las correlaciones más altas entre sensores en `df_limpio`.
**Qué debería producir tu celda:** los pares de sensores con mayor `|r|`, impresos.
**Prompt sugerido:**
> df_limpio y FEATURES definidos. Celda de solución:
> TOP_N_CORR = 3
> corr = df_limpio[FEATURES].corr()
> # imprimir pares con mayor |r| (sin diagonal)

### 7 — Escalado
**Objetivo:** aplicar `StandardScaler` sobre las features antes de PCA.
**Qué debería producir tu celda:** el array escalado y su forma impresa.
**Prompt sugerido:**
> Celda de solución:
> X_features = df_limpio[FEATURES].values
> scaler = StandardScaler()
> X_scaled = scaler.fit_transform(X_features)
> print shape X_scaled

### 8 — Varianza PCA
**Objetivo:** ajustar PCA y calcular la varianza explicada acumulada.
**Qué debería producir tu celda:** un PCA ajustado con `N_COMPONENTES` (entre 3 y 5) y la lista de varianza
acumulada.
**Prompt sugerido:**
> X_scaled listo. Celda de solución:
> N_COMPONENTES = 3
> pca = PCA(n_components=N_COMPONENTES)
> X_pca = pca.fit_transform(X_scaled)
> var_acum = pca.explained_variance_ratio_.cumsum().tolist()
> print varianza por componente

### 9 — Proyección 2D
**Objetivo:** graficar PC1 vs PC2 coloreado por `Condition Label`.
**Qué debería producir tu celda:** un scatter plot con leyenda de estados estructurales.
**Prompt sugerido:**
> X_pca y df_limpio disponibles. Celda de solución:
> N_COMPONENTES_2D = 2
> # scatter X_pca[:,0] vs X_pca[:,1], c=df_limpio['Condition Label']

### 10 — KMeans
**Objetivo:** método del codo y KMeans con el `k` óptimo.
**Qué debería producir tu celda:** el gráfico del codo, un `sil_km` (Silhouette) calculado, y un scatter de
clústeres.
**Prompt sugerido:**
> X_pca_input = X_scaled (o X_pca según celda previa). Celda de solución:
> K_MIN=2, K_MAX=8, K_OPT=3
> # bucle inercias, KMeans, silhouette, plots
>
> Prompt alternativo válido (misma sección, otros parámetros permitidos): K_OPT=4 si el codo lo sugiere;
> sil_km debe calcularse igual.

### 11 — DBSCAN
**Objetivo:** clustering por densidad con `eps` y `min_samples`.
**Qué debería producir tu celda:** conteo de clústeres, conteo de ruido (-1), un `sil_db` sin contar el ruido, y
un scatter.
**Prompt sugerido:**
> X_pca_input disponible. Celda de solución:
> EPS=0.7, MIN_SAMPLES=8
> dbscan fit_predict, contar clústeres y ruido (-1), silhouette sin ruido, plot

### 12 — Comparativa
**Objetivo:** calcular el Adjusted Rand Index (ARI) entre cada clustering y `Condition Label`.
**Qué debería producir tu celda:** `ari_km` y `ari_db` impresos, y una tabla/gráfico comparativo.
**Prompt sugerido:**
> Celda de solución:
> y_true = df_limpio['Condition Label'].values
> ari_km = adjusted_rand_score(y_true, labels_km)
> ari_db = adjusted_rand_score(y_true, labels_db)
> print ambos ARI

### 13 — Clasificación + loadings
**Objetivo:** entrenar un Random Forest sobre componentes PCA y encontrar el sensor con mayor peso en PC1.
**Qué debería producir tu celda:** el accuracy del clasificador sobre PCA y el nombre del sensor top en los
loadings de PC1.
**Prompt sugerido:**
> Train/test y PCA ya hechos. Celda de solución:
> N_PCA_CLF = 3
> # clasificador RF en componentes, accuracy, loadings PC1 → nombre sensor top

## Validación

No hay autoevaluación automática (✅/❌). Compara tus gráficos y métricas (varianza explicada, Silhouette, ARI)
con los del notebook de referencia y valida con tu criterio de ingeniero — la IA propone, el ingeniero valida
visualmente.

## Entrega

- Tu notebook ejecutado de punta a punta
- `prompts_entregados.md` completado
