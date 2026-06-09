#!/usr/bin/env bash
# Entorno virtual centralizado para todos los labs (lab0, lab1, …)
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LABS_DIR"

if [[ ! -f requirements.txt ]]; then
  echo "❌ No se encontró labs/requirements.txt"
  exit 1
fi

_pick_python() {
  # 3.11 = Codespaces; 3.12 también tiene wheels torch/torchvision CPU.
  # Evitar 3.13: torchvision 0.20.x no publica cp313 en el índice CPU.
  for cmd in python3.11 python3.12; do
    if command -v "$cmd" >/dev/null 2>&1; then
      echo "$cmd"
      return 0
    fi
  done
  if command -v python3 >/dev/null 2>&1; then
    echo "python3"
    return 0
  fi
  echo "❌ No se encontró python3.11, python3.12 ni python3" >&2
  exit 1
}

if ! command -v uv >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  echo "→ Instalando uv (instalador oficial de astral.sh)"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="${HOME}/.local/bin:${PATH}"
fi

PYTHON="$(_pick_python)"
echo "→ Python del venv compartido: $PYTHON"

if [[ -d .venv ]]; then
  VENV_MINOR="$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "?")"
  if [[ "$VENV_MINOR" == "3.13" ]]; then
    echo "⚠️  labs/.venv actual usa Python 3.13 (incompatible con torchvision del curso)."
    echo "   Recreando .venv con $PYTHON…"
    rm -rf .venv
  fi
fi

if command -v uv >/dev/null 2>&1; then
  echo "→ Entorno con uv en labs/.venv"
  if [[ ! -d .venv ]]; then
    uv venv .venv --python "$PYTHON"
  fi
  echo "→ Dependencias base (requirements.txt)…"
  uv pip install -r requirements.txt
  echo "→ Lab 5: sentence-transformers (antes del pin de torch CPU)…"
  uv pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
else
  echo "→ uv no encontrado; usando $PYTHON -m venv"
  if [[ ! -d .venv ]]; then
    "$PYTHON" -m venv .venv
  fi
  .venv/bin/pip install --upgrade pip
  echo "→ Dependencias base (requirements.txt)…"
  .venv/bin/pip install -r requirements.txt
  echo "→ Lab 5: sentence-transformers (antes del pin de torch CPU)…"
  .venv/bin/pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
fi

# torch + torchvision CPU al final (compartido Lab 4 y Lab 5)
bash "${LABS_DIR}/_install_torch_cpu.sh"

if [[ -f lab2/_preparar_datos.py ]] && [[ ! -f lab2/data/concrete.csv ]]; then
  echo "→ Generando lab2/data/concrete.csv"
  .venv/bin/python lab2/_preparar_datos.py
fi

if [[ -f lab4/_preparar_datos.py ]] && [[ ! -d lab4/data/cracks_subset/train ]]; then
  echo "→ Preparando lab4/data/cracks_subset (desde zip o RAR local)"
  .venv/bin/python lab4/_preparar_datos.py
fi

if [[ -f lab4/part_2/_preparar_datos.py ]] && [[ ! -f lab4/part_2/data/building_health_monitoring_dataset.csv ]]; then
  echo "→ Preparando lab4/part_2/data (desde archive.zip)"
  .venv/bin/python lab4/part_2/_preparar_datos.py
fi

if [[ -f lab5/_ollama_setup.sh ]]; then
  echo "→ Lab 5: configurando Ollama (opcional, puede tardar)…"
  bash lab5/_ollama_setup.sh || echo "⚠️ Ollama no listo; ejecuta después: bash labs/lab5/_ollama_setup.sh"
fi

echo ""
echo "✅ Entorno centralizado listo (un solo labs/.venv para todos los labs)."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Jupyter:  cd labs/labN && jupyter notebook *_alumno_ia.ipynb"
