from sys import stdin
from timeit import default_timer
from collections import defaultdict

list1 = []
list2 = []
for line in stdin:
    nums = [int(n.strip()) for n in line.strip().split()]
    list1.append(nums[0])
    list2.append(nums[1])

# part one
start_time = default_timer()
sum = 0
for n, m in zip(sorted(list1), sorted(list2)):
    sum += abs(n - m)

end_time = default_timer()
print(f"part 1: {sum} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
seen = defaultdict(int)

for n in list2:
    seen[n] += 1

sum = 0
for n in list1:
    sum += n * seen[n]

end_time = default_timer()
print(f"part 2: {sum} (took {(end_time - start_time) * 1000} ms)")
