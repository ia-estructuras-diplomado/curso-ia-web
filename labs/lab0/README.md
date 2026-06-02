# Lab 0 — Fundamentos de Python para IA

Introducción en **GitHub Codespaces** con enfoque **caja de herramientas**: código base pre-escrito, el alumno solo ajusta parámetros en celdas `### TU TAREA AQUÍ ###`.

## Archivos

| Archivo | Uso |
|---------|-----|
| `fundamentos_python_ia_alumno.ipynb` | Notebook del alumno |
| `fundamentos_python_ia_solucion.ipynb` | Referencia docente |
| `_verificar.py` | Autoevaluación con mensajes ✅ / ❌ |

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
