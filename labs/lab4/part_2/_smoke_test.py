#!/usr/bin/env python3
"""Smoke test docente — Lab 4 Parte 2 (xAI redes + modelos Lab 3)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent.parent))
from _smoke_common import assert_all_pass, check_file, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

from _verificar import (  # noqa: E402
    RUTA_CNN,
    RUTA_LSTM,
    verificar_modelos_lab3,
    verificar_panorama_xai_redes,
)


def main() -> None:
    section("Lab 4 P2 xAI redes — modelos Lab 3")
    check_file(RUTA_CNN)
    check_file(RUTA_LSTM)
    tecnicas = ["grad_cam", "integrated_gradients", "comparacion"]
    assert_all_pass(run_quiet(lambda: verificar_panorama_xai_redes(tecnicas)), "panorama")
    assert_all_pass(run_quiet(lambda: verificar_modelos_lab3(True, True)), "modelos")
    print("\n✅ Lab 4 Parte 2 (xAI redes) smoke OK")


if __name__ == "__main__":
    main()
