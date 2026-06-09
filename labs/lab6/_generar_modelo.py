"""Entrena MLP (best model) con escenarios de seismic_data.csv — solo docente."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DIR = Path(__file__).parent
sys.path.insert(0, str(DIR))

from _preparar_datos import main as preparar_datos  # noqa: E402
from _verificar import (  # noqa: E402
    RUTA_CSV,
    RUTA_META,
    RUTA_PKL,
    TELEMETRIA_DB,
    material_to_index,
    predecir_probabilidad_dano,
    soil_type_to_index,
)

FEATURE_NAMES = [
    "spectral_acceleration_g",
    "soil_type_index",
    "structural_period_s",
    "max_drift_ratio",
    "height_m",
    "material_index",
]

MATERIAL_MAP = {"Steel": 1, "Concrete": 2, "Masonry": 3, "Composite": 4}


def riesgo_ingenieria(
    pga: float,
    soil: int,
    period: float,
    drift: float,
    height: float,
    material_idx: int,
) -> float:
    """Etiqueta coherente con criterio estructural (el CSV original no correlaciona targets)."""
    base = (
        0.22 * min(pga / 1.5, 1.0)
        + 0.28 * (soil / 3.0)
        + 0.12 * min(period / 1.5, 1.0)
        + 0.28 * min(drift / 0.035, 1.0)
        + 0.10 * min(height / 80.0, 1.0)
    )
    vuln = {1: 0.0, 2: 0.04, 3: 0.08, 4: 0.10}.get(material_idx, 0.05)
    if soil >= 3:
        vuln += 0.12
    if material_idx == 4 and soil >= 3:
        vuln += 0.08
    if material_idx == 1 and soil == 1:
        vuln -= 0.18
    if drift < 0.01 and soil <= 2:
        vuln -= 0.08
    return float(np.clip(base + vuln, 0.05, 0.99))


def build_xy(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    x_rows = []
    y_rows = []
    for _, row in df.iterrows():
        freq = float(row["Natural Frequency (Hz)"])
        period = 1.0 / freq if freq > 0 else 4.0
        drift = float(row["Predicted Max Inter-Story Drift Ratio (%)"]) / 100.0
        height = float(row["Building Height (m)"])
        mat = MATERIAL_MAP.get(str(row["Structural Material"]), 2)
        soil = soil_type_to_index(str(row["Soil Type"]))
        pga = float(row["Spectral Acceleration (g)"])
        x_rows.append([pga, soil, period, drift, height, float(mat)])
        y_rows.append(
            riesgo_ingenieria(pga, soil, period, drift, height, mat)
        )
    return np.array(x_rows), np.array(y_rows)


def assert_escenarios() -> None:
    checks = {
        "BLDG-A": ("<", 0.40),
        "BLDG-B": (">", 0.70),
        "BLDG-C": (">", 0.40),
    }
    for bid, (op, umbral) in checks.items():
        t = TELEMETRIA_DB[bid]
        prob, _ = predecir_probabilidad_dano(
            t["expected_pga_g"],
            t["soil_type_index"],
            t["structural_period_s"],
            max_drift_ratio=t["max_drift_ratio"],
            height_m=t["height_m"],
            material=t["material"],
            ruta_modelo=RUTA_PKL,
        )
        ok = prob < umbral if op == "<" else prob > umbral
        if not ok:
            raise AssertionError(f"{bid}: prob={prob:.3f} no cumple {op} {umbral}")
        print(f"✅ {bid}: prob daño severo = {prob * 100:.1f}%")


def main() -> None:
    preparar_datos()
    if not RUTA_CSV.is_file():
        raise FileNotFoundError(RUTA_CSV)

    df = pd.read_csv(RUTA_CSV)
    x, y = build_xy(df)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "mlp",
                MLPRegressor(
                    hidden_layer_sizes=(64, 32),
                    activation="relu",
                    max_iter=800,
                    early_stopping=True,
                    validation_fraction=0.15,
                    random_state=42,
                ),
            ),
        ]
    )
    pipeline.fit(x_train, y_train)

    y_pred = pipeline.predict(x_test)
    test_r2 = float(r2_score(y_test, y_pred))
    test_mae = float(mean_absolute_error(y_test, y_pred))
    val_score = float(
        getattr(pipeline.named_steps["mlp"], "best_validation_score_", test_r2)
    )

    RUTA_PKL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, RUTA_PKL)

    meta = {
        "tipo": "MLP",
        "architecture": "StandardScaler + MLPRegressor(64, 32)",
        "features": FEATURE_NAMES,
        "target": "riesgo_colapso_prob [0-1] (criterio ingeniería sobre escenarios CSV)",
        "n_train": int(len(x_train)),
        "n_test": int(len(x_test)),
        "val_score": round(val_score, 4),
        "test_r2": round(test_r2, 4),
        "test_mae": round(test_mae, 4),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }
    RUTA_META.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"✅ Modelo guardado: {RUTA_PKL}")
    print(f"✅ Meta guardada: {RUTA_META}")
    print(f"   test_r2={test_r2:.4f} | test_mae={test_mae:.4f}")

    assert_escenarios()


if __name__ == "__main__":
    main()
