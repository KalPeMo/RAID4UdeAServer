import subprocess
import re
import csv
import sys
import datetime

def convert_to_kb(size):
    unit = size[-1].lower()
    value = int(size[:-1])
    if unit == 'g':
        return value * 1024 * 1024
    elif unit == 'm':
        return value * 1024
    elif unit == 'k':
        return value
    else:
        return size

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    speeds = output.split(',')
    var22 = speeds[22]
    var23 = speeds[23]
    var30 = speeds[30]

    data_numbers = re.findall(r'\d+', var30)
    #print(f"var30:{var30}, var22:{var22}")

    return var30, var23, var22, data_numbers

# no se puede print(f"var30:{var30}")

def write_to_csv(data):
    with open('iozone_3replicas17-1.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not csvfile.tell():
            writer.writerow(['Benchmark', 'Disk', 'Test', 'Replica', 'file_size_in', 'reg_size_in', 'random_write(KB/s)', 'random_rewrite(KB/s)', 'random-reread', 'time', 'timestamp'])
        writer.writerow(data)


def get_time():
    return datetime.datetime.now()


def run_experiment(file_size, record_size, chunk_size, replicas, experiment_number, total_experiments, disk):
    for replica in range(replicas):
        print(f"\nIniciando prueba {experiment_number} de {total_experiments}, Replica {replica+1} de {replicas}")
        start_time = get_time()

        command = f"sudo iozone -a -i 0 -i 1 -s {file_size} -r {record_size} -I -f {disk}"
        var30, var23, var22, data_numbers = get_iozone_speed(command)

        size = len(data_numbers)
        last_6_numbers = data_numbers[17:23]
        buscandotiempo = data_numbers[24:26]
        print(f"Resultados:{last_6_numbers}")
        print(f"Donde esta el tiempo:{buscandotiempo}")
        time_test = get_time()
        difference = time_test - start_time

        # Eliminar la "k" del tamaño del registro
        record_size_no_unit = record_size[:-1]

        write_to_csv(['iozone', disk, experiment_number, replica+1, file_size, record_size_no_unit] + last_6_numbers + [difference, time_test])

        print(f"Fin de prueba {experiment_number} de {total_experiments}, Replica {replica+1} de {replicas}")


# Definir los parámetros del diseño experimental
file_sizes = [ '64k','4M','8M','16M','32M','64M','100M','500M','1G','2G','4G']
record_sizes = ['1k','4k','8k','16k','32k','64k']
replicas = 3

total_experiments = len(file_sizes) * len(record_sizes) * replicas
experiment_number = 0

# Obtener la ruta del disco desde la línea de comandos
if len(sys.argv) > 1:
    disk = sys.argv[1]
else:
    disk = "/dev/md0"  # Ruta por defecto si no se especifica en la línea de entrada 

#Ejecutar el diseño experimental
for file_size in file_sizes:
    file_size_kb = convert_to_kb(file_size)
    for record_size in record_sizes:
        for _ in range(replicas):
            experiment_number += 1
            run_experiment(file_size_kb, record_size, record_size, replicas, experiment_number, total_experiments, disk)

print("Las pruebas con IOZONE han concluido con éxito")
