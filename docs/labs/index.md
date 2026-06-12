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
