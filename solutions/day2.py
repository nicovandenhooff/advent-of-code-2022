# --- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

from utils import get_input_path, read_data, timer

SHAPE_MAP = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}
STRATEGY_MAP = {"X": "L", "Y": "D", "Z": "W"}
WIN_MAP = {"A": "Y", "B": "Z", "C": "X"}
LOSE_MAP = {"A": "Z", "B": "X", "C": "Y"}
DRAW_MAP = {"A": "X", "B": "Y", "C": "Z"}
SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}
OUTCOME_SCORES = {"L": 0, "D": 3, "W": 6}


def process_data(data):
    processed_data = [i.split(" ") for i in data]
    return processed_data


@timer
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


@timer
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
    day = 2
    input_path = get_input_path(day)
    data = read_data(input_path)
    processed_data = process_data(data)

    part_1 = solve_part_1(processed_data)
    print(f"The total score following the strategy guide is: {part_1}.")

    part_2 = solve_part_2(processed_data)
    print(f"The total score following the elf's instructions is: {part_2}.")
