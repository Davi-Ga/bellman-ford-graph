import matplotlib.pyplot as plt
import igraph as ig
import numpy as np

def cost_matrix(array,weight):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1:
                array[i][j]=weight[i]
            else:
                array[i][j]=100
        
    return array

def plot_graph(graph):
    fig,ax=plt.subplots(figsize=(8,8))
    ig.plot(
        graph,
        target=ax,
        edge_label=graph.es['weight'],
        edge_width=1,
        edge_label_size=8,
        vertex_size=0.3,
        vertex_color='purple',
        vertex_label=range(graph.vcount()),
        vertex_label_size=6,
    )
    plt.show()
    fig.savefig('images/graph100.png')
    
    
def plot_path(graph):
    
    #Primeiro parâmetro indica o vértice de origem e o segundo o vértice de destino
    result=graph.get_shortest_paths(
        0,5,
        weights=graph.es["weight"], 
        output="epath"
    )
    
    fig,ax=plt.subplots(figsize=(8,8))
    ig.plot(
        graph,
        target=ax,
        edge_label=graph.es['weight'],
        edge_width=[4 if i in result[0] else 1 for i in range(graph.ecount())],
        edge_label_size=8,
        vertex_size=0.3,
        vertex_color='purple',
        vertex_label=range(graph.vcount()),
        vertex_label_size=6,
        
    )
    plt.show()
    fig.savefig('images/graph_path100.png')

def matrix_adj_and_cost(graph):
    array_adj=np.array(graph.get_adjacency().data)
    np.savetxt('data/graph100_adjacency.csv', array_adj, delimiter=',', fmt='%d')
    
    array_wgt=np.array(graph.es['weight'])
    c=cost_matrix(array_adj,array_wgt)
    np.savetxt('data/graph100_cost.csv', c, delimiter=',', fmt='%d')
    