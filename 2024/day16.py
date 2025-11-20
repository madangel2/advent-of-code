from utils import get_data
from utils import parseMap, simpleMoves, rightMove, MapGraph

class DirectionalPosition:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
    
    def __eq__(self, other): 
        if not isinstance(other, DirectionalPosition):
            return NotImplemented

        return self.pos == other.pos and self.dir == other.dir
    
    def __hash__(self):
        return hash((self.pos, self.dir))
    
    def __lt__(self, other):
        #hack to compare easily complex
        return f"{str(self.pos)}{str(self.dir)}" < f"{str(other.pos)}{str(other.dir)}"
    
    def __str__(self):
        return f"Pos = {self.pos} | Dir = {self.dir}"

def initGraph(map):
    mapGraph = MapGraph()
    
    for pos, item in map.items():
        if item == "#":
            continue
        
        for sourceDirection in simpleMoves:
            source = DirectionalPosition(pos, sourceDirection)
            for move in simpleMoves:
                neighborPos = source.pos + move
                if neighborPos in map and map[neighborPos] != "#":
                    for neighborDirection in simpleMoves:
                        neighborDirPos = DirectionalPosition(neighborPos, neighborDirection)
                        score = calcScore(source, neighborDirPos)
                        mapGraph.addEdge(source, neighborDirPos, score)

    return mapGraph

def calcScore(source, destination):
    score = 1
    move = destination.pos - source.pos

    if source.dir + move == 0J:
        score += 2000
    elif source.dir != move:
        score += 1000
    
    if destination.dir + move == 0J:
        score += 2000
    elif destination.dir != move:
        score += 1000
    
    return score

# Init challenge
data = get_data(16)
map = parseMap(data)
startPos = None
endPos = None
for pos, item in map.items():
    if item == 'S':
        startPos = pos
    elif item == 'E':
        endPos = pos
if startPos == None or endPos == None:
    raise Exception("Could not find start or end position")

g = initGraph(map)
scores, seats = g.getLowestScoresWithSeats(DirectionalPosition(startPos, rightMove))

allEndScores ={DirectionalPosition(endPos, move): scores[DirectionalPosition(endPos, move)] for move in simpleMoves}
minScore = float('inf')
for endPos, score in allEndScores.items():
    if score < minScore:
        minScore = score
        minEndPos = endPos

print(f'Part1: {minScore}')
print(f'Part2: {len(seats[endPos])}')