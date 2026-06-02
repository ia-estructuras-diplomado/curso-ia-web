"""Autoevaluación amigable para Lab 1 — PCA, clustering y monitoreo estructural."""

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

# Varianza acumulada de referencia (StandardScaler + PCA completo, 904 filas)
VAR_ACUM_REF = [0.272544, 0.472370, 0.669148, 0.862676, 1.0]
PC1_TOP_FEATURE = "Strain (με)"


def verificar(condicion: bool, ok: str, fail: str) -> bool:
    print(ok if condicion else fail)
    return condicion


def resumen_seccion(nombre: str, resultados: list[bool]) -> None:
    if all(resultados):
        print(f"\n✅ Sección {nombre} completada. Puedes continuar.")
    else:
        print(
            f"\n❌ Sección {nombre}: revisa las celdas marcadas con "
            "### TU TAREA AQUÍ ### y vuelve a ejecutar."
        )


def verificar_contexto_pca(metodo: str) -> list[bool]:
    m = metodo.strip().lower()
    return [
        verificar(
            m in ("pca", "acp", "componentes principales"),
            "✅ Correcto: PCA (Análisis de Componentes Principales) reduce dimensionalidad.",
            "❌ Asigna METODO_REDUCCION = 'pca' para este laboratorio.",
        )
    ]


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
    r = []
    r.append(
        verificar(
            col in df.columns,
            f"✅ Columna «{col}» encontrada.",
            f"❌ «{col}» no existe. Usa una feature de sensor o Condition Label.",
        )
    )
    if col in FEATURES_ESPERADAS:
        n_nulos = int(df[col].isna().sum())
        r.append(
            verificar(
                n_nulos > 0,
                f"✅ «{col}» tiene {n_nulos} nulos en datos crudos (esperado en ~20 filas).",
                f"⚠️ «{col}» no tiene nulos en crudo; el dataset pudo cambiar.",
            )
        )
    return r


def verificar_resumen(resumen, columnas: list[str]) -> list[bool]:
    cols = list(columnas)
    return [
        verificar(
            hasattr(resumen, "columns") and set(cols).issubset(set(resumen.columns)),
            f"✅ Resumen estadístico con {len(cols)} columna(s) de sensores.",
            "❌ COLUMNAS_RESUMEN debe incluir columnas válidas del dataset.",
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
                "✅ Clase 0 (normal) es mayoritaria — típico en SHM (más tiempo en servicio normal).",
                "",
            )
        )
    return r


def verificar_correlacion(max_corr: float, top_par: tuple[str, str] | None) -> list[bool]:
    r = []
    r.append(
        verificar(
            0 <= max_corr <= 1,
            f"✅ Correlación máxima entre sensores (|r|) = {max_corr:.3f}.",
            "❌ Revisa el cálculo de correlación entre features.",
        )
    )
    if top_par:
        r.append(
            verificar(
                True,
                f"✅ Par más correlacionado: {top_par[0]} ↔ {top_par[1]}.",
                "",
            )
        )
    return r


def verificar_escalado(usar_escalado: bool, var_pc1_escalado: float, var_pc1_crudo: float) -> list[bool]:
    r = []
    r.append(
        verificar(
            usar_escalado,
            "✅ Estandarización activada (recomendado antes de PCA).",
            "⚠️ Sin escalado, sensores con mayor magnitud dominan PC1 (ej. Accel_Z ~ 9.8 m/s²).",
        )
    )
    if usar_escalado:
        r.append(
            verificar(
                abs(var_pc1_escalado - VAR_ACUM_REF[0]) < 0.02,
                f"✅ PC1 explica ~{var_pc1_escalado*100:.1f}% de varianza (coherente con referencia).",
                f"❌ Varianza PC1 = {var_pc1_escalado:.3f}; esperada ~{VAR_ACUM_REF[0]:.3f}. ¿Ejecutaste la limpieza?",
            )
        )
    else:
        r.append(
            verificar(
                var_pc1_crudo > var_pc1_escalado,
                "⚠️ Sin escalado, PC1 captura sobre todo la magnitud de Accel_Z (gravedad). Activa ESCALAR=True.",
                "❌ Compara varianza PC1 con y sin escalado.",
            )
        )
    return r


