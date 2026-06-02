# Lab 4: Redes Neuronales, CNN y RNN

--8<-- "lab4-actions.md"

!!! warning "En desarrollo"
    Notebook en `labs/lab4/` — próximamente vía sync desde `curso-ia-dev`.

!!! info "Sesiones 7–8"
    **Duración:** ~4 horas (previsto)

## Tema

Deep learning aplicado a señales e imágenes en ingeniería estructural:

| Arquitectura | Entrada típica | Uso en estructuras |
|--------------|----------------|-------------------|
| **CNN** | Imágenes, mapas 2D | Grietas, corrosión, humedad, daño visual |
| **RNN / LSTM** | Series temporales | Sensores SHM, deformaciones, vibración |

### Conceptos base

- Capas, neuronas, activaciones (MLP)
- Entrenamiento: loss, optimizador, epochs, batch size, overfitting
- Regularización: dropout, early stopping, validación temporal (series)

### CNN — inspección visual

- Convolución, pooling, filtros aprendidos
- Transfer learning (backbone preentrenado + cabeza de clasificación)
- Métricas: accuracy, F1, matriz de confusión

### RNN — secuencias de sensores

- RNN simple vs **LSTM** / GRU
- Ventanas deslizantes sobre acelerómetros o inclinómetros
- Train/val/test **sin fuga de futuro**

## Objetivos de aprendizaje

1. Entrenar una **MLP** simple como puente desde ML clásico.
2. Aplicar una **CNN** para clasificar imágenes de patología.
3. Aplicar **RNN/LSTM** para series de sensores.
4. Comparar ventajas y costos (datos, cómputo, interpretabilidad) frente a Lab 1–2.

## Archivos previstos

| Archivo | Uso |
|---------|-----|
| `redes_neuronales_estructuras_alumno.ipynb` | CNN + RNN guiados |
| `redes_neuronales_estructuras_solucion.ipynb` | Referencia docente |
| `_verificar.py` | Autoevaluación |
| `data/` | Imágenes y/o series documentadas |

## Pasos en Codespaces (cuando esté disponible)

1. **Crear Codespace — Lab 4** (arriba).
2. Abrir `labs/lab4/redes_neuronales_estructuras_alumno.ipynb`.

---

**¿Dudas?** → [Codespaces](codespaces.md)
