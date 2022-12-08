# --- Day 8: Treetop Tree House ---
# https://adventofcode.com/2022/day/8#part2
# NumPy is blazing fast!

import numpy as np
from utils import get_input_path, read_data, timer


def process_data(data):
    trees = []

    for nums in data:
        trees.append(np.array([int(n) for n in nums]))

    trees = np.array(trees)

    return trees


@timer
def solve_part_1(trees):
    nrow, ncol = trees.shape
    visible = np.zeros_like(trees)

    # edge trees are always visible
    visible[0, :] = 1
    visible[:, 0] = 1
    visible[-1, :] = 1
    visible[:, -1] = 1

    # find the other visible trees
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            tree = trees[i, j]

            # look left
            if (trees[i, 0:j] < tree).all():
                visible[i, j] = 1

            # look right
            elif (trees[i, j + 1 :] < tree).all():
                visible[i, j] = 1

            # look up
            elif (trees[0:i, j] < tree).all():
                visible[i, j] = 1

            # look down
            if (trees[i + 1 :, j] < tree).all():
                visible[i, j] = 1

    return visible.sum()


@timer
def solve_part_2(trees):
    nrow, ncol = trees.shape
    scenic_score = np.zeros_like(trees)

    # edge trees always 0, so skip them
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            tree = trees[i, j]

            # slices of each directional view
            left = np.where(trees[i, 0:j] >= tree, 1, 0)
            right = np.where(trees[i, j + 1 :] >= tree, 1, 0)
            up = np.where(trees[0:i, j] >= tree, 1, 0)
            down = np.where(trees[i + 1 :, j] >= tree, 1, 0)

            # left and up flipped to evaluate distance from R -> L in array
            left_view = _viewing_distance(np.flip(left))
            right_view = _viewing_distance(right)
            up_view = _viewing_distance(np.flip(up))
            down_view = _viewing_distance(down)

            scenic_score[i, j] = left_view * right_view * up_view * down_view

    return scenic_score.max()


def _viewing_distance(direction):
    distance = 0

    for t in direction:
        distance += 1

        # this means our view is blocked
        if t == 1:
            break

    return distance


if __name__ == "__main__":
    day = 8
    input_path = get_input_path(day)
    data = read_data(input_path)
    trees = process_data(data)

    part_1 = solve_part_1(trees)
    print(f"{part_1} trees are visible outside the grid.")

    part_2 = solve_part_2(trees)
    print(f"The highest scenic score possible is {part_2}.")
