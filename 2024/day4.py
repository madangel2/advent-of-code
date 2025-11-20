from utils import get_data
from utils import allMoves, diagMoves, parseMap

def masSearch(puzzle,pos):
    nbFound = 0

    if puzzle[pos] != 'A':
        return False

    for move in diagMoves:
        newPos1 = pos + move
        newPos2 = pos - move
        
        if puzzle.get(newPos1) == 'M' and puzzle.get(newPos2) == 'S':
            nbFound+=1

    return nbFound > 1


def wordSearch(puzzle,word,pos):
    count = 0

    for move in allMoves:
        exit = False
        for i in range(len(word)):
            newPos = pos + move * i
            if newPos not in puzzle or puzzle[newPos] != word[i]:
                exit = True
                break
        
        if not exit:
            count+=1
    
    return count



data =  get_data(4)
puzzle = parseMap(data)  

print(f"Part 1: {sum([wordSearch(puzzle, 'XMAS', pos) for pos in puzzle])}")
print(f"Part 2: {sum([1 for pos in puzzle if masSearch(puzzle,pos)])}")

