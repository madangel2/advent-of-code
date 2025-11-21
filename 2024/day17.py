import re
from utils import get_data

class ThreeBitComputer:  
    def __init__(self, regA, regB, regC, program):
        self._ops = {0: self._adv, 1: self._bxl, 2: self._bst, 3: self._jnz, 4: self._bxc, 5: self._out, 6: self._bdv, 7: self._cdv}
        self._pointer = 0
        self.regA = regA
        self.regB = regB
        self.regC = regC
        self.program = program
        self.out = []

    def run(self):
        while(self._pointer < len(self.program)):
            opCode = self.program[self._pointer]
            operand = self.program[self._pointer + 1]
            self._ops[opCode](operand)

    def _adv(self, operand):
        self.regA = self.regA // (2 ** self._getComboOperand(operand))
        self._defaultJump()
    
    def _bxl(self, operand):
        self.regB = self.regB ^ operand
        self._defaultJump()
    
    def _bst(self, operand):
        self.regB = self._getComboOperand(operand) % 8
        self._defaultJump()
    
    def _jnz(self, operand):
        if self.regA == 0:
            self._defaultJump()
            return
        
        self._pointer = operand
    
    def _bxc(self, operand):
        self.regB = self.regB ^ self.regC
        self._defaultJump()
    
    def _out(self, operand):
        val = self._getComboOperand(operand) % 8
        self.out.append(val)
        self._defaultJump()
    
    def _bdv(self, operand):
        self.regB = self.regA // (2 ** self._getComboOperand(operand))
        self._defaultJump()
    
    def _cdv(self, operand):
        self.regC = self.regA // (2 ** self._getComboOperand(operand))
        self._defaultJump()
    
    def _defaultJump(self):
        self._pointer += 2

    def _getComboOperand(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.regA
            case 5:
                return self.regB
            case 6:
                return self.regC
            case 7:
                raise Exception("7 operand found and should not be used")
            
def findRegAPart2(originalComputer):
    i = len(originalComputer.program)-1
    mults = [0] * len(originalComputer.program)

    while i >= 0 and i < len(originalComputer.program):
        while mults[i] < 8:
            possibleSolution = sum([pow(8, i) * mult for i, mult in enumerate(mults)])
            testComp = ThreeBitComputer(possibleSolution, originalComputer.regB, originalComputer.regC, originalComputer.program)
            testComp.run()
            if i < len(testComp.out) and testComp.out[i] == originalComputer.program[i]:
                i -= 1
                break
            mults[i] += 1
            
        if(mults[i] > 7):
            mults[i] = 0
            i += 1
            mults[i] += 1

    if(testComp.out != originalComputer.program):
        raise Exception("Could not find solution for regA part 2")
    
    return possibleSolution


# Init challenge
def solve():
    data = get_data(17)

    match = re.search(r"Register A: ([0-9]*)\nRegister B: ([0-9]*)\nRegister C: ([0-9]*)\n\nProgram: ([0-9,]*)", data)
    regA = int(match[1])
    regB = int(match[2])
    regC = int(match[3])
    program = [int(i) for i in match[4].split(',')]

    comp = ThreeBitComputer(regA, regB, regC, program)
    comp.run()

    part1 = comp.out
    part2 = findRegAPart2(comp)
    return part1, part2


