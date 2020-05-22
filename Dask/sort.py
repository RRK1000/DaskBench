from Generators.gen_wordlist import generate_data
from dask import delayed,compute
from dask.distributed import Client
import sys

if (len(sys.argv) < 3):
    print("USAGE ./sort.py <num words> <scheduler url>")
    exit(1)

num_words = int(sys.argv[1])
sched_IP = sys.argv[2]

data = generate_data(num_words)

client = Client(sched_IP)
result = [ x for x in data.split("\n") if x != '' ] 

def sort(data):
    content = data.split("\n")
    return "\n".join(sorted(content))

future = client.scatter(data)
task = delayed(sort)(future)
output = compute(task)
print("Done")
