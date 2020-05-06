from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: Union <file1> <file2>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonUnion")\
        .getOrCreate()

    df1 = spark.read.csv(sys.argv[1], inferSchema=True, header=True)
    df2 = spark.read.csv(sys.argv[2], inferSchema=True, header=True)
    df = df1.join(df2, on=['col-1'])
    spark.stop()