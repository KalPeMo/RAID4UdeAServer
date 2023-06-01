#!/bin/bash

raid_device="/mnt/md0"
benchmark_output="bonnie_results.txt"

# Verificar si el dispositivo RAID existe
if [ ! -e "$raid_device" ]; then
  echo "El dispositivo RAID no existe o no está accesible."
  exit 1
fi

# Ejecutar bonnie++ y redirigir la salida al archivo de resultados
bonnie++ -d "$raid_device" -s 1G -u 1000:1000 -q -n 0:500:200:1 -r 100:500 > "$benchmark_output" 2>&1

# Verificar si bonnie++ se ejecutó correctamente
if [ $? -eq 0 ]; then
  echo "El benchmark se ha completado correctamente."
  echo "Los resultados se encuentran en el archivo: $benchmark_output"
else
  echo "Se produjo un error al ejecutar el benchmark."
fi
