from utils import get_data
from shapely.geometry import Polygon, Point

def fast_polygone_check(polygone, x1, y1, x2, y2):
    p1 = (x1, y1)
    p2 = (x2, y1)
    p3 = (x2, y2)
    p4 = (x1, y2)

    #FIXME save only 0.5 seconds...
    if not polygone.intersects(Point(p1)) or not polygone.intersects(Point(p2)) or not polygone.intersects(Point(p3)) or not polygone.intersects(Point(p4)):
        return False

    return polygone.contains(Polygon([p1, p2, p3, p4]))

def find_biggest_square(coordinates, polygone=None):
    max_square_size = 0
    possible_coordinates = [c for c in coordinates if polygone is None or polygone.intersects(Point(c))]

    for i in range(len(possible_coordinates)):
        x1, y1 = possible_coordinates[i]      
        for j in range(len(possible_coordinates)):
            if i == j:
                continue

            x2, y2 = coordinates[j]

            square_size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if square_size > max_square_size and (polygone is None or fast_polygone_check(polygone, x1, y1, x2, y2)):
                max_square_size = square_size
    
    return max_square_size
            

def solve():
    data = get_data(9)
    coordinates = [tuple(map(int, line.split(","))) for line in data.split("\n")]    
    
    part1 = find_biggest_square(coordinates)
    part2 = find_biggest_square(coordinates, Polygon(coordinates))
    
    return part1, part2