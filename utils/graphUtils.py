from collections import deque, defaultdict

def reverse_graph(graph):
    result = {}
    for node in graph:
        for neighbor in graph[node]:
            result.setdefault(neighbor, []).append(node)
    return result    

def find_all_reachable_nodes(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

def count_all_paths(graph, start, end):    
    forward_g = defaultdict(list, graph)
    reverse_g = defaultdict(list, reverse_graph(graph))

    # Only consider nodes that are on some path from start to end
    reachable_from_start = find_all_reachable_nodes(forward_g, start)
    reachable_from_end = find_all_reachable_nodes(reverse_g, end)
    relevant_nodes = reachable_from_start & reachable_from_end
    
    if start not in relevant_nodes or end not in relevant_nodes:
        return 0
    
    # Compute in-degree for topological sort
    in_degree = defaultdict(int)
    for node in relevant_nodes:
        for neighbor in forward_g[node]:
            if neighbor in relevant_nodes:
                in_degree[neighbor] += 1
    
    # DP: dp[node] = number of paths from start to node
    dp = defaultdict(int)
    dp[start] = 1
    
    # Process nodes in topological order (start with zero in-degree nodes)
    queue = deque(node for node in relevant_nodes if in_degree[node] == 0)
    while queue:
        node = queue.popleft()
        
        # Propagate path count to neighbors
        for neighbor in forward_g[node]:
            if neighbor in relevant_nodes:
                dp[neighbor] += dp[node]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    return dp[end]