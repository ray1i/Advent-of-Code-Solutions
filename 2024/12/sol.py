from sys import stdin
from timeit import default_timer
from collections import deque

nums = []
for line in stdin:
    nums.append([c for c in line.strip()])

m = len(nums)
n = len(nums[0])

# part one
start_time = default_timer()
ans = 0
seen = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if seen[i][j]:
            continue

        perimeter = 0
        area = 0
        q = deque([(i, j)])
        mini_seen = set([(i, j)])
        while len(q) > 0:
            ci, cj = q.popleft()
            area += 1
            seen[ci][cj] = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    not (0 <= ci + di < m)
                    or not (0 <= cj + dj < n)
                    or nums[ci + di][cj + dj] != nums[i][j]
                ):
                    perimeter += 1
                elif (ci + di, cj + dj) not in mini_seen:
                    q.append((ci + di, cj + dj))
                    mini_seen.add((ci + di, cj + dj))

        ans += area * perimeter

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()


def is_same_crop(y, x, type):
    return 0 <= y < m and 0 <= x < n and nums[y][x] == type


# for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
prev_rotation = {
    (-1, 0): (-1, 1),
    (0, -1): (-1, -1),
    (1, 0): (1, -1),
    (0, 1): (1, 1),
}


ans = 0
seen = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if seen[i][j]:
            continue

        area = 0
        corners = 0
        q = deque([(i, j)])
        mini_seen = set([(i, j)])
        while len(q) > 0:
            ci, cj = q.popleft()
            area += 1
            seen[ci][cj] = True
            prev_was_fence = not is_same_crop(ci, cj + 1, nums[i][j])
            corner_count = 0
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if not is_same_crop(ci + di, cj + dj, nums[i][j]):
                    if prev_was_fence:
                        corner_count += 1
                    prev_was_fence = True
                else:
                    if (ci + di, cj + dj) not in mini_seen:
                        q.append((ci + di, cj + dj))
                        mini_seen.add((ci + di, cj + dj))
                    if not prev_was_fence and not is_same_crop(
                        ci + prev_rotation[(di, dj)][0],
                        cj + prev_rotation[(di, dj)][1],
                        nums[i][j],
                    ):
                        corner_count += 1

                    prev_was_fence = False

            corners += corner_count

        ans += corners * area


end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
