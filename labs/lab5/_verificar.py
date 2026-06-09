"""Autoevaluación amigable para Lab 5 — RAG con Ollama y normativa estructural."""

from __future__ import annotations

from pathlib import Path

import numpy as np

PDFS_ESPERADOS = {
    "Norma_E_020_CARGAS.pdf",
    "Norma_E_030_SISMO.pdf",
    "Norma_E_050_SUELOS.pdf",
}
PDF_ACTIVO_REF = "Norma_E_020_CARGAS.pdf"
N_PDFS_REF = 3
E030_MAX_PAGINAS = 30
MODELO_LLM_REF = "llama3.2:3b"
MIN_CARACTERES_TEXTO = 500
MIN_CHUNKS = 3
MAX_CHUNKS = 5000
CHUNK_SIZE_MIN = 200
CHUNK_SIZE_MAX = 2000
TOP_K_MIN = 1
TOP_K_MAX = 8
MIN_RESPUESTA_CHARS = 20


def verificar(condicion: bool, ok: str, fail: str) -> bool:
    print(ok if condicion else fail)
    return condicion


def resumen_seccion(nombre: str, resultados: list[bool]) -> None:
    if all(resultados):
        print(f"\n✅ Sección {nombre} completada. Puedes continuar.")
    else:
        print(
            f"\n❌ Sección {nombre}: revisa tu celda «Aquí coloca tu solución» "
            "y vuelve a ejecutar."
        )


def _norm_paso(paso: str) -> str:
    return paso.strip().lower()


def listar_pdfs(directorio: Path | str = "pdfs") -> list[Path]:
    carpeta = Path(directorio)
    return sorted(carpeta.glob("*.pdf"))


def extraer_texto_pdf(
    ruta_pdf: Path | str,
    *,
    max_paginas: int | None = None,
) -> tuple[str, int]:
    from pypdf import PdfReader

    ruta = Path(ruta_pdf)
    reader = PdfReader(ruta)
    paginas = reader.pages[:max_paginas] if max_paginas else reader.pages
    partes = [(pg.extract_text() or "") for pg in paginas]
    return "\n".join(partes).strip(), len(reader.pages)


def fragmentar_texto(
    texto: str,
    chunk_size: int = 800,
    chunk_overlap: int = 100,
) -> list[str]:
    texto = " ".join(texto.split())
    if not texto:
        return []
    chunks: list[str] = []
    inicio = 0
    while inicio < len(texto):
        fin = min(inicio + chunk_size, len(texto))
        trozo = texto[inicio:fin].strip()
        if trozo:
            chunks.append(trozo)
        if fin >= len(texto):
            break
        inicio = max(fin - chunk_overlap, inicio + 1)
    return chunks


def cosine_top_k(
    query_vec: np.ndarray,
    matrix: np.ndarray,
    k: int,
) -> tuple[np.ndarray, np.ndarray]:
    q = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    m = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-9)
    scores = m @ q
    k = min(k, len(scores))
    idx = np.argsort(scores)[::-1][:k]
    return idx, scores[idx]


def llamar_ollama(
    prompt: str,
    modelo: str,
    url: str = "http://localhost:11434",
    *,
    timeout: int = 120,
) -> str:
    import requests

    resp = requests.post(
        f"{url.rstrip('/')}/api/generate",
        json={"model": modelo, "prompt": prompt, "stream": False},
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json().get("response", "").strip()


def verificar_pasos_rag(pasos: list[str]) -> list[bool]:
    if isinstance(pasos, str):
        pasos = [pasos]
    norm = [_norm_paso(p) for p in pasos]

    def tiene(*palabras: str) -> bool:
        return any(any(pal in p for pal in palabras) for p in norm)

    r = []
    r.append(
        verificar(
            len(norm) >= 5,
            f"✅ Pipeline RAG con {len(norm)} pasos definidos.",
            "❌ PASOS_RAG debe tener al menos 5 pasos (carga → generación).",
        )
    )
    r.append(
        verificar(
            tiene("carga", "extrac", "pdf", "document"),
            "✅ Incluye **carga / extracción** de documentos.",
            "❌ Añade un paso de carga o extracción de PDFs.",
        )
    )
    r.append(
        verificar(
            tiene("fragment", "chunk", "troce"),
            "✅ Incluye **fragmentación** (chunks).",
            "❌ Añade un paso de fragmentación o chunks.",
        )
    )
    r.append(
        verificar(
            tiene("embed", "vector", "embedding"),
            "✅ Incluye **embeddings** o vectorización.",
            "❌ Añade un paso de embeddings.",
        )
    )
    r.append(
        verificar(
            tiene("recuper", "retriev", "busqueda", "búsqueda", "top"),
            "✅ Incluye **recuperación** de fragmentos relevantes.",
            "❌ Añade un paso de recuperación (top-k).",
        )
    )
    r.append(
        verificar(
            tiene("gener", "llm", "ollama", "respuesta"),
            "✅ Incluye **generación** con LLM.",
            "❌ Añade un paso de generación con Ollama/LLM.",
        )
    )
    return r


def verificar_ollama(modelo: str, ollama_ok: bool) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(modelo, str) and len(modelo.strip()) >= 3,
            f"✅ MODELO_LLM = «{modelo}».",
            "❌ MODELO_LLM debe ser un nombre de modelo Ollama (ej. llama3.2:3b).",
        )
    )
    r.append(
        verificar(
            ollama_ok is True,
            "✅ Ollama responde en localhost:11434.",
            "❌ OLLAMA_OK es False. Ejecuta: bash labs/lab5/_ollama_setup.sh",
        )
    )
    return r


