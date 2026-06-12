#!/usr/bin/env bash
set -euo pipefail
cd /home/kurt-asus/curso-ia-web

echo "→ docs/index.md"
cat > docs/index.md << 'EOF'
# Inteligencia Artificial para Ingeniería Civil

# 🚀 Diplomado en IA Aplicada a Estructuras

Desarrolla habilidades prácticas en Machine Learning y Ciencia de Datos para diagnosticar, optimizar y monitorear la salud estructural de obras civiles.

**Mayo – Junio 2026 · 8 sesiones · Enfoque práctico**

[Explorar laboratorios](labs/index.md){ .md-button .md-button--primary }
[Crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json){ .md-button }
[Syllabus](curso/syllabus.md){ .md-button }

## Sobre el curso

Introducción a la **IA aplicada a Ingeniería Civil** con datos reales de sensores, Big Data, Machine Learning, Digital Twins y procesamiento de señales (SHM). Enfoque en **decisiones informadas**, no en programar algoritmos desde cero.

## Cronograma

8 sesiones los **martes y jueves** desde el **28 de mayo de 2026**.

| Sesión | Fecha | Tema teórico | Lab / entregable |
|:------:|:------|:-------------|:-----------------|
| **1** | Jue 28 May | Introducción a IA en Ing. Civil | [Lab 0](labs/lab0.md) |
| **2** | Mar 02 Jun | Big Data, PCA, K-Means, anomalías (DBSCAN / Isolation Forest) | [Lab 1](labs/lab1.md) |
| **3** | Jue 04 Jun | Regresión vs clasificación, RF, SVM, validación y métricas | [Lab 2](labs/lab2.md) |
| **4** | Mar 09 Jun | xAI (SHAP, LIME), presentaciones grupales | [Lab 3](labs/lab3.md) · **T1 (30%)** |
| **5** | Jue 11 Jun | ANN, CNN, transfer learning, RNN/LSTM | [Lab 4](labs/lab4.md) |
| **6** | Mar 16 Jun | Gemelos digitales, Transformers, RAG | [Lab 5](labs/lab5.md) |
| **7** | Jue 18 Jun | Agentes, MCP, Agentic AI | [Lab 6](labs/lab6.md) · **T2 (30%)** |
| **8** | Mar 23 Jun | PINNs, roadmap de adopción, cierre | **T3 (40%)** |

## Calificación

$$NF = 0.30 \times T1 + 0.30 \times T2 + 0.40 \times T3$$

Detalle en [Calificación](curso/calificacion.md) y [Trabajos grupales](trabajos/guia.md).

---

¿Dudas? → [FAQ](faq.md)
EOF

echo "→ docs/labs/index.md"
cat > docs/labs/index.md << 'EOF'
# Laboratorios

