# Resonant Collinearity

# f := number of frequencies
# k := number of antennas per freq

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

antennas = defaultdict(list)

m, n = len(data), len(data[0])
for row in range(m):  # O(m.n)
    for col in range(n):
        if data[row][col] in ants:
            antennas[data[row][col]].append((row, col))


# def get_combinations(arr):
#     res = []
#
#     def backtrack(start, path):
#         if len(path) == 2:
#             res.append(path[:])
#
#         for i in range(start, len(arr)):
#             node = arr[i]
#             if node in path:
#                 continue
#             path.append(node)
#             backtrack(i, path)
#             path.pop()
#
#     backtrack(0, [])
#     return res

def is_valid(i, j):
    if 0 <= i < m and 0 <= j < n:
        return True
    return False

def get_collinear_points(points, get_all=False):
    res = set()

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            if get_all:  # add self
                res.add((x1, y1))
                res.add((x2, y2))

            # get direction vector
            dy, dx = y2 - y1, x2 - x1

            # normalize to get smallest step in direction
            divisor = math.gcd(abs(dy), abs(dx))
            dy //= divisor
            dx //= divisor

            # find collinear points: backward
            x, y = x1 - dx, y1 - dy
            if is_valid(x, y):
                res.add((x, y))
            if get_all:
                while is_valid(x, y):
                    res.add((x, y))
                    x -= dx
                    y -= dy

            # find collinear points: forward
            x, y = x2 + dx, y2 + dy
            if is_valid(x, y):
                res.add((x, y))
            if get_all:
                while is_valid(x, y):
                    res.add((x, y))
                    x += dx
                    y += dy

    return res


# Part 1: O(m.n) + O(f.k^2)
antinodes_all = set()
for freq, freq_antennas in antennas.items():  # O(f)
    antinodes_all.update(get_collinear_points(freq_antennas))  # O(k^2): number of pairs
print("Number of antinode locations:", len(antinodes_all))


# Part 2: O(m.n) + O(f.max(m,n).k^2)
antinodes_all = set()
for freq, freq_antennas in antennas.items():  # O(f)
    antinodes_all.update(get_collinear_points(freq_antennas, get_all=True))  # O(max(m, n) . k^2)
print("Number of updated antinode locations:", len(antinodes_all))
