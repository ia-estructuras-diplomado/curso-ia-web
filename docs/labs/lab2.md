# Lab 2: Monitoreo Estructural Inteligente

--8<-- "lab2-actions.md"

!!! info "Sesión 5"
    **Fecha:** Jueves, 11 de Junio de 2026 | **Duración:** ~2 horas

!!! warning "Notebook en Codespaces — próximamente"
    La guía teórica y el dataset de referencia están disponibles. El notebook interactivo (`*_alumno.ipynb`) se publicará en `labs/` cuando esté listo en el repositorio de desarrollo. Mientras tanto, puedes revisar el contexto y el dataset.

## Objetivo de aprendizaje

Implementar algoritmos de **detección de anomalías** para identificar estados estructurales atípicos o fallos de sensores en infraestructura civil (Monitoreo de Salud Estructural — SHM).

## Contexto del problema

Una presa de hormigón está instrumentada con inclinómetros y sensores de temperatura. Bajo operación normal, la inclinación varía de forma cíclica con la temperatura. Se sospecha comportamiento atípico en juntas de expansión o fallo de sensor.

Tu objetivo será procesar lecturas y entrenar un modelo **no supervisado** (Isolation Forest, LOF) que marque anomalías automáticamente.

## Pasos en Codespaces (cuando haya notebook)

1. Pulsa **Crear Codespace — Lab 2** (arriba).
2. Revisa la guía teórica abajo y el [dataset de referencia](../assets/data/datos_presa_shm.csv).
3. Cuando se publique el notebook, ábrelo en `labs/lab2/`.

## Herramientas

- Python, Pandas, NumPy
- Scikit-learn (`IsolationForest`, `LocalOutlierFactor`)
- Matplotlib / Seaborn
- Jupyter Notebook

## Flujo práctico previsto

### 1. Carga y normalización

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('datos_presa_shm.csv')
X = data[['temperatura', 'inclinacion_sensor_1']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Isolation Forest

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.02, random_state=42)
data['anomaly_label'] = model.fit_predict(X_scaled)
```

### 3. Comparación con LOF

Evaluar qué algoritmo se adapta mejor al contorno normal de los datos.

## Tareas prácticas (guía)

### Tarea 1: Exploración (30 min)
- Scatter `temperatura` vs `inclinacion_sensor_1`.
- Identificar visualmente puntos fuera del patrón.

### Tarea 2: Isolation Forest (45 min)
- Probar `contamination` en 0.01, 0.03, 0.05.
- Graficar normal vs anomalía.

### Tarea 3: LOF (45 min)
- Comparar con `LocalOutlierFactor(n_neighbors=20)`.

## Dataset de referencia

- [datos_presa_shm.csv](../assets/data/datos_presa_shm.csv) (material de apoyo en la documentación)

## Checklist

- [ ] Revisé el contexto del problema SHM
- [ ] Exploré el dataset de referencia
- [ ] *(Pendiente)* Completé el notebook en Codespaces cuando se publique

---

**¿Dudas?** → [Codespaces](codespaces.md) · info@ia-estructuras.edu
