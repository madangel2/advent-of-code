from utils import get_data
from utils.graphUtils import reverse_graph, find_all_reachable_nodes, count_all_paths
from collections import defaultdict, deque

def parse_graph(data):
    graph = {}
    for line in data.strip().split('\n'):
        node, connections = line.split(': ')
        graph[node] = connections.split()
    return graph

def solve():
    data = get_data(11)
    graph = parse_graph(data)
    
    part1 = count_all_paths(graph, 'you', 'out')

    # Only checking 1 way seems to work
    part2 = count_all_paths(graph, 'svr', 'fft') * count_all_paths(graph, 'fft', 'dac') * count_all_paths(graph, 'dac', 'out')
    
    return part1, part2
