from utils import get_data

def merge_overlapping_ranges(ranges):
    if not ranges:
        return []
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    # Initialize result with the first range
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # Check if current range overlaps with the last merged range
        if current_start <= last_end:
            # Merge by extending the end of the last range
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as a new range
            merged.append((current_start, current_end))
    
    return merged

def solve():
    data = get_data(5).split("\n\n")
    ranges = merge_overlapping_ranges([tuple(map(int, r.split("-"))) for r in data[0].split("\n")])
    numbers = [int(number) for number in data[1].split("\n")]

    part1 = sum(any(r[0] <= n <= r[1] for r in ranges) for n in numbers)
    part2 = sum([r[1] - r[0] + 1 for r in ranges])
    
    return part1, part2
