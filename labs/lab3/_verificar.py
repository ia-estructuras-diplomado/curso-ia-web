"""Autoevaluación amigable para Lab 3 — xAI con XGBoost y monitoreo estructural."""

from __future__ import annotations

COLUMNAS_ESPERADAS = [
    "Timestamp",
    "Accel_X (m/s^2)",
    "Accel_Y (m/s^2)",
    "Accel_Z (m/s^2)",
    "Strain (με)",
    "Temp (°C)",
    "Condition Label",
]

FEATURES_ESPERADAS = [
    "Accel_X (m/s^2)",
    "Accel_Y (m/s^2)",
    "Accel_Z (m/s^2)",
    "Strain (με)",
    "Temp (°C)",
]

N_FILAS_RAW = 1000
N_FILAS_LIMPIO = 904
N_FEATURES = 5
ETIQUETAS_VALIDAS = {0, 1, 2}
TOP_FEATURE_REF = "Strain (με)"
MIN_ACC_TEST = 0.75


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


def _norm_tecnica(nombre: str) -> str:
    return nombre.strip().lower().replace(" ", "_")


def verificar_panorama_xai(tecnicas: list[str]) -> list[bool]:
    """Comprueba que el alumno listó las familias xAI del lab."""
    if isinstance(tecnicas, str):
        tecnicas = [tecnicas]
    norm = [_norm_tecnica(t) for t in tecnicas]

    def tiene(*palabras: str) -> bool:
        return any(any(p in t for p in palabras) for t in norm)

    r = []
    r.append(
        verificar(
            len(norm) >= 4,
            f"✅ Panorama xAI con {len(norm)} técnicas listadas.",
            "❌ Define TECNICAS_XAI con al menos 4 entradas (importancia, shap, lime, pdp…).",
        )
    )
    r.append(
        verificar(
            tiene("importancia", "permutation"),
            "✅ Incluye explicación **global** (importancia o permutation).",
            "❌ Añade 'importancia' y/o 'permutation' a TECNICAS_XAI.",
        )
    )
    r.append(
        verificar(
            tiene("shap"),
            "✅ Incluye **SHAP** (global y local en este lab).",
            "❌ Añade 'shap' a TECNICAS_XAI.",
        )
    )
    r.append(
        verificar(
            tiene("lime"),
            "✅ Incluye **LIME** (explicación local alternativa).",
            "❌ Añade 'lime' a TECNICAS_XAI.",
        )
    )
    r.append(
        verificar(
            tiene("pdp", "partial", "dependence"),
            "✅ Incluye **PDP / dependencia** (efecto marginal).",
            "❌ Añade 'pdp' a TECNICAS_XAI.",
        )
    )
    return r


def verificar_contexto_xai(metodo: str) -> list[bool]:
    """Compatibilidad: acepta un solo método o delega a panorama."""
    return verificar_panorama_xai([metodo, "shap", "lime", "pdp"])


def verificar_carga(df, n_filas_head: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            df is not None and df.shape == (N_FILAS_RAW, 7),
            f"✅ Dataset cargado: {N_FILAS_RAW} lecturas × 7 columnas.",
            f"❌ Forma inesperada: {getattr(df, 'shape', None)}. Usa data/building_health_monitoring_dataset.csv.",
        )
    )
    r.append(
        verificar(
            list(df.columns) == COLUMNAS_ESPERADAS,
            "✅ Columnas de sensores listas para SHM.",
            "❌ Revisa el CSV en data/building_health_monitoring_dataset.csv.",
        )
    )
    r.append(
        verificar(
            1 <= n_filas_head <= 20,
            f"✅ Mostrando {n_filas_head} filas con head().",
            "❌ N_FILAS_HEAD debe estar entre 1 y 20.",
        )
    )
    return r


def verificar_features(features: list[str]) -> list[bool]:
    return [
        verificar(
            features == FEATURES_ESPERADAS,
            "✅ 5 features de sensores definidas correctamente.",
            f"❌ FEATURES debe ser exactamente {FEATURES_ESPERADAS}.",
        )
    ]


def verificar_limpieza(df_limpio, n_antes: int, n_despues: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_antes == N_FILAS_RAW,
            f"✅ Partiste de {N_FILAS_RAW} registros crudos.",
            f"❌ Se esperaban {N_FILAS_RAW} filas antes de limpiar; hay {n_antes}.",
        )
    )
    r.append(
        verificar(
            n_despues == N_FILAS_LIMPIO and df_limpio.shape[0] == N_FILAS_LIMPIO,
            f"✅ Tras eliminar nulos: {N_FILAS_LIMPIO} lecturas válidas.",
            f"❌ Tras limpieza se esperaban {N_FILAS_LIMPIO} filas; obtuviste {n_despues}.",
        )
    )
    r.append(
        verificar(
            df_limpio[FEATURES_ESPERADAS].isna().sum().sum() == 0,
            "✅ Sin valores nulos en features de sensores.",
            "❌ Aún hay nulos en las columnas de sensores.",
        )
    )
    return r


def verificar_columna(df, col: str) -> list[bool]:
    return [
        verificar(
            col in df.columns,
            f"✅ Columna «{col}» encontrada.",
            f"❌ «{col}» no existe. Usa una feature de sensor válida.",
        )
    ]


