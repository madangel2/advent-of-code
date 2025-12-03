from utils import get_data

def get_joltage(bank, nb_switches):
    int_bank = [int(i) for i in bank]
    joltage = 0
    last_index = -1
    
    for switches_on in range(nb_switches):
        remaining = nb_switches - switches_on - 1
        slice_start = last_index + 1
        slice_end = len(int_bank) - remaining
        bank_slice = int_bank[slice_start:slice_end]
        
        max_digit = max(bank_slice)
        last_index = slice_start + bank_slice.index(max_digit)
        joltage += max_digit * 10 ** remaining

    return joltage

def solve():
    data = get_data(3)
    banks = data.splitlines()
    part1 = 0
    part2 = 0

    for bank in banks:
        int_bank = [int(i) for i in bank]
        part1 += get_joltage(int_bank, 2)
        part2 += get_joltage(int_bank, 12)
    
    return part1, part2
