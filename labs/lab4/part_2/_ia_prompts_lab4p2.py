"""Prompts IA y celdas vacías para Lab 4 Parte 2 — importar desde _generar_notebooks.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from _ia_helpers import celda_solucion_alumno, ia_guia_seccion  # noqa: E402

IA_Q1 = ia_guia_seccion(
    "1",
    "Panorama RNN/LSTM",
    "Listar componentes clave de una RNN/LSTM aplicada a sensores SHM.",
    [
        "Definir `COMPONENTES_RNN` con al menos 4 entradas",
        "Incluir LSTM, ventana temporal, hidden size, dropout",
        "Imprimir la lista",
    ],
    vars_autoeval=["COMPONENTES_RNN"],
    consideraciones=[
        "Contexto: clasificación de Condition Label desde secuencias de sensores",
        "Diferencia con Lab 3 (XGBoost tabular): aquí importa el ORDEN temporal",
    ],
    prompt="""Lab 4 Parte 2 — LSTM en sensores SHM.
Genera código que:
1) COMPONENTES_RNN = ["ventana temporal", "LSTM", "hidden size", "dropout", "fully connected"]
2) imprima cada componente con print(f"  · {c}")
No uses imports nuevos.""",
)

CELDA_Q1 = celda_solucion_alumno(
    variables=["COMPONENTES_RNN"],
    pasos=["Lista con LSTM, ventana, hidden, dropout…", "Imprimir cada componente"],
)

IA_Q2 = ia_guia_seccion(
    "2",
    "Carga y orden temporal",
    "Definir FEATURES y mostrar primeras filas del CSV ordenado.",
    [
        "Lista `FEATURES` con los 5 nombres exactos de sensores",
        "`N_FILAS_HEAD` entre 1 y 20",
        "Mostrar `df.head(N_FILAS_HEAD)` — la celda anterior ya ordenó por Timestamp",
    ],
    vars_autoeval=["FEATURES", "N_FILAS_HEAD"],
    consideraciones=[
        "No incluir Timestamp ni Condition Label en FEATURES",
        "Nombres exactos del CSV SHM (con unidades entre paréntesis)",
    ],
    prompt="""En Jupyter ya tengo `df` cargado y ordenado por Timestamp (1000 filas).
Genera código que:
1) FEATURES = ["Accel_X (m/s^2)", "Accel_Y (m/s^2)", "Accel_Z (m/s^2)", "Strain (με)", "Temp (°C)"]
2) N_FILAS_HEAD = 5
3) imprima FEATURES y display(df.head(N_FILAS_HEAD))""",
)

CELDA_Q2 = celda_solucion_alumno(
    variables=["FEATURES", "N_FILAS_HEAD"],
    pasos=["FEATURES (5 sensores)", "N_FILAS_HEAD y df.head()"],
)

IA_Q3 = ia_guia_seccion(
    "3",
    "Calidad y balance",
    "Revisar un sensor y confirmar limpieza.",
    [
        "Definir `COLUMNA_REVISAR` (sensor válido)",
        "Calcular `describe()` en datos crudos `df`",
        "Mostrar resultado",
    ],
    vars_autoeval=["COLUMNA_REVISAR"],
    consideraciones=[
        "La celda anterior creó `df_limpio`, `n_antes`, `n_despues`, `conteo`",
        "Strain (με) es el más relevante para daño estructural",
    ],
    prompt="""Tengo df (crudo) y df_limpio (sin nulos en FEATURES).
Genera código que:
1) COLUMNA_REVISAR = "Strain (με)"
2) stats_col = df[COLUMNA_REVISAR].describe()
3) display(stats_col)""",
)

CELDA_Q3 = celda_solucion_alumno(
    variables=["COLUMNA_REVISAR", "stats_col"],
    pasos=["Elegir COLUMNA_REVISAR", "describe() en df crudo"],
)

IA_Q4 = ia_guia_seccion(
    "4",
    "Serie temporal global",
    "Graficar un sensor vs tiempo (EDA antes de entrenar).",
    [
        "Definir `SENSOR_EDA` y `N_PUNTOS_PLOT` (50–500)",
        "Plot línea de df_limpio[SENSOR_EDA] vs índice temporal",
        "Título y etiquetas de ejes",
    ],
    vars_autoeval=["SENSOR_EDA", "N_PUNTOS_PLOT"],
    consideraciones=[
        "Usa df_limpio ya definido",
        "Puedes usar df_limpio.index o range(len) en el eje x",
    ],
    prompt="""Tengo df_limpio con columna SENSOR_EDA.
