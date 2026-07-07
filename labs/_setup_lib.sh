#!/usr/bin/env bash
# Funciones compartidas para labs/setup.sh y labs/doctor.sh
set -euo pipefail

labs_setup_root() {
  cd "$(dirname "${BASH_SOURCE[0]}")"
}

_pick_python() {
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
  return 1
}

_ensure_uv() {
  if command -v uv >/dev/null 2>&1; then
    return 0
  fi
  if ! command -v curl >/dev/null 2>&1; then
    echo "❌ curl no disponible para instalar uv" >&2
    return 1
  fi
  echo "→ Instalando uv (instalador oficial de astral.sh)"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="${HOME}/.local/bin:${PATH}"
}

_pip_cmd() {
  local py="${LABS_DIR}/.venv/bin/python"
  if command -v uv >/dev/null 2>&1; then
    echo "uv pip install --python ${py}"
  else
    echo "${py} -m pip install"
  fi
}

_run_step() {
  local label="$1"
  shift
  echo ""
  echo "━━━ ${label} ━━━"
  "$@"
}

_prepare_lab_data() {
  local script="$1"
  local label="$2"
  if [[ ! -f "$script" ]]; then
    echo "⚠️  ${label}: no existe ${script}"
    return 0
  fi
  echo "→ ${label}"
  if "${LABS_DIR}/.venv/bin/python" "$script"; then
    return 0
  fi
  echo "⚠️  ${label}: falló (revisa datos en data/; el resto del entorno sigue usable)"
  return 0
}
