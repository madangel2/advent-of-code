from utils import get_data
from collections import Counter
import re

def getPath(current_position, destination_position, dead_position):
    move = destination_position - current_position 
    x_move =  "<" if move.real < 0 else ">"
    y_move =  "^" if move.imag < 0 else "v"
    path = ""
    if(current_position.imag == dead_position.imag and destination_position.real == dead_position.real):
        path = int(abs(move.imag)) * y_move + int(abs(move.real)) * x_move
    elif (current_position.real == dead_position.real and destination_position.imag == dead_position.imag):
        path = int(abs(move.real)) * x_move + int(abs(move.imag)) * y_move
    elif (move.real > 0):
        path = int(abs(move.imag)) * y_move + int(abs(move.real)) * x_move
    else:
        path = int(abs(move.real)) * x_move + int(abs(move.imag)) * y_move


    return path + "A"

def parseKeyPad(keypad_string):
    keypad = {complex(x, y): input for y, line in enumerate(keypad_string.splitlines()) for x, input in enumerate(list(line))}
    dead_position = [key for key, value in keypad.items() if value == "#"][0]
    keypadDict = {}
    for position, input in keypad.items():
        if(input != "#"):
            keypadDict[input] = {}
            for destination_position, destination_input in keypad.items():
                keypadDict[input][destination_input] = getPath(position, destination_position, dead_position)

    return keypadDict

def translateInputs(keyPadCache, inputs):
    current = "A"
    translations = []

    for input in list(inputs):
        translations.append(keyPadCache[current][input])
        current = input

    return ''.join(translations)

def splitInput(inputs):
    splittedInputs = re.split(r"(?<=A)", inputs)
    return [s for s in splittedInputs if s]

def getNumberOfInputNeeded(inputs, directionKeyPadCache, robot_counts):
    splittedInputs = splitInput(inputs)
    currentCounter = Counter(splittedInputs)
    
    for i in range(robot_counts):
        newCounter = Counter()
        for item, count in currentCounter.items():
            itemCounter = Counter(splitInput(translateInputs(directionKeyPadCache,item)))
            for key, value in itemCounter.items():
                newCounter[key] += value * count
        currentCounter = newCounter

    return sum([len(key) * value for key, value in currentCounter.items()])



def solve():
    data = get_data(21)
    numericKeyPad = """789
456
123
#0A"""

    directionKeyPad = """#^A
<v>"""

    numericalKeyPadCache = parseKeyPad(numericKeyPad)
    directionKeyPadCache = parseKeyPad(directionKeyPad)

    total2 = 0
    total25 = 0
    for code in data.splitlines():
        firstTranslation = translateInputs(numericalKeyPadCache, code)
        codeNumericValue = int(re.search(r'\d+', code).group())
        total2 += getNumberOfInputNeeded(firstTranslation, directionKeyPadCache, 2) * codeNumericValue
        total25 += getNumberOfInputNeeded(firstTranslation, directionKeyPadCache, 25) * codeNumericValue

    return total2, total25