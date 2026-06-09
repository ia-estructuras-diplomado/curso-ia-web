#!/usr/bin/env bash
# Stack PyTorch CPU compartido por labs/lab4 (CNN + LSTM) y labs/lab5 (embeddings).
# Llamar SIEMPRE al final de setup.sh, después de sentence-transformers.
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${LABS_DIR}/.venv/bin/python"
TORCH_CPU_INDEX="https://download.pytorch.org/whl/cpu"
TORCH_CPU_VERSION="2.5.1"
TORCHVISION_CPU_VERSION="0.20.1"

if [[ ! -x "$PY" ]]; then
  echo "❌ No existe labs/.venv — ejecuta primero: bash labs/setup.sh"
  exit 1
fi

PY_MINOR="$("$PY" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if [[ "$PY_MINOR" == "3.13" ]]; then
  echo "❌ labs/.venv usa Python ${PY_MINOR}; torchvision ${TORCHVISION_CPU_VERSION} no tiene wheels cp313."
  echo "   Recrea el entorno compartido:"
  echo "     rm -rf labs/.venv && bash labs/setup.sh"
  exit 1
fi

if command -v uv >/dev/null 2>&1; then
  PIP=(uv pip install --python "$PY")
else
  PIP=("$PY" -m pip install)
fi

echo "→ Stack PyTorch CPU compartido (Labs 4–5): torch==${TORCH_CPU_VERSION} + torchvision==${TORCHVISION_CPU_VERSION}"
"${PIP[@]}" \
  "torch==${TORCH_CPU_VERSION}" \
  "torchvision==${TORCHVISION_CPU_VERSION}" \
  --index-url "${TORCH_CPU_INDEX}" \
  --force-reinstall

echo "→ Verificando imports compartidos…"
"$PY" -c "
import torch
import torchvision
from sentence_transformers import SentenceTransformer
assert hasattr(torch, 'SymInt'), 'torch sin SymInt — revisa el venv'
print('✅ torch', torch.__version__, '| torchvision', torchvision.__version__, '| sentence-transformers OK')
"
