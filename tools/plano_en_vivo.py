"""Serve the Lab 6 harness board and light it from the Claude Code session.

Reads the newest labs/lab6 transcript under %USERPROFILE%\\.claude\\projects
and exposes it at /api/vivo. The board polls that address.
"""

from __future__ import annotations

import json
import re
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "labs" / "lab6" / "demo.html"
PORT = 8765

ROLES = {
    "experto-modelo": ("exp", "ficha"),
    "analista-etabs": ("ana", "json"),
    "consultor-normativo": ("con", "cita"),
    "redactor-informe": ("red", "excel"),
    "revisor-independiente": ("rev", "veredicto"),
}
NAMES = {
    "exp": "experto-modelo",
    "ana": "analista-etabs",
    "con": "consultor-normativo",
    "red": "redactor-informe",
    "rev": "revisor-independiente",
}

_cache: dict = {"key": None, "payload": None}


def clip(text: str, limit: int = 360) -> str:
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def newest_session() -> Path | None:
    root = Path.home() / ".claude" / "projects"
    if not root.is_dir():
        return None
    found: list[Path] = []
    for folder in root.iterdir():
        if "lab6" not in folder.name.lower():
            continue
        found.extend(path for path in folder.glob("*.jsonl") if path.is_file())
    if not found:
        return None
    return max(found, key=lambda path: path.stat().st_mtime)


def text_blocks(content) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text") or "")
    return "\n".join(parts)


def is_human(obj: dict) -> bool:
    if obj.get("type") != "user" or obj.get("isSidechain"):
        return False
    content = (obj.get("message") or {}).get("content")
    if isinstance(content, list):
        if any(isinstance(block, dict) and block.get("type") == "tool_result" for block in content):
            return False
        text = text_blocks(content).strip()
    elif isinstance(content, str):
        text = content.strip()
    else:
        return False
    if not text or text.startswith("<"):
        return False
    origin = (obj.get("origin") or {}).get("kind")
    return origin == "human" or obj.get("promptSource") == "typed"


def step(title: str, say: str, talk: list[str], wires: list[str], hub: str, artifact: str | None = None, halt: bool = False) -> dict:
    item = {"title": title, "say": clip(say), "talk": talk, "wires": wires, "hub": hub}
    if artifact:
        item["artifact"] = artifact
    if halt:
        item["halt"] = True
    return item


def parse(path: Path) -> dict:
    steps = []
    calls: dict[str, str] = {}
    called: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("isSidechain"):
                continue
            if is_human(obj):
                say = text_blocks((obj.get("message") or {}).get("content"))
                steps.append(step(
                    "Tú → orquestador",
                    say,
                    ["tu", "orq"],
                    ["tu"],
                    "Mensaje de la sesión.",
                ))
                continue
            message = obj.get("message") or {}
            content = message.get("content")
            if obj.get("type") == "user" and isinstance(content, str) and content.lstrip().startswith("<task-notification"):
                tool_id = ""
                match = re.search(r"<tool-use-id>(.*?)</tool-use-id>", content)
                if match:
                    tool_id = match.group(1).strip()
                role = calls.get(tool_id)
                result = ""
                result_match = re.search(r"<result>(.*)</result>", content, re.S)
                if result_match:
                    result = result_match.group(1)
                summary = ""
                summary_match = re.search(r"<summary>(.*?)</summary>", content)
                if summary_match:
                    summary = summary_match.group(1)
                say = result or summary or "El subagente terminó."
                if role:
                    artifact = next((item[1] for item in ROLES.values() if item[0] == role), None)
                    steps.append(step(
                        f"{NAMES.get(role, role)} respondió",
                        say,
                        [role, "orq"],
                        [role],
                        "Respuesta de vuelta al orquestador.",
                        artifact,
                    ))
                continue
            if message.get("role") != "assistant" or not isinstance(content, list):
                continue
            agents = []
            execute = False
            texts = []
            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "text" and (block.get("text") or "").strip():
                    texts.append(block["text"])
                if block.get("type") != "tool_use":
                    continue
                name = block.get("name") or ""
                if name == "Agent":
                    kind = (block.get("input") or {}).get("subagent_type") or ""
                    if kind in ROLES:
                        agents.append((block.get("id") or "", kind, (block.get("input") or {}).get("description") or kind))
                elif name == "mcp__etabs__execute_code":
                    execute = True
            if agents:
                ids = []
                for tool_id, kind, _desc in agents:
                    role = ROLES[kind][0]
                    ids.append(role)
                    called.add(role)
                    if tool_id:
                        calls[tool_id] = role
                unique = list(dict.fromkeys(ids))
                if len(unique) == 1:
                    title = f"Orquestador → {NAMES[unique[0]]}"
                    hub = "Una llamada."
                else:
                    title = "Mismo turno"
                    hub = "Más de un rol en el mismo mensaje."
                say = " · ".join(desc for _id, _kind, desc in agents)
                steps.append(step(title, say, ["orq", *unique], unique, hub))
            elif execute:
                steps.append(step(
                    "Orquestador pidió execute_code",
                    "La llamada salió del orquestador. Ese rol no tiene herramientas de ETABS.",
                    ["orq"],
                    [],
                    "Revisa quién pidió el código.",
                ))
            elif texts:
                say = "\n".join(texts)
                low = say.lower()
                halt = ("detengo" in low or "0.75r" in low) and "ana" not in called
                steps.append(step(
                    "Orquestador",
                    say,
                    ["orq", "tu"],
                    ["tu"],
                    "El orquestador habla contigo.",
                    halt=halt,
                ))
    if not steps:
        steps.append(step(
            "En vivo",
            "La sesión existe y todavía no tiene un mensaje del ingeniero.",
            [],
            [],
            "Esperando.",
        ))
    return {
        "ok": True,
        "session": path.stem,
        "blurb": f"En vivo · sesión {path.stem[:8]} de Claude Code en labs/lab6.",
        "steps": steps,
    }


def snapshot() -> dict:
    path = newest_session()
    if path is None:
        return {
            "ok": True,
            "session": "",
            "blurb": "No hay una sesión de Claude Code en labs/lab6.",
            "steps": [step("En vivo", "Abre claude en labs\\lab6 y el tablero se enciende con esa sesión.", [], [], "Sin sesión.")],
        }
    stat = path.stat()
    key = (str(path), stat.st_mtime_ns, stat.st_size)
    if _cache["key"] == key:
        return _cache["payload"]
    payload = parse(path)
    _cache["key"] = key
    _cache["payload"] = payload
    return payload


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/vivo":
            body = json.dumps(snapshot(), ensure_ascii=False).encode("utf-8")
            self._send(200, "application/json; charset=utf-8", body)
            return
        if path in ("/", "/demo.html"):
            self._send(200, "text/html; charset=utf-8", DEMO.read_bytes())
            return
        self.send_error(404)

    def _send(self, status: int, content_type: str, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    if "--once" in sys.argv:
        json.dump(snapshot(), sys.stdout, ensure_ascii=False, indent=2)
        print()
        return
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/demo.html?vivo=1"
    print(url, flush=True)
    webbrowser.open(url)
    server.serve_forever()


if __name__ == "__main__":
    main()
