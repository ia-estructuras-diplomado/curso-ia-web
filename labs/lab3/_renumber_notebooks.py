#!/usr/bin/env python3
"""Light pass: pipeline cheat sheet + fix section numbering in Lab 3 notebooks."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

CNN_PIPELINE = """## Mapa del flujo típico de deep learning

Cada **Pregunta** del lab sigue el pipeline estándar de un proyecto DL. Úsalo como brújula:

| Paso DL | Pregunta | Qué haces aquí |
|---------|----------|----------------|
| 1. Problema y contexto | **1** | ¿Por qué CNN para grietas? |
| 2. Explorar datos | **2** | EDA, balance de clases, muestras |
| 3. Preprocesar / aumentar | **3** | Resize, normalize, augmentation |
| 4. Pipeline de datos | **4** | DataLoaders train/val |
| 5. Diseñar modelo | **5** | Arquitectura CNN (tu modelo pequeño) |
| 6. Modelo de referencia | **6** | Cargar checkpoint docente (sin reentrenar) |
| 7. Entrenar | **7** | Loss, optimizer, bucle corto en CPU |
| 8. Monitorear | **8** | Curvas train vs val (¿overfitting?) |
| 9. Comparar | **9** | Tu modelo vs docente (épocas e hiperparámetros) |
| 10. Evaluar | **10** | Métricas y matriz de confusión (docente) |
| 11. Analizar errores | **11** | Casos locales: aciertos y fallos |
| 12. Decisión ingeniería | **12** | ¿Desplegarías esto en obra? |

> **Idea clave:** el proceso es siempre el mismo; cambian los datos y la arquitectura (CNN aquí, LSTM en Parte 2).
"""

LSTM_PIPELINE = """## Mapa del flujo típico de deep learning

Cada **Pregunta** del lab sigue el pipeline estándar de un proyecto DL. Úsalo como brújula:

| Paso DL | Pregunta | Qué haces aquí |
|---------|----------|----------------|
| 1. Problema y contexto | **1** | ¿Por qué LSTM para sensores SHM? |
| 2. Cargar y ordenar datos | **2** | CSV temporal, orden cronológico |
| 3. Calidad de datos | **3** | Limpieza, balance de etiquetas |
| 4. Explorar series | **4–5** | EDA global y por condición estructural |
| 5. Ventanas temporales | **6** | Sliding windows + split temporal |
| 6. Diseñar modelo | **7** | Arquitectura LSTM (tu modelo pequeño) |
| 7. Modelo de referencia | **8** | Cargar clasificador docente |
| 8. Entrenar | **9** | Bucle corto en CPU |
| 9. Comparar | **10** | Tu LSTM vs docente |
| 10. Evaluar (regresión) | **11–12** | Interpolación y extrapolación Strain |
| 11. Decisión ingeniería | **13** | ¿Confiarías en alertas automáticas? |

