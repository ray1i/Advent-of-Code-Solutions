from sys import stdin
from timeit import default_timer
import heapq
from collections import deque

grid = []
ox, oy = -1, -1
ex, ey = -1, -1
for line in stdin:
    grid.append([c for c in line.strip()])
    if "S" in line:
        ox = line.strip().find("S")
        oy = len(grid) - 1
    if "E" in line:
        ex = line.strip().find("E")
        ey = len(grid) - 1

m = len(grid)
n = len(grid[0])

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# part one
start_time = default_timer()
ans = 0
min_d = [[-1] * n for _ in range(m)]
q = [(0, 1, ox, oy)]  # dist, dir, x, y
while min_d[ey][ex] <= -1:
    d, dir, x, y = heapq.heappop(q)
    for i in range(len(dirs)):
        dx, dy = dirs[i]
        nx, ny = x + dx, y + dy
        dist = d + 1 + (abs(dir - i) % 2) * 1000
        if min_d[ny][nx] <= -1 and grid[ny][nx] != "#":
            min_d[ny][nx] = dist
            heapq.heappush(q, (dist, i, nx, ny))

ans = min_d[ey][ex]
end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
min_d = [[[-1] * n for _ in range(m)] for __ in range(len(dirs))]
min_d[1][oy][ox] = 0
prev = [[[[] for __ in range(n)] for _ in range(m)] for ___ in range(len(dirs))]
q = [(0, 1, ox, oy)]  # dist, dir, x, y
while len(q) > 0:
    d, dir, x, y = heapq.heappop(q)

    # rotate:
    for i in [1, 3]:
        new_dir = (dir + i) % 4
        dist = d + 1000  # 1000 since we just turn once
        if min_d[new_dir][y][x] <= -1:
            min_d[new_dir][y][x] = dist
            heapq.heappush(q, (dist, new_dir, x, y))
        if dist <= min_d[new_dir][y][x]:
            prev[new_dir][y][x].append((dir, x, y))

    # straight:
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]
    dist = d + 1
    if grid[ny][nx] != "#":
        if min_d[dir][ny][nx] <= -1:
            if grid[ny][nx] != "E":
                min_d[dir][ny][nx] = dist
                heapq.heappush(q, (dist, dir, nx, ny))
            else:
                for j in range(len(dirs)):
                    min_d[j][ny][nx] = dist
        if dist <= min_d[dir][ny][nx]:
            prev[dir][ny][nx].append((dir, x, y))

q = deque(sum([prev[i][ey][ex] for i in range(len(dirs))], []))
seen = [[False] * n for _ in range(m)]
while len(q) > 0:
    dir, x, y = q.popleft()
    for c in prev[dir][y][x]:
        q.append(c)

    if not seen[y][x]:
        ans += 1
        seen[y][x] = True

ans += 1  # for the start

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
