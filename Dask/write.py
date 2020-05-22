from Generators.gen_wc import generate_data
from dask import delayed,compute
from dask.distributed import Client
import sys

if (len(sys.argv) < 3):
    print("USAGE ./write.py <data size> <scheduler url>")
    exit(1)
length_of_data = int(sys.argv[1])
sched_IP = sys.argv[2]

data = generate_data(length_of_data)

client = Client(sched_IP)

def write_to_file(data):
    with open("file.txt",'w') as myfile:
        myfile.write(data)

future = client.scatter(data)
task = delayed(write_to_file)(future)
compute(task)
print("done")