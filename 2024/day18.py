from utils import get_data, initMap, simpleMoves, MapGraph

def initGraph(map):
    mapGraph = MapGraph()
    
    for pos, item in map.items():
        if item == "#":
            continue
        
        for move in simpleMoves:
            neighborPos = pos + move
            if neighborPos in map and map[neighborPos] != "#":
                mapGraph.addEdge(pos, neighborPos, 1)     
                        
    return mapGraph

def buildCorruptedMap(corruptedMemory, nbCorruptedMemory, mapWidth, mapHeight):
    map = initMap(mapWidth, mapHeight, '.')
    for i in range(nbCorruptedMemory):
        map[corruptedMemory[i]] = '#'
    return map

def getLowestPathToEnd(map, startPos, endPos):
    g = initGraph(map)
    lowestScore, path = g.getLowestScores(startPos)
    return lowestScore[endPos]

def solve():
    data = get_data(18)
    corruptedMemory = [complex(int(line.split(",")[0]), int(line.split(",")[1]))for line in data.splitlines()]
    mapWidth = 70
    mapHeight = 70
    startPos = complex(0, 0)
    endPos = complex(mapWidth, mapHeight)
    
    # Part 1
    map = buildCorruptedMap(corruptedMemory, 1024, mapWidth, mapHeight)
    part1 = getLowestPathToEnd(map, startPos, endPos)

    # Part 2
    left, right = 1024, len(corruptedMemory) - 1
    part2 = None

    while left <= right:
        mid = (left + right) // 2
        
        map = buildCorruptedMap(corruptedMemory, mid + 1, mapWidth, mapHeight)
        lowestPathToEnd = getLowestPathToEnd(map, startPos, endPos)
        
        if lowestPathToEnd == float('inf'):
            part2 = corruptedMemory[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return part1, part2