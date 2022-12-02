# --- Day 1: Calorie Counting ---


def read_data(input_file):
    with open(input_file) as f:
        data = f.readlines()
        data = [i.replace("\n", "") for i in data]
        data = [int(i) if i != "" else i for i in data]

    return data


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
    input_file = "../input/day1_input.txt"
    data = read_data(input_file)
    part1_result = solve(data, 1)
    part2_result = solve(data, 3)
    print(f"The elf is carrying {part1_result} calories!")
    print(f"The top 3 elves are carrying {part2_result} calories!")
