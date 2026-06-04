# Lab 6 — Agentes de IA

**Sesión 10** · Orquestación de herramientas con agentes para flujos de trabajo en ingeniería estructural.

## Tema del laboratorio

Un **agente de IA** es un sistema que, a partir de un objetivo en lenguaje natural, **planifica pasos**, **invoca herramientas** (código, búsqueda, APIs, notebooks) y **itera** hasta entregar un resultado — no solo responde un texto fijo como un chat simple.

```
Usuario: "Resume el informe de inspección y lista grietas críticas"
    → Agente: lee archivo → extrae tablas → clasifica severidad → genera informe
```

### Componentes típicos de un agente

| Componente | Función |
|------------|---------|
| **LLM** | Razonamiento y decisión del siguiente paso |
| **Herramientas (tools)** | Leer CSV, ejecutar Python, consultar RAG, llamar modelos de Lab 1–4 |
| **Memoria / estado** | Contexto de la conversación y resultados intermedios |
| **Bucle agente** | Observar → actuar → verificar (ReAct, plan-and-execute, etc.) |

### Casos de uso orientados al curso

- Agente que **encadena** Lab 2 (predicción de resistencia) + Lab 3 (explicación SHAP) en un informe breve.
- Agente con acceso a **documentos locales** (Lab 5) para responder preguntas con citas.
- Agente que **no** sustituye al ingeniero: propone borradores y checklists para revisión humana.

## Estado

**En desarrollo.**

Cuando esté listo, esta carpeta incluirá:

| Archivo | Uso |
|---------|-----|
| `agentes_estructuras_alumno.ipynb` | Definir tools, ejecutar agente, evaluar salidas |
| `agentes_estructuras_solucion.ipynb` | Referencia docente |
| `agentes_estructuras_alumno_ia.ipynb` | *(al publicar)* Vía IA + `prompts_entregados.md` |
| `agentes_estructuras_solucion_ia.ipynb` | *(al publicar)* Prompts canónicos docente |
| `data/` | Escenarios de prueba (informes, CSV, prompts de ejemplo) |

## Objetivos de aprendizaje

1. Diferenciar **chat con LLM** vs **agente con herramientas**.
2. Definir al menos dos **tools** acotadas (p. ej. `load_concrete_csv`, `explain_prediction`).
3. Ejecutar un bucle agente simple y registrar trazas (qué hizo y por qué).
4. Evaluar **límites y riesgos**: permisos, ejecución de código, datos sensibles de obra.

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab6
jupyter notebook agentes_estructuras_alumno.ipynb
```

Dependencias del agente (framework acordado: LangGraph, CrewAI, SDK del curso, etc.) se documentarán al publicar el notebook.

## GitHub Codespaces

Abrir `labs/lab6/agentes_estructuras_alumno.ipynb` (cuando esté publicado).

Guía del curso: [Lab 6 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab6/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
