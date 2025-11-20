from utils import get_data
from mapUtilsComplex import initMap, simpleMoves, MapGraph

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
data = get_data(18)
corruptedMemory = [complex(int(line.split(",")[0]), int(line.split(",")[1]))for line in data.splitlines()]
mapWidth = 70
mapHeight = mapWidth
map = initMap(mapWidth, mapHeight, '.')
startPos = complex(0, 0)
endPos = complex(mapWidth, mapHeight)


for i in range(len(corruptedMemory)):
    map[corruptedMemory[i]] = '#'
    
    if(i >= 1023):
        g = initGraph(map)
        lowestScore = g.getLowestScores(startPos)

        #TODO cleanup and speedup
        if(i == 1023):
            print(f'Part1: {lowestScore[endPos]}')
        elif(lowestScore[endPos] == float('inf')):
            print(f'Part2: {corruptedMemory[i]}')
            break