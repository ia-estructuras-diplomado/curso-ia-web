"""Prompts IA y celdas vacías para Lab 5 — importar desde _generar_notebooks.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from _ia_helpers import celda_solucion_alumno, ia_guia_seccion  # noqa: E402

IA_Q1 = ia_guia_seccion(
    "1",
    "Contexto RAG",
    "Listar los 5 pasos del pipeline RAG que construirás en este lab.",
    [
        "Definir `PASOS_RAG` como lista con al menos 5 pasos",
        "Incluir carga, fragmentación, embeddings, recuperación y generación",
        "Imprimir la lista numerada",
    ],
    vars_autoeval=["PASOS_RAG"],
    consideraciones=[
        "RAG = recuperar fragmentos de normativa antes de preguntar al LLM",
        "En obra: consultas sobre E.020/E.030/E.050 sin enviar PDFs a la nube",
        "Nombres sugeridos: carga PDFs, fragmentación, embeddings, recuperación top-k, generación Ollama",
    ],
    prompt="""Estoy en el Lab 5 de RAG con Ollama para normas estructurales peruanas.
Genera código que:
1) defina PASOS_RAG = ["Carga de PDFs", "Fragmentación en chunks", "Embeddings con MiniLM", "Recuperación top-k", "Generación con Ollama"]
2) imprima "Pipeline RAG:"
3) enumere cada paso con print(f"  {i}. {paso}")
No uses imports nuevos.""",
)

CELDA_Q1 = celda_solucion_alumno(
    variables=["PASOS_RAG"],
    pasos=[
        "Lista con 5 pasos del pipeline RAG",
        "Imprimir cada paso numerado",
    ],
)

IA_Q2 = ia_guia_seccion(
    "2",
    "Verificar Ollama",
    "Configurar el modelo LLM local y comprobar que Ollama responde.",
    [
        "Definir `MODELO_LLM = 'llama3.2:3b'` y `OLLAMA_URL = 'http://localhost:11434'`",
        "Hacer GET a `/api/tags` con requests",
        "Asignar `OLLAMA_OK = True` si responde 200, si no False",
        "Imprimir estado y modelos disponibles",
    ],
    vars_autoeval=["MODELO_LLM", "OLLAMA_OK"],
    consideraciones=[
        "Si OLLAMA_OK es False ejecuta en terminal: bash labs/lab5/_ollama_setup.sh",
        "La primera descarga del modelo puede tardar varios minutos",
        "No uses APIs en la nube — solo localhost:11434",
    ],
    prompt="""En Jupyter del Lab 5 RAG necesito verificar Ollama local.
Genera código que:
1) defina MODELO_LLM = "llama3.2:3b"
2) defina OLLAMA_URL = "http://localhost:11434"
3) intente requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
4) asigne OLLAMA_OK = (resp.status_code == 200) en try/except: OLLAMA_OK = False
5) imprima OLLAMA_OK y, si True, los nombres de modelos del JSON
Usa import requests (ya disponible).""",
)

CELDA_Q2 = celda_solucion_alumno(
    variables=["MODELO_LLM", "OLLAMA_URL", "OLLAMA_OK"],
    pasos=[
        "Definir MODELO_LLM y OLLAMA_URL",
        "Comprobar conexión con /api/tags",
        "Asignar OLLAMA_OK e imprimir diagnóstico",
    ],
)

IA_Q3 = ia_guia_seccion(
    "3",
    "Inventario de PDFs",
    "Elegir el PDF activo para empezar la extracción (E.020 cargas).",
    [
        "Definir `N_PDFS` = número de archivos en pdfs/",
        "Definir `PDF_ACTIVO = 'Norma_E_020_CARGAS.pdf'`",
        "Imprimir ambos valores",
    ],
    vars_autoeval=["PDF_ACTIVO", "N_PDFS"],
    consideraciones=[
        "La celda pre-escrita ya listó los PDFs con listar_pdfs()",
        "Debe haber exactamente 3 PDFs: E.020, E.030, E.050",
        "Empezamos con E.020 (cargas) por ser el más manejable",
    ],
    prompt="""En Jupyter la celda anterior definió lista_pdfs = listar_pdfs("pdfs").
Genera código que:
1) defina N_PDFS = len(lista_pdfs)
2) defina PDF_ACTIVO = "Norma_E_020_CARGAS.pdf"
3) imprima N_PDFS y PDF_ACTIVO
No recalcules lista_pdfs.""",
)

CELDA_Q3 = celda_solucion_alumno(
    variables=["PDF_ACTIVO", "N_PDFS"],
    pasos=[
        "N_PDFS = len(lista_pdfs)",
        "PDF_ACTIVO = Norma_E_020_CARGAS.pdf",
        "Imprimir inventario",
    ],
)

IA_Q4 = ia_guia_seccion(
    "4",
    "Extracción de texto",
    "Extraer texto del PDF activo con pypdf.",
    [
        "Usar `extraer_texto_pdf(Path('pdfs') / PDF_ACTIVO)`",
        "Guardar en `texto_pdf`, `N_PAGINAS` y `N_CARACTERES`",
        "Mostrar los primeros 400 caracteres",
    ],
    vars_autoeval=["texto_pdf", "N_PAGINAS", "N_CARACTERES"],
    consideraciones=[
        "extraer_texto_pdf ya está importada desde _verificar",
        "N_CARACTERES = len(texto_pdf)",
        "Si el texto es muy corto, el PDF puede ser escaneado (fuera de alcance del lab)",
    ],
    prompt="""En Jupyter tengo PDF_ACTIVO y la función extraer_texto_pdf(ruta) -> (texto, n_paginas_total).
