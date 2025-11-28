from utils import get_data
from operator import add, mul

def concat(x, y):
    if y < 10:
        return x * 10 + y
    elif y < 100:
        return x * 100 + y
    elif y < 1000:
        return x * 1000 + y
    else:
        digits = len(str(y))
        return x * (10 ** digits) + y

def check_equation(nums, ops):
    if len(nums) == 2:
        return nums[0] == nums[1]

    total, a, b, *rest = nums
    
    for op in ops:
        result = op(a, b)
        if result <= total or op == concat:
            if check_equation([total, result] + rest, ops):
                return total
    return 0

def solve():
    data = get_data(7)
    problems = [list(map(int, line.replace(':','').split())) for line in data.splitlines()]

    part1_ops = [add, mul]
    part1_result = 0
    unsolved = []
    
    for problem in problems:
        result = check_equation(problem, ops=part1_ops)
        if result:
            part1_result += result
        else:
            unsolved.append(problem)
    
    part2_ops = [add, mul, concat]
    part2_additional = sum(check_equation(problem, ops=part2_ops) for problem in unsolved)
    
    return part1_result, part1_result + part2_additional


