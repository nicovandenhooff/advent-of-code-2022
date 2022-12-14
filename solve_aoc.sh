#!/bin/bash

echo "Advent of Code 2022 Solutions"
echo "Written by Nico Van den Hooff"
echo

solve_aoc () {
    for ((i=1; i<=$1; i++));
    do
        if ((i < 10)); then
            i=0$i
        fi

        FILE=solutions/day$i.py
        
        if [ -f "$FILE" ]; then
            echo "Day $i solution"
            python "$FILE"
            echo
        else
            echo "Day $i solution not completed yet"
            echo
        fi
    done
}

solve_aoc 25
