# Hoof It

import pathlib
import os
from time import time

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [[int(i) for i in list(item.replace("\n", ""))] for item in data]

trailheads = []
m, n = len(data), len(data[0])
for row in range(m):
    for col in range(n):
        if data[row][col] == 0:
            trailheads.append((row, col))

dirs = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0)
]

def dfs(i, j, visited, target, cycles_allowed=False):
    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
        return 0
    if data[i][j] != target:
        return 0

    if not cycles_allowed:
        visited.add((i, j))

    if data[i][j] == 9:
        return 1

    score = 0
    for di, dj in dirs:
        score += dfs(i+di, j+dj, visited, target+1, cycles_allowed=cycles_allowed)

    return score

def dfs_memo(i, j, target, memo):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    if data[i][j] != target:
        return 0

    if (i, j, target) in memo:
        return memo[(i, j, target)]

    if data[i][j] == 9:
        return 1

    score = 0
    for di, dj in dirs:
        score += dfs_memo(i+di, j+dj, target+1, memo)

    memo[(i, j, target)] = score
    return score


# Part 1: O(m.n)
s = 0
for row, col in trailheads:
    s += dfs(row, col, set(), 0, {})
print("Sum of scores:", s)

# Part 2: O(4^(m.n))
s = 0
start = time()
for row, col in trailheads:
    s += dfs(row, col, set(), 0, cycles_allowed=True)
print(f"Part 2 Execution time (DFS only): {time() - start:.4f}s")
print("Sum of scores with cycles:", s)

# Part 2 with memoization: O(m.n)
s = 0
start = time()
for row, col in trailheads:
    s += dfs_memo(row, col, 0, {})
print(f"Part 2 Execution time (DFS with memo): {time() - start:.4f}s")
print("Sum of scores with cycles:", s)
