# --- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1

from utils import get_input_path, read_data, timer


def process_data(data):
    processed_data = [int(i) if i != "" else i for i in data]
    return processed_data


@timer
def solve(data, n):
    result = 0
    running_total = 0
    calorie_counts = []

    for i in data:
        if i == "":
            calorie_counts.append(running_total)
            running_total = 0
        else:
            running_total += i

    calorie_counts.sort(reverse=True)
    result = sum(calorie_counts[:n])

    return result


if __name__ == "__main__":
    day = 1
    input_path = get_input_path(day)
    data = read_data(input_path)
    processed_data = process_data(data)

    part_1 = solve(processed_data, 1)
    print(f"The elf is carrying {part_1} calories.")

    part_2 = solve(processed_data, 3)
    print(f"The top 3 elves are carrying {part_2} calories.")
