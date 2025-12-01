from utils import get_data

def get_password_1(rotations, start):
    password = 0
    current = start
    for rotation in rotations:
        direction, steps = rotation[0], int(rotation[1:])
        current = (current + (-steps if direction == "L" else steps)) % 100
        password += current == 0

    return password

def get_password_2(rotations, start):
    password = 0
    current = start
    for rotation in rotations:
        direction, steps = rotation[0], int(rotation[1:])
        started_at_zero = current == 0
        
        current = (current + (-steps if direction == "L" else steps))
        quotient, current = divmod(current, 100)
        password += abs(quotient)
        
        if started_at_zero and quotient < 0 and current != 0:
            password -= 1
        
        if current == 0 and quotient <= 0:
            password += 1

    return password

def solve():
    data = get_data(1)
    rotations = data.splitlines()
    start = 50
    part1 = get_password_1(rotations, start)
    part2 = get_password_2(rotations, start)

    return part1, part2