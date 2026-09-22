#!/usr/bin/env bash
# Entorno virtual centralizado para todos los labs (lab0, lab1, …)
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$LABS_DIR"
PYTHON_VERSION="3.12"

if [[ ! -f requirements.txt ]]; then
  echo "❌ No se encontró labs/requirements.txt"
  exit 1
fi

if ! command -v uv >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  echo "→ Instalando uv (instalador oficial de astral.sh)"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="${HOME}/.local/bin:${PATH}"
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "❌ uv no está disponible ni se pudo instalar. Instálalo manualmente: https://astral.sh/uv"
  exit 1
fi

echo "→ uv: fijando intérprete Python ${PYTHON_VERSION}"
uv python install "${PYTHON_VERSION}"

if [[ -d .venv ]]; then
  VENV_MINOR="$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "?")"
  if [[ "$VENV_MINOR" != "$PYTHON_VERSION" ]]; then
    echo "→ Recreando labs/.venv (${VENV_MINOR} → ${PYTHON_VERSION})"
    rm -rf .venv
  fi
fi
[[ -d .venv ]] || uv venv .venv --python "${PYTHON_VERSION}"

echo "→ Dependencias base (requirements.txt)…"
uv pip install --python .venv/bin/python -r requirements.txt

echo "→ Stack ML CPU compartido (Lab 4 + Lab 5)…"
bash "${LABS_DIR}/_install_torch_cpu.sh"

echo ""
echo "✅ Entorno centralizado listo (un solo labs/.venv, Python ${PYTHON_VERSION}, para todos los labs)."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Jupyter:  cd labs/labN && jupyter notebook *.ipynb"
