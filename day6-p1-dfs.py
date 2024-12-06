# Guard Gallivant [p1 graph,  p2 optimized]

import pathlib
import os
import sys
from time import time

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


# Part 2: O(k.(m.n))
# k := number of visited cells in Part 1
def is_guard_in_loop(data, start_row, start_col, start_dir):
    visited = set()
    row, col, direction = start_row, start_col, start_dir
    visited.add((row, col, direction))

    while True:
        di, dj = dirs[direction]
        new_row, new_col = row + di, col + dj

        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
            break

        if data[new_row][new_col] == "#":
            direction = turn_map[direction]
        else:
            row, col = new_row, new_col
            # if guard is in the same position with the same dir, then in loop
            if (row, col, direction) in visited:
                return True
            visited.add((row, col, direction))

    return False


count = 0
start = time()
for row, col in visited:
    if data[row][col] == ".":
        data[row][col] = "#"
        if is_guard_in_loop(data, start_row, start_col, start_dir):  # O(m.n)
            count += 1
        data[row][col] = "."  # backtrack

print(f"Part 2 time: {time() - start:.2f}s (vs. 21.42s unoptimized)")
print("Number of ways to place an obstruction that causes a loop:", count)
