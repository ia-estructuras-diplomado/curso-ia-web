"""Extrae seismic_data.csv desde data/archive.zip (Lab 6)."""
from __future__ import annotations

import zipfile
from pathlib import Path

DIR = Path(__file__).parent
DATA = DIR / "data"
ZIP = DATA / "archive.zip"
CSV = DATA / "seismic_data.csv"
CSV_NAME_IN_ZIP = "seismic_data.csv"


def main() -> None:
    if CSV.is_file():
        print(f"✅ {CSV} ya existe ({CSV.stat().st_size // 1024} KB).")
        return
    if not ZIP.is_file():
        raise FileNotFoundError(f"No se encontró {ZIP}.")
    with zipfile.ZipFile(ZIP, "r") as zf:
        names = [n for n in zf.namelist() if n.endswith(".csv")]
        if not names:
            raise ValueError("archive.zip no contiene ningún CSV.")
        member = CSV_NAME_IN_ZIP if CSV_NAME_IN_ZIP in names else names[0]
        DATA.mkdir(parents=True, exist_ok=True)
        zf.extract(member, DATA)
        extracted = DATA / member
        if extracted != CSV:
            extracted.rename(CSV)
    print(f"✅ Escrito {CSV}")


if __name__ == "__main__":
    main()
