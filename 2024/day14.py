from utils import get_data, isInBound
from math import floor

import re

class robot:
    def __init__(self, sx, sy, vx, vy):
        self.startX = int(sx)
        self.startY = int(sy)
        self.velocityX = int(vx)
        self.velocityY = int(vy)
        self.currentX = self.startX
        self.currentY = self.startY

    def reset(self):
        self.currentX = self.startX
        self.currentY = self.startY
        

def printRobots(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(map[y][x], end='')
        print("\n")

def getRobotsMap(robots, width, height):
    arr = [['' for col in range(width)] for row in range(height)]

    for y in range(height):
        for x in range(width):
            val = sum(1 for r in robots if r.currentX == x and r.currentY == y)
            arr[y][x] = ' ' if val == 0 else u"\u2588"

    return arr

def moveRobots(robots, nbSeconds, width, height):
    for r in robots:
        r.currentX = (r.startX + (r.velocityX * nbSeconds)) % width
        r.currentY = (r.startY + (r.velocityY * nbSeconds)) % height

def getSafetyFactor(robots, width, height):
    midX = floor(width/2)
    midY = floor(height / 2)
    q1 = sum(1 for r in robots if r.currentX < midX and r.currentY < midY)
    q2 = sum(1 for r in robots if r.currentX > midX and r.currentY < midY)
    q3 = sum(1 for r in robots if r.currentX < midX and r.currentY > midY)
    q4 = sum(1 for r in robots if r.currentX > midX and r.currentY > midY)
    return q1*q2*q3*q4

def calcEntropy(robots, width, height):
    arr = [[0 for col in range(width)] for row in range(height)]

    perms = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for r in robots:
        arr[r.currentY][r.currentX] = 1
    
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == 1:
                for perm in perms:
                    newX = x + perm[0]
                    newY = y + perm[1]
                    if isInBound(arr, (newY, newX)) and arr[newY][newX] > 0:
                        arr[y][x] += 1
    
    return sum(sum(arr,[]))

data = get_data(14)
nbSeconds = 100
width = 101
height = 103
treeTreshold = 30

pattern = re.compile(r"p=(-?[0-9]*),(-?[0-9]*) v=(-?[0-9]*),(-?[0-9]*)")
robots = [robot(match.group(1), match.group(2), match.group(3), match.group(4)) for match in pattern.finditer(data)]

#Part1
moveRobots(robots, nbSeconds, width, height)
print(f"Part1: {getSafetyFactor(robots, width, height)}")

#Part2
for r in robots:
    r.reset()

#Highest is less random
currentWorstEntropy = 0
currentRobotMap = []
currentSecond = 0

for i in range(10000):
    moveRobots(robots, i, width, height)
    entropy = calcEntropy(robots, width, height)
    if(entropy > currentWorstEntropy):
        currentWorstEntropy = entropy
        currentRobotMap = getRobotsMap(robots, width, height)
        currentSecond = i


#Uncomment to see the tree
#printRobots(currentRobotMap)
print(f"Part2: {currentSecond}")
