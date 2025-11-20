from utils import get_data
from mapUtilsComplex import parse_map, MapGraph, simpleMoves, get_absolute_diff

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

def getAllCheatScores(map, base_lowest_scores, base_score, path, max_cheat_length):
    cheat_scores = {}

    for pos in path:
        current_step = base_lowest_scores[pos]
        for cheat_end_pos in map.get_all_positions_in_radius(pos, max_cheat_length, True):
            cheat_length = get_absolute_diff(pos, cheat_end_pos)
            dist_to_end = reverse_end_scores[cheat_end_pos]
            cheat_score = base_score - (current_step + cheat_length + dist_to_end)
            cheat_scores[(pos,cheat_end_pos)] = cheat_score

    return cheat_scores

# Init challenge
data = get_data(20)
map = parse_map(data)
start_pos = map.find_first_item("S")
end_pos = map.find_first_item("E")

base_graph = init_graph(map.map, [])
base_lowest_scores, path = base_graph.getLowestScores(start_pos)
reverse_end_scores, reverse_path = base_graph.getLowestScores(end_pos)
base_score = base_lowest_scores[end_pos]

cheat_scores2 = getAllCheatScores(map, base_lowest_scores, base_score, path[end_pos], 2)
cheat_scores20 = getAllCheatScores(map, base_lowest_scores, base_score, path[end_pos], 20)

print(f'Part1: {sum([1 for score in cheat_scores2.values() if score >= 100])}')
print(f'Part2: {sum([1 for score in cheat_scores20.values() if score >= 100])}')