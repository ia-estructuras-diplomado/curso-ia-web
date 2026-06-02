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

Los alumnos abren un Codespace sobre este repo:

https://codespaces.new/ia-estructuras-diplomado/curso-ia-web

Guía: ver `docs/labs/codespaces.md` en el sitio o en el repo.

## Sincronización de labs

Los notebooks se editan en **curso-ia-dev** (privado). Al hacer push a `main` en dev, el workflow `.github/workflows/sync-labs-to-web.yml` publica `labs/` y `.devcontainer/` en este repositorio.

**Secreto requerido en curso-ia-dev:** `LABS_SYNC_TOKEN` (PAT con permiso de escritura en este repo).

## Deploy (GitHub Pages)

Push a `main` → GitHub Actions ejecuta `mkdocs build` y publica en la rama `gh-pages`.

## Licencia

MIT
