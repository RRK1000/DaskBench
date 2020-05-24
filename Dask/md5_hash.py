from Generators.gen_wc import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import pprint
import sys
import math

if (len(sys.argv) < 3):
    print("USAGE ./md5_hash.py <data size> <scheduler url>")
    exit(1)
length_of_data = int(sys.argv[1])
sched_IP = sys.argv[2]

data = generate_data(length_of_data)
data_sentence = data.split("\n")

client = Client(sched_IP)
futures_array = []
delayed_array = []
results_array = []
parallel_execs = math.ceil(length_of_data / 128)

def hasher(data):
    result = []
    for line in data:
        result.append(hash(line))
    return result

for i in range(parallel_execs):
    if (i != parallel_execs -1):
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):int((i+1) * len(data_sentence)/parallel_execs)]
    else:
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):]
    futures_array.append(client.scatter(scatter_data))

for i in range(parallel_execs):
    delayed_array.append(delayed(hasher)(futures_array[i]))

results_array = compute(*delayed_array)
results_array = list(results_array)
final_result = list()
for index in range(len(results_array)):
    final_result.extend(results_array[index])
print(final_result)