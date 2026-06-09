"""Autoevaluación y caja de herramientas — Lab 6 Agentes sísmicos."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import joblib
import numpy as np

DIR = Path(__file__).parent
DATA_DIR = DIR / "data"
RUTA_PKL = DATA_DIR / "earthquake_risk_model.pkl"
RUTA_META = DATA_DIR / "model_meta.json"
RUTA_CSV = DATA_DIR / "seismic_data.csv"

SOIL_TO_INDEX: dict[str, int] = {"Rock": 1, "Sand": 2, "Clay": 3, "Soft Soil": 3}
COLLAPSE_THRESHOLD = 70.0
N_FILAS_CSV_REF = 1000

_modelo_cache: Any | None = None

TELEMETRIA_DB: dict[str, dict[str, Any]] = {
    "BLDG-A": {
        "name": "Torre Empresarial Alfa",
        "material": "Acero Estructural (A992)",
        "height_m": 107.0,
        "max_drift_ratio": 0.0054,
        "structural_period_s": 1.71,
        "expected_pga_g": 0.85,
        "soil_type_index": 1,
        "seismic_zone": "High",
        "foundation_type": "Deep",
        "lateral_system": "Moment Frame",
    },
    "BLDG-B": {
        "name": "Complejo Residencial Beta",
        "material": "Concreto Armado (f'c = 210 kg/cm²)",
        "height_m": 6.7,
        "max_drift_ratio": 0.0357,
        "structural_period_s": 0.37,
        "expected_pga_g": 1.49,
        "soil_type_index": 3,
        "seismic_zone": "Very High",
        "foundation_type": "Raft",
        "lateral_system": "Moment Frame",
    },
    "BLDG-C": {
        "name": "Centro Comercial Gamma",
        "material": "Composite (acero-concreto)",
        "height_m": 60.6,
        "max_drift_ratio": 0.0081,
        "structural_period_s": 0.22,
        "expected_pga_g": 0.40,
        "soil_type_index": 3,
        "seismic_zone": "Moderate",
        "foundation_type": "Deep",
        "lateral_system": "Braced Frame",
    },
}


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


def soil_type_to_index(soil: str) -> int:
    return SOIL_TO_INDEX.get(soil.strip(), 3)


def material_to_index(material: str) -> int:
    m = material.lower()
    if "acero" in m or "steel" in m:
        return 1
    if "concreto" in m or "concrete" in m:
        return 2
    if "masonry" in m or "mamposter" in m:
        return 3
    if "composite" in m:
        return 4
    return 2


def features_vector(
    expected_pga_g: float,
    soil_type_index: int,
    structural_period_s: float,
    max_drift_ratio: float = 0.0,
    height_m: float = 10.0,
    material: str = "Concrete",
) -> np.ndarray:
    return np.array(
        [
            [
                expected_pga_g,
                soil_type_index,
                structural_period_s,
                max_drift_ratio,
                height_m,
                float(material_to_index(material)),
            ]
        ],
        dtype=float,
    )


def fila_csv_a_features(row: dict[str, str]) -> list[float]:
    freq = float(row["Natural Frequency (Hz)"])
    period = 1.0 / freq if freq > 0 else 4.0
    return [
        float(row["Spectral Acceleration (g)"]),
        float(soil_type_to_index(row["Soil Type"])),
        period,
    ]


def target_colapso(row: dict[str, str]) -> int:
    return int(float(row["Predicted Collapse Probability (%)"]) >= COLLAPSE_THRESHOLD)


def limite_drift(material: str) -> float:
    m = material.lower()
    if "acero" in m or "steel" in m:
        return 0.025
    return 0.020


def evaluar_drift_asce7(max_drift_ratio: float, material: str) -> str:
    limit = limite_drift(material)
    if max_drift_ratio > limit:
        return (
            f"FALLO: El Drift Máximo de {max_drift_ratio:.3f} EXCEDE el límite normativo "
            f"de {limit:.3f} para estructuras de {material}."
        )
    return (
        f"APROBADO: El Drift Máximo de {max_drift_ratio:.3f} cumple con el umbral seguro "
        f"de {limit:.3f}."
    )


def clasificar_mensaje_ml(prob: float) -> str:
    if prob > 0.70:
        return (
            f"ALERTA CRÍTICA DE ML: El modelo neuronal predice un {prob * 100:.1f}% de "
            "probabilidad de colapso estructural. Vulnerabilidad sísmica muy elevada."
        )
    if prob > 0.40:
        return (
            f"RIESGO MODERADO DE ML: El modelo predice un {prob * 100:.1f}% de "
            "probabilidad de daño significativo. Requiere intervención a mediano plazo."
        )
    return (
        f"RIESGO BAJO DE ML: El modelo predice un {prob * 100:.1f}% de "
        "probabilidad de daño severo. Comportamiento dinámico resiliente."
    )


def cargar_modelo_sismico(ruta: Path | str | None = None) -> Any:
    global _modelo_cache
    path = Path(ruta) if ruta else RUTA_PKL
    if _modelo_cache is not None and path.resolve() == RUTA_PKL.resolve():
        return _modelo_cache
    if not path.is_file():
        raise FileNotFoundError(f"Modelo no encontrado: {path}")
    model = joblib.load(path)
    if path.resolve() == RUTA_PKL.resolve():
        _modelo_cache = model
    return model


def leer_meta_modelo(ruta: Path | str | None = None) -> dict[str, Any]:
    path = Path(ruta) if ruta else RUTA_META
    if not path.is_file():
        return {"tipo": "desconocido", "architecture": "N/A"}
    return json.loads(path.read_text(encoding="utf-8"))


def predecir_probabilidad_dano(
    expected_pga_g: float,
    soil_type_index: int,
    structural_period_s: float,
    *,
    max_drift_ratio: float = 0.0,
    height_m: float = 10.0,
    material: str = "Concrete",
    ruta_modelo: Path | str | None = None,
) -> tuple[float, str]:
    if soil_type_index not in (1, 2, 3):
        raise ValueError("soil_type_index debe ser 1 (duro), 2 (intermedio) o 3 (blando).")
    if expected_pga_g <= 0 or structural_period_s <= 0:
        raise ValueError("expected_pga_g y structural_period_s deben ser positivos.")
    try:
        model = cargar_modelo_sismico(ruta_modelo)
    except FileNotFoundError:
        return 0.0, "AVISO: Archivo del modelo de ML no encontrado. Saltando validación estadística."
    x = features_vector(
        expected_pga_g,
        soil_type_index,
        structural_period_s,
        max_drift_ratio,
        height_m,
        material,
    )
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(x)[0][1])
    else:
        prob = float(np.clip(model.predict(x)[0], 0.0, 1.0))
    return prob, clasificar_mensaje_ml(prob)


def latex_escape(texto: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    out = texto
    for k, v in repl.items():
        out = out.replace(k, v)
    return out


def generar_latex_report(
    building_id: str,
    telemetria: dict[str, Any],
    resultado_norma: str,
    msg_ml: str,
    prob_riesgo: float,
    traza: list[str],
    dictamen_markdown: str,
    ruta_salida: str | Path = "informe_sismico.tex",
) -> Path:
    bid = latex_escape(building_id)
    nombre = latex_escape(str(telemetria.get("name", building_id)))
    material = latex_escape(str(telemetria.get("material", "—")))
    zona = latex_escape(str(telemetria.get("seismic_zone", "—")))
    altura = telemetria.get("height_m", "—")
    drift = telemetria.get("max_drift_ratio", 0)
    pga = telemetria.get("expected_pga_g", 0)
    periodo = telemetria.get("structural_period_s", 0)
    suelo = telemetria.get("soil_type_index", "—")
    sistema = latex_escape(str(telemetria.get("lateral_system", "—")))

    traza_items = "\n".join(
        f"  \\item {latex_escape(t)}" for t in traza if t.strip()
    ) or r"  \item (sin traza registrada)"

    contenido = f"""\\documentclass[11pt]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[spanish]{{babel}}
