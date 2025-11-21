import copy
from datetime import datetime
from multiprocessing import Pool
from utils import get_data

def getNewMap(guardMap, y, x):
    newMap = copy.deepcopy(guardMap)
    newMap[y][x] = "#"
    return newMap

def isInBound(guardMap, position):
    y = position[0]
    x = position[1]

    if x < 0 or y < 0:
        return False

    if x >= len(guardMap[0]) or y >= len(guardMap):
        return False

    return True

def isObstacle(guardMap, position):
    y = position[0]
    x = position[1]
    elem = guardMap[y][x]
    return elem == "#"

def getDirection(elem):
    match elem:
        case '^':
            return "up"
        case '>':
            return "right"
        case '<':
            return "left"
        case 'v':
            return "down"
        case _:
            raise Exception("Invalid elem for direction" + elem)

def switchDirection(currDirection):
    match currDirection:
        case "up":
            return "right"
        case "right":
            return "down"
        case "down":
            return "left"
        case "left":
            return "up"
        case _:
            raise Exception("Invalid current direction: " + currDirection)

def parsingMap(input):
    guardMap = [list(line) for line in input.splitlines()]

    for y, line in enumerate(guardMap):
        for x, elem in enumerate(line):
            if elem == "^":
                return guardMap, [y,x]

def runTheMapWrapper(args):
    return runTheMap(*args)

def runTheMap(guardMap, startingPosition):
    now = datetime.now()
    #print(f"task start {now}")
    
    movement = {
        "up" : [-1,0],
        "right": [0,1],
        "down": [1,0],
        "left": [0,-1]
    }
    
    positionLists = []
    positionAndDirectionList = []
    currPosition = copy.deepcopy(startingPosition)
    currDirection = getDirection(guardMap[currPosition[0]][currPosition[1]])
    inLoop = False

    while isInBound(guardMap, currPosition) and not inLoop:    
        currPositionDirection = (currPosition,currDirection)
        if currPosition not in positionLists:
            positionLists.append(currPosition)

        if currPositionDirection in positionAndDirectionList:
            inLoop = True
            break
        else:
            positionAndDirectionList.append(currPositionDirection)
            

        move = movement[currDirection]
        nextPosition = [currPosition[0] + move[0], currPosition[1] + move[1]]
        if isInBound(guardMap, nextPosition) and isObstacle(guardMap, nextPosition):
            currDirection = switchDirection(currDirection)
        else:
            currPosition = nextPosition
            
    return len(positionLists), inLoop

#### script

def solve():
    return "FIXME", "FIXME"
    possibilities = 0

    invalidElems = ['#','^','v','>','<']
    data = get_data(6)
    guardMap, startingPosition = parsingMap(data)

    tasks = []
    maps = []
    for y in range(len(guardMap)):
        for x in range(len(guardMap[y])):
            if guardMap[y][x] not in invalidElems:
                maps.append((getNewMap(guardMap, y, x), startingPosition))
    
    with Pool(processes=100) as pool:
        results = pool.map(runTheMapWrapper, maps)

    #print(results)
    ## TODO MAKE FASTER
    print(sum(1 for i in results if i[1] == True))
    





