# Curso IA Web

Sitio de documentación y entorno de laboratorios del diplomado **Inteligencia Artificial para Ingeniería Civil** (IA Estructuras Diplomado).

- **Sitio publicado:** https://ia-estructuras-diplomado.github.io/curso-ia-web/
- **Repositorio de desarrollo (privado):** [curso-ia-dev](https://github.com/ia-estructuras-diplomado/curso-ia-dev)

## Qué contiene este repo

| Ruta | Propósito |
|------|-----------|
| `docs/` | Contenido MkDocs (syllabus, sesiones, guías de labs) |
| `labs/` | Notebooks y datos sincronizados desde `curso-ia-dev` (Codespaces) |
| `.devcontainer/` | Configuración GitHub Codespaces |
| `config/course.yaml` | Fechas, calificación y mapeo web ↔ labs |

## Documentación local

```bash
pip install -r requirements.txt
mkdocs serve
```

Abre http://127.0.0.1:8000

## Laboratorios (Codespaces)

Los alumnos usan **un solo Codespace** para todo el curso (todos los labs comparten `labs/.venv`). El enlace con `quickstart=1` reanuda el existente o crea uno nuevo:

https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json

Guía: ver `docs/labs/codespaces.md` en el sitio o en el repo.

## Sincronización de labs

Los notebooks se editan en **curso-ia-dev** (privado). Al hacer push a `main` en dev, el workflow `.github/workflows/sync-labs-to-web.yml` publica `labs/` y `.devcontainer/` en este repositorio.

**Secreto requerido en curso-ia-dev:** `LABS_SYNC_TOKEN` (PAT con permiso de escritura en este repo).

## Deploy (GitHub Pages)

Push a `main` (cambios en `docs/`) → GitHub Actions ejecuta `mkdocs build` y publica en la rama `gh-pages`.

## CI — laboratorios

Cambios en `labs/` o `.devcontainer/` disparan [**Labs CI**](.github/workflows/labs-ci.yml):

1. `bash labs/setup.sh` (sin Ollama)
2. `bash labs/doctor.sh --strict`
3. `labs/_smoke_kernel.py` — kernel **Python (curso-ia labs)** registrado y ejecutable
4. Smoke tests docentes (`labs/_smoke_ia_solucion.sh`)
5. Build del devcontainer (mismo entorno que Codespaces)

[**Codespace smoke**](.github/workflows/codespace-smoke.yml) (semanal o manual) crea un Codespace real vía `gh codespace create` y valida el kernel dentro del contenedor.

Plantilla de sync dev → web: [`.github/workflows/sync-labs-to-web.yml.example`](.github/workflows/sync-labs-to-web.yml.example)

## Licencia

MIT
