from utils import get_data
from operator import add, mul

def concat(x,y):
    return int(f"{x}{y}")

def check_equation(nums, ops):
    if len(nums) == 2:
        return nums[0] == nums[1]

    total, a, b, *rest = nums

    for op in ops:
        if check_equation([total, op(a, b)] + rest, ops):
            return total
    return 0

    
    
def solve():
    data = get_data(7)
    problems = [list(map(int, line.replace(':','').split())) for line in data.splitlines()]

    part1 = sum(check_equation(problem, ops=[add,mul]) for problem in problems)
    part2 = sum(check_equation(problem, ops=[add,mul,concat]) for problem in problems)
    
    return part1, part2


