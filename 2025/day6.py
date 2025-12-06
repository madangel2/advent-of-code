from utils import get_data
from math import prod

def parse_columns(data_text, part2=False):
    lines = data_text.strip().split('\n')
    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]
    
    # Find column boundaries (spaces on all rows)
    separators = [i for i in range(width) if all(line[i] == ' ' for line in lines)]
    
    columns = []
    start = 0
    for end in separators + [width]:
        if end > start:
            if part2:
                # Read numbers vertically (column-wise)
                col_data = [line[start:end] for line in lines]
                operand = col_data[-1][0]
                numbers = []
                for i in range(end - start):
                    num_str = ''.join(row[i] for row in col_data[:-1]).strip()
                    if num_str:
                        numbers.append(int(num_str))
                if numbers:
                    columns.append({'numbers': numbers, 'operand': operand})
            else:
                # Read numbers horizontally (row-wise)
                col_data = [line[start:end].strip() for line in lines if line[start:end].strip()]
                if col_data:
                    columns.append({'numbers': [int(x) for x in col_data[:-1]], 'operand': col_data[-1]})
        start = end + 1
    
    return columns

def evaluate_column(column):
    numbers, operand = column['numbers'], column['operand']
    return sum(numbers) if operand == '+' else prod(numbers)

def solve():
    data = get_data(6)
    part1 = sum(evaluate_column(col) for col in parse_columns(data))
    part2 = sum(evaluate_column(col) for col in parse_columns(data, part2=True))
    return part1, part2
