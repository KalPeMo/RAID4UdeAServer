# bonnie_script.py

Este script de Python se utiliza para ejecutar comandos `bonnie++` en diferentes puntos de montaje RAID y guardar los resultados en un archivo de texto.

## Requisitos

- Python 3 instalado en el sistema.
- Comando `bonnie++` instalado y disponible en la línea de comandos.

## Uso

1. Abre una terminal en el directorio donde se encuentra el script `bonnie_script.py`.
2. Ejecuta el script utilizando el comando `python bonnie_script.py [s] [r]`, donde `[s]` y `[r]` son los tamaños de prueba deseados.
   Por ejemplo: `python bonnie_script.py 8000 2000`
3. El script ejecutará automáticamente los comandos `bonnie++` en los puntos de montaje especificados y guardará los resultados en un archivo llamado `resultados.txt`.
4. Los resultados de cada ejecución se agregarán debajo de los resultados previos en `resultados.txt`, y se incluirá un título con la marca de tiempo para identificar cada ejecución.

## Personalización

- Puedes modificar los puntos de montaje `mount_points` en el script para adaptarlos a tu configuración de RAID.
- Asegúrate de tener los permisos necesarios para ejecutar los comandos `bonnie++` y de tener los puntos de montaje correctos en tu sistema.

## Notas

- Los resultados generados por `bonnie++` son específicos de tu configuración de hardware y software RAID. Ten en cuenta que los resultados pueden variar según estos factores.
- Recuerda que el script utiliza el comando `subprocess.run()` para ejecutar los comandos `bonnie++` en el sistema. Asegúrate de que los comandos sean válidos en tu entorno antes de ejecutar el script.
