"""Prepara datasets de todos los labs (Codespaces / local).

Cada lab se intenta de forma independiente: un fallo no bloquea los demás.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

LABS = Path(__file__).resolve().parent

STEPS: list[tuple[str, Path]] = [
    ("Lab 2 — concrete.csv", LABS / "lab2" / "_preparar_datos.py"),
    ("Lab 4 P1 — cracks_subset", LABS / "lab4" / "part_1" / "_preparar_datos.py"),
    ("Lab 4 P2 — SHM CSV", LABS / "lab4" / "part_2" / "_preparar_datos.py"),
    ("Lab 6 — seismic_data.csv", LABS / "lab6" / "_preparar_datos.py"),
]


def _run_step(label: str, script: Path) -> bool:
    if not script.is_file():
        print(f"⚠️  {label}: no existe {script}")
        return False
    spec = importlib.util.spec_from_file_location(f"prep_{script.parent.name}", script)
    if spec is None or spec.loader is None:
        print(f"❌ {label}: no se pudo cargar {script}")
        return False
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        if hasattr(module, "main"):
            module.main()
        print(f"✅ {label}")
        return True
    except Exception as exc:
        print(f"⚠️  {label}: {exc}")
        return False


def main() -> int:
    ok = 0
    for label, script in STEPS:
        if _run_step(label, script):
            ok += 1
    print(f"\n→ Datos listos: {ok}/{len(STEPS)} pasos")
    return 0 if ok == len(STEPS) else 1


if __name__ == "__main__":
    sys.exit(main())
