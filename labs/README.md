# Labs (Laboratorios)

Recursos prácticos para ejercicios, proyectos y experimentación.

**Estándar del curso (Codespaces, caja de herramientas, validación amigable):** lee [`GUIA_LABORATORIOS.md`](./GUIA_LABORATORIOS.md).

## Entorno local (venv centralizado en `labs/`)

Un solo entorno para **todos** los labs. No crees venvs dentro de `lab0/` o `lab1/`.

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
```

Dependencias: [`labs/requirements.txt`](requirements.txt).

## GitHub Codespaces

El devcontainer ejecuta `labs/setup.sh` y usa el intérprete `labs/.venv/bin/python` para Jupyter.

[Crear Codespace](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web)

## Labs disponibles

| Lab | Carpeta | Tema | Estado |
|-----|---------|------|--------|
| 0 | [`lab0/`](lab0/) | Fundamentos de Python para IA | ✅ |
| 1 | [`lab1/`](lab1/) | PCA, KMeans, DBSCAN y monitoreo SHM (Kaggle) | ✅ |
| 2 | [`lab2/`](lab2/) | Resistencia a compresión del hormigón (UCI) | ✅ |
| 3 | [`lab3/`](lab3/) | Inteligencia artificial explicable (xAI) | 🚧 |
| 4 | [`lab4/`](lab4/) | Redes neuronales, CNN y RNN | 🚧 |
| 5 | [`lab5/`](lab5/) | Modelos locales de lenguaje (LLM) | 🚧 |
| 6 | [`lab6/`](lab6/) | Agentes de IA | 🚧 |

La numeración de carpetas `labs/labN/` coincide con el syllabus del curso (Lab 1, 2, 3…).

## Publicación a alumnos (`curso-ia-dev` → `curso-ia-web`)

1. Editar notebooks **solo** en este repo (`curso-ia-dev`).
2. `git push` a `main` → el workflow **Sync labs to curso-ia-web** copia `labs/` y `.devcontainer/` **desde dev hacia web** (nunca al revés).
3. Requiere secreto `LABS_SYNC_TOKEN` (repository secret) en GitHub Actions de `curso-ia-dev`.

## Notas

- Mantener datos crudos separados de datos procesados
- Documentar la fuente y características de cada dataset
- Notebooks deben ser ejecutables y reproducibles
