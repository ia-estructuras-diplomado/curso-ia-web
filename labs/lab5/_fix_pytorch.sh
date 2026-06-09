#!/usr/bin/env bash
# Repara el stack PyTorch CPU del venv COMPARTIDO (Labs 4 y 5).
# Delega en labs/_install_torch_cpu.sh — no instalar torch solo en lab4/ o lab5/.
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${LABS_DIR}/.venv/bin/python"

if [[ ! -x "$PY" ]]; then
  echo "❌ No existe labs/.venv — ejecuta primero: bash labs/setup.sh"
  exit 1
fi

if command -v uv >/dev/null 2>&1; then
  PIP=(uv pip install --python "$PY")
else
  PIP=("$PY" -m pip install)
fi

echo "→ sentence-transformers y transformers (Lab 5)…"
"${PIP[@]}" 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'

bash "${LABS_DIR}/_install_torch_cpu.sh"

echo ""
echo "Reinicia el kernel de Jupyter y vuelve a ejecutar las celdas."
