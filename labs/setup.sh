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

TORCH_CPU_INDEX="https://download.pytorch.org/whl/cpu"
TORCH_CPU_VERSION="2.5.1"

if command -v uv >/dev/null 2>&1; then
  echo "→ Entorno con uv en labs/.venv"
  if [[ ! -d .venv ]]; then
    uv venv .venv
  fi
  echo "→ Dependencias base (requirements.txt)…"
  uv pip install -r requirements.txt
  echo "→ Lab 5: sentence-transformers…"
  uv pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
  echo "→ PyTorch CPU ${TORCH_CPU_VERSION} (último paso — evita SymInt / wheels CUDA)…"
  uv pip install "torch==${TORCH_CPU_VERSION}" --index-url "${TORCH_CPU_INDEX}" --force-reinstall
else
  echo "→ uv no encontrado; usando python -m venv"
  if [[ ! -d .venv ]]; then
    python3 -m venv .venv
  fi
  .venv/bin/pip install --upgrade pip
  echo "→ Dependencias base (requirements.txt)…"
  .venv/bin/pip install -r requirements.txt
  echo "→ Lab 5: sentence-transformers…"
  .venv/bin/pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
  echo "→ PyTorch CPU ${TORCH_CPU_VERSION} (último paso)…"
  .venv/bin/pip install "torch==${TORCH_CPU_VERSION}" --index-url "${TORCH_CPU_INDEX}" --force-reinstall
fi

echo "→ Verificando torch + sentence-transformers…"
if .venv/bin/python -c "import torch; from sentence_transformers import SentenceTransformer; assert hasattr(torch,'SymInt')" 2>/dev/null; then
  echo "   ✅ PyTorch OK para Lab 5"
else
  echo "   ⚠️ PyTorch/sentence-transformers falló — ejecuta: bash labs/lab5/_fix_pytorch.sh"
fi

if [[ -f lab2/_preparar_datos.py ]] && [[ ! -f lab2/data/concrete.csv ]]; then
  echo "→ Generando lab2/data/concrete.csv"
  .venv/bin/python lab2/_preparar_datos.py
fi

if [[ -f lab4/_preparar_datos.py ]] && [[ ! -d lab4/data/cracks_subset/train ]]; then
  echo "→ Preparando lab4/data/cracks_subset (desde zip o RAR local)"
  .venv/bin/python lab4/_preparar_datos.py
fi

if [[ -f lab5/_ollama_setup.sh ]]; then
  echo "→ Lab 5: configurando Ollama (opcional, puede tardar)…"
  bash lab5/_ollama_setup.sh || echo "⚠️ Ollama no listo; ejecuta después: bash labs/lab5/_ollama_setup.sh"
fi

echo ""
echo "✅ Entorno centralizado listo."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Jupyter:  cd labs/labN && jupyter notebook *_alumno.ipynb"
