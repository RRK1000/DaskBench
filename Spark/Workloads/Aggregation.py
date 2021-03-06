from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Aggregation <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonAggregation")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], inferSchema=True, header=True)
    df.groupBy("col-1").max()
    spark.stop()