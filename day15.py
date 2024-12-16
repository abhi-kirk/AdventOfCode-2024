# Warehouse Woes

import pathlib
import os

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [list(line.replace("\n", "")) for line in f.readlines()]

grid, instructions = [], ""
for line in data:
    if "#" in line:
        grid.append(line)
    elif len(line) > 0:
        instructions += "".join(line)

m, n = len(grid), len(grid[0])

DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


def find_robot(grid):
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "@":
                return row, col

def find_box(grid):
    for row in range(m):
        for col in range(n):
            if grid[row][col] in ["O", "["]:
                yield row, col

def is_valid(grid, row, col):
    return 0 <= row < m and 0 <= col < n and grid[row][col] != "#"


def check_movable(grid, row, col, dr, dc, seen):
    if (row, col) in seen:
        return True
    seen.add((row, col))

    nr, nc = row + dr, col + dc
    if grid[nr][nc] == "#":
        return False
    elif grid[nr][nc] == "[":
        return check_movable(grid, nr, nc, dr, dc, seen) and check_movable(
            grid, nr, nc + 1, dr, dc, seen
        )
    elif grid[nr][nc] == "]":
        return check_movable(grid, nr, nc, dr, dc, seen) and check_movable(
            grid, nr, nc - 1, dr, dc, seen
        )
    elif grid[nr][nc] == "O":
        return check_movable(grid, nr, nc, dr, dc, seen)
    return True


def process_instruction(grid, row, col, instruction):
    dr, dc = DIRECTIONS[instruction]
    nr, nc = row + dr, col + dc

    if not is_valid(grid, nr, nc):
        return row, col

    if grid[nr][nc] in ["[", "]", "O"]:
        seen = set()

        if not check_movable(grid, row, col, dr, dc, seen):
            return row, col

        while len(seen) > 0:
            for r, c in seen.copy():
                nr2, nc2 = r + dr, c + dc
                if (nr2, nc2) not in seen:
                    if grid[nr2][nc2] != "@" and grid[r][c] != "@":
                        grid[nr2][nc2] = grid[r][c]
                        grid[r][c] = "."

                    seen.remove((r, c))

        grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
        return nr, nc

    grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
    return nr, nc


def gps(grid):
    return sum(100 * box[0] + box[1] for box in find_box(grid))


# Part 1
row, col = find_robot(grid)
for instruction in instructions:
    row, col = process_instruction(grid, row, col, instruction)

print("GPS Part-1:", gps(grid))


# Part 2
initial_grid = grid
grid = []

# expand the grid
for row in range(m):
    if len(grid) <= row or row not in grid:
        grid.append([])

    for col in range(n):
        ch = initial_grid[row][col]
        if ch == "#":
            grid[row].extend(["#", "#"])
        elif ch == "O":
            grid[row].extend(["[", "]"])
        elif ch == ".":
            grid[row].extend([".", "."])
        elif ch == "@":
            grid[row].extend(["@", "."])

m, n = len(grid), len(grid[0])
row, col = find_robot(grid)
for instruction in instructions:
    row, col = process_instruction(grid, row, col, instruction)

print("GPS Part-2:", gps(grid))
