"""Start the ETABS MCP server installed by Lab 6.

The executable always lives at %USERPROFILE%\\etabs-mcp\\etabs-mcp.exe.
This process replaces itself with that executable so stdin and stdout stay
attached to Claude Code.
"""

from __future__ import annotations

import os
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
    os.execv(str(exe), [str(exe)])


if __name__ == "__main__":
    main()
