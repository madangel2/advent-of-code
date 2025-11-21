from utils import get_data
import itertools

def compactMem1(nbs):
    idx = 0
    empty = False
    mems = []
    for nb in nbs:
        if empty:
            mems.extend(nb*".")
        else:
            mems.extend(nb*str(idx))
            idx += 1
        empty = not empty
    
    idx1 = 0
    idx2 = len(mems) - 1
    while(idx1 < idx2):
        if(mems[idx1] != "."):
            idx1 += 1
        elif(mems[idx2] == "."):
            idx2 -= 1
        else:
            mems[idx1] = mems[idx2]
            mems[idx2] = "."
            idx1 += 1
            idx2 -= 1

    return mems

def getMemArray(char,number):
    arr = []
    for i in range(number):
        arr.append(char)
    return arr

def compactMem2(nbs):
    idx = 0
    empty = False
    mems = []
    for i, nb in enumerate(nbs):
        if empty:
            mems.append(getMemArray(".", nb))
        else:
            mems.append(getMemArray(str(idx), nb))
            idx += 1
        empty = not empty

    moved = []
    for i in range(len(mems)-1, 0, -1):
        if "." in mems[i] or len(mems[i])==0 or mems[i][0] in moved :
            continue

        for j in range(0, i):
            if("." not in mems[j] or len(mems[j]) < len(mems[i])):
                continue
            tmp = getMemArray(".", len(mems[j]) - len(mems[i]))
            mems[j] = mems[i]
            mems[i] = getMemArray(".", len(mems[i]))
            if(len(tmp) > 0):
                mems.insert(j+1,tmp)
                i += 1
            moved.append(mems[[j][0]])
            break
    
    return list(itertools.chain.from_iterable(mems))


def solve():
    data = get_data(9)
    nbs = [int(item) for item in list(data)]
    mem1 = compactMem1(nbs)
    mem2 = compactMem2(nbs)

    part1 = sum([int(item)*idx for idx, item in enumerate(mem1) if item != "."])
    part2 = sum([int(item)*idx for idx, item in enumerate(mem2) if item != "."])
    
    return part1, part2


