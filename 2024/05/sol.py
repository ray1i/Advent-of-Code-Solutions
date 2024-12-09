from sys import stdin
from timeit import default_timer
from collections import defaultdict

getting_rules = True
rules = defaultdict(set)
updates = []
for line in stdin:
    if line.strip() == "":
        getting_rules = False
    elif getting_rules:
        t = [int(n) for n in line.strip().split("|")]
        # rules[t[0]].add(t[1])
        rules[t[1]].add(t[0])
    else:
        updates.append([int(n) for n in line.strip().split(",")])

# part one
start_time = default_timer()
ans = 0
for u in updates:
    good = True
    for i in range(len(u)):
        if any([n in rules[u[i]] for n in u[i + 1 :]]):
            good = False
    if good:
        ans += u[len(u) // 2]

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
for u in updates:
    good = True
    new = u.copy()
    i, j = 0, 0
    while i < len(u):
        for j in range(i, len(new)):
            if new[j] in rules[new[i]]:
                good = False
                new[i], new[j] = new[j], new[i]
                break
        else:
            i += 1

    if not good:
        ans += new[len(new) // 2]

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
