from Generators.gen_csv import generate_data
from dask import delayed,compute
from dask.distributed import Client
from collections import defaultdict
import dask.dataframe as dd
import pprint
import sys
import math
import dask

if (len(sys.argv) < 6):
    print("USAGE ./union.py <file 1 size> <file 1 columns> <file 2 size> <file 2 columns> <scheduler url>")
    exit(1)

file1 = (int(sys.argv[1]), int(sys.argv[2]))
file2 = (int(sys.argv[3]), int(sys.argv[4]))
sched_IP = sys.argv[5]
client = Client(sched_IP)
datafile1 = generate_data("file1",file1[0],file1[1],0)
datafile2 = generate_data("file2",file2[0],file2[1],0)

dataframe1 = dd.read_csv("file1.csv")
dataframe2 = dd.read_csv("file2.csv")
dataframe3 = dataframe1.merge(dataframe2, on=['col-1'])
dataframe3.compute()
pprint.pprint(dataframe3)