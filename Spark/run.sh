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

echo "\n----------------------------------------------------------------------------------------------------------------------------------------------\n"

echo "RUNNING RANDSAMPLE WORKLOAD"

read -p "Enter data size in MB: " size

python Gens/genRandSample.py $size

spark-submit Workloads/RandSample.py randsample-input.txt

rm randsample-input.txt

# FFT
# Matrix Multiplication
# Read
# Write
# Scan
# OrderBy
# Aggregation
# Project
# Filter
# Select
# Union