# DaskBench

Benchmark Suite using Dask

## Dask Benchmarks

## Hadoop Benchmarks

## Spark Benchmarks

These benchmarks are compiled using pyspark on Spark 2.6.

Requirements:
- Spark >= 2.4.5
- Python >= 2.7
- Pyspark
- Lorem >= 1.3.1

To replicate
```
bash run.sh
```

This compiles all workloads. Specific workloads can be run by commenting out the needful in the run.sh file. Additional parameters for generators can be tweaked in the Gens folder. The workloads can be tweaked under the Workloads/ folder for maximum efficiency on the user setup.