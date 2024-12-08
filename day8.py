# Resonant Collinearity

import pathlib
import os
from collections import defaultdict
import math

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()

data = [list(item.replace("\n", "")) for item in data]

ints = [str(num) for num in range(10)]
chars = [chr(ch + 97) for ch in range(26)]
chars += [ch.upper() for ch in chars]
ants = ints + chars

# Part 1
antennas = defaultdict(list)

m, n = len(data), len(data[0])
for row in range(m):
    for col in range(n):
        if data[row][col] in ants:
            antennas[data[row][col]].append((row, col))


def get_combinations(arr):
    res = []

    def backtrack(start, path):
        if len(path) == 2:
            res.append(path[:])

        for i in range(start, len(arr)):
            node = arr[i]
            if node in path:
                continue
            path.append(node)
            backtrack(i, path)
            path.pop()

    backtrack(0, [])
    return res

def is_valid(i, j):
    if 0 <= i < m and 0 <= j < n:
        return True
    return False

def get_antinodes(n1, n2, get_all=False):
    res = set()

    row_diff, col_diff = abs(n1[0] - n2[0]), abs(n1[1] - n2[1])

    x1, x2 = min(n1[0], n2[0]) - row_diff, max(n1[0], n2[0]) + row_diff
    if n1[1] >= n2[1]:
        y1, y2 = max(n1[1], n2[1]) + col_diff, min(n1[1], n2[1]) - col_diff
    else:
        y1, y2 = min(n1[1], n2[1]) - col_diff, max(n1[1], n2[1]) + col_diff

    if is_valid(x1, y1):
        res.add((x1, y1))
    if is_valid(x2, y2):
        res.add((x2, y2))

    if get_all:
        res.add(n1)
        res.add(n2)

        row_step = n2[0] - n1[0]
        col_step = n2[1] - n1[1]
        step = math.gcd(row_diff, col_diff)

        row_step //= step
        col_step //= step

        x, y = n1[0] - row_step, n1[1] - col_step
        while is_valid(x, y):
            res.add((x, y))
            x -= row_step
            y -= col_step

        x, y = n2[0] + row_step, n2[1] + col_step
        while is_valid(x, y):
            res.add((x, y))
            x += row_step
            y += col_step
    return res


antinodes_all = set()
for ant in antennas:
    locs_combinations = get_combinations(antennas[ant])
    for node1, node2 in locs_combinations:
        antinodes = get_antinodes(node1, node2)
        antinodes_all = antinodes_all.union(antinodes)

print("Number of antinode locations:", len(antinodes_all))


# Part 2
antinodes_all = set()
for ant in antennas:
    locs_combinations = get_combinations(antennas[ant])
    for node1, node2 in locs_combinations:
        antinodes = get_antinodes(node1, node2, get_all=True)
        antinodes_all = antinodes_all.union(antinodes)

print("Number of updated antinode locations:", len(antinodes_all))
