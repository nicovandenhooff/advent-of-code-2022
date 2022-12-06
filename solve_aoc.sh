#!/bin/bash

echo "Advent of Code 2022 Solutions"
echo "Written by Nico Van den Hooff"
echo

solve_aoc () {
    for ((i=1; i<=$1; i++));
    do
        FILE=solutions/day$i.py
        if [ -f "$FILE" ]; then
            echo "Day $i solution"
            python "$FILE"
            echo
        fi
    done
}

solve_aoc 25
