#!/usr/bin/env python3
"""Comprobación básica de disponibilidad y tiempo de respuesta."""
import sys
import time
import urllib.request
import urllib.error

if len(sys.argv) != 2:
    print("Uso: python3 scripts/monitor.py https://usuario.github.io/repositorio/")
    sys.exit(2)

url = sys.argv[1]
inicio = time.perf_counter()
try:
    solicitud = urllib.request.Request(url, headers={"User-Agent": "Practica-CICD-Monitor/1.0"})
    with urllib.request.urlopen(solicitud, timeout=10) as respuesta:
        codigo = respuesta.status
        contenido = respuesta.read()
    duracion = time.perf_counter() - inicio
    print(f"URL: {url}")
    print(f"Código HTTP: {codigo}")
    print(f"Tiempo de respuesta: {duracion:.3f} segundos")
    print(f"Tamaño recibido: {len(contenido)} bytes")
    if codigo == 200 and duracion <= 2:
        print("RESULTADO: servicio disponible; cumple el objetivo de 2 segundos.")
    elif codigo == 200:
        print("RESULTADO: servicio disponible, pero supera el objetivo de 2 segundos.")
        sys.exit(1)
except (urllib.error.URLError, TimeoutError) as error:
    print(f"RESULTADO: no fue posible acceder al servicio: {error}")
    sys.exit(1)
