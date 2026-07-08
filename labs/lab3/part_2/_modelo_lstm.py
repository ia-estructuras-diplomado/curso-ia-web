"""LSTM compartido entre notebook y _generar_modelos.py (Lab 3 Parte 2)."""
from __future__ import annotations

import json
from pathlib import Path

import torch
import torch.nn as nn

DATA_DIR = Path(__file__).parent / "data"
RUTA_CLF_PT = DATA_DIR / "lstm_classifier_best.pt"
RUTA_STRAIN_PT = DATA_DIR / "lstm_strain_best.pt"
RUTA_META = DATA_DIR / "model_meta.json"

FEATURES_DEFAULT = [
    "Accel_X (m/s^2)",
    "Accel_Y (m/s^2)",
    "Accel_Z (m/s^2)",
    "Strain (με)",
    "Temp (°C)",
]


class LSTMClassifier(nn.Module):
    def __init__(
        self,
        input_size: int = 5,
        hidden_size: int = 64,
        n_layers: int = 1,
        dropout: float = 0.2,
        n_classes: int = 3,
    ):
        super().__init__()
        self.hidden_size = hidden_size
        self.n_layers = n_layers
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=n_layers,
            batch_first=True,
            dropout=dropout if n_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, n_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])


class StrainLSTM(nn.Module):
    def __init__(self, hidden: int = 48):
        super().__init__()
        self.hidden = hidden
        self.lstm = nn.LSTM(1, hidden, batch_first=True)
        self.fc = nn.Linear(hidden, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.lstm(x)
        return self.fc(out)


def _load_state(model: nn.Module, ruta: Path, device: torch.device) -> None:
    checkpoint = torch.load(ruta, map_location=device, weights_only=False)
    state = checkpoint["state_dict"] if isinstance(checkpoint, dict) and "state_dict" in checkpoint else checkpoint
    model.load_state_dict(state)


def load_lstm_classifier(
    device: torch.device | None = None,
    ruta: Path | None = None,
) -> tuple[LSTMClassifier, dict]:
    device = device or torch.device("cpu")
    ruta = ruta or RUTA_CLF_PT
    if not ruta.is_file():
        raise FileNotFoundError(
            f"No se encontró {ruta}. Ejecuta (docente): python labs/lab3/_generar_modelos.py"
        )
    meta = json.loads(RUTA_META.read_text(encoding="utf-8")) if RUTA_META.is_file() else {}
    hp = meta.get("classifier", {}).get("hyperparameters", {})
    modelo = LSTMClassifier(
        input_size=hp.get("input_size", 5),
        hidden_size=hp.get("hidden_size", 64),
        n_layers=hp.get("n_layers", 1),
        dropout=hp.get("dropout", 0.2),
    )
    _load_state(modelo, ruta, device)
    modelo.to(device)
    modelo.eval()
    return modelo, meta


def load_strain_lstm(
    device: torch.device | None = None,
    ruta: Path | None = None,
) -> tuple[StrainLSTM, dict]:
    device = device or torch.device("cpu")
    ruta = ruta or RUTA_STRAIN_PT
    if not ruta.is_file():
        raise FileNotFoundError(
            f"No se encontró {ruta}. Ejecuta (docente): python labs/lab3/_generar_modelos.py"
        )
    meta = json.loads(RUTA_META.read_text(encoding="utf-8")) if RUTA_META.is_file() else {}
    hp = meta.get("strain_regressor", {}).get("hyperparameters", {})
    modelo = StrainLSTM(hidden=hp.get("hidden", 48))
    _load_state(modelo, ruta, device)
    modelo.to(device)
    modelo.eval()
    return modelo, meta
