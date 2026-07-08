"""Prompts IA y celdas vacías para Lab 3 — importar desde _generar_notebooks.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from _ia_helpers import celda_solucion_alumno, ia_guia_seccion  # noqa: E402

IA_Q1 = ia_guia_seccion(
    "1",
    "Panorama xAI",
    "Listar las técnicas de explicación que aplicarás en este lab (kit completo).",
    [
        "Definir `TECNICAS_XAI` como lista con al menos 4 técnicas",
        "Incluir importancia, shap, lime y pdp",
        "Imprimir la lista",
    ],
    vars_autoeval=["TECNICAS_XAI"],
    consideraciones=[
        "Este lab aplica varias técnicas sobre el mismo XGBoost — no solo una",
        "Nombres sugeridos: importancia, permutation, shap, lime, pdp",
        "Global = importancia/permutation/PDP; local = SHAP waterfall y LIME",
    ],
    prompt="""Estoy en el Lab 3 de xAI con XGBoost y sensores SHM.
Genera código que:
1) defina TECNICAS_XAI = ["importancia", "permutation", "shap", "lime", "pdp"]
2) imprima "Técnicas xAI que aplicarás en este lab:"
3) recorra la lista e imprima cada técnica con print(f"  · {t}")
No uses imports nuevos.""",
)

CELDA_Q1 = celda_solucion_alumno(
    variables=["TECNICAS_XAI"],
    pasos=[
        "Lista con importancia, shap, lime, pdp (y opcional permutation)",
        "Imprimir cada técnica",
    ],
)

IA_Q2 = ia_guia_seccion(
    "2",
    "Carga del dataset",
    "Definir las 5 features de sensor y mostrar las primeras filas del CSV.",
    [
        "Lista `FEATURES` con los 5 nombres exactos de columnas",
        "`N_FILAS_HEAD` entre 1 y 20",
        "Mostrar `df.head(N_FILAS_HEAD)` con display",
    ],
    vars_autoeval=["FEATURES", "N_FILAS_HEAD"],
    consideraciones=[
        "La celda anterior ya cargó `df` desde `data/building_health_monitoring_dataset.csv` (1000×7)",
        "No incluir `Timestamp` ni `Condition Label` en FEATURES",
        "Nombres exactos: Accel_X (m/s^2), Accel_Y (m/s^2), Accel_Z (m/s^2), Strain (με), Temp (°C)",
    ],
    prompt="""En Jupyter ya tengo `df` cargado (1000 filas, 7 columnas) del CSV de monitoreo estructural.
Genera código que:
1) defina FEATURES como lista con las 5 columnas de sensores (sin Timestamp ni Condition Label)
2) defina N_FILAS_HEAD = 5
3) imprima FEATURES
4) muestre df.head(N_FILAS_HEAD) con display()
Usa los nombres de columna exactos del dataset.""",
)

CELDA_Q2 = celda_solucion_alumno(
    variables=["FEATURES", "N_FILAS_HEAD"],
    pasos=[
        "Definir FEATURES (5 sensores, nombres exactos)",
        "Definir N_FILAS_HEAD",
        "Imprimir FEATURES y mostrar df.head()",
    ],
)

IA_Q3 = ia_guia_seccion(
    "3",
    "Limpieza y revisión de sensor",
    "Elegir un sensor y mostrar sus estadísticas en datos crudos.",
    [
        "Definir `COLUMNA_REVISAR` con un nombre de sensor válido",
        "Calcular `.describe()` sobre `df[COLUMNA_REVISAR]`",
        "Mostrar el resultado",
    ],
    vars_autoeval=["COLUMNA_REVISAR"],
    consideraciones=[
        "La celda anterior ya hizo dropna y creó `df_limpio`, `n_antes`, `n_despues`",
        "Tu tarea es revisar un sensor en datos **crudos** (`df`), no en df_limpio",
        "Strain (με) es el sensor más relevante para daño estructural",
    ],
    prompt="""En Jupyter tengo `df` (crudo) y `df_limpio` (sin nulos en FEATURES).
