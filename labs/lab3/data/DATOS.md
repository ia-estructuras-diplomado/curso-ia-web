# Dataset — Monitoreo estructural con sensores (Kaggle)

**Archivo:** `building_health_monitoring_dataset.csv`  
**Fuente:** [Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset) (Ziya07)

## Contexto en obra

Registro **time-series** (1 Hz) de sensores instalados en una estructura para **Structural Health Monitoring (SHM)**. Cada fila es una lectura instantánea de acelerómetros, extensómetro y termómetro. La columna `Condition Label` resume el estado estructural en ese instante.

| Variable | Unidad | Significado |
|----------|--------|-------------|
| `Timestamp` | fecha-hora | Marca temporal de la lectura |
| `Accel_X`, `Accel_Y`, `Accel_Z` | m/s² | Aceleración en tres ejes (vibración / movimiento) |
| `Strain` | με (microdeformación) | Deformación del material (extensómetro) |
| `Temp` | °C | Temperatura ambiente / del sensor |
| **`Condition Label`** | **0 / 1 / 2** | **Estado estructural (target para clasificación)** |

## Etiquetas de condición

| Valor | Interpretación típica |
|-------|----------------------|
| **0** | Condición **normal** — lecturas dentro de rango esperado |
| **1** | **Daño menor** — desviaciones moderadas en sensores |
| **2** | **Daño severo** — patrones de alerta (deformación/vibración elevadas) |

> En este lab usamos las etiquetas para **colorear proyecciones PCA** y comparar clasificación con features originales vs reducidos.

## Calidad de datos

- **1 000** registros · **7** columnas.
- Hay **lecturas faltantes** en sensores (~96 filas con al menos un nulo). El notebook **elimina** esas filas (estrategia pre-escrita) → **904** muestras limpias para PCA.
- Tras limpieza: ~637 normales, ~165 daño menor, ~102 daño severo.

## Por qué PCA aquí

Con 5 sensores continuos hay **redundancia parcial** (ej. ejes de aceleración correlacionados). PCA:

1. Combina sensores en **componentes principales** (PC1, PC2, …) que capturan la mayor varianza.
2. Permite **visualizar** estados en 2D/3D.
3. Reduce dimensionalidad antes de un clasificador, útil cuando hay muchos sensores o ruido.

**Importante:** PCA es **no supervisado** — no usa `Condition Label` para crear los componentes; la etiqueta solo ayuda a **interpretar** el gráfico después.
