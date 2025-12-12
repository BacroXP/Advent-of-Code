import libs.input
from collections import defaultdict

points = [[int(x) for x in line.split(',')] for line in libs.input.file()]
parent = {i: i for i in range(len(points))}
edges = []


def find_root(node):
    if parent[node] == node:
        return node

    parent[node] = find_root(parent[node])

    return parent[node]


def union(a, b):
    parent[find_root(a)] = find_root(b)


for i, (x1, y1, z1) in enumerate(points):
    for j, (x2, y2, z2) in enumerate(points):
        if i > j:
            dist2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((dist2, i, j))

edges.sort()
connected = 0

for idx, (_, a, b) in enumerate(edges):
    if idx == 1000:
        component_size = defaultdict(int)

        for node in range(len(points)):
            root = find_root(node)
            component_size[root] += 1

        sizes = sorted(component_size.values())

        print(sizes[-1] * sizes[-2] * sizes[-3])

    if find_root(a) != find_root(b):
        connected += 1

        if connected == len(points) - 1:
            print(points[a][0] * points[b][0])

        union(a, b)
