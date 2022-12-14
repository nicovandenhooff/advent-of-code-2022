# --- Day 11: Monkey in the Middle ---
# https://adventofcode.com/2022/day/11

from utils import get_input_path, read_data, timer
from collections import deque


def process_data(data):
    modulo = 1
    monkeys, items, ops, tests, trues, falses = [], [], [], [], [], []

    data = [i.strip() for i in data]
    data = [i for i in data if i != ""]

    for i in data:
        if i[:6] == "Monkey":
            monkeys.append(i)
        elif i[:8] == "Starting":
            items.append(i)
        elif i[:9] == "Operation":
            ops.append(i)
        elif i[:4] == "Test":
            tests.append(i)
        elif i[3:7] == "true":
            trues.append(i)
        else:
            falses.append(i)

    monkey_dict = {k: {} for k in range(len(monkeys))}

    for i, item_string in enumerate(items):
        items_list = item_string.split("Starting items: ")[-1]
        items_list = eval(f"[{items_list}]")
        items_list = deque(items_list)
        monkey_dict[i]["items"] = items_list

    for o, op_string in enumerate(ops):
        op = op_string.split("Operation: new = old ")[-1]

        operand = op[0]
        value = op[2:]

        if value != "old":
            value = int(value)

        monkey_dict[o]["op"] = (operand, value)

    for t, test_string in enumerate(tests):
        test = test_string.split("Test: divisible by ")[-1]
        test = int(test)
        monkey_dict[t]["test"] = test

    for t, true_string in enumerate(trues):
        true = true_string.split("If true: throw to monkey ")[-1]
        true = int(true)
        monkey_dict[t]["true"] = true

    for f, false_string in enumerate(falses):
        false = false_string.split("If false: throw to monkey ")[-1]
        false = int(false)
        monkey_dict[f]["false"] = false

    for monkey in monkey_dict.keys():
        monkey_dict[monkey]["inspected"] = 0

    for monkey in monkey_dict.keys():
        modulo *= monkey_dict[monkey]["test"]

    return monkey_dict, modulo


@timer
def solve(monkey_dict, rounds, divide=False, modulo=None):

    if divide and modulo is not None:
        raise Exception("Either divide (part 1) OR modulo (part 2) for this problem!")

    inspected = []

    for _ in range(rounds):
        for _, monkey in sorted(monkey_dict.items()):
            current_items = len(monkey["items"])

            for _ in range(current_items):
                monkey["inspected"] += 1
                worry_level = monkey["items"].popleft()
                worry_level = _perform_op(worry_level, monkey)

                if divide:
                    worry_level = worry_level // 3

                if modulo is not None:
                    worry_level = worry_level % modulo

                if _perform_test(worry_level, monkey):
                    throw_to = monkey["true"]
                else:
                    throw_to = monkey["false"]

                monkey_dict[throw_to]["items"].append(worry_level)

    for _, monkey in monkey_dict.items():
        inspected.append(monkey["inspected"])

    inspected = sorted(inspected)

    return inspected[-1] * inspected[-2]


def _perform_test(worry_level, monkey):
    value = monkey["test"]
    return worry_level % value == 0


def _perform_op(worry_level, monkey):
    operand, value = monkey["op"]

    if value == "old":
        value = worry_level

    if operand == "+":
        return worry_level + value
    elif operand == "*":
        return worry_level * value
    else:
        raise Exception(f"Problem with operand {operand}")


if __name__ == "__main__":
    day = 11
    input_path = get_input_path(day)
    data = read_data(input_path)

    monkey_dict, _ = process_data(data)
    part_1 = solve(monkey_dict, rounds=20, divide=True)
    print(f"The level of monkey business after 20 rounds is: {part_1}.")

    monkey_dict, modulo = process_data(data)
    part_2 = solve(monkey_dict, rounds=10000, divide=False, modulo=modulo)
    print(f"The level of monkey business after 10000 rounds is: {part_2}.")
