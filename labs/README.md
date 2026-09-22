# Labs (Laboratorios)

Recursos prácticos para ejercicios, proyectos y experimentación.

**Estándar del curso (entorno local, notebook de referencia único, validación visual):** lee [`GUIA_LABORATORIOS.md`](./GUIA_LABORATORIOS.md).

## Entorno local (venv centralizado en `labs/`)

Un solo entorno (`labs/.venv`) para **todos** los labs, con Python fijado vía
[`uv`](https://astral.sh/uv). No crees venvs dentro de `lab0/` o `lab1/`.

**¿Estás en Windows?** Sigue [`INSTALACION_WINDOWS.md`](INSTALACION_WINDOWS.md) — usa `labs\setup.ps1` desde PowerShell (equivalente nativo de `setup.sh`, sin necesidad de WSL).

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
```

Dependencias: [`labs/requirements.txt`](requirements.txt).

**Stack ML CPU compartido (Lab 4 CNN/LSTM + Lab 5 embeddings/RAG):** `setup.sh` termina con [`_install_torch_cpu.sh`](_install_torch_cpu.sh) (`torch` + `torchvision` CPU, compatible con `sentence-transformers`). Este mismo script es el camino de reparación — si falta `torchvision` o ves un error de `SymInt`, simplemente vuelve a ejecutarlo:

```bash
bash labs/_install_torch_cpu.sh
```

**Claude Code + MCP (Lab 5 y Lab 6):** estos dos labs no usan `labs/.venv` ni notebooks — se trabajan con [Claude Code](https://code.claude.com) y servidores MCP que se lanzan solos con `uvx` (viene con `uv`). La instalación de Claude Code y las opciones de acceso (suscripción, API key o gratis con Ollama) están en la Parte 0 de [`lab5/README.md`](lab5/README.md).

## Un notebook de referencia por lab

Cada lab entrega **un solo notebook**, completo y ejecutable de punta a
punta — no un ejercicio en blanco. Ábrelo, ejecútalo (Run All) para ver el
resultado esperado, y luego construye tu propio notebook guiándote por el
README del lab (objetivo + prompts sugeridos por sección) y tu asistente de
IA. Entrega tu notebook ejecutado + [`prompts_entregados.md`](GUIA_LABORATORIOS.md#bitácora-de-prompts) (bitácora de prompts) completado.

Validación por **resultados visuales** (gráficos, métricas), no por
autoevaluación automática ni por código idéntico a la solución.

**Excepción — Lab 5 y Lab 6:** no tienen notebook. Son guías paso a paso para usar un agente real (Claude Code) conectado por MCP a un buscador RAG de normas, a ETABS y a Excel; la entrega es la bitácora, los agentes/skills que el alumno crea y los resultados que generan.

Docente: `bash labs/_verificar_notebooks.sh` ejecuta de punta a punta los 6 notebooks de referencia (Labs 0-4) tras cualquier cambio.

## Labs disponibles

| Lab | Carpeta | Tema |
|-----|---------|------|
| 0 | [`lab0/`](lab0/) | Fundamentos de Python para IA |
| 1 | [`lab1/`](lab1/) | PCA, KMeans, DBSCAN y monitoreo SHM (Kaggle) |
| 2 | [`lab2/`](lab2/) | Resistencia a compresión del hormigón (UCI) |
| 3 | [`lab3/`](lab3/) | Inteligencia artificial explicable (xAI) — XGBoost + SHAP (SHM) |
| 4 | [`lab4/part_1/`](lab4/part_1/) + [`lab4/part_2/`](lab4/part_2/) | CNN grietas (P1) + LSTM sensores SHM (P2) |
| 5 | [`lab5/`](lab5/) | Tu primer agente: Claude Code + MCP de normas peruanas (RAG) |
| 6 | [`lab6/`](lab6/) | Agentes con ETABS y Excel vía MCP: de un agente a un orquestador |

La numeración de carpetas `labs/labN/` coincide con el syllabus del curso (Lab 1, 2, 3…).

Scripts de preparación de datos/modelos de un solo uso (no vistos por los alumnos) viven en [`tools/`](../tools/), fuera de `labs/`.

## Publicación a alumnos (`curso-ia-dev` → `curso-ia-web`)

1. Editar notebooks **solo** en este repo (`curso-ia-dev`).
2. `git push` a `main` → el workflow **Sync labs to curso-ia-web** copia `labs/` **desde dev hacia web** (nunca al revés).
3. Requiere secreto `LABS_SYNC_TOKEN` (repository secret) en GitHub Actions de `curso-ia-dev`.

Como cada lab ya es solo `README.md` + un notebook + `prompts_entregados.md` + `data/` (Labs 5-6: `README.md` + `.mcp.json` + `referencia/`), no hay archivos internos que excluir del sync (ni generadores, ni `_verificar.py`, ni notebooks-solución separados).

## Notas

- Mantener datos crudos separados de datos procesados (`tools/data_raw/` para lo crudo, `labs/labN/data/` para lo que el notebook realmente lee)
- Documentar la fuente y características de cada dataset (`data/DATOS.md`)
- Notebooks deben ser ejecutables y reproducibles
