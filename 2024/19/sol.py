from sys import stdin
from timeit import default_timer
from collections import defaultdict, deque
from functools import reduce, lru_cache

available = [s.strip() for s in next(stdin).strip().split(",")]
desired = []
next(stdin)
for line in stdin:
    desired.append(line.strip())

# part one
Trie = lambda: defaultdict(Trie)
trie = Trie()
for s in available:
    curr_node = trie
    for c in s:
        curr_node = curr_node[c]
    curr_node["$"] = True

start_time = default_timer()
ans = 0
for d in desired:
    # print(f"{d}: ", end="")
    q = deque([(0, "", [])]) # index, node, path
    seen = set([(0, "")])
    while len(q) > 0:
        i, curr_s, path = q.popleft()
        node = reduce(lambda t, k: t[k], curr_s, trie)
        if i >= len(d):
            if "$" in node:
                ans += 1
                # print(" + ".join(path + [curr_s]), end="")
                break
            continue

        if "$" in node and (i, "") not in seen:
            q.append((i, "", path + [curr_s]))
            seen.add((i, ""))
        if d[i] in node and (i + 1, curr_s + d[i]) not in seen:
            q.append((i + 1, curr_s + d[i], path))
            seen.add((i + 1, curr_s + d[i]))
    # print()

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()

set_available = set(available)
@lru_cache(None)
def ways(prefix: str, s: str):
    if len(prefix) == len(s):
        return 1
    
    sols = 0
    for a in available:
        if len(prefix) + len(a) <= len(s) and prefix + a == s[:(len(prefix) + len(a))]:
            sols += ways(prefix + a, s)

    return sols


ans = reduce(lambda s, d: s + ways("", d), desired, 0)

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
