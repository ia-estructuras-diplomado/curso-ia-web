# Lab 6 — Agentes de IA sísmicos

**Sesión 10** · Agente Agno + **Ollama local** + tools + MLP pre-entrenado + informe LaTeX.

## Stack (intro en notebook)

| Herramienta | Rol |
|-------------|-----|
| **Ollama** | LLM local (`llama3.2:3b`) — razonamiento y dictamen |
| **Agno** | Framework agente ReAct + tool calling |
| **MLP (.pkl)** | Best model neuronal (entrenado offline por docente) |
| **LaTeX** | Exportación `informe_sismico.tex` |

## Archivos

| Archivo | Uso |
|---------|-----|
| `agentes_estructuras_alumno_ia.ipynb` | Notebook alumno (vía IA) |
| `agentes_estructuras_solucion.ipynb` | Referencia docente |
| `prompts_entregados.md` | Bitácora de prompts |
| `data/earthquake_risk_model.pkl` | Best model MLP |
| `data/archive.zip` | Dataset sísmico (1000 filas) |

## Setup Codespaces

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
bash labs/lab6/_ollama_setup.sh
cd labs/lab6
python _preparar_datos.py
jupyter notebook agentes_estructuras_alumno_ia.ipynb
```

## Docente

```bash
cd labs/lab6
python _preparar_datos.py
python _generar_modelo.py      # entrena MLP offline → .pkl
python _generar_notebooks.py
python _smoke_test.py
```

Ver [`data/DATOS.md`](data/DATOS.md) y [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md).
