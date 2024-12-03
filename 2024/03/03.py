from sys import stdin
import re

lines = []
for line in stdin:
    lines.append(line)

# part one
ans = 0
for l in lines:
    m = re.findall("mul\((\d+),(\d+)\)", l)
    for t in m:
        ans += int(t[0]) * int(t[1])

print("part 1:", ans)

# part two
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

print("part 2:", ans)
