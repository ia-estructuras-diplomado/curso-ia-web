# Curso IA Web

Sitio de documentación y entorno de laboratorios del diplomado **Inteligencia Artificial para Ingeniería Civil** (IA Estructuras Diplomado).

- **Sitio publicado:** https://ia-estructuras-diplomado.github.io/curso-ia-web/
- **Repositorio de desarrollo (privado):** [curso-ia-dev](https://github.com/ia-estructuras-diplomado/curso-ia-dev)

## Qué contiene este repo

| Ruta | Propósito |
|------|-----------|
| `docs/` | Contenido MkDocs (syllabus, sesiones, guías de labs) |
| `labs/` | Notebooks, guías y datos sincronizados desde `curso-ia-dev` |
| `config/course.yaml` | Fechas, calificación y mapeo web ↔ labs |

## Documentación local

```bash
pip install -r requirements.txt
mkdocs serve
```

Abre http://127.0.0.1:8000

## Laboratorios

Los alumnos trabajan en su computadora con un único entorno (`labs/.venv`):

- **Windows (PowerShell, sin WSL):** `powershell -ExecutionPolicy Bypass -File labs\setup.ps1` — ver [`labs/INSTALACION_WINDOWS.md`](labs/INSTALACION_WINDOWS.md).
- **macOS / Linux:** `bash labs/setup.sh`.

Los Labs 5 y 6 usan Claude Code + MCP; el Lab 6 requiere **Windows nativo con ETABS 21+**.

## Sincronización de labs

Los notebooks se editan en **curso-ia-dev** (privado). Al hacer push a `main` en dev, el workflow `.github/workflows/sync-labs-to-web.yml` publica `labs/` en este repositorio.

**Secreto requerido en curso-ia-dev:** `LABS_SYNC_TOKEN` (PAT con permiso de escritura en este repo).

## Deploy (GitHub Pages)

Push a `main` (cambios en `docs/`) → GitHub Actions ejecuta `mkdocs build` y publica en la rama `gh-pages`.

## CI — laboratorios

Cambios en `labs/` disparan [**Labs CI**](.github/workflows/labs-ci.yml):

1. **Linux:** `bash labs/setup.sh` y `bash labs/_verificar_notebooks.sh` (ejecuta los notebooks de referencia de los Labs 0-4).
2. **Windows:** `labs\setup.ps1` y verificación de imports.

## Licencia

MIT
