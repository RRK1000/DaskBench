from __future__ import print_function
import sys
import os
import lorem


from pyspark.sql import SparkSession

text = lorem.sentence()

def check(line):
    if text in line:
        print("Grepped output")

def grep(rdd):
    rdd.foreach(lambda record: check(record[0]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: grep <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonGrep")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    sortedCount = lines.map(lambda x: grep(x, text))
    print(text)
    # output = sortedCount.collect()
    # for (num, unitcount) in output:
    #     print(num)

    spark.stop()