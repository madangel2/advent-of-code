from utils import get_data, parse_map, ComplexMap

def calculate_paper_to_be_removed(map: ComplexMap, removed: set):    
    new_removed = set()
    for position in map.get_all_positions():
        if map.get_item(position) == "." or position in removed:
            continue
        
        neighbor_count = sum(
            1 for neighbor in map.get_neighbors(position)
            if map.get_item(neighbor) == "@" and neighbor not in removed
        )
        
        if neighbor_count < 4:
            new_removed.add(position)

    return new_removed

def solve():
    data = get_data(4)
    map = parse_map(data)

    part1 = 0
    part2 = 0

    removed = set()
    new_removed = calculate_paper_to_be_removed(map, removed)
    part1 = len(new_removed)
    while len(new_removed) > 0:
        removed.update(new_removed)
        new_removed = calculate_paper_to_be_removed(map, removed)
    
    part2 = len(removed)
    
    return part1, part2
