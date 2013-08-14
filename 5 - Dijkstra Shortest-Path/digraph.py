#!/usr/bin/env python

class WeightedDigraph:
    # internal representation of the adjacency list as a dictionary whose keys
    # are vertices and values are dictionaries of (destination, cost) pairs

    def __init__(self, vertices):
        if vertices < 0:
            raise ValueError("Number of Vertices must be nonnegative")

        self.verts = vertices
        self.adj_dict = { i : { } for i in range(self.verts) }

    def __getitem__(self, v):
        return self.adjacents(v)

    def __setitem__(self, v, adj):
        for w in adj:
            self.add_edge(v, w, adj[w])

    def __iter__(self):
        return iter(self.adj_dict.keys())

    def add_edge(self, v, w, cost):
        if v < 0 or v >= self.verts:
            raise IndexError()
        if w < 0 or w >= self.verts:
            raise IndexError()
        if cost < 0:
            raise ValueError("Edge costs must be nonnegative")

        self.adj_dict[v][w] = cost

    def vertices(self):
        return self.verts

    def adjacents(self, v):
        if v < 0 or v >= self.verts:
            raise IndexError()

        return self.adj_dict[v]

