from typing import Iterable
from utils import get_data

def check_report_is_safe(items):
    ascending = items[0] < items[1]
    for i in range(len(items) - 1):
        diff = abs(items[i] - items[i+1])
        if items[i] > items[i+1] and ascending:
            return False
        elif items[i] < items[i+1] and not ascending:
            return False
        elif diff < 1 or diff > 3:
            return False
    return True

def omit_one(vals: list[int]) -> Iterable[list[int]]:
    for idx in range(len(vals)):
        yield vals[:idx] + vals[idx + 1 :]

data =  get_data(2).splitlines()
nbSafeReports = 0
nbSafeReportsWithDampener = 0

for r in data:
    items = [int(item) for item in r.split()]  
    if check_report_is_safe(items):
        nbSafeReports += 1
    else:
        for fixedItems in omit_one(items):
            if check_report_is_safe(fixedItems):
                nbSafeReportsWithDampener += 1
                break

print(f"Part 1: {nbSafeReports}")
print(f"Part 2: {nbSafeReportsWithDampener+nbSafeReports}")