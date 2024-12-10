from sys import stdin
from timeit import default_timer
from collections import deque

nums = []
heads = []
for i, line in enumerate(stdin):
    nums.append([])
    for j, c in enumerate(line.strip()):
        nums[i].append(int(c))
        if c == "0":
            heads.append((i, j))

m = len(nums)
n = len(nums[0])

# part one
start_time = default_timer()
ans = 0
for hy, hx in heads:
    c_sum = 0
    q = deque([(hy, hx)])
    seen = set([(hy, hx)])

    while len(q) > 0:
        cy, cx = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                0 <= cy + dy < m
                and 0 <= cx + dx < n
                and nums[cy + dy][cx + dx] == nums[cy][cx] + 1
                and (cy + dy, cx + dx) not in seen
            ):
                seen.add((cy + dy, cx + dx))
                if nums[cy + dy][cx + dx] == 9:
                    c_sum += 1
                else:
                    q.append((cy + dy, cx + dx))
    ans += c_sum

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
for hy, hx in heads:
    c_sum = 0
    q = deque([(hy, hx)])
    # seen = set([(hy, hx)])

    while len(q) > 0:
        cy, cx = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                0 <= cy + dy < m
                and 0 <= cx + dx < n
                and nums[cy + dy][cx + dx] == nums[cy][cx] + 1
                # and (cy + dy, cx + dx) not in seen
            ):
                # seen.add((cy + dy, cx + dx))
                if nums[cy + dy][cx + dx] == 9:
                    c_sum += 1
                else:
                    q.append((cy + dy, cx + dx))
    ans += c_sum


end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
