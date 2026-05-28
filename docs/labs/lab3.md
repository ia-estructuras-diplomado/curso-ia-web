# Lab 3: Clustering y Señales

!!! info "📅 Sesión 6"
    **Fecha:** Martes, 16 de Junio de 2026 | **Duración:** 2 horas

## 🎯 Objetivo de Aprendizaje
Aprender a procesar series temporales dinámicas provenientes de acelerómetros, transformarlas al dominio de la frecuencia mediante la **Transformada de Fourier (FFT)**, e identificar los modos de vibración naturales de la estructura aplicando técnicas de **Clustering** no supervisado.

---

## 📊 Contexto del Problema
Cuando un puente es sometido al paso de vehículos, este vibra de acuerdo a sus propiedades dinámicas intrínsecas (frecuencias naturales y modos de vibración). Si el puente sufre una fisura importante o pérdida de tensión en un cable tensor, su rigidez disminuye, lo que provoca que sus frecuencias naturales cambien.

En este laboratorio analizaremos registros de un acelerómetro instalado en un modelo a escala de un puente colgante bajo tres condiciones físicas diferentes:
1. **Estado Sano (Normal)**: Sin daños.
2. **Estado Dañado 1**: Tensión reducida en cable tensor central.
3. **Estado Dañado 2**: Agrietamiento simulado en viga principal.

Utilizaremos FFT para extraer el espectro de potencia de cada señal y aplicaremos K-Means para clasificar de forma no supervisada los estados de salud estructural a partir de las firmas espectrales.

---

## 🛠️ Herramientas
- Python, Pandas, NumPy, SciPy (módulo `scipy.fft`)
- Scikit-learn (`KMeans`, `StandardScaler`)
- Matplotlib/Seaborn
- Jupyter Notebook

---

## 📓 Notebook del Laboratorio
El archivo `Lab3_Clustering_Senales.ipynb` incluye el siguiente flujo estructurado:

### 1. Transformación Espectral (FFT) en Python
Aprenderás a convertir la señal temporal al dominio de la frecuencia.
```python
import numpy as np
from scipy.fft import fft, fftfreq

# Señal temporal: y, Frecuencia de muestreo: fs
N = len(y)
yf = fft(y)
xf = fftfreq(N, 1/fs)[:N//2]
amplitudes = 2.0/N * np.abs(yf[0:N//2])
```

### 2. Extracción de Características (Features)
Para cada tramo de vibración, calcularemos:
- Frecuencia del primer pico dominante ($f_1$).
- Amplitud del primer pico dominante ($A_1$).
- Frecuencia del segundo pico dominante ($f_2$).
- Energía total del espectro.

### 3. Agrupamiento con K-Means
```python
from sklearn.cluster import KMeans

# X contiene las características espectrales de 100 pruebas de vibración
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)
```

---

## 📋 Tareas Prácticas

### Tarea 1: Procesamiento de Señales Temporales (45 min)
- Carga el archivo `senales_acelerometro.csv`.
- Grafica los primeros 2 segundos de vibración para cada uno de los tres estados estructurales.
- Aplica la FFT a las señales y grafica el espectro de frecuencia resultante ($0\text{ a }50\text{ Hz}$).

**Preguntas a responder:**
1. ¿Es fácil distinguir las condiciones estructurales analizando únicamente la señal en el dominio del tiempo? ¿Por qué?
2. ¿Qué diferencias observas en los picos espectrales (frecuencias) entre el estado sano y los dos estados dañados?

### Tarea 2: Extracción de Features y Clustering (45 min)
- Rellena la función en Python para extraer de manera automatizada la frecuencia y amplitud de los dos picos dominantes de cada registro de vibración.
- Normaliza los datos extraídos y ejecuta el algoritmo K-Means para agrupar los registros en 3 clústeres.

**Preguntas a responder:**
1. ¿Se alinean los clústeres identificados por K-Means con las etiquetas reales de daño?
2. ¿Existe traslape entre el clúster de daño moderado y el puente sano?

### Tarea 3: Análisis de Robustez (30 min)
- Agrega ruido blanco gaussiano simulado a las señales y verifica si K-Means sigue siendo capaz de diferenciar los tres estados o si se deteriora la clasificación.

---

## 📥 Descargas y Recursos
- [📓 Notebook de Trabajo: Lab3_Clustering_Senales.ipynb](../assets/notebooks/Lab3_Clustering_Senales.ipynb)
- [📊 Dataset: senales_acelerometro.csv](../assets/data/senales_acelerometro.csv)
- [📖 Guía Teórica de Dinámica de Estructuras (PDF)](../assets/Lab3_Vibraciones.pdf)

---

## ✅ Checklist de Completación
- [ ] Cargué los archivos de datos de aceleración.
- [ ] Implementé la FFT y grafiqué el espectro para las tres condiciones.
- [ ] Creé el dataframe de características espectrales (frecuencia, amplitud, energía).
- [ ] Entrené el algoritmo K-Means con $K=3$ y verifiqué la matriz de confusión contra etiquetas reales.
- [ ] Escribí mis conclusiones en el notebook y subí la entrega al repositorio.

---

**¿Dudas o problemas técnicos?** Escribe en el foro de discusiones de GitHub o contacta al equipo docente en: info@ia-estructuras.edu.
