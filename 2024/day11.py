from utils import get_data
from collections import Counter, defaultdict

data = get_data(11)


def blinks(rockCounts):
    newCounts = defaultdict(int)
    
    for k, v in rockCounts.items():
        if(k == "0"):
            newCounts["1"] += v
        elif len(k) % 2 == 0:
            newCounts[k[:len(k)//2]] += v
            newCounts[str(int(k[len(k)//2:]))] += v
        else:
            newCounts[str(int(k) * 2024)] += v

    return newCounts


def solve():
    rocks = data.split()
    rockCounts = Counter(rocks)
    part1 = 0

    for i in range(75):
        rockCounts = blinks(rockCounts)
        if(i == 24):
            part1 = sum(rockCounts.values())
    
    part2 = sum(rockCounts.values())
    return part1, part2

