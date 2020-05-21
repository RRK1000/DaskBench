import lorem
import sys
import os

size = int(sys.argv[1]) - 1
inputfile = open("grep-input.txt", "w+")
while((os.stat("grep-input.txt").st_size / (1024*1024)) <= size):
    inputfile.write(lorem.sentence() + '\n')
inputfile.close()