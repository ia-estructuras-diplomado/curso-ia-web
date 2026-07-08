"""Autoevaluación amigable para Lab 3 Parte 2 — LSTM en sensores SHM."""

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
MIN_ACC_VAL = 0.65
MIN_ACC_VAL_ALUMNO = 0.55
MAX_EPOCHS_ALUMNO = 5
MIN_COMPONENTES_RNN = 4
MAX_MAE_INTERP = 0.85
MAX_MAE_EXTRAP = 1.2


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


def _norm(nombre: str) -> str:
    return nombre.strip().lower().replace(" ", "_")


def verificar_panorama_rnn(componentes: list[str]) -> list[bool]:
    if isinstance(componentes, str):
        componentes = [componentes]
    norm = [_norm(c) for c in componentes]

    def tiene(*palabras: str) -> bool:
        return any(any(p in t for p in palabras) for t in norm)

    r = []
    r.append(
        verificar(
            len(norm) >= MIN_COMPONENTES_RNN,
            f"✅ Panorama RNN con {len(norm)} componentes listados.",
            f"❌ Define COMPONENTES_RNN con al menos {MIN_COMPONENTES_RNN} entradas.",
        )
    )
    r.append(
        verificar(
            tiene("lstm", "rnn", "recurrent"),
            "✅ Incluye celda recurrente (LSTM/RNN).",
            "❌ Añade 'LSTM' o 'RNN' a COMPONENTES_RNN.",
        )
    )
    r.append(
        verificar(
            tiene("ventana", "window", "secuencia"),
            "✅ Incluye concepto de **ventana temporal**.",
            "❌ Añade 'ventana' o 'secuencia' a COMPONENTES_RNN.",
        )
    )
    return r


def verificar_carga(df, n_filas_head: int, features: list[str]) -> list[bool]:
    r = []
    r.append(
        verificar(
            df is not None and df.shape == (N_FILAS_RAW, 7),
            f"✅ Dataset cargado: {N_FILAS_RAW} lecturas × 7 columnas.",
            f"❌ Forma inesperada: {getattr(df, 'shape', None)}.",
        )
    )
    r.append(
        verificar(
            list(df.columns) == COLUMNAS_ESPERADAS,
            "✅ Columnas de sensores listas para SHM.",
            "❌ Revisa columnas del CSV.",
        )
    )
    r.append(
        verificar(
            features == FEATURES_ESPERADAS,
            "✅ 5 features de sensores definidas correctamente.",
            f"❌ FEATURES debe ser {FEATURES_ESPERADAS}.",
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


def verificar_orden_temporal(df) -> list[bool]:
    ts = df["Timestamp"]
    ordenado = ts.is_monotonic_increasing
    return [
        verificar(
            ordenado,
            "✅ Serie ordenada cronológicamente por Timestamp.",
            "❌ Ordena df por Timestamp antes de continuar.",
        )
    ]


def verificar_limpieza(df_limpio, n_antes: int, n_despues: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            n_antes == N_FILAS_RAW,
            f"✅ Partiste de {N_FILAS_RAW} registros crudos.",
            f"❌ Se esperaban {N_FILAS_RAW} filas antes de limpiar.",
        )
    )
    r.append(
        verificar(
            n_despues == N_FILAS_LIMPIO and df_limpio.shape[0] == N_FILAS_LIMPIO,
            f"✅ Tras eliminar nulos: {N_FILAS_LIMPIO} lecturas válidas.",
            f"❌ Tras limpieza se esperaban {N_FILAS_LIMPIO} filas; obtuviste {n_despues}.",
        )
    )
    return r


def verificar_columna(df, col: str) -> list[bool]:
    return [
        verificar(
            col in df.columns,
            f"✅ Columna «{col}» encontrada.",
            f"❌ «{col}» no existe. Usa un sensor válido.",
        )
    ]


def verificar_etiquetas(conteo: dict) -> list[bool]:
    return [
        verificar(
            set(conteo.keys()) == ETIQUETAS_VALIDAS,
            "✅ Tres clases: 0 (saludable), 1 (menor), 2 (severo).",
            f"❌ Etiquetas inesperadas: {sorted(conteo.keys())}.",
        )
    ]


def verificar_serie_temporal(sensor_eda: str, n_puntos_plot: int, df_limpio) -> list[bool]:
    r = []
    r.append(
        verificar(
            sensor_eda in FEATURES_ESPERADAS,
            f"✅ SENSOR_EDA = «{sensor_eda}» válido.",
            f"❌ SENSOR_EDA debe ser uno de {FEATURES_ESPERADAS}.",
        )
    )
    r.append(
        verificar(
            50 <= n_puntos_plot <= 500,
            f"✅ Graficando hasta {n_puntos_plot} puntos.",
            "❌ N_PUNTOS_PLOT debe estar entre 50 y 500.",
        )
    )
    r.append(
        verificar(
            len(df_limpio) >= n_puntos_plot,
            f"✅ Hay suficientes datos ({len(df_limpio)}) para el gráfico.",
            "❌ N_PUNTOS_PLOT supera el tamaño de df_limpio.",
        )
    )
    return r


def verificar_series_condicion(sensores_comparar: list[str]) -> list[bool]:
    r = []
    r.append(
        verificar(
            2 <= len(sensores_comparar) <= 3,
            f"✅ Comparando {len(sensores_comparar)} sensor(es) por condición.",
            "❌ SENSORES_COMPARAR debe tener 2 o 3 sensores.",
        )
    )
    r.append(
        verificar(
            all(s in FEATURES_ESPERADAS for s in sensores_comparar),
            f"✅ Sensores válidos: {sensores_comparar}.",
            "❌ Algún sensor no está en FEATURES.",
        )
    )
    return r


def verificar_ventanas(
    window_size: int,
    batch_size: int,
    train_loader,
    val_loader,
    n_train: int,
    n_val: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            10 <= window_size <= 120,
            f"✅ WINDOW_SIZE={window_size}.",
            "❌ WINDOW_SIZE debe estar entre 10 y 120.",
        )
    )
    r.append(
        verificar(
            8 <= batch_size <= 64,
            f"✅ BATCH_SIZE={batch_size}.",
            "❌ BATCH_SIZE debe estar entre 8 y 64.",
        )
    )
    try:
        xb, yb = next(iter(train_loader))
        r.append(
            verificar(
                xb.ndim == 3
                and xb.shape[1] == window_size
                and xb.shape[2] == N_FEATURES,
                f"✅ Batch train: {tuple(xb.shape)} (N×ventana×5).",
                f"❌ Forma inesperada: {tuple(xb.shape)}.",
            )
        )
        r.append(
            verificar(
                n_train > n_val,
                f"✅ Split temporal: train={n_train} ventanas, val={n_val} (train > val).",
                "❌ El split temporal debe dejar más ventanas en train que en val.",
            )
        )
        r.append(
            verificar(
                len(val_loader) >= 1,
                f"✅ val_loader listo ({len(val_loader)} batches).",
                "❌ val_loader vacío.",
            )
        )
    except Exception as exc:
        r.append(verificar(False, "", f"❌ Error al iterar train_loader: {exc}"))
    return r


