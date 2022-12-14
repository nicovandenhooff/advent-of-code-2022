# --- Day 6: Tuning Trouble ---
# https://adventofcode.com/2022/day/6

from utils import get_input_path, read_data, timer


@timer
def solve(data, n):
    for i in range(n, len(data)):
        if len(set(data[i - n + 1 : i + 1])) == n:
            return i + 1


if __name__ == "__main__":
    day = 6
    input_path = get_input_path(day)
    data = read_data(input_path)[0]  # only one string for day 6

    part_1 = solve(data, 4)
    print(f"{part_1} characters are processed before the 1st start-of-packet marker.")

    part_2 = solve(data, 14)
    print(f"{part_2} characters are processed before the 1st start-of-message marker.")
