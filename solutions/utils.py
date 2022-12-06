"""Advent of Code 2022 utility functions."""

import os, time


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


def timer(func):
    """Decorator function used to time another function."""

    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__!r} executed in {(end-start):.4f}s!")
        return result

    return wrapped_func