def verificar_arquitectura_lstm(modelo, hidden_size: int, n_layers: int, dropout: float) -> list[bool]:
    import torch.nn as nn

    lstm_layers = [m for m in modelo.modules() if isinstance(m, nn.LSTM)]
    linear_layers = [m for m in modelo.modules() if isinstance(m, nn.Linear)]

    r = []
    r.append(
        verificar(
            16 <= hidden_size <= 128,
            f"✅ HIDDEN_SIZE={hidden_size}.",
            "❌ HIDDEN_SIZE debe estar entre 16 y 128.",
        )
    )
    r.append(
        verificar(
            1 <= n_layers <= 3,
            f"✅ N_LAYERS={n_layers}.",
            "❌ N_LAYERS debe estar entre 1 y 3.",
        )
    )
    r.append(
        verificar(
            0.0 <= dropout <= 0.5,
            f"✅ DROPOUT={dropout}.",
            "❌ DROPOUT debe estar entre 0.0 y 0.5.",
        )
    )
    r.append(
        verificar(
            len(lstm_layers) >= 1,
            "✅ Modelo con capa LSTM.",
            "❌ El modelo debe incluir nn.LSTM.",
        )
    )
    out_features = getattr(linear_layers[-1], "out_features", None) if linear_layers else None
    r.append(
        verificar(
            out_features == 3,
            "✅ Salida con 3 clases (Condition Label).",
            f"❌ La última Linear debe tener out_features=3; obtuviste {out_features}.",
        )
    )
    return r


