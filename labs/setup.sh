#!/usr/bin/env bash
# Entorno virtual centralizado para todos los labs (lab0, lab1, …)
#
# Uso:
#   bash labs/setup.sh              # core + datos + kernel (sin Ollama)
#   bash labs/setup.sh --with-ollama
#   LABS_SETUP_OLLAMA=1 bash labs/setup.sh
#   bash labs/setup.sh --only core|data|torch|kernel|ollama
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_setup_lib.sh
source "${LABS_DIR}/_setup_lib.sh"
cd "$LABS_DIR"

WITH_OLLAMA=0
ONLY=""

usage() {
  cat <<'EOF'
Uso: bash labs/setup.sh [opciones]

Opciones:
  --with-ollama     Instala Ollama y descarga llama3.2:3b (Labs 5–6; puede tardar)
  --only PASO       Ejecuta solo: core | data | torch | kernel | ollama
  -h, --help        Esta ayuda

Variables de entorno:
  LABS_SETUP_OLLAMA=1   Equivalente a --with-ollama

Por defecto en Codespaces (LABS_SETUP_SKIP_OLLAMA=1) Ollama no bloquea el build.
Después: bash labs/lab5/_ollama_setup.sh
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-ollama) WITH_OLLAMA=1; shift ;;
    --only)
      ONLY="${2:-}"
      [[ -n "$ONLY" ]] || { echo "❌ --only requiere un paso"; exit 1; }
      shift 2
      ;;
    -h|--help) usage; exit 0 ;;
    *) echo "❌ Opción desconocida: $1"; usage; exit 1 ;;
  esac
done

if [[ "${LABS_SETUP_OLLAMA:-0}" == "1" ]]; then
  WITH_OLLAMA=1
fi
if [[ "${LABS_SETUP_SKIP_OLLAMA:-0}" == "1" ]]; then
  WITH_OLLAMA=0
fi

if [[ ! -f requirements.txt ]]; then
  echo "❌ No se encontró labs/requirements.txt"
  exit 1
fi

setup_core() {
  _run_step "Core — Python y dependencias base" true
  _ensure_uv
  PYTHON="$(_pick_python)"
  echo "→ Python del venv compartido: $PYTHON"

  if [[ -d .venv ]]; then
    VENV_MINOR="$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "?")"
    if [[ "$VENV_MINOR" == "3.13" ]]; then
      echo "⚠️  labs/.venv usa Python 3.13 (incompatible con torchvision del curso)."
      echo "   Recreando .venv con $PYTHON…"
      rm -rf .venv
    fi
  fi

  if command -v uv >/dev/null 2>&1; then
    echo "→ Entorno con uv en labs/.venv"
    [[ -d .venv ]] || uv venv .venv --python "$PYTHON"
    echo "→ Dependencias base (requirements.txt)…"
    uv pip install -r requirements.txt
    echo "→ Lab 5: sentence-transformers (antes del pin de torch CPU)…"
    uv pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
  else
    echo "→ uv no encontrado; usando $PYTHON -m venv"
    [[ -d .venv ]] || "$PYTHON" -m venv .venv
    .venv/bin/pip install --upgrade pip
    echo "→ Dependencias base (requirements.txt)…"
    .venv/bin/pip install -r requirements.txt
    echo "→ Lab 5: sentence-transformers (antes del pin de torch CPU)…"
    .venv/bin/pip install 'sentence-transformers>=3.0.0,<4.0.0' 'transformers>=4.41.0,<4.48.0'
  fi
}

setup_torch() {
  bash "${LABS_DIR}/_install_torch_cpu.sh"
}

setup_data() {
  _run_step "Datos — preparación por lab" true
  "${LABS_DIR}/.venv/bin/python" "${LABS_DIR}/_prepare_all_data.py" || true
}

setup_kernel() {
  _run_step "Jupyter — kernel curso-ia-labs" true
  .venv/bin/python -m ipykernel install \
    --name curso-ia-labs \
    --display-name "Python (curso-ia labs)" \
    --prefix="${LABS_DIR}/.venv"
  .venv/bin/python -m ipykernel install \
    --user \
    --name curso-ia-labs \
    --display-name "Python (curso-ia labs)" || true

  REPO_ROOT="$(cd "${LABS_DIR}/.." && pwd)"
  ln -sfn labs/.venv "${REPO_ROOT}/.venv"
  echo "→ Enlace ${REPO_ROOT}/.venv → labs/.venv (para que el IDE detecte el entorno)"
}

setup_ollama() {
  if [[ -f lab5/_ollama_setup.sh ]]; then
    _run_step "Ollama — Labs 5 y 6 (opcional)" true
    bash lab5/_ollama_setup.sh || echo "⚠️ Ollama no listo; ejecuta después: bash labs/lab5/_ollama_setup.sh"
  fi
}

if [[ -n "$ONLY" ]]; then
  case "$ONLY" in
    core) setup_core ;;
    torch)
      [[ -x .venv/bin/python ]] || { echo "❌ Ejecuta primero: bash labs/setup.sh --only core"; exit 1; }
      setup_torch
      ;;
    data)
      [[ -x .venv/bin/python ]] || { echo "❌ Ejecuta primero: bash labs/setup.sh --only core"; exit 1; }
      setup_data
      ;;
    kernel)
      [[ -x .venv/bin/python ]] || { echo "❌ Ejecuta primero: bash labs/setup.sh --only core"; exit 1; }
      setup_kernel
      ;;
    ollama) setup_ollama ;;
    *)
      echo "❌ Paso desconocido: $ONLY (usa core|data|torch|kernel|ollama)"
      exit 1
      ;;
  esac
else
  setup_core
  setup_torch
  setup_data
  setup_kernel
  if [[ "$WITH_OLLAMA" == "1" ]]; then
    setup_ollama
  else
    echo ""
    echo "ℹ️  Ollama omitido (rápido para Codespaces). Labs 5–6:"
    echo "   bash labs/lab5/_ollama_setup.sh"
  fi
fi

echo ""
echo "✅ Entorno centralizado listo (un solo labs/.venv para todos los labs)."
echo "   Activar:  source labs/.venv/bin/activate"
echo "   Kernel:   Python (curso-ia labs)"
echo "   Diagnóstico: bash labs/doctor.sh"
