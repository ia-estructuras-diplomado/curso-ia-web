# Sesión 1: Introducción a la IA en Ingeniería Civil

!!! info "📅 Programada"
    **Fecha:** Jueves, 28 de Mayo de 2026 | **Hora:** 09:00 - 12:00 | **Ubicación:** Aula Virtual

## 🎯 Objetivos

Al finalizar esta sesión, serás capaz de:

- Comprender los conceptos fundamentales de IA, Machine Learning y Deep Learning
- Conocer la evolución de métodos tradicionales en ingeniería civil
- Familiarizarte con Python y Jupyter Notebooks
- Preparar tu entorno de desarrollo

## 📚 Contenido Teórico (1 hora)

### 1. ¿Qué es Inteligencia Artificial?

**Definición:** La IA es la rama de la informática que busca crear máquinas capaces de realizar tareas que requieren inteligencia humana.

#### Subdivisiones:
- **Machine Learning (ML)**: Sistemas que aprenden de datos
- **Deep Learning (DL)**: Redes neurales artificiales
- **Data Science**: Análisis e interpretación de datos

### 2. Evolución en Ingeniería Civil

#### Métodos Tradicionales
- Análisis manual de señales de sensores
- Inspección visual de estructuras
- Cálculos simplificados y heurísticos

#### Con IA/ML
- Procesamiento automático y en tiempo real
- Análisis predictivo de daños
- Optimización de diseños
- Monitoreo continuo (SHM)

### 3. Aplicaciones Reales en Estructuras

| Aplicación | Descripción | Impacto |
|-----------|-------------|---------|
| **SHM** | Monitoreo de salud estructural | Prevención de colapsos |
| **Detección de Daños** | Identificar grietas y anomalías | Mantenimiento predictivo |
| **Digital Twins** | Réplicas digitales de estructuras | Simulación y optimización |
| **Predicción de Fallos** | Anticipar roturas | Seguridad y economía |

## 💻 Contenido Práctico (2 horas)

### 1. Configuración del Entorno

**Opción 1: Google Colab (Recomendado)**
- Gratuito, basado en la nube
- No requiere instalación
- Acceso: https://colab.research.google.com

**Opción 2: Instalación Local**
- Instala Anaconda: https://www.anaconda.com/download
- Crea un entorno: `conda create -n curso python=3.11`
- Activa: `conda activate curso`
- Instala librerías: `pip install notebook pandas numpy scikit-learn`

### 2. Primer Notebook

```python
# ¡Bienvenido a Python!
import numpy as np
import pandas as pd

# Crear un array simple
data = np.array([1, 2, 3, 4, 5])
print(f"Array: {data}")
print(f"Promedio: {np.mean(data)}")

# Crear un DataFrame
df = pd.DataFrame({
    'sensores': ['S1', 'S2', 'S3'],
    'lectura': [10.5, 11.2, 9.8]
})
print(df)
```

### 3. Herramientas Clave

#### Librerías Fundamentales

| Librería | Uso |
|----------|-----|
| **NumPy** | Cálculos numéricos y arrays |
| **Pandas** | Manipulación de datos |
| **Matplotlib** | Visualización básica |
| **Scikit-learn** | Machine Learning |

### 4. Actividad Práctica

**Taller Introductorio:**

1. **Cargar datos** de sensores simulados
2. **Explorar** la estructura de los datos
3. **Visualizar** series temporales
4. **Calcular** estadísticas básicas

## 📖 Lecturas Recomendadas

- Goodfellow et al. (2016): "Deep Learning" - Capítulo 1
- Russell & Norvig: "AI: A Modern Approach" - Introducción
- [Intro to ML - Google Developers](https://developers.google.com/machine-learning/crash-course)

## 🎤 Preguntas para Reflexionar

1. ¿Cómo podría la IA mejorar el monitoreo de tu estructura favorita?
2. ¿Qué datos necesitaría para detectar daños antes del colapso?
3. ¿Cuáles son los desafíos éticos de usar IA en seguridad estructural?

## 📝 Próximos Pasos

Antes de la **Sesión 2**:
- [ ] Instalar Python/Jupyter o crear cuenta en Google Colab
- [ ] Revisar [Sesión 2 - Big Data](sesion2.md)
- [ ] Explorar un dataset simple
- [ ] Familiarizarse con Pandas

## 📺 Recursos

- 📓 Notebook: `Sesion1_Intro_IA.ipynb` (disponible en el repositorio)
- 🔗 [Google Colab Link](https://colab.research.google.com)
- 📚 [Cheat Sheet Python](../recursos/referencias.md)

---

**Nota:** El contenido de próximas sesiones aún no está disponible públicamente. Se habilitará gradualmente después de cada sesión.