def verificar_etiquetas(conteo: dict, n_clases_mostrar: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            set(conteo.keys()) == ETIQUETAS_VALIDAS,
            "✅ Tres clases de condición: 0 (normal), 1 (menor), 2 (severo).",
            f"❌ Etiquetas inesperadas: {sorted(conteo.keys())}.",
        )
    )
    r.append(
        verificar(
            1 <= n_clases_mostrar <= 3,
            f"✅ Mostrando distribución de {n_clases_mostrar} clase(s).",
            "❌ N_CLASES_MOSTRAR debe estar entre 1 y 3.",
        )
    )
    if conteo.get(0, 0) > conteo.get(2, 0):
        r.append(
            verificar(
                True,
                "✅ Clase 0 (normal) es mayoritaria — típico en SHM.",
                "",
            )
        )
    return r


def verificar_xgboost(
    acc_test: float,
    n_estimators: int,
    max_depth: int,
    learning_rate: float,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            10 <= n_estimators <= 500,
            f"✅ n_estimators={n_estimators} en rango razonable.",
            "❌ N_ESTIMATORS debe estar entre 10 y 500.",
        )
    )
    r.append(
        verificar(
            2 <= max_depth <= 12,
            f"✅ max_depth={max_depth} configurado.",
            "❌ MAX_DEPTH debe estar entre 2 y 12.",
        )
    )
    r.append(
        verificar(
            0.01 <= learning_rate <= 0.5,
            f"✅ learning_rate={learning_rate} en rango válido.",
            "❌ LEARNING_RATE debe estar entre 0.01 y 0.5.",
        )
    )
    r.append(
        verificar(
            acc_test >= MIN_ACC_TEST,
            f"✅ Accuracy en test = {acc_test:.3f} (≥ {MIN_ACC_TEST:.2f}).",
            f"❌ Accuracy {acc_test:.3f} < {MIN_ACC_TEST:.2f}. Revisa hiperparámetros o limpieza.",
        )
    )
    return r


def verificar_importancia_global(top_features: list[str]) -> list[bool]:
    r = []
    r.append(
        verificar(
            len(top_features) >= 3,
            f"✅ Top-3 importancias identificadas: {top_features[:3]}.",
            "❌ Define TOP3_IMPORTANCIA con al menos 3 nombres de sensores.",
        )
    )
    r.append(
        verificar(
            TOP_FEATURE_REF in top_features[:3],
            f"✅ «{TOP_FEATURE_REF}» entre las 3 más importantes (coherente con daño estructural).",
            f"⚠️ Se esperaba «{TOP_FEATURE_REF}» en el top-3; revisa el modelo o datos.",
        )
    )
    return r


def verificar_shap_global(clase_shap: int) -> list[bool]:
    return [
        verificar(
            clase_shap in ETIQUETAS_VALIDAS,
            f"✅ Explicando SHAP para clase {clase_shap} (Condition Label).",
            "❌ CLASE_SHAP debe ser 0, 1 o 2.",
        )
    ]


def verificar_shap_local(
    index_caso: int,
    n_test: int,
    y_true: int,
    y_pred: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            0 <= index_caso < n_test,
            f"✅ INDEX_CASO={index_caso} válido en el conjunto de test (n={n_test}).",
            f"❌ INDEX_CASO debe estar entre 0 y {n_test - 1}.",
        )
    )
    r.append(
        verificar(
            y_true in ETIQUETAS_VALIDAS and y_pred in ETIQUETAS_VALIDAS,
            f"✅ Caso local: etiqueta real={y_true}, predicha={y_pred}.",
            "❌ Etiquetas del caso local fuera de rango 0–2.",
        )
    )
    return r


def _normalizar_feature_lime(nombre: str, features: list[str] | None = None) -> str:
    """LIME devuelve p. ej. 'Strain (με) <= -0.68' — extrae el nombre del sensor."""
    features = features or FEATURES_ESPERADAS
    for f in features:
        if nombre.strip().startswith(f):
            return f
    return nombre.split("<=")[0].split(">=")[0].strip()


def verificar_lime_local(
    index_caso: int,
    n_test: int,
    top_features: list[str],
) -> list[bool]:
    norm = [_normalizar_feature_lime(f) for f in top_features[:3]]
    r = []
    r.append(
        verificar(
            0 <= index_caso < n_test,
            f"✅ INDEX_CASO={index_caso} válido para LIME (n={n_test}).",
            f"❌ INDEX_CASO debe estar entre 0 y {n_test - 1}.",
        )
    )
    r.append(
        verificar(
            len(top_features) >= 3,
            f"✅ LIME top features: {top_features[:3]}.",
            "❌ Define TOP_LIME_FEATURES con al menos 3 entradas.",
        )
    )
    r.append(
        verificar(
            all(f in FEATURES_ESPERADAS for f in norm),
            f"✅ Sensores LIME reconocidos: {norm}.",
            f"❌ Normaliza nombres LIME a sensores de FEATURES. Obtuviste: {norm}",
        )
    )
    return r


def verificar_pdp(feature: str) -> list[bool]:
    return [
        verificar(
            feature in FEATURES_ESPERADAS,
            f"✅ Partial dependence calculado para «{feature}».",
            f"❌ FEATURE_PDP debe ser una de: {FEATURES_ESPERADAS}.",
        )
    ]
