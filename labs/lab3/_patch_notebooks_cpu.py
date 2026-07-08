#!/usr/bin/env python3
"""Parchea notebooks Lab 3 P1/P2: CPU, modelo docente + entrenamiento corto alumno."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent

DEVICE_CPU = "device = torch.device('cpu')  # Codespaces / Binder: solo CPU\nprint(f\"✅ Entorno listo | device={device} (entrenamiento corto alumno)\")"

CNN_SETUP_IMPORTS = """from _verificar import (
    verificar_panorama_cnn, verificar_eda_dataset, verificar_augmentation,
    verificar_dataloaders, verificar_arquitectura, verificar_entrenamiento,
    verificar_curvas, verificar_metricas, verificar_casos_locales, resumen_seccion,
    verificar_modelo_docente_cargado, verificar_comparacion_docente,
)
from _modelo_cnn import CrackCNN, load_crack_cnn"""

LSTM_SETUP_IMPORTS = """from _verificar import (
    verificar_panorama_rnn, verificar_carga_datos, verificar_eda_sensores,
    verificar_comparacion_sensores, verificar_ventanas, verificar_arquitectura_lstm,
    verificar_entrenamiento_lstm, verificar_interpolacion, verificar_extrapolacion,
    resumen_seccion, verificar_modelo_docente_lstm, verificar_comparacion_docente_lstm,
)
from _modelo_lstm import LSTMClassifier, StrainLSTM, load_lstm_classifier, load_strain_lstm"""

CNN_DOCENTE_MD = """## Pregunta 5b — Modelo docente (referencia)

El archivo `data/crack_cnn_best.pt` es el **mejor modelo** entrenado por el docente (más épocas, más filtros, BatchNorm). Lo cargamos **sin reentrenar** para comparar con tu modelo pequeño.

### 📘 Subpreguntas
- **5b.a** ¿Qué hiperparámetros usa el docente (`model_meta.json`)?
- **5b.b** ¿Por qué no reentrenamos este checkpoint en clase?
"""

CNN_DOCENTE_CODE = """# --- PRE-ESCRITO: cargar modelo docente (no reentrenar) ---
modelo_docente, meta_docente = load_crack_cnn(device=device)
hp_docente = meta_docente.get('hyperparameters', {})
N_EPOCHS_DOCENTE = hp_docente.get('epochs', 15)
_, acc_docente = eval_epoch(modelo_docente, val_loader, nn.CrossEntropyLoss(), device)
print(f"Modelo docente | acc val = {acc_docente:.3f}")
print(f"Hiperparámetros docente: {hp_docente}")
"""

CNN_COMPARE_MD = """## Pregunta 8 — Comparación: tu modelo vs docente

Entrenaste **pocas épocas en CPU** con una CNN más pequeña. El docente usó **más tiempo y mejores hiperparámetros**. Compara accuracy y reflexiona.

### 📘 Subpreguntas
- **8.a** ¿Cuánto mejora el modelo docente respecto al tuyo?
- **8.b** ¿Qué cambió entre ambos (épocas, `n_filters`, BatchNorm)?
- **8.c** ¿Vale la pena en obra pagar más cómputo por ese salto?
"""

CNN_COMPARE_CODE_SOL = """acc_alumno = history['val_acc'][-1]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(
    [f'Tu modelo\\n({N_EPOCHS} ép., CPU)', f'Docente\\n({N_EPOCHS_DOCENTE} ép., ref)'],
    [acc_alumno, acc_docente],
    color=['#3498db', '#27ae60'],
)
ax.set_ylim(0, 1.05)
ax.set_ylabel('Accuracy validación')
ax.set_title('Comparación alumno vs modelo docente')
for i, v in enumerate([acc_alumno, acc_docente]):
    ax.text(i, v + 0.02, f'{v:.3f}', ha='center')
