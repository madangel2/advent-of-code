from utils import parse_map, MapGraph, simpleMoves, get_absolute_diff, get_data

def init_graph(map, cheats):
    map_graph = MapGraph()
    
    for pos, item in map.items():
        if item == "#" and pos not in cheats:
            continue
        
        for move in simpleMoves:
            neighbor_pos = pos + move
            if neighbor_pos in map and (map[neighbor_pos] != "#" or neighbor_pos in cheats):
                map_graph.addEdge(pos, neighbor_pos, 1)     
                        
    return map_graph

def countCheatScoresBoth(map, base_lowest_scores, base_score, path, max_cheat_length, reverse_end_scores, min_score=100, part1_max_length=2):
    part1_count = 0
    part2_count = 0
    
    # Pre-compute all (offset, distance) pairs once
    offset_distance_pairs = []
    for dx in range(-max_cheat_length, max_cheat_length + 1):
        abs_dx = abs(dx)
        remaining = max_cheat_length - abs_dx
        for dy in range(-remaining, remaining + 1):
            offset_distance_pairs.append((complex(dx, dy), abs_dx + abs(dy)))
    
    # Main loop
    for pos in path:
        current_step = base_lowest_scores[pos]
        
        for offset, cheat_length in offset_distance_pairs:
            cheat_end_pos = pos + offset
            
            # Skip if not reachable
            if cheat_end_pos not in reverse_end_scores:
                continue
            
            dist_to_end = reverse_end_scores[cheat_end_pos]
            cheat_score = base_score - (current_step + cheat_length + dist_to_end)
            
            if cheat_score >= min_score:
                part2_count += 1
                if cheat_length <= part1_max_length:
                    part1_count += 1

    return part1_count, part2_count

# Init challenge
def solve():
    data = get_data(20)
    map = parse_map(data)
    start_pos = map.find_first_item("S")
    end_pos = map.find_first_item("E")

    base_graph = init_graph(map.map, [])
    base_lowest_scores, path = base_graph.getLowestScores(start_pos)
    reverse_end_scores, reverse_path = base_graph.getLowestScores(end_pos)
    base_score = base_lowest_scores[end_pos]

    # Calculate both parts in a single pass
    part1, part2 = countCheatScoresBoth(map, base_lowest_scores, base_score, path[end_pos], 20, reverse_end_scores)
    
    return part1, part2