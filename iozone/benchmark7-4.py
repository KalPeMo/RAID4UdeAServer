
import subprocess

def get_iozone_speed(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Get the read and write speed
    speeds = output.split(',')
    # Print the size of speeds
    #size_of_speeds = len(speeds)
    #print(f"Size of speeds: {size_of_speeds}")
    #read_speed = speeds[0]
    #write_speed = speeds[1]

    # Get the rewrite, read reread, random read, and random write speed
    #rewrite_speed = speeds[2]
    #read_reread_speed = speeds[3]
    #random_read_speed = speeds[4]
    #random_write_speed = speeds[5]

    # Create 5 more variables
    #sequential_read_speed = speeds[6]
    #sequential_write_speed = speeds[7]
    #stride_read_speed = speeds[8]
    #stride_write_speed = speeds[9]
    #random_rw_speed = speeds[10]
    var20=speeds[20]
    var21=speeds[21]
    var22=speeds[22]
    var23=speeds[23]
    var24=speeds[24]
    var25=speeds[25]
    var26=speeds[26]
    var27=speeds[27]
    var28=speeds[28]
    var29=speeds[29]
    var30=speeds[30]
    #var31=speeds[31]
    #speeds = re.findall(r'(\d+) B/sec', output)


    #return read_speed, write_speed, rewrite_speed, read_reread_speed, random_read_speed, random_write_speed, sequential_read_speed, sequential_write_speed, stride_read_speed, stride_write_speed, random_rw_speed
    return var30, var29, var28, var27, var26, var25, var24, var23, var22, var21, var20


var30, var29, var28, var27, var26, var25, var24, var23, var22, var21, var20 = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

    #return read_speed, write_speed, rewrite_speed, read_reread_speed, random_read_speed, random_write_speed, sequential_read_speed, sequential_write_speed, stride_read_speed, stride_write_speed, random_rw_speed = get_iozone_speed("sudo iozone -a -i 0 -i 1 -s 1M -r 4k -I -f /dev/md0")

print(f"var20: {var20}")
print(f"var21: {var21}")
print(f"var22: {var22}")
print(f"var23: {var23}")
print(f"var24: {var24}")
print(f"var25: {var25}")
print(f"var26: {var26}")
print(f"var27: {var27}")
print(f"var28: {var28}")
print(f"var29: {var29}")


#print(f"Read speed: {read_speed}")
#print(f"Write speed: {write_speed}")
#print(f"Rewrite speed: {rewrite_speed}")
#print(f"Read reread speed: {read_reread_speed}")
#print(f"Random read speed: {random_read_speed}")
#print(f"Random write speed: {random_write_speed}")
#print(f"Sequential read speed: {sequential_read_speed}")
#print(f"Sequential write speed: {sequential_write_speed}")
#print(f"Stride read speed: {stride_read_speed}")
#print(f"Stride write speed: {stride_write_speed}")
#print(f"Random rw speed: {random_rw_speed}")
