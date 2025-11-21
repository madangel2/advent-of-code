from utils import get_data
import os

def parse(key_or_lock):
    lines = key_or_lock.splitlines()
    isKey = '.' in lines[0]
    info = [col.count("#") - 1 for col in zip(*lines)]
    return isKey, info

def solve():
    data = get_data(25)

    keys = []
    locks = []

    rawData = data.split(os.linesep + os.linesep)
    for key_or_lock in rawData:
        isKey, info = parse(key_or_lock)
        if isKey:
            keys.append(info)
        else:
            locks.append(info)

    nb_of_fit = sum(
        all(key[i] + lock[i] <= 5 for i in range(len(lock)))
        for key in keys
        for lock in locks
    )

    return nb_of_fit, "Merry Christmas!"