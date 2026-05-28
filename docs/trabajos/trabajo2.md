# Trabajo Grupal 2: Clustering y Procesamiento de Señales

!!! info "📅 Evaluación 2"
    **Sesión:** 7 | **Fecha:** Jueves, 18 de Junio de 2026 | **Peso:** 30%

## 🎯 Objetivo del Proyecto
Aplicar de manera práctica el procesamiento de señales en el dominio de la frecuencia y técnicas de aprendizaje no supervisado (Clustering) para clasificar dinámicamente firmas de vibración en puentes o edificios e identificar de forma autónoma anomalías de rigidez.

---

## 📊 Contexto del Problema
Cada grupo recibirá un dataset que contiene registros continuos de vibración dinámica en formato de series temporales de 100 pruebas de carga. Algunos registros pertenecen al puente en su condición original sana, otros corresponden a desgaste en soportes fijos, y un porcentaje representa fisuras estructurales iniciales. 

**Tu tarea:**
1. Filtrar las señales de vibración y convertirlas al dominio de la frecuencia mediante la FFT.
2. Extraer características espectrales representativas (frecuencias, amplitudes, distribución de potencia).
3. Entrenar y comparar dos algoritmos de clustering (K-Means y DBSCAN) para identificar las firmas de daño sin etiquetas previas.

---

## 📋 Entregables Requeridos

### 1. Presentación Técnica (12-15 minutos)
- **Introducción**: Contexto físico y objetivos.
- **Procesamiento de Señales**: Explicación de los filtros y la FFT aplicada.
- **Ingeniería de Características**: Selección de features.
- **Modelación y Comparativa**: Resultados e interpretaciones físicas.
- **Conclusiones y Recomendaciones de Ingeniería**.

### 2. Notebook Jupyter (.ipynb)
Código estructurado y reproducible que realice:
- Carga y visualización de la señal en tiempo.
- Procesamiento espectral (FFT) y gráficos espectrales.
- Extracción automatizada de variables.
- Ejecución de clustering, evaluación del número óptimo de grupos (método del codo/silueta).
- Visualización interactiva de los clústeres en 2D o 3D.

### 3. Reporte Ejecutivo (3-4 páginas)
- **Metodología**: Flujo de análisis y algoritmos seleccionados.
- **Resultados**: Análisis comparativo de los algoritmos y métricas de clustering (Silhouette Score).
- **Interpretación Física**: Qué significan los clústeres en términos de salud estructural del puente.

---

## ✅ Requisitos Técnicos y Checklist
- [ ] Cargar las señales y aplicar un filtro digital (opcional: pasa-banda o Butterworth) para remover ruido de alta frecuencia.
- [ ] Aplicar FFT y visualizar el espectro para varios tramos de la señal.
- [ ] Extraer al menos 4 características espectrales por tramo de vibración.
- [ ] Escalar las características (StandardScaler o MinMaxScaler).
- [ ] Entrenar K-Means probando de 2 a 6 clústeres y reportar el coeficiente de silueta.
- [ ] Entrenar DBSCAN y optimizar el parámetro `eps` y `min_samples` para identificar outliers.
- [ ] Comparar K-Means vs DBSCAN: ¿Cuál fue más efectivo para separar el puente sano de las condiciones de daño?
- [ ] Interpretar los centroides físicamente.

---

## 🎓 Rúbrica de Evaluación

| Criterio | Excelente (4.5 - 5.0) | Muy Bueno (4.0 - 4.4) | Bueno (3.5 - 3.9) | Satisfactorio (3.0 - 3.4) | Insuficiente (< 3.0) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Comprensión Conceptual (30%)** | Explican la teoría de la FFT y el clustering con rigor físico-matemático impecable. | Demuestran buen entendimiento físico de la FFT y los algoritmos. | Comprensión sólida pero con explicaciones físicas superficiales. | Errores conceptuales menores al definir clustering o espectros. | Graves malentendidos conceptuales sobre FFT o clustering. |
| **Aplicación Práctica (40%)** | Implementan filtros de señal, extraen features con robustez y optimizan los hiperparámetros. | Implementación correcta de FFT y clustering. Código limpio. | Código ejecutable pero sin filtros de ruido o baja optimización. | Implementación con errores en escalamiento de datos o FFT. | Código no ejecutable o con errores de cálculo graves. |
| **Comunicación y Reporte (20%)** | Presentación e informe con gráficos profesionales de alta calidad. Código autodocumentado. | Presentación y reporte claros y bien redactados. | Presentación correcta, pero el reporte carece de rigor formal. | Explicación poco clara de gráficos y tablas. | Presentación confusa y reporte incompleto. |
| **Pensamiento Crítico (10%)** | Analizan a fondo las limitaciones del modelo, falsas alarmas y viabilidad industrial. | Identifican limitaciones clave del análisis espectral. | Comentarios críticos generales sobre el ruido de los sensores. | Escaso análisis crítico de los resultados obtenidos. | Nula interpretación crítica de los datos. |

---

**Soporte de Proyectos**: Utiliza el foro del curso en GitHub para consultas técnicas sobre procesamiento espectral en Python.
