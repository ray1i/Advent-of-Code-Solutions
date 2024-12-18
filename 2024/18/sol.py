from sys import stdin
from timeit import default_timer
from collections import deque

nums = []
for line in stdin:
    nums.append(tuple([int(c) for c in line.strip().split(",")]))

n = max(t[1] for t in nums) + 1

start_time = default_timer()
ex, ey = n - 1, n - 1
grid = [[False] * n for _ in range(n)]
# bytes = 12
bytes = 1024
for i in range(bytes):
    bx, by = nums[i]
    grid[by][bx] = True

# part one
# bfs
ans = 0
q = deque([(0, 0, 0)])  # d, x, y
seen = [[False] * n for _ in range(n)]
seen[0][0] = True
while len(q) > 0:
    d, x, y = q.popleft()
    if (x, y) == (ex, ey):
        ans = d
        break
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and not seen[ny][nx] and not grid[ny][nx]:
            q.append((d + 1, nx, ny))
            seen[ny][nx] = True

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
byte_idx = [[len(nums) + 1] * n for _ in range(n)]
for i, (bx, by) in enumerate(nums):
    byte_idx[by][bx] = i + 1

start_time = default_timer()
ans = 0
q = deque([(0, 0, [])])  # x, y, path
seen = [[False] * n for _ in range(n)]
seen[0][0] = True
while len(q) > 0:
    x, y, path = q.popleft()
    if (x, y) == (ex, ey):
        min_bytes = min([byte_idx[by][bx] for bx, by in path])
        for bx, by in nums[bytes : min_bytes + 1]:
            grid[by][bx] = True
        bytes = min_bytes

        q = deque([(0, 0, [])])
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True
        continue
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and not seen[ny][nx] and not grid[ny][nx]:
            q.append((nx, ny, path + [(x, y)]))
            seen[ny][nx] = True
ans = ",".join([str(num) for num in nums[bytes - 1]])
end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
