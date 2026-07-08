# Dataset — Monitoreo estructural SHM (Kaggle)

**Archivo:** `building_health_monitoring_dataset.csv` (dentro de `archive.zip`)  
**Fuente:** [Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset) (Ziya07)

> Mismo dataset que **Lab 1** (PCA) y **Lab 3** (xAI). En Lab 4 Parte 2 usamos **series temporales** y **LSTM**.

## Columnas

| Variable | Unidad | Significado |
|----------|--------|-------------|
| `Timestamp` | fecha-hora | Marca temporal (1 Hz) — ordena la serie |
| `Accel_X`, `Accel_Y`, `Accel_Z` | m/s² | Aceleración en tres ejes |
| `Strain` | με | Deformación (extensómetro) |
| `Temp` | °C | Temperatura |
| **`Condition Label`** | **0 / 1 / 2** | **Estado estructural (target)** |

## Etiquetas

| Valor | Interpretación |
|-------|----------------|
| **0** | Saludable (Healthy) |
| **1** | Daño menor (Minor Damage) |
| **2** | Daño severo (Severe Damage) |

## Calidad

- **1 000** registros crudos · **7** columnas.
- Tras `dropna` en sensores: **904** lecturas válidas.
- Split en Parte 2: **temporal** (80 % train / 20 % val) — sin barajar el tiempo.

## Uso en Lab 4 Parte 2

1. **EDA** con gráficos de series temporales (antes de entrenar).
2. **LSTM** clasificador con ventanas deslizantes sobre 5 sensores.
3. **Tests** de interpolación y extrapolación sobre `Strain`.
