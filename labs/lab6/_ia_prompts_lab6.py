"""Prompts IA y celdas vacías para Lab 6 — importar desde _generar_notebooks.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from _ia_helpers import celda_solucion_alumno, ia_guia_seccion  # noqa: E402

IA_Q1 = ia_guia_seccion(
    "1",
    "Bucle ReAct",
    "Definir los pasos del bucle ReAct (Razonamiento + Acción) que seguirá el agente.",
    [
        "Definir `PASOS_REACT` como lista con al menos 4 pasos",
        "Incluir observación, razonamiento, acción con tools y verificación",
        "Imprimir la lista numerada",
    ],
    vars_autoeval=["PASOS_REACT"],
    consideraciones=[
        "ReAct = el LLM decide qué tool llamar según el objetivo",
        "En obra: el agente no calcula drift — invoca herramientas acotadas",
    ],
    prompt="""Estoy en Lab 6 (agentes sísmicos). Genera código que:
1) defina PASOS_REACT = ["Observar objetivo del usuario", "Razonar siguiente paso", "Invocar herramienta (tool call)", "Verificar resultado y sintetizar"]
2) imprima "Bucle ReAct:" y enumere cada paso numerado
No uses imports nuevos.""",
)

CELDA_Q1 = celda_solucion_alumno(
    variables=["PASOS_REACT"],
    pasos=["Lista ≥4 pasos ReAct", "Imprimir numerada"],
)

IA_Q2 = ia_guia_seccion(
    "2",
    "Entorno Ollama + best model",
    "Verificar Ollama, el CSV sísmico y el best model MLP entregado (.pkl).",
    [
        "Definir `MODELO_LLM = 'llama3.2:3b'` y comprobar `/api/tags` → `OLLAMA_OK`",
        "Comprobar que existe `data/earthquake_risk_model.pkl` → `PKL_OK`",
        "Contar filas del CSV → `N_FILAS_CSV`",
        "Leer meta → `TIPO_MODELO` debe contener 'MLP'",
    ],
    vars_autoeval=["MODELO_LLM", "OLLAMA_OK", "PKL_OK", "N_FILAS_CSV", "TIPO_MODELO"],
    consideraciones=[
        "Si OLLAMA_OK es False: bash labs/lab6/_ollama_setup.sh",
        "No re-entrenes el modelo — solo verifica el .pkl entregado",
    ],
    prompt="""En Jupyter Lab 6 necesito verificar entorno.
Genera código que:
1) MODELO_LLM = "llama3.2:3b"
2) OLLAMA_URL = "http://localhost:11434"; intente requests.get(.../api/tags); OLLAMA_OK = status==200
3) PKL_OK = Path("data/earthquake_risk_model.pkl").is_file()
4) N_FILAS_CSV = len(pd.read_csv("data/seismic_data.csv"))
5) meta = leer_meta_modelo(); TIPO_MODELO = meta.get("tipo","?")
6) imprima OLLAMA_OK, PKL_OK, N_FILAS_CSV, TIPO_MODELO
Usa requests, pandas, Path, leer_meta_modelo de _verificar.""",
)

CELDA_Q2 = celda_solucion_alumno(
    variables=["MODELO_LLM", "OLLAMA_OK", "PKL_OK", "N_FILAS_CSV", "TIPO_MODELO"],
    pasos=["Verificar Ollama", "Verificar pkl y CSV", "Leer TIPO_MODELO"],
)

IA_Q3 = ia_guia_seccion(
    "3",
    "Tool telemetría",
    "Implementar `get_building_telemetry(building_id)` usando `TELEMETRIA_DB`.",
    [
        "Función retorna dict del edificio o error si no existe",
        "Probar con BLDG-B y guardar en `TELEMETRIA_B`",
        "Imprimir claves principales",
    ],
    vars_autoeval=["TELEMETRIA_B"],
    consideraciones=[
        "TELEMETRIA_DB ya está en _verificar — no inventes otra base",
        "BLDG-B es concreto en suelo blando con drift > 2%",
    ],
    prompt="""Lab 6 — implementa get_building_telemetry(building_id: str) -> dict
