"""Arranca el servidor del tablero (plano_en_vivo.py) si no está corriendo ya.

Pensado para un hook SessionStart de Claude Code: no bloquea, no duplica
el proceso si el puerto 8765 ya responde.
"""

from __future__ import annotations

import socket
import subprocess
import sys
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8765
ROOT = Path(__file__).resolve().parents[4]  # .../curso-ia-web
SCRIPT = ROOT / "tools" / "plano_en_vivo.py"


def ya_corriendo() -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.3)
        try:
            sock.connect((HOST, PORT))
            return True
        except OSError:
            return False


def main() -> None:
    if ya_corriendo():
        print(f"Tablero ya activo en http://{HOST}:{PORT}/demo.html?vivo=1")
        return
    if not SCRIPT.is_file():
        print(f"No encontré {SCRIPT}, no arranco el tablero.")
        return
    flags = 0
    if sys.platform == "win32":
        flags = subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
    subprocess.Popen(
        [sys.executable, str(SCRIPT)],
        cwd=str(SCRIPT.parent),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=flags,
        close_fds=True,
    )
    print(f"Tablero arrancado en http://{HOST}:{PORT}/demo.html?vivo=1")


if __name__ == "__main__":
    main()
