from vertex import Vertex

class Graph(object):
    
    def __init__(self,directed=False):
        self._vertexes={}
        self._directed=directed
        
    def add_vertex(self,key):
        vertex=Vertex(key)
        self._vertexes[key]=vertex
        
        return vertex
            
    def insert_edge(self,fromk, to, weight=0):
        if fromk not in self._vertexes:
            self.add_vertex(fromk)
        if to not in self._vertexes:
            self.add_vertex(to)
            
        self._vertexes[fromk].insert_neighbor(self._vertexes[to], weight)
        
        if not self._directed:
            self._vertexes[to].insert_neighbor(self._vertexes[fromk], weight)
    
        return list(self.adj.keys())
    
  
    

edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

graph=Graph(edges)

print(graph.adj)