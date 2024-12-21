from sys import stdin
from timeit import default_timer
from collections import deque

grid = []
sx, sy = -1, -1
ex, ey = -1, -1
for line in stdin:
    grid.append([c for c in line.strip()])
    if "S" in grid[-1]:
        sx = grid[-1].index("S")
        sy = len(grid) - 1
        grid[sy][sx] = "."
    if "E" in grid[-1]:
        ex = grid[-1].index("E")
        ey = len(grid) - 1
        grid[ey][ex] = "."

m = len(grid)
n = len(grid[0])

# part one
start_time = default_timer()
ans = 0
dist = [[-1] * n for _ in range(m)]
dist[sy][sx] = 0
path_nodes = set([(sx, sy)])

# regular bfs for inital lengths
q = deque([(sx, sy)])
while len(q) > 0:
    x, y = q.popleft()
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if dist[ny][nx] < 0 and grid[ny][nx] != '#':
            q.append((nx, ny))
            dist[ny][nx] = dist[y][x] + 1
            path_nodes.add((nx, ny))

# bfs with 1 cheat allowed
q = deque([(sx, sy, 0)]) # x, y, d
seen = [[False] * n for _ in range(m)]
seen[sy][sx] = True
while len(q) > 0:
    x, y, d = q.popleft()
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[y][x] == "#" and grid[ny][nx] == "." and dist[ny][nx] - d - 1 >= 100:
                ans += 1
            elif grid[y][x] == "." and not seen[ny][nx]:
                q.append((nx, ny, d + 1))
                seen[ny][nx] = True

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
for ox, oy in path_nodes:
    q = deque([(ox, oy)]) # x, y
    seen = set([(ox, oy)])
    while len(q) > 0:
        x, y = q.popleft()

        d = abs(ox - x) + abs(oy - y)
        new_dist = dist[oy][ox] + d
        if grid[y][x] == "." and new_dist < dist[y][x]:
            if dist[y][x] - new_dist >= 100:
                ans += 1

        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in seen or abs(ox - nx) + abs(oy - ny) > 20: continue
            q.append((nx, ny))
            seen.add((nx, ny))

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

# fuck
# misinterpreted the problem
'''
def merge(l1: dict, l2: dict):
    res = l1.copy()
    for t in l2.keys():
        if t not in res or l2[t] < res[t]:
            res[t] = l2[t]
    return res

wall_dists = {}
for i in range(n):
    for j in range(m):
        if grid[j][i] != "#": continue

        q = deque([(i, j, 0)]) # x, y, d
        seen = set((i, j))
        res = {}
        while len(q) > 0:
            x, y, d = q.popleft()
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m) or d >= 19 or (nx, ny) in seen: continue
                if grid[ny][nx] == ".":
                    res[(nx, ny)] = d + 1
                elif (nx, ny) in wall_dists:
                    p = {}
                    for k, v in wall_dists[(nx, ny)].items():
                        if v + d + 1 <= 20:
                            p[k] = v + d + 1
                    res = merge(res, p)
                else:
                    q.append((nx, ny, d + 1))

                seen.add((nx, ny))
        wall_dists[(i, j)] = res

q = deque([(sx, sy)])
seen = set([(sx, sy)])
count = [0 for _ in range(100)]
while len(q) > 0:
    x, y = q.popleft()
    r = {}
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m): continue
        if grid[ny][nx] == '.' and (nx, ny) not in seen:
            q.append((nx, ny))
            seen.add((nx, ny))
        elif grid[ny][nx] == '#':
            r = merge(r, wall_dists[(nx, ny)])
    # print(x, y, r)
    for (tx, ty), d in r.items():
        # print(dist[ty][tx] - d - 1)
        if dist[ty][tx] - d - 1 > 0:
            count[dist[ty][tx] - d - 1] += 1
        # if dist[ty][tx] - d - 1 >= 100:
        #     count[dist[ty]]
        #     ans += 1

    # c = [row.copy() for row in grid]
    # c[y][x] = "@"
    # for K, V in r.items():
    #     c[K[1]][K[0]] = V
    # print(x, y)
    # for r in c:
    #     print("".join([str(C).ljust(3) for C in r]))
    # break

for i, d in enumerate(count):
    print(i, d)

# for k, v in wall_dists.items():
#     c = [row.copy() for row in grid]
#     c[k[1]][k[0]] = "@"
#     for K, V in v.items():
#         c[K[1]][K[0]] = V
#     print(k)
#     for r in c:
#         print("".join([str(C).ljust(3) for C in r]))
'''
