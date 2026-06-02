# Sesión 5: Procesamiento de Señales y Clústeres

!!! info "📅 Programada"
    **Fecha:** Jueves, 11 de Junio de 2026 | **Hora:** 09:00 - 12:00 | **Ubicación:** Aula Virtual

## 🎯 Objetivos de la Sesión

Al finalizar esta sesión, serás capaz de:
- Comprender el flujo de trabajo para procesar señales dinámicas provenientes de sensores de vibración.
- Aplicar la **Transformada Rápida de Fourier (FFT)** para pasar del dominio del tiempo al de la frecuencia.
- Implementar algoritmos de **Clustering** (como K-Means y DBSCAN) para agrupar comportamientos estructurales.
- Detectar anomalías operacionales o fallas estructurales a partir de vibración no supervisada.

---

## 📚 Contenido Teórico (1.5 horas)

### 1. El Dominio del Tiempo vs. Dominio de la Frecuencia
Los sensores de aceleración instalados en puentes o edificios registran señales en el **dominio del tiempo** (aceleración vs. segundo). Sin embargo, las propiedades físicas de una estructura (rigidez y masa) se manifiestan de forma clara en el **dominio de la frecuencia**.

```
    Señal de Sensor (Tiempo)            Transformada de Fourier (FFT)          Espectro de Frecuencia
     Aceleración (g)                         ┌───────────┐                         Amplitud
        │   /\    /\                         │           │                            │       /\
        │  /  \  /  \                        │    FFT    │  ────────────────────────► │      /  \
        │ /    \/    \                       │           │                            │     /    \  /\
      ──┴───────────────► Tiempo             └───────────┘                            └────┴──────┴──┴──► Frecuencia (Hz)
```

La **Transformada Rápida de Fourier (FFT)** descompone una señal temporal compleja en sus frecuencias constituyentes, identificando las **frecuencias naturales o modos de vibración** de la estructura. Un cambio repentino en estas frecuencias naturales suele indicar una pérdida de rigidez (es decir, daño estructural).

### 2. Algoritmos de Aprendizaje No Supervisado: Clustering
El agrupamiento o clustering busca organizar conjuntos de datos en grupos (clústeres) cuyos elementos son similares entre sí y diferentes a los de otros grupos.

#### A. K-Means
- **Funcionamiento**: Divide el espacio en un número predefinido $K$ de clústeres. Asigna puntos al centroide más cercano e itera recalculando los centroides.
- **Ventaja**: Rápido y escalable.
- **Desventaja**: Sensible a outliers y requiere definir $K$ de antemano (usando el método del codo o coeficiente de silueta).

#### B. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **Funcionamiento**: Agrupa puntos basándose en la densidad de vecindad (parámetros `eps` y `min_samples`).
- **Ventaja**: No requiere predefinir el número de clústeres y detecta automáticamente outliers (clasificándolos como "ruido").
- **Aplicación en SHM**: Ideal para detectar lecturas anormales de sensores que no encajan con los estados operativos estándar.

---

## 💻 Contenido Práctico (1.5 horas)

En esta práctica aprenderemos a aplicar FFT a una señal de acelerómetro simulada y a agrupar los picos espectrales utilizando K-Means.

### Código Paso a Paso: Análisis Espectral y Clustering

```python
import numpy as np
import pandas as pd
from scipy.fft import fft, fftfreq
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Simulación de una señal dinámica (Vibración del puente)
# Dos frecuencias predominantes (modos estructurales a 5 Hz y 12 Hz) más ruido
fs = 100.0  # Frecuencia de muestreo: 100 Hz
t = np.arange(0, 10, 1/fs)  # 10 segundos
vibracion = 2.0 * np.sin(2 * np.pi * 5.0 * t) + 1.5 * np.sin(2 * np.pi * 12.0 * t) + np.random.normal(0, 1.0, len(t))

# 2. Aplicar Transformada Rápida de Fourier (FFT)
N = len(t)
y_fft = fft(vibracion)
xf = fftfreq(N, 1/fs)[:N//2]
yf = 2.0/N * np.abs(y_fft[0:N//2])

# 3. Clustering para identificar frecuencias predominantes (K-Means)
# Extraemos los puntos con mayor amplitud para agruparlos
picos = pd.DataFrame({'frecuencia': xf, 'amplitud': yf})
picos_significativos = picos[picos['amplitud'] > 0.3]

# Agrupar las frecuencias de los picos en 2 clústeres principales
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
picos_significativos['cluster'] = kmeans.fit_predict(picos_significativos[['frecuencia']])

# 4. Visualizar Espectro y Clústeres
plt.figure(figsize=(10, 5))
colors = ['red', 'blue']
for cluster_id in [0, 1]:
    sub = picos_significativos[picos_significativos['cluster'] == cluster_id]
    plt.scatter(sub['frecuencia'], sub['amplitud'], label=f'Modo Estructural {cluster_id + 1}', s=100, color=colors[cluster_id])

plt.plot(xf, yf, color='gray', alpha=0.5, label='Espectro FFT')
plt.title('Identificación de Modos Estructurales Mediante FFT y Clustering')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🔬 Laboratorio Vinculado
Esta sesión sienta las bases teóricas y de código para el **[Laboratorio 1 — PCA y SHM](../labs/lab1.md)** y el desarrollo del **Trabajo Grupal 2 (T2)**.

## 📖 Lecturas Recomendadas
- **Oppenheim, A. V., & Schafer, R. W. (2009)**: *Discrete-Time Signal Processing*. Prentice Hall.
- **Clustering Tutorial**: [Scikit-learn Clustering Overview](https://scikit-learn.org/stable/modules/clustering.html)
