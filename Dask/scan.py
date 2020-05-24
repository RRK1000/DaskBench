from Generators.gen_csv import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import dask.dataframe as dd
import pprint
import sys
import dask

if (len(sys.argv) < 4):
    print("USAGE ./scan.py <file 1 size> <file 1 columns> <scheduler url>")
    exit(1)

file1 = (int(sys.argv[1]), int(sys.argv[2]))
sched_IP = sys.argv[3]
client = Client(sched_IP)

datafile1 = generate_data("file1",file1[0],file1[1],0)

def scan_data(file):
    output = []
    for i in range(len(file)):
        for line in file[1].split("\n"):
            output.append(line)
    return output

task = delayed(scan_data)(open("file1.csv"))
output = compute(task)
print(output)