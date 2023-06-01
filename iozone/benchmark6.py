import subprocess
import pexpect
import re
import sys
import os.path
import subprocess
import csv
import datetime
import getpass

# Get the disk from the command line arguments
if len(sys.argv) > 1:
    disk = sys.argv[1]
else:
    disk = '/dev/sda'  # Default disk if none is specified

# Check if the disk file exists
if not os.path.exists(disk):
    print(f"The disk {disk} does not exist.")
    sys.exit(1)



# Define the test parameters
file_sizes = ['4M', '8M', '16M']  # File sizes
block_sizes = ['4k', '8k', '16k']  # Block sizes

# Name of the CSV file to store the results
csv_file = 'benchmark_results.csv'

# Get the current timestamp and username
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
username = getpass.getuser()

# Open the CSV file in append mode
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # Run the tests with different combinations of parameters
    total_tests = len(file_sizes) * len(block_sizes)
    current_test = 1

    for file_size in file_sizes:
        for block_size in block_sizes:
            # Print test information to the console
            print(f"Starting test {current_test} of {total_tests}...")
            print(f"Specifications: File size: {file_size}, Block size: {block_size}")

            # Get the start time of the test
            start_time = datetime.datetime.now()
            # Run the performance test using iozone and the specified disk
            command = f"iozone -a -i 0 -i 1 -s {file_size} -r {block_size} -I -f {disk}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Get the output of the test
            output = result.stdout

            # Get the test results
            read_speed = re.findall(r'\s+read\s+(\d+\.\d+)', output)[0]
            write_speed = re.findall(r'\s+write\s+(\d+\.\d+)', output)[0]

            # Print the test results to the console
            print("Test results:")
            print(f"Read speed: {read_speed}")
            print(f"Write speed: {write_speed}")


            # Get the end time of the test and calculate the elapsed time
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time

            # Write the results to the CSV file
            writer.writerow([timestamp, username, file_size, block_size, read_speed, write_speed, str(elapsed_time)])

            # Print test completion information to the console
            print(f"Finished test {current_test} of {total_tests}. Time elapsed: {elapsed_time}\n")

            current_test += 1

print("Performance tests complete. Results have been saved to the CSV file.")
