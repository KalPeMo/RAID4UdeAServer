import subprocess

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    speeds = output.split(',')
    var29=speeds[29]
    var30=speeds[30]

    return var30, var29

var30, var29 = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

    #return read_speed, write_speed, rewrite_speed, read_reread_speed, random_read_speed, random_write_speed, sequential_read_speed, sequential_write_speed>

print(f"var29: {var29}")
print(f"var29: {var30}")

#print(f"Read speed: {read_speed}")
#print(f"Write speed: {write_speed}")
#print(f"Rewrite speed: {rewrite_speed}")
#print(f"Read reread speed: {read_reread_speed}")
#print(f"Random read speed: {random_read_speed}")
#print(f"Random write speed: {random_write_speed}")
#print(f"Sequential read speed: {sequential_read_speed}")
#print(f"Sequential write speed: {sequential_write_speed}")
#print(f"Stride read speed: {stride_read_speed}")