\\usepackage{{geometry}}
\\geometry{{margin=2.5cm}}
\\usepackage{{booktabs}}

\\title{{Informe de Evaluación Sísmica Estructural}}
\\author{{Agente Inspector — {nombre}}}
\\date{{{date.today().isoformat()}}}

\\begin{{document}}
\\maketitle

\\section{{Identificación del edificio}}
\\begin{{tabular}}{{ll}}
\\toprule
Campo & Valor \\\\
\\midrule
ID & {bid} \\\\
Nombre & {nombre} \\\\
Material & {material} \\\\
Zona sísmica & {zona} \\\\
Altura (m) & {altura} \\\\
Drift máx. registrado & {drift:.4f} \\\\
PGA esperada (g) & {pga:.3f} \\\\
Periodo estructural (s) & {periodo:.2f} \\\\
Índice de suelo & {suelo} \\\\
Sistema resistente & {sistema} \\\\
\\bottomrule
\\end{{tabular}}

\\section{{Cumplimiento normativo (ASCE 7)}}
{latex_escape(resultado_norma)}

\\section{{Análisis probabilístico (MLP)}}
Probabilidad de daño severo/colapso: \\textbf{{{prob_riesgo * 100:.1f}\\%}}

{latex_escape(msg_ml)}

\\section{{Dictamen de ingeniería}}
{latex_escape(dictamen_markdown)}

