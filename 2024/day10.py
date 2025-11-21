from utils import parseMapInt, simpleMoves, get_data
    
def hike(map, pos):
    peaks = []

    if(map[pos] == 9):
        return [pos]
    
    for move in simpleMoves:
        newPos = pos + move
        if newPos in map and map[newPos] - map[pos] == 1:
            peaks.extend(hike(map, newPos))
    
    return peaks

def solve():
    data = get_data(10)
    map = parseMapInt(data)
    trailHead = [pos for pos, item in map.items() if item == 0]
    peakPerHead = {head: hike(map, head) for head in trailHead}

    part1 = sum([len(set(peaks)) for peaks in peakPerHead.values()])
    part2 = sum([len(peaks) for peaks in peakPerHead.values()])
    
    return part1, part2