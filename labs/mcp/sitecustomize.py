"""Loaded automatically when this folder is on PYTHONPATH.

knowledge-rag prints status lines with print(). After startup it points
stdout back at the MCP client, so the BM25 log is written into the JSON-RPC
stream and the client disconnects. Sending every print() to stderr keeps
that stream JSON-only.

A relative KNOWLEDGE_RAG_DIR is resolved once, here, before the server reads
it. Resolved again later it pointed at an empty index.
"""

from __future__ import annotations

import builtins
import os
import sys
from pathlib import Path

_raw = os.environ.get("KNOWLEDGE_RAG_DIR")
if _raw:
    _path = Path(_raw).expanduser()
    if not _path.is_absolute():
        _path = Path.cwd() / _path
    os.environ["KNOWLEDGE_RAG_DIR"] = str(_path.resolve())

_print = builtins.print


def _print_to_stderr(*args, **kwargs):
    if kwargs.get("file", None) is None or kwargs.get("file") is sys.stdout:
        kwargs["file"] = sys.stderr
    _print(*args, **kwargs)


builtins.print = _print_to_stderr
