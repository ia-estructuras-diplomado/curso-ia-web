#!/usr/bin/env bash
# Instala Ollama y descarga el modelo LLM del Lab 5 (no bloquea el resto del curso si falla).
set -euo pipefail

MODELO="${OLLAMA_MODEL:-llama3.2:3b}"

_ensure_zstd() {
  if command -v zstd >/dev/null 2>&1; then
    return 0
  fi
  echo "→ Instalando zstd (requerido por el instalador de Ollama)…"
  if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update -qq
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y zstd
  elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y zstd
  elif command -v yum >/dev/null 2>&1; then
    sudo yum install -y zstd
  elif command -v apk >/dev/null 2>&1; then
    sudo apk add --no-cache zstd
  else
    echo "❌ zstd no está instalado y no se detectó gestor de paquetes."
    echo "   Instálalo manualmente y vuelve a ejecutar este script."
    exit 1
  fi
}

if command -v ollama >/dev/null 2>&1; then
  echo "✅ Ollama ya instalado: $(ollama --version 2>/dev/null || echo ok)"
else
  _ensure_zstd
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
