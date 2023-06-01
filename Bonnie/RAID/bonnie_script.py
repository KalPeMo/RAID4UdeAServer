import subprocess
import sys
import datetime

def run_bonnie_command(mount_point, size, range_size):
    command = f"bonnie++ -d {mount_point} -u raid -s {size} -r {range_size} -b -n 0 -m raid"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def export_results_to_file(results):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("resultados.txt", "a") as file:
        file.write(f"\n\n==== Resultados - {timestamp} ====\n\n")
        for command, output in results.items():
            file.write(f"Comando: {command}\n")
            file.write(output)
            file.write("\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Debe proporcionar los tamaños de prueba (s y r) como parámetros de entrada.")
        sys.exit(1)

    size = sys.argv[1]
    range_size = sys.argv[2]

    mount_points = ["/mnt/md0", "/mnt/md1", "/mnt/md5"]
    commands = [f"bonnie++ -d {mount_point} -u raid -s {size} -r {range_size} -b -n 0 -m raid" for mount_point in mount_points]

    results = {}
    for mount_point, command in zip(mount_points, commands):
        output = run_bonnie_command(mount_point, size, range_size)
        results[command] = output

    export_results_to_file(results)

    print("La ejecución de los comandos ha finalizado. Los resultados se han agregado en el archivo resultados.txt.")
