# Restroom Redoubt

import pathlib
import os
import re

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [line.replace("\n", "") for line in f.readlines()]


def get_pv(robot):
    pattern = r"p=(\d+,\d+) v=(-?\d+,-?\d+)"
    p, v = re.findall(pattern, robot)[0]
    p = [int(i) for i in p.split(",")][::-1]  # row, col
    v = [int(i) for i in v.split(",")][::-1]  # row-offset, col-offset
    return p, v


def convert_to_complex(coord):
    x, y = coord
    return complex(x, y)

def move_robot(pos, vel, t):
    pos = convert_to_complex(pos)
    vel = convert_to_complex(vel)

    for _ in range(t):
        pos += vel
        if pos.real < 0 or pos.real >= m:
            pos = complex(pos.real % m, pos.imag)
        if pos.imag < 0 or pos.imag >= n:
            pos = complex(pos.real, pos.imag % n)
    grid[int(pos.real)][int(pos.imag)] += 1
    return [int(pos.real), int(pos.imag)]


def get_safety_factor():
    mid_row = m // 2
    mid_col = n // 2

    quadrants = {
        "top_left": [(i, j) for i in range(mid_row) for j in range(mid_col)],
        "top_right": [(i, j) for i in range(mid_row) for j in range(mid_col + (n % 2), n)],
        "bottom_left": [(i, j) for i in range(mid_row + (m % 2), m) for j in range(mid_col)],
        "bottom_right": [(i, j) for i in range(mid_row + (m % 2), m) for j in range(mid_col + (n % 2), n)]
    }
    safety = 1
    for _, indices in quadrants.items():
        safety *= sum(grid[i][j] for i, j in indices)
    return safety


# Part 1
m, n = 103, 101  # rows, cols
# m, n = 7, 11
t = 100
grid = [[0] * n for i in range(m)]

for robot in data:
    pos, vel = get_pv(robot)
    move_robot(pos, vel, t)
print("Safety factor:", get_safety_factor())

# Part 2

def get_init_pv():
    pv = []
    for robot in data:
        pos, vel = get_pv(robot)
        pv.append([pos, vel])
    return pv


m, n = 103, 101  # rows, cols
grid = [[0] * n for i in range(m)]
pv = get_init_pv()

seconds = 0
while True:
    positions = set()
    for i in range(len(pv)):
        pos, vel = pv[i]
        positions.add(tuple(pos))
        pos_new = move_robot(pos, vel, 1)
        pv[i][0] = pos_new

    if len(set(positions)) == len(data):  # all robots in unique positions
        break
    seconds += 1

print("Seconds till Christmas tree:", seconds)
