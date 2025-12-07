from utils import get_data, parse_map, downMove, leftMove, rightMove

def move_tachyon(map, pos):
    new_pos = pos + downMove
    
    if not map.is_in_map(new_pos):
        return []
    elif map.get_item(new_pos) == "^":
        return [new_pos + leftMove, new_pos + rightMove]
    else:
        return [new_pos]
        

def solve():
    data = get_data(7)
    map = parse_map(data)
    tachyon_paths = {map.find_first_item("S"): 1}
    
    part1=0
    part2=0
    
    while len(tachyon_paths) > 0:
        new_tachyon_paths = {}
        
        for pos, path_count in tachyon_paths.items():
            new_positions = move_tachyon(map, pos)
            
            if len(new_positions) > 1:
                part1 += 1
            
            if len(new_positions) == 0:
                # This path exited the map
                part2 += path_count
            else:
                # Propagate the path count to each destination
                for new_pos in new_positions:
                    new_tachyon_paths[new_pos] = new_tachyon_paths.get(new_pos, 0) + path_count
        
        tachyon_paths = new_tachyon_paths

    
    return part1, part2
