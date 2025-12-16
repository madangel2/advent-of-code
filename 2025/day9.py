from utils import get_data
from shapely.geometry import Polygon, Point, box
from shapely.strtree import STRtree
from shapely import prepare

def find_biggest_square(coordinates, polygone=None):
    max_square_size = 0
    
    if polygone is None:
        possible_coordinates = coordinates
    else:
        # Create spatial index from all coordinate points
        points = [Point(c) for c in coordinates]
        tree = STRtree(points)
        
        # Bulk query: get all points that intersect the polygon at once
        intersecting_indices = tree.query(polygone, predicate='intersects')
        possible_coordinates = [coordinates[idx] for idx in intersecting_indices]
    
    # Generate all coordinate pairs with their potential square sizes
    pairs = []
    for i in range(len(possible_coordinates)):
        for j in range(i + 1, len(possible_coordinates)):
            x1, y1 = possible_coordinates[i]
            x2, y2 = possible_coordinates[j]
            square_size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            pairs.append((square_size, x1, y1, x2, y2))
    
    # Sort by size descending for early exit optimization
    pairs.sort(reverse=True)
    
    # Check largest squares first
    for square_size, x1, y1, x2, y2 in pairs:
        # Early exit: if current pair's size can't beat max, we're done
        if square_size <= max_square_size:
            break
        
        if polygone is None:
            max_square_size = square_size
        else:
            # Use box() for faster rectangle geometry creation
            rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            
            # Single containment check instead of multiple intersects
            if polygone.contains(rect):
                max_square_size = square_size
    
    return max_square_size

def solve():
    data = get_data(9)
    coordinates = [tuple(map(int, line.split(","))) for line in data.split("\n")]
    coordinate_polygone = Polygon(coordinates)
    prepare(coordinate_polygone)
    
    part1 = find_biggest_square(coordinates)
    part2 = find_biggest_square(coordinates, coordinate_polygone)
    
    return part1, part2