plt.tight_layout()
plt.show()
print(f"Tu modelo: acc={acc_alumno:.3f} | n_filters={N_FILTERS} | épocas={N_EPOCHS}")
print(f"Docente:   acc={acc_docente:.3f} | hp={hp_docente}")
"""

CNN_COMPARE_CODE_ALUM = """# --- PRE-ESCRITO: gráfico comparación (usa tu history y el docente cargado) ---
acc_alumno = history['val_acc'][-1]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(
    [f'Tu modelo\\n({N_EPOCHS} ép., CPU)', f'Docente\\n({N_EPOCHS_DOCENTE} ép., ref)'],
    [acc_alumno, acc_docente],
    color=['#3498db', '#27ae60'],
)
ax.set_ylim(0, 1.05)
ax.set_ylabel('Accuracy validación')
ax.set_title('Comparación alumno vs modelo docente')
for i, v in enumerate([acc_alumno, acc_docente]):
    ax.text(i, v + 0.02, f'{v:.3f}', ha='center')
plt.tight_layout()
plt.show()
print("Reflexiona: ¿qué hiperparámetros explican la diferencia?")
"""

CNN_COMPARE_AUTO = """# --- Autoevaluación 8 (comparación) ---
r = []
try:
    r = verificar_comparacion_docente(acc_alumno, acc_docente, N_EPOCHS, N_EPOCHS_DOCENTE)
except NameError as err:
    print(f"❌ Ejecuta primero las celdas anteriores. Falta: {err}")
    r = [False]
resumen_seccion('8 — Comparación docente', r)
"""

CNN_METRICS_MD_OLD = "## Pregunta 8 — Métricas en validación"
CNN_METRICS_MD_NEW = """## Pregunta 9 — Métricas en validación (modelo docente)

Usamos el **modelo docente** para la matriz de confusión y el informe (mejor calidad que tu entrenamiento corto).

### 📘 Subpreguntas
- **9.a** ¿Qué clase se confunde más?
- **9.b** ¿Un falso positivo (grieta) es más grave que un falso negativo?
"""

LSTM_DOCENTE_MD = """## Pregunta 7b — Modelo docente LSTM (referencia)

`data/lstm_classifier_best.pt` es el clasificador entrenado más tiempo por el docente. Lo cargamos para comparar con tu LSTM corto.

### 📘 Subpreguntas
- **7b.a** ¿Qué `hidden_size` y épocas usó el docente?
- **7b.b** ¿Por qué entrenamos poco en CPU en clase?
"""

LSTM_DOCENTE_CODE = """# --- PRE-ESCRITO: clasificador docente ---
modelo_docente, meta_docente = load_lstm_classifier(device=device)
hp_docente = meta_docente.get('classifier', {}).get('hyperparameters', {})
N_EPOCHS_DOCENTE = hp_docente.get('epochs', 10)
acc_docente = meta_docente.get('classifier', {}).get('val_accuracy', hp_docente.get('val_accuracy', 0.0))
_, acc_docente_live = eval_epoch(modelo_docente, val_loader, nn.CrossEntropyLoss(), device)
acc_docente = float(acc_docente_live)
print(f"Modelo docente LSTM | acc val = {acc_docente:.3f}")
print(f"Hiperparámetros docente: {hp_docente}")
"""

LSTM_COMPARE_MD = """## Pregunta 9 — Comparación: tu LSTM vs docente

### 📘 Subpreguntas
- **9.a** ¿Cuánto gana el docente en accuracy?
- **9.b** ¿Más `hidden_size` o más épocas explican la brecha?
"""

LSTM_COMPARE_CODE = """acc_alumno = acc_val
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(
    [f'Tu LSTM\\n({N_EPOCHS} ép.)', f'Docente\\n({N_EPOCHS_DOCENTE} ép.)'],
    [acc_alumno, acc_docente],
    color=['#9b59b6', '#27ae60'],
)
ax.set_ylim(0, 1.05)
ax.set_ylabel('Accuracy validación')
ax.set_title('Comparación clasificador alumno vs docente')
for i, v in enumerate([acc_alumno, acc_docente]):
    ax.text(i, v + 0.02, f'{v:.3f}', ha='center')
