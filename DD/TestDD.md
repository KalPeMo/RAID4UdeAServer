# Bencharmark de DD

El benchmark de disco duro (DD) es una herramienta utilizada para evaluar el rendimiento de un conjunto RAID (Redundant Array of Independent Disks, o conjunto redundante de discos independientes). Un RAID combina múltiples discos duros en un solo sistema para mejorar la velocidad, la capacidad o la tolerancia a fallos.

El benchmark de DD se utiliza para medir la velocidad de transferencia de datos, el tiempo de acceso a los datos y otros parámetros relacionados con el rendimiento de los discos duros en un RAID. Esto proporciona información valiosa sobre el desempeño general del conjunto RAID y puede ayudar a identificar posibles cuellos de botella o áreas de mejora.

Al realizar un benchmark de DD en un RAID, generalmente se utilizan aplicaciones específicas o utilidades diseñadas para medir el rendimiento de los discos duros. Estas herramientas generan una serie de pruebas y mediciones, como la velocidad de lectura/escritura secuencial y aleatoria, el rendimiento de entrada/salida por segundo (IOPS), el tiempo medio de búsqueda (latencia), entre otros.

Los resultados del benchmark de DD pueden compararse con los resultados de referencia o con otros sistemas RAID similares para evaluar el rendimiento relativo. También pueden utilizarse para detectar posibles problemas, como discos duros defectuosos o configuraciones subóptimas.

Es importante tener en cuenta que el rendimiento de un RAID no solo depende de los discos duros utilizados, sino también de otros factores como el controlador RAID, la configuración del RAID, el tamaño de la caché y el sistema operativo. Por lo tanto, el benchmark de DD es una herramienta útil para evaluar el rendimiento de los discos duros en un RAID, pero no proporciona una imagen completa del rendimiento general del sistema.

## Pruebas de DD benchmark

### Prueba 1

![Prueba 1](./img/PruebaInicialDD.jpg)

Esta prueba se realizó con el comando `dd if=/dev/zero of=/tmp/output.img bs=8k count=256k conv=fdatasync` y se obtuvo un resultado de 1.1 GB/s.

### Prueba 2

![Prueba 2](./img/PruebaFinalDD.jpg)

Esta prueba se realizó con el ScriptDD.sh, sobre el RAID 0.
