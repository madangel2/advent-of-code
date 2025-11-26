from utils import get_data, parse_map, simpleMoves

def walk(map, current_position, current_direction_idx, obstacle_position=None):
    next_direction_idx = current_direction_idx
    new_position = current_position + simpleMoves[next_direction_idx]

    while map.is_in_map(new_position) and (map.get_item(new_position) == "#" or (obstacle_position and new_position == obstacle_position)):
            next_direction_idx = (next_direction_idx + 1) % 4
            new_position = current_position + simpleMoves[next_direction_idx]

    return new_position, next_direction_idx

def solve_part1(map, starting_position):
    current_position = starting_position
    current_direction_idx = 0

    visited_positions = set()
    path_with_directions = []
    
    while map.is_in_map(current_position):
        visited_positions.add(current_position)
        path_with_directions.append((current_position, current_direction_idx))
        current_position, current_direction_idx = walk(map, current_position, current_direction_idx)

    return visited_positions, path_with_directions  

def is_looping(map, start_state, new_obstacle, pre_visited):
    visited_positions_with_direction = set()
    current_position, current_direction_idx = start_state
    
    while map.is_in_map(current_position):
        current_position_and_direction = (current_position, current_direction_idx)
        
        if current_position_and_direction in visited_positions_with_direction:
            return True
            
        if current_position_and_direction in pre_visited:
            return True
        
        visited_positions_with_direction.add(current_position_and_direction)
        current_position, current_direction_idx = walk(map, current_position, current_direction_idx, new_obstacle)
    
    return False

def solve_part2(map, path_with_directions):
    valid_positions = set()
    visited_path_set = set()
    tested_obstacles = set()
    
    start_pos = path_with_directions[0][0]
    
    for i in range(len(path_with_directions) - 1):
        current_state = path_with_directions[i]
        current_pos = current_state[0]
        
        next_state = path_with_directions[i+1]
        candidate_pos = next_state[0]
        
        if candidate_pos == current_pos:
            visited_path_set.add(current_state)
            continue
            
        if candidate_pos == start_pos:
            visited_path_set.add(current_state)
            continue
            
        if candidate_pos in tested_obstacles:
            visited_path_set.add(current_state)
            continue
            
        tested_obstacles.add(candidate_pos)
        
        if is_looping(map, current_state, candidate_pos, visited_path_set):
            valid_positions.add(candidate_pos)
        
        visited_path_set.add(current_state)
            
    return valid_positions

def solve():
    data = get_data(6)
    map = parse_map(data)
    startingPosition = map.find_first_item("^")
    visitedPositions, path_with_directions = solve_part1(map, startingPosition)
    possiblePositions = solve_part2(map, path_with_directions)

    part1 = len(visitedPositions)
    part2 = len(possiblePositions)

    return part1, part2
    





