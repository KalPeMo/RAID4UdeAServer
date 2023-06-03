import subprocess
import re
import csv
import sys
import datetime

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    speeds = output.split(',')
    var28 = speeds[28]
    var30 = speeds[30]

    data_numbers = re.findall(r'\d+', var30)
    #print(f"var28:{var29}, var30:{var30}")
    print(f"var28:{var28}")

    return var30, var28, data_numbers


def write_to_csv(data):
    with open('iozone_results15.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not csvfile.tell():
            writer.writerow(['Benchmark', 'Disk', 'Test', 'Replica', 'file_size_in', 'reg_size_in', 'random_write(KB/s)', 'random_rewrite(KB/s)', 'random_read(KB/s)', 'random-reread', 'time', 'timestamp'])
        writer.writerow(data)


def get_time():
    return datetime.datetime.now()


def run_experiment(file_size, record_size, chunk_size, replicas, experiment_number, total_experiments, disk):
    for replica in range(replicas):
        print(f"Iniciando prueba {experiment_number} de {total_experiments}, Replica {replica+1} de {replicas}")
        start_time = get_time()

        command = f"sudo iozone -a -i 0 -i 1 -s {file_size} -r {record_size} -I -f {disk}"
        var30, var29, data_numbers = get_iozone_speed(command)

        size = len(data_numbers)
        last_6_numbers = data_numbers[17:23]

        time_test = get_time()
        difference = time_test - start_time

        write_to_csv(['iozone', disk, experiment_number, replica+1] + last_6_numbers + [difference, time_test])

        print(f"Fin de prueba {experiment_number} de {total_experiments}, Replica {replica+1} de {replicas}")


# Definir los parámetros del diseño experimental
file_sizes = ['20M', '19M', '18M', '17M', '16M', '8M']
record_sizes = ['4k', '8k', '16k']
replicas = 1

total_experiments = len(file_sizes) * len(record_sizes) * replicas
experiment_number = 0

# Obtener la ruta del disco desde la línea de comandos
if len(sys.argv) > 1:
    disk = sys.argv[1]
else:
    disk = "/dev/md0"  # Ruta por defecto si no se especifica en la línea de comandos

# Ejecutar el diseño experimental
for file_size in file_sizes:
    for record_size in record_sizes:
        for _ in range(replicas):
            experiment_number += 1
            run_experiment(file_size, record_size, record_size, replicas, experiment_number, total_experiments, disk)

print("Las pruebas con IOZONE han finalizado con éxito")
