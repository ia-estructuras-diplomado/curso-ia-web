# Lab 4 Parte 1 — CNN para grietas en hormigón

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ia-estructuras-diplomado/curso-ia-web/main?labpath=labs/lab4/part_1/cnn_grietas_estructuras_alumno_ia.ipynb)

> **Un solo Codespace para todo el curso.** El enlace con `quickstart=1` muestra **Resume this codespace** si ya tienes uno para este repositorio; si no, **Create codespace**. Todos los labs comparten `labs/.venv`. Gestiona tus entornos en [github.com/codespaces](https://github.com/codespaces).
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

## GitHub Codespaces

1. Pulsa el badge **Open in GitHub Codespaces** (arriba) — reanuda tu Codespace existente o crea uno nuevo.
2. Abre el notebook alumno en esta carpeta.

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4/part_1
jupyter notebook cnn_grietas_estructuras_alumno_ia.ipynb
```

**Parte 2 (LSTM):** [`../part_2/README.md`](../part_2/README.md)
