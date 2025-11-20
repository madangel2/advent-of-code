from pathlib import (Path)
import os, sys

def get_data(day: int) -> str:
    # Try to get year from env var (set by main.py)
    year = os.environ.get("AOC_YEAR")
    
    # If not set, try to deduce from caller's path (if running dayXX.py directly)
    if not year:
        import inspect
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        if module and module.__file__:
            path_parts = Path(module.__file__).parts
            # Assuming structure .../2024/dayXX.py
            if len(path_parts) >= 2 and path_parts[-2].isdigit():
                year = path_parts[-2]
    
    if not year:
        year = "2024" # Default fallback
        
    # Look for data in project_root/data/{year}/day{day}.txt
    # We assume utils.py is in project_root/utils/
    project_root = Path(__file__).parent.parent
    file = project_root / "data" / year / f"day{day}.txt"
    
    if file.exists():
        return file.open().read()
    else:
        raise Exception(f"File not found {file}")
    
def isInBound(arr, pos):
    y, x = pos
    return not (y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]))