plt.tight_layout()
plt.show()
"""

LSTM_COMPARE_AUTO = """# --- Autoevaluación 9 (comparación) ---
r = []
try:
    r = verificar_comparacion_docente_lstm(acc_alumno, acc_docente, N_EPOCHS, N_EPOCHS_DOCENTE)
except NameError as err:
    print(f"❌ Falta: {err}")
    r = [False]
resumen_seccion('9 — Comparación docente', r)
"""

STRAIN_CELL_OLD_START = "# --- PRE-ESCRITO: LSTM regresor Strain + tests interpolación/extrapolación ---"
STRAIN_CELL_NEW = """# --- PRE-ESCRITO: regresor Strain docente + helpers interp/extrap ---
strain_raw = df_limpio['Strain (με)'].values.astype(np.float32)
strain_norm = (strain_raw - strain_raw.mean()) / (strain_raw.std() + 1e-8)
SEGMENTO_LEN = 120
W_EXTRAP = 80

modelo_reg, meta_strain = load_strain_lstm(device=device)
hp_strain = meta_strain.get('strain_regressor', {}).get('hyperparameters', {})
mae_interp_docente = meta_strain.get('strain_regressor', {}).get('mae_interp', 0.71)
mae_extrap_docente = meta_strain.get('strain_regressor', {}).get('mae_extrap', 0.90)
print(f"Regresor Strain docente | MAE ref interp={mae_interp_docente:.3f} extrap={mae_extrap_docente:.3f}")
print(f"Hiperparámetros: {hp_strain}")
print("Compara tus MAE con estos valores de referencia (entrenado más tiempo).")

