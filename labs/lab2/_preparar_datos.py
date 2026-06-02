"""Convierte Concrete_Data.xls (UCI) a concrete.csv con columnas en español."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

DIR = Path(__file__).parent / "data"
XLS = DIR / "Concrete_Data.xls"
CSV = DIR / "concrete.csv"

COLUMNAS = [
    "Cemento",
    "Escoria",
    "CenizaVolante",
    "Agua",
    "Superplastificante",
    "AgregadoGrueso",
    "AgregadoFino",
    "Edad",
    "Resistencia",
]


def main() -> None:
    if not XLS.exists():
        raise FileNotFoundError(f"No se encontró {XLS}")

    df = pd.read_excel(XLS, header=0)
    if df.shape != (1030, 9):
        raise ValueError(f"Forma inesperada: {df.shape}, se esperaba (1030, 9)")

    # Asegurar tipos numéricos (por si el Excel trae strings)
    df = df.apply(pd.to_numeric, errors="coerce")

    df.columns = COLUMNAS
    df.to_csv(CSV, index=False)
    print(f"✅ Escrito {CSV} ({len(df)} filas × {len(COLUMNAS)} columnas)")


if __name__ == "__main__":
    main()
