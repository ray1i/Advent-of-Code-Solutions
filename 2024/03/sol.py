from sys import stdin
from timeit import default_timer
import re

lines = []
for line in stdin:
    lines.append(line)

# part one
start_time = default_timer()
ans = 0
for l in lines:
    m = re.findall("mul\((\d+),(\d+)\)", l)
    for t in m:
        ans += int(t[0]) * int(t[1])

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
do = True
for l in lines:
    m = re.findall("(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", l)
    for t in m:
        if t[3]:
            do = True
        elif t[4]:
            do = False
        elif do and t[0]:
            ans += int(t[2]) * int(t[1])

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
