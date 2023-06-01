import subprocess

output_file = "raid@raid:~/repo/RAID4UdeAServer/Bonnie/md0/bonnie_results.csv"

# Ejecutar bonnie++ y redirigir la salida al archivo personalizado
subprocess.run(["bonnie++", "-d", "/mnt/md0", "-u", "raid", "-s", "0", "-r", "0", "-b", "-n", "0", "-m", "raid", "-f", output_file], stdout=subprocess.PIPE)

print("Bonnie++ ejecutado correctamente.")
