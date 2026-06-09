# Lab 4 Parte 1 — CNN para grietas en hormigón

**Sesión 7** · Clasificación de imágenes con redes convolucionales aplicadas a inspección estructural.

## Tema

Entrenar una **CNN binaria** (PyTorch) sobre el dataset [Concrete Crack Images for Classification](https://data.mendeley.com/datasets/5y9wdsg2zt/1) (METU, CC BY 4.0):

| Clase | Significado |
|-------|-------------|
| **Negative** | Hormigón sin grieta visible |
| **Positive** | Hormigón con grieta |

## Estado

**✅ Completa.** 10 secciones: panorama CNN → EDA visual → data augmentation → entrenamiento y métricas.

| Archivo | Uso |
|---------|-----|
| `cnn_grietas_estructuras_alumno_ia.ipynb` | Notebook alumno (vía IA) |
| `cnn_grietas_estructuras_solucion.ipynb` | Referencia docente |
| `prompts_entregados.md` | Bitácora de prompts |
| `referencia_celdas_ia.md` | Solo docente |
| `data/cracks_subset.zip` | Subconjunto versionado (2 000 imágenes) |
| `data/DATOS.md` | Fuente y estructura del dataset |
| `_verificar.py` | Autoevaluación |
| `_preparar_datos.py` | Descomprime zip o regenera desde RAR local |

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4/part_1
jupyter notebook cnn_grietas_estructuras_alumno_ia.ipynb
```

**Parte 2 (LSTM):** [`../part_2/README.md`](../part_2/README.md)
