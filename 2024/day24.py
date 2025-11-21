from utils import get_data
import os

def parseOperationLine(line):
    operRaw = line.split(" -> ")[0]
    leftKey = operRaw.split(" ")[0]
    gateKey = operRaw.split(" ")[1]
    rightKey = operRaw.split(" ")[2]
    resultKey = line.split(" -> ")[1]

    return leftKey, gateKey, rightKey, resultKey

def execOperation(operation, leftValue, rightValue):
    if operation == "AND" :
        return leftValue and rightValue
    elif operation == "OR" :
        return leftValue or rightValue
    elif operation == "XOR" :
        return leftValue != rightValue
    else:
        raise ValueError('Unknown operation: ' + operation)
    
def getOutputKeyFromLine(line):
    return line.split(" -> ")[1]

def findLine(operation_lines, operator, key, key2=None, match_mode='and'):
    for line in operation_lines:
        rightPart = line.split(" -> ")[0]
        
        # Check operator first
        if f" {operator} " not in rightPart:
            continue
        
        # Single key case
        if key2 is None:
            if key in rightPart:
                return line
        # Two keys case
        else:
            if match_mode == 'and':
                if key in rightPart and key2 in rightPart:
                    return line
            elif match_mode == 'or':
                if key in rightPart or key2 in rightPart:
                    return line
    
    return None

def getOperationLinesForIndex(operation_lines, index, last_reminder_key):
    padded_index = str(index).zfill(2)
    
    #Part1 - result
    first_result_line = findLine(operation_lines, "XOR", f"x{padded_index}", f"y{padded_index}")
    second_result_line = findLine(operation_lines, "XOR", last_reminder_key)
    
    #Part1 - reminder calculation
    first_reminder_line = findLine(operation_lines, "AND", f"x{padded_index}", f"y{padded_index}")
    first_reminder_output_key = getOutputKeyFromLine(first_reminder_line)
    
    second_reminder_line = findLine(operation_lines, "AND", last_reminder_key)
    second_reminder_output_key = getOutputKeyFromLine(second_reminder_line)
    
    third_reminder_line = findLine(operation_lines, "OR", first_reminder_output_key, second_reminder_output_key, match_mode='or')

    return first_result_line, second_result_line, first_reminder_line, second_reminder_line, third_reminder_line


def solve():
    data = get_data(24)

    initialValues = data.split(os.linesep + os.linesep)[0].splitlines()
    operations = data.split(os.linesep + os.linesep)[1].splitlines()
    valueCache = {line.split(": ")[0]: bool(int(line.split(": ")[1])) for line in initialValues}

    #Run operation
    while operations:
        i = 0
        while i < len(operations):
            leftKey, gateKey, rightKey, resultKey = parseOperationLine(operations[i])

            if leftKey not in valueCache or rightKey not in valueCache:
                i += 1
            else:
                valueCache[resultKey] = execOperation(gateKey, valueCache[leftKey], valueCache[rightKey])        
                del operations[i]

    #Calc result for z keys
    zKeys = sorted([key for key in valueCache.keys() if key.startswith("z")], reverse=True)
    binary_string = "0b" + "".join(['1' if valueCache[key] else '0' for key in zKeys])
    part1Answer = int(binary_string, 2)

    # Part2
    operation_lines = data.split(os.linesep + os.linesep)[1].splitlines()
    maxIndex = int(sorted([key for key in valueCache.keys() if key.startswith("x")], reverse=True)[0][1:])
    fixedOutputs=[]
    reminderKey = "mqs"

    for i in range(1, maxIndex + 1):
        padded_index = str(i).zfill(2)
        res_line_1, res_line_2, rem_line_1, rem_line_2, rem_line_3 = getOperationLinesForIndex(operation_lines, i, reminderKey)
        reminderKey = getOutputKeyFromLine(rem_line_3)
        
        #Cheated from manual fix. It's possible this code cannot find all the fix necessary
        if getOutputKeyFromLine(res_line_2) != f"z{padded_index}":
            fixedOutputs.append(getOutputKeyFromLine(res_line_2))
            fixedOutputs.append(f"z{padded_index}")
            if reminderKey == f"z{padded_index}":
                    reminderKey = getOutputKeyFromLine(res_line_2)
        elif getOutputKeyFromLine(res_line_1) not in res_line_2:
            fixedOutputs.append(getOutputKeyFromLine(res_line_1))
            if getOutputKeyFromLine(rem_line_1) in res_line_2:
                fixedOutputs.append(getOutputKeyFromLine(rem_line_1))
            elif getOutputKeyFromLine(rem_line_2) in res_line_2:
                fixedOutputs.append(getOutputKeyFromLine(rem_line_2))
            elif reminderKey in res_line_2:
                fixedOutputs.append(reminderKey)
                reminderKey = getOutputKeyFromLine(res_line_1)

    part2Answer = ",".join(sorted(fixedOutputs))
    return part1Answer, part2Answer