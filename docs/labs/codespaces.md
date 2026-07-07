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
2. Esperar build (`labs/setup.sh` — **sin Ollama** en el primer arranque; tarda ~2–5 min).
3. Abrir notebook en `labs/labN/`.
4. Kernel: **Python (curso-ia labs)** (`labs/.venv/bin/python`).

### Labs 5 y 6 (Ollama)

Tras crear el Codespace, en terminal:

```bash
bash labs/lab5/_ollama_setup.sh
```

La primera descarga de `llama3.2:3b` (~2 GB) puede tardar varios minutos.

### Si algo falla

```bash
bash labs/doctor.sh --strict   # falla si falta algún artefacto
bash labs/setup.sh             # reinstalar entorno + datos
bash labs/lab5/_fix_pytorch.sh   # si falta torchvision o SymInt
```

En GitHub: pestaña **Actions** → workflow **Labs CI** (mismas comprobaciones en cada push a `labs/`).

El kernel correcto en el selector del notebook es **Python (curso-ia labs)** (`curso-ia-labs` internamente). Validación automática: `labs/.venv/bin/python labs/_smoke_kernel.py`.

[← Laboratorios](index.md)
