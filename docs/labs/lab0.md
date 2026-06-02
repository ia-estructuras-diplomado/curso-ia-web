# Lab 0: Fundamentos de Python para IA

--8<-- "lab0-actions.md"

!!! info "Sesión 1"
    **Duración:** ~2 horas · Introducción al entorno del curso

## Objetivo

Familiarizarte con **Python y Jupyter** en **GitHub Codespaces** usando el enfoque **caja de herramientas**: código pre-escrito; tú solo completas celdas `### TU TAREA AQUÍ ###`.

Este lab prepara el terreno para Lab 1–6 (Scikit-learn, deep learning, LLM y agentes).

## Pasos en Codespaces

1. Pulsa **Crear Codespace — Lab 0** (arriba) e inicia sesión en GitHub si te lo pide.
2. Espera el build del contenedor (`labs/setup.sh` instala dependencias).
3. Abre **`labs/lab0/fundamentos_python_ia_alumno.ipynb`**.
4. Ejecuta celdas en orden; completa solo bloques marcados.

## Secciones del notebook

| # | Tema |
|---|------|
| 0 | **Sintaxis** — tipos, comentarios, f-strings, indentación |
| 1 | **Paquetes e imports** — `import`, `pip`, `requirements.txt`, Codespaces |
| 2 | Listas y diccionarios (JSON / APIs) |
| 3 | List comprehensions |
| 4 | Funciones como *tools* de agentes |
| 5 | Pandas + filtrado |
| 6 | Gráfico de validación visual |
| 7 | Cierre y puente hacia Scikit-Learn, DL y agentes |

Cada sección incluye **preguntas teóricas** y **autoevaluación** con ✅ / ⚠️ / ❌.

## Recursos en el repositorio

- **Notebook alumno:** `labs/lab0/fundamentos_python_ia_alumno.ipynb`
- **Entorno:** `labs/.venv` (compartido por todos los labs)
- **Setup:** `labs/setup.sh`

## Alternativa local

```bash
git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
cd curso-ia-web
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab0
jupyter notebook fundamentos_python_ia_alumno.ipynb
```

## Checklist

- [ ] Creé mi Codespace y abrí el notebook alumno
- [ ] Completé las celdas `### TU TAREA AQUÍ ###`
- [ ] Entiendo imports, `pip` y el entorno compartido `labs/.venv`
- [ ] Puedo cargar y filtrar datos con Pandas

## Próximo paso

- [Sesión 2 — Big Data](../sesiones/sesion2.md)
- [Lab 1 — PCA y SHM](lab1.md) (cuando avance el curso)

---

**¿Dudas?** → [Codespaces](codespaces.md) · [FAQ](../faq.md)
