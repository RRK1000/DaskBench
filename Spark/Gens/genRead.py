import lorem
import sys
import os

size = int(sys.argv[1]) - 1
inputfile = open("read-input.txt", "w+")
while((os.stat("read-input.txt").st_size / (1024*1024)) <= size):
    inputfile.write(lorem.sentence() + '\n')
inputfile.close()