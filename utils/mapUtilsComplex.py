from functools import cmp_to_key
from heapq import heappop, heappush, heapify
from rich.console import Console

upMove = 0-1j
rightMove = 1+0j
downMove = 0+1j
leftMove = -1+0j

upLeftMove = upMove + leftMove
upRightMove = upMove + rightMove
downLeftMove = downMove + leftMove
downRightMove = downMove + rightMove

simpleMoves = [upMove, rightMove, downMove, leftMove]
diagMoves = [upRightMove, downRightMove, downLeftMove, upLeftMove]
allMoves = [upMove, upRightMove, rightMove, downRightMove, downMove, downLeftMove, leftMove, upLeftMove]

class ComplexMap:
    def __init__(self, map: dict, width: int, height: int):
        self.graph = {}
        self.map = map
        self.width = width
        self.height = height
    
    def get_all_positions(self):
        return self.map.keys()

    def get_neighbors(self, position : complex):
        neighbors = []
        for move in allMoves:
            neighbor = position + move
            if neighbor in self.map:
                neighbors.append(neighbor)
        return neighbors

    def get_absolute_diff(self, position: complex, other_position: complex):
        diff = position-other_position
        return abs(diff.real) + abs(diff.imag)

    def get_all_positions_in_radius(self, source_position: complex, radius: int, walkable_only=False):
        if(radius >= self.width and radius >= self.height):
            return self.map.keys()

        radius_positions = []
        for x in range(-radius, radius+1):
            for y in range(-radius, radius+1):
                pos = source_position + complex(x,y)
                manhattan_dist = abs(x) + abs(y)
                if(pos in self.map and manhattan_dist <= radius and (not walkable_only or self.map[pos] != "#")):
                    radius_positions.append(pos)

        return radius_positions
            

    def get_item(self, position : complex):
        return self.map[position]
    
    def is_in_map(self, position: complex):
        return position in self.map
    
    def get_all_walkable_position(self):
        return {pos for pos, item in self.map.items() if item != "#"}

    def find_first_item(self, item_to_search):
        for pos, item in self.map.items():
            if item == item_to_search:
                return pos
        
        raise Exception(f"Cound not item in map {item_to_search}")


class MapGraph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    #TODO cleanup multiple lowest score
    def getLowestScores(self, start):
        scores = {node: float('inf') for node in self.graph}    
        scores[start] = 0
        paths = {node: {} for node in self.graph}
        paths[start] = {start}

        priority_queue = [(0, str(start))]
        heapify(priority_queue)

        visited = set()

        while priority_queue:
            current_score, current_node_str = heappop(priority_queue)
            current_node = complex(current_node_str)

            if current_node in visited:
               continue
            visited.add(current_node)

            if current_score > scores[current_node]:
                continue
            
            for neighbor, weight in self.graph[current_node].items():
                score = current_score + weight
                
                if score < scores[neighbor]:
                    scores[neighbor] = score
                    heappush(priority_queue, (score, str(neighbor)))
                    paths[neighbor] = paths[current_node].union({neighbor})

        return scores, paths

    def getLowestScoresWithSeats(self, start):
        scores = {node: float('inf') for node in self.graph}    
        scores[start] = 0
        seats = {node: {} for node in self.graph}
        seats[start] = {start.pos}

        priority_queue = [(0, start)]
        heapify(priority_queue)

        visited = set()

        while priority_queue:
            current_score, current_node = heappop(priority_queue)

            if current_node in visited:
               continue
            visited.add(current_node)

            if current_score > scores[current_node]:
                continue
            
            for neighbor, weight in self.graph[current_node].items():
                score = current_score + weight
                
                if score < scores[neighbor]:
                    scores[neighbor] = score
                    seats[neighbor] = seats[current_node].union({neighbor.pos})
                    heappush(priority_queue, (score, neighbor))
                elif score == scores[neighbor]:
                    seats[neighbor] = seats[neighbor].union(seats[current_node])

        return scores, seats

def get_absolute_diff(position: complex, other_position: complex):
        diff = position-other_position
        return abs(diff.real) + abs(diff.imag)

def parse_map(data):
    height = len(data.splitlines())
    width = len(list(data.splitlines()[0]))
    
    return ComplexMap({complex(x, y): item for y, line in enumerate(data.splitlines()) for x, item in enumerate(list(line))}, width, height)
    

def parseMapInt(data):
    return {complex(x, y): int(item) for y, line in enumerate(data.splitlines()) for x, item in enumerate(list(line))}

def initMap(width, height, defaultItem):
    return {complex(x, y): defaultItem for x in range(width+1) for y in range(height+1)}

def is_on_perimiter(position, map_width, map_height):
    return position.real == 0 or position.imag == 0 or position.real == (map_width - 1) or position.imag == (map_height - 1)

def mapPosCompare(a : complex, b : complex):
    if a.imag < b.imag:
        return  - 1
    elif a.imag > b.imag:
        return 1
    elif a.real < b.real:
        return -1
    elif a.real > b.real:
        return 1
    
    return 0

def printMap(map: ComplexMap, path=[]):
    sortedMapPositions = sorted(map.get_all_positions(), key=cmp_to_key(mapPosCompare))

    lastY = 0
    console = Console()
    for pos in sortedMapPositions:
        if pos.imag > lastY:
            console.print("\n", end="")
            lastY = pos.imag

        match map.get_item(pos):
            case "#":
               console.print(":white_large_square:", end="") 
            case ".":
                if pos in path:
                    console.print(":purple_square:", end="")
                else:
                    console.print(":black_large_square:", end="")
            case "S":
               console.print(":green_square:", end="")
            case "E":
                console.print(":red_square:", end="")   
            case _:
               console.print(map.get_item(pos), end="")

    console.print("\n", end="")