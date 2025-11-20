from utils import get_data

data = get_data(1)

list1 = []
list2 = []

for line in data.splitlines():
    data = line.split()
    list1.append(int(data[0]))
    list2.append(int(data[1]))

list1.sort()
list2.sort()

print(f"Part 1: {sum([abs(elem - list2[idx]) for idx, elem in enumerate(list1)])}")
print(f"Part 2: {sum([i * list2.count(i) for i in list1])}")