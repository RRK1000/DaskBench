import lorem
import sys
import os

size = int(sys.argv[1]) - 1
inputfile = open("wc-input.txt", "w+")
while((os.stat("wc-input.txt").st_size / (1024*1024)) <= size):
    inputfile.write(lorem.sentence() + '\n')
inputfile.close()