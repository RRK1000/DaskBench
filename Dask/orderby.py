from Generators.gen_csv import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import dask.dataframe as dd
import pprint
import sys
import math
import dask

if (len(sys.argv) < 4):
    print("USAGE ./orderby.py <file 1 size> <file 1 columns> <scheduler url>")
    exit(1)

file1 = (int(sys.argv[1]), int(sys.argv[2]))
sched_IP = sys.argv[3]
client = Client(sched_IP)
datafile1 = generate_data("file1",file1[0],file1[1],0)
dataframe1 = dd.read_csv("file1.csv")
dataframe1.set_index('col-1')
dataframe1.compute()
print(dataframe1)