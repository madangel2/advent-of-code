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

def moveRobotsFromStart(robots, nbSeconds, width, height):
    for r in robots:
        r.currentX = (r.startX + (r.velocityX * nbSeconds)) % width
        r.currentY = (r.startY + (r.velocityY * nbSeconds)) % height

def moveRobots(robots, nbSeconds, width, height):
    for r in robots:
        r.currentX = (r.currentX + (r.velocityX * nbSeconds)) % width
        r.currentY = (r.currentY + (r.velocityY * nbSeconds)) % height

def getSafetyFactor(robots, width, height):
    midX = floor(width/2)
    midY = floor(height / 2)
    q1 = sum(1 for r in robots if r.currentX < midX and r.currentY < midY)
    q2 = sum(1 for r in robots if r.currentX > midX and r.currentY < midY)
    q3 = sum(1 for r in robots if r.currentX < midX and r.currentY > midY)
    q4 = sum(1 for r in robots if r.currentX > midX and r.currentY > midY)
    return q1*q2*q3*q4

def calcEntropy(robots, width, height):
    positions = {(r.currentX, r.currentY) for r in robots}
    
    perms = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    total = 0
    for x, y in positions:
        neighbor_count = 1  # Count self
        for dx, dy in perms:
            newX, newY = x + dx, y + dy
            if 0 <= newX < width and 0 <= newY < height and (newX, newY) in positions:
                neighbor_count += 1
        total += neighbor_count
    
    return total

def calcEntropyOptimized(robots, width, height):
    pos_set = {(r.currentX, r.currentY) for r in robots}
    
    total = len(pos_set)
    
    for x, y in pos_set:
        if (x + 1, y) in pos_set:
            total += 2
        if (x, y + 1) in pos_set:
            total += 2
    
    return total

def solve():
    data = get_data(14)
    nbSeconds = 100
    width = 101
    height = 103

    pattern = re.compile(r"p=(-?[0-9]*),(-?[0-9]*) v=(-?[0-9]*),(-?[0-9]*)")
    robots = [robot(match.group(1), match.group(2), match.group(3), match.group(4)) for match in pattern.finditer(data)]

    #Part1
    moveRobotsFromStart(robots, nbSeconds, width, height)
    part1 = getSafetyFactor(robots, width, height)

    #Part2
    for r in robots:
        r.reset()

    #Highest is less random
    currentWorstEntropy = 0
    currentRobotMap = []
    currentSecond = 0

    for i in range(1, 10000):
        moveRobots(robots, 1, width, height)
        entropy = calcEntropyOptimized(robots, width, height)
        if(entropy > currentWorstEntropy):
            currentWorstEntropy = entropy
            #Uncomment to see the tree
            #currentRobotMap = getRobotsMap(robots, width, height)
            currentSecond = i

    #Uncomment to see the tree
    #printRobots(currentRobotMap)
    return part1, currentSecond
