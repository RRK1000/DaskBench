import lorem
import sys
import os

def generate_data(size):
    data = ''
    while((len(data) / (1024*1024)) <= size):
        data += lorem.sentence() + '\n'
    with open("wcfile.txt",'w') as myfile:
        myfile.write(data)
    return data
#generate_data(10)