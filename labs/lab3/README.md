# Lab 3 — Inteligencia Artificial Explicable (xAI)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ia-estructuras-diplomado/curso-ia-web/main?labpath=labs/lab3/xai_estructuras_alumno_ia.ipynb)

> **Un solo Codespace para todo el curso.** El enlace con `quickstart=1` muestra **Resume this codespace** si ya tienes uno para este repositorio; si no, **Create codespace**. Todos los labs comparten `labs/.venv`. Gestiona tus entornos en [github.com/codespaces](https://github.com/codespaces).
**Sesión 6** · Interpretar y auditar predicciones de modelos ML en contexto de ingeniería estructural.

## Enfoque del lab

Además de entrenar un **XGBoost** multiclass sobre sensores SHM, el objetivo central es **probar un kit xAI** sobre el mismo modelo — no depender de una sola técnica.

| Técnica | Alcance | Sección |
|---------|---------|---------|
| Importancia del booster | Global | 7 |
| Permutation importance | Global | 7 (pre-escrito) |
| **SHAP** (`TreeExplainer`) | Global + local | 8–9 |
| **LIME** | Local | 10 |
| **PDP** + SHAP dependence | Global marginal | 11 |

En la sección 10 se **compara LIME vs SHAP** en el mismo caso de test.

## ¿Qué es xAI?

**Inteligencia Artificial Explicable (xAI)** permite **entender por qué** un modelo produce una predicción — no solo la clase o la probabilidad.

En obra esto importa porque:

- Un modelo puede acertar por **sensores correctos** (Strain, vibración) o por **artefactos**.
- El ingeniero necesita **trazabilidad** antes de activar alertas de daño.
- xAI **apoya** la validación humana; no sustituye normativa ni inspección.

## Estado

**✅ Completo.**

| Archivo | Uso |
|---------|-----|
| `xai_estructuras_alumno_ia.ipynb` | **Única vía alumno** — guía IA + celda vacía por sección |
| `xai_estructuras_solucion.ipynb` | Referencia docente |
| `prompts_entregados.md` | Bitácora obligatoria de prompts |
| `referencia_celdas_ia.md` | **Solo docente** — código canónico por celda (✅) |
| `data/` | Dataset SHM (mismo que Lab 1) |

## Objetivos de aprendizaje

1. Diferenciar explicación **global** vs **local**.
2. Aplicar **varias técnicas xAI** sobre un mismo `XGBClassifier`.
3. Comparar **SHAP y LIME** en un caso concreto de test.
4. Interpretar resultados en lenguaje de ingeniería estructural.

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab3
jupyter notebook xai_estructuras_alumno_ia.ipynb
```

Dependencias: `xgboost`, `shap`, `lime` en [`labs/requirements.txt`](../requirements.txt).

## GitHub Codespaces

1. Pulsa el badge **Open in GitHub Codespaces** (arriba) — reanuda tu Codespace existente o crea uno nuevo.
2. Abre `labs/lab3/xai_estructuras_alumno_ia.ipynb`.
3. Kernel: **Python (curso-ia labs)** / `labs/.venv/bin/python`.

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
