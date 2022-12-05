"""Advent of Code 2022 utility functions."""

import os


def get_input_path(day):
    """Get the path to the input file for a day."""
    repo = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
    input_file = os.path.join("input", f"day{day}_input.txt")
    input_path = os.path.join(repo, input_file)
    return input_path


def read_data(input_path):
    """Read in the data from a input file for a day."""
    with open(input_path) as f:
        data = f.readlines()
        data = [i.replace("\n", "") for i in data]

    return data
