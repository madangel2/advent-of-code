from pathlib import (Path)
import os, sys

def get_data(day: int) -> str:
    file = Path(os.path.abspath(os.path.dirname(sys.argv[0])) + f"/data/day{day}.txt")
    if file.exists():
        return file.open().read()
    else:
        raise Exception(f"File not found {file}")
    
def isInBound(arr, pos):
    y, x = pos
    return not (y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]))

