#!/usr/bin/env python

class UndirectedGraph:
    def __init__(self, vertices):
        if vertices < 0:
            raise ValueError("Number of Vertices must be nonnegative")

        self.adj_list = [ list() for v in range(0, vertices) ]

    def copy(self):
        from copy import deepcopy

        new_graph          = UndirectedGraph(0)
        new_graph.adj_list = deepcopy(self.adj_list)
        return new_graph

    def add_edge(self, v, w):
        if v < 0 or v >= self.vertices():
            raise IndexError()
        self.adj_list[v].append(w)

    def neighbors(self, v):
        if v < 0 or v >= self.vertices():
            raise IndexError()
        return self.adj_list[v]

    def vertices(self):
        return len(self.adj_list)

    def contract(self, v, w):
        self.adj_list[v]= [ x for x in self.adj_list[v] if x is not w ]

        for x in self.adj_list[w]:
            if x is not v:
                self.add_edge(v, x)
                self.adj_list[x] = [ v if z is w else z for z in self.adj_list[x] ]

        self.adj_list[w] = self.adj_list[-1]

        last = self.vertices() - 1
        for x in self.adj_list[w]:
            self.adj_list[x] = [ w if z is last else z for z in self.adj_list[x] ]

        self.adj_list.pop()

    def min_cut(self, iterations, display = True):
        import random

        def karger_cut(graph):
            while graph.vertices() > 2:
                v = random.randint(0, graph.vertices() - 1)
                w = random.choice(graph.neighbors(v))
                graph.contract(v, w)
            return len(graph.neighbors(0))

        minimum = float("inf")
        for i in range(0, iterations):
            # random.seed(i) # make it "easily predictable"
            mincut = karger_cut(self.copy())
            minimum = min(mincut, minimum)
            if display:
                print("Iteration", str(i), ":", str(mincut))

        return minimum


def read_graph_file(path):
    lines = [ [int(v) - 1 for v in line.split('\t')[:-1] ] \
              for line in open(path).readlines() ]

    graph = UndirectedGraph(len(lines))
    for line in lines:
        v = line[0]
        for w in line[1:]:
            graph.add_edge(v, w)

    return graph


if __name__ == '__main__':
    import argparse, math

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the graph file", type = str)
    parser.add_argument("-n", "--no_display", \
            help = "don't show progress of iterations", action = "store_false")
    parser.add_argument("-i", "--iterations", \
            help = "number of iterations to perform", type = int)
    args = parser.parse_args()

    graph = read_graph_file(args.file)
    if not args.iterations:
        args.iterations = int(graph.vertices() ** 2 * math.log(graph.vertices()))

    mincut = graph.min_cut(args.iterations, args.no_display)
    print("Minimum Cut length:", mincut)
