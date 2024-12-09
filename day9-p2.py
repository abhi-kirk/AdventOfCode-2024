# Disk Fragmenter

# Part 2: O(n^3)

import pathlib
import os
from time import time

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [int(i) for i in list(f.read())]

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

max_file_id = idx

def find_block(blocks, block_id):  # O(n)
    # find the start position and len of a given block
    block_id = str(block_id)
    start = blocks.index(block_id)
    block_len = len([i for i in blocks if i == block_id])
    return start, block_len


def find_space(blocks, block_len):  # O(n^2)
    # find free space, starting from left, of block_len
    for idx, char in enumerate(blocks):
        if char != ".":
            continue
        for i in range(block_len):
            idx_next = idx + i
            if idx_next < len(blocks) and blocks[idx_next] != ".":
                break  # found
        else:
            return idx


tstart = time()
# traverse from left <- right
for block_id in range(max_file_id-1, -1, -1):  # O(n)
    block_start, block_len = find_block(blocks, block_id)  # O(n)
    block_end = block_start + block_len

    free_index_start = find_space(blocks, block_len)  # O(n)
    if free_index_start is None or free_index_start > block_start:
        continue
    free_index_end = free_index_start + block_len

    # swap blocks
    blocks[free_index_start:free_index_end], blocks[block_start:block_end] = (
        blocks[block_start:block_end], blocks[free_index_start:free_index_end])

s = 0
for i in range(len(blocks)):
    if blocks[i] != ".":
        s += i * int(blocks[i])
print(f"Part 2 Execution time: {time() - tstart:.2f}s")
print("Checksum:", s)

