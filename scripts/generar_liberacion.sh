#!/usr/bin/env bash
set -e
echo "Generando carpeta de liberación..."
rm -rf dist
mkdir -p dist
cp index.html styles.css app.js dist/
echo "Contenido generado en la carpeta dist/"
ls -la dist
