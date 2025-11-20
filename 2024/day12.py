from utils import get_data, isInBound

data = get_data(12)
fullMap = [list(line) for line in data.splitlines()]
posCheck = [(0, -1), (-1, 0), (0, 1), (1, 0)]
posCheckDiag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def findSameNeighbors(pos, neighbors):
    if pos in neighbors or not isInBound(fullMap, pos):
        return neighbors

    neighbors.append(pos)

    for moveY, moveX in posCheck:
        neighbor = (pos[0] + moveY, pos[1] + moveX)
        if isInBound(fullMap, neighbor) and fullMap[neighbor[0]][neighbor[1]] == fullMap[pos[0]][pos[1]]:
            findSameNeighbors(neighbor, neighbors)

    return neighbors

def calcFencesPrice(group):
    totalFences = 0
    for elem in group:
        fences = 4
        for check in posCheck:
            neighbor = (elem[0] + check[0], elem[1] + check[1])
            if neighbor in group:
                fences -= 1
        totalFences += fences

    return totalFences * len(group)

def calcFencesPrice2(group):
    totalFences = 0
    for elem in group:
        for diag in posCheckDiag:
            neighborD = (elem[0] + diag[0], elem[1] + diag[1])
            neighbor1 = (elem[0], elem[1] + diag[1])
            neighbor2 = (elem[0] + diag[0], elem[1])

            if neighborD not in group and neighbor1 not in group and neighbor2 not in group:
                totalFences += 1
            elif neighborD not in group and neighbor1 in group and neighbor2 in group:
                totalFences += 1
            elif neighborD in group and neighbor1 not in group and neighbor2 not in group:
                totalFences += 1

    return totalFences * len(group)
    

groups = []
visited = []

for y, line in enumerate(fullMap):
    for x, item in enumerate(line):
        pos = (y, x)
        if pos in visited:
            continue
        
        group = findSameNeighbors(pos, [])
        groups.append(group)
        visited.extend(group)

print(f"Part1 -> {sum([calcFencesPrice(g) for g in groups])}")
print(f"Part2 -> {sum([calcFencesPrice2(g) for g in groups])}")
