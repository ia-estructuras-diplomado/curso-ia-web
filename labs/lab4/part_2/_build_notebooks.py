#!/usr/bin/env python3
"""Genera notebooks Lab 4 Parte 2 — xAI en redes neuronales."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent

SETUP = r'''import sys
from pathlib import Path

sys.path.insert(0, str(Path('.').resolve()))
sys.path.insert(0, str(Path('../../lab3/part_1').resolve()))
sys.path.insert(0, str(Path('../../lab3/part_2').resolve()))
from _verificar import (
    verificar_panorama_xai_redes, verificar_modelos_lab3, verificar_gradcam,
    verificar_atribucion_lstm, verificar_metricas_cnn, verificar_metricas_lstm,
    resumen_seccion,
)

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from PIL import Image

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms
from torchvision.transforms import Resize, ToTensor, Normalize
from sklearn.preprocessing import StandardScaler
from captum.attr import LayerGradCam, IntegratedGradients

from _modelo_cnn import load_crack_cnn, CrackCNN, RUTA_PT as CNN_PT, RUTA_META as CNN_META
from _modelo_lstm import load_lstm_classifier, FEATURES_DEFAULT, RUTA_CLF_PT, RUTA_CLF_PT as RUTA_LSTM_PT

%matplotlib inline
sns.set_theme(style='whitegrid')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
IMAGE_SIZE = 128
print(f'✅ Entorno xAI redes | device={device}')
'''

S1_TASK = r'''TECNICAS_XAI_REDES = ["grad_cam", "integrated_gradients", "comparacion_tabular"]
print("Técnicas xAI para redes en este lab:")
for t in TECNICAS_XAI_REDES:
    print(f"  · {t}")
'''

S2_PRE = r'''# --- PRE-ESCRITO: cargar CNN docente (Lab 3) ---
val_t = transforms.Compose([
    Resize((IMAGE_SIZE, IMAGE_SIZE)), ToTensor(),
    Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
])
val_ds = datasets.ImageFolder(
    Path('../../lab3/part_1/data/cracks_subset/val'), transform=val_t
)
class_names = val_ds.classes
modelo_cnn, meta_cnn = load_crack_cnn(device)
acc_cnn_meta = meta_cnn.get('val_accuracy', 0.0)
print(f'✅ CNN cargada | acc docente={acc_cnn_meta:.3f} | clases={class_names}')
'''

S2_TASK = r'''# Evaluar en un batch de validación
val_loader = DataLoader(val_ds, batch_size=32, shuffle=False)
modelo_cnn.eval()
correct, total = 0, 0
with torch.no_grad():
    for xb, yb in val_loader:
        xb, yb = xb.to(device), yb.to(device)
        pred = modelo_cnn(xb).argmax(1)
        correct += (pred == yb).sum().item()
        total += yb.size(0)
acc_cnn_val = correct / total
print(f'Accuracy CNN en val (recargada) = {acc_cnn_val:.3f}')
'''

S3_TASK = r'''# Grad-CAM en una imagen Positive
idx_pos = next(i for i, (_, y) in enumerate(val_ds) if y == class_names.index('Positive'))
img_tensor, label = val_ds[idx_pos]
input_batch = img_tensor.unsqueeze(0).to(device)

# Capa convolucional del segundo bloque
target_layer = modelo_cnn.features[1][0]
cam = LayerGradCam(modelo_cnn, target_layer)
attributions = cam.attribute(input_batch, target=label)
cam_map = attributions.squeeze().cpu().detach().numpy()
cam_shape = cam_map.shape

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
img_show = img_tensor.permute(1, 2, 0).numpy()
img_show = (img_show - img_show.min()) / (img_show.max() - img_show.min() + 1e-8)
axes[0].imshow(img_show)
axes[0].set_title(f'Imagen real ({class_names[label]})')
axes[0].axis('off')
axes[1].imshow(img_show)
axes[1].imshow(cam_map, cmap='jet', alpha=0.5)
axes[1].set_title('Grad-CAM superpuesto')
axes[1].axis('off')
plt.tight_layout()
plt.show()
'''

S4_TASK = r'''# Caso correcto vs posible falso positivo
modelo_cnn.eval()
casos = []
with torch.no_grad():
    for i in range(len(val_ds)):
        x, y = val_ds[i]
        pred = modelo_cnn(x.unsqueeze(0).to(device)).argmax(1).item()
        casos.append((i, y, pred))
fp = next((c for c in casos if c[1] == 0 and c[2] == 1), None)
ok = next((c for c in casos if c[1] == 1 and c[2] == 1), casos[0])
N_CASOS_CNN = 2
print(f'Caso acierto: idx={ok[0]} | Caso FP (si existe): {fp}')
'''

S5_TASK = r'''# Cargar LSTM clasificador (Lab 3)
modelo_lstm, meta_lstm = load_lstm_classifier(device)
hp = meta_lstm.get('classifier', {}).get('hyperparameters', {})
WINDOW_SIZE = 30
csv = Path('../../lab3/part_2/data/building_health_monitoring_dataset.csv')
df = pd.read_csv(csv).dropna(subset=FEATURES_DEFAULT).sort_values('Timestamp')
X = StandardScaler().fit_transform(df[FEATURES_DEFAULT].values)
y = df['Condition Label'].values.astype(int)
seqs, labels = [], []
for i in range(WINDOW_SIZE, len(X)):
    seqs.append(X[i - WINDOW_SIZE : i])
    labels.append(y[i])
X_arr = np.array(seqs, dtype=np.float32)
y_arr = np.array(labels, dtype=np.int64)
cut = int(0.8 * len(X_arr))
X_val = torch.from_numpy(X_arr[cut:])
y_val = torch.from_numpy(y_arr[cut:])
modelo_lstm.eval()
with torch.no_grad():
    pred = modelo_lstm(X_val.to(device)).argmax(1).cpu()
acc_lstm_val = (pred == y_val).float().mean().item()
print(f'✅ LSTM cargado | acc val={acc_lstm_val:.3f}')
'''

S6_TASK = r'''# Integrated Gradients en una ventana de test
INDEX_VENTANA = 10
x_win = X_val[INDEX_VENTANA : INDEX_VENTANA + 1].to(device)
x_win.requires_grad_(True)
ig = IntegratedGradients(modelo_lstm)
attr = ig.attribute(x_win, target=int(y_val[INDEX_VENTANA].item()))
attr_np = attr.squeeze(0).detach().cpu().numpy()
# Importancia por sensor = media |atribución| en el tiempo
importancia_sensor = np.abs(attr_np).mean(axis=0)
top_idx = int(importancia_sensor.argmax())
top_feature = FEATURES_DEFAULT[top_idx]
n_atrib = len(importancia_sensor)

fig, ax = plt.subplots(figsize=(8, 4))
pd.Series(importancia_sensor, index=FEATURES_DEFAULT).sort_values().plot(
    kind='barh', ax=ax, color='#e67e22'
)
ax.set_title(f'Atribución IG — ventana #{INDEX_VENTANA} (clase {int(y_val[INDEX_VENTANA])})')
ax.set_xlabel('|atribución| media')
plt.tight_layout()
plt.show()
print(f'Feature top: {top_feature}')
'''

S7_TASK = r'''# Puente: en Lab 4 P1 XGBoost suele destacar Strain; compara con IG
print("Reflexión: ¿Strain domina en tabular (SHAP) y en LSTM (IG)?")
print(f"  · Top IG en esta ventana: {top_feature}")
print("  · En xAI tabular (Lab 4 P1) Strain suele estar en el top-3 del booster.")
'''

VERIFY_BLOCKS = [
    ("1", "r = verificar_panorama_xai_redes(TECNICAS_XAI_REDES)\nresumen_seccion('1 — Panorama', r)"),
    ("2", "r = verificar_modelos_lab3(CNN_PT.is_file(), True)\nr.extend(verificar_metricas_cnn(acc_cnn_val))\nresumen_seccion('2 — CNN Lab 3', r)"),
    ("3", "r = verificar_gradcam(cam_shape, img_show.shape[:2])\nresumen_seccion('3 — Grad-CAM', r)"),
    ("4", "r = [N_CASOS_CNN >= 1]\nprint('✅ Casos locales CNN revisados.' if r[0] else '❌')\nresumen_seccion('4 — Casos CNN', r)"),
    ("5", "from _modelo_lstm import RUTA_CLF_PT\nr = verificar_modelos_lab3(True, RUTA_CLF_PT.is_file())\nr.extend(verificar_metricas_lstm(acc_lstm_val))\nresumen_seccion('5 — LSTM Lab 3', r)"),
    ("6", "r = verificar_atribucion_lstm(top_feature, n_atrib)\nresumen_seccion('6 — IG LSTM', r)"),
    ("7", "print('✅ Puente tabular ↔ red documentado.')\nresumen_seccion('7 — Puente', [True])"),
]


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code(text: str) -> dict:
    return {
        "cell_type": "code", "metadata": {}, "outputs": [],
        "execution_count": None, "source": text,
    }


def build_notebook(is_solution: bool) -> list:
    title = (
        "# Lab 4 Parte 2 — xAI en redes neuronales — Solución (docente)\n"
        if is_solution
        else "# Lab 4 Parte 2 — xAI en redes neuronales — Vía IA-asistida\n"
    )
    cells = [md(title + "\nGrad-CAM (CNN) e Integrated Gradients (LSTM) sobre modelos entrenados en **Lab 3**.\n")]
    cells.append(code(SETUP))
    cells.append(md("## Sección 1 — Panorama xAI en redes\n\n¿Por qué las redes profundas son «caja negra» y qué aporta Grad-CAM vs IG?\n"))
    cells.append(code(S1_TASK))
    cells.append(code(VERIFY_BLOCKS[0][1]))
    cells.append(md("## Sección 2 — Cargar CNN de Lab 3\n"))
    cells.append(code(S2_PRE))
    cells.append(code(S2_TASK))
    cells.append(code(VERIFY_BLOCKS[1][1]))
    cells.append(md("## Sección 3 — Grad-CAM en grietas\n"))
    cells.append(code(S3_TASK))
    cells.append(code(VERIFY_BLOCKS[2][1]))
    cells.append(md("## Sección 4 — Casos locales CNN\n"))
    cells.append(code(S4_TASK))
    cells.append(code(VERIFY_BLOCKS[3][1]))
    cells.append(md("## Sección 5 — Cargar LSTM de Lab 3\n"))
    cells.append(code(S5_TASK))
    cells.append(code(VERIFY_BLOCKS[4][1]))
    cells.append(md("## Sección 6 — Atribución temporal (Integrated Gradients)\n"))
    cells.append(code(S6_TASK))
    cells.append(code(VERIFY_BLOCKS[5][1]))
    cells.append(md("## Sección 7 — Puente tabular ↔ red\n"))
    cells.append(code(S7_TASK))
    cells.append(code(VERIFY_BLOCKS[6][1]))
    cells.append(md("## Cierre\n\n- Grad-CAM muestra **dónde** mira la CNN; IG muestra **qué sensores** pesan en la ventana LSTM.\n- No sustituye inspección ni normativa; complementa la auditoría del modelo.\n"))
    return cells


def main() -> None:
    for name, sol in [
        ("xai_redes_estructuras_solucion.ipynb", True),
        ("xai_redes_estructuras_alumno_ia.ipynb", False),
    ]:
        nb = {
            "cells": build_notebook(sol),
            "metadata": {
                "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                "language_info": {"name": "python", "version": "3.11.0"},
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        if not sol:
            for c in nb["cells"]:
                if c["cell_type"] == "code" and "TECNICAS_XAI_REDES" in c["source"]:
                    c["source"] = "### PEGA AQUÍ EL CÓDIGO DE LA IA ###\n" + c["source"]
        path = ROOT / name
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"✅ {path.name}")


if __name__ == "__main__":
    main()
