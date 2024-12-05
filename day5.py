# Print Queue

import pathlib
import os
import re
from collections import defaultdict

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
ordering = [line.replace("\n", "") for line in data if "|" in line]
updates = [line.replace("\n", "") for line in data if "," in line]

# Part 1
adj = defaultdict(list)
for order in ordering:
    a, b = order.split("|")
    adj[a].append(b)

s = 0
invalids = []
for update in updates:
    invalid = False
    update = update.split(",")
    n = len(update)
    for i in range(n):
        check = update[i]
        for j in range(i+1, n):
            target = update[j]
            if target not in adj[check]:
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        s += int(update[n//2])
    else:
        invalids.append(update)

print("correct order mid page sum:", s)

# Part 2
s = 0
for update in invalids:
    n = len(update)
    res = []
    i = 0
    while len(res) < n:
        el = update[i]
        elmap = adj[el]
        rest = update[1:]
        if len(set(elmap).intersection(rest)) == 0:
            res.append(el)
            update.remove(el)
            i = 0
        else:
            i += 1
    res = res[::-1]
    s += int(res[n//2])

print("corrected order mid page sum", s)