#!/usr/bin/env python3
"""Smoke test docente — Lab 4 Parte 1 (xAI tabular)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent.parent))
from _smoke_common import assert_all_pass, check_file, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

import pandas as pd  # noqa: E402

from _verificar import FEATURES_ESPERADAS, verificar_carga, verificar_panorama_xai  # noqa: E402


def main() -> None:
    csv = ROOT / "data" / "building_health_monitoring_dataset.csv"
    section("Lab 4 P1 xAI — datos")
    if not check_file(csv):
        prep = ROOT / "_preparar_datos.py"
        if prep.is_file():
            import subprocess
            subprocess.run([sys.executable, str(prep)], check=False)
        if not csv.is_file():
            raise SystemExit("❌ Falta CSV — ejecuta _preparar_datos.py")

    df = pd.read_csv(csv)
    section("Lab 4 P1 — verificadores")
    tecnicas = ["importancia", "permutation", "shap", "lime", "pdp"]
    assert_all_pass(run_quiet(lambda: verificar_panorama_xai(tecnicas)), "panorama")
    assert_all_pass(run_quiet(lambda: verificar_carga(df, 5, FEATURES_ESPERADAS)), "carga")
    print("\n✅ Lab 4 Parte 1 (xAI tabular) smoke OK")


if __name__ == "__main__":
    main()
