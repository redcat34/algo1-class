#!/usr/bin/env python

class Digraph:
    def __init__(self, vertices):
        if vertices < 0:
            raise ValueError("Number of Vertices must be nonnegative")

        self.verts = vertices
        self.adj_list = { i : [ ] for i in range(self.verts) }

    def add_edge(self, v, w):
        if v < 0 or v >= self.verts:
            raise IndexError()
        if w < 0 or w >= self.verts:
            raise IndexError()

        self.adj_list[v].append(w)

    def vertices(self):
        return self.verts

    def adjacents(self, v):
        if v < 0 or v >= self.verts:
            raise IndexError()

        return self.adj_list[v]


class KosarajuSCC:
    def __init__(self, digraph, reverse):
        self.dfs_loop(reverse)
        finish = self.finished_time_graph(digraph)
        self.dfs_loop(finish)

    def dfs_loop(self, graph):
        self.marked = set()
        self.finish = [None]  * graph.vertices()
        self.leader = [None]  * graph.vertices()

        self.time   = 0
        self.source = None

        for node in reversed(range(graph.vertices())):
            if node not in self.marked:
                self.source = node
                self.dfs(graph, node)

    def dfs(self, graph, node):
        self.marked.add(node)
        self.leader[node] = self.source
        for v in graph.adjacents(node):
            if v not in self.marked:
                self.dfs(graph, v)
        self.finish[node] = self.time
        self.time += 1

    def finished_time_graph(self, graph):
        finished_graph = Digraph(graph.vertices())
        for v in range(graph.vertices()):
            for w in graph.adjacents(v):
                finished_graph.add_edge(self.finish[v], self.finish[w])
        return finished_graph

    def leaders(self):
        return self.leader

def read_digraph_file(path):
    lines = open(path).readlines()

    digraph = Digraph(len(lines))
    reverse = Digraph(len(lines))

    for line in lines:
        edge = line.split()
        v = int(edge[0]) - 1
        w = int(edge[1]) - 1
        digraph.add_edge(v, w)
        reverse.add_edge(w, v)

    return digraph, reverse

def compute_stats(leaders, largest_n = 5):
    from collections import Counter

    counter = Counter(leaders)
    return [ x[1] for x in counter.most_common(largest_n) ]

if __name__ == '__main__':
    import argparse, resource, sys

    sys.setrecursionlimit(2 ** 20)
    resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the graph file", type = str)
    parser.add_argument("-n", "--number", help = "print the largest n scc", \
            type = int, default = 5)
    args = parser.parse_args()

    digraph, reverse = read_digraph_file(args.file)
    kosaraju = KosarajuSCC(digraph, reverse)
    
    largest = compute_stats(kosaraju.leaders(), args.number)
    print("The size of the", args.number, "largest SCCs are:", largest)
