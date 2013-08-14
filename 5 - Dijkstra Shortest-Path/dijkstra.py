#!/usr/bin/env python

from graph  import WeightedGraph
from priodict import PriorityDict
 
def dijkstra(graph, start, end):
    heap        = PriorityDict({ v: float("inf") for v in graph })
    heap[start] = 0
    distance    = { }
    
    for v in heap:
        distance[v] = heap[v]
        if v is end: return distance

        for w in graph[v]:
            len_vw = distance[v] + graph[v][w]
            heap[w] = min(heap[w], len_vw) if w in heap else len_vw

    return distance

def read_weighted_graph_file(path):
    lines = [ [ tuple.split(",") for tuple in line.split() ] \
              for line in open(path).readlines() ]

    graph = WeightedGraph(len(lines))
    for line in lines:
        v = int(line[0][0]) - 1
        for edge in line[1:]:
            w    = int(edge[0]) - 1
            cost = int(edge[1])
            graph.add_edge(v, w, cost)
            graph.add_edge(w, v, cost)

    return graph

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file",  help = "the graph file", type = str)
    parser.add_argument("start", help = "the start node", type = int)
    parser.add_argument("end",   help = "the destination node", type = int)
    args = parser.parse_args()

    graph     = read_weighted_graph_file(args.file)
    distances = dijkstra(graph, args.start - 1, args.end - 1)

    print("Distance from", args.start,
          "to", args.end,
          "is:", distances[args.end - 1])
