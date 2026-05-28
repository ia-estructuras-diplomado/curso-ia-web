# Lab 1: Fundamentos de Machine Learning

!!! info "📅 Sesión 3"
    **Fecha:** Jueves, 4 de Junio de 2026 | **Duración:** 2 horas

## 🎯 Objetivo

Aprender a entrenar un modelo de Machine Learning usando datos estructurales, entendiendo cada paso del proceso: exploración, entrenamiento, evaluación e interpretación.

## 📊 Contexto del Problema

Tenemos datos de una estructura (edificio o puente) con múltiples sensores que miden:
- Desplazamiento
- Velocidad
- Aceleración
- Temperatura

**Objetivo:** Predecir el estado de salud de la estructura (Bueno/Deficiente/Crítico).

## 🛠️ Herramientas

- Python, Pandas, NumPy
- Scikit-learn
- Matplotlib/Plotly
- Jupyter Notebook

## 📓 Notebook

El notebook `Lab1_Fundamentos_ML.ipynb` contiene:

1. **Carga de datos**
   ```python
   import pandas as pd
   data = pd.read_csv('sensores_estructura.csv')
   ```

2. **Exploración (EDA)**
   - Estadísticas descriptivas
   - Visualización de distribuciones
   - Correlaciones

3. **Preparación**
   - Normalización de datos
   - Train/test split (80/20)
   - Feature selection

4. **Entrenamiento**
   - Modelo: Random Forest
   - Ajuste de hiperparámetros
   - Validación cruzada

5. **Evaluación**
   - Accuracy, Precision, Recall, F1
   - Matriz de confusión
   - Curva ROC

## 📋 Tareas Prácticas

### Tarea 1: Exploración de Datos (30 min)
- Carga el dataset
- Calcula estadísticas descriptivas
- Crea visualizaciones (histogramas, boxplots)
- Identifica outliers

**Preguntas:**
- ¿Qué variable tiene más variabilidad?
- ¿Existen correlaciones fuertes?
- ¿Hay datos faltantes?

### Tarea 2: Entrenamiento (45 min)
- Divide datos en train/test
- Entrena modelo Random Forest
- Prueba con diferentes parámetros:
  - `n_estimators`: [50, 100, 200]
  - `max_depth`: [5, 10, 15, None]
  - `min_samples_split`: [2, 5, 10]

**Experimenta:**
- ¿Cuál combinación da mejor accuracy?
- ¿Mejora la validación cruzada la confianza?
- ¿Hay overfitting?

### Tarea 3: Interpretación (30 min)
- Analiza feature importance
- Crea matriz de confusión
- Interpreta resultados reales
- Propón mejoras

**Preguntas:**
- ¿Qué sensores son más importantes?
- ¿El modelo comete errores sistemáticos?
- ¿Cómo usarías esto en una estructura real?

## 💡 Conceptos Clave

### Train/Test Split
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Normalización
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
```

### Modelo
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

### Evaluación
```python
from sklearn.metrics import accuracy_score, classification_report
pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, pred)}")
```

## 📥 Descargas

- [📓 Notebook: Lab1_Fundamentos_ML.ipynb](../assets/notebooks/Lab1_Fundamentos_ML.ipynb)
- [📊 Dataset: sensores_estructura.csv](../assets/data/sensores_estructura.csv)
- [📖 Guía PDF](../assets/Lab1_Guia.pdf)

## 🔗 Google Colab

Ejecuta directamente en la nube sin instalaciones:

[➡️ Abrir en Google Colab](https://colab.research.google.com/drive/1example)

## 📚 Lecturas Adicionales

- Scikit-learn: [Classification Tutorial](https://scikit-learn.org/stable/modules/classification.html)
- Random Forest: [Intuición](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)

## ✅ Checklist

- [ ] Descargué el notebook
- [ ] Instalé/usé entorno Python
- [ ] Ejecuté la exploración de datos
- [ ] Entrené un modelo
- [ ] Experimenté con hiperparámetros
- [ ] Interpreté los resultados
- [ ] Respondí todas las preguntas

## 🎓 Próximos Pasos

Después de este lab:
- Pasarás a Lab 2 en la Sesión 4-5
- Aplicarás estos conceptos en el Trabajo Grupal 1
- Explorarás casos más complejos

---

**¿Dudas?** Consulta [FAQ](../faq.md) o contacta a info@ia-estructuras.edu