\\appendix
\\section{{Trazabilidad del agente (ReAct)}}
\\begin{{itemize}}
{traza_items}
\\end{{itemize}}

\\end{{document}}
"""
    path = Path(ruta_salida)
    path.write_text(contenido, encoding="utf-8")
    return path


# --- Verificadores por sección ---


def verificar_pasos_react(pasos: list[str]) -> list[bool]:
    if isinstance(pasos, str):
        pasos = [pasos]
    norm = [p.strip().lower() for p in pasos]
    r = []
    r.append(
        verificar(
            len(norm) >= 4,
            f"✅ Bucle ReAct con {len(norm)} pasos definidos.",
            "❌ PASOS_REACT debe tener al menos 4 pasos.",
        )
    )

    def tiene(*palabras: str) -> bool:
        return any(any(p in paso for paso in norm) for p in palabras)

    r.append(
        verificar(
            tiene("observ", "percib", "leer", "consult"),
            "✅ Incluye fase de **observación**.",
            "❌ Añade un paso de observación/percepción.",
        )
    )
    r.append(
        verificar(
            tiene("pens", "razon", "plan"),
            "✅ Incluye fase de **razonamiento**.",
            "❌ Añade un paso de razonamiento/planificación.",
        )
    )
    r.append(
        verificar(
            tiene("act", "ejecut", "tool", "herramient"),
            "✅ Incluye fase de **acción** (tool call).",
            "❌ Añade un paso de acción con herramientas.",
        )
    )
    return r


def verificar_ollama(modelo: str, ollama_ok: bool) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(modelo, str) and len(modelo.strip()) >= 3,
            f"✅ MODELO_LLM = «{modelo}» (Ollama local).",
            "❌ MODELO_LLM debe ser un nombre de modelo Ollama (ej. llama3.2:3b).",
        )
    )
    if ollama_ok:
        r.append(verificar(True, "✅ Ollama responde en localhost:11434.", ""))
    else:
        print("⚠️ Ollama no disponible. Ejecuta: bash labs/lab6/_ollama_setup.sh")
        r.append(False)
    return r


def verificar_entorno(
    ollama_ok: bool,
    pkl_ok: bool,
    n_filas: int,
    tipo_modelo: str,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            pkl_ok,
            "✅ Best model `.pkl` encontrado.",
            f"❌ Falta {RUTA_PKL}. Ejecuta (docente): python _generar_modelo.py",
        )
    )
    r.append(
        verificar(
            n_filas == N_FILAS_CSV_REF,
            f"✅ CSV con {n_filas} filas.",
            f"❌ N_FILAS_CSV debe ser {N_FILAS_CSV_REF}. Ejecuta _preparar_datos.py",
        )
    )
    r.append(
        verificar(
            "mlp" in str(tipo_modelo).lower(),
            f"✅ Tipo de modelo: {tipo_modelo}.",
            f"❌ TIPO_MODELO debe contener 'MLP' (valor: {tipo_modelo}).",
        )
    )
    if ollama_ok:
        r.append(verificar(True, "✅ Ollama responde en localhost:11434.", ""))
    else:
        print("⚠️ Ollama no disponible — secciones 7+ pueden quedar limitadas.")
        r.append(True)
    return r


def verificar_telemetria_b(data: dict[str, Any]) -> list[bool]:
    r = []
    r.append(
        verificar(
            isinstance(data, dict) and "error" not in data,
            "✅ Telemetría BLDG-B cargada.",
            "❌ TELEMETRIA_B debe ser un dict válido (sin clave 'error').",
        )
    )
    if isinstance(data, dict) and "error" not in data:
        r.append(
            verificar(
                "max_drift_ratio" in data and data["max_drift_ratio"] > 0.02,
                f"✅ Drift BLDG-B = {data.get('max_drift_ratio', 0):.4f} (>2%).",
                "❌ BLDG-B debe tener max_drift_ratio > 0.02.",
            )
        )
        r.append(
            verificar(
                data.get("soil_type_index") == 3,
                "✅ Suelo blando (índice 3) en BLDG-B.",
                "❌ BLDG-B debe tener soil_type_index = 3.",
            )
        )
    return r


def verificar_resultado_norma_b(texto: str) -> list[bool]:
    t = (texto or "").upper()
    r = [
        verificar(
            "FALLO" in t,
            "✅ Norma detecta FALLO en BLDG-B (drift > límite concreto).",
            "❌ RESULTADO_NORMA_B debe contener 'FALLO' para BLDG-B.",
        )
    ]
    return r


def verificar_ml_b(prob: float, msg: str) -> list[bool]:
    r = []
    r.append(
        verificar(
            0.0 <= prob <= 1.0,
            f"✅ PROB_RIESGO_B = {prob:.3f} (probabilidad válida).",
            f"❌ PROB_RIESGO_B debe estar en [0,1] (valor: {prob}).",
        )
    )
    r.append(
        verificar(
            prob > 0.70,
            f"✅ Alerta ML crítica ({prob * 100:.1f}% > 70%).",
            f"❌ PROB_RIESGO_B debe ser > 0.70 para BLDG-B (valor: {prob:.3f}).",
        )
    )
    r.append(
        verificar(
            "ML" in (msg or "").upper() or "RIESGO" in (msg or "").upper(),
            "✅ MSG_ML_B describe el riesgo.",
            "❌ MSG_ML_B debe describir el resultado del modelo.",
        )
    )
    return r


def verificar_agente_config(bot: Any, n_tools: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            bot is not None,
            "✅ Agente `structural_bot` definido.",
            "❌ Define structural_bot con Agent(...).",
        )
    )
    r.append(
        verificar(
            n_tools == 4,
            "✅ Agente con 4 herramientas.",
            f"❌ N_TOOLS debe ser 4 (valor: {n_tools}).",
        )
    )
    return r


def verificar_respuesta_agente(respuesta: str, traza: list[str]) -> list[bool]:
    r = []
    texto = (respuesta or "").lower()
    r.append(
        verificar(
            len(texto) > 80,
            f"✅ RESPUESTA_B con {len(texto)} caracteres.",
            "❌ RESPUESTA_B demasiado corta — el agente debe generar un reporte.",
        )
    )
    r.append(
        verificar(
            isinstance(traza, list) and len(traza) >= 1,
            f"✅ TRAZA_HERRAMIENTAS con {len(traza) if isinstance(traza, list) else 0} entradas.",
            "❌ TRAZA_HERRAMIENTAS debe ser una lista no vacía.",
        )
    )
    return r


def verificar_tabla_comparativa(tabla: Any) -> list[bool]:
    r = []
    try:
        import pandas as pd

        if not isinstance(tabla, pd.DataFrame):
            r.append(verificar(False, "", "❌ TABLA_COMPARATIVA debe ser un pandas DataFrame."))
            return r
        r.append(
            verificar(
                len(tabla) >= 3,
                f"✅ Tabla con {len(tabla)} edificios.",
                "❌ TABLA_COMPARATIVA debe tener al menos 3 filas (A, B, C).",
            )
        )
        cols = {c.lower() for c in tabla.columns}
        r.append(
            verificar(
                "drift" in "".join(cols) or "norma" in "".join(cols),
                "✅ Columnas de drift/norma presentes.",
                "❌ Incluye columnas de drift y resultado normativo.",
            )
        )
    except ImportError:
        r.append(verificar(False, "", "❌ pandas no disponible."))
    return r


def verificar_latex_report(ruta: str | Path, building_id: str = "BLDG-B") -> list[bool]:
    path = Path(ruta)
    r = []
    r.append(
        verificar(
            path.is_file(),
            f"✅ Informe LaTeX generado: {path}",
            f"❌ No existe {path}.",
        )
    )
    if path.is_file():
        txt = path.read_text(encoding="utf-8")
        r.append(
            verificar(
                "\\section{Dictamen de ingeniería}" in txt,
                "✅ Sección Dictamen presente.",
                "❌ Falta \\section{Dictamen de ingeniería}.",
            )
        )
        r.append(
            verificar(
                building_id in txt,
                f"✅ Informe menciona {building_id}.",
                f"❌ El .tex debe mencionar {building_id}.",
            )
        )
    return r
