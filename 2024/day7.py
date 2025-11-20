from utils import get_data
from operator import add, mul

def concat(x,y):
    return int(f"{x}{y}")

def solve(nums, ops):
    if len(nums) == 2:
        return nums[0] == nums[1]

    total, a, b, *rest = nums

    for op in ops:
        if solve([total, op(a, b)] + rest, ops):
            return total
    return 0

    
    
data = get_data(7)
problems = [list(map(int, line.replace(':','').split())) for line in data.splitlines()]

print(f"Part 1: {sum(solve(problem, ops=[add,mul]) for problem in problems)}")
print(f"Part 2: {sum(solve(problem, ops=[add,mul,concat]) for problem in problems)}")


