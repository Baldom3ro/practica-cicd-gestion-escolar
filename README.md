# Práctica CI/CD - Gestión Escolar

Aplicación estática de demostración para automatizar validación, pruebas y despliegue en GitHub Pages.

## Archivos
- `index.html`, `styles.css`, `app.js`: aplicación.
- `tests/test_aplicacion.py`: pruebas automatizadas.
- `scripts/`: preparación, pruebas, liberación, despliegue y monitoreo.
- `.github/workflows/ci-cd.yml`: pipeline GitHub Actions.

## Ejecución local
```bash
bash scripts/configurar_entorno.sh
bash scripts/ejecutar_pruebas.sh
bash scripts/generar_liberacion.sh
python3 -m http.server 8000
```
Abre http://localhost:8000

## Despliegue
Sube el proyecto a GitHub en la rama `main`, habilita Pages mediante GitHub Actions en Settings > Pages y revisa Actions. El workflow publicará el contenido de `dist/`.
