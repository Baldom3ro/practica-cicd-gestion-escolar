#!/usr/bin/env bash
set -e
echo "Ejecutando pruebas automatizadas..."

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

$PYTHON_CMD -m unittest discover -s tests -v
