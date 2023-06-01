import subprocess
import re
import csv

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    speeds = output.split(',')
    var29=speeds[29]
    var30=speeds[30]

    data_numbers = re.findall(r'\d+', var30)

    return var30, var29, data_numbers

def write_to_csv(data):
    with open('iozone_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

var30, var29, data_numbers = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

size = len(data_numbers)
last_6_numbers = data_numbers[17:23]

write_to_csv(last_6_numbers)
