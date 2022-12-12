# --- Day 9: Rope Bridge ---
# https://adventofcode.com/2022/day/9

import math
from collections import Counter
from utils import get_input_path, read_data, timer


def process_data(data):
    instructions = []

    for d in data:
        direction, steps = d.split(" ")
        instructions.append((direction, int(steps)))

    return instructions


@timer
def solve(instructions, total_tails):
    head = (0, 0)
    tails = {i: (0, 0) for i in range(total_tails)}
    tail_counts = {i: Counter() for i in range(total_tails)}

    for i, tail in tails.items():
        tail_counts[i][tail] += 1

    for i in instructions:
        direction, steps = i[0], i[1]

        while steps > 0:
            head = move_head(head, direction)
            current_head = head

            for i in sorted(tails.keys()):
                tails[i] = move_tail(tail=tails[i], following=current_head)
                tail_counts[i][tails[i]] += 1
                current_head = tails[i]

            steps -= 1

    visited = len(tail_counts[total_tails - 1])

    return visited


def move_head(head, direction):
    if direction == "L":
        return (head[0], head[1] - 1)
    elif direction == "R":
        return (head[0], head[1] + 1)
    elif direction == "D":
        return (head[0] - 1, head[1])
    elif direction == "U":
        return (head[0] + 1, head[1])
    else:
        raise Exception(f"Direction error: {direction}")


def move_tail(tail, following):
    # if norm = 2 we need to move up or down
    if norm(following, tail) == 2:
        for i in [-1, 1]:
            move_up = tail[0] + i, tail[1]
            move_down = tail[0], tail[1] + i

            if norm(following, move_up) == 1:
                return move_up
            elif norm(following, move_down) == 1:
                return move_down

    # if norm > 2 we need to move diagonal
    elif norm(following, tail) > 2:
        for i in [-1, 1]:
            for j in [-1, 1]:
                move_diagonal = tail[0] + i, tail[1] + j

                # sqrt 2 generalizes to multiple tail knots in part 2
                if norm(following, move_diagonal) <= math.sqrt(2):
                    return move_diagonal

    return tail


def norm(head, tail):
    return math.sqrt(math.pow((head[0] - tail[0]), 2) + math.pow((head[1] - tail[1]), 2))


if __name__ == "__main__":
    day = 9
    input_path = get_input_path(day)
    data = read_data(input_path)
    instructions = process_data(data)

    part_1 = solve(instructions, total_tails=1)
    print(f"The tail of the rope visits {part_1} positions at least once.")

    part_2 = solve(instructions, total_tails=9)
    print(f"The tail of the rope visits {part_2} positions at least once.")
