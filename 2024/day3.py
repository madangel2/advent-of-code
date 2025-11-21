import re
from utils import get_data

def mul(x: int, y: int) -> int:
    return x * y

def solve():
    data = get_data(3)

    fixedMemory = re.sub(r'(don\'t\(\))((?!do\(\)).|\n)*(do\(\))','',data)

    res1 = sum([eval(call) for call in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)])
    res2 = sum([eval(call) for call in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', fixedMemory)])

    return res1, res2