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


# Init challenge
def solve():
    data = get_data(18)
    corruptedMemory = [complex(int(line.split(",")[0]), int(line.split(",")[1]))for line in data.splitlines()]
    mapWidth = 70
    mapHeight = mapWidth
    map = initMap(mapWidth, mapHeight, '.')
    startPos = complex(0, 0)
    endPos = complex(mapWidth, mapHeight)

    part1 = None
    part2 = None

    for i in range(len(corruptedMemory)):
        map[corruptedMemory[i]] = '#'
        
        if(i >= 1023):
            g = initGraph(map)
            lowestScore, path = g.getLowestScores(startPos)

            #TODO cleanup and speedup
            if(i == 1023):
                part1 = lowestScore[endPos]
            elif(lowestScore[endPos] == float('inf')):
                part2 = corruptedMemory[i]
                break
    
    return part1, part2