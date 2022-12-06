# --- Day 3: Rucksack Reorganization ---
# https://adventofcode.com/2022/day/3

import string
from utils import get_input_path, read_data, timer

LETTERS = string.ascii_lowercase + string.ascii_uppercase
PRIORITIES = {k: i + 1 for i, k in enumerate(LETTERS)}


@timer
def solve_part_1(data):
    total = 0

    for items in data:
        # common item is the intersection of the two compartments
        mid = len(items) // 2
        compartments = set(items[:mid]), set(items[mid:])
        common_item = compartments[0].intersection(compartments[1])
        common_item = list(common_item)[0]
        priority = PRIORITIES[common_item]
        total += priority

    return total


@timer
def solve_part_2(data):
    total = 0

    for i in range(0, len(data), 3):
        group = data[i : i + 3]

        for i, g in enumerate(group):
            group[i] = set(g)

        # common item is the intersection of the three groups
        common_item = group[0].intersection(group[1], group[2])
        common_item = list(common_item)[0]
        priority = PRIORITIES[common_item]
        total += priority

    return total


if __name__ == "__main__":
    day = 3
    input_path = get_input_path(day)
    data = read_data(input_path)

    part_1 = solve_part_1(data)
    print(f"The sum of the common item priorities for each rucksack is: {part_1}.")

    part_2 = solve_part_2(data)
    print(f"The sum of the common item priorities for each group is: {part_2}.")
