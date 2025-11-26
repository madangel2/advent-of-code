from utils import get_data

class Node:
    def __init__(self, size, is_free, file_id=None, pos=0):
        self.size = size
        self.is_free = is_free
        self.file_id = file_id
        self.pos = pos
        self.prev = None
        self.next = None

def compactMem1(nbs):
    idx = 0
    empty = False
    mems = []
    for nb in nbs:
        if empty:
            mems.extend(nb*".")
        else:
            mems.extend([str(idx)] * nb)
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


def compactMem2(disk_map):
    # Build linked list
    head = tail = None
    pos = file_id = 0
    
    for i, size in enumerate(disk_map):
        is_free = i % 2 == 1
        if size > 0:
            node = Node(size, is_free, None if is_free else file_id, pos)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                node.prev = tail
                tail = node
            pos += size
        if not is_free:
            file_id += 1
    
    # Index first free block of each size
    first_free = [None] * 10
    node = head
    while node:
        if node.is_free:
            for s in range(1, min(node.size + 1, 10)):
                if first_free[s] is None:
                    first_free[s] = node
        node = node.next
    
    # Move files from right to left
    current = tail
    while current:
        prev = current.prev
        if not current.is_free and current.size < 10:
            target = first_free[current.size]
            if target and target.pos < current.pos:
                # Move file
                remaining = target.size - current.size
                target.is_free = False
                target.file_id = current.file_id
                target.size = current.size
                current.is_free = True
                current.file_id = None
                
                # Split free space if needed
                new_free = None
                if remaining > 0:
                    new_free = Node(remaining, True, None, target.pos + current.size)
                    new_free.prev = target
                    new_free.next = target.next
                    if target.next:
                        target.next.prev = new_free
                    target.next = new_free
                
                # Update free index
                for s in range(1, 10):
                    if first_free[s] == target:
                        if new_free and s <= remaining:
                            first_free[s] = new_free
                        else:
                            runner = target.next
                            while runner and runner.pos < current.pos:
                                if runner.is_free and runner.size >= s:
                                    break
                                runner = runner.next
                            first_free[s] = runner if runner and runner.pos < current.pos else None
        current = prev
    
    # Render result
    result = []
    node = head
    while node:
        result.extend(["."] * node.size if node.is_free else [str(node.file_id)] * node.size)
        node = node.next
    return result



def solve():
    data = get_data(9)
    nbs = [int(item) for item in list(data)]
    mem1 = compactMem1(nbs)
    mem2 = compactMem2(nbs)

    part1 = sum([int(item)*idx for idx, item in enumerate(mem1) if item != "."])
    part2 = sum([int(item)*idx for idx, item in enumerate(mem2) if item != "."])
    
    return part1, part2


