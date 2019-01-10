from graph import Node, W, dijkstra
from random import Random
from draw import drawGraph, drawDijkstraGraph

rng = Random()
rng.seed = "A"
# Gen random nodes
NODECOUNT = 20
EXTRAEDGECOUNT = 2
MAXX, MAXY = 1000,1000


nodes = []
for i in range(NODECOUNT):
    nodes += [Node(rng.randint(0, MAXX), rng.randint(0, MAXY))]

edges = []
for i in nodes:
    while True:
        a = rng.choice(nodes)
        if a != i:
            break
    edges += [(i,a)]
for i in range(EXTRAEDGECOUNT):
    a, b = None, None
    while a == b and not (a,b) in edges:
        a, b = rng.choice(nodes), rng.choice(nodes)
    edges += [(a, b)]
for n in nodes:
    n.calc_adjacent(edges)
dijkstra(nodes, edges, nodes[0], nodes[-1])
drawDijkstraGraph(nodes,edges,nodes[-1].get_path_to_root())
input()