#!/usr/bin/env bash
# PyTorch CUDA para entrenar modelos docente Lab 3 (local con GPU).
# Codespaces / alumnos siguen con _install_torch_cpu.sh
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${LABS_DIR}/.venv/bin/python"
CUDA_INDEX="https://download.pytorch.org/whl/cu124"

if [[ ! -x "$PY" ]]; then
  echo "❌ Ejecuta primero: bash labs/setup.sh"
  exit 1
fi

if command -v uv >/dev/null 2>&1; then
  PIP=(uv pip install --python "$PY")
else
  PIP=("$PY" -m pip install)
fi

echo "→ Instalando torch + torchvision (CUDA 12.4) para entrenamiento local…"
"${PIP[@]}" torch torchvision --index-url "${CUDA_INDEX}" --reinstall

echo "→ Verificando GPU…"
"$PY" -c "
import torch
print('torch', torch.__version__, '| cuda', torch.version.cuda)
assert torch.cuda.is_available(), 'CUDA no disponible — revisa drivers / WSL'
print('GPU:', torch.cuda.get_device_name(0))
"

echo "✅ Listo. Entrena con:"
echo "   python labs/lab3/_generar_modelos.py --device cuda"
