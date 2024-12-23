from sys import stdin
from timeit import default_timer
from collections import defaultdict

adj = defaultdict(set)
for line in stdin:
    a, b = [c for c in line.strip().split("-")]
    adj[a].add(b)
    adj[b].add(a)

# part one
start_time = default_timer()
ans = 0
seen = set()
for a in adj.keys():
    if a[0] == "t":
        for b in adj[a]:
            for c in adj[a].intersection(adj[b]):
                group = "".join(sorted([a, b, c]))
                if group not in seen:
                    ans += 1
                    seen.add(group)

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
curr = set()


# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def BronKerbosch1(r, p, x):
    if len(p) <= 0 and len(x) <= 0:
        return r
    ans = set()
    for v in p.copy():
        guh = BronKerbosch1(r | {v}, p.intersection(adj[v]), x.intersection(adj[v]))
        if len(guh) > len(ans):
            ans = guh
        p.discard(v)
        x.add(v)
    return ans


R, P, X = set(), set(adj.keys()), set()
ans = ",".join(sorted(list(BronKerbosch1(R, P, X))))

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