Genera código que:
1) defina COLUMNA_REVISAR = "Strain (με)"
2) calcule stats_col = df[COLUMNA_REVISAR].describe()
3) imprima el nombre de la columna y muestre stats_col con display()""",
)

CELDA_Q3 = celda_solucion_alumno(
    variables=["COLUMNA_REVISAR", "stats_col"],
    pasos=[
        "Elegir COLUMNA_REVISAR (sensor válido)",
        "Calcular describe() en df",
        "Imprimir y mostrar estadísticas",
    ],
)

IA_Q4 = ia_guia_seccion(
    "4",
    "Balance de clases",
    "Mostrar el conteo de las clases de Condition Label.",
    [
        "Definir `N_CLASES_MOSTRAR` (1 a 3)",
        "Usar el dict `conteo` ya calculado",
        "Mostrar las primeras N clases ordenadas",
    ],
    vars_autoeval=["N_CLASES_MOSTRAR"],
    consideraciones=[
        "La celda anterior ya graficó y creó `conteo` desde df_limpio['Condition Label']",
        "Clases: 0=normal, 1=daño menor, 2=daño severo",
        "N_CLASES_MOSTRAR = 3 muestra las tres clases",
    ],
    prompt="""En Jupyter ya existe conteo = dict con value_counts de Condition Label.
Genera código que:
1) defina N_CLASES_MOSTRAR = 3
2) cree serie_clases = pd.Series(conteo).sort_index().head(N_CLASES_MOSTRAR)
3) imprima cuántas clases muestra y display(serie_clases)""",
)

CELDA_Q4 = celda_solucion_alumno(
    variables=["N_CLASES_MOSTRAR", "serie_clases"],
    pasos=[
        "Definir N_CLASES_MOSTRAR",
        "Construir serie desde conteo",
        "Mostrar distribución",
    ],
)

IA_Q5 = ia_guia_seccion(
    "5",
    "Entrenar XGBoost",
    "Configurar hiperparámetros y entrenar el clasificador multiclass.",
    [
        "Definir N_ESTIMATORS, MAX_DEPTH, LEARNING_RATE en rangos válidos",
        "Crear XGBClassifier con objective='multi:softprob' y num_class=3",
        "Entrenar con modelo.fit(X_train, y_train)",
    ],
    vars_autoeval=["modelo", "N_ESTIMATORS", "MAX_DEPTH", "LEARNING_RATE"],
    consideraciones=[
        "X_train, X_test, y_train, y_test y RANDOM_STATE=42 ya existen (split estratificado)",
        "Rangos válidos: n_estimators 10–500, max_depth 2–12, learning_rate 0.01–0.5",
        "Usar eval_metric='mlogloss' y random_state=RANDOM_STATE",
    ],
    prompt="""En Jupyter tengo X_train, X_test, y_train, y_test (datos escalados, stratify) y RANDOM_STATE=42.
Genera código que:
1) defina N_ESTIMATORS=100, MAX_DEPTH=6, LEARNING_RATE=0.1
2) cree modelo = XGBClassifier(objective='multi:softprob', num_class=3, n_estimators=..., max_depth=..., learning_rate=..., random_state=RANDOM_STATE, eval_metric='mlogloss')
3) entrene con modelo.fit(X_train, y_train)
4) imprima confirmación de entrenamiento""",
)

CELDA_Q5 = celda_solucion_alumno(
    variables=["N_ESTIMATORS", "MAX_DEPTH", "LEARNING_RATE", "modelo"],
    pasos=[
        "Definir hiperparámetros",
        "Instanciar XGBClassifier multiclass",
        "Entrenar el modelo",
    ],
)

IA_Q6 = ia_guia_seccion(
    "6",
    "Métricas de clasificación",
    "Matriz de confusión y classification_report.",
    [
        "Construir matriz de confusión 3×3",
        "Graficar heatmap con seaborn",
        "Imprimir classification_report",
    ],
    vars_autoeval=[],
    consideraciones=[
        "modelo, X_test, y_test ya existen; la celda anterior calculó y_pred y acc_test",
        "La autoevaluación usa acc_test de la celda pre-escrita y N_ESTIMATORS/MAX_DEPTH/LEARNING_RATE de la sección 5",
        "Usa labels=[0, 1, 2] en confusion_matrix",
        "La autoevaluación reutiliza acc_test de la celda pre-escrita",
    ],
    prompt="""En Jupyter tengo y_test, y_pred (predicciones del XGBoost en test).
