# Lab 0 — Fundamentos de Python para IA

Introducción en **GitHub Codespaces** con enfoque **caja de herramientas**: código base pre-escrito. Elige una vía:

- **Manual:** edita `### TU TAREA AQUÍ ###`
- **IA-asistida:** prompts + `### PEGA AQUÍ EL CÓDIGO DE LA IA ###` + bitácora `prompts_entregados.md`

## ¿Qué notebook abrir?

| Si… | Abre |
|-----|------|
| Sabes editar variables Python | `fundamentos_python_ia_alumno.ipynb` |
| Prefieres Copilot / Gemini / Cursor | `fundamentos_python_ia_alumno_ia.ipynb` |

## Archivos

| Archivo | Uso |
|---------|-----|
| `fundamentos_python_ia_alumno.ipynb` | Vía manual |
| `fundamentos_python_ia_alumno_ia.ipynb` | Vía IA |
| `fundamentos_python_ia_solucion.ipynb` | Referencia docente (manual) |
| `fundamentos_python_ia_solucion_ia.ipynb` | Referencia docente (IA) |
| `prompts_entregados.md` | Bitácora de prompts |
| `_verificar.py` | Autoevaluación ✅ / ❌ |
| `_generar_notebooks.py` | Regenera los cuatro notebooks |

**Entorno:** compartido en [`labs/.venv`](../.venv) — ver [`labs/setup.sh`](../setup.sh).

## Codespaces (recomendado)

1. Cuenta en [GitHub](https://github.com).
2. En el repo del curso: **Code** → **Codespaces** → **Create codespace**.
3. Abrir `labs/lab0/fundamentos_python_ia_alumno.ipynb`.
4. Ejecutar celdas en orden; completar solo bloques `### TU TAREA AQUÍ ###`.

El contenedor ejecuta [`labs/setup.sh`](../setup.sh) al crearse.

## Local (alternativa)

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab0
jupyter notebook fundamentos_python_ia_alumno.ipynb
```

## Secciones

0. **Sintaxis** — tipos, comentarios, f-strings, indentación
1. **Paquetes e imports** — `import`, `pip`, `requirements.txt`, Codespaces
2. Listas y diccionarios (JSON / APIs)
3. List comprehensions
4. Funciones como *tools* de agentes
5. Pandas + filtrado (target `Compro`)
6. Gráfico de validación visual
7. Cierre y puente hacia Scikit-Learn, DL y agentes

Cada sección incluye **preguntas teóricas** (sintaxis, paquetes, etc.) y **autoevaluación** con ✅.

## Estándar del curso

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md) (sin Otter; validación amigable en notebook).
