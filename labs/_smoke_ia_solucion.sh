#!/usr/bin/env bash
# Valida vía IA: smoke tests + ejecución de *_solucion_ia.ipynb (prompts canónicos).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="${ROOT}/.venv/bin/python"
JUP="${ROOT}/.venv/bin/jupyter"

if [[ ! -x "$PY" ]]; then
  echo "❌ Crea el entorno: bash labs/setup.sh"
  exit 1
fi

"$PY" "${ROOT}/lab0/_smoke_test.py"
"$PY" "${ROOT}/lab2/_smoke_test.py"
"$PY" "${ROOT}/lab4/part_1/_smoke_test.py"
"$PY" "${ROOT}/lab4/part_2/_smoke_test.py"
"$PY" "${ROOT}/lab6/_smoke_test.py"

for nb in \
  "${ROOT}/lab0/fundamentos_python_ia_solucion_ia.ipynb" \
  "${ROOT}/lab1/pca_monitoreo_estructural_solucion_ia.ipynb" \
  "${ROOT}/lab2/resistencia_compresion_solucion_ia.ipynb"
do
  echo "▶ Ejecutando $(basename "$nb")..."
  (cd "$(dirname "$nb")" && "$JUP" nbconvert --execute --to notebook --ExecutePreprocessor.timeout=300 "$(basename "$nb")")
done

echo "✅ Smoke IA completado."
