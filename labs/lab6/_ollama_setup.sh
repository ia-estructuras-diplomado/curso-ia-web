#!/usr/bin/env bash
# Lab 6 — instala Ollama y modelo llama3.2:3b (delega en Lab 5).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "${ROOT}/lab5/_ollama_setup.sh"
