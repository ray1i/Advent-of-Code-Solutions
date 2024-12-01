from sys import stdin
from collections import defaultdict

list1 = []
list2 = []
for line in stdin:
    nums = [int(n.strip()) for n in line.strip().split()]
    list1.append(nums[0])
    list2.append(nums[1])

# part one
sum = 0
for n, m in zip(sorted(list1), sorted(list2)):
    sum += abs(n - m)

print("part 1:", sum)

# part two
seen = defaultdict(int)

for n in list2:
    seen[n] += 1

sum = 0
for n in list1:
    sum += n * seen[n]

print("part 2:", sum)
