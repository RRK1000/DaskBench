import random

def generate_data(num_words):
    data = []
    with open('/etc/dictionaries-common/words','r') as myfile:
        data = myfile.readlines()
    output = "".join([ x for x in random.sample(data,num_words)])
    return output
