import subprocess

def run_bonnie_raid0():
    raid_device = subprocess.getoutput("sudo lsblk -o NAME,MOUNTPOINT | grep md0 | awk '{print $2}'")
    benchmark_output = 'bonnie_results.txt'

    # Construir el comando para ejecutar Bonnie++ en el RAID 0
    command = f'sudo bonnie++ -d {raid_device} -s 1G -u 1000:1000 -q -n 0:500:200:1 -r 100:500'

    # Ejecutar el comando y capturar la salida
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Guardar los resultados en un archivo de texto
    with open(benchmark_output, 'w') as file:
        file.write(stdout.decode())

    # Imprimir la salida y el error (si los hay)
    print('Salida:')
    print(stdout.decode())
    print('Error:')
    print(stderr.decode())

# Ejecutar la función para realizar el benchmark del RAID 0
run_bonnie_raid0()