> **Idea clave:** mismos pasos que en la CNN; aquí los datos son **secuencias**, no imágenes.
"""


def _src(cell: dict) -> str:
    return "".join(cell.get("source", []))


def _set_src(cell: dict, text: str) -> None:
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    cell["source"] = lines


def _insert_after(cells: list, idx: int, cell: dict) -> None:
    cells.insert(idx + 1, cell)


def _md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def add_pipeline_cheat_sheet(nb_path: Path, pipeline_md: str) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = nb["cells"]
    if any("Mapa del flujo típico" in _src(c) for c in cells):
        return
    _insert_after(cells, 0, _md(pipeline_md))
    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  + cheat sheet → {nb_path.name}")


def replace_all(nb_path: Path, replacements: list[tuple[str, str]]) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    changed = False
    for cell in nb["cells"]:
        text = _src(cell)
        new = text
        for old, new_s in replacements:
            new = new.replace(old, new_s)
        if new != text:
            _set_src(cell, new)
            changed = True
    if changed:
        nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"  ✓ renumbered → {nb_path.name}")


def fix_cnn(nb_path: Path) -> None:
    replace_all(
        nb_path,
        [
            ("# Lab 4 Parte 1 —", "# Lab 3 Parte 1 —"),
            ("Estoy en el Lab 4 (CNN", "Estoy en el Lab 3 (CNN"),
            ("## Pregunta 10 — Reflexión ingeniería", "## Pregunta 12 — Reflexión ingeniería"),
            ("## Pregunta 9 — Casos locales", "## Pregunta 11 — Casos locales"),
            ("### 🤖 Guía IA — Sección 9: Casos", "### 🤖 Guía IA — Sección 11: Casos"),
            ("- **9.a** ¿La CNN mira", "- **11.a** ¿La CNN mira"),
            ("- **9.b** ¿Qué harías", "- **11.b** ¿Qué harías"),
            (
                "# --- Autoevaluación 9 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `N_CASOS_MOSTRADOS`",
                "# --- Autoevaluación 11 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `N_CASOS_MOSTRADOS`",
            ),
            ("resumen_seccion('9 — Casos locales'", "resumen_seccion('11 — Casos locales'"),
            ("## Pregunta 8 — Métricas en validación\n", "## Pregunta 10 — Métricas en validación (modelo docente)\n"),
            ("### 🤖 Guía IA — Sección 8: Métricas", "### 🤖 Guía IA — Sección 10: Métricas"),
            (
                "# --- Autoevaluación 8 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `acc_val`, `cm`",
                "# --- Autoevaluación 10 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `acc_val`, `cm`",
            ),
            ("resumen_seccion('9 — Métricas'", "resumen_seccion('10 — Métricas'"),
            ("- **8.a** ¿Qué clase se confunde más?", "- **10.a** ¿Qué clase se confunde más?"),
            ("- **8.b** ¿Un falso positivo (grieta)", "- **10.b** ¿Un falso positivo (grieta)"),
            ("# --- Autoevaluación 8 (comparación) ---", "# --- Autoevaluación 9 (comparación) ---"),
            ("resumen_seccion('8 — Comparación docente'", "resumen_seccion('9 — Comparación docente'"),
            (
                "## Pregunta 9 — Métricas en validación (modelo docente)\n\n"
                "Usamos el **modelo docente** para la matriz de confusión y el informe (mejor calidad que tu entrenamiento corto).\n\n"
                "### 📘 Subpreguntas\n"
                "- **9.a** ¿Qué clase se confunde más?\n"
                "- **9.b** ¿Un falso positivo (grieta) es más grave que un falso negativo?",
                "## Pregunta 9 — Comparación: tu modelo vs docente\n\n"
                "Entrenaste **pocas épocas en CPU** con una CNN más pequeña. El docente usó **más tiempo y mejores hiperparámetros**.\n\n"
                "### 📘 Subpreguntas\n"
                "- **9.a** ¿Cuánto mejora el modelo docente respecto al tuyo?\n"
                "- **9.b** ¿Qué cambió (épocas, `n_filters`, BatchNorm)?\n"
                "- **9.c** ¿Vale la pena en obra pagar más cómputo por ese salto?",
            ),
            ("## Pregunta 7 — Curvas de entrenamiento", "## Pregunta 8 — Curvas de entrenamiento"),
            ("### 🤖 Guía IA — Sección 7: Curvas", "### 🤖 Guía IA — Sección 8: Curvas"),
            (
                "# --- Autoevaluación 7 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`",
                "# --- Autoevaluación 8 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`",
            ),
            ("resumen_seccion('7 — Curvas'", "resumen_seccion('8 — Curvas'"),
            ("## Pregunta 6 — Entrenamiento\n", "## Pregunta 7 — Entrenamiento\n"),
            ("### 🤖 Guía IA — Sección 6: Entrenamiento", "### 🤖 Guía IA — Sección 7: Entrenamiento"),
            (
                "# --- Autoevaluación 6 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`, `LEARNING_RATE`",
                "# --- Autoevaluación 7 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`, `LEARNING_RATE`",
            ),
            ("resumen_seccion('6 — Entrenamiento'", "resumen_seccion('7 — Entrenamiento'"),
            ("## Pregunta 5b — Modelo docente (referencia)", "## Pregunta 6 — Modelo docente (referencia)"),
            ("- **5b.a**", "- **6.a**"),
            ("- **5b.b**", "- **6.b**"),
            (
                "\nacc_alumno = history['val_acc'][-1]\nprint(f\"✅ Entrenamiento corto | acc_val={acc_alumno:.3f}\")\n",
                "\n",
            ),
        ],
    )


def fix_lstm(nb_path: Path) -> None:
    replace_all(
        nb_path,
        [
            ("# Lab 4 Parte 2 —", "# Lab 3 Parte 2 —"),
            ("## Pregunta 11 — Reflexión ingeniería", "## Pregunta 13 — Reflexión ingeniería"),
            ("## Pregunta 10 — Test de extrapolación (Strain)", "## Pregunta 12 — Test de extrapolación (Strain)"),
            ("- **10.a** ¿El error crece", "- **12.a** ¿El error crece"),
            ("- **10.b** ¿Usarías esto", "- **12.b** ¿Usarías esto"),
            (
                "# --- Autoevaluación 10 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `mae_extrap`",
                "# --- Autoevaluación 12 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `mae_extrap`",
            ),
            ("resumen_seccion('10 — Extrapolación'", "resumen_seccion('12 — Extrapolación'"),
            ("## Pregunta 9 — Test de interpolación (Strain)", "## Pregunta 11 — Test de interpolación (Strain)"),
            ("- **9.a** ¿El modelo captura", "- **11.a** ¿El modelo captura"),
            ("- **9.b** ¿Interpolar es más fácil", "- **11.b** ¿Interpolar es más fácil"),
            (
                "# --- Autoevaluación 9 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `mae_interp`",
                "# --- Autoevaluación 11 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `mae_interp`",
            ),
            ("resumen_seccion('9 — Interpolación'", "resumen_seccion('11 — Interpolación'"),
            ("## Pregunta 9 — Comparación: tu LSTM vs docente", "## Pregunta 10 — Comparación: tu LSTM vs docente"),
            ("- **9.a** ¿Cuánto gana", "- **10.a** ¿Cuánto gana"),
            ("- **9.b** ¿Más `hidden_size`", "- **10.b** ¿Más `hidden_size`"),
            ("# --- Autoevaluación 9 (comparación) ---", "# --- Autoevaluación 10 (comparación) ---"),
            ("resumen_seccion('9 — Comparación docente'", "resumen_seccion('10 — Comparación docente'"),
            ("## Pregunta 8 — Entrenamiento y métricas", "## Pregunta 9 — Entrenamiento (modelo alumno)"),
            ("- **8.a** ¿Val accuracy", "- **9.a** ¿Val accuracy"),
            ("- **8.b** ¿Qué clase", "- **9.b** ¿Qué clase"),
            ("#### ✅ Reflexión 8\n\nAccuracy val", "#### ✅ Reflexión 9\n\nAccuracy val"),
            (
                "# --- Autoevaluación 8 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`, `LEARNING_RATE`, `acc_val`",
                "# --- Autoevaluación 9 ---\n"
                "# Requiere (celda «Aquí coloca tu solución»): `history`, `N_EPOCHS`, `LEARNING_RATE`, `acc_val`",
            ),
            ("resumen_seccion('8 — Entrenamiento'", "resumen_seccion('9 — Entrenamiento'"),
            ("## Pregunta 7b — Modelo docente LSTM (referencia)", "## Pregunta 8 — Modelo docente LSTM (referencia)"),
            ("- **7b.a**", "- **8.a**"),
            ("- **7b.b**", "- **8.b**"),
        ],
    )


def reorder_cnn_docente_before_train(nb_path: Path) -> None:
    """Order: Q6 docente → train funcs → Q7 entrenamiento."""
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = nb["cells"]

    def idx(needle: str) -> int:
        for i, c in enumerate(cells):
            if needle in _src(c):
                return i
        raise ValueError(f"Not found: {needle} in {nb_path.name}")

    i_q7 = idx("## Pregunta 7 — Entrenamiento")
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, device)")
    i_doc_md = idx("## Pregunta 6 — Modelo docente")
    if i_doc_md < i_funcs:
        return  # already ordered

    q7_hdr = cells.pop(i_q7)
    i_doc_md = idx("## Pregunta 6 — Modelo docente")
    i_doc_code = idx("load_crack_cnn(device=device)")
    doc_code = cells.pop(i_doc_code)
    doc_md = cells.pop(i_doc_md)
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, device)")
    cells.insert(i_funcs, doc_code)
    cells.insert(i_funcs, doc_md)
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, device)")
    cells.insert(i_funcs + 2, q7_hdr)

    for c in cells:
        t = _src(c)
        if t.startswith("## Pregunta 7 — Entrenamiento"):
            _set_src(
                c,
                "## Pregunta 7 — Entrenamiento\n\n"
                "### 📘 Subpreguntas\n"
                "- **7.a** ¿Qué optimizador y loss usas para clasificación binaria?\n"
                "- **7.b** ¿Cómo detectas overfitting con train vs val?\n",
            )

    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  ↕ reordered cells → {nb_path.name}")


def reorder_lstm_docente_before_train(nb_path: Path) -> None:
    """Order: Q8 docente → train funcs → Q9 entrenamiento."""
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = nb["cells"]

    def idx(needle: str) -> int:
        for i, c in enumerate(cells):
            if needle in _src(c):
                return i
        raise ValueError(f"Not found: {needle}")

    i_q9 = idx("## Pregunta 9 — Entrenamiento")
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, dev)")
    if i_q9 > i_funcs:
        return  # already ordered

    q9_hdr = cells.pop(i_q9)
    i_doc_md = idx("## Pregunta 8 — Modelo docente")
    i_doc_code = idx("load_lstm_classifier(device=device)")
    doc_code = cells.pop(i_doc_code)
    doc_md = cells.pop(i_doc_md)
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, dev)")
    cells.insert(i_funcs, doc_code)
    cells.insert(i_funcs, doc_md)
    i_funcs = idx("def train_one_epoch(model, loader, criterion, optimizer, dev)")
    cells.insert(i_funcs + 2, q9_hdr)

    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  ↕ reordered cells → {nb_path.name}")


def main() -> None:
    notebooks = [
        (ROOT / "part_1/cnn_grietas_estructuras_alumno_ia.ipynb", CNN_PIPELINE, fix_cnn),
        (ROOT / "part_1/cnn_grietas_estructuras_solucion.ipynb", CNN_PIPELINE, fix_cnn),
        (ROOT / "part_2/rnn_sensores_estructuras_alumno_ia.ipynb", LSTM_PIPELINE, fix_lstm),
        (ROOT / "part_2/rnn_sensores_estructuras_solucion.ipynb", LSTM_PIPELINE, fix_lstm),
    ]
    for path, pipeline, fix_fn in notebooks:
        add_pipeline_cheat_sheet(path, pipeline)
        fix_fn(path)

    for path in [
        ROOT / "part_1/cnn_grietas_estructuras_alumno_ia.ipynb",
        ROOT / "part_1/cnn_grietas_estructuras_solucion.ipynb",
    ]:
        reorder_cnn_docente_before_train(path)

    for path in [
        ROOT / "part_2/rnn_sensores_estructuras_alumno_ia.ipynb",
        ROOT / "part_2/rnn_sensores_estructuras_solucion.ipynb",
    ]:
        reorder_lstm_docente_before_train(path)


if __name__ == "__main__":
    main()
