#!/usr/bin/env bash
# Repara PyTorch + sentence-transformers en Codespaces (SymInt / import errors)
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$LABS_DIR"
PY="${LABS_DIR}/.venv/bin/python"
TORCH_INDEX="https://download.pytorch.org/whl/cpu"
TORCH_VER="2.5.1"

if [[ ! -x "$PY" ]]; then
  echo "❌ No existe labs/.venv — ejecuta primero: bash labs/setup.sh"
  exit 1
fi

if command -v uv >/dev/null 2>&1; then
  PIP=(uv pip install --python "$PY")
else
  PIP=("$PY" -m pip install)
fi

echo "→ sentence-transformers y transformers…"
"${PIP[@]}" 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
echo "→ PyTorch CPU ${TORCH_VER} (al final — evita que ST sobrescriba con CUDA)…"
"${PIP[@]}" "torch==${TORCH_VER}" --index-url "${TORCH_INDEX}" --force-reinstall

echo "→ Verificando import…"
"$PY" -c "
import torch
from sentence_transformers import SentenceTransformer
assert hasattr(torch, 'SymInt'), 'torch sin SymInt — revisa el venv'
print('✅ PyTorch', torch.__version__, '| sentence-transformers OK')
"

echo ""
echo "Reinicia el kernel de Jupyter y vuelve a ejecutar las celdas."