Genera código que:
1) calcule cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])
2) dibuje heatmap con sns.heatmap (annot=True, ejes Real/Predicho)
3) imprima classification_report(y_test, y_pred, digits=3)
Incluye plt.show().""",
)

CELDA_Q6 = celda_solucion_alumno(
    variables=["cm"],
    pasos=[
        "Matriz de confusión 3 clases",
        "Heatmap etiquetado",
        "classification_report",
    ],
    nota="acc_test ya está definido en la celda pre-escrita anterior.",
)

IA_Q7 = ia_guia_seccion(
    "7",
    "xAI global — importancia del booster",
    "Identificar el top-3 de features por importancia del booster (la celda pre-escrita ya muestra permutation).",
    [
        "Calcular importancias desde modelo.feature_importances_",
        "Definir TOP3_IMPORTANCIA (lista de 3 nombres)",
        "Imprimir el top-3",
    ],
    vars_autoeval=["TOP3_IMPORTANCIA"],
    consideraciones=[
        "imp_series ya está graficado en la celda pre-escrita",
        "Puedes reutilizar imp_series o recalcular desde modelo",
        "Se espera que Strain (με) esté en el top-3 (coherencia física)",
    ],
    prompt="""En Jupyter tengo modelo (XGBoost entrenado) y FEATURES (lista de 5 sensores).
Genera código que:
1) ordene importancias en una Series indexada por FEATURES
2) defina TOP3_IMPORTANCIA = lista con los 3 nombres más importantes
3) imprima TOP3_IMPORTANCIA""",
)

CELDA_Q7 = celda_solucion_alumno(
    variables=["TOP3_IMPORTANCIA"],
    pasos=[
        "Ordenar feature_importances_",
        "Extraer top-3 nombres",
        "Imprimir resultado",
    ],
)

IA_Q8 = ia_guia_seccion(
    "8",
    "SHAP global",
    "Summary plot de SHAP para una clase de daño.",
    [
        "Definir CLASE_SHAP (0, 1 o 2)",
        "Graficar shap.summary_plot para esa clase",
        "Título que indique la clase explicada",
    ],
    vars_autoeval=["CLASE_SHAP"],
    consideraciones=[
        "explainer, shap_values y la función shap_values_clase() ya están en la celda pre-escrita",
        "Usa shap_values_clase(shap_values, CLASE_SHAP) — no indexes shap_values[CLASE_SHAP] directo",
        "CLASE_SHAP=2 explica daño severo (recomendado para alertas)",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo modelo, X_test, FEATURES, shap_values y la función:

def shap_values_clase(shap_values, clase):
    if isinstance(shap_values, list):
        return shap_values[clase]
    return shap_values[:, :, clase]

Genera código que:
1) defina CLASE_SHAP = 2
2) cree figura plt.figure(figsize=(8, 5))
3) llame shap.summary_plot(shap_values_clase(shap_values, CLASE_SHAP), X_test, feature_names=FEATURES, show=False)
4) ponga título con la clase y plt.show()""",
)

CELDA_Q8 = celda_solucion_alumno(
    variables=["CLASE_SHAP"],
    pasos=[
        "Elegir CLASE_SHAP (0, 1 o 2)",
        "Summary plot con shap_values_clase()",
        "Título y plt.show()",
    ],
    nota="Usa shap_values_clase() de la celda pre-escrita.",
)

