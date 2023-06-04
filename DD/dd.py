import subprocess
import csv
import datetime
import re

def get_dd_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stderr.strip()

    # Utilizar expresiones regulares para extraer los valores
    time_match = re.search(r'(\d+\.\d+)\s+s,', output)
    speed_match = re.search(r'(\d+)\s+MB/s', output)

    # Obtener el tiempo y la velocidad de escritura secuencial
    time = time_match.group(1) if time_match else ''
    sequential_write = speed_match.group(1) if speed_match else ''

    # Convertir la velocidad de escritura a KB/s
    sequential_write = str(float(sequential_write) * 1024) if sequential_write else ''

    # Asignar el valor de sequential_write a sequential_read
    sequential_read = sequential_write

    return sequential_write, sequential_read, time


def write_to_csv(data):
    with open('dd_results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not csvfile.tell():
            writer.writerow(['BenchmarkName', 'DiskName', 'Test', 'Replica', 'file_size_in', 'reg_size_in',
                             'sequential_write (KB/s)', 'random_write(KB/s)', 'random_rewrite(KB/s)', 'random_read(KB/s)',
                             'time(s)', 'timestamp(s)', 'sequential_read (KB/s)'])
        writer.writerow(data)


def run_experiment(file_size, chunk_size, replicas):
    for replica in range(replicas):
        print(f"Iniciando prueba con file_size={file_size}, chunk_size={chunk_size}, Réplica {replica + 1}")
        start_time = datetime.datetime.now()

        # Eliminar la letra "M" o "K" de file_size y chunk_size
        file_size_numeric = file_size[:-1]
        chunk_size_numeric = chunk_size[:-1]

        # Convertir file_size_numeric y chunk_size_numeric a KB/s
        file_size_numeric = str(int(file_size_numeric) * 1024)
        chunk_size_numeric = str(int(chunk_size_numeric) * 1024)

        command = f"dd if=/dev/zero of={output_file} bs={chunk_size} count={file_size}"
        sequential_write, sequential_read, time = get_dd_speed(command)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        write_to_csv(['DD',output_file,experiment_number, replica + 1, file_size_numeric, file_size_numeric, sequential_write, '0', '0', '0',
                      time, timestamp, sequential_read])

        print(f"Prueba con file_size={file_size}, chunk_size={chunk_size}, Réplica {replica + 1} finalizada")


# Definir los parámetros del diseño experimental
file_sizes = ['1M', '4M', '16M', '32M', '64M', '1024M']
chunk_sizes = ['4k', '8k', '16k']
replicas = 5
output_file = '/mnt/md1/archivo_salida'
experiment_number = 1

# Ejecutar el diseño experimental
for file_size in file_sizes:
    for chunk_size in chunk_sizes:
        run_experiment(file_size, chunk_size, replicas)
        experiment_number += 1

print("Las pruebas con DD han concluido con éxito")
