# Guard Gallivant [with graph algorithms]

import pathlib
import os

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "test.txt")

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


print("Number of distinct positions:", len(visited))


# Part 2: O((m.n)^2)

print("Number of ways to place an obstruction that causes a loop:", count)