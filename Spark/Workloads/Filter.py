from __future__ import print_function

import sys

from pyspark.sql import SparkSession
import pyspark.sql.functions as f


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Filter <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonFilter")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], inferSchema=True, header=True)
    df.filter((f.col('col-1') > 1))
    spark.stop()