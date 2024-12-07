# Bridge Repair

import pathlib
import os
from time import time

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.readlines()

data = [item.replace("\n", "") for item in data]

# Part 1: Backtracking O(n.2^(n-1))
def is_valid(arr, target, ops_possible):
    n = len(arr) - 1  # number of ops for arr

    def compute(ops):
        curr = arr[0]
        for i in range(len(ops)):
            num1, num2 = curr, arr[i+1]
            if ops[i] == "+":
                curr = num1 + num2
            elif ops[i] == "*":
                curr = num1 * num2
            elif ops[i] == "||":
                curr = int(str(num1)+str(num2))
        return curr

    def backtrack(path):
        if len(path) == n:
            res = compute(path)
            if res == target:
                return True
            return False

        for op in ops_possible:
            path.append(op)
            if backtrack(path):
                return True
            path.pop()
        return False

    return backtrack([])


s = 0
for eqn in data:
    test_val = int(eqn.split(":")[0])
    nums = [int(num) for num in eqn.split(":")[1].split()]
    if is_valid(nums, test_val, ["+", "*"]):
        s += test_val

print("Total calibration result:", s)

# Part 2: O(n.3^(n-1))
s = 0
start = time()
for eqn in data:
    test_val = int(eqn.split(":")[0])
    nums = [int(num) for num in eqn.split(":")[1].split()]
    if is_valid(nums, test_val, ["+", "*", "||"]):
        s += test_val

print(f"Part 2 Execution time: {time() - start:.2f}s")
print("Total updated calibration result:", s)
