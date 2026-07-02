# Labs (Laboratorios)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)

> **Un solo Codespace para todo el curso.** El enlace con `quickstart=1` muestra **Resume this codespace** si ya tienes uno para este repositorio; si no, **Create codespace**. Todos los labs comparten `labs/.venv`. Gestiona tus entornos en [github.com/codespaces](https://github.com/codespaces).
Recursos prácticos para ejercicios, proyectos y experimentación.

**Estándar del curso (Codespaces, caja de herramientas, validación amigable):** lee [`GUIA_LABORATORIOS.md`](./GUIA_LABORATORIOS.md).

## Entorno local (venv centralizado en `labs/`)

Un solo entorno (`labs/.venv`) para **todos** los labs. No crees venvs dentro de `lab0/` o `lab1/`.

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
```

Dependencias: [`labs/requirements.txt`](requirements.txt).

**PyTorch compartido (Lab 4 CNN + Lab 5 embeddings):** `setup.sh` termina con [`_install_torch_cpu.sh`](_install_torch_cpu.sh) (`torch` + `torchvision` CPU, compatible con `sentence-transformers`). Si falta `torchvision` o ves `SymInt`:

```bash
bash labs/lab5/_fix_pytorch.sh   # repara el venv compartido, no solo Lab 5
```

Usa **Python 3.11 o 3.12** en el venv (igual que Codespaces). Si tu `.venv` quedó en 3.13: `rm -rf labs/.venv && bash labs/setup.sh`.

## GitHub Codespaces

Usa **un solo Codespace** para todos los labs (mismo `labs/.venv`). El enlace con `quickstart=1` prioriza **Resume this codespace** si ya existe uno para este repo.

El devcontainer ejecuta `labs/setup.sh` y usa el intérprete `labs/.venv/bin/python` para Jupyter.

[Abrir o reanudar Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)

## Dos vías por lab (opcional)

| Perfil | Notebook | Entrega |
|--------|----------|---------|
| Edita hiperparámetros | `*_alumno.ipynb` | Notebook con ✅ |
| Asistente IA (Copilot, Gemini, Cursor…) | `*_alumno_ia.ipynb` | Notebook con ✅ + [`prompts_entregados.md`](lab2/prompts_entregados.md) |

Validación por **resultados** (`_verificar.py`), no por código idéntico a la solución. Ver [Vía IA-asistida](GUIA_LABORATORIOS.md#vía-ia-asistida-opcional) en la guía.

Docente: `bash labs/_smoke_ia_solucion.sh` tras cambiar prompts o generadores.

## Labs disponibles

| Lab | Carpeta | Tema | Manual | Vía IA |
|-----|---------|------|--------|--------|
| 0 | [`lab0/`](lab0/) | Fundamentos de Python para IA | ✅ | ✅ |
| 1 | [`lab1/`](lab1/) | PCA, KMeans, DBSCAN y monitoreo SHM (Kaggle) | ✅ | ✅ |
| 2 | [`lab2/`](lab2/) | Resistencia a compresión del hormigón (UCI) | ✅ | ✅ |
| 3 | [`lab3/`](lab3/) | Inteligencia artificial explicable (xAI) — XGBoost + SHAP (SHM) | — | ✅ |
| 4 | [`lab4/`](lab4/) | CNN grietas (P1) + LSTM sensores SHM (P2) | — | ✅ |
| 5 | [`lab5/`](lab5/) | Modelos locales de lenguaje (LLM) / RAG | — | ✅ |
| 6 | [`lab6/`](lab6/) | Agentes de IA (Agno + Ollama) | — | ✅ |

La numeración de carpetas `labs/labN/` coincide con el syllabus del curso (Lab 1, 2, 3…).

## Publicación a alumnos (`curso-ia-dev` → `curso-ia-web`)

1. Editar notebooks **solo** en este repo (`curso-ia-dev`).
2. `git push` a `main` → el workflow **Sync labs to curso-ia-web** copia `labs/` y `.devcontainer/` **desde dev hacia web** (nunca al revés).
3. Requiere secreto `LABS_SYNC_TOKEN` (repository secret) en GitHub Actions de `curso-ia-dev`.

## Notas

- Mantener datos crudos separados de datos procesados
- Documentar la fuente y características de cada dataset
- Notebooks deben ser ejecutables y reproducibles