def verificar_inventario_pdfs(pdf_activo: str, n_pdfs: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_pdfs == N_PDFS_REF,
            f"✅ Inventario: {n_pdfs} PDFs en pdfs/.",
            f"❌ N_PDFS debe ser {N_PDFS_REF}.",
        )
    )
    r.append(
        verificar(
            pdf_activo in PDFS_ESPERADOS,
            f"✅ PDF_ACTIVO = «{pdf_activo}».",
            f"❌ PDF_ACTIVO debe ser uno de: {sorted(PDFS_ESPERADOS)}.",
        )
    )
    return r


def verificar_extraccion(
    texto_pdf: str,
    n_paginas: int,
    n_caracteres: int | None = None,
) -> list[bool]:
    n_car = n_caracteres if n_caracteres is not None else len(texto_pdf)
    r = []
    r.append(
        verificar(
            n_paginas >= 1,
            f"✅ PDF con {n_paginas} página(s) detectadas.",
            "❌ N_PAGINAS debe ser ≥ 1.",
        )
    )
    r.append(
        verificar(
            n_car >= MIN_CARACTERES_TEXTO,
            f"✅ Texto extraído: {n_car} caracteres.",
            f"❌ Muy poco texto ({n_car} chars). Revisa PDF_ACTIVO o la extracción.",
        )
    )
    r.append(
        verificar(
            isinstance(texto_pdf, str) and len(texto_pdf.strip()) >= MIN_CARACTERES_TEXTO,
            "✅ Variable texto_pdf contiene contenido utilizable.",
            "❌ texto_pdf está vacío o es demasiado corto.",
        )
    )
    return r


def verificar_chunks(
    chunks: list[str],
    n_chunks: int,
    chunk_size: int,
    chunk_overlap: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_chunks == len(chunks),
            f"✅ N_CHUNKS = {n_chunks} coincide con len(CHUNKS).",
            f"❌ N_CHUNKS ({n_chunks}) ≠ len(CHUNKS) ({len(chunks)}).",
        )
    )
    r.append(
        verificar(
            MIN_CHUNKS <= n_chunks <= MAX_CHUNKS,
            f"✅ {n_chunks} fragmentos generados.",
            f"❌ N_CHUNKS debe estar entre {MIN_CHUNKS} y {MAX_CHUNKS}.",
        )
    )
    r.append(
        verificar(
            CHUNK_SIZE_MIN <= chunk_size <= CHUNK_SIZE_MAX,
            f"✅ CHUNK_SIZE = {chunk_size}.",
            f"❌ CHUNK_SIZE debe estar entre {CHUNK_SIZE_MIN} y {CHUNK_SIZE_MAX}.",
        )
    )
    r.append(
        verificar(
            0 <= chunk_overlap < chunk_size,
            f"✅ CHUNK_OVERLAP = {chunk_overlap} (< CHUNK_SIZE).",
            "❌ CHUNK_OVERLAP debe ser ≥ 0 y menor que CHUNK_SIZE.",
        )
    )
    r.append(
        verificar(
            all(isinstance(c, str) and len(c.strip()) > 20 for c in chunks[:3]),
            "✅ Los chunks tienen texto legible.",
            "❌ CHUNKS contiene entradas vacías o demasiado cortas.",
        )
    )
    return r