Usa TELEMETRIA_DB importado de _verificar.
Luego TELEMETRIA_B = get_building_telemetry("BLDG-B") e imprime name, max_drift_ratio, material.""",
)

CELDA_Q3 = celda_solucion_alumno(
    variables=["TELEMETRIA_B"],
    pasos=["Definir get_building_telemetry", "Asignar TELEMETRIA_B"],
)

IA_Q4 = ia_guia_seccion(
    "4",
    "Tool normativa ASCE 7",
    "Implementar `check_seismic_code_compliance(max_drift_ratio, material)` con evaluar_drift_asce7.",
    [
        "Usar evaluar_drift_asce7 de _verificar",
        "Aplicar a BLDG-B → `RESULTADO_NORMA_B`",
        "Imprimir resultado",
    ],
    vars_autoeval=["RESULTADO_NORMA_B"],
    consideraciones=[
        "Límite depende del material: acero 2.5%, concreto 2.0%",
        "BLDG-B debe arrojar FALLO",
    ],
    prompt="""Implementa check_seismic_code_compliance(max_drift_ratio, material) -> str
usando evaluar_drift_asce7 de _verificar.
RESULTADO_NORMA_B = check_seismic_code_compliance(TELEMETRIA_B["max_drift_ratio"], TELEMETRIA_B["material"])
print(RESULTADO_NORMA_B)""",
)

CELDA_Q4 = celda_solucion_alumno(
    variables=["RESULTADO_NORMA_B"],
    pasos=["Definir check_seismic_code_compliance", "Evaluar BLDG-B"],
)

IA_Q5 = ia_guia_seccion(
    "5",
    "Tool ML (best model .pkl)",
    "Implementar predict_earthquake_vulnerability con predecir_probabilidad_dano.",
    [
        "Usar predecir_probabilidad_dano con pga, suelo, periodo, drift, height, material",
        "Asignar PROB_RIESGO_B y MSG_ML_B",
        "Imprimir probabilidad y mensaje",
    ],
    vars_autoeval=["PROB_RIESGO_B", "MSG_ML_B"],
    consideraciones=[
        "El .pkl es un MLPRegressor — no re-entrenar",
        "PROB_RIESGO_B debe ser > 0.70 para BLDG-B",
    ],
    prompt="""Implementa predict_earthquake_vulnerability(...) -> str que llame predecir_probabilidad_dano
con todos los campos de TELEMETRIA_B (expected_pga_g, soil_type_index, structural_period_s,
max_drift_ratio, height_m, material). Asigna PROB_RIESGO_B (float) y MSG_ML_B (str). Imprime ambos.""",
)

CELDA_Q5 = celda_solucion_alumno(
    variables=["PROB_RIESGO_B", "MSG_ML_B"],
    pasos=["Definir predict_earthquake_vulnerability", "Calcular PROB_RIESGO_B y MSG_ML_B"],
)

IA_Q6 = ia_guia_seccion(
    "6",
    "Configurar agente Agno",
    "Crear structural_bot con Ollama y 4 tools (telemetría, norma, ML, LaTeX).",
    [
        "Importar Agent y Ollama de agno",
        "Pasar las 4 funciones como tools",
        "instructions con flujo: telemetría → norma → ML → dictamen → export LaTeX",
        "N_TOOLS = 4",
    ],
    vars_autoeval=["N_TOOLS"],
    consideraciones=[
        "model=Ollama(id=MODELO_LLM)",
        "show_tool_calls=True para ver ReAct en consola",
    ],
    prompt="""Crea structural_bot = Agent(model=Ollama(id=MODELO_LLM), tools=[get_building_telemetry,
check_seismic_code_compliance, predict_earthquake_vulnerability, export_latex_report],
instructions=[...5-6 instrucciones en español...], show_tool_calls=True, markdown=True)
N_TOOLS = 4
No ejecutes aún el agente.""",
)

CELDA_Q6 = celda_solucion_alumno(
    variables=["N_TOOLS"],
    pasos=["Definir export_latex_report si falta", "Crear structural_bot", "N_TOOLS=4"],
)

IA_Q7 = ia_guia_seccion(
    "7",
    "Ejecutar agente BLDG-B",
    "Ejecutar el agente sobre BLDG-B y capturar RESPUESTA_B y TRAZA_HERRAMIENTAS.",
    [
        "Consulta en lenguaje natural sobre inspección BLDG-B",
        "Guardar texto final en RESPUESTA_B",
        "TRAZA_HERRAMIENTAS = lista con pasos registrados (usa lista global o atributo del run)",
    ],
    vars_autoeval=["RESPUESTA_B", "TRAZA_HERRAMIENTAS"],
    consideraciones=[
        "Requiere OLLAMA_OK=True",
        "Si falla Ollama, simula traza mínima documentando el error",
    ],
    prompt="""Ejecuta structural_bot.run(...) o print_response con consulta de inspección BLDG-B.
