# Red-Nodes Reports

# n := length of an individual report

import pathlib
import os

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [item.split() for item in data]

def is_increasing_safe(l):  # O(n)
    for i in range(1, len(l)):
        # check increasing
        if l[i-1] >= l[i]:
            return False
        # check adjacent levels
        diff = l[i] - l[i-1]
        if diff < 1 or diff > 3:
            return False
    return True

def is_decreasing_safe(l):  # O(n)
    for i in range(1, len(l)):
        # check decreasing
        if l[i-1] <= l[i]:
            return False
        # check adjacent levels
        diff = l[i-1] - l[i]
        if diff < 1 or diff > 3:
            return False
    return True


# Part 1: O(n)
num_safe = 0
for report in data:
    report = [int(level) for level in report]
    if is_increasing_safe(report) or is_decreasing_safe(report):  # O(n)
        num_safe += 1
print("Number of safe reports:", num_safe)

# Part 2: O(n^2)
num_safe_dampner = 0
for report in data:
    report = [int(level) for level in report]
    if not is_increasing_safe(report) and not is_decreasing_safe(report):  # O(n)
        for k in range(len(report)):  # O(n)
            report_new = report[:k] + report[k+1:]
            if is_increasing_safe(report_new) or is_decreasing_safe(report_new):  # O(n)
                num_safe_dampner += 1
                break
print("Number of safe reports with dampner:", num_safe + num_safe_dampner)