Genera matplotlib que:
1) SENSOR_EDA = "Strain (με)"; N_PUNTOS_PLOT = 300
2) tome df_limpio[SENSOR_EDA].iloc[:N_PUNTOS_PLOT]
3) plot línea con título "Serie temporal — Strain" y plt.show()""",
)

CELDA_Q4 = celda_solucion_alumno(
    variables=["SENSOR_EDA", "N_PUNTOS_PLOT"],
    pasos=["SENSOR_EDA y N_PUNTOS_PLOT", "Gráfico línea vs tiempo"],
)

IA_Q5 = ia_guia_seccion(
    "5",
    "Series por condición",
    "Comparar sensores según Condition Label (0/1/2).",
    [
        "Definir `SENSORES_COMPARAR` (lista de 2–3 sensores)",
        "Subplots: para cada sensor, plot por clase con leyenda",
    ],
    vars_autoeval=["SENSORES_COMPARAR"],
    consideraciones=[
        "Filtra df_limpio por Condition Label 0, 1, 2",
        "Muestra ~100 puntos por clase para legibilidad",
    ],
    prompt="""Tengo df_limpio con FEATURES y Condition Label.
Genera código que:
1) SENSORES_COMPARAR = ["Strain (με)", "Temp (°C)"]
2) fig, axes = subplots(1, len(SENSORES_COMPARAR), figsize=(10,4))
3) para cada sensor y clase 0,1,2: plot de los primeros 100 puntos de esa clase
4) leyenda, títulos, plt.show()""",
)

CELDA_Q5 = celda_solucion_alumno(
    variables=["SENSORES_COMPARAR"],
    pasos=["2–3 sensores", "Subplots coloreados por Condition Label"],
)

IA_Q6 = ia_guia_seccion(
    "6",
    "Ventanas y split temporal",
    "Crear DataLoaders con ventanas deslizantes (sin fuga de futuro).",
    [
        "Definir `WINDOW_SIZE` (10–120) y `BATCH_SIZE` (8–64)",
        "Usar `train_loader` y `val_loader` de la celda pre-escrita (make_sequence_loaders)",
    ],
    vars_autoeval=["WINDOW_SIZE", "BATCH_SIZE", "train_loader", "val_loader"],
    consideraciones=[
        "La celda anterior define make_sequence_loaders y ya creó los loaders",
        "Tu tarea: redefinir WINDOW_SIZE/BATCH_SIZE y recrear loaders si cambias valores",
    ],
    prompt="""Tengo make_sequence_loaders(df_limpio, FEATURES, window_size, batch_size).
Genera código que:
1) WINDOW_SIZE = 30; BATCH_SIZE = 32
2) train_loader, val_loader, n_train, n_val = make_sequence_loaders(df_limpio, FEATURES, WINDOW_SIZE, BATCH_SIZE)
3) imprima n_train, n_val y shape del primer batch""",
)

CELDA_Q6 = celda_solucion_alumno(
    variables=["WINDOW_SIZE", "BATCH_SIZE", "train_loader", "val_loader"],
    pasos=["WINDOW_SIZE, BATCH_SIZE", "Recrear loaders y mostrar shapes"],
)

IA_Q7 = ia_guia_seccion(
    "7",
    "Arquitectura LSTM",
    "Construir clasificador LSTM multiclass.",
    [
        "Definir `HIDDEN_SIZE`, `N_LAYERS`, `DROPOUT`",
        "Crear `modelo` (nn.LSTM + Linear) con salida 3 clases",
        "Mover a `device`",
    ],
    vars_autoeval=["modelo", "HIDDEN_SIZE", "N_LAYERS", "DROPOUT"],
    consideraciones=[
        "Entrada: (batch, WINDOW_SIZE, 5)",
        "Usar último hidden state de LSTM para clasificar",
    ],
    prompt="""Lab 4 LSTM. Tengo WINDOW_SIZE, device, 5 features, 3 clases.
Genera class LSTMClassifier(nn.Module):
- LSTM(5, HIDDEN_SIZE, N_LAYERS, batch_first=True, dropout=DROPOUT si N_LAYERS>1)
- Linear(HIDDEN_SIZE, 3)
HIDDEN_SIZE=64, N_LAYERS=1, DROPOUT=0.2
modelo = LSTMClassifier().to(device); print(modelo)""",
)

CELDA_Q7 = celda_solucion_alumno(
    variables=["modelo", "HIDDEN_SIZE", "N_LAYERS", "DROPOUT"],
    pasos=["Hiperparámetros LSTM", "modelo.to(device)"],
)

IA_Q8 = ia_guia_seccion(
    "8",
    "Entrenamiento clasificación",
    "Entrenar LSTM y registrar history + acc_val.",
    [
        "Definir `N_EPOCHS`, `LEARNING_RATE`",
        "Bucle con train_one_epoch / eval_epoch (pre-escritos)",
        "Calcular `acc_val` al final",
    ],
    vars_autoeval=["history", "N_EPOCHS", "LEARNING_RATE", "acc_val"],
    consideraciones=[
        "CrossEntropyLoss + Adam",
        "history con train_loss, val_loss, train_acc, val_acc",
    ],
    prompt="""Tengo modelo, train_loader, val_loader, train_one_epoch, eval_epoch, device.
