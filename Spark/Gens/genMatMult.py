import sys
import os
import random

size = int(sys.argv[1])
inputfile = open("matrix-input.txt", "w+")
for i in range(size):
    for j in range(i):
        inputfile.write(str(random.randint(1, 100)) + ' ')
    inputfile.write("\n")
inputfile.close()