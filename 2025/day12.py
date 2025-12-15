from utils import get_data
import re

class Section:
    def __init__(self, width, height, shapes):
        self.width = width
        self.height = height
        self.shapes = shapes

def parse(data):
    shape_pattern = r'[0-5]{1}:\n[#.]{3}\n[#.]{3}\n[#.]{3}'    
    shapes = []
    for match in re.finditer(shape_pattern, data):
        shapes.append([list(line) for line in match.group().splitlines()[1:]])
    
    section_pattern = r'[0-9]{1,}x[0-9]{1,}: ([0-9]{1,} ){5}[0-9]{1,}'
    sections = []
    for match in re.finditer(section_pattern, data):
        dimensions, shapes_str = match.group().split(': ')
        width, height = map(int, dimensions.split('x'))
        shape_ids = list(map(int, shapes_str.split()))
        sections.append(Section(width, height, shape_ids))
    
    return shapes, sections


# The problem should be way harder than this, but by only checking if the total area fits, we can get the answer....
def check_fit(shapes, section):
    section_total = section.width * section.height
    shape_sizes = [sum(row.count('#') for row in shape) for shape in shapes]
    shape_totals = sum(shape_sizes[shape_id] * count for shape_id, count in enumerate(section.shapes))
    
    return shape_totals <= section_total


def solve():
    data = get_data(12)
    shapes, sections = parse(data)
    
    part1 = sum(1 for section in sections if check_fit(shapes, section))
    part2 = "Merry Christmas!"
    
    return part1, part2