def verificar_varianza(
    var_acum: list[float],
    umbral: float,
    n_componentes: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            len(var_acum) == N_FEATURES,
            f"✅ Varianza acumulada calculada para {N_FEATURES} componentes.",
            f"❌ Se esperaban {N_FEATURES} ratios; obtuviste {len(var_acum)}.",
        )
    )
    n_min = int(__import__("numpy").searchsorted(var_acum, umbral) + 1)
    r.append(
        verificar(
            n_componentes == n_min,
            f"✅ Con umbral {umbral:.0%} se necesitan {n_componentes} componente(s).",
            f"❌ Para {umbral:.0%} de varianza usa N_COMPONENTES = {n_min}.",
        )
    )
    if umbral == 0.90:
        r.append(
            verificar(
                n_componentes == 5,
                "✅ Umbral 90% → 5 componentes (todas las features originales).",
                f"⚠️ Con UMBRAL_VARIANZA=0.90 se esperaban 5 componentes; tienes {n_componentes}.",
            )
        )
    return r


def verificar_proyeccion_2d(
    n_muestras: int,
    colorear_por: str,
    var_pc1: float,
    var_pc2: float,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_muestras == N_FILAS_LIMPIO,
            f"✅ Proyección 2D con {n_muestras} puntos.",
            f"❌ Se esperaban {N_FILAS_LIMPIO} puntos; hay {n_muestras}.",
        )
    )
    r.append(
        verificar(
            colorear_por.strip() == "Condition Label",
            "✅ Puntos coloreados por estado estructural (Condition Label).",
            "❌ Usa COLOREAR_POR = 'Condition Label' para interpretar el SHM.",
        )
    )
    r.append(
        verificar(
            var_pc1 + var_pc2 >= 0.40,
            f"✅ PC1+PC2 explican {100*(var_pc1+var_pc2):.1f}% de varianza (vista 2D útil).",
            "❌ Varianza 2D muy baja; revisa escalado y limpieza.",
        )
    )
    return r


def verificar_loadings(feature_pc1: str) -> list[bool]:
    return [
        verificar(
            feature_pc1 == PC1_TOP_FEATURE,
            f"✅ PC1 está dominado por «{feature_pc1}» (deformación — coherente con daño estructural).",
            f"❌ Se esperaba «{PC1_TOP_FEATURE}» como mayor peso en PC1; obtuviste «{feature_pc1}».",
        )
    ]


def verificar_clasificacion_pca(
    acc_orig: float,
    acc_pca: int,
    n_componentes_ml: int,
    min_acc_orig: float = 0.70,
    min_acc_pca: float = 0.65,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            1 <= n_componentes_ml <= N_FEATURES,
            f"✅ Clasificador entrenado con {n_componentes_ml} componente(s) PCA.",
            f"❌ N_COMPONENTES_ML debe estar entre 1 y {N_FEATURES}.",
        )
    )
    r.append(
        verificar(
            acc_orig >= min_acc_orig,
            f"✅ Accuracy con features originales = {acc_orig:.3f}.",
            f"❌ Accuracy original {acc_orig:.3f} < {min_acc_orig}. Revisa split y limpieza.",
        )
    )
    r.append(
        verificar(
            acc_pca >= min_acc_pca,
            f"✅ Accuracy con PCA ({n_componentes_ml} comp.) = {acc_pca:.3f}.",
            f"❌ Accuracy PCA {acc_pca:.3f} < {min_acc_pca}. Prueba más componentes.",
        )
    )
    if n_componentes_ml == 3 and acc_orig > 0:
        diff = acc_orig - acc_pca
        if diff <= 0.05:
            r.append(
                verificar(
                    True,
                    f"✅ PCA-3 pierde poco rendimiento (Δacc ≈ {diff:.3f}) — buena compresión.",
                    "",
                )
            )
        else:
            r.append(
                verificar(
                    True,
                    f"⚠️ PCA-3 reduce accuracy en {diff:.3f}; prueba N_COMPONENTES_ML = 4.",
                    "",
                )
            )
    return r


