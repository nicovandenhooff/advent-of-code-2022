# --- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

SHAPE_MAP = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}
STRATEGY_MAP = {"X": "L", "Y": "D", "Z": "W"}
WIN_MAP = {"A": "Y", "B": "Z", "C": "X"}
LOSE_MAP = {"A": "Z", "B": "X", "C": "Y"}
DRAW_MAP = {"A": "X", "B": "Y", "C": "Z"}
SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}
OUTCOME_SCORES = {"L": 0, "D": 3, "W": 6}


def read_data(input_file):
    with open(input_file) as f:
        data = f.readlines()
        data = [i.replace("\n", "") for i in data]
        data = [i.split(" ") for i in data]

    return data


def solve_part_1(data):
    result = 0

    for game in data:
        opp_shape, my_shape = game[0], game[1]

        # determine the game outcome for part 1
        if SHAPE_MAP[opp_shape] == SHAPE_MAP[my_shape]:
            outcome = "D"
        elif WIN_MAP[opp_shape] == my_shape:
            outcome = "W"
        else:
            outcome = "L"

        score = OUTCOME_SCORES[outcome] + SHAPE_SCORE[my_shape]

        result += score

    return result


def solve_part_2(data):
    result = 0

    for game in data:
        opp_shape, game_outcome = game[0], game[1]
        game_outcome = STRATEGY_MAP[game_outcome]

        # determine what shape to play for part 2
        if game_outcome == "D":
            my_shape = DRAW_MAP[opp_shape]
        elif game_outcome == "W":
            my_shape = WIN_MAP[opp_shape]
        else:
            my_shape = LOSE_MAP[opp_shape]

        shape_score = SHAPE_SCORE[my_shape]
        round_score = OUTCOME_SCORES[game_outcome]

        result += shape_score + round_score

    return result


if __name__ == "__main__":
    input_file = "../input/day2_input.txt"
    data = read_data(input_file)
    part_1 = solve_part_1(data)
    part_2 = solve_part_2(data)

    print(f"The total score following the strategy guide is: {part_1}")
    print(f"The total score following the elf's instructions is: {part_2}")
