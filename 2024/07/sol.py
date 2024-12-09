from sys import stdin
from timeit import default_timer
from collections import deque
from math import log10

vals = []
operands = []
for line in stdin:
    temp = line.split(":")
    vals.append(int(temp[0]))
    operands.append([int(n) for n in temp[1].strip().split()])

# part one
start_time = default_timer()
ans = 0
for i in range(len(vals)):
    for b in range(2 ** (len(operands[i]) - 1)):
        s = operands[i][0]
        for d in range(1, len(operands[i])):
            if b & (1 << (d - 1)) > 0:
                s *= operands[i][d]
            else:
                s += operands[i][d]
        if s == vals[i]:
            ans += s
            break

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
for i in range(len(vals)):
    q = deque([(operands[i][0], 1)])
    while len(q) > 0:
        c = q.popleft()
        if c[1] >= len(operands[i]):
            if c[0] == vals[i]:
                ans += c[0]
                break
            else:
                continue
        q.append((c[0] + operands[i][c[1]], c[1] + 1))
        q.append((c[0] * operands[i][c[1]], c[1] + 1))
        q.append(
            (
                c[0] * (10 ** (int(log10(operands[i][c[1]])) + 1)) + operands[i][c[1]],
                c[1] + 1,
            )
        )

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
