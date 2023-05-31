#!/bin/bash

raid_device="/dev/md0"
benchmark_output="bonnie_results.txt"

# Cambiar al directorio raíz para poder acceder al dispositivo RAID 0
cd /

# Ejecutar Bonnie++ en el RAID 0 y redirigir la salida al archivo de resultados
sudo bonnie++ -d "$raid_device" -s 1G -u 1000:1000 -q -n 0:500:200:1 -r 100:500 > "$benchmark_output" 2>&1

# Imprimir la salida del comando
cat "$benchmark_output"
