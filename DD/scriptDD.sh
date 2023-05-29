#!/bin/bash

# Configuración de variables
archivo_salida="resultado.csv"
tamanos_bloques=("1M" "2M" "4M")
cantidades_bloques=("100" "200" "500")

# Encabezado del archivo CSV
echo "Tamaño Bloque, Cantidad Bloques, Tiempo, Temperatura" > $archivo_salida

# Bucle para ejecutar las pruebas con diferentes configuraciones
for tamano_bloque in "${tamanos_bloques[@]}"
do
    for cantidad_bloques in "${cantidades_bloques[@]}"
    do
        tiempo=$(sudo dd if=/dev/zero of=./archivo_salida bs=$tamano_bloque count=$cantidad_bloques 2>&1 | grep "elapsed" | awk '{print $NF}')
        temperatura=$(sensors | grep "RAID Temperature" | awk '{print $3}')
        echo "$tamano_bloque, $cantidad_bloques, $tiempo, $temperatura"
        echo "$tamano_bloque, $cantidad_bloques, $tiempo, $temperatura" >> $archivo_salida
    done
done
sudo dd if=/dev/zero of=./archivo_salida bs=1M count=100
echo "Pruebas completadas."
