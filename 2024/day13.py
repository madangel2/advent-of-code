from utils import get_data
import re

class ClawInfo:
    def __init__(self, ax, ay, bx, by, px, py):
        self.ax = int(ax)
        self.ay = int(ay)
        self.bx = int(bx)
        self.by = int(by)
        self.px = int(px)
        self.py = int(py)
    
    def __str__(self):
        return f'Button A: X+{self.ax}, Y+{self.ay} / Button B: X+{self.bx}, Y+{self.by} / Prize: X={self.px}, Y={self.py}'

    def __repr__(self):
        return str(self)
    

def solve(problem, pTranformation):
    px = problem.px + pTranformation
    py = problem.py + pTranformation
    a = divmod(px*problem.by - py*problem.bx, problem.ax*problem.by - problem.ay*problem.bx)
    b = divmod(problem.ax*py - problem.ay*px, problem.ax*problem.by - problem.ay*problem.bx)
    
    #if we have a reminder, the problem is not possible
    if(a[1] == 0 and b[1] == 0):
        return a[0] * 3 + b[0]
    
    return 0


data = get_data(13)
pattern = re.compile(r"Button A: X\+([0-9]*), Y\+([0-9]*)\nButton B: X\+([0-9]*), Y\+([0-9]*)\nPrize: X=([0-9]*), Y=([0-9]*)")
problems = [ClawInfo(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6)) for match in pattern.finditer(data)]

nbTokens = 0
nbTokensPart2 = 0
for p in problems:
    nbTokens += solve(p, 0)
    nbTokensPart2 += solve(p, 10000000000000)


print(f'Part1: {nbTokens}')
print(f'Part1: {nbTokensPart2}')