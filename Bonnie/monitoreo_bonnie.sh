#!/bin/bash

output_file="resultadosbonnie.csv"

# Get the current date and time
current_date=$(date +"%Y-%m-%d %H:%M:%S")

# Header of the CSV file
echo "Disco, Fecha y Hora, Resultados" > $output_file

# List of disks
discos=("sda" "sdb" "sdc" "sdd" "sde" "sdf" "sdg" "sdh")

# Execute bonnie++ for each disk and append the results to the CSV file
for disco in "${discos[@]}"
do
    echo "Ejecutando bonnie++ en el disco $disco..."

    # Execute bonnie++ and append the output to the CSV file
    sudo bonnie++ -u root -x 10 -q -r 1024 -s 0 -m "$disco benchmark" >> $output_file

    echo "Finalizado bonnie++ en el disco $disco."
done

echo "Proceso completado. Los resultados se han guardado en $output_file."
