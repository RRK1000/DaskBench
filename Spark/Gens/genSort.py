import random
import sys
import os

size = int(sys.argv[1]) - 1
inputfile = open("sort-input.txt", "w+")
while((os.stat("sort-input.txt").st_size / (1024*1024)) <= size):
    inputfile.write(str(random.randint(1, 1000000)) + '\n')
inputfile.close()