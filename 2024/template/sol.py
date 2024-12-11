from sys import stdin
from timeit import default_timer

nums = []
for line in stdin:
    nums = [int(c) for c in line.strip()]

# part one
start_time = default_timer()
ans = 0

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
