# Lab 2: Monitoreo Estructural Inteligente

!!! info "📅 Sesión 5"
    **Fecha:** Jueves, 11 de Junio de 2026 | **Duración:** 2 horas

## 🎯 Objetivo de Aprendizaje
Aprender a implementar algoritmos de **Detección de Anomalías** para identificar estados estructurales atípicos o fallos de sensores en puentes e infraestructuras civiles utilizando datos de Monitoreo de Salud Estructural (SHM).

---

## 📊 Contexto del Problema
Una presa de hormigón está instrumentada con sensores de inclinación (inclinómetros) y temperatura. Bajo condiciones operativas normales, la inclinación de la presa varía de manera cíclica debido a las fluctuaciones de temperatura diaria y estacional (efecto térmico). 

Recientemente se sospecha de un comportamiento atípico en las juntas de expansión o de un posible fallo físico en uno de los inclinómetros. Tu objetivo es procesar las lecturas de los inclinómetros y entrenar un modelo de detección no supervisado que identifique automáticamente estas anomalías.

---

## 🛠️ Herramientas
- Python, Pandas, NumPy
- Scikit-learn (`IsolationForest`, `LocalOutlierFactor`)
- Matplotlib/Seaborn
- Jupyter Notebook

---

## 📓 Notebook del Laboratorio
El archivo `Lab2_Monitoreo_Inteligente.ipynb` contiene la siguiente estructura práctica:

### 1. Carga y Normalización de Datos
El dataset contiene: `temperatura`, `presion_hidrostatica`, e `inclinacion_sensor_1`.
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('datos_presa_shm.csv')
X = data[['temperatura', 'inclinacion_sensor_1']]

# Normalización crucial para algoritmos basados en distancias
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Entrenamiento de Isolation Forest
El algoritmo **Isolation Forest** aísla las observaciones seleccionando aleatoriamente una característica y luego seleccionando aleatoriamente un valor de división entre los valores mínimo y máximo de esa característica. Los datos anómalos requieren menos particiones para ser aislados.

```python
from sklearn.ensemble import IsolationForest

# Definimos una tasa esperada de anomalías (contamination) del 2%
model = IsolationForest(contamination=0.02, random_state=42)
data['anomaly_label'] = model.fit_predict(X_scaled)

# Las anomalías se etiquetan con -1, los datos normales con 1
data['anomaly'] = data['anomaly_label'].map({1: 'Normal', -1: 'Anomalía'})
```

---

## 📋 Tareas Prácticas

### Tarea 1: Exploración e Identificación de Patrones (30 min)
- Carga el dataset `datos_presa_shm.csv` y realiza un gráfico de dispersión (Scatter Plot) de `temperatura` vs `inclinacion_sensor_1`.
- Identifica visualmente si existen puntos dispersos fuera del patrón elíptico estándar.

**Preguntas a responder:**
1. ¿Cómo se relacionan la temperatura y la inclinación en condiciones normales?
2. ¿Qué rango térmico o de inclinación parece agrupar la mayoría de los datos normales?

### Tarea 2: Implementación de Isolation Forest (45 min)
- Entrena el modelo usando diferentes valores del parámetro `contamination` (0.01, 0.03, 0.05).
- Grafica los puntos resultantes coloreados según la etiqueta predicha (`Normal` o `Anomalía`).

**Preguntas a responder:**
1. ¿Qué efecto tiene incrementar el parámetro `contamination` en el número de falsas alarmas detectadas?
2. ¿El modelo aísla correctamente los puntos que habías identificado visualmente en la Tarea 1?

### Tarea 3: Comparación con Local Outlier Factor (LOF) (45 min)
- Implementa `LocalOutlierFactor` con `n_neighbors=20` y compara las clasificaciones con las de `IsolationForest`.
- Evalúa qué algoritmo se adapta mejor al contorno normal de los datos.

---

## 📥 Descargas y Recursos
- [📓 Notebook de Trabajo: Lab2_Monitoreo_Inteligente.ipynb](../assets/notebooks/Lab2_Monitoreo_Inteligente.ipynb)
- [📊 Dataset: datos_presa_shm.csv](../assets/data/datos_presa_shm.csv)
- [📖 Guía Teórica de SHM y Anomalías (PDF)](../assets/Lab2_Manual.pdf)

---

## ✅ Checklist de Completación
- [ ] Completé la carga de datos y grafiqué la serie de tiempo.
- [ ] Entrené el modelo `IsolationForest` y classifiqué las anomalías.
- [ ] Grafiqué y comparé los resultados de `IsolationForest` y `LOF`.
- [ ] Respondí las preguntas de análisis técnico en el notebook.
- [ ] Subí el archivo `.ipynb` resuelto a mi rama personal del repositorio.

---

**¿Dudas adicionales?** Abre un hilo en el foro del curso en GitHub o escribe a info@ia-estructuras.edu.
