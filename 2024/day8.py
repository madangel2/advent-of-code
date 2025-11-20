from utils import get_data
from collections import defaultdict
from mapUtilsComplex import parseMap

def getAntinodes(ant1, ant2, map, isPart1):
    antinodes = []
    diff = ant1 - ant2
    antinode = complex(ant1 - diff * 2)
    while(antinode in map):
        antinodes.append(antinode)
        if isPart1:
            break
        antinode = antinode - diff
    return antinodes
    
        
data = get_data(8)
map = parseMap(data)
antennas = defaultdict(list)
for pos, item in map.items():
    if item != ".":
        antennas[item].append(pos)


antinodes = set()
antinodes2 = set()
for signal, posList in antennas.items():
    for idx, antenna in enumerate(posList):
        antinodes2.add(antenna)
        for op in posList[:idx] + posList[idx+1:]:
            antinodes.update(getAntinodes(antenna, op, map, True))
            antinodes2.update(getAntinodes(antenna, op, map, False))

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes2)}")

