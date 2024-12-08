from sys import stdin
from collections import defaultdict

city = []
nodes = defaultdict(list)
for i, line in enumerate(stdin):
    city.append(list(line.strip()))
    for j, c in enumerate(line.strip()):
        if c != ".":
            nodes[c].append((i, j))

m = len(city)
n = len(city[0])

# part one
ans = 0
temp_city = [s.copy() for s in city]
for c in nodes.keys():
    for y1, x1 in nodes[c]:
        for y2, x2 in nodes[c]:
            if y1 == y2 and x1 == x2:
                continue

            my = y2 - y1
            mx = x2 - x1

            if 0 <= y1 + my * 2 < m and 0 <= x1 + mx * 2 < n:
                if temp_city[y1 + my * 2][x1 + mx * 2] != "#":
                    temp_city[y1 + my * 2][x1 + mx * 2] = "#"
                    ans += 1

print("part 1:", ans)

# part two
ans = 0
temp_city = [s.copy() for s in city]
for c in nodes.keys():
    for y1, x1 in nodes[c]:
        for y2, x2 in nodes[c]:
            if y1 == y2 and x1 == x2:
                continue

            my = y2 - y1
            mx = x2 - x1
            l = 1

            while 0 <= y1 + my * l < m and 0 <= x1 + mx * l < n:
                if temp_city[y1 + my * l][x1 + mx * l] != "#":
                    temp_city[y1 + my * l][x1 + mx * l] = "#"
                    ans += 1
                l += 1

print("part 2:", ans)
