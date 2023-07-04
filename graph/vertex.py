class Vertex:
    
    def __init__(self, key):
        self._key = key
        self._neighbors = {}
        self._distance = 0
        self._visited = False
        self._ancestor = None
        
        
    def get_key(self):
        return self._key
    
    def insert_neighbor(self, to=None, weight=0):
        self._neighbors[to] = weight
    
    def get_neighbors(self):
        return self._neighbors.keys()
    
    def set_distance(self, distance):
        self._distance = distance
    
    def get_distance(self):
        return self._distance
    
    def set_visited(self):
        self._visited = True
        
    def get_visited(self):
        return self._visited
    
    def get_weight(self, to):
        return self._neighbors[to]

    def set_ancestor(self, ancestor):
        self._ancestor = ancestor
        
    def get_ancestor(self):
        return self._ancestor
    
    def __str__(self):
        return str(self._key) + ' connected to: ' + str([x.get_key() for x in self._neighbors])