def verificar_embeddings(
    embeddings: np.ndarray,
    n_vectores: int,
    n_chunks: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(embeddings, np.ndarray) and embeddings.ndim == 2,
            f"✅ EMBEDDINGS con forma {getattr(embeddings, 'shape', None)}.",
            "❌ EMBEDDINGS debe ser un array 2D (n_chunks × dim).",
        )
    )
    r.append(
        verificar(
            n_vectores == embeddings.shape[0] == n_chunks,
            f"✅ N_VECTORES = {n_vectores} alineado con chunks.",
            f"❌ N_VECTORES ({n_vectores}) debe igualar filas de EMBEDDINGS y N_CHUNKS ({n_chunks}).",
        )
    )
    r.append(
        verificar(
            embeddings.shape[1] >= 32,
            f"✅ Dimensión de embedding = {embeddings.shape[1]}.",
            "❌ Dimensión de embedding demasiado pequeña.",
        )
    )
    return r


def verificar_recuperacion(
    consulta: str,
    chunks_recuperados: list[str],
    top_k: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(consulta, str) and len(consulta.strip()) >= 10,
            f"✅ CONSULTA definida ({len(consulta.strip())} caracteres).",
            "❌ CONSULTA debe ser una pregunta técnica con al menos 10 caracteres.",
        )
    )
    r.append(
        verificar(
            TOP_K_MIN <= top_k <= TOP_K_MAX,
            f"✅ TOP_K = {top_k}.",
            f"❌ TOP_K debe estar entre {TOP_K_MIN} y {TOP_K_MAX}.",
        )
    )
    r.append(
        verificar(
            len(chunks_recuperados) == top_k,
            f"✅ Recuperados {len(chunks_recuperados)} fragmentos (top-{top_k}).",
            f"❌ CHUNKS_RECUPERADOS debe tener exactamente {top_k} entradas.",
        )
    )
    r.append(
        verificar(
            all(isinstance(c, str) and len(c.strip()) > 20 for c in chunks_recuperados),
            "✅ Fragmentos recuperados con contenido.",
            "❌ CHUNKS_RECUPERADOS contiene entradas vacías.",
        )
    )
    return r


def verificar_rag_respuesta(prompt_rag: str, respuesta_rag: str) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(prompt_rag, str) and len(prompt_rag.strip()) >= 100,
            f"✅ PROMPT_RAG armado ({len(prompt_rag.strip())} caracteres).",
            "❌ PROMPT_RAG debe incluir contexto recuperado (≥ 100 caracteres).",
        )
    )
    r.append(
        verificar(
            "contexto" in prompt_rag.lower() or "fragmento" in prompt_rag.lower(),
            "✅ PROMPT_RAG menciona contexto o fragmentos.",
            "❌ Incluye en PROMPT_RAG la palabra «contexto» o «fragmento» con los chunks.",
        )
    )
    r.append(
        verificar(
            isinstance(respuesta_rag, str) and len(respuesta_rag.strip()) >= MIN_RESPUESTA_CHARS,
            f"✅ RESPUESTA_RAG recibida ({len(respuesta_rag.strip())} caracteres).",
            "❌ RESPUESTA_RAG vacía. ¿Ollama está activo?",
        )
    )
    return r


def verificar_comparacion(
    respuesta_sin_rag: str,
    usa_fuente: bool,
    respuesta_rag: str | None = None,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(respuesta_sin_rag, str)
            and len(respuesta_sin_rag.strip()) >= MIN_RESPUESTA_CHARS,
            f"✅ RESPUESTA_SIN_RAG generada ({len(respuesta_sin_rag.strip())} caracteres).",
            "❌ RESPUESTA_SIN_RAG vacía.",
        )
    )
    r.append(
        verificar(
            usa_fuente is True,
            "✅ USA_FUENTE = True — la respuesta RAG cita o usa el contexto recuperado.",
            "❌ Marca USA_FUENTE = True solo si RESPUESTA_RAG menciona norma, artículo o contenido del fragmento.",
        )
    )
    if respuesta_rag is not None:
        r.append(
            verificar(
                len(respuesta_rag.strip()) >= MIN_RESPUESTA_CHARS,
                "✅ Comparación RAG vs sin contexto disponible.",
                "❌ Falta RESPUESTA_RAG de la sección anterior.",
            )
        )
    return r
