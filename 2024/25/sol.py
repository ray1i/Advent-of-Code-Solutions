from sys import stdin
from timeit import default_timer

locks = []
keys = []
curr = [-1, -1, -1, -1, -1]
prev = ""
for line in stdin:
    if line.strip() == "":
        if prev[0] == ".":
            keys.append(tuple(curr))
        else:
            locks.append(tuple(curr))
        curr = [-1, -1, -1, -1, -1]
        continue

    for i, c in enumerate(line.strip()):
        if c == "#":
            curr[i] += 1

    prev = line

if prev[0] == ".":
    keys.append(curr)
else:
    locks.append(curr)

# part one
start_time = default_timer()
ans = 0

for lock in locks:
    for key in keys:
        for l, k in zip(lock, key):
            if l + k > 5:
                break
        else:
            ans += 1

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
