# Lab 4 — Inteligencia Artificial Explicable (xAI)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)

**Sesión 5** · Explicar modelos tabulares (XGBoost) y redes neuronales (Lab 3).

| Parte | Tema | Carpeta | Notebook |
|-------|------|---------|----------|
| **1** | xAI tabular — SHAP, LIME, PDP | [`part_1/`](part_1/) | `xai_estructuras_alumno_ia.ipynb` |
| **2** | xAI redes — Grad-CAM, Integrated Gradients | [`part_2/`](part_2/) | `xai_redes_estructuras_alumno_ia.ipynb` |

## Parte 1 — XGBoost + kit xAI

Mismo dataset SHM que Lab 1. Técnicas: importancia, permutation, SHAP, LIME, PDP.

## Parte 2 — Redes de Lab 3

Requiere checkpoints de `labs/lab3/_generar_modelos.py`. Grad-CAM en CNN de grietas; IG en ventanas LSTM.

```bash
bash labs/setup.sh
cd labs/lab4/part_1   # o part_2
```

Guía: [Lab 4 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab4/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
