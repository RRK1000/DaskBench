from pyspark import SQLContext, SparkContext
from graphframes.examples import Graphs
from graphframes import *
import random
import sys

sc = SparkContext()
sqlContext=SQLContext(sc)
sc.setCheckpointDir("/home/shaanzie/sparkchecks/")


v = sqlContext.createDataFrame([
  ("a", "Alice", 34),
  ("b", "Bob", 36),
  ("c", "Charlie", 30),
  ("d", "David", 29),
  ("e", "Esther", 32),
  ("f", "Fanny", 36),
  ("g", "Gabby", 60)
], ["id", "name", "age"])
# Edge DataFrame
e = sqlContext.createDataFrame([
  ("a", "b", "friend"),
  ("b", "c", "follow"),
  ("c", "b", "follow"),
  ("f", "c", "follow"),
  ("e", "f", "follow"),
  ("e", "d", "friend"),
  ("d", "a", "friend"),
  ("a", "e", "friend")
], ["src", "dst", "relationship"])
# Create a GraphFrame
g = GraphFrame(v, e)

result = g.connectedComponents()
result.select("id", "component").orderBy("component").show()