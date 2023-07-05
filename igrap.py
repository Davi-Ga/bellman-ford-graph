import matplotlib.pyplot as plt
import igraph as ig
import random
import numpy as np
from helpers import cost_matrix,bellman_ford

graph=ig.Graph.Erdos_Renyi(10, p=0.5, directed=False)

graph.es['weight']=[random.randint(1, 5) for _ in range(graph.ecount())]


array_adj=np.array(graph.get_adjacency().data)
np.savetxt('data/graph10_adjacency.csv', array_adj, delimiter=',', fmt='%.2f')


array_wgt=np.array(graph.es['weight'])
c=cost_matrix(array_adj,array_wgt)
np.savetxt('data/graph10_cost.csv', c, delimiter=',', fmt='%d')

fig,ax=plt.subplots(figsize=(8,8))
ig.plot(
    graph,
    target=ax,
    edge_label=graph.es['weight'],
    edge_label_size=8,
    vertex_size=0.3,
    vertex_color='purple',
    vertex_label=range(graph.vcount()),
    vertex_label_size=6,
)

print(bellman_ford(graph,0))

plt.show()
fig.savefig('images/graph50.png')

