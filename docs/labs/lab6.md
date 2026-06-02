# Lab 6: Agentes de IA

--8<-- "lab6-actions.md"

!!! warning "En desarrollo"
    Notebook en `labs/lab6/` — próximamente.

!!! info "Sesión 10"
    **Duración:** ~3 horas (previsto)

## Tema

Un **agente de IA** planifica pasos, **invoca herramientas** (código, búsqueda, APIs, notebooks) e **itera** hasta entregar un resultado — no solo responde texto como un chat simple.

```
Usuario: "Resume el informe y lista grietas críticas"
  → Agente: lee archivo → extrae tablas → clasifica → genera informe
```

### Componentes típicos

| Componente | Función |
|------------|---------|
| **LLM** | Razonamiento y siguiente paso |
| **Tools** | Leer CSV, ejecutar Python, RAG, modelos de Lab 1–4 |
| **Memoria** | Contexto y resultados intermedios |
| **Bucle agente** | Observar → actuar → verificar (ReAct, etc.) |

### Casos de uso del curso

- Encadenar **Lab 2** (resistencia) + **Lab 3** (SHAP) en un informe breve
- Agente con documentos locales (**Lab 5**) para responder con citas
- Borradores y checklists para **revisión humana** — no sustituye al ingeniero

## Objetivos de aprendizaje

1. Diferenciar **chat con LLM** vs **agente con herramientas**.
2. Definir al menos dos **tools** acotadas (p. ej. `load_concrete_csv`, `explain_prediction`).
3. Ejecutar un bucle agente simple y registrar trazas.
4. Evaluar **límites y riesgos**: permisos, ejecución de código, datos sensibles.

## Archivos previstos

| Archivo | Uso |
|---------|-----|
| `agentes_estructuras_alumno.ipynb` | Tools, agente, evaluación |
| `agentes_estructuras_solucion.ipynb` | Referencia docente |
| `data/` | Escenarios de prueba (informes, CSV, prompts) |

## Pasos en Codespaces (cuando esté disponible)

1. **Crear Codespace — Lab 6** (arriba).
2. Abrir `labs/lab6/agentes_estructuras_alumno.ipynb`.

---

**¿Dudas?** → [Codespaces](codespaces.md)
