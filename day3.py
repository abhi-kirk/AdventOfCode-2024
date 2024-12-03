# Mull It Over

# n := length of input string
# m := number of matches

import pathlib
import os
import re

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.read()

# Part 1: O(n)
pattern = r"mul\((\d+),(\d+)\)"
valid_seqs = re.findall(pattern, data)  # O(n)

s = 0
for a, b in valid_seqs:  # O(m)
    a, b = int(a), int(b)
    s += a * b
print(f"Result of multiplications:", s)

# Part 2: O(n)
muls = [(match.start(), match.end()) for match in re.finditer(pattern, data)]  # O(n)
dos = [match.start() for match in re.finditer(r"do\(\)", data)]  # O(n)
donts = [match.start() for match in re.finditer(r"don't\(\)", data)]  # O(n)

def get_sum(mul):  # O(1)
    a, b = re.findall(r"mul\((\d+),(\d+)\)", mul)[0]
    return int(a) * int(b)

s = 0
enabled = True
for i in range(len(data)):  # O(n)
    if len(donts) > 0 and donts[0] == i:
        donts = donts[1:]
        enabled = False
    elif len(dos) > 0 and dos[0] == i:
        dos = dos[1:]
        enabled = True
    elif len(muls) > 0 and muls[0][0] == i:
        if enabled:
            mul = data[muls[0][0]:muls[0][1]]
            s += get_sum(mul)
        muls = muls[1:]
print("New instructions multiplications:", s)