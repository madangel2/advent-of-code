import re
from utils import get_data

def mul(x: int, y: int) -> int:
    return x * y

data = get_data(3)

fixedMemory = re.sub(r'(don\'t\(\))((?!do\(\)).|\n)*(do\(\))','',data)

res1 = sum([eval(call) for call in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)])
res2 = sum([eval(call) for call in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', fixedMemory)])

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")