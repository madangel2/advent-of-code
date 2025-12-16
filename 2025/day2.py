from utils import get_data
from bisect import bisect_left, bisect_right

def generate_part1_nums(max_val):
    candidates = []
    max_s = str(max_val)
    max_len = len(max_s)
    
    # Iterate through even lengths 2, 4, 6...
    for length in range(2, max_len + 1, 2):
        half_len = length // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        
        for i in range(start, end):
            s = str(i)
            # Create palindrome-like repetition: "123" -> "123123"
            cand_s = s + s
            cand = int(cand_s)
            if cand > max_val:
                break
            candidates.append(cand)
            
    return candidates

def generate_part2_nums(max_val):
    candidates = set()  # Use set to avoid duplicates (e.g., '1111' from '1'x4 and '11'x2)
    max_s = str(max_val)
    max_len = len(max_s)
    
    # Iterate through all possible lengths of the final number
    for length in range(1, max_len + 1):
        # Iterate through possible lengths of the repeating unit (seed)
        # Seed length must be a proper divisor of total length
        for seed_len in range(1, length // 2 + 1):
            if length % seed_len == 0:
                repeats = length // seed_len
                start = 10**(seed_len - 1)
                end = 10**seed_len
                
                for i in range(start, end):
                    s = str(i)
                    cand_s = s * repeats
                    cand = int(cand_s)
                    
                    if cand > max_val:
                        break
                    candidates.add(cand)
                    
    return sorted(list(candidates))

def count_in_range(candidates, lower, upper):
    # Find indices in sorted list
    start_idx = bisect_left(candidates, lower)
    end_idx = bisect_right(candidates, upper)
    return sum(candidates[start_idx:end_idx])

def solve():
    data = get_data(2)

    # Pre-parse ranges to find global max
    ranges = []
    global_max = 0
    
    for range_string in data.split(","):
        lower, upper = map(int, range_string.split("-"))
        ranges.append((lower, upper))
        if upper > global_max:
            global_max = upper
            
    # Generate all valid numbers up to the largest upper bound
    part1_cands = generate_part1_nums(global_max)
    part2_cands = generate_part2_nums(global_max)
    
    part1 = 0
    part2 = 0
    
    for lower, upper in ranges:
        part1 += count_in_range(part1_cands, lower, upper)
        part2 += count_in_range(part2_cands, lower, upper)
    
    return part1, part2
