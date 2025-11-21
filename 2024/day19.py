from collections import Counter
from utils import get_data

def can_form_pattern(pattern, towels):
    pattern_count = Counter(pattern)
    towels_count = Counter(''.join(towels))
    
    for char in pattern_count:
        if towels_count[char] < pattern_count[char]:
            return False
    return True

def count_combinations(pattern, towels):
    dp = [0] * (len(pattern) + 1)
    dp[0] = 1
    
    # Iterate over each possible length of the pattern
    for i in range(1, len(pattern) + 1):
        for towel in towels:
            if i >= len(towel) and pattern[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)]
    
    return dp[len(pattern)]

# Function to find all combinations of towels that form patterns
def find_combinations(towels, patterns):
    results = []
    
    # For each pattern, check if it can be formed with infinite towels
    for pattern in patterns:
        if can_form_pattern(pattern, towels):
            result = count_combinations(pattern, towels)
            results.append(result)
        else:
            # If the pattern can't be formed, return 0
            results.append(0)
    
    return results

# Init challenge
def solve():
    data = get_data(19)
    lines = data.splitlines()
    towels = lines[0].split(", ")
    patterns = lines[2:]

    pattern_combinations = find_combinations(towels, patterns)

    part1 = len([1 for r in pattern_combinations if r > 0])
    part2 = sum(pattern_combinations)
    return part1, part2