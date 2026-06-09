#!/usr/bin/env bash
# Instala Ollama y descarga el modelo LLM del Lab 5 (no bloquea el resto del curso si falla).
set -euo pipefail

MODELO="${OLLAMA_MODEL:-llama3.2:3b}"

if command -v ollama >/dev/null 2>&1; then
  echo "✅ Ollama ya instalado: $(ollama --version 2>/dev/null || echo ok)"
else
  echo "→ Instalando Ollama…"
  curl -fsSL https://ollama.com/install.sh | sh
fi

if ! pgrep -x ollama >/dev/null 2>&1; then
  echo "→ Iniciando servicio Ollama en segundo plano…"
  nohup ollama serve >/tmp/ollama-serve.log 2>&1 &
  sleep 3
fi

echo "→ Descargando modelo ${MODELO} (puede tardar varios minutos la primera vez)…"
if ollama pull "${MODELO}"; then
  echo "✅ Modelo ${MODELO} listo."
else
  echo "⚠️ No se pudo descargar ${MODELO}. Ejecuta manualmente: ollama pull ${MODELO}"
  exit 0
fi

if curl -sf http://localhost:11434/api/tags >/dev/null; then
  echo "✅ Ollama responde en http://localhost:11434"
else
  echo "⚠️ Ollama instalado pero no responde aún. Revisa /tmp/ollama-serve.log"
fi