def verificar_kmeans(k_opt: int, k_min: int, k_max: int, sil: float) -> list[bool]:
    r = []
    r.append(
        verificar(
            k_min <= k_opt <= k_max,
            f"✅ K_OPT={k_opt} dentro del rango del codo ({k_min}–{k_max}).",
            f"❌ K_OPT debe estar entre {k_min} y {k_max}.",
        )
    )
    r.append(
        verificar(
            k_opt == 3,
            "✅ k=3 coherente con tres estados de condición estructural (0/1/2).",
            f"⚠️ Con el codo, k=3 suele ser adecuado; probaste k={k_opt}.",
        )
    )
    r.append(
        verificar(
            sil > 0.05,
            f"✅ Silhouette KMeans = {sil:.3f} (separación positiva en datos reales).",
            f"❌ Silhouette muy bajo ({sil:.3f}). Revisa escalado y K_OPT.",
        )
    )
    return r


def verificar_dbscan(
    eps: float,
    min_samples: int,
    n_clusters: int,
    n_noise: int,
    sil: float,
) -> list[bool]:
    import math

    r = []
    r.append(
        verificar(
            0.3 <= eps <= 1.5,
            f"✅ eps={eps} en rango razonable para datos escalados.",
            "❌ eps fuera de rango típico (0.3–1.5); revisa la escala de X_pca_input.",
        )
    )
    r.append(
        verificar(
            3 <= min_samples <= 20,
            f"✅ min_samples={min_samples} configurado.",
            "❌ min_samples debe estar entre 3 y 20 para este dataset.",
        )
    )
    r.append(
        verificar(
            n_clusters >= 2,
            f"✅ DBSCAN encontró {n_clusters} clúster(es) densos.",
            "❌ Menos de 2 clústeres: aumenta eps o reduce min_samples.",
        )
    )
    if eps == 0.7 and min_samples == 8:
        r.append(
            verificar(
                n_noise >= 100,
                f"✅ {n_noise} puntos marcados como ruido (-1) — lecturas atípicas detectadas.",
                f"⚠️ Con eps=0.7 y min_samples=8 se esperaban ≥100 ruidos; obtuviste {n_noise}.",
            )
        )
    if n_clusters >= 2 and not math.isnan(sil):
        r.append(
            verificar(
                sil > 0.05,
                f"✅ Silhouette DBSCAN (sin ruido) = {sil:.3f}.",
                f"⚠️ Silhouette DBSCAN bajo ({sil:.3f}); ajusta eps/min_samples.",
            )
        )
    return r


def verificar_comparativa_clustering(
    sil_km: float,
    sil_db: float,
    ari_km: float,
    ari_db: float,
    metrica_prioritaria: str,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            sil_km >= sil_db or abs(sil_km - sil_db) < 0.05,
            f"✅ Silhouette KMeans ({sil_km:.3f}) ≥ DBSCAN ({sil_db:.3f}) o muy cercanos.",
            f"⚠️ DBSCAN supera a KMeans en Silhouette; revisa parámetros de DBSCAN.",
        )
    )
    r.append(
        verificar(
            ari_km >= 0.08,
            f"✅ ARI KMeans = {ari_km:.3f} — alineación moderada con Condition Label.",
            f"❌ ARI KMeans bajo ({ari_km:.3f}). Usa K_OPT=3 y datos limpios.",
        )
    )
    mp = metrica_prioritaria.strip().lower()
    r.append(
        verificar(
            mp in ("ari", "silhouette", "sil"),
            "✅ Métrica de comparación registrada (ARI o Silhouette).",
            "❌ METRICA_PRIORITARIA debe ser 'ari' o 'silhouette'.",
        )
    )
    if mp == "ari":
        r.append(
            verificar(
                ari_km >= ari_db,
                f"✅ KMeans alinea mejor con la etiqueta de daño (ARI {ari_km:.3f} vs {ari_db:.3f}).",
                "⚠️ DBSCAN supera a KMeans en ARI; documenta por qué en tu reflexión.",
            )
        )
    return r
