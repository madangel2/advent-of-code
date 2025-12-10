from utils import get_data
import re
from functools import reduce
from itertools import combinations
from operator import xor
from z3 import Int, Optimize, sat

def parse_line(line):
    # Part 1: Extract desired outcome from [...]
    pattern_match = re.search(r'\[([.#]*)\]', line)
    if not pattern_match:
        raise ValueError("No pattern found in brackets")
    
    pattern = pattern_match.group(1)
    desired_outcome = [c == '#' for c in pattern]
    array_size = len(desired_outcome)
    
    # Part 2: Extract all switches tuples (...)
    switch_tuple_matches = re.findall(r'\(([0-9,]+)\)', line)
    switches = []
    
    for tuple_str in switch_tuple_matches:
        indices = list(map(int, tuple_str.split(',')))
        bool_array = [False] * array_size
        for idx in indices:
            if idx < array_size:
                bool_array[idx] = True
        switches.append(bool_array)
    
    # Part 3: Extract joltage values from {...}
    joltage_matches = re.findall(r'{([0-9,]*)}', line)
    joltage = list(map(int, joltage_matches[0].split(',')))
    
    return desired_outcome, switches, joltage

# Part 1: every problem seems to be solvable with a combination of 1 or more switches press only 1 time
def find_minimum_press_to_solve_part1(problem, switches):
    for i in range(1, len(switches) + 1):
        for switch_combination in combinations(switches, i):
            # XOR all switch combinations
            if [reduce(xor, values_at_pos) for values_at_pos in zip(*switch_combination)] == problem:
                return i

# Part 2: Formulate problem as an integer linear programming problem an let z3 solver find the solution
def find_minimum_press_to_solve_part2(joltage, switches):    
    # Create Z3 variables for each switch (number of times to press it)
    press_counts = [Int(f'switch_{i}') for i in range(len(switches))]
    opt = Optimize()
    
    # Add constraints: each press count must be non-negative
    for count in press_counts:
        opt.add(count >= 0)
    
    # Add constraints: for each index in joltage array
    for idx in range(len(joltage)):
        # Sum of (press_count * switch_value) must equal target joltage
        total = sum(
            press_counts[switch_idx] if switches[switch_idx][idx] else 0
            for switch_idx in range(len(switches))
        )
        opt.add(total == joltage[idx])
    
    # Minimize the total number of presses
    total_presses = sum(press_counts)
    opt.minimize(total_presses)
    
    # Solve
    if opt.check() == sat:
        model = opt.model()
        return model.eval(total_presses).as_long()
    else:
        raise ValueError(f"No solution found for problem {joltage} with switches {switches}")

def solve():
    data = get_data(10)
    part1, part2 = 0, 0
    
    for line in data.splitlines():
        desired_outcome, switches, joltage = parse_line(line)
        part1 += find_minimum_press_to_solve_part1(desired_outcome, switches)
        part2 += find_minimum_press_to_solve_part2(joltage, switches)
    
    return part1, part2
