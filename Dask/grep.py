from Generators.gen_wc import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import pprint
import sys
import math
import re

if (len(sys.argv) < 3):
    print("USAGE ./grep.py <data size> <scheduler url>")
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

def find_key(data,key):
    results = []
    count = 0
    for line in data:
        a = re.findall(key,line)
        if (a != []):
            results.append([count,a])
        count += 1
    if (results!=[]):
        return results
    return None

for i in range(parallel_execs):
    if (i != parallel_execs -1):
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):int((i+1) * len(data_sentence)/parallel_execs)]
    else:
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):]
    futures_array.append(client.scatter(scatter_data))

for i in range(parallel_execs):
    delayed_array.append(delayed(find_key)(futures_array[i],'amet'))

results_array = compute(*delayed_array)
results_array = list(results_array)

final_result = list()
for index in range(len(results_array)):
    if (results_array[index] != None):
        for item in results_array[index]:
            item[0] = item[0] + int(index * len(data_sentence)/parallel_execs)
        final_result.extend(results_array[index])
print(final_result)
