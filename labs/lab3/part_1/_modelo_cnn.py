"""CrackCNN compartido entre notebook y _generar_modelos.py (Lab 3 Parte 1)."""
from __future__ import annotations

import json
from pathlib import Path

import torch
import torch.nn as nn

DATA_DIR = Path(__file__).parent / "data"
RUTA_PT = DATA_DIR / "crack_cnn_best.pt"
RUTA_META = DATA_DIR / "model_meta.json"


class CrackCNN(nn.Module):
    def __init__(self, n_filters: int = 32, dropout: float = 0.3, use_batchnorm: bool = False):
        super().__init__()
        self.n_filters = n_filters
        self.dropout_p = dropout
        self.use_batchnorm = use_batchnorm

        def conv_block(in_ch: int, out_ch: int) -> nn.Sequential:
            layers: list[nn.Module] = [nn.Conv2d(in_ch, out_ch, 3, padding=1)]
            if use_batchnorm:
                layers.append(nn.BatchNorm2d(out_ch))
            layers.extend([nn.ReLU(), nn.MaxPool2d(2)])
            return nn.Sequential(*layers)

        self.features = nn.Sequential(
            conv_block(3, n_filters),
            conv_block(n_filters, n_filters * 2),
            nn.AdaptiveAvgPool2d((4, 4)),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(n_filters * 2 * 16, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 2),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.classifier(self.features(x))


def load_crack_cnn(
    device: torch.device | None = None,
    ruta: Path | None = None,
) -> tuple[CrackCNN, dict]:
    """Carga pesos docente y devuelve (modelo, meta)."""
    device = device or torch.device("cpu")
    ruta = ruta or RUTA_PT
    if not ruta.is_file():
        raise FileNotFoundError(
            f"No se encontró {ruta}. Ejecuta (docente): python labs/lab3/_generar_modelos.py"
        )
    meta = json.loads(RUTA_META.read_text(encoding="utf-8")) if RUTA_META.is_file() else {}
    hp = meta.get("hyperparameters", {})
    modelo = CrackCNN(
        n_filters=hp.get("n_filters", 32),
        dropout=hp.get("dropout", 0.3),
        use_batchnorm=hp.get("use_batchnorm", False),
    )
    checkpoint = torch.load(ruta, map_location=device, weights_only=False)
    if isinstance(checkpoint, dict) and "state_dict" in checkpoint:
        modelo.load_state_dict(checkpoint["state_dict"])
    else:
        modelo.load_state_dict(checkpoint)
    modelo.to(device)
    modelo.eval()
    return modelo, meta
