
def cost_matrix(array,weight):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1:
                array[i][j]=weight[i]
            else:
                array[i][j]=100
        
    return array
    

def bellman_ford(graph, start):
    n_vertexes=graph.vcount()
    print(n_vertexes)
    dist = [float('inf')*n_vertexes]
    dist[start] = 0
    for _ in range(n_vertexes-1):
        for edge in graph.es:
            u=edge.source
            v=edge.target
            weight=edge['weight']
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for edge in graph.es:
        u = edge.source
        v = edge.target
        weight = edge["weight"]
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return dist