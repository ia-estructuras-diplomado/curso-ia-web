#!/usr/bin/env bash
# Diagnóstico rápido del entorno de labs (Codespaces / local).
set -euo pipefail

LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_setup_lib.sh
source "${LABS_DIR}/_setup_lib.sh"

QUIET=0
RUN_SMOKE=0
STRICT=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --quiet|-q) QUIET=1; shift ;;
    --smoke) RUN_SMOKE=1; shift ;;
    --strict) STRICT=1; shift ;;
    -h|--help)
      echo "Uso: bash labs/doctor.sh [--quiet] [--strict] [--smoke]"
      exit 0
      ;;
    *) echo "Opción desconocida: $1"; exit 1 ;;
  esac
done

_log() {
  [[ "$QUIET" == "1" ]] || echo "$@"
}

PY="${LABS_DIR}/.venv/bin/python"
FAIL=0

_check() {
  local label="$1"
  shift
  if "$@"; then
    _log "✅ ${label}"
  else
    echo "❌ ${label}"
    FAIL=1
  fi
}

_log "━━━ Diagnóstico labs ━━━"

_check "labs/.venv existe" test -x "$PY"
if [[ -x "$PY" ]]; then
  _log "   Python: $("$PY" -c 'import sys; print(sys.executable)')"
  _log "   Versión: $("$PY" -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
fi

_check "Kernel curso-ia-labs" test -f "${LABS_DIR}/.venv/share/jupyter/kernels/curso-ia-labs/kernel.json"

if [[ -x "$PY" ]]; then
  _log ""
  _log "→ Imports clave"
  for mod in pandas sklearn torch torchvision xgboost shap; do
    if "$PY" -c "import ${mod}" 2>/dev/null; then
      _log "   ✅ ${mod}"
    else
      echo "   ❌ ${mod}"
      FAIL=1
    fi
  done

  _log ""
  _log "→ Datos"
  for path in \
    "lab2/data/concrete.csv" \
    "lab3/part_1/data/cracks_subset/train" \
    "lab3/part_2/data/building_health_monitoring_dataset.csv" \
    "lab3/part_1/data/crack_cnn_best.pt" \
    "lab3/part_2/data/lstm_classifier_best.pt" \
    "lab4/part_1/data/building_health_monitoring_dataset.csv" \
    "lab6/data/seismic_data.csv" \
    "lab6/data/earthquake_risk_model.pkl" \
    "lab5/pdfs/Norma_E_020_CARGAS.pdf"
  do
    if [[ -e "${LABS_DIR}/${path}" ]]; then
      _log "   ✅ ${path}"
    else
      if [[ "$STRICT" == "1" ]]; then
        echo "   ❌ falta ${path}"
        FAIL=1
      else
        echo "   ⚠️  falta ${path} — ejecuta: bash labs/setup.sh"
      fi
    fi
  done

  if command -v ollama >/dev/null 2>&1 && curl -sf http://localhost:11434/api/tags >/dev/null 2>&1; then
    _log ""
    _log "✅ Ollama activo en :11434"
  elif [[ "$STRICT" == "1" ]]; then
    _log ""
    _log "ℹ️  Ollama no activo (omitido en CI; Labs 5–6 lo requieren en Codespaces)"
  else
    _log ""
    _log "⚠️  Ollama no activo (Labs 5–6): bash labs/lab5/_ollama_setup.sh"
  fi
fi

if [[ "$RUN_SMOKE" == "1" && -x "$PY" ]]; then
  _log ""
  _log "→ Smoke tests docentes"
  bash "${LABS_DIR}/_smoke_ia_solucion.sh" || FAIL=1
fi

if [[ "$FAIL" == "1" ]]; then
  echo ""
  echo "❌ Diagnóstico con errores. Repara con: bash labs/setup.sh"
  exit 1
fi

_log ""
_log "✅ Entorno labs OK"
exit 0
