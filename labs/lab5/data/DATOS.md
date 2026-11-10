# Corpus del Lab 5 — Normas técnicas peruanas

Documentos en [`../pdfs/`](../pdfs/), indexados por el servidor MCP `normas`
(knowledge-rag, configurado en [`../rag/config.yaml`](../rag/config.yaml)).
Todo se procesa **en tu máquina**: los PDFs no se suben a ningún índice en la
nube (los fragmentos que el agente recupera sí se envían al modelo como
contexto de la conversación).

## Archivos

| PDF | Norma | Tema | Tamaño aprox. | Texto extraíble |
|-----|-------|------|---------------|-----------------|
| `Norma_E_020_CARGAS.pdf` | **E.020** | Cargas: muerta, viva, viento, nieve | ~470 KB | Sí |
| `Norma_E_030_SISMO.pdf` | **E.030** | Diseño sismorresistente | ~18 MB | Sí — copia OCR en `../pdfs_ocr/` (68 páginas) |
| `Norma_E_050_SUELOS.pdf` | **E.050** | Suelos y cimentaciones | ~865 KB | Sí |

El PDF original de la E.030 es escaneado. `ocr_e030.py` genera una copia con
capa de texto invisible en `../pdfs_ocr/`; esa es la copia que indexa el MCP.
El original no se modifica.

## Consultas de ejemplo

- *«¿Qué tipos de sobrecarga considera la E.020?»* → E.020
- *«¿Cuándo es obligatorio un Estudio de Mecánica de Suelos?»* → E.050
- *«¿Cuál es el factor de zona Z para la zona 4?»* → E.030 (por RAG, con cita verificable)

## Límites

- El agente puede **alucinar** cifras o artículos: siempre contrastar con el
  fragmento citado y con la norma oficial vigente.
