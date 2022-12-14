# --- Day 5: Supply Stacks ---
# https://adventofcode.com/2022/day/5
# Note: Part 2 could be more efficency with a deque, but since the
# string processing took so long to code I was too lazy to implement
# this approach (although my approach is already fast) :D

from collections import defaultdict
from utils import get_input_path, read_data, timer


def process_data(data):
    """Day 5 special: brute force string processing..."""
    moves = []
    stacks = []

    for datum in data:
        if datum == "":
            continue
        elif "[" in datum:
            stacks.append(datum)
        elif datum[0] == " ":
            total_stacks = int(datum[-2])
        elif "move" in datum:
            moves.append(datum)

    processed_stacks = process_stacks(stacks, total_stacks)
    processed_moves = process_moves(moves)

    return processed_stacks, processed_moves


def process_stacks(stacks, total_stacks):
    # stack number: [stack items]
    processed_stacks = defaultdict(list)

    # where the stack # are in each stack string
    stack_idx = [4 * i + 1 for i in range(0, total_stacks + 2)]

    # build the stacks with python lists
    for i, j in zip(range(1, total_stacks + 1), stack_idx):
        for s in stacks:
            if s[j] != " ":
                processed_stacks[i].insert(0, s[j])

    return processed_stacks


def process_moves(moves):
    # keys: "n" crates to move, "from" this stack, "to" this stack
    processed_moves = []

    for m in moves:
        m = m.replace(" ", "").replace(",", "")

        n, m_from = m.split("from")
        n = int(n.split("move")[-1])
        m_from, m_to = m_from.split("to")
        m_from, m_to = int(m_from), int(m_to)

        processed_moves.append({"n": n, "from": m_from, "to": m_to})

    return processed_moves


@timer
def solve_part_1(processed_stacks, processed_moves):
    top_crates = ""

    # move one crate at a time
    for m in processed_moves:
        for _ in range(m["n"]):
            elem = processed_stacks[m["from"]].pop()
            processed_stacks[m["to"]].append(elem)

    for _, stack in processed_stacks.items():
        top_crates += stack[-1]

    return top_crates


@timer
def solve_part_2(processed_stacks, processed_moves):
    top_crates = ""

    # move "slices" of crates
    for m in processed_moves:
        crates = []

        for _ in range(m["n"]):
            elem = processed_stacks[m["from"]].pop()
            crates.insert(0, elem)

        processed_stacks[m["to"]] += crates

    for _, stack in processed_stacks.items():
        top_crates += stack[-1]

    return top_crates


if __name__ == "__main__":
    day = 5
    input_path = get_input_path(day)
    data = read_data(input_path)
    processed_stacks, processed_moves = process_data(data)

    part_1 = solve_part_1(processed_stacks, processed_moves)
    print(f"Top crates with CrateMover9000: {part_1}")

    processed_stacks, processed_moves = process_data(data)
    part_2 = solve_part_2(processed_stacks, processed_moves)
    print(f"Top crates with CrateMover9001: {part_2}")
