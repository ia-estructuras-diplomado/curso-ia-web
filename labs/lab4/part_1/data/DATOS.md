# Dataset — Monitoreo estructural con sensores (Kaggle)

**Archivo:** `building_health_monitoring_dataset.csv`  
**Fuente:** [Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset) (Ziya07)

> Mismo dataset que **Lab 1** (PCA/clustering). En Lab 3 entrenamos un **clasificador supervisado** y lo **explicamos** con xAI.

## Contexto en obra

Registro **time-series** (1 Hz) de sensores para **Structural Health Monitoring (SHM)**. La columna `Condition Label` es el **target** de clasificación multicategoría.

| Variable | Unidad | Significado |
|----------|--------|-------------|
| `Timestamp` | fecha-hora | Marca temporal (no entra al modelo) |
| `Accel_X`, `Accel_Y`, `Accel_Z` | m/s² | Aceleración en tres ejes |
| `Strain` | με | Deformación (extensómetro) — suele dominar en daño |
| `Temp` | °C | Temperatura del sensor / ambiente |
| **`Condition Label`** | **0 / 1 / 2** | **Estado estructural (target)** |

## Etiquetas de condición

| Valor | Interpretación típica |
|-------|----------------------|
| **0** | Condición **normal** |
| **1** | **Daño menor** |
| **2** | **Daño severo** |

## Calidad de datos

- **1 000** registros crudos · **7** columnas.
- ~**96** filas con nulos en sensores → tras `dropna`: **904** muestras.
- Distribución aproximada tras limpieza: ~637 normales, ~165 daño menor, ~102 daño severo.

## Uso en Lab 3 (kit xAI + XGBoost)

1. **Clasificar** `Condition Label` con `XGBClassifier` sobre sensores escalados.
2. **Explicar** con varias técnicas sobre el **mismo modelo**:
   - **Global:** importancia del booster, permutation importance
   - **SHAP:** summary (global) y waterfall (local)
   - **LIME:** explicación local alternativa (comparar con SHAP)
   - **PDP + SHAP dependence:** efecto marginal de un sensor
3. **Validar** que las explicaciones tienen sentido físico (Strain, vibración) antes de confiar en alertas.

**Importante:** xAI explica el modelo entrenado, no la física ni la normativa. SHAP y LIME pueden coincidir o diferir — siempre revisar con criterio del ingeniero estructural.
