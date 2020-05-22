from Generators.gen_edges import generate_data
from dask import delayed,compute
from dask.distributed import Client
import sys
class Graph: 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
        visited[v] = True
        temp.append(v) 
        for i in self.adj[v]: 
            if visited[i] == False: 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    def addEdge(self, t): 
        self.adj[t[0]].append(t[1]) 
        self.adj[t[1]].append(t[0]) 
  
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 

if (len(sys.argv) < 3):
    print("USAGE ./connected_components.py <number of edges> <num vertices> <scheduler url>")
    exit(1)

num_edges = int(sys.argv[1])
num_vertices = int(sys.argv[2])
sched_IP = sys.argv[3]

data = generate_data(num_edges,num_vertices)
client = Client(sched_IP)

g = Graph(num_vertices)
for item in data:
    g.addEdge(item)

task = delayed(g.connectedComponents)
compute(task)
print("done")