import igraph as ig
import random
from helpers import plot_graph,plot_path,matrix_adj_and_cost
from bellman import bellman_ford

class Main:
    
    def __init__(self):
        pass
    
    graph=ig.Graph.Erdos_Renyi(100, p=0.08, directed=False)

    graph.es['weight']=[random.randint(1, 5) for _ in range(graph.ecount())]

    plot_path(graph)
    plot_graph(graph)
  
    matrix_adj_and_cost(graph)
  
    distances=bellman_ford(graph,0)
    for i,distance in enumerate(distances):
        print(f"Distances from vertex 0 to {i}: {distance}")

if __name__ == '__main__':
    Main()