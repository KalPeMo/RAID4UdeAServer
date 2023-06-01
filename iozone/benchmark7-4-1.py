import subprocess
import re

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Get the read and write speed
    speeds = output.split(',')

    # Print the size of speeds
    size_of_speeds = len(speeds)
    print(f"Size of speeds: {size_of_speeds}")


if __name__ == "__main__":
    get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")
