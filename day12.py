# Garden Groups

import pathlib
import os
from collections import defaultdict

base_path = pathlib.Path(__file__).parent.resolve()
input_path = os.path.join(base_path, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = [list(line.replace("\n", "")) for line in f.readlines()]

class UnionFind:
    def __init__(self, num_nodes):
        self.root = [i for i in range(num_nodes)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = rootY


def is_valid(i, j):
    return 0 <= i < m and 0 <= j < n


def get_positions():
    pos = {}
    idx = 0
    for i in range(m):
        for j in range(n):
            pos[(i, j)] = idx
            idx += 1
    return pos


def create_graph():
    adj = defaultdict(list)
    for i in range(m):
        for j in range(n):
            dirs = [
                (i-1, j),
                (i, j-1),
                (i+1, j),
                (i, j+1)
            ]
            for di, dj in dirs:
                if is_valid(di, dj) and data[i][j] == data[di][dj]:
                    adj[pos[(i, j)]].append(pos[(di, dj)])
    return adj


m, n = len(data), len(data[0])
uf = UnionFind(m*n)
pos = get_positions()
adj = create_graph()

for node in adj:
    neighbors = adj[node]
    for nei in neighbors:
        uf.union(node, nei)

regions = defaultdict(list)
for node in range(m*n):
    regions[uf.find(node)].append(node)

def get_perimeter(region):
    perim = 0
    for node in region:
        perim += 4 - len(adj[node])
    return perim

def get_area(region):
    return len(region)


def get_region_coords(region):
    coords = []
    coords_map = {k: v for v, k in pos.items()}
    for node in region:
        coords.append(coords_map[node])
    return coords

def convert_to_complex(region):
    return [complex(x, y) for x, y in region]

def get_sides(region):
    sides = 0

    visited = set()
    region = set(get_region_coords(region))
    region = convert_to_complex(region)

    for node in region:
        for direction in (1, -1, 1j, -1j):
            if (node, direction) in visited:
                continue
            visited.add((node, direction))

            if node + direction not in region:
                sides += 1

                # move along the edge in forward direction (90 degrees from current)
                nei = node + direction * 1j
                while nei in region and nei + direction not in region:
                    visited.add((nei, direction))
                    nei += direction * 1j

                # move along the edge in backward direction (-90 degrees from current)
                nei = node - direction * 1j
                while nei in region and nei + direction not in region:
                    visited.add((nei, direction))
                    nei -= direction * 1j

    return sides


# Part 1
price = 0
for root, region in regions.items():
    price += get_area(region) * get_perimeter(region)
print("Fencing price:", price)

# Part 2
price = 0
for root, region in regions.items():
    price += get_area(region) * get_sides(region)
print("Fencing price with bulk discount:", price)
