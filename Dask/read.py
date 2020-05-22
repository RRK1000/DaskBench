from Generators.gen_wc import generate_data
from dask import delayed,compute
from dask.distributed import Client
import sys

if (len(sys.argv) < 3):
    print("USAGE ./read.py <data size> <scheduler url>")
    exit(1)
length_of_data = int(sys.argv[1])
sched_IP = sys.argv[2]

data = generate_data(length_of_data)
myfile = open("sample_file.txt",'w')
myfile.write(data)
myfile.close()

client = Client(sched_IP)

def read_from_file(filepointer):
    return filepointer

myfile = open("sample_file.txt",'r')
task = delayed(read_from_file)(myfile)
res = compute(task)
myfile.close()
print("done")