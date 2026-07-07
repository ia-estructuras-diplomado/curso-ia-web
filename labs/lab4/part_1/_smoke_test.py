#!/usr/bin/env python3
"""Smoke test docente — Lab 4 Parte 1 (datos + imports PyTorch, sin entrenar)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent.parent))
from _smoke_common import assert_all_pass, check_dir, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

from _verificar import CLASES_ESPERADAS, verificar_eda_dataset  # noqa: E402


def _conteos_subset(ruta: Path) -> dict:
    out: dict[str, dict[str, int]] = {}
    for split in ("train", "val"):
        out[split] = {}
        for cls in CLASES_ESPERADAS:
            out[split][cls] = len(list((ruta / split / cls).glob("*.jpg")))
    return out


def main() -> None:
    data = ROOT / "data" / "cracks_subset"
    section("Lab 4 P1 — dataset")
    if not check_dir(data / "train") or not check_dir(data / "val"):
        prep = ROOT / "_preparar_datos.py"
        if prep.is_file():
            print("→ Intentando _preparar_datos.py …")
            import subprocess

            subprocess.run([sys.executable, str(prep)], check=False)
        if not data.is_dir():
            raise SystemExit("❌ Falta data/cracks_subset — ejecuta: python _preparar_datos.py")

    section("Lab 4 P1 — PyTorch")
    import torch  # noqa: F401
    import torchvision  # noqa: F401

    print(f"✅ torch {torch.__version__} | torchvision {torchvision.__version__}")
    assert hasattr(torch, "SymInt"), "torch sin SymInt — ejecuta: bash labs/lab5/_fix_pytorch.sh"

    conteos = _conteos_subset(data)
    section("Lab 4 P1 — verificadores EDA")
    assert_all_pass(
        run_quiet(lambda: verificar_eda_dataset(conteos, 4, 40)),
        "eda",
    )
    print("\n✅ Lab 4 Parte 1 smoke OK")


if __name__ == "__main__":
    main()
