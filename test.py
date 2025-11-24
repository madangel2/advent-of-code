import sys
import os
import importlib
import json
import time
import traceback
from pathlib import Path

# Emojis
CHECK = "🟩"
ERROR = "🟥"
WARN = "🟨"
UNKNOWN = "⬜"

def printLine(day, run_status, exec_time, part1_answer, part2_answer):
    print(f"{day:<6} {run_status:<12} {exec_time:<16} {part1_answer:<15} {part2_answer:<15}")

def main():
    # Setup path
    project_root = Path(__file__).parent.absolute()
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    if len(sys.argv) < 2:
        print("Usage: python test.py <year>")
        sys.exit(1)

    year = sys.argv[1]
    os.environ["AOC_YEAR"] = year

    # Load answers
    try:
        with open(f"data/{year}/answers.json", "r") as f:
            answers = json.load(f)
    except FileNotFoundError:
        print(f"Warn: data/{year}/answers.json not found, you will get warning for all answer check")
        answers = {}

    printLine("Day", "Run status", "Execution time", "Part 1 answer", "Part 2 answer")
    print("-" * 66)

    for day in range(1, 26):
        day_str = str(day)
        module_name = f"{year}.day{day}"
        
        status_icon = ERROR
        time_icon = ""
        time_str = ""
        p1_icon = ERROR
        p2_icon = ERROR
        
        try:
            # Import and run
            start_time = time.time()
            module = importlib.import_module(module_name)
            
            if not hasattr(module, 'solve'):
                 printLine(day, WARN, 'No solve()', '-', '-')
                 continue

            part1, part2 = module.solve()
            end_time = time.time()
            duration = end_time - start_time
            
            # Status: Ran without error
            status_icon = CHECK
            
            # Time check
            time_str = f"{duration:.4f}s"
            if duration < 1.0:
                time_icon = CHECK
            else:
                time_icon = WARN
            
            # Answer check
            expected = answers.get(day_str)
            if expected:
                # Convert to string for comparison
                if str(part1) == str(expected[0]):
                    p1_icon = CHECK
                else:
                    p1_icon = ERROR
                
                if str(part2) == str(expected[1]):
                    p2_icon = CHECK
                else:
                    p2_icon = ERROR
            else:
                p1_icon = WARN # No answer known
                p2_icon = WARN

            time_display = f"{time_icon} {time_str}"
            printLine(day, status_icon, time_display, p1_icon, p2_icon)

        except ImportError:
             # Day not implemented yet
             printLine(day, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN)
             pass
        except Exception:
            # Error during run
            printLine(day, ERROR, 'Error', '-', '-')

if __name__ == "__main__":
    main()
