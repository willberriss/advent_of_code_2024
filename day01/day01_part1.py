#!/usr/bin/env python3

import os
from operator import sub, abs

def day01_part1(filename: str):
    f = open(filename, "r")
    (a, b) = read_two_column_file(filename)
    a.sort()
    b.sort()
    deltas = []
    #result1 = map(sub, b, a)
    result2 = map(lambda x, y: abs(x - y), a, b)
    deltas = list(result2)
    total = sum(deltas)
    print(f"total: {total}")
    return total

def read_two_column_file(filename):
    with open(filename, 'r') as data:
        x = []
        y = []
        for line in data:
            cols = line.split()
            x.append(int(cols[0]))
            y.append(int(cols[1]))
    return x, y

