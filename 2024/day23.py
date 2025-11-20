from utils import get_data
from collections import defaultdict
from itertools import combinations

def find_all_cliques_3(graph):
    all_nodes = list(graph.keys())
    cliques = []

    for combo in combinations(all_nodes, 3):
        a, b, c = combo
        if (b in graph[a] and c in graph[a] and c in graph[b]):
            cliques.append(list(combo))

    return cliques


def find_all_max_cliques(graph):    
    def bron_kerbosch(current_clique, candidates, excluded, cliques):
        if not candidates and not excluded:
            cliques.append(sorted(current_clique))
            return
        
        for node in list(candidates):
            neighbors = graph[node]
            bron_kerbosch(
                current_clique | {node},
                candidates & neighbors,
                excluded & neighbors,
                cliques
            )
            candidates.remove(node)
            excluded.add(node)
    
    cliques = []
    all_nodes = set(graph.keys())
    bron_kerbosch(set(), all_nodes, set(), cliques)
    return cliques

data = get_data(23)

connections = data.splitlines()
connections_graph = defaultdict(set)
for conn in connections:
    node1, node2 = conn.split('-')
    connections_graph[node1].add(node2)
    connections_graph[node2].add(node1)

cliques_3 = find_all_cliques_3(connections_graph)
cliques_3_t = [c for c in cliques_3 if any(e.startswith("t") for e in c)]

max_cliques = find_all_max_cliques(connections_graph)
largest_clique = max(max_cliques, key=len)
password =  ",".join(largest_clique)

print(f"Part 1: {len(cliques_3_t)}")
print(f"Part 2: {password}")