# Lab 5 — RAG con Ollama (normativa estructural)

**Sesión 9** · Consulta técnica sobre normas peruanas con **RAG local** + **Ollama** en GitHub Codespaces.

## Tema del laboratorio

Construir paso a paso un pipeline **Retrieval-Augmented Generation (RAG)** para responder preguntas sobre:

- **E.020** — Cargas (`Norma_E_020_CARGAS.pdf`)
- **E.030** — Sismo (`Norma_E_030_SISMO.pdf`, muestra parcial en el lab)
- **E.050** — Suelos (`Norma_E_050_SUELOS.pdf`)

| Capa | Herramienta |
|------|-------------|
| Extracción PDF | `pypdf` |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Recuperación | Similitud coseno (`numpy`) |
| Generación | **Ollama** (`llama3.2:3b`) en `localhost:11434` |

## Archivos

| Archivo | Uso |
|---------|-----|
| `llm_local_estructuras_alumno_ia.ipynb` | Vía IA-asistida + autoevaluación ✅ |
| `llm_local_estructuras_solucion.ipynb` | Referencia docente (no distribuir al inicio) |
| `prompts_entregados.md` | Bitácora de prompts (entrega obligatoria) |
| `pdfs/` | Corpus normativo |
| `data/DATOS.md` | Descripción del corpus |
| `_verificar.py` | Autoevaluación amigable |
| `_ollama_setup.sh` | Instalar Ollama y descargar modelo |

## Objetivos de aprendizaje

1. Explicar las 5 etapas de un pipeline RAG (carga → chunks → embeddings → top-k → LLM).
2. Extraer y fragmentar PDFs de normativa con `pypdf`.
3. Recuperar fragmentos relevantes con embeddings locales.
4. Generar respuestas con **Ollama** ancladas al contexto recuperado.
5. Comparar respuestas **con y sin RAG**; detectar alucinaciones.

## GitHub Codespaces

1. Abrir el repo → **Code** → **Codespaces** → **Create codespace**.
2. Esperar `labs/setup.sh` (Python + dependencias; Ollama se intenta instalar al final).
3. Si `OLLAMA_OK` es False en el notebook, ejecutar en terminal:

```bash
bash labs/lab5/_ollama_setup.sh
```

4. Abrir [`llm_local_estructuras_alumno_ia.ipynb`](llm_local_estructuras_alumno_ia.ipynb).
5. Ejecutar celdas en orden; buscar ✅ antes de avanzar.
6. Completar [`prompts_entregados.md`](prompts_entregados.md).

**Primera ejecución:** la descarga de `all-MiniLM-L6-v2` (~90 MB) y `llama3.2:3b` (~2 GB) puede tardar varios minutos.

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
bash labs/lab5/_ollama_setup.sh   # si Ollama no está listo
cd labs/lab5
jupyter notebook llm_local_estructuras_alumno_ia.ipynb
```

## Verificación docente

```bash
source labs/.venv/bin/activate
python labs/lab5/_generar_notebooks.py   # regenerar notebooks
python labs/lab5/_smoke_test.py          # secciones 1–7 sin Ollama; 8–9 si está activo
```

## Límites importantes

- El LLM puede **alucinar** cifras o artículos: contrastar siempre con el fragmento recuperado.
- E.030 se usa parcialmente (30 páginas) por memoria y tiempo en Codespaces.
- Este lab **no sustituye** la normativa oficial ni el criterio profesional.

Guía del curso: [Lab 5 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab5/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
