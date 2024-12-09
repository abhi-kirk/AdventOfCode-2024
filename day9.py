# Disk Fragmenter

import pathlib
import os
import copy

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [i for i in list(f.read())]

blocks = []
idx = 0
for i in range(len(data)):
    if i % 2 == 0:  # block len
        for j in range(int(data[i])):
            blocks.append(str(idx))
        idx += 1
    else:  # free space
        for j in range(int(data[i])):
            blocks.append(".")

# Part 1
blocks_p1 = copy.deepcopy(blocks)
left, right = 0, len(blocks_p1)-1
while left < right:
    if blocks_p1[left] == ".":
        while blocks_p1[right] == ".":
            right -= 1
        blocks_p1[left], blocks_p1[right] = blocks_p1[right], blocks_p1[left]
    else:
        left += 1

s = 0
for i in range(len(blocks_p1)):
    if blocks_p1[i] != ".":
        s += i * int(blocks_p1[i])
print("Checksum:", s)
