"""Start the ETABS MCP server installed by Lab 6.

The executable always lives at %USERPROFILE%\\etabs-mcp\\etabs-mcp.exe.
This process stays in front of it and passes through stdin and stdout.
On Windows, os.execv closes those pipes and Claude Code times out.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    exe = Path.home() / "etabs-mcp" / "etabs-mcp.exe"
    if not exe.is_file():
        print(
            f"ETABS MCP no está en {exe}. "
            "Descárgalo como indica la Parte 0 del Lab 6 y vuelve a abrir Claude Code.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    raise SystemExit(subprocess.call([str(exe)]))


if __name__ == "__main__":
    main()
