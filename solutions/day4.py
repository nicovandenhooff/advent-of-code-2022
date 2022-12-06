# --- Day 4: Camp Cleanup ---
# https://adventofcode.com/2022/day/4

from utils import get_input_path, read_data, timer


def process_data(data):
    processed_data = [i.split(",") for i in data]

    for i, pairs in enumerate(processed_data):
        assignment_pair = []

        for elf in pairs:
            start, stop = elf.split("-")
            start, stop = int(start), int(stop)
            assignment_pair.append([start, stop])

        processed_data[i] = assignment_pair

    return processed_data


def fully_contains(r1_start, r1_end, r2_start, r2_end):
    # range 1 contains range 2
    if r1_start <= r2_start and r1_end >= r2_end:
        return 1
    # range 2 contains range 1
    elif r2_start <= r1_start and r2_end >= r1_end:
        return 1
    else:
        return 0


def overlaps(r1_start, r1_end, r2_start, r2_end):
    # one common number in the range
    if len(set([r1_start, r1_end]).intersection(set([r2_start, r2_end]))) > 0:
        return 1
    # overlap from range 1 to 2
    elif r1_start < r2_start and r2_start < r1_end and r1_end < r2_end:
        return 1
    # overlap from range 2 to 1
    elif r2_start < r1_start and r1_start < r2_end and r2_end < r1_end:
        return 1
    else:
        return 0


@timer
def solve(processed_data):
    part_1 = 0
    part_2 = 0

    for i in processed_data:
        elf1_start, elf1_end = i[0][0], i[0][1]
        elf2_start, elf2_end = i[1][0], i[1][1]

        one_range_contains_another = fully_contains(
            elf1_start, elf1_end, elf2_start, elf2_end
        )

        ranges_overlap = overlaps(elf1_start, elf1_end, elf2_start, elf2_end)

        part_1 += one_range_contains_another
        part_2 += one_range_contains_another or ranges_overlap

    return part_1, part_2


if __name__ == "__main__":
    day = 4
    input_path = get_input_path(day)
    data = read_data(input_path)
    processed_data = process_data(data)

    part_1, part_2 = solve(processed_data)
    print(f"{part_1} pairs have ranges that fully contain the other.")
    print(f"{part_2} pairs have ranges that overlap with one another.")
