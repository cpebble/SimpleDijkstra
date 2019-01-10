from math import sqrt, inf
from draw import drawDijkstraGraph
from time import sleep


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = inf
        self.predecessor = None
        self.adj = []
    def __str__(self):
        return f"x: {self.x}\t y: {self.y}\t adj: {self.adj}"
    
    def calc_adjacent(self, edges):
        for (u,v) in edges:
            if self == u:
                self.adj += [v]
            if self == v:
                self.adj += [u]

    def get_path_to_root(self):
        path = []
        a = self 
        while True:
            path +=[a]
            if a.predecessor == None:
                break
            a = a.predecessor
        return path

    @classmethod
    def get_min_dist(self, V):
        # min_dist = inf
        # n = None
        # for v in V:
        #     if v.dist < min_dist:
        #         min_dist = v.dist 
        #         n = v
        n = sorted(V, key=lambda x: x.dist)[0]
        return n
    

def distance(x1, x2, y1, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2-y1)**2))


def W(u, v):
    return distance(v.x, u.x, v.y, u.y)

def init_ss(V,s:Node):
    s.dist = 0
    Q = [v for v in V]
    return Q

def relax(u,v,w):
    """ If distance to v is greater than distance to u + distance from u to v then update v.dist"""
    if v.dist > w(u,v) + u.dist:
        v.dist = w(u,v) + u.dist
        v.predecessor = u

def dijkstra(V, E, s, t):
    """ Takes V: vertices, E: edges, s: source node, t: target node """ 
    Q = init_ss(V, s)
    S = []
    while len(Q) > 0:
        u = Node.get_min_dist(Q) 
        uIndex = Q.index(u) 
        del Q[uIndex]
        S += [u]
        if u == t:
           break
        for v in u.adj:
            relax(u,v,W)
            drawDijkstraGraph(V, E, u.get_path_to_root() , (u, v))
                   

