from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Read <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonRead")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1])
    output = lines.collect()
    spark.stop()