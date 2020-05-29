from Generators.gen_wc import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import pprint
import sys
import math

if (len(sys.argv) < 4):
    print("USAGE ./wordcount.py <data size> <scheduler url> <validate? 0-F 1-T>")
    exit(1)
length_of_data = int(sys.argv[1])
sched_IP = sys.argv[2]
validate = sys.argv[3]

#data = generate_data(length_of_data)
data = None
with open("wcfile.txt",'r') as myfile:
    data = myfile.read()
data_sentence = data.split("\n")
result = None
if (validate == 1):
    data_words = []
    [data_words.extend(x.split(" ")) for x in data_sentence]
    result = defaultdict(int)

    for word in data_words:
        result[word]+= 1

client = Client(sched_IP)
futures_array = []
delayed_array = []
results_array = []
parallel_execs = math.ceil(length_of_data / 128)

def wordcount(data):
    result = defaultdict(int)
    data_words = []
    [data_words.extend(x.split(" ")) for x in data]
    for word in data_words:
        result[word]+=1
    return result

for i in range(parallel_execs):
    if (i != parallel_execs -1):
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):int((i+1) * len(data_sentence)/parallel_execs)]
    else:
        scatter_data = data_sentence[int(i*len(data_sentence)/parallel_execs):]
    futures_array.append(client.scatter(scatter_data))

for i in range(parallel_execs):
    delayed_array.append(delayed(wordcount)(futures_array[i]))

results_array = compute(*delayed_array)
results_array = list(results_array)
final_result = defaultdict(int)
for index in range(len(results_array)):
    for item in results_array[index]:
        final_result[item] += results_array[index][item]
print(final_result)
if (validate == 1):
    if (final_result == result):
        print("valid")