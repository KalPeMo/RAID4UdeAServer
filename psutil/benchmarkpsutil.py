import psutil
import csv
import datetime
import getpass

# Obtener el disco desde los argumentos de línea de comandos
if len(sys.argv) > 1:
    disk = sys.argv[1]
else:
    disk = '/dev/sda'  # Disco predeterminado si no se especifica ninguno

# Definir los parámetros de prueba
file_sizes = ['1M', '4M', '16M']  # Tamaños de archivo
block_sizes = ['4k', '8k', '16k']  # Tamaños de bloque

# Nombre del archivo CSV para almacenar los resultados
csv_file = 'benchmark_results.csv'

# Obtener el timestamp actual y el nombre de usuario
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
username = getpass.getuser()

# Abrir el archivo CSV en modo de escritura
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Realizar las pruebas con diferentes combinaciones de parámetros
    total_tests = len(file_sizes) * len(block_sizes)
    current_test = 1

    for file_size in file_sizes:
        for block_size in block_sizes:
            # Imprimir información de la prueba en la consola
            print(f"Iniciando prueba {current_test} de {total_tests}...")
            print(f"Especificaciones: Tamaño de archivo: {file_size}, Tamaño de bloque: {block_size}")

            # Obtener el timestamp de inicio de la prueba
            start_time = datetime.datetime.now()

            # Ejecutar la prueba de rendimiento utilizando psutil
            disk_stats_before = psutil.disk_io_counters(perdisk=True)[disk]

            # Realizar la operación de lectura/escritura en el disco
            # Aquí puedes implementar tu lógica específica de lectura/escritura

            # Obtener los datos de rendimiento después de la operación
            disk_stats_after = psutil.disk_io_counters(perdisk=True)[disk]

            # Calcular las velocidades de lectura y escritura
            read_speed = disk_stats_after.read_bytes - disk_stats_before.read_bytes
            write_speed = disk_stats_after.write_bytes - disk_stats_before.write_bytes

            # Obtener el timestamp de finalización de la prueba y calcular el tiempo transcurrido
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time

            # Escribir los resultados en el archivo CSV
            writer.writerow([timestamp, username, file_size, block_size, read_speed, write_speed, str(elapsed_time)])

            # Imprimir información de finalización de la prueba en la consola
            print(f"Finalizada prueba {current_test} de {total_tests}. Tiempo transcurrido: {elapsed_time}\n")

            current_test += 1

print("Pruebas de rendimiento completadas. Los resultados se han guardado en el archivo CSV.")
