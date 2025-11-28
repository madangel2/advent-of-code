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
    
    # Track total bananas for each sequence across all buyers
    sequence_totals = defaultdict(int)
    
    for secret in buyerSecrets:
        lastVariations = deque(maxlen=4)
        seen_sequences = set()  # Track sequences seen for this buyer
        lastPrice = secret % 10
        
        for i in range(2000):
            secret = calcNextSecret(secret)
            currentPrice = secret % 10
            priceDiff = currentPrice - lastPrice
            lastVariations.append(priceDiff)
            
            # Only process when we have a full sequence of 4
            if i >= 3:  # After 4 iterations (0,1,2,3), we have 4 diffs
                key = tuple(lastVariations)
                # Only count first occurrence of this sequence for this buyer
                if key not in seen_sequences:
                    seen_sequences.add(key)
                    sequence_totals[key] += currentPrice
            
            lastPrice = currentPrice
        total += secret
    
    part1 = total
    part2 = max(sequence_totals.values())
    return part1, part2