Captura RESPUESTA_B (str) y TRAZA_HERRAMIENTAS (list[str] con nombres de tools invocadas).
Si OLLAMA_OK es False, RESPUESTA_B = mensaje de error y TRAZA_HERRAMIENTAS = [].""",
)

CELDA_Q7 = celda_solucion_alumno(
    variables=["RESPUESTA_B", "TRAZA_HERRAMIENTAS"],
    pasos=["Ejecutar agente", "Capturar respuesta y traza"],
)

IA_Q8 = ia_guia_seccion(
    "8",
    "Contraste A / B / C",
    "Tabla comparativa determinista vs probabilístico para los 3 edificios.",
    [
        "Para BLDG-A, B, C ejecutar tools de norma y ML (sin agente)",
        "Construir TABLA_COMPARATIVA DataFrame con columnas: edificio, drift, norma, prob_ml",
    ],
    vars_autoeval=["TABLA_COMPARATIVA"],
    consideraciones=[
        "BLDG-C: norma OK pero ML alto — clave pedagógica",
    ],
    prompt="""Crea TABLA_COMPARATIVA (pandas DataFrame) con filas BLDG-A, BLDG-B, BLDG-C.
Columnas: edificio, drift, resultado_norma, prob_ml.
Usa get_building_telemetry, check_seismic_code_compliance y predecir_probabilidad_dano.""",
)

CELDA_Q8 = celda_solucion_alumno(
    variables=["TABLA_COMPARATIVA"],
    pasos=["Iterar A/B/C", "Armar DataFrame comparativo"],
)

IA_Q9 = ia_guia_seccion(
    "9",
    "Export LaTeX",
    "Implementar export_latex_report y generar informe_sismico.tex para BLDG-B.",
    [
        "Wrapper que llame generar_latex_report de _verificar",
        "RUTA_INFORME = Path('informe_sismico.tex')",
        "Incluir dictamen y traza en el .tex",
    ],
    vars_autoeval=["RUTA_INFORME"],
    consideraciones=[
        "No instalar TeX Live — solo generar .tex",
        "Escapar caracteres LaTeX via generar_latex_report",
    ],
    prompt="""Implementa export_latex_report(...) -> str usando generar_latex_report de _verificar.
Genera informe para BLDG-B con telemetría, RESULTADO_NORMA_B, MSG_ML_B, PROB_RIESGO_B,
TRAZA_HERRAMIENTAS y un dictamen breve. RUTA_INFORME = Path('informe_sismico.tex').""",
)

CELDA_Q9 = celda_solucion_alumno(
    variables=["RUTA_INFORME"],
    pasos=["Definir export_latex_report", "Generar informe_sismico.tex"],
)

IA_Q10 = ia_guia_seccion(
    "10",
    "Cierre MCP",
    "Reflexionar sobre puente hacia MCP y completar bitácora.",
    [
        "Definir `EJEMPLO_MCP` = una frase sobre cómo las tools serían un servidor MCP",
        "Imprimir EJEMPLO_MCP",
    ],
    vars_autoeval=["EJEMPLO_MCP"],
    consideraciones=[
        "Las 4 funciones Python = prototipo de servidor MCP",
        "Completa prompts_entregados.md",
    ],
    prompt="""Define EJEMPLO_MCP como string de 1-2 oraciones explicando que get_building_telemetry,
check_seismic_code_compliance, predict_earthquake_vulnerability y export_latex_report
podrían exponerse como tools MCP. Imprime EJEMPLO_MCP.""",
)

CELDA_Q10 = celda_solucion_alumno(
    variables=["EJEMPLO_MCP"],
    pasos=["Definir EJEMPLO_MCP", "Imprimir reflexión MCP"],
)
