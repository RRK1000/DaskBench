# Spark workloads require the following to be installed
# Spark version >= 1.2
# Java 8
# Python 2.7 (initial release) 

# Sort

read -p "Enter data size in MB: " size

python Gens/genSort.py $size

spark-submit Workloads/Sort.py sort-input.txt

rm sort-input.txt

# Grep
# Wordcount

# python3 Wordcount.py ../Data/WC.txt

# MD5
# Connected Components
# RandSample
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