def evaluar_interpolacion(model, serie, gap_inicio, gap_fin, seg_len=SEGMENTO_LEN):
    seg = serie[200 : 200 + seg_len].copy()
    entrada = seg.copy()
    entrada[gap_inicio:gap_fin] = 0.0
    x = torch.tensor(entrada[:, None], dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = model(x).squeeze().cpu().numpy()
    real = seg[gap_inicio:gap_fin]
    pred_gap = pred[gap_inicio:gap_fin]
    mae = float(np.mean(np.abs(real - pred_gap)))
    return mae, real, pred_gap

def evaluar_extrapolacion(model, serie, w, horizonte, start=300):
    full_len = w + horizonte
    hist = serie[start : start + w]
    real_fut = serie[start + w : start + w + horizonte]
    entrada = np.zeros(full_len, dtype=np.float32)
    entrada[:w] = hist
    x = torch.tensor(entrada[:, None], dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = model(x).squeeze().cpu().numpy()
    pred_fut = pred[w : w + horizonte]
    mae = float(np.mean(np.abs(real_fut - pred_fut)))
    return mae, hist, real_fut, pred_fut

print("✅ modelo_reg cargado desde checkpoint | helpers listos.")
"""


def _cell_source(cells: list, idx: int) -> str:
    return "".join(cells[idx]["source"])


def _set_cell_source(cells: list, idx: int, text: str) -> None:
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    cells[idx]["source"] = lines


def _find_cell(cells: list, needle: str) -> int:
    for i, c in enumerate(cells):
        if needle in _cell_source(cells, i):
            return i
    return -1


def _insert_after(cells: list, idx: int, new_cells: list[dict]) -> None:
    for j, nc in enumerate(new_cells):
        cells.insert(idx + 1 + j, nc)


def _md_cell(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def _code_cell(text: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.splitlines(keepends=True)}


def patch_cnn(nb_path: Path, alumno: bool) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = nb["cells"]

    # setup
    setup = _find_cell(cells, "from _verificar import")
    src = _cell_source(cells, setup)
    if "verificar_modelo_docente_cargado" not in src:
        old = """from _verificar import (
    verificar_panorama_cnn, verificar_eda_dataset, verificar_augmentation,
    verificar_dataloaders, verificar_arquitectura, verificar_entrenamiento,
    verificar_curvas, verificar_metricas, verificar_casos_locales, resumen_seccion,
)"""
        src = src.replace(old, CNN_SETUP_IMPORTS)
    src = src.replace(
        "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\nprint(f\"✅ Entorno listo | device={device}\")",
        DEVICE_CPU,
    )
    if "from _modelo_cnn import" not in src:
        src = src.replace(
            "from PIL import Image\n",
            "from PIL import Image\n\nfrom _modelo_cnn import CrackCNN, load_crack_cnn\n",
        )
    _set_cell_source(cells, setup, src)

    # architecture: use shared CrackCNN small
    arch = _find_cell(cells, "class CrackCNN")
    if arch >= 0:
        if alumno:
            new_arch = """N_FILTERS = 32
DROPOUT = 0.3

modelo = CrackCNN(n_filters=N_FILTERS, dropout=DROPOUT, use_batchnorm=False).to(device)
print(modelo)
"""
        else:
            new_arch = """N_FILTERS = 32
DROPOUT = 0.3

modelo = CrackCNN(n_filters=N_FILTERS, dropout=DROPOUT, use_batchnorm=False).to(device)
print(modelo)
"""
        _set_cell_source(cells, arch, new_arch)

    # insert docente after train/eval helpers (Q6 pre-written)
    if _find_cell(cells, "load_crack_cnn(device=device)") < 0:
        train_fn = _find_cell(cells, 'print("✅ Funciones train_one_epoch / eval_epoch listas.")')
        if train_fn >= 0:
            _insert_after(cells, train_fn, [_md_cell(CNN_DOCENTE_MD), _code_cell(CNN_DOCENTE_CODE)])

    # N_EPOCHS = 3
    train_cell = _find_cell(cells, "N_EPOCHS = 5")
    if train_cell >= 0:
        src = _cell_source(cells, train_cell)
        src = src.replace("N_EPOCHS = 5", "N_EPOCHS = 3")
        if "acc_alumno" not in src:
            src = src.replace(
                'print("✅ Entrenamiento completado.")',
                'acc_alumno = history[\'val_acc\'][-1]\nprint(f"✅ Entrenamiento corto completado | acc_val={acc_alumno:.3f}")',
            )
            if "acc_alumno" not in src:
                src += "\nacc_alumno = history['val_acc'][-1]\nprint(f\"✅ Entrenamiento corto | acc_val={acc_alumno:.3f}\")\n"
        _set_cell_source(cells, train_cell, src)

    # comparison before metrics
    metrics_md = _find_cell(cells, CNN_METRICS_MD_OLD)
    if metrics_md >= 0 and _find_cell(cells, "Comparación alumno vs modelo docente") < 0:
        _insert_after(
            cells,
            metrics_md - 1,
            [
                _md_cell(CNN_COMPARE_MD),
                _code_cell(CNN_COMPARE_CODE_ALUM if alumno else CNN_COMPARE_CODE_SOL),
                _code_cell(CNN_COMPARE_AUTO),
            ],
        )
        _set_cell_source(cells, metrics_md, CNN_METRICS_MD_NEW)

    # metrics use modelo_docente
    metrics_code = _find_cell(cells, "modelo.eval()")
    if metrics_code >= 0 and "modelo_docente" not in _cell_source(cells, metrics_code):
        src = _cell_source(cells, metrics_code)
        src = src.replace("modelo.eval()", "modelo_docente.eval()")
        src = src.replace("modelo(images)", "modelo_docente(images)")
        _set_cell_source(cells, metrics_code, src)

    # renumber autoeval metrics 8 -> 9
    mauto = _find_cell(cells, "resumen_seccion('8 — Métricas'")
    if mauto >= 0:
        src = _cell_source(cells, mauto)
        src = src.replace("resumen_seccion('8 — Métricas'", "resumen_seccion('9 — Métricas'")
        _set_cell_source(cells, mauto, src)

    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ {nb_path.name}")


def patch_lstm(nb_path: Path, alumno: bool) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells = nb["cells"]

    setup = _find_cell(cells, "from _verificar import")
    src = _cell_source(cells, setup)
    old_imports = [
        """from _verificar import (
    verificar_panorama_rnn, verificar_carga_datos, verificar_eda_sensores,
    verificar_comparacion_sensores, verificar_ventanas, verificar_arquitectura_lstm,
    verificar_entrenamiento_lstm, verificar_interpolacion, verificar_extrapolacion,
    resumen_seccion,
)""",
        """from _verificar import (
    verificar_panorama_rnn, verificar_carga_datos, verificar_eda_sensores,
    verificar_comparacion_sensores, verificar_ventanas, verificar_arquitectura_lstm,
    verificar_entrenamiento_lstm, verificar_interpolacion, verificar_extrapolacion,
    resumen_seccion,
)
""",
    ]
    for old in old_imports:
        if old in src:
            src = src.replace(old, LSTM_SETUP_IMPORTS)
    src = src.replace(
        "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')",
        "device = torch.device('cpu')",
    )
    if "from _modelo_lstm import" not in src:
        src = src.replace(
            "import torch.nn as nn\n",
            "import torch.nn as nn\nfrom _modelo_lstm import LSTMClassifier, StrainLSTM, load_lstm_classifier, load_strain_lstm\n",
        )
    _set_cell_source(cells, setup, src)

    arch = _find_cell(cells, "class LSTMClassifier")
    if arch >= 0:
        _set_cell_source(
            cells,
            arch,
            """HIDDEN_SIZE = 64
N_LAYERS = 1
DROPOUT = 0.2

modelo = LSTMClassifier(
    input_size=len(FEATURES), hidden_size=HIDDEN_SIZE,
    n_layers=N_LAYERS, dropout=DROPOUT,
).to(device)
print(modelo)
""",
        )

    train_fn = _find_cell(cells, 'print("✅ Funciones train_one_epoch / eval_epoch listas.")')
    if _find_cell(cells, "load_lstm_classifier(device=device)") < 0:
        _insert_after(cells, train_fn, [_md_cell(LSTM_DOCENTE_MD), _code_cell(LSTM_DOCENTE_CODE)])

    train_cell = _find_cell(cells, "N_EPOCHS = 5")
    if train_cell >= 0:
        src = _cell_source(cells, train_cell).replace("N_EPOCHS = 5", "N_EPOCHS = 3")
        _set_cell_source(cells, train_cell, src)

    strain = _find_cell(cells, STRAIN_CELL_OLD_START)
    if strain >= 0:
        _set_cell_source(cells, strain, STRAIN_CELL_NEW)

    # comparison after train autoeval
    train_auto = _find_cell(cells, "resumen_seccion('8 — Entrenamiento'")
    if train_auto >= 0 and _find_cell(cells, "Comparación clasificador alumno") < 0:
        _insert_after(
            cells,
            train_auto,
            [_md_cell(LSTM_COMPARE_MD), _code_cell(LSTM_COMPARE_CODE), _code_cell(LSTM_COMPARE_AUTO)],
        )

    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ {nb_path.name}")


def main() -> None:
    patch_cnn(ROOT / "part_1/cnn_grietas_estructuras_solucion.ipynb", alumno=False)
    patch_cnn(ROOT / "part_1/cnn_grietas_estructuras_alumno_ia.ipynb", alumno=True)
    patch_lstm(ROOT / "part_2/rnn_sensores_estructuras_solucion.ipynb", alumno=False)
    patch_lstm(ROOT / "part_2/rnn_sensores_estructuras_alumno_ia.ipynb", alumno=True)


if __name__ == "__main__":
    main()
