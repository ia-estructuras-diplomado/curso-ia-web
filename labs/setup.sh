#!/usr/bin/env bash
# Entorno virtual centralizado para todos los labs (lab0, lab1, …)
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LABS_DIR"

if [[ ! -f requirements.txt ]]; then
  echo "❌ No se encontró labs/requirements.txt"
  exit 1
fi

if command -v uv >/dev/null 2>&1; then
  echo "→ Creando entorno con uv en labs/.venv"
  uv venv .venv
  uv pip install -r requirements.txt
else
  echo "→ uv no encontrado; usando python -m venv"
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip
  .venv/bin/pip install -r requirements.txt
fi

if [[ -f lab1/_preparar_datos.py ]] && [[ ! -f lab1/data/concrete.csv ]]; then
  echo "→ Generando lab1/data/concrete.csv"
  .venv/bin/python lab1/_preparar_datos.py
fi

echo ""
echo "✅ Entorno centralizado listo."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Jupyter:  cd labs/labN && jupyter notebook *_alumno.ipynb"
