#!/usr/bin/env bash
set -e
echo "Verificando herramientas necesarias..."

if python3 --version >/dev/null 2>&1; then
  PYTHON_CMD="python3"
elif python --version >/dev/null 2>&1; then
  PYTHON_CMD="python"
elif py --version >/dev/null 2>&1; then
  PYTHON_CMD="py"
else
  echo "ERROR: Python 3 no está instalado."
  exit 1
fi

$PYTHON_CMD --version
echo "No se requieren paquetes externos. Entorno listo."
