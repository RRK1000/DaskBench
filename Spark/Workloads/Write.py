from __future__ import print_function

import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

def write(line):
    outfile = open("write-output.txt", "w+")
    outfile.write(line)

conf = SparkConf().setAppName("PythonWrite")
sc = SparkContext(conf=conf)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Read <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonRead")\
        .getOrCreate()

    lines = sc.textFile(sys.argv[1]).map(write)
    output = lines.collect()
    spark.stop()