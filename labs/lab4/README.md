# Lab 4 — Redes Neuronales, CNN y RNN

**Sesión 7–8** · Deep learning aplicado a señales e imágenes en ingeniería estructural.

## Tema del laboratorio

Introducción práctica a **redes neuronales profundas** con dos arquitecturas clave:

| Arquitectura | Entrada típica | Uso en estructuras |
|--------------|----------------|-------------------|
| **CNN** (Convolutional Neural Network) | Imágenes, mapas 2D | Grietas, corrosión, humedad, daño visual |
| **RNN / LSTM** (Recurrent Neural Network) | Series temporales | Sensores SHM, deformaciones, vibración en el tiempo |

### Redes neuronales (conceptos base)

- **Capas, neuronas y activaciones** — de perceptrón a redes multicapa (MLP).
- **Entrenamiento** — loss, optimizador, epochs, batch size, overfitting.
- **Regularización** — dropout, early stopping, validación cruzada temporal (para series).

### CNN — visión para inspección

- Convolución, pooling, filtros aprendidos.
- Transfer learning (p. ej. backbone preentrenado + cabeza de clasificación).
- Métricas: accuracy, F1, matriz de confusión en clases de daño.

### RNN — secuencias de sensores

- Memoria en el tiempo: RNN simple vs **LSTM** / GRU.
- Ventanas deslizantes sobre lecturas de acelerómetros o inclinómetros.
- Partición **train/val/test respetando el orden temporal** (sin fuga de futuro).

## Estado

**En desarrollo.**

Cuando esté listo, esta carpeta incluirá:

| Archivo | Uso |
|---------|-----|
| `redes_neuronales_estructuras_alumno.ipynb` | CNN + RNN en ejercicios guiados |
| `redes_neuronales_estructuras_solucion.ipynb` | Referencia docente |
| `redes_neuronales_estructuras_alumno_ia.ipynb` | *(al publicar)* Vía IA + `prompts_entregados.md` |
| `redes_neuronales_estructuras_solucion_ia.ipynb` | *(al publicar)* Prompts canónicos docente |
| `_verificar.py` | Autoevaluación ✅ / ❌ |
| `data/` | Imágenes de inspección y/o series de sensores documentadas |

## Objetivos de aprendizaje

1. Construir y entrenar una **MLP** simple como puente desde ML clásico.
2. Aplicar una **CNN** para clasificar imágenes de patología estructural.
3. Aplicar una **RNN/LSTM** para pronosticar o clasificar estados en series de sensores.
4. Comparar ventajas y costos (datos, cómputo, interpretabilidad) frente a Lab 1–2.

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4
jupyter notebook redes_neuronales_estructuras_alumno.ipynb
```

## GitHub Codespaces

Abrir `labs/lab4/redes_neuronales_estructuras_alumno.ipynb` (cuando esté publicado).

Guía del curso: [Lab 4 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab4/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
