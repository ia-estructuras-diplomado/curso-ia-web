# Corpus del Lab 5 — Normas técnicas peruanas (RAG)

Documentos en [`../pdfs/`](../pdfs/) para construir un sistema **RAG** (Retrieval-Augmented Generation) con **Ollama** en local.

## Archivos

| PDF | Norma | Tema en obra | Tamaño aprox. |
|-----|-------|--------------|---------------|
| `Norma_E_020_CARGAS.pdf` | **E.020** | Cargas: dead load, live load, viento, nieve | ~470 KB |
| `Norma_E_030_SISMO.pdf` | **E.030** | Diseño sismorresistente | ~18 MB |
| `Norma_E_050_SUELOS.pdf` | **E.050** | Estudios de suelos y cimentaciones | ~865 KB |

## Uso en el laboratorio

| PDF | Estrategia didáctica |
|-----|---------------------|
| **E.020** | PDF **activo** en las primeras secciones (extracción, chunks, primera consulta) |
| **E.050** | Se indexa junto con E.020 a partir de la sección de embeddings |
| **E.030** | Solo las **primeras 30 páginas** en la celda pre-escrita (evita tiempos largos y memoria en Codespaces) |

## Consultas de ejemplo (ingeniería estructural)

- *«¿Qué tipos de sobrecarga considera la norma de cargas?»* → E.020
- *«¿Qué parámetros geotécnicos debe incluir un estudio de suelos?»* → E.050
- *«¿Qué zonas sísmicas define la norma?»* → E.030 (muestra parcial)

## Privacidad y límites

- Los PDFs **no salen del entorno** (Codespaces o máquina local).
- El LLM puede **alucinar** cifras o artículos: siempre contrastar con el fragmento recuperado y la norma oficial vigente.
- Este lab **no sustituye** el criterio de un ingeniero estructural ni la normativa oficial publicada por el ente regulador.
