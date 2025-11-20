from utils import get_data, allMoves, diagMoves, parse_map

def masSearch(puzzle,pos):
    nbFound = 0

    if puzzle.get_item(pos) != 'A':
        return False

    for move in diagMoves:
        newPos1 = pos + move
        newPos2 = pos - move

        if newPos1 not in puzzle.get_all_positions() or newPos2 not in puzzle.get_all_positions():
            continue
        if puzzle.get_item(newPos1) == 'M' and puzzle.get_item(newPos2) == 'S':
            nbFound+=1

    return nbFound > 1


def wordSearch(puzzle,word,pos):
    count = 0

    for move in allMoves:
        exit = False
        for i in range(len(word)):
            newPos = pos + move * i
            if newPos not in puzzle.get_all_positions() or puzzle.get_item(newPos) != word[i]:
                exit = True
                break
        
        if not exit:
            count+=1
    
    return count



data =  get_data(4)
puzzle = parse_map(data)  

print(f"Part 1: {sum([wordSearch(puzzle, 'XMAS', pos) for pos in puzzle.get_all_positions()])}")
print(f"Part 2: {sum([1 for pos in puzzle.get_all_positions() if masSearch(puzzle,pos)])}")

