def getElem(map, pos):
    return map[pos[0]][pos[1]]

def setElem(map, pos, elem):
    map[pos[0]][pos[1]] = elem

def applyMove(currentPos, direction):
    return (currentPos[0] + direction[0], currentPos[1] + direction[1])

def findFirstItemOnMap(map, item):
    for y, line in enumerate(map):
        for x, elem in enumerate(line):
            if elem == item:
                return (y,x)
    raise Exception("No robot found in map")

def printMap(map):
    for line in map:
        for item in line:
            print(item, end="")
        print(" ")
        
