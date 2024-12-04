# Ceres Search

# (m, n) := number of rows, number of columns

import pathlib
import os
import re

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [list(row.replace("\n", "")) for row in data]

# Part 1: O(m.n)
word = "XMAS"
m, n = len(data), len(data[0])
xmas_count = 0

def dfs(i, j, dist, visited, direction):
    if dist == len(word):
        return 1
    
    if i<0 or i>= m or j<0 or j>=n or (i, j) in visited or data[i][j] != word[dist]:
        return 0
    visited.add((i, j))
    count = 0

    dirs = [
        (0, -1),  # Left
        (-1, -1), # Top-left
        (-1, 0),  # Top
        (-1, 1),  # Top-right
        (0, 1),   # Right
        (1, 1),   # Bottom-right
        (1, 0),   # Bottom
        (1, -1),  # Bottom-left
    ]
    if direction is None:
        for di, dj in dirs:
            count += dfs(i+di, j+dj, dist+1, visited, (di, dj))
    else:
        di, dj = direction
        count += dfs(i+di, j+dj, dist+1, visited, direction)
    
    visited.remove((i, j))
    return count

for row in range(m):
    for col in range(n):
        if data[row][col] == word[0]:
            xmas_count += dfs(row, col, 0, set(), None)

print("xmas count:", xmas_count)

# Part 2: O(m.n)
def is_valid(a, b, c, d):
    target = ["M", "S"]
    if sorted([a, d]) == target and sorted([b, c]) == target:
        return True
    return False

x_mas_count = 0

for row in range(1, m-1):
    for col in range(1, n-1):
        if data[row][col] == "A":
            left_up, right_up = data[row-1][col-1], data[row-1][col+1]
            left_down, right_down = data[row+1][col-1], data[row+1][col+1]
            if is_valid(left_up, right_up, left_down, right_down):
                x_mas_count += 1
print("x-mas count:", x_mas_count)
