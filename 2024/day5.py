from utils import get_data
from collections import defaultdict
from math import ceil

def getRuleDict(input):
    lines = input.splitlines()
    rules = defaultdict(list)
    lastIndex = len(lines) - 1
    for idx, line in enumerate(lines):
        if line :
            ruleSplit = line.split("|")
            rules[ruleSplit[0]].append(ruleSplit[1])
        else:
            lastIndex = idx
            break
    
    return rules, lastIndex

def getPageGroups(input,startIndex):
    pageGroups = []
    lines = input.splitlines()
    for i in range(startIndex, len(lines)):
        pageGroups.append(lines[i].split(","))
    
    return pageGroups

def isValidGroup(group, rules):
    pageToWatch = []
    for p in reversed(group):
        if p in pageToWatch:
            return False
        else:
            pageToWatch.extend(rules[p])
    return True

def canComeBefore(val, otherVal, rules):
    for ov in otherVal:
        if val in rules[ov]:
            return False
    return True

def fixGroup(group, rules):
    newGroup = []
    while len(group) > 0:
        i = 0
        while i < len(group):
            if canComeBefore(group[i], [p for p in group if p != group[i]], rules):
                break
            i += 1
        newGroup.append(group[i])
        group.remove(group[i])
    
    if not isValidGroup(newGroup, rules):
         raise Exception("Could not fix group " + group)

    return newGroup

def getMiddleValue(arr):
    return int(arr[ceil((len(arr))/2) - 1])

    

res1 = 0
res2 = 0
data = get_data(5)
rules, lastIndex = getRuleDict(data)
pageGroups = getPageGroups(data, lastIndex + 1)

for idx, group in enumerate(pageGroups):
    if isValidGroup(group, rules):
        res1 += getMiddleValue(group)
    else:
        fixedGroup = fixGroup(group, rules)
        res2 += getMiddleValue(fixedGroup)

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")

