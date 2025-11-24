# Advent of Code

This repository contains my scripts to solve the [Advent of Code](https://adventofcode.com) challenges.

## Requirements

-   Python 3.x
-   `pip`

## Setup

To set up the project environment, run the provided setup script. This will create a virtual environment and install the necessary dependencies.

```bash
bash setup.sh
```

After the setup is complete, activate the virtual environment:

```bash
source .venv/bin/activate
```

## Running a Day Script

You can run the solution for a specific day using the `main.py` script.

### Command

```bash
python main.py <year> <day>
```

**Example:**
To run the solution for Day 1 of 2024:
```bash
python main.py 2024 1
```

### Puzzle Input

The script expects the puzzle input file to be located at:
`data/<year>/day<day>.txt`

**Example:**
For Day 1 of 2024, put your input in:
`data/2024/day1.txt`

## Testing All Day Scripts

You can test all implemented solutions for a specific year to ensure they produce the correct answers and run within acceptable time limits.

### Command

```bash
python test.py <year>
```

**Example:**
To test all days for 2024:
```bash
python test.py 2024
```

### Answers File

The test runner checks your solutions against an answers file located at:
`data/<year>/answers.json`

**Structure:**
The `answers.json` file should be a JSON object where:
-   **Keys**: The day number (as a string, e.g., "1", "2").
-   **Values**: A list containing two elements: `[Part 1 Answer, Part 2 Answer]`.

**Example `data/2024/answers.json`:**
```json
{
  "1": ["12345", "67890"],
  "2": ["ABC", "DEF"]
}
```
