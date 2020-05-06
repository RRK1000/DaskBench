from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Project <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonProject")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], inferSchema=True, header=True)
    df.select([c for c in df.columns if c in ['col1']])
    spark.stop()