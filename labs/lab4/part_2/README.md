# Lab 4 Parte 2 — LSTM en sensores SHM

**Sesión 8** · Redes recurrentes aplicadas a monitoreo estructural con series temporales.

## Tema

Entrenar una **LSTM** (PyTorch) sobre el dataset [Building Structural Health Sensor Dataset](https://www.kaggle.com/datasets/ziya07/building-structural-health-sensor-dataset) — el mismo CSV que Labs 1 y 3, pero explotando el **orden temporal**.

| Etapa | Contenido |
|-------|-----------|
| EDA | Series temporales de Strain, Accel, Temp **antes** de entrenar |
| Modelo | LSTM clasificador de `Condition Label` (0/1/2) con ventanas deslizantes |
| Tests | **Interpolación** (hueco interior en Strain) vs **extrapolación** (forecast) |

## Estado

**Parte 2** — vía IA-asistida.

| Archivo | Uso |
|---------|-----|
| `rnn_sensores_estructuras_alumno_ia.ipynb` | Notebook alumno |
| `rnn_sensores_estructuras_solucion.ipynb` | Referencia docente |
| `prompts_entregados.md` | Bitácora de prompts |
| `referencia_celdas_ia.md` | Solo docente |
| `data/archive.zip` | CSV SHM (~50 KB) |
| `_verificar.py` | Autoevaluación |

## Parte 1 vs Parte 2

| | Parte 1 (CNN) | Parte 2 (LSTM) |
|---|---------------|----------------|
| Datos | Imágenes de grietas | Sensores 1 Hz |
| EDA | Mosaico de fotos | **Gráficos de series temporales** |
| Modelo | CNN espacial | LSTM secuencial |

## Entorno

Mismo `labs/.venv` que el resto del curso. Ejecutar desde esta carpeta:

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4/part_2
jupyter notebook rnn_sensores_estructuras_alumno_ia.ipynb
```

Ver también [Parte 1 — CNN](../part_1/README.md).
