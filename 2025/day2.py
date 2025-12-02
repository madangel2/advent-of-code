from utils import get_data

def check_invalid_part_1(string_id):
    length = len(string_id)
    
    if length % 2 > 0:
        return False
    
    middle = length // 2
    return string_id[:middle] == string_id[middle:]

def check_invalid_part_2(string_id):
    length = len(string_id)
    
    # Only check divisors of the length
    for substring_length in range(length // 2, 0, -1):
        if length % substring_length == 0:
            div = length // substring_length
            if string_id == string_id[:substring_length] * div:
                return True
    
    return False

def solve():
    data = get_data(2)

    part1 = 0
    part2 = 0

    for range_string in data.split(","):
        lower_range, upper_range = range_string.split("-")
        for id in range(int(lower_range), int(upper_range) + 1):
            string_id = str(id)
            if check_invalid_part_1(string_id):
                part1 += id
                part2 += id
            elif check_invalid_part_2(string_id):
                part2 += id
    
    return part1, part2
