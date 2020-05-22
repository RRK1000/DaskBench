import lorem
import sys
import os
import random

def generate_data(filename,rows,cols, col_offset):
    inputfile = open(filename+ ".csv", "w+")
    for i in range(rows):
        for j in range(col_offset,cols+ col_offset):
            if i == 0:
                if (j == cols + col_offset -1):
                    inputfile.write("col-" + str(j))
                else:
                    inputfile.write("col-" + str(j) + ",")
            else:
                if (j == 0):
                    inputfile.write(str(random.randint(1,1000))+",")
                    continue
                if (j == cols + col_offset -1):
                    inputfile.write(lorem.sentence())
                else:
                    inputfile.write(lorem.sentence() + ",")
        inputfile.write("\n")
    inputfile.close()