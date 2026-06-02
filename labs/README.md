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

| Lab | Carpeta | Tema | Guía web |
|-----|---------|------|----------|
| 0 | [`lab0/`](lab0/) | Fundamentos de Python para IA | Sesión 1 |
| 1 | [`lab1/`](lab1/) | Fundamentos ML — resistencia hormigón (UCI) | [Lab 1](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab1/) |
| 2 | [`lab2/`](lab2/) | Monitoreo SHM — detección de anomalías | [Lab 2](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab2/) *(notebook pendiente)* |
| 3 | [`lab3/`](lab3/) | PCA, clustering y señales (Kaggle SHM) | [Lab 3](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab3/) |

La numeración de carpetas `labs/labN/` coincide con el syllabus del curso (Lab 1, 2, 3).

## Publicación a alumnos

1. Editar notebooks en este repo (`curso-ia-dev`).
2. `git push` a `main` → workflow **Sync labs to curso-ia-web** copia `labs/` y `.devcontainer/` al repo público.
3. Requiere secreto `LABS_SYNC_TOKEN` en GitHub Actions de este repo.

## Notas

- Mantener datos crudos separados de datos procesados
- Documentar la fuente y características de cada dataset
- Notebooks deben ser ejecutables y reproducibles
