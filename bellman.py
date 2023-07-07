
def bellman_ford(graph, start):
    dist = [float('inf')]*graph.vcount()
    dist[start] = 0
    
    for _ in range(graph.vcount()-1): ##n^1
        for edge in graph.es: ##n^2
            u=edge.source
            v=edge.target
            weight=edge['weight']
         
            if dist[u] !=float('inf') and dist[u] + weight < dist[v]: ##
                dist[v] = dist[u] + weight

    for edge in graph.es:
        u = edge.source
        v = edge.target
        weight = edge["weight"]
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return dist