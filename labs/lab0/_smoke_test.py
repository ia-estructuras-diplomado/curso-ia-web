#!/usr/bin/env python3
"""Smoke test docente — Lab 0 (valores canónicos de solucion_ia)."""
from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from _smoke_common import assert_all_pass, ensure_lab_path, run_quiet, section

ensure_lab_path(ROOT)

import pandas as pd  # noqa: E402

from _verificar import (  # noqa: E402
    resumen_seccion,
    verificar_diccionario,
    verificar_imports,
    verificar_listas,
    verificar_paquetes,
    verificar_pandas,
    verificar_precios,
    verificar_riesgo,
    verificar_sintaxis,
)

edades_clientes = [25, 34, 45, 28, 52]
perfil_usuario = {"nombre": "Ana", "edad": 34, "activo": True}
precios = [100, 250, 45, 800, 120]


def main() -> None:
    section("Lab 0 — verificadores canónicos")
    assert_all_pass(
        run_quiet(lambda: verificar_sintaxis(24, "Mi-Primer-ML", 2)),
        "sintaxis",
    )
    assert_all_pass(
        run_quiet(lambda: verificar_imports(math.sqrt(25), 25)),
        "imports",
    )
    assert_all_pass(
        run_quiet(lambda: verificar_paquetes(pd.__version__, 2.0, pd)),
        "paquetes",
    )
    assert_all_pass(
        run_quiet(lambda: verificar_listas(edades_clientes, 2, 45)),
        "listas",
    )
    perfil = dict(perfil_usuario)
    perfil["ciudad"] = "Bogotá"
    assert_all_pass(
        run_quiet(lambda: verificar_diccionario(perfil, "Bogotá")),
        "diccionario",
    )
    umbral = 100
    precios_resultado = [p * 0.9 if p > umbral else p for p in precios]
    assert_all_pass(
        run_quiet(lambda: verificar_precios(precios_resultado, umbral)),
        "precios",
    )

    def predecir_riesgo(edad: int, ingresos: float) -> str:
        if ingresos > 50000 and edad > 25:
            return "Riesgo Bajo"
        if ingresos < 20000:
            return "Riesgo Alto"
        return "Riesgo Medio"

    resultado = predecir_riesgo(perfil["edad"], 60_000)
    assert_all_pass(
        run_quiet(lambda: verificar_riesgo(resultado, 60_000, "Riesgo Bajo")),
        "riesgo",
    )
    data = {
        "ID": [1, 2, 3, 4],
        "Edad": [25, 30, 35, 40],
        "Salario": [50000, 60000, 75000, 90000],
        "Compro": [0, 0, 1, 1],
    }
    df = pd.DataFrame(data)
    umbral_salario = 55_000
    filtro = df[df["Salario"] > umbral_salario]
    assert_all_pass(
        run_quiet(
            lambda: verificar_pandas(
                df, filtro, int(filtro["Compro"].sum()), umbral_salario
            )
        ),
        "pandas",
    )
    resumen_seccion("smoke", [True])
    print("\n✅ Lab 0 smoke OK")


if __name__ == "__main__":
    main()
