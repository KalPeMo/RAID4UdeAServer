import subprocess
import datetime

def run_bonnie_test(device, file_size, chunk_size, replica):
    command = f"bonnie++ -d {device} -u raid -s {file_size} -r {chunk_size} -b -n 0 -m raid"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    export_results_to_txt(output, device, file_size, chunk_size, replica)

def export_results_to_txt(output, device, file_size, chunk_size, replica):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "salida.txt"
    with open(filename, "a") as file:
        file.write(f"\n=====================\n")
        file.write(f"RAID: {device}\n")
        file.write(f"Tamaño de archivo: {file_size} KB\n")
        file.write(f"Tamaño de chunk: {chunk_size} KB\n")
        file.write(f"Réplica: {replica}\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"\n{output}\n")

if __name__ == "__main__":
    raid_mount_points = ["/mnt/md0", "/mnt/md1", "/mnt/md5"]
    file_sizes = [1024, 4096, 16384, 32768, 65536, 1048576]  # Tamaños de archivo en KB (de menor a mayor)
    chunk_sizes = [4, 8, 16]  # Tamaños de chunk en KB
    replicas = range(1, 6)
    
    with open("salida.txt", "w") as file:
        file.write("Resultados de las pruebas\n")
        file.write("=====================\n")

    for device in raid_mount_points:
        for file_size in file_sizes:
            for chunk_size in chunk_sizes:
                print(f"Corriendo pruebas en RAID {device}")
                print(f"Tamaño de archivo: {file_size} KB")
                print(f"Tamaño de chunk: {chunk_size} KB")
                print("---------------------")
                
                for replica in replicas:
                    print(f"Réplica actual: {replica}")
                    run_bonnie_test(device, file_size, chunk_size, replica)
                    
                print("---------------------")
                print("Pruebas completadas para este RAID y configuración.")
                print("=====================")
                
    print("La ejecución de las pruebas ha finalizado. Los resultados se han guardado en el archivo salida.txt.")