Genera:
N_EPOCHS=5, LEARNING_RATE=1e-3
criterion, optimizer, history dict, loop de épocas
Al final: acc_val = última val_acc de history; print acc_val""",
)

CELDA_Q8 = celda_solucion_alumno(
    variables=["history", "N_EPOCHS", "LEARNING_RATE", "acc_val"],
    pasos=["Entrenar LSTM", "history y acc_val"],
)

IA_Q9 = ia_guia_seccion(
    "9",
    "Test interpolación (Strain)",
    "Predecir un hueco interior en la serie de Strain normalizada.",
    [
        "Definir `GAP_INICIO` y `GAP_FIN` dentro del segmento",
        "Llamar `evaluar_interpolacion(modelo_reg, strain_norm, GAP_INICIO, GAP_FIN)`",
        "Guardar `mae_interp` y mostrar gráfico real vs predicho en el hueco",
    ],
    vars_autoeval=["mae_interp", "GAP_INICIO", "GAP_FIN"],
    consideraciones=[
        "modelo_reg y strain_norm vienen de la celda pre-escrita",
        "MAE en escala normalizada (0–1 aprox.)",
    ],
    prompt="""Tengo modelo_reg, strain_norm, evaluar_interpolacion() pre-escritos.
Genera:
GAP_INICIO=40; GAP_FIN=60
mae_interp, y_real, y_pred = evaluar_interpolacion(modelo_reg, strain_norm, GAP_INICIO, GAP_FIN)
plot hueco: real vs predicho; print(f"MAE interp: {mae_interp:.4f}")""",
)

CELDA_Q9 = celda_solucion_alumno(
    variables=["mae_interp", "GAP_INICIO", "GAP_FIN"],
    pasos=["GAP_INICIO/GAP_FIN", "evaluar_interpolacion + gráfico"],
)

IA_Q10 = ia_guia_seccion(
    "10",
    "Test extrapolación (Strain)",
    "Predecir pasos futuros a partir del histórico.",
    [
        "Definir `HORIZONTE_EXTRAP` (3–30)",
        "Llamar `evaluar_extrapolacion(modelo_reg, strain_norm, W, HORIZONTE_EXTRAP)`",
        "Guardar `mae_extrap` y graficar histórico + forecast",
    ],
    vars_autoeval=["mae_extrap", "HORIZONTE_EXTRAP"],
    consideraciones=[
        "W (ventana histórica) está definido en celda pre-escrita como W_EXTRAP=80",
        "Comparar visualmente con interpolación (sección 9)",
    ],
    prompt="""Tengo modelo_reg, strain_norm, evaluar_extrapolacion(), W_EXTRAP=80.
Genera:
HORIZONTE_EXTRAP = 15
mae_extrap, hist, real_fut, pred_fut = evaluar_extrapolacion(modelo_reg, strain_norm, W_EXTRAP, HORIZONTE_EXTRAP)
plot histórico + real vs predicho; print(f"MAE extrap: {mae_extrap:.4f}")""",
)

CELDA_Q10 = celda_solucion_alumno(
    variables=["mae_extrap", "HORIZONTE_EXTRAP"],
    pasos=["HORIZONTE_EXTRAP", "evaluar_extrapolacion + gráfico"],
)

IA_Q11 = ia_guia_seccion(
    "11",
    "Reflexión ingeniería",
    "Cuándo usar LSTM vs XGBoost y límites de extrapolación.",
    [
        "2–3 bullets en markdown (opcional)",
    ],
    vars_autoeval=[],
    consideraciones=["No requiere código Python"],
    prompt="""3 bullets en español para ingeniero civil:
- Cuándo LSTM aporta vs XGBoost (Lab 3)
- Por qué split temporal
- Por qué extrapolación es más arriesgada que interpolación""",
    nota_asistente=False,
)

CELDA_Q11 = celda_solucion_alumno(
    variables=[],
    pasos=["Respuesta breve opcional en markdown"],
    nota="Sección 11 sin autoevaluación de código.",
)
