# Hystorian Hysteria

from collections import Counter
import pathlib
import os

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [item.split() for item in data]
data = list(zip(*data))


def convert_to_int(l):
    return [int(i) for i in l]

l1, l2 = data
l1, l2 = convert_to_int(l1), convert_to_int(l2)

assert len(l1) == len(l2)
n = len(l1)

# Part 1
l1.sort()  # nlog(n)
l2.sort()

total_distance = 0
for i in range(n):  # O(n)
    total_distance += abs(l1[i] - l2[i])
print("Total Distance:", total_distance)

# Part 2
similarity_score = 0
l2_count = Counter(l2)  # O(n)
for i in range(n):  # O(n)
    similarity_score += l1[i] * l2_count[l1[i]]
print("Similarity Score", similarity_score)