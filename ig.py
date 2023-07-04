import matplotlib.pyplot as plt
import igraph as ig
import random

graph=ig.Graph.Erdos_Renyi(10, p=0.4, directed=False)

graph.es['width']=[random.randint(1, 5) for _ in range(graph.ecount())]

fig,ax=plt.subplots(figsize=(8,8))
ig.plot(
    graph,
    target=ax,
    edge_label=graph.es['width'],
    edge_width=2,
    vertex_size=0.08,
    vertex_color='purple',
    vertex_label=range(graph.vcount()),
    vertex_label_size=6,
)

plt.show()

fig.savefig('images/graph-10.png')
print(graph.get_edgelist()[:10])