Notebooks en [`labs/`](https://github.com/ia-estructuras-diplomado/curso-ia-web/tree/main/labs), sincronizados desde `curso-ia-dev`.

[Crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json){ .md-button .md-button--primary }

## Labs disponibles

| Lab | Tema | Guía | Notebook |
|:---:|:-----|:-----|:---------|
| **0** | Python para IA | [Lab 0](lab0.md) | [📓 Manual](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab0/fundamentos_python_ia_alumno.ipynb) · [🤖 IA](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab0/fundamentos_python_ia_alumno_ia.ipynb) |
| **1** | PCA, KMeans, DBSCAN (SHM) | [Lab 1](lab1.md) | [📓 Manual](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/pca_monitoreo_estructural_alumno.ipynb) · [🤖 IA](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/pca_monitoreo_estructural_alumno_ia.ipynb) |
| **2** | Resistencia hormigón (UCI) | [Lab 2](lab2.md) | [📓 Manual](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab2/resistencia_compresion_alumno.ipynb) · [🤖 IA](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab2/resistencia_compresion_alumno_ia.ipynb) |
| **3** | xAI — XGBoost + SHAP | [Lab 3](lab3.md) | [🤖 Notebook](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab3/xai_estructuras_alumno_ia.ipynb) |
| **4** | CNN grietas + LSTM sensores | [Lab 4](lab4.md) | [🤖 P1 CNN](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_1/cnn_grietas_estructuras_alumno_ia.ipynb) · [🤖 P2 LSTM](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_2/rnn_sensores_estructuras_alumno_ia.ipynb) |
| **5** | LLM local / RAG (Ollama) | [Lab 5](lab5.md) | [🤖 Notebook](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab5/llm_local_estructuras_alumno_ia.ipynb) |
| **6** | Agentes (Agno + Ollama) | [Lab 6](lab6.md) | [🤖 Notebook](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab6/agentes_estructuras_alumno_ia.ipynb) |

!!! tip "Dos vías (Lab 0–2)"
    - **📓 Manual:** `*_alumno.ipynb` — editas hiperparámetros.
    - **🤖 IA:** `*_alumno_ia.ipynb` + [`prompts_entregados.md`](https://github.com/ia-estructuras-diplomado/curso-ia-web/tree/main/labs).

!!! note "Labs 3–6"
    Vía **IA-asistida**. Validación por resultados (`_verificar.py`).

## Cómo empezar

1. [Crear Codespace](codespaces.md) → `labs/setup.sh` configura el entorno.
2. Abrir el notebook del lab.
3. Kernel: `labs/.venv/bin/python`.

[Guía Codespaces](codespaces.md)
EOF

echo "→ docs/labs/codespaces.md"
cat > docs/labs/codespaces.md << 'EOF'
# GitHub Codespaces

Notebooks en `labs/labN/` — [curso-ia-web](https://github.com/ia-estructuras-diplomado/curso-ia-web) (sync desde `curso-ia-dev`).

[Crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json){ .md-button .md-button--primary }

## Enlaces por lab

| Lab | Tema | Guía | Notebook |
|:---:|:-----|:-----|:---------|
| **0** | Python IA | [Lab 0](lab0.md) | [📓](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab0/fundamentos_python_ia_alumno.ipynb) · [🤖](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab0/fundamentos_python_ia_alumno_ia.ipynb) |
| **1** | PCA / SHM | [Lab 1](lab1.md) | [📓](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/pca_monitoreo_estructural_alumno.ipynb) · [🤖](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/pca_monitoreo_estructural_alumno_ia.ipynb) |
| **2** | Hormigón UCI | [Lab 2](lab2.md) | [📓](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab2/resistencia_compresion_alumno.ipynb) · [🤖](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab2/resistencia_compresion_alumno_ia.ipynb) |
| **3** | xAI | [Lab 3](lab3.md) | [🤖 `xai_estructuras_alumno_ia.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab3/xai_estructuras_alumno_ia.ipynb) |
| **4** | CNN / RNN | [Lab 4](lab4.md) | [🤖 P1](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_1/cnn_grietas_estructuras_alumno_ia.ipynb) · [🤖 P2](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_2/rnn_sensores_estructuras_alumno_ia.ipynb) |
| **5** | LLM / RAG | [Lab 5](lab5.md) | [🤖 `llm_local_estructuras_alumno_ia.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab5/llm_local_estructuras_alumno_ia.ipynb) |
| **6** | Agentes | [Lab 6](lab6.md) | [🤖 `agentes_estructuras_alumno_ia.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab6/agentes_estructuras_alumno_ia.ipynb) |

## Pasos

1. Clic en **Crear Codespace** → iniciar sesión en GitHub.
2. Esperar build (`labs/setup.sh`).
3. Abrir notebook en `labs/labN/`.
4. Kernel: Python de `labs/.venv`.

[← Laboratorios](index.md)
EOF

echo "→ docs/labs/lab3.md"
cat > docs/labs/lab3.md << 'EOF'
# Lab 3: Inteligencia Artificial Explicable (xAI)

--8<-- "lab3-actions.md"

!!! info "Sesión 4"
    **Duración:** ~2 h · Vía IA-asistida

## Tema

Interpretar predicciones de **XGBoost** sobre sensores SHM con un kit xAI: importancias globales, **SHAP**, **LIME** y PDP.

| Técnica | Alcance |
|---------|---------|
| Importancia del booster | Global |
| Permutation importance | Global |
| SHAP (`TreeExplainer`) | Global + local |
| LIME | Local |
| PDP + SHAP dependence | Global marginal |

## Objetivos

1. Diferenciar explicación **global** vs **local**.
2. Aplicar varias técnicas xAI sobre un mismo modelo.
3. Comparar SHAP y LIME en un caso de test.
4. Interpretar en lenguaje de ingeniería estructural.

## Archivos

| Archivo | Uso |
|---------|-----|
| `xai_estructuras_alumno_ia.ipynb` | Notebook alumno |
| `prompts_entregados.md` | Bitácora de prompts |
| `data/` | Dataset SHM (Lab 1) |

## Pasos

1. **Crear Codespace** (botón arriba).
2. `cd labs/lab3` → abrir `xai_estructuras_alumno_ia.ipynb`.
3. Completar `prompts_entregados.md`.

[Codespaces](codespaces.md)
EOF

echo "→ docs/labs/lab4.md"
cat > docs/labs/lab4.md << 'EOF'
# Lab 4: Redes Neuronales — CNN y RNN/LSTM

--8<-- "lab4-actions.md"

!!! info "Sesión 5"
    **Duración:** ~4 h · Dos partes · Vía IA-asistida

## Partes

| Parte | Tema | Carpeta | Notebook |
|-------|------|---------|----------|
| **1** | CNN — grietas en hormigón | `part_1/` | `cnn_grietas_estructuras_alumno_ia.ipynb` |
| **2** | LSTM — sensores SHM | `part_2/` | `rnn_sensores_estructuras_alumno_ia.ipynb` |

## Objetivos

1. Entrenar una **CNN** para clasificación de imágenes de patología.
2. Entrenar **LSTM** para series de sensores (ventanas temporales).
3. Comparar costos (datos, cómputo, interpretabilidad) frente a Labs 1–2.

## PyTorch

Si falta `torchvision` o hay error `SymInt`:

```bash
bash labs/lab5/_fix_pytorch.sh