Genera código que:
1) from pathlib import Path
2) texto_pdf, N_PAGINAS = extraer_texto_pdf(Path("pdfs") / PDF_ACTIVO)
3) N_CARACTERES = len(texto_pdf)
4) imprima N_PAGINAS, N_CARACTERES
5) print(texto_pdf[:400])
No uses imports nuevos salvo Path si hace falta.""",
)

CELDA_Q4 = celda_solucion_alumno(
    variables=["texto_pdf", "N_PAGINAS", "N_CARACTERES"],
    pasos=[
        "Extraer texto del PDF activo",
        "Calcular N_CARACTERES",
        "Mostrar muestra de 400 caracteres",
    ],
)

IA_Q5 = ia_guia_seccion(
    "5",
    "Fragmentación",
    "Dividir el texto en chunks solapados para la búsqueda.",
    [
        "Definir `CHUNK_SIZE = 800` y `CHUNK_OVERLAP = 100`",
        "Crear `CHUNKS = fragmentar_texto(texto_pdf, CHUNK_SIZE, CHUNK_OVERLAP)`",
        "Definir `N_CHUNKS = len(CHUNKS)` e imprimir",
    ],
    vars_autoeval=["CHUNKS", "N_CHUNKS", "CHUNK_SIZE", "CHUNK_OVERLAP"],
    consideraciones=[
        "fragmentar_texto está en _verificar",
        "Chunks más pequeños = más precisión pero más vectores",
        "CHUNK_OVERLAP evita cortar artículos de norma a la mitad",
    ],
    prompt="""En Jupyter tengo texto_pdf y fragmentar_texto(texto, chunk_size, chunk_overlap).
Genera código que:
1) CHUNK_SIZE = 800; CHUNK_OVERLAP = 100
2) CHUNKS = fragmentar_texto(texto_pdf, CHUNK_SIZE, CHUNK_OVERLAP)
3) N_CHUNKS = len(CHUNKS)
4) imprima N_CHUNKS y el primer chunk ([:200])
No uses imports nuevos.""",
)

CELDA_Q5 = celda_solucion_alumno(
    variables=["CHUNKS", "N_CHUNKS", "CHUNK_SIZE", "CHUNK_OVERLAP"],
    pasos=[
        "Definir CHUNK_SIZE y CHUNK_OVERLAP",
        "Crear CHUNKS con fragmentar_texto",
        "Imprimir N_CHUNKS",
    ],
)

IA_Q6 = ia_guia_seccion(
    "6",
    "Embeddings e índice",
    "Vectorizar chunks con sentence-transformers (all-MiniLM-L6-v2).",
    [
        "Cargar `modelo_emb = SentenceTransformer(MODELO_EMB)`",
        "Calcular `EMBEDDINGS = modelo_emb.encode(CHUNKS, show_progress_bar=False)`",
        "Definir `N_VECTORES = EMBEDDINGS.shape[0]` e imprimir forma",
    ],
    vars_autoeval=["EMBEDDINGS", "N_VECTORES"],
    consideraciones=[
        "MODELO_EMB ya está definido en la celda setup: 'all-MiniLM-L6-v2'",
        "La primera ejecución descarga el modelo (~90 MB)",
        "N_VECTORES debe igualar N_CHUNKS",
    ],
    prompt="""En Jupyter tengo CHUNKS, N_CHUNKS, MODELO_EMB = "all-MiniLM-L6-v2" y SentenceTransformer importado.
Genera código que:
1) modelo_emb = SentenceTransformer(MODELO_EMB)
2) EMBEDDINGS = modelo_emb.encode(CHUNKS, show_progress_bar=False)
3) N_VECTORES = EMBEDDINGS.shape[0]
4) imprima N_VECTORES y EMBEDDINGS.shape
No uses imports nuevos.""",
)

CELDA_Q6 = celda_solucion_alumno(
    variables=["EMBEDDINGS", "N_VECTORES"],
    pasos=[
        "Instanciar SentenceTransformer",
        "Codificar CHUNKS en EMBEDDINGS",
        "Imprimir N_VECTORES y shape",
    ],
)

IA_Q7 = ia_guia_seccion(
    "7",
    "Recuperación top-k",
    "Buscar los fragmentos más similares a una consulta técnica.",
    [
        "Definir `CONSULTA` sobre cargas o norma E.020",
        "Definir `TOP_K = 3`",
        "Codificar consulta, usar `cosine_top_k`, llenar `CHUNKS_RECUPERADOS`",
    ],
    vars_autoeval=["CONSULTA", "CHUNKS_RECUPERADOS", "TOP_K"],
    consideraciones=[
        "cosine_top_k está en _verificar",
        "Muestra los fragmentos recuperados antes de la sección 8",
        "Ejemplo: '¿Qué tipos de sobrecarga considera la norma E.020?'",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo CHUNKS, EMBEDDINGS, modelo_emb, cosine_top_k(query_vec, matrix, k).
Genera código que:
1) CONSULTA = "¿Qué tipos de sobrecarga considera la norma E.020 de cargas?"
2) TOP_K = 3
3) q_vec = modelo_emb.encode([CONSULTA])[0]
4) idx, scores = cosine_top_k(q_vec, EMBEDDINGS, TOP_K)
5) CHUNKS_RECUPERADOS = [CHUNKS[i] for i in idx]
6) imprima CONSULTA y cada fragmento con su score
No uses imports nuevos.""",
)

