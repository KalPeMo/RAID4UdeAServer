import subprocess

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Get the read and write speed
    speeds = output.split(',')
    read_speed = speeds[0]
    write_speed = speeds[1]

    return read_speed, write_speed


read_speed, write_speed = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

print(f"Read speed: {read_speed}")
print(f"Write speed: {write_speed}")

