#!/usr/bin/env bash
# Entorno virtual centralizado para todos los labs (lab0, lab1, …)
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LABS_DIR"

if [[ ! -f requirements.txt ]]; then
  echo "❌ No se encontró labs/requirements.txt"
  exit 1
fi

if ! command -v uv >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  echo "→ Instalando uv (instalador oficial de astral.sh)"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="${HOME}/.local/bin:${PATH}"
fi

if command -v uv >/dev/null 2>&1; then
  echo "→ Entorno con uv en labs/.venv"
  if [[ ! -d .venv ]]; then
    uv venv .venv
  fi
  echo "→ PyTorch CPU (Lab 5 / sentence-transformers)…"
  uv pip install torch --index-url https://download.pytorch.org/whl/cpu
  uv pip install -r requirements.txt
else
  echo "→ uv no encontrado; usando python -m venv"
  if [[ ! -d .venv ]]; then
    python3 -m venv .venv
  fi
  .venv/bin/pip install --upgrade pip
  echo "→ PyTorch CPU (Lab 5 / sentence-transformers)…"
  .venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
  .venv/bin/pip install -r requirements.txt
fi

if [[ -f lab2/_preparar_datos.py ]] && [[ ! -f lab2/data/concrete.csv ]]; then
  echo "→ Generando lab2/data/concrete.csv"
  .venv/bin/python lab2/_preparar_datos.py
fi

if [[ -f lab5/_ollama_setup.sh ]]; then
  echo "→ Lab 5: configurando Ollama (opcional, puede tardar)…"
  bash lab5/_ollama_setup.sh || echo "⚠️ Ollama no listo; ejecuta después: bash labs/lab5/_ollama_setup.sh"
fi

echo ""
echo "✅ Entorno centralizado listo."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Jupyter:  cd labs/labN && jupyter notebook *_alumno.ipynb"