CELDA_Q7 = celda_solucion_alumno(
    variables=["CONSULTA", "TOP_K", "CHUNKS_RECUPERADOS"],
    pasos=[
        "Definir CONSULTA técnica",
        "TOP_K = 3 y cosine_top_k",
        "Llenar CHUNKS_RECUPERADOS",
    ],
)

IA_Q8 = ia_guia_seccion(
    "8",
    "Prompt RAG y respuesta Ollama",
    "Armar prompt con contexto recuperado y generar respuesta local.",
    [
        "Unir CHUNKS_RECUPERADOS en `contexto`",
        "Armar `PROMPT_RAG` con instrucciones + contexto + CONSULTA",
        "Llamar `llamar_ollama(PROMPT_RAG, MODELO_LLM, OLLAMA_URL)` → `RESPUESTA_RAG`",
    ],
    vars_autoeval=["PROMPT_RAG", "RESPUESTA_RAG"],
    consideraciones=[
        "Requiere OLLAMA_OK = True (sección 2)",
        "Pide al modelo citar solo el contexto; si no sabe, decir 'no consta'",
        "llamar_ollama está en _verificar",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo CONSULTA, CHUNKS_RECUPERADOS, MODELO_LLM, OLLAMA_URL y llamar_ollama().
Genera código que:
1) contexto = "\\n---\\n".join(CHUNKS_RECUPERADOS)
2) PROMPT_RAG = f'''Eres un asistente de normativa estructural peruana.
Responde SOLO con base en el CONTEXTO. Si no está, di "No consta en el contexto".

CONTEXTO:
{contexto}

PREGUNTA: {CONSULTA}
'''
3) RESPUESTA_RAG = llamar_ollama(PROMPT_RAG, MODELO_LLM, OLLAMA_URL)
4) print(PROMPT_RAG[:300], "...")
5) print("RESPUESTA:", RESPUESTA_RAG)
No uses imports nuevos.""",
)

CELDA_Q8 = celda_solucion_alumno(
    variables=["PROMPT_RAG", "RESPUESTA_RAG"],
    pasos=[
        "Armar PROMPT_RAG con contexto",
        "Llamar Ollama",
        "Imprimir respuesta",
    ],
    nota="Requiere Ollama activo (sección 2).",
)

IA_Q9 = ia_guia_seccion(
    "9",
    "RAG vs sin contexto",
    "Comparar respuesta con y sin fragmentos recuperados; detectar uso de fuente.",
    [
        "Generar `RESPUESTA_SIN_RAG` con la misma CONSULTA pero sin contexto",
        "Comparar longitud o contenido de ambas respuestas",
        "Definir `USA_FUENTE = True` si RESPUESTA_RAG menciona norma, E.020, artículo o texto del contexto",
    ],
    vars_autoeval=["RESPUESTA_SIN_RAG", "USA_FUENTE"],
    consideraciones=[
        "Sin contexto el modelo suele ser más genérico o alucinar",
        "USA_FUENTE es True solo si hay evidencia de uso del contexto",
        "Imprime ambas respuestas lado a lado para comparar",
    ],
    prompt="""En Jupyter tengo CONSULTA, RESPUESTA_RAG, MODELO_LLM, OLLAMA_URL, llamar_ollama().
Genera código que:
1) prompt_vacio = f"Responde brevemente: {CONSULTA}"
2) RESPUESTA_SIN_RAG = llamar_ollama(prompt_vacio, MODELO_LLM, OLLAMA_URL)
3) imprima "CON RAG:", RESPUESTA_RAG[:500]
4) imprima "SIN RAG:", RESPUESTA_SIN_RAG[:500]
5) USA_FUENTE = any(p in RESPUESTA_RAG.lower() for p in ["e.020", "norma", "artículo", "sobrecarga", "carga"])
6) print("USA_FUENTE:", USA_FUENTE)
No uses imports nuevos.""",
)

CELDA_Q9 = celda_solucion_alumno(
    variables=["RESPUESTA_SIN_RAG", "USA_FUENTE"],
    pasos=[
        "Generar RESPUESTA_SIN_RAG sin contexto",
        "Comparar con RESPUESTA_RAG",
        "Evaluar USA_FUENTE",
    ],
)
