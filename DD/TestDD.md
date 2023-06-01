# Bencharmark de DD

El benchmark de disco duro (DD) es una herramienta utilizada para evaluar el rendimiento de un conjunto RAID (Redundant Array of Independent Disks, o conjunto redundante de discos independientes). Un RAID combina múltiples discos duros en un solo sistema para mejorar la velocidad, la capacidad o la tolerancia a fallos.

El benchmark de DD se utiliza para medir la velocidad de transferencia de datos, el tiempo de acceso a los datos y otros parámetros relacionados con el rendimiento de los discos duros en un RAID. Esto proporciona información valiosa sobre el desempeño general del conjunto RAID y puede ayudar a identificar posibles cuellos de botella o áreas de mejora.

Al realizar un benchmark de DD en un RAID, generalmente se utilizan aplicaciones específicas o utilidades diseñadas para medir el rendimiento de los discos duros. Estas herramientas generan una serie de pruebas y mediciones, como la velocidad de lectura/escritura secuencial y aleatoria, el rendimiento de entrada/salida por segundo (IOPS), el tiempo medio de búsqueda (latencia), entre otros.

Los resultados del benchmark de DD pueden compararse con los resultados de referencia o con otros sistemas RAID similares para evaluar el rendimiento relativo. También pueden utilizarse para detectar posibles problemas, como discos duros defectuosos o configuraciones subóptimas.

Es importante tener en cuenta que el rendimiento de un RAID no solo depende de los discos duros utilizados, sino también de otros factores como el controlador RAID, la configuración del RAID, el tamaño de la caché y el sistema operativo. Por lo tanto, el benchmark de DD es una herramienta útil para evaluar el rendimiento de los discos duros en un RAID, pero no proporciona una imagen completa del rendimiento general del sistema.

## Pruebas de DD benchmark

### Prueba 1

![Prueba 1](./img/PruebaInicialDD.jpg)

Esta prueba se realizó con el comando `sudo dd if=/dev/zero of=./dd/archivo_salida bs=1M count=directconv=fdatasync`

### Prueba 2

![Prueba 2](./img/PruebaFinalDD.jpg)

Esta prueba se realizó con el RAID 0. En uno de los discos duros de 1TB.

Para realizar esta prueba es necesario tener en cuenta los siguientes archivos:

![ArchivosDD](./img/ArchivosNecesariosDD.jpg)

Donde el archivo `scriptDD.sh` contiene el siguiente código:

```bash
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
```

El archivo `scriptDD.sh` se encarga de ejecutar las pruebas y guardar los resultados en el archivo `resultado.csv` (el cual se crea automáticamente al correr el script).

Además, en el archivo `archivo_salida` se encuentran los datos que se escriben en el disco duro, los cuales son traidos desde `/dev/zero`. Este archivo también se crea automáticamente al correr el script.

## Prueba 3

Se realizó una prueba sobre el disco H, el cual es un disco de 1TB. Se realizó con el RAID 0.

![Prueba DiscoH](./img/PruebaDiscoH.png)

![Prueba DiscoH 2](./img/PruebaDiscoH2.png)

![Prueba DiscoH 3](./img/PruebaDiscoH3.png)

Para realizar la prueba, se asigno la variable "of" la cual tenía la ruta del disco H: `of=/mnt/discoh/`

## Dificultades

Al momento de realizar las pruebas, se presentaron las siguientes dificultades:

- El archivo `scriptDD.sh` no se ejecutaba correctamente. Esto se debía a que el archivo no tenía permisos de ejecución. Para solucionar esto, se ejecutó el comando `chmod +x scriptDD.sh` para darle permisos de ejecución al archivo.
- La carpeta "discoh" no se podría crear, dentro del disco sdh:
  ![Errores al crear carpeta](./img/ErrorCrearCarpeta.png)
  Así que se tuvo que usar el comando -t y ext4 para crear la carpeta.
