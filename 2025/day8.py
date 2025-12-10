import math
from utils import get_data

def find_all_closest_pairs(points, max_pairs=None):
    # Pre-compute all pairwise distances once
    all_pairs_with_distances = []
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = math.dist(points[i], points[j])
            all_pairs_with_distances.append(((points[i], points[j]), distance))
    
    # Sort by distance
    all_pairs_with_distances.sort(key=lambda x: x[1])
    
    # Select pairs without reuse and build circuits as we go
    used_pairs = set()
    circuits = []  # List of sets, each representing a circuit
    
    last_pair_key = None
    for pair, distance in all_pairs_with_distances:
        if max_pairs is not None and len(used_pairs) >= max_pairs:
            break
        elif len(circuits) == 1 and len(circuits[0]) == len(points):
            break
        
        pair_key = tuple(sorted([pair[0], pair[1]]))
        if pair_key not in used_pairs:
            used_pairs.add(pair_key)
            last_pair_key = pair_key
            
            # Find circuits that contain either point in the pair
            matching_circuits = []
            for i, circuit in enumerate(circuits):
                if pair[0] in circuit or pair[1] in circuit:
                    matching_circuits.append(i)
            
            if not matching_circuits:
                # No existing circuit contains these points, create a new one
                circuits.append(set(pair))
            elif len(matching_circuits) == 1:
                # One circuit contains one of the points, add both to it
                circuits[matching_circuits[0]].update(pair)
            else:
                # Multiple circuits contain these points, merge them
                merged_circuit = set(pair)
                for i in sorted(matching_circuits, reverse=True):
                    merged_circuit.update(circuits[i])
                    circuits.pop(i)
                circuits.append(merged_circuit)
    
    return [(list(c), len(c)) for c in circuits], last_pair_key

def solve():
    data = get_data(8)
    points = sorted([tuple(map(int, line.split(","))) for line in data.split("\n")])
    
    # Part1
    circuits = find_all_closest_pairs(points, max_pairs=1000)[0]
    ordered_circuits = sorted(circuits, key=lambda x: x[1], reverse=True)
    part1 = ordered_circuits[0][1] * ordered_circuits[1][1] * ordered_circuits[2][1]
    
    # Part2 (Not very efficient but still under 1 second)
    last_pair_key = find_all_closest_pairs(points)[1]
    part2 = last_pair_key[0][0] * last_pair_key[1][0]
    
    return part1, part2

