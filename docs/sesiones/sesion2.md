# Sesión 2: Casos Reales y Big Data

!!! info "📅 Programada"
    **Fecha:** Martes, 2 de Junio de 2026 | **Hora:** 09:00 - 12:00 | **Ubicación:** Aula Virtual

## 🎯 Objetivos de la Sesión

Al finalizar esta sesión, serás capaz de:
- Comprender los fundamentos de **Big Data** y su relevancia en la ingeniería estructural moderna.
- Identificar los componentes clave de un sistema de **Monitoreo de Salud Estructural (SHM)**.
- Diferenciar los tipos de sensores utilizados en estructuras y sus características de adquisición de datos.
- Cargar, limpiar y analizar de forma exploratoria datos provenientes de sensores usando Python.

---

## 📚 Contenido Teórico (1.5 horas)

### 1. ¿Qué es Big Data en Ingeniería Civil?
En el ámbito de las estructuras, Big Data se refiere a la recopilación masiva de datos generados por sensores instalados en obras civiles (puentes, presas, rascacielos). Estos datos cumplen con las "V" clásicas del Big Data:
- **Volumen**: Gigabytes de registros continuos por día.
- **Velocidad**: Frecuencias de muestreo altas (ej. acelerómetros a 100 Hz).
- **Variedad**: Combinación de señales de aceleración, deformación, temperatura, y registros climáticos.
- **Veracidad**: Desafíos en la calibración y el ruido de las lecturas.

### 2. Monitoreo de Salud Estructural (SHM - Structural Health Monitoring)
El SHM es el proceso de implementar una estrategia de detección de daños para la infraestructura de ingeniería civil. Consiste en:
1. **Adquisición**: Sensores y sistemas de digitalización.
2. **Transmisión**: Redes cableadas o inalámbricas (IoT).
3. **Procesamiento y Gestión**: Almacenamiento y normalización.
4. **Evaluación de Diagnóstico**: Algoritmos de Machine Learning para estimar la vida útil, detectar fallas y predecir mantenimientos.

```
       [Estructura Real] 
               │
               ▼  (Monitoreo Continuo)
         [Sensores] (Acelerómetros, Deformímetros, etc.)
               │
               ▼  (Adquisición a alta frecuencia)
       [Procesamiento Data] (Limpieza de Ruido, Filtros)
               │
               ▼  (Machine Learning)
      [Estado de la Estructura] (Diagnóstico / Alerta)
```

### 3. Tipos de Sensores en Ingeniería Estructural
- **Acelerómetros**: Miden vibraciones dinámicas causadas por sismos, tráfico o viento.
- **Deformímetros (Strain Gauges)**: Registran la deformación unitaria micro-strain ($\mu\epsilon$) en vigas o columnas bajo cargas estáticas o dinámicas.
- **Inclinómetros (Tiltmeters)**: Miden la variación angular o rotaciones en apoyos de puentes o muros de contención.
- **Termocuplas**: Monitorean los gradientes térmicos que producen dilataciones estructurales.

---

## 💻 Contenido Práctico (1.5 horas)

En esta práctica realizaremos un **Análisis Exploratorio de Datos (EDA)** con registros reales de un puente instrumentado. 

### 1. Concepto de Frecuencia de Muestreo ($f_s$)
Si un acelerómetro registra a $100\text{ Hz}$, significa que toma **100 lecturas por segundo**. Para un día completo, un solo canal genera:
$$\text{Lecturas por día} = 100 \times 60 \times 60 \times 24 = 8,640,000\text{ registros}$$

### 2. Ejemplo Práctico de Carga y Limpieza en Python
Aprenderemos a detectar registros nulos (outliers) y a alinear series de tiempo bajo variaciones de temperatura.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar dataset de sensores de deformación (micro-strain) y temperatura
df = pd.read_csv('datos_puente.csv', parse_dates=['timestamp'])
df.set_index('timestamp', inplace=True)

# 1. Identificar datos faltantes
print("Valores nulos por columna:")
print(df.isnull().sum())

# 2. Filtrar Outliers mediante desviación estándar (Filtro Z-score)
mean_val = df['sensor_deformacion'].mean()
std_val = df['sensor_deformacion'].std()
df_clean = df[np.abs(df['sensor_deformacion'] - mean_val) <= (3 * std_val)]

# 3. Graficar correlación entre temperatura y deformación
plt.figure(figsize=(10, 5))
plt.scatter(df_clean['temperatura'], df_clean['sensor_deformacion'], alpha=0.5, color='teal')
plt.title('Correlación: Temperatura vs Deformación en Apoyo de Puente')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Deformación ($\mu\epsilon$)')
plt.grid(True)
plt.show()
```

---

## 📖 Lecturas Recomendadas y Material
- **Farrar, C. R., & Worden, K. (2012)**: *Structural Health Monitoring: A Machine Learning Perspective*. John Wiley & Sons.
- **Lectura**: [Introduction to Structural Health Monitoring (SHM)](https://www.sciencedirect.com/topics/engineering/structural-health-monitoring)
- **Notebook**: `Sesion2_BigData_Puentes.ipynb` (disponible en `/assets/notebooks/`)

---

## 📝 Actividades antes de la Sesión 3
- [ ] Asegurarse de tener instalado `matplotlib` y `seaborn` en tu entorno de Python.
- [ ] Descargar el dataset `datos_puente.csv` de la carpeta de recursos.
- [ ] Revisar el concepto de **Regresión Lineal** (ya que lo aplicaremos para modelar el efecto térmico en la Sesión 3).
