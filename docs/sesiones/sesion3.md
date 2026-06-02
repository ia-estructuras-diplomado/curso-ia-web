# Sesión 3: Aprendizaje Automático - Modelos

!!! info "📅 Programada"
    **Fecha:** Jueves, 4 de Junio de 2026 | **Hora:** 09:00 - 12:00 | **Ubicación:** Aula Virtual

## 🎯 Objetivos de la Sesión

Al finalizar esta sesión, serás capaz de:
- Distinguir entre problemas de **Aprendizaje Supervisado** y **No Supervisado** en ingeniería.
- Implementar y evaluar modelos de **Regresión** y **Clasificación**.
- Aplicar correctamente la división de datos en conjuntos de **Entrenamiento y Prueba (Train/Test Split)**.
- Diagnosticar el sobreajuste (**Overfitting**) y aplicar técnicas básicas de regularización.

---

## 📚 Contenido Teórico (1.5 horas)

### 1. Taxonomía del Machine Learning en Ingeniería
El Machine Learning se clasifica principalmente en dos grandes paradigmas según la disponibilidad de etiquetas:

```
                            ┌────────────────────────┐
                            │    Machine Learning    │
                            └───────────┬────────────┘
                                        │
                 ┌──────────────────────┴──────────────────────┐
                 ▼                                             ▼
     [Aprendizaje Supervisado]                    [Aprendizaje No Supervisado]
    (Datos etiquetados: X -> Y)                  (Solo datos de entrada: X)
      │                                            │
      ├─► Regresión (Ej. predecir carga útil)      ├─► Clustering (Ej. agrupar fallas)
      └─► Clasificación (Ej. Daño/No Daño)        └─► Detección de Anomalías (Ruido)
```

- **Ejemplo Supervisado**: Predecir el módulo de elasticidad del hormigón ($Y$) a partir de su dosificación y edad ($X$).
- **Ejemplo No Supervisado**: Agrupar registros de acelerómetros de un edificio durante un terremoto para encontrar modos de vibración naturales sin etiquetas previas.

### 2. Métricas de Evaluación de Modelos

#### Para Regresión (Predicción de valores continuos)
- **Error Cuadrático Medio (MSE)**:
  $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- **Coeficiente de Determinación ($R^2$)**: Mide la proporción de la varianza explicada por el modelo (de 0 a 1).

#### Para Clasificación (Predicción de categorías discretas)
- **Matriz de Confusión**:
  - **Verdaderos Positivos (TP)**: Estructura dañada clasificada como dañada.
  - **Falsos Negativos (FN)**: Estructura dañada clasificada como sana (**¡Crítico en ingeniería estructural!**).
- **Precision (Precisión)**: Porcentaje de predicciones positivas correctas.
- **Recall (Sensibilidad)**: Porcentaje de casos reales positivos identificados correctamente.
- **F1-Score**: Media armónica de precisión y sensibilidad.

### 3. Generalización, Overfitting y Underfitting
- **Underfitting (Subajuste)**: El modelo es demasiado simple para aprender la tendencia. Alto error en entrenamiento y prueba.
- **Overfitting (Sobreajuste)**: El modelo memoriza el ruido del conjunto de entrenamiento. Bajo error en entrenamiento, pero alto error en prueba.
- **Soluciones**: Simplificar el modelo, usar más datos, o aplicar **Regularización** (L1/Lasso, L2/Ridge) para penalizar coeficientes grandes.

---

## 💻 Contenido Práctico (1.5 horas)

En este taller utilizaremos la librería `scikit-learn` para crear un predictor del estado del hormigón.

### Código Paso a Paso: Regresión para Resistencia a la Compresión ($f'_c$)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Simulación de datos de dosificación de concreto
# Columnas: Cemento (kg), Agua (kg), Edad (días) -> Resistencia (MPa)
np.random.seed(42)
n_samples = 500
cemento = np.random.uniform(200, 450, n_samples)
agua = np.random.uniform(140, 220, n_samples)
edad = np.random.choice([3, 7, 28, 90], n_samples)
# Resistencia con cierta aleatoriedad física
resistencia = 0.12 * cemento - 0.08 * agua + 0.5 * edad + np.random.normal(0, 3, n_samples)

df = pd.DataFrame({'cemento': cemento, 'agua': agua, 'edad': edad, 'resistencia': resistencia})

# 2. Dividir datos en Características (X) y Target (y)
X = df[['cemento', 'agua', 'edad']]
y = df['resistencia']

# 3. Train/Test Split (80% entrenamiento, 20% evaluación)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenar modelo (Bosque Aleatorio / Random Forest)
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 5. Predicción y Evaluación
y_pred = modelo.predict(X_test)
print(f"R² Score del Modelo: {r2_score(y_test, y_pred):.3f}")
print(f"Error Absoluto Medio (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} MPa")
```

---

## 🔬 Laboratorio Vinculado
Esta sesión inicia el desarrollo práctico del **[Laboratorio 2](../labs/lab2.md)** (regresión UCI — hormigón), el cual debes resolver antes de la sesión de exposiciones (Sesión 4).

## 📖 Lecturas Recomendadas
- **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013)**: *An Introduction to Statistical Learning with Applications in R/Python*. Capítulo 2.
- **Documentación oficial**: [Scikit-learn Train/Test Split Guide](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
