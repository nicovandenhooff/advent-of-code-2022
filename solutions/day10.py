# --- Day 10: Cathode-Ray Tube ---
# https://adventofcode.com/2022/day/10

from utils import get_input_path, read_data, timer


def process_data(data):
    instructions = []

    for d in data:
        if d == "noop":
            instructions.append("noop")
        else:
            cmd, add = d.split(" ")
            instructions.append((cmd, int(add)))

    return instructions


@timer
def solve_part_1(instructions, special_cycles={20, 60, 100, 140, 180, 220}):
    total_signal = 0
    cycle, register = 1, 1

    for i in instructions:
        if i == "noop":
            if cycle in special_cycles:
                total_signal += cycle * register

            cycle += 1
        else:
            executing = 0

            while executing < 2:
                executing += 1

                if cycle in special_cycles:
                    total_signal += cycle * register

                cycle += 1

            register += i[1]

    return total_signal


@timer
def solve_part_2(instructions, crt_rows=6, crt_cols=40):
    cycle, register = 1, 1
    crt = _get_crt(rows=crt_rows, cols=crt_cols)

    # this is where the computer is currently drawing
    draw_row, draw_col = 5, 0

    # if cycle is one of these, we advance to draw in the next row
    cycle_changes = {
        i + 1 for i in range(crt_cols, crt_cols * (crt_rows + 1), crt_cols)
    }

    for i in instructions:
        if i == "noop":
            _draw_pixel(crt, draw_row, draw_col, register)
            cycle += 1

            if cycle in cycle_changes:
                draw_row -= 1
                draw_col = 0
            else:
                draw_col += 1

        else:
            executing = 0

            while executing < 2:
                executing += 1
                _draw_pixel(crt, draw_row, draw_col, register)
                cycle += 1

                if cycle in cycle_changes:
                    draw_row -= 1
                    draw_col = 0
                else:
                    draw_col += 1

            register += i[1]

    return crt


def _draw_pixel(crt, draw_row, draw_col, sprite_pos):
    diff = abs(sprite_pos - draw_col)

    if diff == 1 or diff == 0:
        crt[draw_row][draw_col] = "#"


def _get_crt(rows, cols):
    pixels = [["."] * cols for _ in range(rows)]
    return pixels


def print_crt(crt):
    for row in reversed(crt):
        joined_pixels = "".join(row)
        print(joined_pixels)


if __name__ == "__main__":
    day = 10
    input_path = get_input_path(day)
    data = read_data(input_path)
    instructions = process_data(data)

    part_1 = solve_part_1(instructions)
    print(f"The total signal strength is: {part_1}.")

    part_2 = solve_part_2(instructions)
    print("The CRT is displaying these characters:")
    print_crt(part_2)
