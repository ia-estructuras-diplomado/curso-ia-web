"""Autoevaluación amigable para Lab 2 — Resistencia a la compresión."""

from __future__ import annotations

COLUMNAS_ESPERADAS = [
    "Cemento",
    "Escoria",
    "CenizaVolante",
    "Agua",
    "Superplastificante",
    "AgregadoGrueso",
    "AgregadoFino",
    "Edad",
    "Resistencia",
]

# Top-3 |correlación| con Resistencia en el dataset UCI (referencia docente)
TOP3_CORR_ESPERADAS = {"Cemento", "Superplastificante", "Edad"}


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


def verificar_tipo_problema(tipo: str) -> list[bool]:
    tipo_norm = tipo.strip().lower()
    return [
        verificar(
            tipo_norm in ("regresion", "regresión"),
            "✅ Correcto: predecir MPa es un problema de **regresión** supervisada.",
            "❌ La resistencia es un valor continuo (MPa). Asigna TIPO_PROBLEMA = 'regresion'.",
        )
    ]


def verificar_carga(df, n_filas_head: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            df is not None and df.shape == (1030, 9),
            "✅ Dataset cargado: 1 030 mezclas × 9 columnas.",
            f"❌ Forma inesperada: {getattr(df, 'shape', None)}. Ejecuta la celda de carga.",
        )
    )
    r.append(
        verificar(
            list(df.columns) == COLUMNAS_ESPERADAS,
            "✅ Columnas en español técnico listas para ML.",
            "❌ Revisa que uses data/concrete.csv generado desde el XLS UCI.",
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


def verificar_columna(df, col: str) -> list[bool]:
    r = []
    r.append(
        verificar(
            col in df.columns,
            f"✅ Columna «{col}» encontrada en el dataset.",
            f"❌ «{col}» no existe. Usa una de: {', '.join(COLUMNAS_ESPERADAS)}.",
        )
    )
    if col in df.columns:
        n_nulos = int(df[col].isna().sum())
        r.append(
            verificar(
                n_nulos == 0,
                f"✅ Sin valores nulos en «{col}» ({len(df)} registros).",
                f"❌ Hay {n_nulos} nulos en «{col}».",
            )
        )
    return r


def verificar_resumen(resumen, columnas: list[str]) -> list[bool]:
    cols = list(columnas)
    return [
        verificar(
            hasattr(resumen, "columns") and set(cols).issubset(set(resumen.columns)),
            f"✅ Resumen estadístico con {len(cols)} columna(s) elegida(s).",
            "❌ COLUMNAS_RESUMEN debe incluir columnas válidas del dataset.",
        )
    ]


def verificar_umbral_resistencia(
    df,
    umbral: float,
    n_fuertes: int,
    n_debiles: int,
) -> list[bool]:
    esperado_fuertes = int((df["Resistencia"] >= umbral).sum())
    esperado_debiles = int((df["Resistencia"] < umbral).sum())
    r = []
    r.append(
        verificar(
            n_fuertes == esperado_fuertes and n_debiles == esperado_debiles,
            f"✅ Con umbral {umbral} MPa: {n_fuertes} fuertes / {n_debiles} por debajo.",
            f"❌ Conteos incorrectos. Esperado ≥{umbral}: {esperado_fuertes}, <{umbral}: {esperado_debiles}.",
        )
    )
    if umbral == 40:
        r.append(
            verificar(
                n_fuertes == 379 and n_debiles == 651,
                "✅ Umbral 40 MPa coherente con el dataset UCI.",
                "⚠️ Revisa UMBRAL_RESISTENCIA = 40 para la autoevaluación detallada.",
            )
        )
    return r


def verificar_correlaciones(top_corr: list[str], top_n: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            len(top_corr) == top_n,
            f"✅ Top {top_n} correlaciones con Resistencia calculadas.",
            f"❌ Debes obtener {top_n} variables; obtuviste {len(top_corr)}.",
        )
    )
    if top_n == 3:
        r.append(
            verificar(
                set(top_corr) == TOP3_CORR_ESPERADAS,
                f"✅ Top 3 esperado: {', '.join(sorted(top_corr))}.",
                f"❌ Top 3 esperado: Cemento, Superplastificante, Edad. Obtuviste: {top_corr}.",
            )
        )
    return r


def verificar_scatter_filtro(n_filtradas: int, edad_min: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_filtradas > 0,
            f"✅ Subconjunto con Edad ≥ {edad_min} días: {n_filtradas} muestras.",
            f"❌ Filtro Edad ≥ {edad_min} dejó 0 filas. Baja EDAD_MIN_DIAS.",
        )
    )
    if edad_min == 28:
        r.append(
            verificar(
                n_filtradas == 706,
                "✅ Filtro a 28 días (referencia obra) con 706 probetas.",
                f"⚠️ Con EDAD_MIN_DIAS=28 esperábamos 706 filas; hay {n_filtradas}.",
            )
        )
    return r


def verificar_split(n_train: int, n_test: int, test_size: float, random_state: int) -> list[bool]:
    total = n_train + n_test
    r = []
    r.append(
        verificar(
            total == 1030,
            f"✅ Partición cubre las 1 030 muestras ({n_train} train + {n_test} test).",
            f"❌ Train+test = {total}, debería ser 1030.",
        )
    )
    if test_size == 0.2 and random_state == 42:
        r.append(
            verificar(
                n_train == 824 and n_test == 206,
                "✅ Split 80/20 con random_state=42 (824 / 206).",
                f"❌ Con TEST_SIZE=0.2 y RANDOM_STATE=42 esperábamos 824/206; obtuviste {n_train}/{n_test}.",
            )
        )
    return r


def verificar_modelo(
    r2_test: float,
    min_r2: float,
    importancias: dict[str, float],
    col_top_esperada: str = "Edad",
) -> list[bool]:
    r = []
    r.append(
        verificar(
            r2_test >= min_r2,
            f"✅ R² en test = {r2_test:.3f} (≥ {min_r2}).",
            f"❌ R² = {r2_test:.3f} por debajo de {min_r2}. Sube N_ESTIMATORS o incluye Edad en COLUMNAS_X.",
        )
    )
    if importancias:
        top = max(importancias, key=importancias.get)
        r.append(
            verificar(
                top == col_top_esperada,
                f"✅ Variable más importante: «{top}».",
                f"❌ Se esperaba «{col_top_esperada}» como top; obtuviste «{top}». ¿Quitaste Edad de COLUMNAS_X?",
            )
        )
    return r


def verificar_importancias(
    importancias_ordenadas: list[str],
    n_top: int,
    col_top_esperada: str = "Edad",
) -> list[bool]:
    r = []
    r.append(
        verificar(
            len(importancias_ordenadas) == n_top,
            f"✅ Mostrando top {n_top} importancias.",
            f"❌ Ajusta N_TOP_IMPORTANCIAS; obtuviste {len(importancias_ordenadas)}.",
        )
    )
    if importancias_ordenadas:
        r.append(
            verificar(
                importancias_ordenadas[0] == col_top_esperada,
                f"✅ Mayor impacto: «{importancias_ordenadas[0]}» (coherente con curado y dosificación).",
                f"❌ La importancia #1 debería ser «{col_top_esperada}»; obtuviste «{importancias_ordenadas[0]}».",
            )
        )
    return r
