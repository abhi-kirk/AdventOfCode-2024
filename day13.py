# Claw Contraption

import pathlib
import os
import re
import sympy as sym

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

def get_xy(item, prize=False):
    if prize:
        pattern = r"X\=(\d+), Y\=(\d+)"
    else:
        pattern = r"X\+(\d+), Y\+(\d+)"
    x, y = re.findall(pattern, item)[0]
    return int(x), int(y)


button_a, button_b, prize = [], [], []
for item in data:
    if "Button A" in item:
        button_a.append(get_xy(item))
    elif "Button B" in item:
        button_b.append(get_xy(item))
    elif "Prize" in item:
        prize.append(get_xy(item, prize=True))

machines = list(zip(button_a, button_b, prize))

def is_valid(solution):
    return isinstance(solution[x], sym.core.numbers.Integer) and isinstance(solution[y], sym.core.numbers.Integer)


def solve_machine(machine, p_offset=0):
    a, b, p = machine
    p = (p[0] + p_offset, p[1] + p_offset)
    eq1 = sym.Eq(a[0] * x + b[0] * y, p[0])
    eq2 = sym.Eq(a[1] * x + b[1] * y, p[1])
    return sym.solve((eq1, eq2), (x, y))


# Part 1
tokens_total = 0
for machine in machines:
    x, y = sym.symbols("x y")
    solution = solve_machine(machine)
    if is_valid(solution):
        tokens_total += solution[x] * 3 + solution[y]
print("Total tokens:", tokens_total)

# Part 2
tokens_total = 0
for machine in machines:
    x, y = sym.symbols("x y")
    solution = solve_machine(machine, p_offset=10000000000000)
    if is_valid(solution):
        tokens_total += solution[x] * 3 + solution[y]
print("Total tokens with offset:", tokens_total)
