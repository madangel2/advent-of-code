from utils import get_data
from utils import parseMapInt, simpleMoves

data = get_data(10)
    
def hike(map, pos):
    peaks = []

    if(map[pos] == 9):
        return [pos]
    
    for move in simpleMoves:
        newPos = pos + move
        if newPos in map and map[newPos] - map[pos] == 1:
            peaks.extend(hike(map, newPos))
    
    return peaks

map = parseMapInt(data)
trailHead = [pos for pos, item in map.items() if item == 0]
peakPerHead = {head: hike(map, head) for head in trailHead}

print(f"Part1 -> {sum([len(set(peaks)) for peaks in peakPerHead.values()])}")
print(f"Part2 -> {sum([len(peaks) for peaks in peakPerHead.values()])}")