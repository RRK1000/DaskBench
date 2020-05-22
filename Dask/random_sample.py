from Generators.gen_wordlist import generate_data
from dask import delayed,compute
from dask.distributed import Client
import sys
import random

if (len(sys.argv) < 4):
    print("USAGE ./random_sample.py <num words in set> <number of samples> <scheduler url>")
    exit(1)

num_words_total = int(sys.argv[1])
num_samples = int(sys.argv[2])
sched_IP = sys.argv[3]

data = generate_data(num_words_total)

client = Client(sched_IP)

def sample(data,number):
    content = data.split("\n")
    return "\n".join(random.sample(content,number))

future = client.scatter(data)
task = delayed(sample)(future,num_samples)
output = compute(task)
print(output)
print("Done")
