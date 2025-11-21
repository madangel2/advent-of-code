from utils import get_data
from collections import deque, defaultdict

def calcNextSecret(secret):
    p1 = (secret ^ (secret << 6)) & 0xFFFFFF
    p2 = (p1 ^ (p1 >> 5)) & 0xFFFFFF
    p3 = (p2 ^ (p2 << 11)) & 0xFFFFFF
    return p3

def solve():
    data = get_data(22)
    buyerSecrets = [int(line) for line in data.splitlines()]
    total = 0
    occurences = defaultdict(dict)

    for secret in buyerSecrets:
        lastVariations = deque(maxlen=4)
        originalSecret = secret
        lastSecret = secret
        for i in range(2000):
            secret = calcNextSecret(secret)
            lastPrice = lastSecret % 10
            currentPrice = secret % 10
            priceDiff = currentPrice - lastPrice
            lastVariations.append(priceDiff)
            if len(lastVariations) == 4:
                key = tuple(lastVariations)
                if originalSecret not in occurences[key]:
                    occurences[key][originalSecret] = currentPrice          
            lastSecret = secret
        total += secret

    sequence = max(occurences, key=lambda k: sum(occurences[k].values()))
    
    part1 = total
    part2 = f"{sequence} -> {sum(occurences[sequence].values())}"
    return part1, part2