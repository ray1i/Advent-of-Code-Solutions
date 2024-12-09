from sys import stdin
from collections import defaultdict
import heapq

nums = []
for line in stdin:
    nums = [int(c) for c in line.strip()]

original = []
blank = False
curr_num = 0
free = defaultdict(list)
for n in nums:
    if blank:
        heapq.heappush(free[n], len(original))
        original.extend([""] * n)
    else:
        original.extend([curr_num] * n)
        curr_num += 1
    blank = not blank

# part one
ans = 0
curr = original.copy()
end_i = len(curr) - 1
for i, n in enumerate(curr):
    if n == "":
        while curr[end_i] == "":
            end_i -= 1

        if i > end_i:
            break

        curr[i], curr[end_i] = curr[end_i], curr[i]
    ans += i * curr[i]

print("part 1:", ans)

# part two
ans = 0
curr = original.copy()
n = 0
i = len(curr) - 1
while i >= 0:
    n = 1
    while curr[i] == "":
        i -= 1
    f = curr[i]
    while i > 0 and curr[i - 1] == f:
        n += 1
        i -= 1

    cn = -1
    c = i
    for ci in range(n, 10):
        if len(free[ci]) > 0 and free[ci][0] < c:
            cn = ci
            c = free[ci][0]

    if cn > -1 and c < i:
        for j in range(n):
            curr[c + j], curr[i + j] = curr[i + j], curr[c + j]
        heapq.heappush(free[cn - n], c + n)
        heapq.heappop(free[cn])

    i -= 1

for i, n in enumerate(curr):
    ans += i * n if n != "" else 0

print("part 2:", ans)
