# Guard Gallivant [with graph algorithms]

import pathlib
import os
import sys
from collections import defaultdict

sys.setrecursionlimit(10_000)

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [list(line.replace("\n", "")) for line in data]

# Part 1: O(m.n)
pos_map = {
    "^": "up",
    "<": "left",
    ">": "right",
    "v": "down"
}
m, n = len(data), len(data[0])
for row in range(m):
    for col in range(n):
        if data[row][col] in pos_map:
            start_row, start_col = row, col
            start_dir = pos_map[data[row][col]]

turn_map = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

dirs = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def dfs(i, j, direction, visited):
    di, dj = dirs[direction]
    i_new, j_new = i+di, j+dj

    if i_new < 0 or i_new >= m or j_new < 0 or j_new >= n:
        return visited

    if data[i_new][j_new] == "#":
        direction = turn_map[direction]
        dfs(i, j, direction, visited)
    else:
        visited.add((i_new, j_new))
        dfs(i_new, j_new, direction, visited)

    return visited


visited = dfs(start_row, start_col, start_dir, set())
print("Number of distinct positions:", len(visited))


# Part 2: O((m.n)^2)
def build_graph(path):
    pass


def is_cycle_kahns(i, j, direction, visited, grid):
    # create graph
    di, dj = dirs[direction]
    i_new, j_new = i+di, j+dj
    if i_new < 0 or i_new >= m or j_new < 0 or j_new >= n:
        return False

    pass


count = 0
for i, j in visited:
    data[i][j] = "#"
    graph, nodes = build_graph(path)
    if is_cycle_kahns(graph, nodes):
        count += 1
    data[i][j] = "."

print("Number of ways to place an obstruction that causes a loop:", count)
