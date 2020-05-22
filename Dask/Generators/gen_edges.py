import random

def generate_data(numberofedges,numvertices):
    result = []
    for i in range(numberofedges):
        edge = (random.randint(1,numvertices-1),random.randint(1,numvertices-1))
        while (edge[0] != edge[1] and edge in result):
            edge = (random.randint(1,numvertices),random.randint(1,numvertices))
        result.append(edge)
    return result