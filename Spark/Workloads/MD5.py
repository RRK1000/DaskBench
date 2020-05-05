from __future__ import print_function
import sys
import os

from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: MD5 <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonMD5")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    hashed = lines.map(lambda x: hash(x))
    output = hashed.collect()
    for num in output:
        print(num)

    spark.stop()