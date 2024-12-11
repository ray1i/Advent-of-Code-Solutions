from sys import stdin
from timeit import default_timer
from collections import defaultdict
from math import log10, floor

nums = []
for i, line in enumerate(stdin):
    nums = [int(n) for n in line.strip().split(" ")]

# part one
start_time = default_timer()
ans = 0

curr_nums = nums.copy()
for i in range(25):
    new = []
    for n in curr_nums:
        if n == 0:
            new.append(1)
        elif len(str(n)) % 2 == 0:
            new.append(int(str(n)[: len(str(n)) // 2]))
            new.append(int(str(n)[len(str(n)) // 2 :]))
        else:
            new.append(n * 2024)
    curr_nums = new
ans = len(curr_nums)

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
seen = [defaultdict(list) for _ in range(75)]


def traverse(n, blinks):
    if blinks >= 75:
        return 1
    elif n in seen[blinks]:
        pass
    elif n == 0:
        a = traverse(1, blinks + 1)
        seen[blinks][n] = a
    elif (floor(log10(n)) + 1) % 2 == 0:
        half = 10 ** ((floor(log10(n)) + 1) // 2)
        a = traverse(n // half, blinks + 1)
        b = traverse(n % half, blinks + 1)
        seen[blinks][n] = a + b
    else:
        a = traverse(n * 2024, blinks + 1)
        seen[blinks][n] = a
    return seen[blinks][n]


for n in nums:
    ans += traverse(n, 0)

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")
