#!/usr/bin/env python3
"""Smoke test docente — Lab 6 (artefactos + verificadores sin Ollama)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from _smoke_common import assert_all_pass, check_file, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

import pandas as pd  # noqa: E402

from _verificar import (  # noqa: E402
    N_FILAS_CSV_REF,
    RUTA_CSV,
    RUTA_META,
    RUTA_PKL,
    verificar_entorno,
    verificar_pasos_react,
)


def main() -> None:
    section("Lab 6 — artefactos")
    for path in (RUTA_PKL, RUTA_META, ROOT / "data" / "archive.zip"):
        if not check_file(path):
            raise SystemExit(1)

    prep = ROOT / "_preparar_datos.py"
    if not RUTA_CSV.is_file() and prep.is_file():
        import subprocess

        subprocess.run([sys.executable, str(prep)], check=False)
    if not check_file(RUTA_CSV):
        raise SystemExit(1)

    meta = json.loads(RUTA_META.read_text(encoding="utf-8"))
    n_filas = len(pd.read_csv(RUTA_CSV))
    section("Lab 6 — verificadores")
    assert_all_pass(
        run_quiet(
            lambda: verificar_entorno(
                ollama_ok=False,
                pkl_ok=RUTA_PKL.is_file(),
                n_filas=n_filas,
                tipo_modelo=meta.get("tipo", "?"),
            )
        ),
        "entorno",
    )
    assert_all_pass(
        run_quiet(
            lambda: verificar_pasos_react(
                [
                    "Pensar y planificar",
                    "Observar telemetría",
                    "Actuar con herramientas",
                    "Responder al ingeniero",
                ]
            )
        ),
        "react",
    )
    if n_filas != N_FILAS_CSV_REF:
        print(f"⚠️  CSV con {n_filas} filas (referencia {N_FILAS_CSV_REF})")
    print("\n✅ Lab 6 smoke OK (Ollama no requerido)")


if __name__ == "__main__":
    main()
