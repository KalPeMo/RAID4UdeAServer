import subprocess
import time
import tempfile
import os

disks = ['/dev/sda', '/dev/sdb', '/dev/sdc', '/dev/sdd', '/dev/sde', '/dev/sdf', '/dev/sdg', '/dev/sdh']
block_size = '1024M'
amount_of_blocks = '1024'
output_file = 'resultadosbonnie.csv'

with open(output_file, 'w') as file:
    file.write('disk,block_size,amount_of_blocks,time_needed\n')

    for disk in disks:
        start_time = time.time()

        with tempfile.TemporaryDirectory() as temp_dir:
            command = ['bonnie++', '-d', temp_dir, '-s', block_size, '-n', '0', '-m', disk[5:], '-r', amount_of_blocks]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, _ = process.communicate()

        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000

        file.write(f'{disk},{block_size},{amount_of_blocks},{elapsed_time_ms:.2f}\n')

print('Bonnie++ test completed.')

