import subprocess
import re

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    speeds = output.split(',')
    var29=speeds[29]
    var30=speeds[30]

    data_numbers = re.findall(r'\d+', var30)

    return var30, var29, data_numbers

var30, var29, data_numbers = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

print(f"var29: {var29}")
print(f"var30: {var30}")
print(f"data_numbers: {data_numbers}")
size = len(data_numbers)
print(size)
last_6_numbers = data_numbers[17:23]
print(last_6_numbers)
