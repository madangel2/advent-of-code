import sys
import os
import importlib
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <year> <day>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    # Set environment variable for utils.get_data
    os.environ["AOC_YEAR"] = year

    # Add project root to sys.path so we can import utils
    project_root = Path(__file__).parent.absolute()
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Construct module path
    # Assuming days are in a folder named after the year, e.g., 2024/day1.py
    # We need to import it as a module.
    # Since 2024 is a number, we might need to use importlib or ensure it's importable.
    # Python modules usually shouldn't start with numbers, but importlib can handle it if it's a folder.
    # However, `import 2024.day1` is invalid syntax.
    # We can use importlib.import_module("2024.day1")
    
    module_name = f"{year}.day{day}"
    
    try:
        print(f"Running Advent of Code {year} Day {day}...")
        importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error importing module {module_name}: {e}")
    except Exception as e:
        print(f"Error running day {day}: {e}")

if __name__ == "__main__":
    main()
