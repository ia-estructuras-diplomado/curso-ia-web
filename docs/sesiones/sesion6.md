# Sesión 6: Futuro de los Modelos y Tendencias

!!! info "📅 Programada"
    **Fecha:** Martes, 16 de Junio de 2026 | **Hora:** 09:00 - 12:00 | **Ubicación:** Aula Virtual

## 🎯 Objetivos de la Sesión

Al finalizar esta sesión, serás capaz de:
- Definir el concepto de **Digital Twin (Gemelo Digital)** y su aplicación en la gestión del ciclo de vida de infraestructuras.
- Explicar la integración de sensores e inteligencia artificial en la conceptualización de **Smart Cities**.
- Diferenciar metodologías de **Aprendizaje Paramétrico** frente a **No Paramétrico**.
- Evaluar comparativamente el rendimiento de algoritmos paramétricos (como Regresión Logística) y no paramétricos (como K-Nearest Neighbors).

---

## 📚 Contenido Teórico (1.5 horas)

### 1. Digital Twins (Gemelos Digitales)
Un **Gemelo Digital** es una representación virtual dinámica de una estructura física (como un puente o una presa) que se actualiza continuamente mediante datos de sensores en tiempo real (SHM) y simulaciones de ingeniería (Método de Elementos Finitos - FEM).

```
  ┌──────────────────────┐                     ┌──────────────────────┐
  │   Estructura Física  │  ───[Datos IoT]───► │    Digital Twin      │
  │  (Puente instrumentado)│  ◄──[Optimización]──│  (Modelo Predictivo) │
  └──────────────────────┘                     └──────────────────────┘
```

A diferencia de un modelo CAD estático, un Gemelo Digital:
- **Aprende y se adapta**: Modifica sus parámetros mecánicos virtuales según las deformaciones observadas.
- **Predice fallos**: Simula escenarios destructivos virtuales (sismos, sobrecarga extrema) para calcular factores de seguridad actualizados en tiempo real.

### 2. Smart Cities e Infraestructura Conectada
El concepto de Ciudades Inteligentes se basa en la interconectividad de la infraestructura civil para optimizar la movilidad, la seguridad estructural y la gestión de recursos. La IA actúa como el cerebro que procesa datos distribuidos (GIS + IoT) para automatizar decisiones urbanas, como la alerta temprana ante fallos estructurales en redes de transporte o acueductos.

### 3. Aprendizaje Paramétrico vs. No Paramétrico
Al entrenar modelos de Machine Learning, podemos clasificar los algoritmos en dos filosofías:

#### A. Aprendizaje Paramétrico
- **Definición**: Asume una forma matemática específica (lineal, logística, etc.) para la relación entre las variables de entrada y salida. Reduce el problema a la estimación de un conjunto fijo de parámetros (pesos o coeficientes).
- **Ejemplos**: Regresión Lineal, Regresión Logística, Análisis Discriminante Lineal.
- **Pros**: Rápido de entrenar, requiere pocos datos, altamente interpretable.
- **Contras**: Si la forma asumida es incorrecta, el modelo tendrá sesgo alto.

#### B. Aprendizaje No Paramétrico
- **Definición**: No asume una forma funcional fija. El modelo ajusta libremente su complejidad para adaptarse a la distribución de los datos de entrenamiento.
- **Ejemplos**: Árboles de Decisión, Random Forest, K-Nearest Neighbors (KNN), Redes Neuronales Artificiales.
- **Pros**: Altamente flexible, capaz de modelar relaciones complejas y no lineales.
- **Contras**: Propenso al sobreajuste, requiere un volumen de datos significativamente mayor, menor interpretabilidad ("caja negra").

---

## 💻 Contenido Práctico (1.5 horas)

En esta práctica realizaremos una comparación de rendimiento entre un modelo paramétrico (Regresión Logística) y uno no paramétrico (K-Nearest Neighbors - KNN) para predecir si una columna requiere refuerzo estructural.

### Código Paso a Paso: Paramétrico vs. No Paramétrico

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Simulación de datos de columnas de hormigón armado
# Características: Carga axial aplicada (kN), Desviación geométrica (mm)
# Target: Requiere Refuerzo (1: Sí, 0: No)
np.random.seed(123)
n_samples = 400
carga_axial = np.random.uniform(500, 3000, n_samples)
desviacion = np.random.uniform(0, 50, n_samples)

# Condición no lineal de fallo (ej. pandeo excéntrico)
fallo_line = 0.015 * carga_axial + 0.6 * desviacion + (carga_axial * desviacion * 0.001)
requiere_refuerzo = (fallo_line > 45).astype(int)

df = pd.DataFrame({'carga': carga_axial, 'desviacion': desviacion, 'refuerzo': requiere_refuerzo})

X = df[['carga', 'desviacion']]
y = df['refuerzo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Modelo Paramétrico: Regresión Logística
modelo_param = LogisticRegression()
modelo_param.fit(X_train, y_train)
y_pred_param = modelo_param.predict(X_test)

# 3. Modelo No Paramétrico: KNN (k=5)
modelo_no_param = KNeighborsClassifier(n_neighbors=5)
modelo_no_param.fit(X_train, y_train)
y_pred_no_param = modelo_no_param.predict(X_test)

# 4. Comparar Resultados
print("--- MODELO PARAMÉTRICO (Regresión Logística) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred_param):.3f}")
print("--- MODELO NO PARAMÉTRICO (K-Nearest Neighbors) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred_no_param):.3f}")
```

---

## 🔬 Laboratorio Vinculado
Esta sesión sienta las bases conceptuales para completar el **[Laboratorio 3 — xAI](../labs/lab3.md)** y la modelación final del **Trabajo Grupal 3 (T3)**.

## 📖 Lecturas Recomendadas
- **Sacks, J., Welch, W. J., Mitchell, T. J., & Wynn, H. P. (1989)**: *Design and Analysis of Computer Experiments*. Statistical Science, 4(4), 409-423. (Fundacional para Gemelos Digitales).
- **Lectura**: [Parametric vs Nonparametric Models - Machine Learning](https://machinelearningmastery.com/parametric-and-nonparametric-machine-learning-algorithms/)
