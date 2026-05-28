# Trabajo Grupal 3: Integración Avanzada y Digital Twins

!!! info "📅 Evaluación Final"
    **Sesión:** 8 | **Fecha:** Martes, 23 de Junio de 2026 | **Peso:** 40%

## 🎯 Objetivo del Proyecto
Desarrollar una solución integral de Machine Learning aplicada a un caso real de ingeniería civil, estructurando conceptualmente un **Digital Twin (Gemelo Digital)** que incorpore un pipeline predictivo automatizado, optimización de hiperparámetros y toma de decisiones operativas.

---

## 📊 Contexto del Problema
Cada grupo elegirá uno de los siguientes proyectos de aplicación práctica basado en datos de simulación y monitoreo real:

1. **Predicción Sísmica de Edificios**: Estimar la deriva máxima de entrepiso en un edificio de gran altura ante diferentes acelerogramas sísmicos.
2. **Degradación de Cables en Puentes**: Modelar la pérdida de tensión a largo plazo en los tirantes de un puente atirantado debido a fatiga y corrosión.
3. **Optimización de Cimentaciones**: Predecir el asentamiento final de zapatas en suelos arcillosos complejos a partir de ensayos de penetración estándar (SPT).

**Tu tarea:**
- Diseñar el pipeline completo de Machine Learning (Limpieza, Feature Engineering, Modelación y Optimización).
- Implementar y comparar críticamente modelos paramétricos y no paramétricos.
- Proponer el esquema arquitectónico de un **Gemelo Digital** detallando cómo se actualizaría el modelo predictivo con datos de campo continuos.

---

## 📋 Entregables Requeridos

### 1. Presentación Final Profesional (15-20 minutos)
- **Definición del Problema**: Importancia física y económica.
- **Arquitectura de Datos**: Preprocesamiento y variables sintéticas creadas.
- **Modelación y Búsqueda de Hiperparámetros**: Comparativa de los modelos entrenados.
- **Propuesta de Gemelo Digital**: Diagrama conceptual de flujos de datos.
- **Impacto Práctico**: Cómo usará la constructora o el operador esta herramienta para prevenir fallos.

### 2. Notebook Jupyter de Producción
Código robusto, modularizado (mediante funciones) y documentado:
- Pipeline de preprocesamiento usando clases de `scikit-learn`.
- Búsqueda sistemática de hiperparámetros (`GridSearchCV` o `RandomizedSearchCV`).
- Comparación de al menos tres modelos (ej. Regresión Lasso, Random Forest, XGBoost).
- Gráficos de análisis de residuos y de importancia de características.

### 3. Reporte Final Completo (4-5 páginas)
Redacción formal en formato de paper científico corto:
- Portada e Introducción.
- Metodología del Pipeline e Hiperparámetros.
- Discusión Detallada de Resultados (Tablas comparativas, métricas de error).
- Diseño Conceptual del Gemelo Digital (Flujo de datos físico-virtual).
- Conclusiones y Trabajo Futuro.

---

## ✅ Requisitos Técnicos y Checklist
- [ ] Implementar un preprocesador completo con imputación y escalamiento.
- [ ] Entrenar al menos un modelo paramétrico y dos no paramétricos.
- [ ] Aplicar validación cruzada (`K-Fold Cross-Validation`) para reportar métricas robustas.
- [ ] Utilizar ajuste sistemático de hiperparámetros (Grid Search).
- [ ] Graficar la comparación de métricas ($R^2$, RMSE, MAE) en el set de testeo.
- [ ] Analizar los residuos del mejor modelo ($y_{test} - y_{pred}$) para verificar sesgos.
- [ ] Diseñar y adjuntar en el reporte un esquema conceptual de la arquitectura del **Digital Twin** (captura de sensores -> API -> modelo ML -> actualización de simulación FEM -> panel de control).

---

## 🎓 Rúbrica de Evaluación Final

| Criterio | Excelente (4.5 - 5.0) | Muy Bueno (4.0 - 4.4) | Bueno (3.5 - 3.9) | Satisfactorio (3.0 - 3.4) | Insuficiente (< 3.0) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Comprensión Conceptual (30%)** | Integración conceptual impecable entre la teoría de IA y la mecánica de estructuras. Planteamiento sólido del Gemelo Digital. | Comprensión completa de los modelos comparados y del flujo del Gemelo Digital. | Entendimiento general de los algoritmos pero con debilidad en el flujo interactivo del Gemelo Digital. | Dificultades al justificar la elección de métricas de validación o algoritmos. | Errores conceptuales graves en la formulación de los modelos. |
| **Aplicación Práctica (40%)** | Código modular limpio. Uso correcto de Cross-Validation y Grid Search. Análisis de residuos riguroso. | Pipeline correcto con validación de datos e hiperparámetros ajustados. | Modelos entrenados correctamente pero sin validación cruzada robusta o sin búsqueda formal de parámetros. | Código con errores menores o baja eficiencia de ejecución en preprocesamiento. | Código que no compila, con filtración de datos (data leakage) o errores severos. |
| **Comunicación y Reporte (20%)** | Reporte escrito formal con estructura científica sobresaliente. Presentación oral dinámica y profesional. | Informe completo bien estructurado y código bien documentado. | Reporte con algunos vacíos de contenido o gráficos mal etiquetados. | Presentación poco clara o reporte que carece de secciones principales. | Entrega incompleta de reportes o código indocumentado. |
| **Pensamiento Crítico (10%)** | Discusión brillante sobre el sesgo del modelo, representatividad de datos y desafíos de implementación en obra. | Análisis adecuado del comportamiento físico del modelo y sus límites de predicción. | Comentarios críticos sobre el rendimiento de los modelos sin profundizar en la física del problema. | Nulo análisis de errores o sesgos de los modelos. | No identifican las limitaciones de su modelo frente a casos reales. |

---

**Cierre del Diplomado**: Mucho éxito en su entrega final. Para consultoría de proyectos, agendar horas de asesoría con el coordinador docente.
