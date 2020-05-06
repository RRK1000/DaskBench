from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Select <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonSelect")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], inferSchema=True, header=True)
    df.createOrReplaceTempView("table1")
    df2 = spark.sql("SELECT * FROM table1").collect()
    spark.stop()