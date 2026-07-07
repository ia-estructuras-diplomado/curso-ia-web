#!/usr/bin/env python3
"""Smoke test: kernel Jupyter «Python (curso-ia labs)» registrado y ejecutable.

Valida lo que el alumno debe ver en Codespaces → selector de kernel del notebook:
  - kernelspec `curso-ia-labs` con display_name «Python (curso-ia labs)»
  - intérprete apunta a `labs/.venv/bin/python`
  - el kernel ejecuta código (pandas) sin error
  - devcontainer.json declara el mismo intérprete para la extensión Python
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

LABS = Path(__file__).resolve().parent
REPO = LABS.parent
VENV_PY = LABS / ".venv" / "bin" / "python"
KERNEL_NAME = "curso-ia-labs"
DISPLAY_NAME = "Python (curso-ia labs)"
KERNEL_JSON = LABS / ".venv" / "share" / "jupyter" / "kernels" / KERNEL_NAME / "kernel.json"
DEVCONTAINER_JSON = REPO / ".devcontainer" / "devcontainer.json"


def _fail(msg: str) -> None:
    print(f"❌ {msg}")
    raise SystemExit(1)


def _ok(msg: str) -> None:
    print(f"✅ {msg}")


def _resolved(path: Path) -> Path:
    return path.resolve()


def check_venv() -> None:
    if not VENV_PY.is_file():
        _fail(f"No existe {VENV_PY} — ejecuta: bash labs/setup.sh")
    _ok(f"venv Python: {VENV_PY}")


def check_kernelspec_file() -> dict:
    if not KERNEL_JSON.is_file():
        _fail(
            f"No existe {KERNEL_JSON} — ejecuta: bash labs/setup.sh "
            "(registra ipykernel curso-ia-labs)"
        )
    meta = json.loads(KERNEL_JSON.read_text(encoding="utf-8"))
    if meta.get("display_name") != DISPLAY_NAME:
        _fail(
            f"display_name esperado «{DISPLAY_NAME}», obtuvo «{meta.get('display_name')}»"
        )
    argv = meta.get("argv") or []
    if not argv:
        _fail("kernel.json sin argv")
    kernel_py = Path(str(argv[0]))
    if _resolved(kernel_py) != _resolved(VENV_PY):
        _fail(
            f"kernel.json argv[0]={argv[0]} no coincide con {VENV_PY}"
        )
    _ok(f"kernelspec «{DISPLAY_NAME}» → {kernel_py}")
    return meta


def check_jupyter_kernelspec_list() -> None:
    env = os.environ.copy()
    env["PATH"] = f"{LABS / '.venv' / 'bin'}:{env.get('PATH', '')}"
    proc = subprocess.run(
        [str(VENV_PY), "-m", "jupyter", "kernelspec", "list"],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    if proc.returncode != 0:
        _fail(f"jupyter kernelspec list falló:\n{proc.stderr}")
    if KERNEL_NAME not in proc.stdout:
        _fail(
            f"«{KERNEL_NAME}» no aparece en jupyter kernelspec list:\n{proc.stdout}"
        )
    _ok(f"jupyter kernelspec list incluye «{KERNEL_NAME}» (UI: «{DISPLAY_NAME}»)")


def check_devcontainer_settings() -> None:
    if not DEVCONTAINER_JSON.is_file():
        print(f"⚠️  Sin {DEVCONTAINER_JSON} (omitido)")
        return
    cfg = json.loads(DEVCONTAINER_JSON.read_text(encoding="utf-8"))
    interp = (
        cfg.get("customizations", {})
        .get("vscode", {})
        .get("settings", {})
        .get("python.defaultInterpreterPath", "")
    )
    if "labs/.venv/bin/python" not in interp:
        _fail(
            "devcontainer.json debe fijar "
            "python.defaultInterpreterPath → labs/.venv/bin/python"
        )
    _ok("devcontainer.json apunta al intérprete labs/.venv")


def check_kernel_executes() -> None:
    try:
        from jupyter_client.manager import start_new_kernel
    except ImportError as exc:
        _fail(f"jupyter_client no disponible: {exc}")

    env = os.environ.copy()
    env["PATH"] = f"{LABS / '.venv' / 'bin'}:{env.get('PATH', '')}"

    km, kc = start_new_kernel(
        kernel_name=KERNEL_NAME,
        cwd=str(LABS),
        env=env,
    )
    try:
        msg_id = kc.execute("import pandas as pd; print('KERNEL_OK', pd.__version__)")
        deadline = time.time() + 60
        while time.time() < deadline:
            try:
                msg = kc.get_iopub_msg(timeout=5)
            except Exception:
                continue
            if msg.get("parent_header", {}).get("msg_id") != msg_id:
                continue
            msg_type = msg.get("msg_type")
            if msg_type == "stream" and "KERNEL_OK" in msg.get("content", {}).get("text", ""):
                _ok("kernel ejecutó import pandas correctamente")
                return
            if msg_type == "error":
                content = msg.get("content", {})
                _fail(
                    f"kernel error: {content.get('ename')}: {content.get('evalue')}"
                )
        _fail("timeout esperando ejecución en el kernel")
    finally:
        km.shutdown_kernel(now=True)


def check_nbconvert_with_kernel() -> None:
    """Ejecuta una celda mínima con --kernel curso-ia-labs (como en el IDE)."""
    out_dir = Path("/tmp/curso-ia-kernel-smoke")
    out_dir.mkdir(parents=True, exist_ok=True)
    nb = out_dir / "fixture.ipynb"
    nb.write_text(
        json.dumps(
            {
                "nbformat": 4,
                "nbformat_minor": 5,
                "metadata": {
                    "kernelspec": {
                        "display_name": DISPLAY_NAME,
                        "language": "python",
                        "name": KERNEL_NAME,
                    }
                },
                "cells": [
                    {
                        "cell_type": "code",
                        "metadata": {},
                        "source": ["import pandas as pd\n", "print('NB_OK', pd.__version__)\n"],
                        "outputs": [],
                        "execution_count": None,
                    }
                ],
            },
            indent=1,
        ),
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["PATH"] = f"{LABS / '.venv' / 'bin'}:{env.get('PATH', '')}"
    proc = subprocess.run(
        [
            str(VENV_PY),
            "-m",
            "jupyter",
            "nbconvert",
            "--execute",
            "--to",
            "notebook",
            "--kernel",
            KERNEL_NAME,
            "--ExecutePreprocessor.timeout=120",
            f"--output-dir={out_dir}",
            str(nb),
        ],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(out_dir),
        check=False,
    )
    if proc.returncode != 0:
        _fail(f"nbconvert con kernel {KERNEL_NAME} falló:\n{proc.stderr}\n{proc.stdout}")
    _ok(f"nbconvert ejecutó notebook con kernel «{KERNEL_NAME}»")


def main() -> None:
    print("━━━ Smoke kernel Jupyter (curso-ia labs) ━━━")
    check_venv()
    check_kernelspec_file()
    check_jupyter_kernelspec_list()
    check_devcontainer_settings()
    check_kernel_executes()
    check_nbconvert_with_kernel()
    print("\n✅ Kernel visible y ejecutable (equivalente a selector en Codespaces)")


if __name__ == "__main__":
    main()
