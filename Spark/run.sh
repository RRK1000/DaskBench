# Spark workloads require the following to be installed
# Spark version >= 1.2
# Java 8
# Python 2.7 (initial release) 

# Sort

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING SORT WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genSort.py $size

# spark-submit Workloads/Sort.py sort-input.txt

# rm sort-input.txt

# Grep

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING GREP WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genGrep.py $size

# python Workloads/Grep.py grep-input.txt

# rm grep-input.txt

# Wordcount

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING WORDCOUNT WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genWC.py $size

# spark-submit Workloads/Wordcount.py wc-input.txt

# rm wc-input.txt

# MD5

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING MD5 WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genMD5.py $size

# spark-submit Workloads/MD5.py md5-input.txt

# rm md5-input.txt

# Connected Components

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING CONNECTED COMPONENTS WORKLOAD"

# spark-submit --packages graphframes:graphframes:0.3.0-spark2.0-s_2.11 Workloads/ConnectedComponents.py 

# RandSample

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING RANDSAMPLE WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genRandSample.py $size

# spark-submit Workloads/RandSample.py randsample-input.txt

# rm randsample-input.txt

# FFT

# Cannot implement in Spark due to non-existence of complex classes

# Matrix Multiplication

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING MATRIX MULTIPLICATION WORKLOAD"

# read -p "Enter Rows and Columns (Square): " size

# python Gens/genMatMult.py $size

# spark-submit Workloads/MatrixMultiplication.py matrix-input.txt matrix-output.txt

# rm matrix-input.txt matrix-output.txt

# Read

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING READ WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genRead.py $size

# spark-submit Workloads/Read.py read-input.txt

# rm read-input.txt

# Write

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING WRITE WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genWrite.py $size

# spark-submit Workloads/Write.py write-input.txt

# rm write-input.txt write-output.txt

# Scan

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING SCAN WORKLOAD"

# read -p "Enter data size in MB: " size

# python Gens/genScan.py $size

# spark-submit Workloads/Scan.py scan-input.txt

# rm scan-input.txt

# OrderBy

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING ORDERBY WORKLOAD"

# read -p "Enter rows: " rows

# read -p "Enter cols: " cols

# python Gens/genCSV.py $rows $cols

# spark-submit Workloads/OrderBy.py csv-input.csv

# rm csv-input.csv

# Aggregation

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING AGGREGATION WORKLOAD"

# read -p "Enter rows: " rows

# read -p "Enter cols: " cols

# python Gens/genCSV.py $rows $cols

# spark-submit Workloads/Aggregation.py csv-input.csv

# rm csv-input.csv

# Project

# echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

# echo "RUNNING PROJECT WORKLOAD"

# read -p "Enter rows: " rows

# read -p "Enter cols: " cols

# python Gens/genCSV.py $rows $cols

# spark-submit Workloads/Project.py csv-input.csv

# rm csv-input.csv

# Filter


echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

echo "RUNNING FILTER WORKLOAD"

read -p "Enter rows: " rows

read -p "Enter cols: " cols

python Gens/genCSV.py $rows $cols

spark-submit Workloads/Filter.py csv-input.csv

rm csv-input.csv

# Select
# Union