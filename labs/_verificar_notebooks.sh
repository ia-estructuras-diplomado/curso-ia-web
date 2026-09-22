#!/usr/bin/env bash
# Docente: ejecuta de punta a punta los 6 notebooks de referencia (nbconvert).
# Lab 5 y Lab 6 no tienen notebook (son guías con Claude Code + MCP).
#
# Uso:
#   bash labs/_verificar_notebooks.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
JUP="${ROOT}/.venv/bin/jupyter"

if [[ ! -x "$JUP" ]]; then
  echo "❌ Crea el entorno: bash labs/setup.sh"
  exit 1
fi

NOTEBOOKS=(
  "lab0/fundamentos_python_ia.ipynb"
  "lab1/pca_monitoreo_estructural.ipynb"
  "lab2/resistencia_compresion.ipynb"
  "lab3/xai_estructuras.ipynb"
  "lab4/part_1/cnn_grietas_estructuras.ipynb"
  "lab4/part_2/rnn_sensores_estructuras.ipynb"
)

for nb in "${NOTEBOOKS[@]}"; do
  echo "▶ ${nb}"
  (cd "$(dirname "${ROOT}/${nb}")" && "$JUP" nbconvert --execute --to notebook --inplace \
    --ExecutePreprocessor.timeout=600 "$(basename "$nb")")
done

echo "✅ Todos los notebooks ejecutan de punta a punta."
