# Lab 5 — Modelos Locales de Lenguaje (LLM)

**Sesión 9** · Uso de LLM **en local** para consulta técnica, borradores y apoyo a documentación de obra.

## Tema del laboratorio

Trabajar con **Large Language Models (LLM) ejecutados localmente** — sin depender obligatoriamente de APIs en la nube — para tareas acotadas de ingeniería estructural:

- Resumir informes de inspección o memorias de cálculo (texto ya disponible).
- Formular preguntas sobre normativa o especificaciones **a partir de documentos cargados**.
- Generar borradores de actas, checklists o descripciones de patologías (**siempre revisados por un profesional**).

### ¿Por qué modelos locales?

| Aspecto | Modelo local | API en la nube |
|---------|--------------|----------------|
| **Privacidad** | Datos de obra no salen del entorno | Requiere política de datos clara |
| **Costo recurrente** | Hardware / Codespaces; sin token por llamada | Pago por uso |
| **Control** | Versión fija, offline posible | Dependencia del proveedor |
| **Calidad** | Modelos más pequeños; prompts cuidadosos | Modelos más grandes |

### Herramientas previstas (referencia docente)

- Runtime local: **Ollama**, **llama.cpp**, o equivalente acordado para Codespaces.
- Modelos open-weight de tamaño razonable (p. ej. Llama, Mistral, Qwen — según disponibilidad en el entorno del curso).
- **RAG ligero** (opcional): embeddings + búsqueda en PDFs o Markdown del curso.

## Estado

**En desarrollo.**

Cuando esté listo, esta carpeta incluirá:

| Archivo | Uso |
|---------|-----|
| `llm_local_estructuras_alumno.ipynb` | Prompting, comparación de respuestas, límites del modelo |
| `llm_local_estructuras_solucion.ipynb` | Referencia docente |
| `llm_local_estructuras_alumno_ia.ipynb` | *(al publicar)* Vía IA + `prompts_entregados.md` |
| `llm_local_estructuras_solucion_ia.ipynb` | *(al publicar)* Prompts canónicos docente |
| `data/` | Fragmentos de normativa, informes sintéticos o anonimizados |

## Objetivos de aprendizaje

1. Instalar y ejecutar un LLM local en el entorno del curso.
2. Diseñar **prompts estructurados** para tareas técnicas (contexto + restricciones + formato de salida).
3. Detectar **alucinaciones** y respuestas genéricas; verificar con fuentes.
4. Articular cuándo un LLM **no** debe usarse (decisiones de diseño estructural sin revisión humana).

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab5
jupyter notebook llm_local_estructuras_alumno.ipynb
```

Documentación adicional de dependencias (Ollama, etc.) se añadirá en `labs/requirements.txt` cuando el notebook esté definido.

## GitHub Codespaces

Abrir `labs/lab5/llm_local_estructuras_alumno.ipynb` (cuando esté publicado).

Guía del curso: [Lab 5 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab5/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
