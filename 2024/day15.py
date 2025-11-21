from utils import applyMove, getElem, setElem, findFirstItemOnMap, get_data, isInBound

def moveBox(map, box, direction):
    possibleEmptySpot = applyMove(box, direction)
    while(isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == 'O'):
        possibleEmptySpot = applyMove(possibleEmptySpot, direction)
    if isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == '.':
        map[possibleEmptySpot[0]][possibleEmptySpot[1]] = 'O'
        map[box[0]][box[1]] = "."

def moveBox2(map, leftBox, rightBox, direction):
    if direction == '<':
        moveBoxLeft(map, rightBox)
    elif direction == '>':
        moveBoxRight(map, leftBox)
    elif direction == 'v':
        moveBoxDown(map, leftBox, rightBox)
    elif direction == '^':
        moveBoxUp(map, leftBox, rightBox)

def moveBoxLeft(map, box):
    possibleEmptySpot = applyMove(box, (0, -2))
    while(isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == ']'):
        possibleEmptySpot = applyMove(possibleEmptySpot, (0, -2))
    if isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == '.':
        for i in range(possibleEmptySpot[1], box[1]):
            map[box[0]][i] = map[box[0]][i+1]
        setElem(map, box, '.')

def moveBoxRight(map, box):
    possibleEmptySpot = applyMove(box, (0, 2))
    while(isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == '['):
        possibleEmptySpot = applyMove(possibleEmptySpot, (0, 2))
    if isInBound(map, possibleEmptySpot) and getElem(map, possibleEmptySpot) == '.':
        for i in range(possibleEmptySpot[1], box[1], -1):
            map[box[0]][i] = map[box[0]][i-1]
        setElem(map, box, '.')

def getElementsToMoveVertical(elems, map, heigth, yMovement):
    currentHeight = heigth
    needToCheckOtherLevel = True
    while(needToCheckOtherLevel):
        needToCheckOtherLevel = False
        currentHeightElems = [(y, x) for y, x in elems if y == currentHeight]

        for y, x in currentHeightElems:
            elem = getElem(map, (y + yMovement, x))
            if elem == '[':
                elems.append((y + yMovement, x))
                elems.append((y + yMovement, x+1))
                needToCheckOtherLevel = True
            elif elem == ']':
                elems.append((y + yMovement, x))
                elems.append((y + yMovement, x-1))
                needToCheckOtherLevel = True
            elif elem == "#":
                raise Exception("Cannot move into walls")
            
        currentHeight = currentHeight + yMovement

    return list(set(elems))
        
def moveBoxUp(map, leftBox, rightBox):
    try:
        boxesToMove = getElementsToMoveVertical([leftBox, rightBox], map, leftBox[0], - 1)
    except:
        #could not move boxes
        return
    
    sortedByY = sorted(boxesToMove, key=lambda tup: tup[0], reverse=False)

    for y, x in sortedByY:
        setElem(map, (y-1, x), map[y][x])
        setElem(map, (y, x), '.')

def moveBoxDown(map, leftBox, rightBox):
    try:
        boxesToMove = getElementsToMoveVertical([leftBox, rightBox], map, leftBox[0], 1)
    except:
        #could not move boxes
        return
    
    sortedByY = sorted(boxesToMove, key=lambda tup: tup[0], reverse=True)

    for y, x in sortedByY:
        setElem(map, (y+1, x), map[y][x])
        setElem(map, (y, x), '.')


def move(map, direction, currentPos):
    dirDict = {'<': (0, -1), 'v': (1,0), '^': (-1,0), '>': (0,1)}
    dir = dirDict.get(direction)
    newPos =  applyMove(currentPos, dir)
    
    if getElem(map, newPos) == 'O':
        moveBox(map, newPos, dir)
    
    if getElem(map, newPos) == '.':
        map[newPos[0]][newPos[1]] = "@"
        map[currentPos[0]][currentPos[1]] = "."
        return newPos
    
    return currentPos

def move2(map, direction, currentPos):
    dirDict = {'<': (0, -1), 'v': (1,0), '^': (-1,0), '>': (0,1)}
    dir = dirDict.get(direction)
    newPos =  applyMove(currentPos, dir)
    
    if getElem(map, newPos) == '[':
        otherBox = (newPos[0], newPos[1] + 1)
        moveBox2(map, newPos, otherBox, direction)
    elif getElem(map, newPos) == ']':
        otherBox = (newPos[0], newPos[1] - 1)
        moveBox2(map, otherBox, newPos, direction)

    
    if getElem(map, newPos) == '.':
        setElem(map, newPos, '@')
        setElem(map, currentPos, '.')
        return newPos
    
    return currentPos

def solve():
    data = get_data(15).split("\n\n")

    #Part 1
    map = [list(line) for line in data[0].splitlines()]
    directions = list(data[1].replace("\n", ""))
    currentPos = findFirstItemOnMap(map, "@")
    for dir in directions:
        currentPos = move(map, dir, currentPos)
    allBoxGpsCoords = sum([x + (y * 100) for y, line in enumerate(map) for x, item in enumerate(line) if item == 'O'])

    #Part 2
    map2 = [list(line) for line in data[0].replace('.','..').replace('#','##').replace('O', '[]').replace('@','@.').splitlines()]
    currentPos = findFirstItemOnMap(map2, "@")
    for dir in directions:
        currentPos = move2(map2, dir, currentPos)
    allBoxGpsCoords2 = sum([x + (y * 100) for y, line in enumerate(map2) for x, item in enumerate(line) if item == '['])
    
    return allBoxGpsCoords, allBoxGpsCoords2