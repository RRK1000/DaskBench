import random

def generate_data(size):
    data = []
    with open('/etc/dictionaries-common/words','r') as myfile:
        data = myfile.readlines()
    output = ""
    while (len(output) < size*1024*1024):
        output += "".join([ x for x in random.sample(data,1000)])
    return output