def verificar_entrenamiento_lstm(
    history: dict,
    n_epochs: int,
    learning_rate: float,
    acc_val: float,
) -> list[bool]:
    keys = {"train_loss", "val_loss", "train_acc", "val_acc"}
    r = []
    r.append(
        verificar(
            keys.issubset(history.keys()),
            "✅ history con train/val loss y accuracy.",
            f"❌ history debe incluir {sorted(keys)}.",
        )
    )
    r.append(
        verificar(
            1 <= n_epochs <= MAX_EPOCHS_ALUMNO,
            f"✅ N_EPOCHS={n_epochs} (entrenamiento corto en CPU).",
            f"❌ N_EPOCHS debe estar entre 1 y {MAX_EPOCHS_ALUMNO} para el modelo alumno.",
        )
    )
    r.append(
        verificar(
            1e-4 <= learning_rate <= 0.1,
            f"✅ LEARNING_RATE={learning_rate}.",
            "❌ LEARNING_RATE debe estar entre 1e-4 y 0.1.",
        )
    )
    if keys.issubset(history.keys()) and len(history["train_loss"]) >= 2:
        loss_baja = history["train_loss"][-1] <= history["train_loss"][0]
        r.append(
            verificar(
                loss_baja,
                "✅ Pérdida de entrenamiento no aumentó respecto a la 1.ª época.",
                "❌ La loss de train subió — revisa LR o arquitectura.",
            )
        )
    min_acc = MIN_ACC_VAL_ALUMNO
    r.append(
        verificar(
            acc_val >= min_acc,
            f"✅ Accuracy en validación = {acc_val:.3f} (≥ {min_acc:.2f}, modelo corto).",
            f"❌ Accuracy val {acc_val:.3f} < {min_acc:.2f}.",
        )
    )
    return r


def verificar_modelo_docente_lstm(acc_docente: float, min_acc: float = 0.60) -> list[bool]:
    return [
        verificar(
            acc_docente >= min_acc,
            f"✅ Checkpoint LSTM docente cargado (acc ref = {acc_docente:.3f}).",
            "❌ Falta lstm_classifier_best.pt — docente: python labs/lab3/_generar_modelos.py",
        )
    ]


def verificar_comparacion_docente_lstm(
    acc_alumno: float,
    acc_docente: float,
    n_epochs_alumno: int,
    n_epochs_docente: int,
) -> list[bool]:
    r = [
        verificar(
            1 <= n_epochs_alumno <= MAX_EPOCHS_ALUMNO,
            f"✅ Comparaste tu LSTM ({n_epochs_alumno} ép.) con el docente ({n_epochs_docente} ép.).",
            f"❌ N_EPOCHS alumno debe estar entre 1 y {MAX_EPOCHS_ALUMNO}.",
        ),
        verificar(
            acc_docente >= acc_alumno,
            f"✅ Modelo docente ({acc_docente:.3f}) ≥ tu modelo ({acc_alumno:.3f}).",
            f"❌ Se esperaba acc_docente ≥ acc_alumno ({acc_docente:.3f} vs {acc_alumno:.3f}).",
        ),
    ]
    return r


def verificar_interpolacion(
    mae_interp: float,
    gap_inicio: int,
    gap_fin: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            0 <= gap_inicio < gap_fin,
            f"✅ Hueco de interpolación [{gap_inicio}, {gap_fin}).",
            "❌ GAP_INICIO debe ser menor que GAP_FIN.",
        )
    )
    r.append(
        verificar(
            0.0 <= mae_interp <= MAX_MAE_INTERP,
            f"✅ MAE interpolación = {mae_interp:.4f} (escala normalizada).",
            f"❌ MAE interpolación {mae_interp:.4f} > {MAX_MAE_INTERP}. Revisa GAP o modelo_reg.",
        )
    )
    return r


def verificar_extrapolacion(
    mae_extrap: float,
    horizonte_extrap: int,
    mae_interp: float | None = None,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            3 <= horizonte_extrap <= 30,
            f"✅ HORIZONTE_EXTRAP={horizonte_extrap} pasos.",
            "❌ HORIZONTE_EXTRAP debe estar entre 3 y 30.",
        )
    )
    r.append(
        verificar(
            0.0 <= mae_extrap <= MAX_MAE_EXTRAP,
            f"✅ MAE extrapolación = {mae_extrap:.4f} (escala normalizada).",
            f"❌ MAE extrapolación {mae_extrap:.4f} > {MAX_MAE_EXTRAP}.",
        )
    )
    if mae_interp is not None:
        r.append(
            verificar(
                mae_extrap >= mae_interp * 0.8,
                "✅ Extrapolación ≥ interpolación (típico: predecir futuro es más difícil).",
                "⚠️ Extrapolación mucho mejor que interpolación — revisa el tramo elegido.",
            )
        )
    return r
