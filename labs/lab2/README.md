# Lab 2 — Predicción de Resistencia a la Compresión

**Sesión 3** · Regresión supervisada con el dataset UCI de **resistencia a compresión del hormigón**.

## ¿Qué notebook abrir?

| Si… | Abre |
|-----|------|
| Sabes editar variables Python | `resistencia_compresion_alumno.ipynb` |
| Prefieres Copilot / Gemini / Cursor | `resistencia_compresion_alumno_ia.ipynb` + entrega `prompts_entregados.md` |

## Archivos

| Archivo | Uso |
|---------|-----|
| `resistencia_compresion_alumno.ipynb` | Vía manual — hiperparámetros (10 preguntas) |
| `resistencia_compresion_alumno_ia.ipynb` | Vía IA — prompts y pegar código |
| `resistencia_compresion_solucion.ipynb` | Referencia docente (manual) |
| `resistencia_compresion_solucion_ia.ipynb` | Referencia docente (prompts canónicos) |
| `prompts_entregados.md` | Bitácora de prompts (entrega vía IA) |
| `_verificar.py` | Autoevaluación ✅ / ❌ (ambas vías) |
| `_generar_notebooks.py` | Regenera los cuatro notebooks |
| `_preparar_datos.py` | Convierte `data/Concrete_Data.xls` → `data/concrete.csv` |
| `data/DATOS.md` | Documentación de variables |
| `data/concrete.csv` | Dataset listo (1 030 × 9) |

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab2
jupyter notebook resistencia_compresion_alumno.ipynb
```

## GitHub Codespaces

Abrir `labs/lab2/resistencia_compresion_alumno.ipynb`

Guía del curso: [Lab 2 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab2/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)
