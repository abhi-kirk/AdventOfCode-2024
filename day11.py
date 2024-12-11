# Plutonian Pebbles

# n := number of stones per blink

import pathlib
import os
from collections import defaultdict, Counter

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.read()

stones = data.split()

def rules(num):
    if int(num) == 0:
        return ["1"]
    elif len(num) % 2 == 0:
        mid = len(num) // 2
        s1 = int(num[:mid])
        s2 = int(num[mid:])
        return [str(s1), str(s2)]
    else:
        return [str(int(num) * 2024)]


# Part 1: O(n)
blinks = 25
for _ in range(blinks):
    stones_new = []
    for stone in stones:
        stones_new.extend(rules(stone))
    stones = stones_new
print(f"num of stones for {blinks} blinks:", len(stones))


# Part 2: O(n)
stones = data.split()
count = Counter(stones)

blinks = 75
for _ in range(blinks):
    count_new = defaultdict(int)
    for stone, freq in count.items():
        for stone_new in rules(stone):
            count_new[stone_new] += freq
    count = count_new

print(f"num of stones for {blinks} blinks:", sum(count.values()))
