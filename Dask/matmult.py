import sys
import dask.array as da
from dask.distributed import Client

if (len(sys.argv) < 3):
    print("USAGE ./matmult.py <one dimension of matrix> <scheduler url>")
    exit(1)
number = int(sys.argv[1])
sched_IP = sys.argv[2]
client = Client(sched_IP)
a = da.random.random(number,number)
b = da.random.random(number,number)
a.dot(b).compute()