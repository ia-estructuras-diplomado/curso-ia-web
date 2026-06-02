# Lab 5: Modelos Locales de Lenguaje (LLM)

--8<-- "lab5-actions.md"

!!! warning "En desarrollo"
    Notebook en `labs/lab5/` — próximamente.

!!! info "Sesión 9"
    **Duración:** ~3 horas (previsto)

## Tema

**LLM ejecutados localmente** para tareas acotadas de ingeniería estructural:

- Resumir informes de inspección o memorias de cálculo
- Preguntas sobre normativa a partir de **documentos cargados**
- Borradores de actas, checklists o descripciones de patologías (**revisión humana obligatoria**)

### ¿Por qué modelos locales?

| Aspecto | Modelo local | API en la nube |
|---------|--------------|----------------|
| **Privacidad** | Datos no salen del entorno | Política de datos clara |
| **Costo** | Hardware / Codespaces | Pago por uso |
| **Control** | Versión fija, offline posible | Dependencia del proveedor |
| **Calidad** | Modelos más pequeños; prompts cuidadosos | Modelos más grandes |

### Herramientas previstas

- **Ollama**, **llama.cpp** o equivalente en Codespaces
- Modelos open-weight (Llama, Mistral, Qwen — según entorno)
- **RAG ligero** (opcional): embeddings + búsqueda en PDFs del curso

## Objetivos de aprendizaje

1. Instalar y ejecutar un LLM local en el entorno del curso.
2. Diseñar **prompts estructurados** (contexto + restricciones + formato).
3. Detectar **alucinaciones**; verificar con fuentes.
4. Articular cuándo un LLM **no** debe usarse en decisiones de diseño sin revisión humana.

## Archivos previstos

| Archivo | Uso |
|---------|-----|
| `llm_local_estructuras_alumno.ipynb` | Prompting, comparación, límites |
| `llm_local_estructuras_solucion.ipynb` | Referencia docente |
| `data/` | Normativa, informes sintéticos o anonimizados |

## Pasos en Codespaces (cuando esté disponible)

1. **Crear Codespace — Lab 5** (arriba).
2. Abrir `labs/lab5/llm_local_estructuras_alumno.ipynb`.

---

**¿Dudas?** → [Codespaces](codespaces.md)
