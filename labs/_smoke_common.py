"""Utilidades compartidas para smoke tests docentes (labs/*/_smoke_test.py)."""
from __future__ import annotations

import contextlib
import io
import sys
from collections.abc import Callable
from pathlib import Path


def lab_dir(name: str = "") -> Path:
    """Directorio del lab que invoca el smoke test."""
    return Path(__file__).resolve().parent / name if name else Path.cwd().resolve()


def ensure_lab_path(lab_path: Path) -> None:
    lab_str = str(lab_path)
    if lab_str not in sys.path:
        sys.path.insert(0, lab_str)


def section(title: str) -> None:
    print(f"\n▶ {title}")


def assert_all_pass(checks: list[bool], label: str) -> None:
    if not all(checks):
        raise AssertionError(f"Smoke falló: {label}")


def run_quiet(fn: Callable[[], list[bool]]) -> list[bool]:
    """Ejecuta verificadores que imprimen ✅/❌ sin contaminar el resumen."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return fn()


def check_file(path: Path, label: str | None = None) -> bool:
    ok = path.is_file()
    name = label or path.name
    print(f"{'✅' if ok else '❌'} {name}: {path}")
    return ok


def check_dir(path: Path, label: str | None = None) -> bool:
    ok = path.is_dir()
    name = label or path.name
    print(f"{'✅' if ok else '❌'} {name}: {path}")
    return ok