IA_Q9 = ia_guia_seccion(
    "9",
    "SHAP local (waterfall)",
    "Explicar una predicción individual del conjunto de test.",
    [
        "Definir INDEX_CASO válido en test",
        "Obtener y_true_caso y y_pred_caso",
        "Graficar waterfall SHAP para ese caso",
    ],
    vars_autoeval=["INDEX_CASO", "y_true_caso", "y_pred_caso"],
    consideraciones=[
        "etiqueta_en_test(idx) ya está definida en la celda pre-escrita",
        "Usa CLASE_SHAP de la sección anterior para elegir qué clase explicar",
        "Para expected_value multiclass, si es lista/array toma el índice CLASE_SHAP",
        "INDEX_CASO debe estar entre 0 y len(X_test)-1",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo X_test, y_test, y_pred, shap_values, explainer, FEATURES, CLASE_SHAP
y la función etiqueta_en_test(idx) que devuelve (y_true, y_pred).

También existe shap_values_clase(shap_values, clase).

Genera código que:
1) defina INDEX_CASO = 0
2) obtenga y_true_caso, y_pred_caso = etiqueta_en_test(INDEX_CASO) e imprima ambos
3) tome sv = shap_values_clase(shap_values, CLASE_SHAP)[INDEX_CASO]
4) base = explainer.expected_value; si es lista o ndarray, base = base[CLASE_SHAP]
5) cree exp = shap.Explanation(values=sv, base_values=base, data=X_test[INDEX_CASO], feature_names=FEATURES)
6) llame shap.plots.waterfall(exp, max_display=6, show=False) y plt.show()""",
    prompt_alt="Prueba INDEX_CASO=5 si quieres otro caso; imprime si acertó o no antes del gráfico.",
)

CELDA_Q9 = celda_solucion_alumno(
    variables=["INDEX_CASO", "y_true_caso", "y_pred_caso"],
    pasos=[
        "Elegir INDEX_CASO",
        "Imprimir etiquetas real y predicha",
        "Waterfall SHAP del caso",
    ],
    nota="Reutiliza CLASE_SHAP, shap_values_clase y etiqueta_en_test.",
)

IA_Q10 = ia_guia_seccion(
    "10",
    "LIME local",
    "Explicar el mismo caso de test con LIME y comparar con SHAP (sección 9).",
    [
        "Usar el mismo INDEX_CASO y CLASE_SHAP",
        "Llamar explainer_lime.explain_instance con modelo.predict_proba",
        "Graficar con as_pyplot_figure(label=CLASE_SHAP)",
        "Definir TOP_LIME_FEATURES (3 nombres de sensor)",
    ],
    vars_autoeval=["TOP_LIME_FEATURES"],
    consideraciones=[
        "explainer_lime ya está creado en la celda pre-escrita",
        "Reutiliza INDEX_CASO de la sección 9 (ejecútala antes)",
        "LIME devuelve umbrales (ej. 'Strain (με) <= -0.68') — normaliza a nombre de sensor",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo explainer_lime, modelo, X_test, INDEX_CASO, CLASE_SHAP, FEATURES.
Genera código que:
1) exp_lime = explainer_lime.explain_instance(X_test[INDEX_CASO], modelo.predict_proba, num_features=5, labels=(CLASE_SHAP,))
2) fig = exp_lime.as_pyplot_figure(label=CLASE_SHAP); plt.title(...); plt.show()
3) TOP_LIME_FEATURES = [next((f for f in FEATURES if feat.startswith(f)), feat.split('<=')[0].strip()) for feat, _ in exp_lime.as_list(label=CLASE_SHAP)[:3]]
4) print(TOP_LIME_FEATURES)
Nota: LIME devuelve umbrales (ej. "Strain (με) <= -0.68"); normaliza al nombre del sensor.""",
)

CELDA_Q10 = celda_solucion_alumno(
    variables=["TOP_LIME_FEATURES"],
    pasos=[
        "explain_instance en INDEX_CASO",
        "Gráfico LIME para CLASE_SHAP",
        "Extraer TOP_LIME_FEATURES (3 sensores)",
    ],
    nota="Mismo INDEX_CASO que SHAP local (sección 9).",
)

IA_Q11 = ia_guia_seccion(
    "11",
    "PDP y SHAP dependence",
    "Partial dependence y dependence plot para una feature adicional.",
    [
        "Definir FEATURE_PDP (nombre de sensor válido)",
        "PDP con PartialDependenceDisplay y target=CLASE_SHAP",
        "SHAP dependence_plot para la misma feature",
    ],
    vars_autoeval=["FEATURE_PDP"],
    consideraciones=[
        "modelo es multiclass: PDP requiere target=CLASE_SHAP",
        "Usa shap_values_clase(shap_values, CLASE_SHAP) en dependence_plot",
        "La celda pre-escrita ya muestra PDP de Strain; tu tarea es otra feature (ej. Temp)",
    ],
    prompt_listo=True,
    prompt="""En Jupyter tengo modelo, X_test, FEATURES, shap_values, CLASE_SHAP
y shap_values_clase(shap_values, clase).

Genera código que:
1) defina FEATURE_PDP = "Temp (°C)"
2) idx_pdp = FEATURES.index(FEATURE_PDP)
3) PDP: PartialDependenceDisplay.from_estimator(modelo, X_test, [idx_pdp], feature_names=FEATURES, target=CLASE_SHAP, ax=ax) con título
4) dependence: shap.dependence_plot(idx_pdp, shap_values_clase(shap_values, CLASE_SHAP), X_test, feature_names=FEATURES, show=False)
Incluye plt.show() en cada gráfico.""",
)

CELDA_Q11 = celda_solucion_alumno(
    variables=["FEATURE_PDP", "idx_pdp"],
    pasos=[
        "Elegir FEATURE_PDP",
        "Gráfico PDP con target=CLASE_SHAP",
        "Gráfico SHAP dependence",
    ],
    nota="Multiclass: no olvides target=CLASE_SHAP en el PDP.",
)
