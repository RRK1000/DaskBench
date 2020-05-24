import lorem
import sys
import os

def generate_data(filename,size,cols, col_offset):
    if (os.path.exists(filename+".csv")):
        return
    inputfile = open(filename+ ".csv", "w")
    i = 0
    while (os.stat(filename+".csv").st_size < size*1024*1024):
        for j in range(col_offset,cols+ col_offset):
            if i == 0:
                if (j == cols + col_offset -1):
                    inputfile.write("col-" + str(j))
                else:
                    inputfile.write("col-" + str(j) + ",")
            else:
                if (j == cols + col_offset -1):
                    inputfile.write(lorem.sentence())
                else:
                    inputfile.write(lorem.sentence() + ",")
        inputfile.write("\n")
        inputfile.flush()
        i+=1
    inputfile.close()