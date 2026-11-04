#!/usr/bin/env bash
set -e
echo "Este proyecto utiliza GitHub Pages para el despliegue."
echo "1. Confirma que los cambios estén en la rama main."
echo "2. El workflow .github/workflows/ci-cd.yml realiza el despliegue automáticamente."
echo "3. Para solicitar una ejecución manual, usa: gh workflow run ci-cd.yml --ref main"
if command -v gh >/dev/null 2>&1; then
  read -r -p "¿Deseas iniciar ahora el workflow? (s/n): " respuesta
  if [[ "$respuesta" == "s" || "$respuesta" == "S" ]]; then
    gh workflow run ci-cd.yml --ref main
  fi
else
  echo "GitHub CLI no está instalado; realiza un push a main o ejecuta el workflow desde GitHub."
fi
