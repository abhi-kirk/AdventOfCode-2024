# Guard Gallivant

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

visited = set()
row, col, dir = start_row, start_col, start_dir
visited.add((row, col))

while True:
    di, dj = dirs[dir]
    new_row, new_col = row + di, col + dj

    if new_row<0 or new_row>=m or new_col<0 or new_col>=n:
        break

    if data[new_row][new_col] == "#":
        dir = turn_map[dir]
    else:
        row, col = new_row, new_col
        visited.add((row, col)) 

print("Number of distinct positions:", len(visited))


# Part 2: O((m.n)^2)

def is_guard_in_loop(data, start_row, start_col, start_dir):
    visited = set()  
    row, col, dir = start_row, start_col, start_dir
    visited.add((row, col, dir))

    while True:
        di, dj = dirs[dir]
        new_row, new_col = row + di, col + dj

        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
            break

        if data[new_row][new_col] == "#":
            dir = turn_map[dir]
        else:
            row, col = new_row, new_col
            # if guard is in the same position with the same dir, then in loop
            if (row, col, dir) in visited:
                return True
            visited.add((row, col, dir))

    return False

count = 0

for row in range(m):
    for col in range(n):
        if data[row][col] == ".":
            data[row][col] = "#"
            if is_guard_in_loop(data, start_row, start_col, start_dir):  # O(m.n)
                count += 1
            data[row][col] = "."  # backtrack

print("Number of ways to place an obstruction that causes a loop:", count)