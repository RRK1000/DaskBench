import lorem
import sys
import os

rows = int(sys.argv[1])
cols = int(sys.argv[2])
inputfile = open("csv-input.csv", "w+")
for i in range(rows):
    for j in range(cols):
        if i == 0:
            inputfile.write("col-" + str(j) + ",")
        else:
            inputfile.write(lorem.sentence() + ",")
    inputfile.write("\n")
inputfile.close()