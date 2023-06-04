import subprocess
import csv
import datetime

file_sizes = [256]  # Tamaños de archivo en KB (de menor a mayor)
chunk_sizes = [4]  # Tamaños de chunk en KB
replicas = 1  # Número de réplicas

raid_mount_points = ["/mnt/md0"]  # Puntos de montaje de los RAID

def run_bonnie_command(mount_point, file_size, chunk_size):
    command = f"bonnie++ -d {mount_point} -u raid -s {file_size} -r {chunk_size} -b -n 0 -m raid"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def extract_value(line, prefix):
    value = line.partition(prefix)[2].strip()
    if "KB/s" in value:
        value = value.replace("KB/s", "")
    elif "us" in value:
        value = value.replace("us", "")
    elif "ms" in value:
        value = value.replace("ms", "")
    return value.strip()

def export_results_to_csv(results, file_size, chunk_size, raid_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "results.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BenchmarkName", "DiskName", "Test", "Replica", "file_size_in", "reg_size_in", "sequential_write (KB/s)", "random_write(KB/s)", "random_rewrite(KB/s)", "random_read(KB/s)", "time(s)", "timestamp(s)", "sequential_read (KB/s)"])

        for test_num, (command, output) in enumerate(results.items(), start=1):
            benchmark_name = "bonnie"
            disk_name = raid_name
            replica = (test_num - 1) % replicas + 1
            reg_size_in = chunk_size

            sequential_write = ""
            sequential_read = ""
            random_write = ""
            random_rewrite = ""
            random_read = ""
            time = ""

            rows = output.strip().split("\n")
            for row in rows:
                if "raid" in row:
                    columns = row.split()
                    sequential_write = columns[2]
                    sequential_read = columns[5]
                    random_write = columns[8]
                    random_rewrite = columns[11]
                    random_read = columns[14]
                    time = columns[17]
                    break
            writer.writerow([benchmark_name, disk_name, test_num, replica, file_size, reg_size_in, sequential_write, random_write, random_rewrite, random_read, time, timestamp, sequential_read])

total_tests = len(file_sizes) * len(chunk_sizes) * len(raid_mount_points)
current_test = 0

for raid_index, mount_point in enumerate(raid_mount_points):
    raid_name = f"dev/md{raid_index}"
    for file_size in file_sizes:
        for chunk_size in chunk_sizes:
            current_test += 1
            print(f"Corriendo prueba {current_test} de {total_tests} en RAID {raid_name}")
            print(f"Tamaño de archivo: {file_size} KB")
            print(f"Tamaño de chunk: {chunk_size} KB")
            results = {}
            for replica in range(replicas):
                output = run_bonnie_command(mount_point, file_size, chunk_size)
                results[replica + 1] = output
                print(f"Réplica actual: {replica + 1}")
            export_results_to_csv(results, file_size, chunk_size, raid_name)

print("La ejecución de las pruebas ha finalizado. Los resultados se han guardado en el archivo CSV.")
