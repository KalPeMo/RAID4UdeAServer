import subprocess

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Get the read and write speed
    speeds = output.split(',')
    read_speed = speeds[0]
    write_speed = speeds[1]

    # Get the rewrite, read reread, random read, and random write speed
    rewrite_speed = speeds[2]
    read_reread_speed = speeds[3]
    random_read_speed = speeds[4]
    random_write_speed = speeds[5]

    return read_speed, write_speed, rewrite_speed, read_reread_speed, random_read_speed, random_write_speed


read_speed, write_speed, rewrite_speed, read_reread_speed, random_read_speed, random_write_speed = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

print(f"Read speed: {read_speed}")
print(f"Write speed: {write_speed}")
print(f"Rewrite speed: {rewrite_speed}")
print(f"Read reread speed: {read_reread_speed}")
print(f"Random read speed: {random_read_speed}")
print(f"Random write speed: {random_write_speed}")


