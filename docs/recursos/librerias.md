# Librerías Python Esenciales

## 📚 Análisis de Datos

### NumPy
**Computación numérica**

```python
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
matriz = np.zeros((3, 3))

# Operaciones
media = np.mean(arr)
std = np.std(arr)
resultado = np.dot(arr, arr.T)
```

**Documentación:** https://numpy.org

### Pandas
**Manipulación de datos**

```python
import pandas as pd

# Cargar datos
df = pd.read_csv('datos.csv')

# Exploración
print(df.head())
print(df.describe())
print(df.info())

# Limpieza
df = df.dropna()
df['columna_nueva'] = df['A'] + df['B']

# Operaciones
media = df['sensor1'].mean()
agrupado = df.groupby('estado').mean()
```

**Documentación:** https://pandas.pydata.org

## 🤖 Machine Learning

### Scikit-learn
**Algoritmos de ML clásicos**

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predicción
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
```

**Algoritmos disponibles:**
- Regresión: LinearRegression, Ridge, Lasso
- Clasificación: LogisticRegression, SVM, RandomForest, GradientBoosting
- Clustering: KMeans, DBSCAN, AgglomerativeClustering
- Reducción: PCA, TSNE

**Documentación:** https://scikit-learn.org

### TensorFlow/Keras
**Deep Learning**

```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(10,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

**Documentación:** https://tensorflow.org

## 📊 Visualización

### Matplotlib
**Gráficos estáticos**

```python
import matplotlib.pyplot as plt

# Línea
plt.plot(x, y, label='Serie 1')
plt.plot(x, y2, label='Serie 2')
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Datos de Sensores')
plt.show()

# Histograma
plt.hist(data, bins=30, edgecolor='black')

# Scatter
plt.scatter(x, y)
```

**Documentación:** https://matplotlib.org

### Plotly
**Gráficos interactivos**

```python
import plotly.express as px
import plotly.graph_objects as go

# Línea interactiva
fig = px.line(df, x='tiempo', y='sensor1', title='Datos en Tiempo Real')
fig.show()

# Heatmap
fig = go.Figure(data=go.Heatmap(z=matriz))
fig.show()

# 3D
fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='categoria')
fig.show()
```

**Documentación:** https://plotly.com

### Seaborn
**Visualización estadística**

```python
import seaborn as sns

# Heatmap de correlaciones
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Boxplot
sns.boxplot(data=df, x='categoria', y='valor')

# Distribuciones
sns.pairplot(df)
```

**Documentación:** https://seaborn.pydata.org

## 📈 Procesamiento de Señales

### SciPy
**Computación científica**

```python
from scipy import signal
from scipy.fft import fft

# FFT
frecuencias = fft(datos_temporales)

# Filtro
sos = signal.butter(4, 0.5, 'hp', output='sos')
datos_filtrados = signal.sosfilt(sos, datos)

# Windowing
ventana = signal.windows.hann(len(datos))
```

**Documentación:** https://scipy.org

## 📋 Utilidades

### Logging y Debugging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Mensaje informativo")
logger.warning("Advertencia")
logger.error("Error")
```

### Manejo de Datos Faltantes

```python
# Detectar
print(df.isnull().sum())

# Llenar
df.fillna(df.mean())

# Eliminar
df.dropna()
```

### Normalización y Escalado

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Estandarizar
scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos)

# Normalizar [0,1]
scaler = MinMaxScaler()
datos_normalizados = scaler.fit_transform(datos)
```

## 🚀 Importación Rápida

```python
# Análisis de datos
import numpy as np
import pandas as pd

# ML
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Visualización
import matplotlib.pyplot as plt
import plotly.express as px

# Procesamiento
from scipy import signal

# Setup gráficos
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)
```

## 📚 Cheat Sheets

- [NumPy Cheat Sheet](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Scikit-learn Cheat Sheet](https://scikit-learn.org/stable/user_guide.html)
- [Matplotlib Cheat Sheet](https://matplotlib.org/cheatsheets/)

---

¿Preguntas sobre librerías? Consulta [FAQ](../faq.md)
