#!/usr/bin/env bash
# Stack ML CPU compartido por labs/lab4 (CNN + LSTM) y labs/lab5 (embeddings/RAG).
# Idempotente — también sirve como script de reparación: si torch/torchvision
# fallan o ves un error de SymInt, simplemente vuelve a ejecutar:
#   bash labs/_install_torch_cpu.sh
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

if command -v uv >/dev/null 2>&1; then
  PIP=(uv pip install --python "$PY")
else
  PIP=("$PY" -m pip install)
fi

echo "→ sentence-transformers / transformers (Lab 5)…"
"${PIP[@]}" 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'

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
