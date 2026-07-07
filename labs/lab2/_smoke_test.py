#!/usr/bin/env python3
"""Smoke test docente — Lab 2 (carga UCI + verificadores clave)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from _smoke_common import assert_all_pass, check_file, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

import pandas as pd  # noqa: E402
from sklearn.ensemble import RandomForestRegressor  # noqa: E402
from sklearn.metrics import r2_score  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402

from _verificar import (  # noqa: E402
    verificar_carga,
    verificar_columna,
    verificar_correlaciones,
    verificar_modelo,
    verificar_split,
    verificar_tipo_problema,
)


def main() -> None:
    csv = ROOT / "data" / "concrete.csv"
    section("Lab 2 — datos")
    if not check_file(csv):
        raise SystemExit(1)

    df = pd.read_csv(csv)
    section("Lab 2 — verificadores")
    assert_all_pass(run_quiet(lambda: verificar_tipo_problema("regresión")), "tipo")
    assert_all_pass(run_quiet(lambda: verificar_carga(df, 5)), "carga")
    assert_all_pass(run_quiet(lambda: verificar_columna(df, "Resistencia")), "columna")

    corr = df.corr(numeric_only=True)["Resistencia"].abs().sort_values(ascending=False)
    top_corr = corr.drop("Resistencia").head(3).index.tolist()
    assert_all_pass(run_quiet(lambda: verificar_correlaciones(top_corr, 3)), "corr")

    features = [c for c in df.columns if c != "Resistencia"]
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], df["Resistencia"], test_size=0.2, random_state=42
    )
    assert_all_pass(
        run_quiet(lambda: verificar_split(len(x_train), len(x_test), 0.2, 42)),
        "split",
    )

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(x_train, y_train)
    y_pred = modelo.predict(x_test)
    r2 = float(r2_score(y_test, y_pred))
    importancias = dict(zip(features, modelo.feature_importances_))
    assert_all_pass(
        run_quiet(lambda: verificar_modelo(r2, 0.5, importancias)),
        "modelo",
    )
    print("\n✅ Lab 2 smoke OK")


if __name__ == "__main__":
    main()
